from django.shortcuts import render
from django.views.generic import (TemplateView, ListView, CreateView, DetailView,
                                    FormView)
from .models import Penulis
from .forms import PenulisForm, PenulisBukuFormSet
from django.urls import reverse
from django.contrib import messages
from django.views.generic.detail import SingleObjectMixin
from django.http import HttpResponseRedirect


# Create your views here.
class HomeView(TemplateView):
    template_name = 'app/home.html'


class PenulisListView(ListView):
    model = Penulis
    template_name = 'app/daftar_penulis.html'


class PenulisCreateView(CreateView):
    model = Penulis
    template_name = 'app/tambah_penulis.html'
    form_class = PenulisForm

    def form_valid(self, form):
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Penulis sudah ditambahkan'
        )
        return super().form_valid(form)


class PenulisDetailView(DetailView):
    model = Penulis
    template_name = 'app/detail_penulis.html'


class PenulisBukuUpdateView(SingleObjectMixin, FormView):
    model = Penulis
    template_name = 'app/penulis_buku_edit.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Penulis.objects.all())
        return super().get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Penulis.objects.all())
        return super().post(request, *args, **kwargs)

    def get_form(self, form_class=None):
        return PenulisBukuFormSet(**self.get_form_kwargs(), instance=self.object)

    def form_valid(self, form):
        form.save()

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Perubahan berhasil disimpan'
        )
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('app:detail_penulis', kwargs={'pk': self.object.pk })
