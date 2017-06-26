# Postmail

## Server

```sh
gunicorn postmail:app
```

## Send

```python
from postmail import send
send('<email>', '<secret_key>', 'http://localhost:5000', subject='', text='')
```

## License

[MIT](https://marksteve.mit-license.org)

