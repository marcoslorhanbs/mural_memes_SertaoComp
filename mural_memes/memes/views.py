from django.shortcuts import render, get_object_or_404, redirect
from .models import Meme
from .forms import MemeForm


def lista_memes(request):
    categoria = request.GET.get('categoria', '')
    memes = Meme.objects.all()

    if categoria:
        memes = memes.filter(categoria=categoria)

    categorias = Meme.CATEGORIAS

    return render(request, 'memes/lista.html', {
        'memes':           memes,
        'categorias':      categorias,
        'categoria_atual': categoria,
    })


def detalhe_meme(request, pk):
    meme = get_object_or_404(Meme, pk=pk)
    return render(request, 'memes/detalhe.html', {'meme': meme})


def enviar_meme(request):
    if request.method == 'POST':
        form = MemeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('memes:lista')
    else:
        form = MemeForm()

    return render(request, 'memes/enviar.html', {'form': form})
