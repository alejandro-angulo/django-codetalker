"""
Settings for shortcodes are namespaced in the SHORTCODES setting.
For exmaple your project's `settings.py` file might looks like this:

SHORTCODES = {
    'SHORTCODE_DELIMETER': '@@',
}
"""

from django.conf import settings

DEFAULTS = {
    'SHORTCODE_DELIMETER': '@@',
    'SHORTCODE_PATH': 'shortcodes',
}

# Check if a setting is applied in the Django project settings.py,
#   if not use the default.
SETTINGS = {}
for setting_name, setting_default in DEFAULTS.items():
    try:
        SETTINGS.SHORTCODES[setting_name]
        SETTINGS[setting_name] = SETTINGS.SHORTCODES[setting_name]
    except AttributeError:
        SETTINGS[setting_name] = DEFAULTS[setting_name]
