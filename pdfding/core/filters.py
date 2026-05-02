from django import template

register = template.Library()


@register.filter
def to_milliseconds(value):
    """Convert a datetime to milliseconds since epoch."""
    if value is None:
        return ""
    return int(value.timestamp() * 1000)