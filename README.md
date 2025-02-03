# Sistema de Casamento

Este é um projeto full-stack de um site de casamento desenvolvido com Angular (frontend) e Django (backend). O site permite que os convidados visualizem informações sobre o evento, confirmem presença e escolham presentes da lista de casamento.

## 📋 Funcionalidades

- Página Inicial
  - Contagem regressiva para o evento
  - Informações sobre os noivos
  - Detalhes do evento
  - Localização

- Lista de Presentes
  - Visualização de presentes disponíveis
  - Sistema de compra de presentes
  - Integração com sistema de pagamento

- Confirmação de Presença
  - Busca de convite por código ou nome
  - Formulário para confirmação de presença
  - Gestão de convidados

- Área Administrativa
  - Gerenciamento de presentes
  - Controle de convidados
  - Relatórios e estatísticas

## 🚀  Tecnologias Utilizadas

### Backend

- Python 3.10
- Django 4.2+
- Django REST Framework
- PostgreSQL

### Frontend

- Angular 17
- TypeScript
- Bootstrap 5
- SCSS

## 🛠️ Instalação e Configuração

### Frontend Angular

1. Clone o repositório

```bash
git clone <url-do-repositorio>

# Entre na pasta do frontend
cd frontend_casamento

# Instale as dependências
npm install

# Execute o servidor de desenvolvimento
ng serve
```

### Backend

1. Clone o repositório

```bash
git clone <url-do-repositorio>

# Entre na pasta do backend
cd backend_casamento

# Crie um ambiente virtual
python -m venv venv

# Ative o ambiente virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt

# Execute as migrações
python manage.py migrate

# Inicie o servidor
python manage.py runserver
```

## 🌐 Endpoints da API

- `GET /api/presentes/`: Lista todos os presentes
- `GET /api/convidados/`: Lista todos os convidados
- `POST /api/confirmacao/`: Registra confirmação de presença

## 💻 Estrutura do Projeto

```text
frontend_casamento/
├── src/
│   ├── app/
│   │   ├── components/
│   │   │   ├── home/
│   │   │   ├── lista-presentes/
│   │   │   ├── confirma-presenca/
│   │   │   └── shared/
│   │   ├── services/
│   │   └── ...
│   ├── assets/
│   └── styles/
└── ...

backend_casamento/
├── casamento/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── api/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   └── ...
└── ...
```

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## ✨ Autores

- **Bárbara Zamperete** - *Desenvolvimento Full-stack*

---
⌨️ com ❤️ por Bárbara Zamperete
