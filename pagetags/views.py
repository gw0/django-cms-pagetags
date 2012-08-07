# -*- coding: utf-8 -*-
"""
Views for Pagetags Django CMS plugin.

.. seealso::
    http://docs.djangoproject.com/en/1.4/ref/class-based-views/
"""
from django.http import HttpResponse
from django.shortcuts import render

from tagging.models import Tag
import json


def autocomplete_ajax(req):
    """Ajax view for autocompletion functionality."""
    q = req.GET.get('q')
    tags = []
    if q:
        tags = (Tag.objects
                .filter(name__istartswith=q)
                .values_list('name', flat=True))
    response = [ {'id':tag, 'label':tag, 'value':tag}  for tag in tags ]
    return HttpResponse(json.dumps(response), mimetype='application/json')

list_tags = autocomplete_ajax  # backwards compatibility


def page_list(req, tag):
    """View for listing pages containing given tag."""
    return render(req, 'pagetags/page_list.html', {
        'tag': tag,
    })

