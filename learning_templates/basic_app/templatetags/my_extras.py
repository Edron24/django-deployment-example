from django import template

register = template.library()

def cut(value, arg):
    """
    This cuts out all values of "arg" from string!
    """
    return value.replace(arg, '')


register.filter('cut', cut)
