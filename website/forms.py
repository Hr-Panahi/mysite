from django import forms
from website.models import Contact,Newsletter

class NameForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(max_length=255, required=True)
    message = forms.CharField(widget=forms.Textarea())


class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = ['name','email', 'subject', 'message']
        

class NewsletterForm(forms.ModelForm):

    class Meta:
        model = Newsletter
        fields = '__all__'