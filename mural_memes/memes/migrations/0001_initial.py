from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Meme',
            fields=[
                ('id',         models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo',     models.CharField(max_length=200, verbose_name='Título')),
                ('imagem_url', models.URLField(help_text='Cole a URL direta de uma imagem (ex: https://i.imgur.com/abc.jpg)')),
                ('descricao',  models.TextField(blank=True, verbose_name='Descrição')),
                ('categoria',  models.CharField(
                    choices=[
                        ('programacao', 'Programação'),
                        ('faculdade',   'Faculdade'),
                        ('games',       'Games'),
                        ('outros',      'Outros'),
                    ],
                    default='outros',
                    max_length=20,
                    verbose_name='Categoria',
                )),
                ('criado_em',  models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name':        'Meme',
                'verbose_name_plural': 'Memes',
                'ordering':            ['-criado_em'],
            },
        ),
    ]
