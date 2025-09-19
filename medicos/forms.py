from django.contrib.auth.models import User
from django import forms

def calc_digito(cpf, digito):
    if digito == 1:
        pesos = range(10, 1, -1)
        numeros = cpf[:9]
    else:
        pesos = range(11, 1, -1)
        numeros = cpf[:10]
    soma = sum(int(n) * p for n, p in zip(numeros, pesos))
    resto = soma % 11
    return 0 if resto < 2 else 11 - resto

INVALID_CPFS = {
    '01234567890',
    '12345678909',
    '98765432100',
    '12312312312',
    '32132132132',
    '12345678900',
    '00000000191',
    '11122233396',
}

class MedicoForm(forms.Form):
    # Dados do User
    first_name = forms.CharField(label="Nome", max_length=30)
    last_name = forms.CharField(label="Sobrenome", max_length=30)
    username = forms.CharField(label="Usuário", max_length=30)
    email = forms.EmailField(label="Email")
    senha = forms.CharField(label="Senha", widget=forms.PasswordInput)
        
    # Dados do Medico
    cpf = forms.CharField(label="CPF", max_length=15)
    crm = forms.CharField(label="CRM", max_length=15, required=False)
    phone = forms.CharField(label="Telefone", max_length=16, required=False)

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Usuário já existe.")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("E-mail já cadastrado.")
        return email

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')

        if not cpf:
            raise forms.ValidationError("O campo CPF é obrigatório.")

        cpf = ''.join(filter(str.isdigit, cpf))  # Remove caracteres não numéricos

        if len(cpf) != 11:
            raise forms.ValidationError("CPF deve conter 11 dígitos.")

        if cpf in INVALID_CPFS:
            raise forms.ValidationError("CPF inválido.")
        
        if cpf == cpf[0] * 11:
            raise forms.ValidationError("CPF inválido.")

        digito1 = calc_digito(cpf, 1)
        digito2 = calc_digito(cpf, 2)

        if digito1 != int(cpf[9]) or digito2 != int(cpf[10]):
            raise forms.ValidationError("CPF inválido.")

        return cpf
