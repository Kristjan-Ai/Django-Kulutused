from django.template.defaulttags import register

@register.filter
def cut(value, arg):
    return value.replace(arg, "")

@register.filter
def absolute(value):
    return abs(value)
