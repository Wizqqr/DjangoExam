from django.shortcuts import render, get_object_or_404
from . import models, forms
from django.views import generic

class ClothListView(generic.ListView):
    model = models.Cloth
    template_name = 'clothes/cloth_list.html'
    context_object_name = 'clothes'

class YoungClothListView(generic.ListView):
    model = models.Cloth
    template_name = 'clothes/young.html'
    context_object_name = 'clothes'

    def get_queryset(self):
        return models.Cloth.objects.filter(tags__name='молодежь').order_by('-id')

class OldClothListView(generic.ListView):
    model = models.Cloth
    template_name = 'clothes/old.html'
    context_object_name = 'clothes'

    def get_queryset(self):
        return models.Cloth.objects.filter(tags__name='пенсионерам').order_by('-id')

class ClothDetailView(generic.DetailView):
    template_name = 'clothes/cloth_detail.html'
    context_object_name = 'cloth_id'

    def get_object(self, **kwargs):
        cloth_id = self.kwargs.get('id')
        return get_object_or_404(models.Cloth, id=cloth_id)

