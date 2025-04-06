# Simple Image Processing Package

O pacote `simple_img` é uma biblioteca Python simples para processamento de imagens com base no pacote skimage. Ele oferece funcionalidades básicas, como redimensionamento, conversão para tons de cinza e aplicação de filtros.

## Funcionalities

- Redimensionar imagens para um tamanho específico.
- Converter imagens para escala de cinza.
- Aplicar filtros básicos como desfoque e nitidez.

## Installation

Use o gerenciador de pacotes [pip](https://pip.pypa.io/en/stable/) para instalar o `simple_img`:

```bash
pip install simple_img

## Usage

from simple_img.processing import resize_image, apply_grayscale

# Redimensionar uma imagem
resize_image("imagem_entrada.jpg", "imagem_saida_redimensionada.jpg", (200, 200))

# Converter uma imagem para tons de cinza
apply_grayscale("imagem_entrada.jpg", "imagem_saida_cinza.jpg")
```

## Author
Filipe L

## License
[MIT](https://choosealicense.com/licenses/mit/)