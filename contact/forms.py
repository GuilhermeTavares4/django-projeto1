from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Nome')
    email = forms.EmailField(label='Email')
    phone = forms.CharField(label='Telefone')
    message = forms.CharField(widget=forms.Textarea(attrs={'name':'body', 'rows':3, 'cols':5}), label='Mensagem')
