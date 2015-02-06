from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse
from django.views.generic import View


class UserLogin(View):
    template_name = "login.html"


    def get(self, request, *args, **kwargs):
        msg = 'Welcome'
        return HttpResponse(render(request, self.template_name, {'msg': msg}))




