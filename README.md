# clocky

```python
#!/usr/bin/python

import time
from clocky import clocky

@clocky
def test():
    for x in "hello world!":
        print x
        time.sleep(0.25)
        
test()
```
