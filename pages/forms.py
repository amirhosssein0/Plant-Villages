from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'placeholder': 'Your Name',
        'required': True
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your Email',
        'required': True
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Your Message',
        'rows': 5,
        'required': True
    }))


