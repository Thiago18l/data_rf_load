import psycopg2
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import csv
from sqlalchemy import create_engine, Column, String, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import uuid
from sqlalchemy.dialects.postgresql import UUID
import _csv
import chardet
# Conexão com o banco de dados

host = "localhost",
database = "starship",
user = "starship_user",
password = "starship_password",
port = "5432"

path = "/mnt/c/Users/Thiago/Downloads/DADOS RECEITA/Estabelecimentos"
csv_files = [f"{path}/K3241.K03200Y2.D30408.csv"]


# Define a base para as classes de modelo
Base = declarative_base()

# Define a classe que representa a tabela "establishments"


class Establishment(Base):
    __tablename__ = 'establishment'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    taxpayerRegistry = Column(String, unique=True, nullable=True)
    cnpjOrder = Column(String, nullable=True)
    cnpjDv = Column(String, nullable=True)
    branchIdentifier = Column(String, nullable=True)
    fantasyName = Column(String, nullable=True)
    cadastralSituation = Column(String, nullable=True)
    dateCadastralSituation = Column(String, nullable=True)
    reasonCadastralSituation = Column(String, nullable=True)
    outsideCityName = Column(String, nullable=True)
    country = Column(String, nullable=True)
    startDateActivity = Column(String, nullable=True)
    principalCNAEFiscal = Column(String, nullable=True)
    secondaryCNAEFiscal = Column(String, nullable=True)
    typeOfStreet = Column(String, nullable=True)
    street = Column(String, nullable=True)
    number = Column(String, nullable=True)
    complement = Column(String, nullable=True)
    neighborhood = Column(String, nullable=True)
    cep = Column(String, nullable=True)
    UF = Column(String, nullable=True)
    city = Column(String, nullable=True)
    ddd1 = Column(String, nullable=True)
    phone1 = Column(String, nullable=True)
    ddd2 = Column(String, nullable=True)
    phone2 = Column(String, nullable=True)
    faxDDD = Column(String, nullable=True)
    fax = Column(String, nullable=True)
    email = Column(String, nullable=True)
    specialSituation = Column(String, nullable=True)
    dateSpecialSituation = Column(String, nullable=True)


# Cria uma engine para conectar ao banco de dados
engine = create_engine(
    f'postgresql://starship_user:starship_password@0.0.0.0:{port}/starship')
print(engine)
# Cria uma sessão para interagir com o banco de dados
Session = sessionmaker(bind=engine)
session = Session()


def convert_row_to_dict(row):
    return {
        'taxpayerRegistry': row[0].replace('"', ''),
        'cnpjOrder': row[1].replace('"', '') if len(row) > 1 else '',
        'cnpjDv': row[2].replace('"', '') if len(row) > 2 else '',
        'branchIdentifier': row[3].replace('"', '') if len(row) > 3 else '',
        'fantasyName': row[4].replace('"', '') if len(row) > 4 else '',
        'cadastralSituation': row[5].replace('"', '') if len(row) > 5 else '',
        'dateCadastralSituation': row[6].replace('"', '') if len(row) > 6 else '',
        'reasonCadastralSituation': row[7].replace('"', '') if len(row) > 7 else '',
        'outsideCityName': row[8].replace('"', '') if len(row) > 8 else '',
        'country': row[9].replace('"', '') if len(row) > 9 else '',
        'startDateActivity': row[10].replace('"', '') if len(row) > 10 else '',
        'principalCNAEFiscal': row[11].replace('"', '') if len(row) > 11 else '',
        'secondaryCNAEFiscal': row[12].replace('"', '') if len(row) > 12 else '',
        'typeOfStreet': row[13].replace('"', '') if len(row) > 13 else '',
        'street': row[14].replace('"', '') if len(row) > 14 else '',
        'number': row[15].replace('"', '') if len(row) > 15 else '',
        'complement': row[16].replace('"', '') if len(row) > 16 else '',
        'neighborhood': row[17].replace('"', '') if len(row) > 17 else '',
        'cep': row[18].replace('"', '') if len(row) > 18 else '',
        'UF': row[19].replace('"', '') if len(row) > 19 else '',
        'city': row[20].replace('"', '') if len(row) > 20 else '',
        'ddd1': row[21].replace('"', '') if len(row) > 21 else '',
        'phone1': row[22].replace('"', '') if len(row) > 22 else '',
        'ddd2': row[23].replace('"', '') if len(row) > 23 else '',
        'phone2': row[24].replace('"', '') if len(row) > 24 else '',
        'faxDDD': row[25].replace('"', '') if len(row) > 25 else '',
        'fax': row[26].replace('"', '') if len(row) > 26 else '',
        'email': row[27].replace('"', '') if len(row) > 27 else '',
        'especialSituation': row[28].replace('"', '') if len(row) > 28 else '',
        'dateSpecialSituation': row[29].replace('"', '') if len(row) > 29 else ''
    }


# Loop over CSV files
for csv_file in csv_files:
    # Abra o arquivo CSV
    with open(csv_file, 'r', encoding="latin1") as file:
        reader = csv.reader(file, delimiter=';')

        # Pule o cabeçalho
        next(reader)

        chunk_size = 50000
        chunk_count = 0
        while True:
            rows = []
            for idx, row in enumerate(reader):
                if ('NUL' in row):
                    print(f"AQUI {idx + 1}")
                if '\0' in ''.join(row):
                    print("ENTREI")
                    print(f"Ignorando linha {idx + 1} com erro de decodificação")
                    continue
                try:
                    if idx >= chunk_size:
                        break
                    rows.append(tuple(field.replace('"', '') for field in row))
                except _csv.Error:
                    print(
                        f"Ignorando linha {idx + 1} com erro de decodificação")
                    continue

            # Verifique se há mais linhas para serem processadas
            if not rows:
                break
            rows = [convert_row_to_dict(row) for row in rows]

            try:
                session.bulk_insert_mappings(
                    Establishment, rows, render_nulls=True)
                session.commit()
                chunk_count += 1
                print(f"{chunk_count} Chunk Processadas")
            except psycopg2.errors.UniqueViolation as e:
                print(f"Chave única duplicada: {e}")
                session.rollback()
                continue
            finally:
                del rows


# Fechar a conexão com o banco de dados
