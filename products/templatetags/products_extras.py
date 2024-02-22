from django import template
from urllib.parse import urlparse, parse_qs, urlencode

register = template.Library()


@register.simple_tag
def query_replace(request, field, value):
    dict_ = request.GET.copy()
    dict_[field] = value
    return dict_.urlencode()
