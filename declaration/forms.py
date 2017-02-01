from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms


class DeclarationForm(forms.Form):
    next = forms.CharField(widget=forms.HiddenInput, required=False)

    def __init__(self, *args, **kwargs):
        super(DeclarationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_action = 'declaration:form'
        self.helper.add_input(
            Submit('declaration', 'I confirm I am a HCP', css_class="circle-button")
        )
