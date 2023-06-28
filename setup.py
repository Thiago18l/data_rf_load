from setuptools import setup, find_packages



setup(
    name='load_data_rf',
    version='0.0.3',
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


