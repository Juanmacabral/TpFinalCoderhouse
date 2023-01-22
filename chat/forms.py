from django import forms

class MensajeForm(forms.Form):
    texto = forms.CharField(label='Mensaje', max_length=200)
    correo = forms.EmailField(label='Correo electrónico')