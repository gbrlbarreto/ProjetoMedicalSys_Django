### Projeto Desafio Django - Medical


Esse projeto foi desenvolvido com as seguintes tecnologias:

- [Python](https://www.python.org/)
- [JavaScript](#)
- [Html](#)
- [Css](#)
- [Django](https://www.djangoproject.com/)
- [Bootstrap](https://facebook.github.io/react-native/)
- [ViaCEP](https://viacep.com.br/)
- [Select2](https://select2.org/)
- [JQuery](https://jquery.com/)

## Instalação

1. Criar ambiente virtual :
```bash
python -m venv venv
```

2. Ativar ambiente virtual (cmd):
```bash
venv\Scripts\activate
```

3. Atualizar pip:
```bash
python -m pip install --upgrade pip
```

4. Instalar dependências:
```bash
pip install -r requirements.txt
```

5. Sincronizar database:
```bash
python manage.py migrate
```

6. Criar um super usuário:
```bash
python manage.py createsuperuser
```

7. Iniciar o servidor:
```bash
python manage.py runserver
```

## 🔖 Implementações

- Autenticação (Login/Logout)
- Controle de acesso
- Acesso dos dados dos Médicos através do Django RestFramework
- Módulo Agendamento (Create, Read, Update, Delete)
- Módulo Médico (Create, Read, Update, Delete)
- Módulo Paciente(Cliente) (Create, Read, Update, Delete)