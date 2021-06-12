from django import template

register = template.Library()

@register.filter
def flatten_stanzas(stanzas):
    lines = []
    for stanza in stanzas.all():
        lines += [ line.line for line in stanza.lines.all() ] + [ '' ]
    return lines
