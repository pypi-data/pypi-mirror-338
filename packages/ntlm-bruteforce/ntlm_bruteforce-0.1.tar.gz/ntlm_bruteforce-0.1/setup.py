from setuptools import setup, find_packages

setup(
    name="ntlm_bruteforce",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        # Liste des dépendances externes si nécessaire
    ],
    entry_points={
        'console_scripts': [
            'ntml=ntlm_bruteforce.ntlm_bruteforce:main',  # Commande CLI principale
        ],
    },
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author="Noloxoyt",
    author_email="noloxoyt@hotmail.com",
    description="Librairie Python pour bruteforce NTLM hash",
    url="https://github.com/noloxoyt/ntlm_bruteforce",
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
