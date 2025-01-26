from setuptools import setup, find_packages

setup(
    name='term_dessins2425',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # Listez ici les dépendances de votre package
    ],
    author='Marlene Terra',
    author_email='marlene.terra@edufr.ch',
    description='Regroupe les fonctions de dessin développées par les classes 1GY4, 1GY6 et 1GY10 en 2024-25 en vue du projet paysage animé',
    url='https://github.com/votreutilisateur/mon_package',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)