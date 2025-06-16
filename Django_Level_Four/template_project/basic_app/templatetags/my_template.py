from django import template

register = template.Library()

@register.filter(name = "cut_peace")
def cut_peace(val, arg):
    """
    This cuts out all values of "arg" from the string! 
    """
    return val.replace(arg,'')
    

# register.filter('cut', cut_peace)    