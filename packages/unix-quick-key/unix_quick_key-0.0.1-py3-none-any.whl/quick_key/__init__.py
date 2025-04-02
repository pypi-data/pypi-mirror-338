"""
Provides quick and dirty keypress reading for scripts on unix.

```python
from quick_key import Key, get_key, readmode

with readmode():
    curr_key = None
    while curr_key != Key.q:
        curr_key = get_key()
        # do something with keypresses...
```
"""

from __future__ import annotations

__all__ = ['Key', 'get_key', 'readmode']

from quick_key.key import Key, get_key, readmode
