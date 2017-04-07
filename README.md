# girox

[![Build Status](https://travis-ci.org/sandrofolk/girox.svg?branch=master)](https://travis-ci.org/sandrofolk/girox)
[![Code Health](https://landscape.io/github/sandrofolk/girox/master/landscape.svg?style=flat)](https://landscape.io/github/sandrofolk/girox/master)
[![Coverage Status](https://coveralls.io/repos/github/sandrofolk/girox/badge.svg?branch=master)](https://coveralls.io/github/sandrofolk/girox?branch=master)

## Como desenvolver?

1. Clone o repositório.
2. Crie um virtualenv com Python 3.5
3. Ative o virtualenv.
4. Instale as dependências.
5. Configure a instância com o .env
6. Execute os testes.

```console
git clone git@github.com:sandrofolk/girox.git
cd girox
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test
```

## Como traduzir

1. Gere os arquivos de tradução.
2. Compile os textos traduzidos.

```console
manage makemessages -l en -l pt_BR
manage compilemessages
```

## Como fazer o deploy?

1. Crie uma instância no heroku.
2. Envie as configurações para o heroku.
3. Defina uma SECRET_KEY segura para a instância.
4. Defina DEBUG=False
5. Configure o serviço de email.
6. Envie o código para o heroku.

```console
heroku create NOME_DA_INSTANCIA
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
# configuro o email
git push heroku master --force
```

## Util

Comando para desabilitar o collectstatic do heroku  
```console
heroku config:set DISABLE_COLLECTSTATIC=1
```
