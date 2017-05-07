from django import forms
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core import mail


class ContactForm(forms.Form):
    name = forms.CharField(label='Nome')
    email = forms.EmailField(label='E-mail', required=False)
    phone = forms.CharField(label='Telefone', required=False)
    message = forms.CharField(label='Mensagem', widget=forms.Textarea)

    def clean(self):
        self.cleaned_data = super().clean()

        if not self.cleaned_data.get('email') and not self.cleaned_data.get('phone'):
            raise ValidationError('Informe seu e-mail ou telefone.')

        return self.cleaned_data

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        to = self.cleaned_data.get('email')
        from_ = str(settings.DEFAULT_FROM_EMAIL),

        message = "{name} / {email} / {phone} disse: ".format(
            name=self.cleaned_data.get('name'),
            email=to,
            phone=self.cleaned_data.get('phone'),
        )
        message += "\n\n{0}".format(self.cleaned_data.get('message'))
        # mail.send_mail(
        #     subject='Contato pelo site www.girox.com.br',
        #     message=message,
        #     from_email=settings.DEFAULT_FROM_EMAIL,
        #     recipient_list=[settings.DEFAULT_FROM_EMAIL],
        # )
        email = mail.EmailMessage(
            subject='Contato pelo site www.girox.com.br',
            body=message,
            to=from_,
            reply_to=[to],
        )
        email.send()
