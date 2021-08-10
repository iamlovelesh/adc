from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from . import forms
from django.shortcuts import render


class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"


@login_required
def profile_detail(request):
    return render(request, "profile.html")


class LogoutRedirectView(TemplateView):
    template_name = "thanks.html"
