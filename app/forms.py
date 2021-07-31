from django.forms import ModelForm
from django.forms import TextInput
from django.utils.translation import gettext_lazy as _
from django.forms.models import inlineformset_factory
from .models import Penulis, Buku


class PenulisForm(ModelForm):
    class Meta:
        model = Penulis
        fields = ['nama',]

        labels = {
            'nama': _('Nama Penulis'),
        }
        help_texts = {
            'nama': _('Disini tempat isi nama penulis.'),
        }
        widgets = {
            'nama': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Isi nama penulis.'
                }),
        }

PenulisBukuFormSet = inlineformset_factory(Penulis, Buku, fields=('judul',))
