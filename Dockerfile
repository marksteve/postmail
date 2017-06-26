FROM python:3-onbuild
CMD ['gunicorn', 'postmail:app']
