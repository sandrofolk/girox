from django import forms
from django.core.exceptions import ValidationError
from girox.event.models import Subscription, Event


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['name', 'rg', 'cpf', 'email', 'phone', 'date_of_birth', 'address', 'city', 'team', 'event']

    def clean_name(self):
        name = self.cleaned_data['name']
        words = [w.capitalize() for w in name.split()]

        return ' '.join(words)

    def clean(self):
        self.cleaned_data = super().clean()

        _event = self.cleaned_data.get('event')
        if _event.number_limit_subscription != 0 and _event.number_limit_subscription <= _event.subscription_set.count():
            raise ValidationError('As vagas estão esgotadas para este evento!')

        return self.cleaned_data
