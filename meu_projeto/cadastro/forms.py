from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'telefone']


        #Validação da quantidade de caracteres do nome do usuário no input
    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        if len(nome) <5 or len(nome) > 40:
            raise forms.ValidationError("Caro usuário, o seu nome deve ter entre 5 e 40 caracteres.")
        return nome
    
        #Validação da quantidade de caracteres do telefone do usuário no input
    def clean_telefone(self):
        telefone = self.cleaned_data.get('telefone')
        if not telefone.isdigit() or len(telefone) != 11:
            raise forms.ValidationError("Caro usuário, o telefone deve conter 11 dígitos numéricos")
        return telefone