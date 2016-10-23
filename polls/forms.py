from django import forms
from polls.models import Human, Purchase

class NameForm(forms.Form):
	username = forms.CharField(max_length=64)

class AutoForm(forms.ModelForm):
	class Meta:
		model = Human
		fields = '__all__'

class PurchaseForm(forms.ModelForm):
	class Meta:
		model = Purchase
		fields = '__all__'
