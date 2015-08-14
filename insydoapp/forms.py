__author__ = 'Apolikamixitos'

from django import forms

class LongestStringForm(forms.Form):


    list_of_strings = forms.CharField(label='Your strings list (One string per line)', widget=forms.Textarea, max_length=300)
