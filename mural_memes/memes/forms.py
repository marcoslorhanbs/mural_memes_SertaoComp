from django import forms
from .models import Meme


class MemeForm(forms.ModelForm):
    class Meta:
        model  = Meme
        fields = ['titulo', 'imagem_url', 'descricao', 'categoria']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Quando o código funciona na primeira tentativa',
            }),
            'imagem_url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://i.imgur.com/exemplo.jpg',
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Conte um pouco sobre esse meme (opcional)',
            }),
            'categoria': forms.Select(attrs={
                'class': 'form-select',
            }),
        }
        labels = {
            'titulo':     'Título',
            'imagem_url': 'URL da Imagem',
            'descricao':  'Descrição (opcional)',
            'categoria':  'Categoria',
        }
