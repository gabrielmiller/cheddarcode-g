from django import forms

class ContactForm(forms.Form):
    email = forms.EmailField()
    text = forms.CharField( widget=forms.Textarea )

    def clean_text(self):
        cd = self.cleaned_data
        text = cd.get('text')
        if len(text) < 25:
            raise forms.ValidationError("Please enter at least 25 characters.")
        return text

    def clean(self):
        cd = self.cleaned_data

        email = cd.get('email')
        text = cd.get('text')

        if email == text:
            raise forms.ValidationError("Your text should not be the same as your email address.")

        return cd
