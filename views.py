import json
from django.conf.urls import patterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.shortcuts import render_to_response as render
from django.http import HttpResponse as response
from django.http import JsonResponse

jsonify = lambda **data: JsonResponse(dict(**data))

def index(request):
    return render('base.html')

def users(request):
    return jsonify(
        users=['Mike', 'Tim']
    )

urlpatterns = patterns('',
    (r'^$', index),
    (r'^users.json$', users),
    )

urlpatterns += staticfiles_urlpatterns()
