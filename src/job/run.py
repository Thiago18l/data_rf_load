import pandas as pd
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy import exc
import importlib
from src.utils import utils
from src.utils.log.log import Logger

logging = Logger()


CHUNK_SIZE=50000
pd.options.mode.chained_assignment = None  # default='warn'
pd.options.mode.use_inf_as_na = True  # default=False

def run(csv_files: list, class_name: str, session):
    # Obter o caminho para o módulo e a classe a partir do nome da classe
    module_path = f"src.model.{class_name.lower()}"
    class_name = class_name.capitalize()

    # Importar a classe dinamicamente
    module = importlib.import_module(module_path)
    class_obj = getattr(module, class_name)
    dtype = utils.get_dtypes(class_name)
    columns = utils.get_columns(class_name)

    for csv_file in csv_files:
        if class_name == 'Lucro':
            reader = pd.read_csv(csv_file, sep=',', header=None, chunksize=CHUNK_SIZE, on_bad_lines='skip', dtype=dtype, 
                            na_values=['NULL', " "], keep_default_na=False, low_memory=False, encoding='latin1')
        else:
            # Cria uma instância do DataFrameReader
            reader = pd.read_csv(csv_file, sep=';', header=None, chunksize=CHUNK_SIZE, on_bad_lines='skip', dtype=str, 
                            na_values=['NULL', " "], keep_default_na=False, low_memory=False, encoding='latin1')


        # Define o número de chunks processados
        chunk_count = 0
        count = 0

        # Itera sobre os chunks do arquivo
        for chunk in reader:
            chunk = chunk.rename(columns=columns)
            # Converte o chunk do DataFrame em uma lista de dicionários
            records = chunk.to_dict('records')
            # Insere os registros no banco de dados em lotes
            
            try:
                with session.begin_nested():
                    session.bulk_insert_mappings(class_obj, records, render_nulls=True)
                    session.commit()
                    chunk_count += 1
                    logging.info(f"{chunk_count} Chunk Processadas com sucesso")
            except exc.IntegrityError as e:
                count += 1
                logging.error(f"A chunk {count} foi pulada por já existir no banco")
                session.rollback()
                continue
