from django import template
from django.utils.safestring import mark_safe
register = template.Library()

@register.filter
def highlight_search(text, query):
    highlighted = text.replace(query, '<span class="text-info" style="">{}</span>'.format(query))
    return mark_safe(highlighted)