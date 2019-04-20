from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Reset
from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name'}), required=True)
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}), required=False)
    message = forms.CharField(
        label='Message',
        widget=forms.Textarea(attrs={"rows": 5, "cols": 20})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-6 mb-0'),
                Column('email', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'message',
            Submit('submit', 'Save'),
            Reset('reset', 'Reset', css_class='btn-danger')
        )
