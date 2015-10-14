from django import template
import markdown2

register = template.Library()


@register.simple_tag(takes_context=True)
def some_tags(context):
  pass


@register.filter
def markdownify(text):
  """
  GitHub Flavored Markdown 
  Usage:
    {{ content | markdownify | safe }}
  Requirements:
    $ pip install pygments
    link to one of the css: https://github.com/richleland/pygments-css
  """
  return markdown2.markdown(text, extras=["fenced-code-blocks"], safe_mode=None)
