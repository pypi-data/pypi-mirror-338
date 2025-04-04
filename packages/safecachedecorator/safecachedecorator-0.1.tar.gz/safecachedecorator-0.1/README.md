# SafeCacheDecorator 🚀

[![PyPI Version](https://img.shields.io/pypi/v/safecachedecorator?color=blue)](https://pypi.org/project/safecachedecorator/)
[![Python Versions](https://img.shields.io/pypi/pyversions/safecachedecorator)](https://pypi.org/project/safecachedecorator/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Thread-safe Python caching decorator with TTL support**  
*Final Project for Harvard's [CS50P](https://cs50.harvard.edu/python/)*  

---

## Features ✨
- 🧵 **Thread-safe** using `RLock`  
- ⏱️ **TTL (Time-to-Live)** support for auto-expiring cache  
- ♻️ **LRU eviction** when `maxsize` is reached  
- 🛡️ **Hashable args/kwargs** (supports lists/dicts as keys)  
- � **Lightweight** (~100 LOC, no external dependencies)  

---

## Installation 📦
```bash
pip install safecachedecorator
```

---

## Usage 🛠️
### Basic Caching
```python
from safecache import SafeCache

@SafeCache(maxsize=100, ttl=60)  # Cache expires after 60 seconds
def expensive_operation(x):
    print("Computing...")
    return x ** 2

print(expensive_operation(4))  # Computes (not cached)
print(expensive_operation(4))  # Uses cache
```

### Thread-Safe Demo
```python
import threading

@SafeCache()
def thread_task():
    print("Thread-safe computation")

threads = [threading.Thread(target=thread_task) for _ in range(10)]
[t.start() for t in threads]
[t.join() for t in threads]
```

---

## Documentation 📖
### Parameters
| Argument  | Description                          |
|-----------|--------------------------------------|
| `maxsize` | Maximum cached items (default=10000) |
| `ttl`     | Cache expiry in seconds (optional)   |

### Methods
```python
cache.clear()  # Wipe all cached data
```

---

## CS50P Submission Details
- **Demo Video**: [YouTube Link](#) *(Required - show installation + usage)*  
- **Key Innovation**: Adds thread-safety and TTL to Python's native caching  

---

## Contributing 🤝
Pull requests welcome!  
1. Fork the repo  
2. Add tests in `tests/`  
3. Submit a PR  

---

## License 📜
MIT © [Pappa1945-tech](https://github.com/Pappa1945-tech)