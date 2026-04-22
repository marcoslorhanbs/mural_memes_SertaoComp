# 🎭 Mural de Memes — Projeto Django

Plataforma simples para enviar e visualizar memes, desenvolvida com Django e Bootstrap 5.

## 🚀 Como rodar o projeto

### 1. Instalar o Django
```bash
pip install django
```

### 2. Aplicar as migrations
```bash
python manage.py migrate
```

### 3. Criar o superusuário (para acessar o admin)
```bash
python manage.py createsuperuser
```

### 4. Iniciar o servidor
```bash
python manage.py runserver
```

### 5. Acessar no navegador
- **Site:** http://127.0.0.1:8000/
- **Admin:** http://127.0.0.1:8000/admin/

---

## 📁 Estrutura do projeto

```
mural_memes/
├── mural_memes/        # Configurações do projeto
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── memes/              # Aplicação principal
│   ├── migrations/
│   ├── templates/
│   │   └── memes/
│   │       ├── base.html
│   │       ├── lista.html
│   │       ├── detalhe.html
│   │       └── enviar.html
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
└── manage.py
```

## 🔧 Funcionalidades

- Listagem de memes em grid responsivo
- Filtro por categoria (Programação, Faculdade, Games, Outros)
- Página de detalhe do meme
- Formulário para envio de novos memes
- Painel administrativo completo

## 🎨 Tecnologias

- **Backend:** Python 3 + Django 4+
- **Frontend:** Bootstrap 5.3 (via CDN)
- **Banco de dados:** SQLite (padrão Django)
