#!/bin/bash

CLASS=$1

# Exporta as variáveis de ambiente
export DATABASE_URL="postgres://starship_user:starship_password@localhost/starship"
export DEBUG=True
export PATH_FILES="/mnt/c/Users/Thiago/Downloads/DADOS RECEITA/Estabelecimentos"

# Executa o programa Python
run $CLASS

# Desfaz a exportação das variáveis
unset DATABASE_URL
unset DEBUG
unset PATH_FILES
