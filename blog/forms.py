from django import forms

class PostSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Word')
    data_val = forms.DateTimeField(label='date_value')