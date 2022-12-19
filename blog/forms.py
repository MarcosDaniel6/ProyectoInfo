from django.forms import ModelForm
from django import forms
from .models import Contact, News, Denuncia

class NewsForm(ModelForm):
    class Meta:
        model = News
        exclude = ('date',)        


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        exclude = ('date',)      

class DenunciaForm(forms.ModelForm):
    class Meta:
        model = Denuncia
        fields = [
            "direccion", "texto_denuncia", "email", "telefono",
        ]