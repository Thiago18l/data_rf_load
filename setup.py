from dotenv import load_dotenv
import os
from setuptools import setup, find_packages

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
print(BASE_DIR)
load_dotenv(os.path.join(BASE_DIR, '.env'), verbose=True)





database_url = os.getenv('DATABASE_URL')
print(database_url)
debug = os.getenv('DEBUG') == 'True'
path_files = os.getenv('PATH_FILES')
print(path_files)

setup(
    name='load_data_rf',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'python-dotenv',
        'sqlalchemy',
        'pandas'
    ],
    entry_points={
        'console_scripts': [
            'run=src:main'
        ]
    }
)

def run():
    from src import main
    main()


