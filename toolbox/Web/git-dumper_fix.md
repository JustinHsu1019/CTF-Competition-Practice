# Git-Dumper Debug

## cookie.py 問題

```bash
File "C:\Users\crazy\AppData\Local\Programs\Python\Python311\Lib\site-packages\requests\cookies.py", line 174, in <module>
  class RequestsCookieJar(cookielib.CookieJar, collections.MutableMapping):       
                                                 ^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: module 'collections' has no attribute 'MutableMapping'
```

## cookie.py 解法

### cookie: 原 Code

```python
class RequestsCookieJar(cookielib.CookieJar, collections.MutableMapping):
```

### cookie: 修改後

```python
from collections import abc
class RequestsCookieJar(cookielib.CookieJar, abc.MutableMapping):
```

## structures.py 問題

```bash
File "C:\Users\crazy\AppData\Local\Programs\Python\Python311\Lib\site-packages\requests\structures.py", line 15, in <module>
  class CaseInsensitiveDict(collections.MutableMapping):
                              ^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: module 'collections' has no attribute 'MutableMapping'
```

## structures.py 解法

### structures: 原 Code

```python
class CaseInsensitiveDict(collections.MutableMapping):
```

### structures: 修改後

```python
from collections import abc
class CaseInsensitiveDict(abc.MutableMapping):
```

## urllib3 問題

```bash
ImportError: cannot import name 'ProxySchemeUnsupported' from 'requests.packages.urllib3.exceptions' (C:\Users\crazy\AppData\Local\Programs\Python\Python311\Lib\site-packages\requests\packages\urllib3\exceptions.py)
```

## urllib3 解法

```bash
pip install --upgrade requests urllib3
```
