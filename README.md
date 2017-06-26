# Postmail

```python
import requests
import hashlib
token = hashlib.sha1(
    '<secret_key>:<email>'.encode('utf-8')).hexdigest()
requests.post('http://localhost:5000/' + token, data={
    'from': '',
    'to': '',
    'subject': '',
    'text': '',
})
```
