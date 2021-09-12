from django import template

register = template.Library()

@register.filter
def filter_first_letter(words, arg):
    return [ word for word in words if word.acronym.first_letter == arg ]
