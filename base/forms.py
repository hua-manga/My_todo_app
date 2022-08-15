from django import forms

# voy a reordenar los formatos y las vistas


class PositionForm(forms.Form):
    position = forms.CharField()
