from .job.run import run
from .database.session import get_session
import os
import glob
import argparse
from dotenv import load_dotenv

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(BASE_DIR, '.env'), verbose=True)

database_url = os.getenv('DATABASE_URL')
debug = os.getenv('DEBUG') == 'True'
path_files = os.getenv('PATH_FILES')

def main():
    PATH = os.getenv('PATH_FILES')
    CSV_FILES = glob.glob(PATH + "/*.csv")
    parser = argparse.ArgumentParser()
    parser.add_argument('class_name', type=str, help='Insira o nome da classe para inserir no banco')
    args = parser.parse_args()
    instance = get_session()
    run(CSV_FILES, args.class_name, instance)

if __name__ == '__main__':
    main()
    