from django import forms


class DoForm(forms.Form):
    text = forms.CharField(max_length=50,
                           widget=forms.TextInput(
                            attrs={'class': 'form-control',
                                   'placeholder': 'a django todo list',
                                   }
                               ))
