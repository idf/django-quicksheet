from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def some_tags(context):
  pass
