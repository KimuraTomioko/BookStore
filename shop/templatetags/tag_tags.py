

from django import template
from shop.models import Tag  

register = template.Library()

@register.simple_tag
def list_tags():
    """Возвращает список тегов или категорий."""
    tags = Tag.objects.all()  # Получаем все теги или категории из базы данных
    return tags
