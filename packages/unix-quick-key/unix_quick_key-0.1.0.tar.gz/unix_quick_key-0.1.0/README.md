# Quick Key

Provides an easy way to get keypresses on linux.

```python
from quick_key import Key, get_key, readmode

with readmode():
    curr_key = None
    while curr_key != Key.q:
        curr_key = get_key()
        # do something with keypresses...
```