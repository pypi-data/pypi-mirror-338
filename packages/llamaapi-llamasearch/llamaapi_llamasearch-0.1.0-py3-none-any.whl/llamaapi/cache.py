"""
Caching implementation for API responses.
"""
from abc import ABC, abstractmethod
import json
import os
import pickle
import threading
import time
from typing import Any, Dict, Optional, Union
import logging

logger = logging.getLogger(__name__)

class BaseCache(ABC):
    """
    Base class for all cache implementations.
    """
    @abstractmethod
    def get(self, key: str) -> Optional[Any]:
        """
        Get a value from the cache.
        
        Args:
            key: The cache key.
            
        Returns:
            The cached value or None if not found.
        """
        pass
    
    @abstractmethod
    def set(self, key: str, value: Any, ttl: Optional[int] = None) -> None:
        """
        Set a value in the cache.
        
        Args:
            key: The cache key.
            value: The value to cache.
            ttl: Time-to-live in seconds.
        """
        pass
    
    @abstractmethod
    def delete(self, key: str) -> None:
        """
        Delete a value from the cache.
        
        Args:
            key: The cache key.
        """
        pass
    
    @abstractmethod
    def clear(self) -> None:
        """
        Clear all values from the cache.
        """
        pass


class NoCache(BaseCache):
    """
    A cache implementation that doesn't actually cache anything.
    """
    def get(self, key: str) -> Optional[Any]:
        """Always returns None."""
        return None
    
    def set(self, key: str, value: Any, ttl: Optional[int] = None) -> None:
        """Does nothing."""
        pass
    
    def delete(self, key: str) -> None:
        """Does nothing."""
        pass
    
    def clear(self) -> None:
        """Does nothing."""
        pass


class MemoryCache(BaseCache):
    """
    In-memory cache implementation.
    """
    def __init__(self, max_size: int = 1000):
        """
        Initialize the in-memory cache.
        
        Args:
            max_size: Maximum number of items to store in the cache.
        """
        self.cache: Dict[str, Dict[str, Any]] = {}
        self.max_size = max_size
        self.lock = threading.RLock()
    
    def get(self, key: str) -> Optional[Any]:
        """
        Get a value from the cache.
        
        Args:
            key: The cache key.
            
        Returns:
            The cached value or None if not found or expired.
        """
        with self.lock:
            if key not in self.cache:
                return None
            
            item = self.cache[key]
            expires_at = item.get("expires_at")
            
            # Check if the item has expired
            if expires_at and time.time() > expires_at:
                del self.cache[key]
                return None
            
            return item["value"]
    
    def set(self, key: str, value: Any, ttl: Optional[int] = None) -> None:
        """
        Set a value in the cache.
        
        Args:
            key: The cache key.
            value: The value to cache.
            ttl: Time-to-live in seconds.
        """
        with self.lock:
            # Evict oldest items if cache is full
            if len(self.cache) >= self.max_size and key not in self.cache:
                self._evict_oldest()
            
            # Calculate expiration time if TTL is provided
            expires_at = time.time() + ttl if ttl else None
            
            # Store the value with expiration time
            self.cache[key] = {
                "value": value,
                "expires_at": expires_at,
                "created_at": time.time()
            }
    
    def delete(self, key: str) -> None:
        """
        Delete a value from the cache.
        
        Args:
            key: The cache key.
        """
        with self.lock:
            if key in self.cache:
                del self.cache[key]
    
    def clear(self) -> None:
        """
        Clear all values from the cache.
        """
        with self.lock:
            self.cache.clear()
    
    def _evict_oldest(self) -> None:
        """
        Evict the oldest item from the cache.
        """
        if not self.cache:
            return
        
        # Find the oldest item based on creation time
        oldest_key = min(self.cache.keys(), key=lambda k: self.cache[k]["created_at"])
        del self.cache[oldest_key]


