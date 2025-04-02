# Django
from django import forms

# Local application / specific library imports
from .fields import SIRENField, SIRETField


class SIRETForm(forms.Form):
    siret = SIRETField(label="Siret", max_length=14)


class SIRENForm(forms.Form):
    siren = SIRENField(label="Siren", max_length=9)
