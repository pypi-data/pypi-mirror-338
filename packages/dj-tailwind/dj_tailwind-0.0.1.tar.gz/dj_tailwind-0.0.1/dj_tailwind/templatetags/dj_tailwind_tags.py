import os
import time

from django import template
from django.conf import settings
from django.templatetags.static import static
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def dj_tailwind_css(v=None):
    dj_tailwind_css_path = settings.DJ_TAILWIND_CSS_OUTPUT  # type: ignore
    is_static_path = not os.path.isabs(dj_tailwind_css_path)
    href = dj_tailwind_css_path
    if v is None and settings.DEBUG:
        # append a time-based suffix to force reload of css in dev mode
        v = int(time.time())
    if is_static_path:
        href = static(dj_tailwind_css_path)
    if v:
        href += f"?v={v}"

    tailwind_stylesheet = f'<link rel="stylesheet" href="{href}">'

    if settings.DEBUG:
        tailwind_stylesheet += f'<link rel="preload" as="style" href="{href}">'

    return mark_safe(tailwind_stylesheet)
