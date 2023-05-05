# LOAD DATA RECEITA FEDERAL

## Instalação

1. Clone o repositório:
```bash
    git clone git@github.com:TechPayment/load_data_rf.git
```


2. Instale as dependências do projeto:

```bash
    pip install -r requirements.txt
```

## Configuração

Antes de executar o projeto, é necessário criar um arquivo .env na raiz do projeto e configurar as seguintes variáveis de ambiente:

    DATABASE_URL: URL de conexão com o banco de dados PostgreSQL.
    DEBUG: Booleano que define se o modo debug está ativo ou não.
    PATH_FILES: Caminho absoluto para a pasta que contém os arquivos CSV a serem importados.

Exemplo de arquivo .env:

```bash
DATABASE_URL=postgresql://user:password@localhost/database
DEBUG=TRUE
PATH_FILES=$HOME/DADOS RECEITA/Estabelecimentos
```
## Execução


Primeiro precisamos instalar o projeto:
```bash
pip install -e .
```
*OBS: Você deve estar na raiz do projeto para executar o comando acima.*

### Para executar o projeto, basta rodar o seguinte comando:

```bash
bash execute.sh ${ClassName}
```

Onde `${ClassName}` é o nome da classe que irá ser executada, Exemplo:
```bash
bash execute.sh Establishment
```



O projeto utiliza as seguintes tecnologias:

- Python 3
- PostgreSQL
- SQLAlchemy
- Pandas

Caso haja algum problema na execução do projeto, entre em contato com o desenvolvedor pelo email cto@techpaynmentbrazi.com.br.