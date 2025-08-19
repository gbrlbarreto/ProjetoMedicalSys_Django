### Projeto Desafio Django - Medical

Este projeto é uma aplicação web desenvolvida em Django para gerenciamento de agendamentos médicos, gerenciamento de pacientes e também gerenciamento de médicos.
O sistema foi criado para facilitar o controle de consultas, oferecendo funcionalidades de cadastro, edição, arquivamento e desarquivamento de agendamentos de forma simples e intuitiva.

Esse projeto foi desenvolvido com as seguintes tecnologias:

- [Python 3.9.0](https://www.python.org/)
- [HTML](#)
- [CSS](#)
- [JavaScript](#)
- [Django Framework](https://www.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)
- [ViaCEP](https://viacep.com.br/)
- [Select2](https://select2.org/)
- [JQuery](https://jquery.com/)
- [SQLite](https://sqlite.org/)

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

8. Acesse o navegador:
```bash
http://127.0.0.1:8000
```

9. Dados para teste:
```bash
Username: admin
Password: admin
```

## ✨ Funcionalidades

- 📋 Listagem de Agendamentos com status (Cancelado, A Confirmar, Confirmado, Finalizado)
- ➕ Cadastro de novos pacientes com informações completas
- ➕ Cadastro de novos médicos
- ➕ Cadastro de novos agendamentos com paciente, médico e data e hora do agendamento
- ✏️ Edição de agendamentos existentes
- 🗄️ Arquivamento e desarquivamento de agendamentos existentes
- 🔐 Autenticação de usuários (login/logout e saudação personalizada)
- 🎨 Interface estilizada com Bootstrap e imagens de fundo personalizadas
- 📊 Controle visual por badges para facilitar a identificação do status das consultas

## 🔖 Implementações

- Autenticação (Login/Logout)
- Controle de acesso
- Acesso dos dados dos Médicos através do Django RestFramework
- Módulo Agendamento (Create, Read, Update, Archive, Unarchive)
- Módulo Médico (Create, Read, Update, Delete)
- Módulo Paciente (Cliente) (Create, Read, Update, Delete)
- Acesso aos dados através do Django RestFramework
- Banco de dados SQLite
- Disponibilidade do Swagger
