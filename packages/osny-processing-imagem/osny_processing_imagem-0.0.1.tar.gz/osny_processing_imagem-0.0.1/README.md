# Processamento de Imagens com Python

Descrição: 

O pacote é usado para:
	
    Processing: 
	- Histogram matching
	- Structural similarity
	- Resize image

	Utils:
	- Read image
	- Save image
	- Plot image
	- Plot result
	- Plot histogram

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install processamento-imagens-com-python

```bash
# Boas Práticas
# Primeiro fazer o upgrade do pip e programas utilizados

python -m pip install --upgrade pip, twine, setuptools
python -m pip --user twine
python -m pip --user setuptools

# Instalando o pacote

pip install processamento-imagens-com-python
```

## Comando para criar as distribuições
```bash
python setup.py sdist bdist_wheel

```
## Comando para fazer o deploy do projeto no pyTest

```bash
python -m twine upload --repository testpypi dist/*
```
## Comando para fazer o deploy do projeto no PyPi

```bash
python -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
```

### Uso

```python
# Exemplos de utilização
from processamento-imagens-com-python.processing import combination, transformation
    # opção 1
    combination.find_difference(image1,image2)
    # opção 2
    combination.transfer_histogram(image1,image2)
    # opção 3
    transformation.resize_image(image,proportion)
```

## Author
Osny Neto

## Github
💻 [GituHub](https://github.com/OsnyNeto/Programas_Python/tree/main/processamento_imagens_com_python)

## License
[MIT](https://choosealicense.com/licenses/mit/)