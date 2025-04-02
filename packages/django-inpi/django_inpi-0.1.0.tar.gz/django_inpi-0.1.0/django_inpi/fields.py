# Django
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


class SIRETField(forms.CharField):
    # TODO: handle the case where a pasted siret contain spaces (truncate them before validating data?).
    def to_python(self, value):
        if not value:
            return ""
        return value

    def validate(self, value):
        length = len(value)
        if length != 14:
            raise ValidationError(
                _(f"SIRET must be 14 chars long (yours is {length})."),
                code="invalid",
            )
        if not value.isnumeric():
            raise ValidationError(
                _("SIRET must only contains numbers."),
                code="invalid",
            )


class SIRENField(forms.CharField):
    # TODO: handle the case where a pasted siren contain spaces (truncate them before validating data?).
    def to_python(self, value):
        if not value:
            return ""
        return value

    def validate(self, value):
        length = len(value)
        if length != 9:
            raise ValidationError(
                _(f"SIREN must be 9 chars long (yours is {length})."),
                code="invalid",
            )
        if not value.isnumeric():
            raise ValidationError(
                _("SIREN must only contains numbers."),
                code="invalid",
            )
