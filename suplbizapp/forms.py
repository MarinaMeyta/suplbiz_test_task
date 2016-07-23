from django import forms

class Search(forms.Form):
    customer = forms.CharField(max_length=50)