from django import forms


class SignupForm(forms.Form):
    email = forms.EmailField(label='Your email')