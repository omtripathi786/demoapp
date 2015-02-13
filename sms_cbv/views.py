from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth import authenticate
from django.template import loader


class UserLogin(View):
    """
        This is a class based view to handle login and authentication
    """
    template_name = "sms_cbv/login.html"

    def get(self, request, *args, **kwargs):
        msg = ''
        return HttpResponse(render(request, self.template_name, {'msg': msg}))

    def post(self, request, *args, **kwargs):
        msg = ''
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        print user
        if user:
            if user.is_active:
                msg = 'done'
            else:
                msg = 'fail'
        return HttpResponse(render(request, self.template_name, {'msg': msg}))


class UserRegistration(View):
    """
        This is a class based view to handle user registration
    """
    template_name = "sms_cbv/register.html"

    def get(self, request, *args, **kwargs):
        msg = ''
        return HttpResponse(render(request, self.template_name, {'msg': msg}))


