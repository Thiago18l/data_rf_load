#!/bin/bash
# Author: Thiago Lopes

load_env_file() {
  while IFS= read -r line || [[ -n "$line" ]]; do
    if [[ $line =~ ^[[:alnum:]] ]]; then
      export "$line"
    fi
  done < "$1"
}


run_program() {
  # Classe para executar
  local class=$1

  # Executa o programa Python
  run $class
}

# Caminho para o arquivo .env
env_file=".env"

# Verifica se o arquivo .env existe
if [ -f "$env_file" ]; then
  # Exporta as variáveis de ambiente a partir do arquivo .env
  load_env_file "$env_file"

  # Classe para executar
  class=$1

  # Executa o programa Python
  run_program "$class"

  echo -e $DATABASE_URL
  echo -e $DEBUG
  echo -e $PATH_FILES

  # Desfaz a exportação das variáveis
  unset DATABASE_URL
  unset DEBUG
  unset PATH_FILES
else
  echo "Arquivo .env não encontrado."
  exit 1
fi
