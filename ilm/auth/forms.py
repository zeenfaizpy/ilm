from django.contrib.auth.forms import AuthenticationForm

from crispy_forms.helper import FormHelper

class LoginForm(AuthenticationForm):
    """
    Overriding default authentication form for crispy.
    """
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = "form-horizontal"
        self.helper.form_tag = False