class FileCache(BaseCache):
    """
    File-based cache implementation.
    """
    def __init__(self, cache_dir: str = ".cache", max_size: int = 1000):
        """
        Initialize the file cache.
        
        Args:
            cache_dir: Directory to store cache files.
            max_size: Maximum number of files to store.
        """
        self.cache_dir = os.path.expanduser(cache_dir)
        self.max_size = max_size
        self.lock = threading.RLock()
        
        # Create cache directory if it doesn't exist
        os.makedirs(self.cache_dir, exist_ok=True)
        
        # Create metadata file to track cache entries
        self.metadata_file = os.path.join(self.cache_dir, "metadata.json")
        self.metadata: Dict[str, Dict[str, Any]] = self._load_metadata()
    
    def _load_metadata(self) -> Dict[str, Dict[str, Any]]:
        """
        Load cache metadata from the metadata file.
        
        Returns:
            The metadata dictionary.
        """
        if not os.path.exists(self.metadata_file):
            return {}
        
        try:
            with open(self.metadata_file, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            logger.warning(f"Failed to load cache metadata: {str(e)}")
            return {}
    
    def _save_metadata(self) -> None:
        """
        Save cache metadata to the metadata file.
        """
        try:
            with open(self.metadata_file, "w") as f:
                json.dump(self.metadata, f)
        except IOError as e:
            logger.warning(f"Failed to save cache metadata: {str(e)}")
    
    def _get_cache_path(self, key: str) -> str:
        """
        Get the file path for a cache key.
        
        Args:
            key: The cache key.
            
        Returns:
            The file path.
        """
        # Convert the key to a valid filename
        filename = key.replace("/", "_").replace(":", "_")
        return os.path.join(self.cache_dir, filename)
    
    def get(self, key: str) -> Optional[Any]:
        """
        Get a value from the cache.
        
        Args:
            key: The cache key.
            
        Returns:
            The cached value or None if not found or expired.
        """
        with self.lock:
            # Check if the key exists in metadata
            if key not in self.metadata:
                return None
            
            # Check if the item has expired
            item_meta = self.metadata[key]
            expires_at = item_meta.get("expires_at")
            if expires_at and time.time() > expires_at:
                self.delete(key)
                return None
            
            # Get the file path
            cache_path = self._get_cache_path(key)
            if not os.path.exists(cache_path):
                # Metadata is out of sync, clean it up
                del self.metadata[key]
                self._save_metadata()
                return None
            
            # Load the cached value
            try:
                with open(cache_path, "rb") as f:
                    return pickle.load(f)
            except (pickle.PickleError, IOError) as e:
                logger.warning(f"Failed to load cached value: {str(e)}")
                return None
    
    def set(self, key: str, value: Any, ttl: Optional[int] = None) -> None:
        """
        Set a value in the cache.
        
        Args:
            key: The cache key.
            value: The value to cache.
            ttl: Time-to-live in seconds.
        """
        with self.lock:
            # Check if we need to evict items
            if len(self.metadata) >= self.max_size and key not in self.metadata:
                self._evict_oldest()
            
            # Calculate expiration time if TTL is provided
            expires_at = time.time() + ttl if ttl else None
            
            # Update metadata
            self.metadata[key] = {
                "expires_at": expires_at,
                "created_at": time.time()
            }
            
            # Save the value to a file
            cache_path = self._get_cache_path(key)
            try:
                with open(cache_path, "wb") as f:
                    pickle.dump(value, f)
                
                # Save updated metadata
                self._save_metadata()
            except IOError as e:
                logger.warning(f"Failed to save cached value: {str(e)}")
    
    def delete(self, key: str) -> None:
        """
        Delete a value from the cache.
        
        Args:
            key: The cache key.
        """
        with self.lock:
            if key not in self.metadata:
                return
            
            # Delete the cache file
            cache_path = self._get_cache_path(key)
            if os.path.exists(cache_path):
                try:
                    os.remove(cache_path)
                except IOError as e:
                    logger.warning(f"Failed to delete cache file: {str(e)}")
            
            # Update metadata
            del self.metadata[key]
            self._save_metadata()
    
    def clear(self) -> None:
        """
        Clear all values from the cache.
        """
        with self.lock:
            # Delete all cache files
            for key in list(self.metadata.keys()):
                cache_path = self._get_cache_path(key)
                if os.path.exists(cache_path):
                    try:
                        os.remove(cache_path)
                    except IOError as e:
                        logger.warning(f"Failed to delete cache file: {str(e)}")
            
            # Clear metadata
            self.metadata.clear()
            self._save_metadata()
    
    def _evict_oldest(self) -> None:
        """
        Evict the oldest item from the cache.
        """
        if not self.metadata:
            return
        
        # Find the oldest item based on creation time
        oldest_key = min(self.metadata.keys(), key=lambda k: self.metadata[k]["created_at"])
        self.delete(oldest_key)


class RedisCache(BaseCache):
    """
    Redis-based cache implementation.
    Requires redis-py package: pip install redis
    """
    def __init__(
        self,
        host: str = "localhost",
        port: int = 6379,
        db: int = 0,
        password: Optional[str] = None,
        prefix: str = "llamaapi:",
        **kwargs
    ):
        """
        Initialize Redis cache.
        
        Args:
            host: Redis host.
            port: Redis port.
            db: Redis database number.
            password: Redis password.
            prefix: Key prefix for all cache entries.
            **kwargs: Additional arguments to pass to Redis client.
        """
        try:
            import redis
        except ImportError:
            raise ImportError(
                "Redis cache requires the 'redis' package. "
                "Install it with: pip install redis"
            )
        
        self.prefix = prefix
        self.redis = redis.Redis(
            host=host,
            port=port,
            db=db,
            password=password,
            **kwargs
        )
    
    def get(self, key: str) -> Optional[Any]:
        """
        Get a value from the cache.
        
        Args:
            key: The cache key.
            
        Returns:
            The cached value or None if not found.
        """
        prefixed_key = f"{self.prefix}{key}"
        value = self.redis.get(prefixed_key)
        
        if value is None:
            return None
        
        try:
            return pickle.loads(value)
        except pickle.PickleError as e:
            logger.warning(f"Failed to unpickle cached value: {str(e)}")
            return None
    
    def set(self, key: str, value: Any, ttl: Optional[int] = None) -> None:
        """
        Set a value in the cache.
        
        Args:
            key: The cache key.
            value: The value to cache.
            ttl: Time-to-live in seconds.
        """
        prefixed_key = f"{self.prefix}{key}"
        
        try:
            pickled_value = pickle.dumps(value)
            if ttl:
                self.redis.setex(prefixed_key, ttl, pickled_value)
            else:
                self.redis.set(prefixed_key, pickled_value)
        except (pickle.PickleError, Exception) as e:
            logger.warning(f"Failed to cache value: {str(e)}")
    
    def delete(self, key: str) -> None:
        """
        Delete a value from the cache.
        
        Args:
            key: The cache key.
        """
        prefixed_key = f"{self.prefix}{key}"
        self.redis.delete(prefixed_key)
    
    def clear(self) -> None:
        """
        Clear all values from the cache with the same prefix.
        """
        pattern = f"{self.prefix}*"
        cursor = 0
        while True:
            cursor, keys = self.redis.scan(cursor, pattern, 100)
            if keys:
                self.redis.delete(*keys)
            if cursor == 0:
                break 