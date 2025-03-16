# myapp/templatetags/custom_tags.py

from django import template
from django.urls import resolve

register = template.Library()

@register.simple_tag(takes_context=True)
def active_class(context, url_name, class_name='active'):
    """Возвращает класс для активной страницы."""
    request = context['request']
    current_url = resolve(request.path_info).url_name
    if current_url == url_name:
        return class_name
    return ''

