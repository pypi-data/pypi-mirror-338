import pickle
import os
import functools
import threading
import warnings
import fcntl
import time

class PersistentBox:
    """
    A wrapper class that automatically loads/saves the wrapped object
    to/from disk before and after every operation, with process-safe file locking.
    """
    
    def __init__(self, filepath=None, default_val=None, overwrite_val=None, cls = None, lock_timeout=1_000_000, *args, **kwargs):
        """
        Initialize an on-disk persistent object.
        
        Args:
            filepath: Path to save/load the object (required)
            default_val: Value to use if file doesn't exist and overwrite_val is None
            overwrite_val: Value to write to file, overriding any existing content
            cls: Class to instantiate if file doesn't exist and both default_val and overwrite_val are None
            lock_timeout: Timeout in seconds for acquiring locks (default 1_000_000)
            *args, **kwargs: Arguments to pass to cls constructor
        """
        if filepath is None:
            raise ValueError("Must provide a filepath for persistence")
        elif overwrite_val is not None and default_val is not None:
            raise ValueError("Cannot have a default and overwrite value")

        self._filepath = filepath
        self._initialized = False
        self._lock = threading.RLock()  # For thread safety within a process
        self._lock_timeout = lock_timeout
        
        # If overwrite_val is provided, use it regardless of whether file exists
        if overwrite_val is not None:
            self._obj = overwrite_val
            # Create directory structure if needed
            directory = os.path.dirname(self._filepath)
            if directory and not os.path.exists(directory):
                os.makedirs(directory)
            # Write the overwrite value to file right away
            self._save()
        # Otherwise, follow normal load/default logic
        elif os.path.exists(filepath):
            try:
                self._load()
            except Exception as e:
                warnings.warn(f"Error loading from disk: {e}. Creating new object.")
                if default_val is not None:
                    self._obj = default_val
                elif cls is not None:
                    self._obj = cls(*args, **kwargs)
                else:
                    raise ValueError("Could not load from disk and no fallback provided")
                self._save()
        else:
            # Create new object and save it
            if default_val is not None:
                self._obj = default_val
            elif cls is not None:
                self._obj = cls(*args, **kwargs)
            else:
                raise ValueError("No existing file and no object or class provided")
            self._save()
        
        self._initialized = True

    def _acquire_file_lock(self, file_handle, exclusive=True):
        """
        Acquire a lock on the file.
        
        Args:
            file_handle: Open file handle to lock
            exclusive: If True, acquire an exclusive (write) lock, otherwise a shared (read) lock
            
        Returns:
            True if lock was acquired, False otherwise
        """
        lock_type = fcntl.LOCK_EX if exclusive else fcntl.LOCK_SH
        lock_type |= fcntl.LOCK_NB  # Non-blocking mode
        
        start_time = time.time()
        while True:
            try:
                fcntl.flock(file_handle.fileno(), lock_type)
                return True
            except IOError:
                # Could not acquire lock, check if we've timed out
                if time.time() - start_time > self._lock_timeout:
                    warnings.warn(f"Could not acquire {'exclusive' if exclusive else 'shared'} "
                                 f"lock on {self._filepath} within {self._lock_timeout} seconds")
                    return False
                # Wait a bit before trying again
                time.sleep(0.1)
    
    def _release_file_lock(self, file_handle):
        """Release the lock on the file."""
        try:
            fcntl.flock(file_handle.fileno(), fcntl.LOCK_UN)
        except Exception as e:
            warnings.warn(f"Error releasing file lock: {e}")
    
    def _load(self):
        """Load the object from disk with file locking."""
        with self._lock:  # Thread safety
            # Ensure directory exists
            directory = os.path.dirname(self._filepath)
            if directory and not os.path.exists(directory):
                os.makedirs(directory)
                
            # If file doesn't exist yet, create an empty one
            if not os.path.exists(self._filepath):
                with open(self._filepath, 'wb') as f:
                    pickle.dump(None, f)
            
            # Open the file and acquire a shared (read) lock
            with open(self._filepath, 'rb') as f:
                if self._acquire_file_lock(f, exclusive=False):
                    try:
                        self._obj = pickle.load(f)
                    finally:
                        self._release_file_lock(f)
                else:
                    raise IOError(f"Could not acquire read lock on {self._filepath}")
    
    def _save(self):
        """Save the object to disk with file locking."""
        with self._lock:  # Thread safety
            # Ensure directory exists
            directory = os.path.dirname(self._filepath)
            if directory and not os.path.exists(directory):
                os.makedirs(directory)
            
            # Create a UNIQUE temporary file using process ID to avoid collisions
            pid = os.getpid()
            temp_path = f"{self._filepath}.{pid}.tmp"
            
            # Write to the temporary file
            with open(temp_path, 'wb') as f:
                pickle.dump(self._obj, f)
            
            # Now open the real file with an exclusive lock to replace its contents
            with open(self._filepath, 'r+b' if os.path.exists(self._filepath) else 'wb') as f:
                if self._acquire_file_lock(f, exclusive=True):
                    try:
                        # Read the temp file content
                        with open(temp_path, 'rb') as temp_f:
                            content = temp_f.read()
                        
                        # Truncate the target file and write new content
                        f.seek(0)
                        f.truncate()
                        f.write(content)
                        f.flush()
                        os.fsync(f.fileno())  # Ensure data is written to disk
                    finally:
                        self._release_file_lock(f)
                        # Clean up temp file
                        try:
                            os.unlink(temp_path)
                        except OSError:
                            pass
                else:
                    raise IOError(f"Could not acquire write lock on {self._filepath}")
    
    def __iadd__(self, other):
        """
        Support for += operator.
        
        Args:
            other: Value to add to the wrapped object
            
        Returns:
            self: Returns self to support in-place operations
            
        Raises:
            TypeError: If the underlying object doesn't support += operator
        """
        self._load()
        try:
            self._obj += other
            self._save()
        except Exception as e:
            # Propagate the error with context about the underlying type
            raise type(e)(f"Underlying object of type '{type(self._obj).__name__}' doesn't support '+=' operation: {str(e)}")
        return self

    def __isub__(self, other):
        """
        Support for -= operator.
        
        Args:
            other: Value to subtract from the wrapped object
            
        Returns:
            self: Returns self to support in-place operations
            
        Raises:
            TypeError: If the underlying object doesn't support -= operator
        """
        self._load()
        try:
            self._obj -= other
            self._save()
        except Exception as e:
            # Propagate the error with context about the underlying type
            raise type(e)(f"Underlying object of type '{type(self._obj).__name__}' doesn't support '-=' operation: {str(e)}")
        return self

    def __getattribute__(self, name):
        """Intercept all attribute access."""
        # Handle our own attributes directly
        if name.startswith('_'):
            return super().__getattribute__(name)
        
        # Reload from disk before operation
        try:
            with super().__getattribute__('_lock'):
                super().__getattribute__('_load')()
        except Exception as e:
            warnings.warn(f"Could not reload object from disk: {e}")
        
        # Get the attribute from the wrapped object
        try:
            obj = super().__getattribute__('_obj')
            attr = getattr(obj, name)
            
            # If it's a method, wrap it to save after execution
            if callable(attr) and not isinstance(attr, type):
                # Store a reference to self for the inner function to use
                self_ref = self
                
                @functools.wraps(attr)
                def wrapped(*args, **kwargs):
                    result = attr(*args, **kwargs)
                    try:
                        # Use self_ref instead of super()
                        self_ref._save()
                    except Exception as e:
                        warnings.warn(f"Could not save object to disk: {e}")
                    return result
                return wrapped
            
            return attr
        except AttributeError:
            obj = super().__getattribute__('_obj')
            raise AttributeError(f"'{type(obj).__name__}' object has no attribute '{name}'")
    
    def __setattr__(self, name, value):
        """Intercept all attribute assignment."""
        if name.startswith('_'):
            # Handle our private attributes
            super().__setattr__(name, value)
        elif hasattr(self, '_initialized') and self._initialized:
            # Reload first to ensure we're working with fresh data
            try:
                with self._lock:
                    self._load()
            except Exception as e:
                warnings.warn(f"Could not reload object from disk: {e}")
            
            # Forward to wrapped object and save
            setattr(self._obj, name, value)
            try:
                with self._lock:
                    self._save()
            except Exception as e:
                warnings.warn(f"Could not save object to disk: {e}")
        else:
            # During initialization
            super().__setattr__(name, value)
    
    # Container methods
    def __getitem__(self, key):
        self._load()
        item = self._obj[key]
        self._save()
        return item
    
    def __setitem__(self, key, value):
        self._load()
        self._obj[key] = value
        self._save()

    def __delitem__(self, key):
        self._load()
        try:
            del self._obj[key]
            self._save()
        except Exception as e:
            raise type(e)(f"Underlying object of type '{type(self._obj).__name__}' doesn't support item deletion: {str(e)}")

    def __len__(self):
        self._load()
        return len(self._obj)
    
    # String representation
    def __str__(self):
        return str(self._obj)
    
    def __repr__(self):
        return f"PersistentBox({repr(self._obj)}, filepath='{self._filepath}')"
