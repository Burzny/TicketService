from django import forms

class CreateNewTicket(forms.Form):
    name = forms.CharField(label='Name', max_length=200)
