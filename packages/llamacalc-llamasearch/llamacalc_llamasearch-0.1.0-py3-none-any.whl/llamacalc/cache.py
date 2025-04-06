"""
Caching functionality for LlamaCalc.

This module provides caching mechanisms for storing and retrieving
calculation results to improve performance.
"""

import os
import json
import time
from typing import Dict, List, Optional, Any, Union
from pathlib import Path
import sqlite3
from datetime import datetime, timedelta

# Local imports
# When moved to package structure, will need to update these imports
try:
    # For internal imports within the package
    from .core import RelevanceResult
except ImportError:
    # For development/testing before package structure
    RelevanceResult = Any


class MemoryCache:
    """In-memory cache for RelevanceResult objects."""
    
    def __init__(self, max_size: int = 1000, ttl: int = 3600):
        """
        Initialize the memory cache.
        
        Args:
            max_size: Maximum number of items to store in cache
            ttl: Time-to-live in seconds for cached items
        """
        self.cache: Dict[str, Dict[str, Any]] = {}
        self.max_size = max_size
        self.ttl = ttl
        self.hits = 0
        self.misses = 0
    
    def _make_key(self, question: str, answer: str) -> str:
        """Create a cache key from question and answer."""
        # Simple key generation - could be improved with hashing
        return f"{question[:100]}||{answer[:100]}"
    
    def get(self, question: str, answer: str) -> Optional[RelevanceResult]:
        """
        Retrieve a cached result if available.
        
        Args:
            question: The question text
            answer: The answer text
            
        Returns:
            Cached RelevanceResult or None if not found
        """
        key = self._make_key(question, answer)
        item = self.cache.get(key)
        
        if item is None:
            self.misses += 1
            return None
        
        # Check if item has expired
        now = time.time()
        if now - item["timestamp"] > self.ttl:
            # Remove expired item
            del self.cache[key]
            self.misses += 1
            return None
        
        self.hits += 1
        return RelevanceResult.from_dict(item["data"])
    
    def put(self, result: RelevanceResult) -> None:
        """
        Store a result in the cache.
        
        Args:
            result: The RelevanceResult to cache
        """
        key = self._make_key(result.question, result.answer)
        
        # Evict oldest item if cache is full
        if len(self.cache) >= self.max_size:
            oldest_key = min(self.cache, key=lambda k: self.cache[k]["timestamp"])
            del self.cache[oldest_key]
        
        # Store the item
        self.cache[key] = {
            "timestamp": time.time(),
            "data": result.to_dict()
        }
    
    def clear(self) -> None:
        """Clear all items from the cache."""
        self.cache.clear()
    
    @property
    def size(self) -> int:
        """Get the current number of items in the cache."""
        return len(self.cache)
    
    @property
    def hit_rate(self) -> float:
        """Get the cache hit rate."""
        total = self.hits + self.misses
        return self.hits / total if total > 0 else 0.0
    
    def stats(self) -> Dict[str, Any]:
        """Get cache statistics."""
        return {
            "size": self.size,
            "max_size": self.max_size,
            "hits": self.hits,
            "misses": self.misses,
            "hit_rate": self.hit_rate
        }


