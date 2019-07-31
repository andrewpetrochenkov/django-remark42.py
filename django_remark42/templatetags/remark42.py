from django import template
from django.conf import settings
from django.utils.safestring import mark_safe

""""
https://github.com/umputun/remark
"""

register = template.Library()

"""
{% load remark42 %}
"""

"""comments:
<div id="remark42"></div>

{% remark42_comments_script 'Page Title' %}
{% remark42_comments_script 'Page Title' max_shown_comments=10 theme='dark' %}
"""

"""last comments:
<div class="remark42__last-comments" data-max="50"></div>

{% remark42_last_comments_script %}
"""

"""comments counter:
<span class="remark42__counter" data-url="https://domain.com/path/to/article/"></span>

{% remark42_counter_script %}
"""

def format(html,**kwargs):
    kwargs.update(host = settings.REMARK42_HOST,site_id = settings.REMARK42_SITE_ID)
    return mark_safe(html.format(**kwargs))

@register.simple_tag
def remark42_comments_script(page_title,max_shown_comments=None,theme=None):
    page_title = page_title.replace("'","\'")
    max_shown_comments = int(max_shown_comments) if max_shown_comments else getattr(settings,'REMARK42_MAX_SHOWN_COMMENTS',15)
    theme = theme if theme else getattr(settings,'REMARK42_THEME','light'), # light, dark
    return format("""
<script>
  var remark_config = {{
    host: '{host}',
    site_id: '{site_id}',
    components: ['embed'],
    max_shown_comments: '{max_shown_comments}',
    theme: '{theme}',
    page_title: '{page_title}'
  }};

  (function(c) {{
    for(var i = 0; i < c.length; i++){{
      var d = document, s = d.createElement('script');
      s.src = remark_config.host + '/web/' +c[i] +'.js';
      s.defer = true;
      (d.head || d.body).appendChild(s);
    }}
  }})(remark_config.components || ['embed']);
</script>
<noscript>
    Please enable JavaScript to view the comments powered by Remark.
</noscript>
""",page_title=page_title,max_shown_comments=max_shown_comments,theme=theme)

@register.simple_tag
def remark42_last_comments_script():
    return format("""
<script>
  var remark_config = {{
    host: '{host}',
    site_id: '{site_id}',
    components: ['last-comments']
  }};

  (function(c) {{
    for(var i = 0; i < c.length; i++){{
      var d = document, s = d.createElement('script');
      s.src = remark_config.host + '/web/' +c[i] +'.js';
      s.defer = true;
      (d.head || d.body).appendChild(s);
    }}
  }})(remark_config.components || ['embed']);
</script>
<noscript>
    Please enable JavaScript to view the comments powered by Remark.
</noscript>
""")

@register.simple_tag
def remark42_counter_script():
    return format("""
<script>
  var remark_config = {{
    host: '{host}',
    site_id: '{site_id}',
    components: ['counter']
  }};

  (function(c) {{
    for(var i = 0; i < c.length; i++){{
      var d = document, s = d.createElement('script');
      s.src = remark_config.host + '/web/' +c[i] +'.js';
      s.defer = true;
      (d.head || d.body).appendChild(s);
    }}
  }})(remark_config.components || ['embed']);
</script>
""")
