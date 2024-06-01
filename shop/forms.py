from django import forms
from . import models

class ShopForm(forms.ModelForm):
    class Meta:
        model = models.Gadget
        fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'placeholder': 'Добавить комментарий'}),
        }
