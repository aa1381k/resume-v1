from django import template

register = template.Library()


@register.filter(name='mul')
def mul(value):
    return int(value) * 20