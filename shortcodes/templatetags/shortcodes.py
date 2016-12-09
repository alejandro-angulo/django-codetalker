from django import template
from django.template.defaultfilters import stringfilter
from shortcodes.parser import Shortcode_Parser

register = template.Library()
shortcodes = Shortcode_Parser()


@register.filter
@stringfilter
def expand_shortcodes(val):
    return shortcodes.expand_shortcodes(val)
