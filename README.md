
# Satelite telemetry

## Instalação

Verifique a versão do python:

`python --version`

Funciona na versão a partir da 3.5

Selecione o diretório:

```
sat_telemetry
```

Para instalar o software execute o  comando:
```
python setup.py develop
```

Em seguida

```
python manage.py runserver
```

Se não deu nenhum erro vai aparecer um endereço para entrar,

normalmente é o [localhost:8000]()

Caso houve algum erro favor instalar os seguintes pacotes.

`pip install numpy` 

`pip install django`

`pip install django_extensions`

`pip install django-cors-headers`

