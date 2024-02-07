# Usa una imagen base de Python
FROM python:3.9

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo requirements.txt al contenedor
COPY requirements.txt .

# Instala las dependencias del proyecto
RUN pip install -r requirements.txt

# Copia todos los archivos del directorio actual al contenedor en /app
COPY . .

# Expone el puerto 8501 para Streamlit
EXPOSE 8501

# Comando para ejecutar la aplicación cuando se inicie el contenedor
CMD ["streamlit", "run", "app.py"]

