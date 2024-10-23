from PIL import Image
#import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from huggingface_hub import login
#login()
# Carregar o modelo pré-treinado ImageGPT


access_token_read = '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'

login(token = access_token_read, add_to_git_credential=True)
model_name = "nlpconnect/imagegpt"  # Substitua pelo nome do modelo se necessário
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def describe_food(image_path):
  """Gera uma descrição textual para uma imagem de comida.

  Args:
    image_path: Caminho para a imagem.

  Returns:
    Uma string contendo a descrição da imagem.
  """

  # Carregar a imagem
  image = Image.open(image_path)

  # Transformar a imagem em um tensor
  inputs = tokenizer(image, return_tensors="pt")

  # Gerar a descrição
  output = model.generate(**inputs)

  # Decodificar a saída
  description = tokenizer.decode(output[0], skip_special_tokens=True)

  return description

# Exemplo de uso
image_path = "C:/Users/david/OneDrive/Área de Trabalho/bife-de-frango-coberto-com-gergelim-branco-ervilhas-tomates-brocolis-e-abobora-em-um-prato-branco-1.jpg" # Substitua pelo caminho da sua imagem
description = describe_food(image_path)
print(description)