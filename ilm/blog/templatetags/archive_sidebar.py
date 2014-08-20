import datetime

from django import template
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect

register = template.Library()

@register.inclusion_tag('post_year_archive.html')
def archive_sidebar_widget():
    """
    Returns the url(redirect) of post archive view to show
    post archives.
    """
    url = reverse_lazy('post_year_archive', 
                        kwargs={'year': datetime.date.today().year})
    redirect(url) 
