from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    """
    Multiplica dos valores.
    value: El primer número.
    arg: El segundo número.
    """
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return 0
