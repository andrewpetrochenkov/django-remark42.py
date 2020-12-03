<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/django-remark42.svg?maxAge=3600)](https://pypi.org/project/django-remark42/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/django-remark42.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/django-remark42.py/actions)

### Installation
```bash
$ [sudo] pip install django-remark42
```

##### `settings.py`
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

{% remark42_comments_script 'Page Title' %}
{% remark42_comments_script 'Page Title' max_shown_comments=10 theme='dark' %}
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
    <a href="https://readme42.com/">readme42.com</a>
</p>
