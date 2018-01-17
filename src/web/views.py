# -*- coding:utf8 -*-

from django.shortcuts import render


def index(request):
    context={}
    login_page = "index.html"

    return render(request, login_page, context=context)