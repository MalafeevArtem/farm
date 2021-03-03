from django import forms

from fields.models import Field
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class FieldForm(forms.ModelForm):
    class Meta:
        model = Field
        fields = ('name', 'square', 'coordinate', 'cadastral_number')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))
