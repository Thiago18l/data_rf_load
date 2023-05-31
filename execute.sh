#!/bin/bash

CLASS=$1

# Exporta as variáveis de ambiente
export DATABASE_URL="postgres://starship_user:starship_password@localhost/starship"
export DEBUG=True
export PATH_FILES="/home/lionheart/dev/dados_receita/Simples/"

# Executa o programa Python
run $CLASS

# Desfaz a exportação das variáveis
unset DATABASE_URL
unset DEBUG
unset PATH_FILES
