# myapp/templatetags/custom_filters.py

from django import template

register = template.Library()

@register.filter
def currency(value, currency_type='руб.'):
    """Добавляет валютный знак к числу."""
    try:
        value = float(value)
    except (ValueError, TypeError):
        return value
    return f'{value:.2f} {currency_type}'

