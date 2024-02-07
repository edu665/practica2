import torch
from PIL import Image
from transformers import AutoTokenizer, AutoModelForImageGeneration, AutoModelForImageClassification

def generate_image(text_input):
    # Cargar el tokenizador y el modelo pre-entrenado para generación de imágenes
    tokenizer = AutoTokenizer.from_pretrained("modelo_generacion_de_imagenes")
    model = AutoModelForImageGeneration.from_pretrained("modelo_generacion_de_imagenes")

    # Tokenizar el texto de entrada
    inputs = tokenizer(text_input, return_tensors="pt", padding=True, truncation=True)

    # Generar la imagen
    with torch.no_grad():
        output = model.generate(**inputs)

    # Decodificar la imagen generada
    generated_image = Image.open(output)
    return generated_image

def classify_image(image_file):
    # Cargar el modelo pre-entrenado para clasificación de imágenes
    model = AutoModelForImageClassification.from_pretrained("modelo_clasificacion_de_imagenes")

    # Preprocesar la imagen
    image = Image.open(image_file)
    image = image.resize((224, 224))  # Ajustar tamaño de imagen según modelo pre-entrenado
    image = image.convert("RGB")      # Convertir a formato RGB
    image = torch.tensor(image).permute(2, 0, 1)  # Convertir a tensor y ajustar formato

    # Realizar la clasificación de la imagen
    with torch.no_grad():
        outputs = model(image.unsqueeze(0))  # Añadir dimensión de lote

    # Obtener la etiqueta predicha
    predicted_label = torch.argmax(outputs.logits, dim=1).item()
    # Aquí puedes mapear el índice de la etiqueta predicha a la etiqueta real si es necesario

    return predicted_label
