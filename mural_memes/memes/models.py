from django.db import models


class Meme(models.Model):
    CATEGORIAS = [
        ('programacao', 'Programação'),
        ('faculdade',   'Faculdade'),
        ('games',       'Games'),
        ('outros',      'Outros'),
    ]

    titulo     = models.CharField(max_length=200, verbose_name='Título')
    imagem_url = models.URLField(help_text='Cole a URL direta de uma imagem (ex: https://i.imgur.com/abc.jpg)')
    descricao  = models.TextField(blank=True, verbose_name='Descrição')
    categoria  = models.CharField(max_length=20, choices=CATEGORIAS, default='outros', verbose_name='Categoria')
    criado_em  = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-criado_em']
        verbose_name = 'Meme'
        verbose_name_plural = 'Memes'

    def __str__(self):
        return self.titulo
