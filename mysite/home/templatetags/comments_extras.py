# home/templatetags/comments_extras.py
from django import template

register = template.Library()

@register.simple_tag
def some_tag():
    return "This is a custom tag"
