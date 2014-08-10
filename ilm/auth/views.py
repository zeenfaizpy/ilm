from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import FormView
from django.contrib.auth import REDIRECT_FIELD_NAME, login, logout

from .forms import LoginForm

class LoginView(FormView):
    """
    View to login the user.
    """
    form_class = LoginForm
    template_name = "login.html"
    
    def get_success_url(self):
        """
        Return success url after login.
        """
        next_url = self.request.GET(REDIRECT_FIELD_NAME, None)
        if not next_url:
            next_url = reverse_lazy('home')
        return next_url

    def get(self, request, *args, **kwargs):
        """
        Returns to success url if authenticated.
        """
        if request.user.is_authenticated():
            redirect(self.get_success_url())
        return super(LoginView, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        """
        Override form_valid to login.
        """
        login(self.request, form.get_user())
        super(LoginView, self).form_valid(form)


class LogoutView(FormView):
    """
    View to logout the User.
    """
    def get_success_url(self):
        """
        Returns to url after logout.
        """
        next_url = self.request.GET(REDIRECT_FIELD_NAME, None)
        if not next_url:
            pass
        return next_url

    def get(self, request, *args, **kwargs):
        """
        Logout the user and returns to success url.
        """
        logout(request)
        return redirect(self.get_success_url())