from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Penulis(models.Model):
    nama = models.CharField(null=False, blank=False, max_length=255)

    def get_absolute_url(self):
        return reverse('app:detail_penulis', kwargs={'pk': self.pk})

    def __str__(self):
        return self.nama


class Buku(models.Model):
    judul = models.CharField(null=False, blank=False, max_length=255)
    penulis = models.ForeignKey('Penulis', null=False, blank=False,
                                on_delete=models.CASCADE,
                                related_name='penulis_buku')

    def __str__(self):
        return self.nama
