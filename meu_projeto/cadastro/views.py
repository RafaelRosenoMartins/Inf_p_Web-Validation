from django.shortcuts import render, redirect
from .forms import UsuarioForm

# Create your views here.

def cadastrar_usuario(request):

    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sucesso')
    else: 

        form = UsuarioForm()

        return render(request, 'cadastro/formulario.html', {'form': form})
    
def sucesso(request):
      return render(request, 'cadastro/sucesso.html')



