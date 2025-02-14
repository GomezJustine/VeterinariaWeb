# appVeterinaria/templatetags/base64_filters.py

import base64
from django import template

register = template.Library()

@register.filter
def b64encode(value):
    """Codifica el valor en base64."""
    if value is None:
        return ""
    return base64.b64encode(value).decode('utf-8')
