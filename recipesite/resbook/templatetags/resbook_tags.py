from django import template
from resbook.models import *

register = template.Library()

@register.simple_tag(name="getcats")
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('resbook/list_categories.html')
def show_categories():
    cats = Category.objects.all()
    return {"cats": cats}

