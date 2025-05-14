


# 🐍 Como criar e ativar um Virtual Environment
## 1. 📦 Instale o virtualenv (se ainda não tiver)

pip install virtualenv

## 2. 🛠️ Crie o ambiente virtual
Na pasta do seu projeto:


virtualenv venv
Isso cria uma pasta chamada venv com o ambiente isolado.

## 3. ▶️ Ative o ambiente virtual
Windows:

venv\Scripts\activate


## 5. 📄 Salvar dependências
Depois de instalar tudo que seu projeto precisa:


pip freeze > requirements.txt


## 6. 📥 Instalar dependências depois
Se for clonar o projeto em outro lugar:

pip install -r requirements.txt


## 7. ❌ Desativar o ambiente virtual
Quando terminar:

deactivate 