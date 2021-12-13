from django import template
register = template.Library()

@register.simple_tag
def multiply(x,y):
    return x*y
