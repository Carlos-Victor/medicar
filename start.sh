#!/bin/bash

## Copiar Script e executar como SUDO

## Variáveis
cian='\033[0;36m'
green='\033[0;32m'
red='\033[0;31m'
yellow='\033[1;33m'
NC='\033[0m' # No Color

    echo -e "${green} ______________________________________________________________ "
    echo "|                                                              |"
    echo "|                         Iniciando                            |"
    echo -e "|______________________________________________________________|${NC}"

    echo -e "${green} ______________________________________________________________"
    echo "|                                                              |"
    echo "|         Instalando Pacotes Django, Django rest, Django cors  |"
    echo -e "|______________________________________________________________|${NC}"

pip install Django django-rest-framework django-cors-headers
    echo -e "${green} ______________________________________________________________"
    echo "|                                                              |"
    echo "|         Pacotes Instalados, Rodando Migrates                 |"
    echo -e "|______________________________________________________________|${NC}"
python manage.py migrate
    echo -e "${green} ______________________________________________________________"
    echo "|                                                              |"
    echo "|                       Migrate aplicada.                      |"
    echo -e "|______________________________________________________________|${NC}"

# python manage.py generator_token
#     echo -e "${green} ______________________________________________________________"
#     echo "|                                                              |"
#     echo "|               Token Gerado e configurado                     |"
#     echo -e "|______________________________________________________________|${NC}"
