from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class ContactForm(forms.Form):
	Subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Subject'}))
	Email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'E-mail'}))
	Message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Message'}))
	CC_myself = forms.BooleanField(required=False)
	def __init__(self, *args, **kwargs):
		super(ContactForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_id = 'contact_form'
		self.helper.form_class = 'blueForms'
		self.helper.form_method = 'post'
		self.helper.form_action = 'email'
		self.helper.add_input(Submit('submit', 'Submit'))