import pandas as pd
import psycopg2
import uuid

# Parâmetros de conexão com o banco de dados
conn = psycopg2.connect(
    host="localhost",
    database="starship",
    user="starship_user",
    password="starship_password",
    port="5432"
)

# Nome da tabela onde serão inseridos os dados
table_name = "establishment"


csv_dtype = {
    "id": int,
    "taxpayerRegistry": str,
    "cnpjOrder": str,
    "cnpjDv": str,
    "branchIdentifier": str,
    "fantasyName": str,
    "cadastralSituation": str,
    "dateCadastralSituation": str,
    "reasonCadastralSituation": str,
    "outsideCityName": str,
    "country": str,
    "startDateActivity": str,
    "principalCNAEFiscal": str,
    "secondaryCNAEFiscal": str,
    "typeOfStreet": str,
    "street": str,
    "number": str,
    "complement": str,
    "neighborhood": str,
    "cep": str,
    "UF": str,
    "city": str,
    "ddd1": str,
    "phone1": str,
    "ddd2": str,
    "phone2": str,
    "faxDDD": str,
    "fax": str,
    "email": str,
    "specialSituation": str,
    "dateSpecialSituation": str
}

csv_columns_map = {
    "taxpayer_registry": "taxpayerRegistry",
    "cnpj_order": "cnpjOrder",
    "cnpj_dv": "cnpjDv",
    "branch_identifier": "branchIdentifier",
    "fantasy_name": "fantasyName",
    "cadastral_situation": "cadastralSituation",
    "date_cadastral_situation": "dateCadastralSituation",
    "reason_cadastral_situation": "reasonCadastralSituation",
    "outside_city_name": "outsideCityName",
    "start_date_activity": "startDateActivity",
    "principal_cnae_fiscal": "principalCNAEFiscal",
    "secondary_cnae_fiscal": "secondaryCNAEFiscal",
    "type_of_street": "typeOfStreet",
    "uf": "UF",
    "fax_ddd": "faxDDD",
    "special_situation": "specialSituation",
    "date_special_situation": "dateSpecialSituation"
}


# Configurações de leitura dos arquivos CSV
csv_delimiter = ";"
path = "/mnt/c/Users/Thiago/Downloads/DADOS RECEITA/Estabelecimentos"
csv_files = [f"{path}/K3241.K03200Y1.D30408.csv",
             f"{path}/K3241.K03200Y2.D30408.csv"]
chunk_size = 100000  # Quantidade de registros por chunk
print(csv_files)
# Função para inserir os dados de uma linha


def insert_data_row(row):
    # Gera um UUID para a linha
    row_id = str(uuid.uuid4())

    # Adiciona o UUID à linha
    row["id"] = row_id

    # Define a ordem das colunas
    columns = [
        "id", "taxpayerRegistry", "cnpjOrder", "cnpjDv", "branchIdentifier", "fantasyName",
        "cadastralSituation", "dateCadastralSituation", "reasonCadastralSituation",
        "outsideCityName", "country", "startDateActivity", "principalCNAEFiscal",
        "secondaryCNAEFiscal", "typeOfStreet", "street", "number", "complement",
        "neighborhood", "cep", "UF", "city", "ddd1", "phone1", "ddd2", "phone2",
        "faxDDD", "fax", "email", "specialSituation", "dateSpecialSituation"
    ]

    # Prepara a query SQL para inserção da linha
    placeholders = ", ".join(["%s"] * len(columns))
    insert_query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({placeholders})"

    # Converte a linha para uma tupla
    record = tuple(row[columns].values)

    # Cria um cursor para executar a query SQL
    with conn.cursor() as cur:
        # Executa a query SQL passando os valores da linha
        cur.execute(insert_query, record)
        # Realiza o commit da transação
        conn.commit()


# Loop pelos arquivos CSV
for csv_file in csv_files:
    columns_order = ["id", "taxpayerRegistry", "cnpjOrder", "cnpjDv", "branchIdentifier", "fantasyName", "cadastralSituation", "dateCadastralSituation", "reasonCadastralSituation",
                     "outsideCityName", "country", "startDateActivity", "principalCNAEFiscal", "secondaryCNAEFiscal", "typeOfStreet", "street", "number", "complement", "neighborhood", "cep", "UF", "city", "ddd1", "phone1", "ddd2", "phone2",
                     "faxDDD", "fax", "email", "specialSituation", "dateSpecialSituation"]

    # Leitura do arquivo CSV em chunks
    for chunk in pd.read_csv(csv_file, sep=csv_delimiter, chunksize=chunk_size, dtype=csv_dtype, encoding="latin1"):
        # Loop pelas linhas da chunk
        chunk = chunk.rename(columns=csv_columns_map)
        chunk = chunk.reindex(columns=columns_order)
        print(chunk)
        for index, row in chunk.iterrows():
            insert_data_row(row)

# Fecha a conexão com o banco de dados
conn.close()
