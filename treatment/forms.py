from django import forms

class TreatmentUploadForm(forms.Form):
    photo = forms.ImageField(label='Upload Plant Photo', required=True)
    description = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': 'Describe the problem (optional)',
            'rows': 3
        }),
        required=False
    ) 