from django import forms
from .models import News, Category
from django.forms import ModelForm, TextInput, Textarea, NumberInput, FileInput

class NewsForm(ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Виберіть категорію")

    class Meta:
        model = News
        fields = ['title', 'description', 'price', 'location', 'author', 'category']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Назва оголошення"
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Опис публікації",
                'rows': 4,
            }),
            'price': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': "Ціна"
            }),
            'location': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Місцезнаходження"
            }),
            'author': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Автор'
            }),
        }

