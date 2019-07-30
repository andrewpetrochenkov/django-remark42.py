<!--
https://pypi.org/project/readme-generator/
https://pypi.org/project/python-readme-generator/
https://pypi.org/project/django-readme-generator/
-->

[![](https://img.shields.io/pypi/pyversions/django-remark42.svg?longCache=True)](https://pypi.org/project/django-remark42/)
[![](https://img.shields.io/pypi/v/django-remark42.svg?maxAge=3600)](https://pypi.org/project/django-remark42/)
[![Travis](https://api.travis-ci.org/andrewp-as-is/django-remark42.py.svg?branch=master)](https://travis-ci.org/andrewp-as-is/django-remark42.py/)

#### Installation
```bash
$ [sudo] pip install django-remark42
```

#### `settings.py`
```python
INSTALLED_APPS+= [
    'django_remark42'
]

REMARK42_HOST=os.getenv('REMARK42_HOST')
REMARK42_SITE_ID=os.getenv('REMARK42_SITE_ID')
# optional:
REMARK42_MAX_SHOWN_COMMENTS=os.getenv('REMARK42_MAX_SHOWN_COMMENTS') # 15 by default
REMARK42_THEME=os.getenv('REMARK42_THEME') # 'light' by default
```

#### Examples
```
{% load remark42 %}
```

comments:
```html
<div id="remark42"></div>

{% remark42_comments_script %}
{% remark42_comments_script count=10 theme='dark' title='Title' %}
```

last comments:
```html
<div id="remark42"></div>

{% remark42_last_comments_script %}
```

counter:
```html
<div id="remark42"></div>

{% remark42_counter_script %}
```

#### Links
+   [github.com/umputun/remark](https://github.com/umputun/remark)

<p align="center">
    <a href="https://pypi.org/project/django-readme-generator/">django-readme-generator</a>
</p>