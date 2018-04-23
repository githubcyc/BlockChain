import json
# https://www.pydanny.com/pretty-formatting-json-django-admin.html
# http://pygments.org/
from pygments import highlight
from pygments.lexers import JsonLexer
from pygments.formatters import HtmlFormatter

from django.contrib import admin
from django.utils.safestring import mark_safe


def data_prettified(js):
    """Function to display pretty version of our data"""

    # Convert the data to sorted, indented JSON
    response = json.dumps(js, sort_keys=True, indent=2)

    # Truncate the data. Alter as needed
    response = response[:5000]

    # Get the Pygments formatter
    formatter = HtmlFormatter(style='colorful')

    # Highlight the data
    response = highlight(response, JsonLexer(), formatter)

    # Get the stylesheet
    style = "<style>" + formatter.get_style_defs() + "</style><br>"

    # Safe the output
    return mark_safe(style + response)


data_prettified.short_description = 'data prettified'
