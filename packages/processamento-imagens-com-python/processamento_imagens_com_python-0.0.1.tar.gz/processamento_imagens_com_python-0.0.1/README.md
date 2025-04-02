# processamento_imagens_com_python

Description. 
The package processamento_imagens_com_python is used to:
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

### Comandos de instalação (Boas práticas)
```bash
python -m pip install --upgrade pip
python -m pip install --user twine
python -m pip install --user setuptools
```
### Comandos para criar as distribuições
```bash
python setup.py sdist bdist_wheel
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install processamento_imagens_com_python

```bash
pip install processamento_imagens_com_python
```

## Usage

```python
from processamento_imagens_com_python.processing import combination
	Encontra diferença entre duas imagens
		processing.find_difference(image1,image2)

	Aplica o histogram da segunda imagem a primeira imagem
		processing.transfer_histogram(image1, image2)
	
	Normaliza as imagens
		processing.resize_image(image, proportion)
```

## Author
Osny

## License
[MIT](https://choosealicense.com/licenses/mit/)