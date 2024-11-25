from django.shortcuts import render
from contact.forms import ContactForm
from django.conf import settings
from django.core import mail
from django.http import HttpResponseRedirect
from django.template.loader import render_to_string
from django.contrib import messages



def enviarContato(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)
    
def create(request):
    form = ContactForm(request.POST)

    if not form.is_valid():
        return render(request, 'contact/contact_form.html', {'form': form})
    
    form_data = form.cleaned_data

    _send_mail(
        'contact/contact_email.txt',
        form_data,
        'Contato enviado.',
        form_data['email'],
        settings.DEFAULT_FROM_EMAIL
        )

    messages.success(request, 'Contato enviado com sucesso!')
    return HttpResponseRedirect('/contato/')


def new(request):
    return render(request, 'contact/contact_form.html', {'form': ContactForm()})


#TRADUZIR PARA CONTATO (TALVEZ)
def _send_mail(template_name, context, subject, from_, to):
    body = render_to_string(template_name, context)
    email = mail.send_mail(subject, body, from_, [from_, to])