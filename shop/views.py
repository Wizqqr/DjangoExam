from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from . import forms
from . import models


class GadgetListView(generic.ListView):
    model = models.Gadget
    template_name = 'shop/shop_list.html'
    context_object_name = 'gadgets'

    def get_queryset(self):
        return models.Gadget.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = models.Comment.objects.all()
        context['comment_form'] = forms.CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(request.POST)
        if comment_form.is_valid():
            comment_form.save()
            return redirect('phone_list')
        else:
            gadgets = self.get_queryset()
            comments = models.Comment.objects.all()
            context = self.get_context_data(object_list=gadgets)
            context['comments'] = comments
            context['comment_form'] = comment_form
            return render(request, self.template_name, context)


class GadgetDetailForm(generic.DetailView):
    template_name = 'shop/shop_detail.html'
    context_object_name = 'shop_id'

    def get_object(self, **kwargs):
        shop_id = self.kwargs.get('id')
        return get_object_or_404(models.Gadget, id=shop_id)

class GadgetCreateComment(generic.CreateView):
    template_name = 'shop/shop_list.html'
    form_class = forms.CommentForm
    success_url = '/shop_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(GadgetCreateComment, self).form_valid(form=form)