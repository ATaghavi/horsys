from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.core.urlresolvers import reverse_lazy

from horses.models import Horse
from horses.forms import HorseForm

class HorseList(ListView):
    model = Horse
    context_obj_name = 'horse_list'

class HorseCreate(CreateView):
    model = Horse
    form_class = HorseForm
    success_url = reverse_lazy('horse_list')

class HorseDetail(DetailView):
    model = Horse
    context_obj_name = 'horse'

class HorseUpdate(UpdateView):
    model = Horse
    context_obj_name = 'horses'

class HorseDelete(DeleteView):
    model = Horse
    success_url = reverse_lazy('horse_list')