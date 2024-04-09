from django import forms
from .models import Article, Comment
from django.conf import settings


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        data = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
        widgets = {'dates': forms.TextInput(attrs={'placeholder': '%Y-%m-%d'})}


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        data = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
        widgets = {'dates': forms.TextInput(attrs={'placeholder': '%Y-%m-%d'})}