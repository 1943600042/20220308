from django import template

register = template.Library()


@register.filter()
def my_add(num):
    return (num/5+10)/2+100