class DiskCache:
    """Persistent disk-based cache for RelevanceResult objects using SQLite."""
    
    def __init__(
        self, 
        cache_dir: Optional[str] = None, 
        max_size: int = 10000, 
        ttl: int = 86400 * 7  # 1 week default TTL
    ):
        """
        Initialize the disk cache.
        
        Args:
            cache_dir: Directory to store cache file (default: ~/.llamacalc)
            max_size: Maximum number of entries to store
            ttl: Time-to-live for entries in seconds
        """
        # Set up cache directory
        if cache_dir is None:
            cache_dir = os.path.expanduser("~/.llamacalc")
        
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        
        self.db_path = self.cache_dir / "cache.db"
        self.max_size = max_size
        self.ttl = ttl
        
        # Statistics
        self.hits = 0
        self.misses = 0
        
        # Initialize database
        self._init_db()
    
    def _init_db(self) -> None:
        """Initialize the SQLite database."""
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        # Create cache table if it doesn't exist
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS relevance_cache (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question_hash TEXT,
            answer_hash TEXT, 
            question TEXT,
            answer TEXT,
            result_json TEXT,
            created_at TIMESTAMP,
            UNIQUE(question_hash, answer_hash)
        )
        """)
        
        # Create index for faster lookups
        cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_hashes 
        ON relevance_cache(question_hash, answer_hash)
        """)
        
        conn.commit()
        conn.close()
    
    def _hash_text(self, text: str) -> str:
        """Create a simple hash of the text."""
        import hashlib
        return hashlib.md5(text.encode()).hexdigest()
    
    def _prune_old_entries(self, conn: sqlite3.Connection) -> None:
        """Remove old entries from the cache."""
        cursor = conn.cursor()
        
        # Remove expired entries
        expiry_date = datetime.now() - timedelta(seconds=self.ttl)
        cursor.execute(
            "DELETE FROM relevance_cache WHERE created_at < ?", 
            (expiry_date.isoformat(),)
        )
        
        # If still over max size, remove oldest entries
        cursor.execute("SELECT COUNT(*) FROM relevance_cache")
        count = cursor.fetchone()[0]
        
        if count > self.max_size:
            # Calculate how many to remove
            to_remove = count - self.max_size
            cursor.execute(
                "DELETE FROM relevance_cache WHERE id IN (SELECT id FROM relevance_cache ORDER BY created_at ASC LIMIT ?)",
                (to_remove,)
            )
        
        conn.commit()
    
    def get(self, question: str, answer: str) -> Optional[RelevanceResult]:
        """
        Retrieve a cached result if available.
        
        Args:
            question: The question text
            answer: The answer text
            
        Returns:
            Cached RelevanceResult or None if not found
        """
        q_hash = self._hash_text(question)
        a_hash = self._hash_text(answer)
        
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        cursor.execute(
            "SELECT result_json, created_at FROM relevance_cache WHERE question_hash = ? AND answer_hash = ?",
            (q_hash, a_hash)
        )
        
        row = cursor.fetchone()
        if row is None:
            self.misses += 1
            conn.close()
            return None
        
        result_json, created_at = row
        
        # Check if entry has expired
        created_datetime = datetime.fromisoformat(created_at)
        if (datetime.now() - created_datetime).total_seconds() > self.ttl:
            # Remove expired item
            cursor.execute(
                "DELETE FROM relevance_cache WHERE question_hash = ? AND answer_hash = ?",
                (q_hash, a_hash)
            )
            conn.commit()
            conn.close()
            self.misses += 1
            return None
        
        conn.close()
        self.hits += 1
        
        # Parse the result
        result_dict = json.loads(result_json)
        return RelevanceResult.from_dict(result_dict)
    
    def put(self, result: RelevanceResult) -> None:
        """
        Store a result in the cache.
        
        Args:
            result: The RelevanceResult to cache
        """
        q_hash = self._hash_text(result.question)
        a_hash = self._hash_text(result.answer)
        result_json = json.dumps(result.to_dict())
        
        conn = sqlite3.connect(str(self.db_path))
        
        # First, prune old entries if needed
        self._prune_old_entries(conn)
        
        # Then insert the new entry
        cursor = conn.cursor()
        cursor.execute("""
        INSERT OR REPLACE INTO relevance_cache
        (question_hash, answer_hash, question, answer, result_json, created_at)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (
            q_hash, 
            a_hash, 
            result.question, 
            result.answer, 
            result_json,
            datetime.now().isoformat()
        ))
        
        conn.commit()
        conn.close()
    
    def clear(self) -> None:
        """Clear all items from the cache."""
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        cursor.execute("DELETE FROM relevance_cache")
        conn.commit()
        conn.close()
    
    @property
    def size(self) -> int:
        """Get the current number of items in the cache."""
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM relevance_cache")
        count = cursor.fetchone()[0]
        conn.close()
        return count
    
    @property
    def hit_rate(self) -> float:
        """Get the cache hit rate."""
        total = self.hits + self.misses
        return self.hits / total if total > 0 else 0.0
    
    def stats(self) -> Dict[str, Any]:
        """Get cache statistics."""
        return {
            "size": self.size,
            "max_size": self.max_size,
            "hits": self.hits,
            "misses": self.misses,
            "hit_rate": self.hit_rate,
            "db_path": str(self.db_path)
        } 