# Imagen base
FROM samge/f5-tts:v20241101-main-2a3deaa

# Configuración de localización
ENV LANG=zh_CN.UTF-8
ENV LANGUAGE=zh_CN:zh
ENV LC_ALL=zh_CN.UTF-8

# Definir el directorio de trabajo
WORKDIR /app

# Copiar todos los archivos al contenedor
COPY . .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto correcto
EXPOSE 17781

# Definir volúmenes en directorios escribibles
VOLUME [ "/tmp/cache", "/tmp/output", "/tmp/music" ]

# Configurar la variable PYTHONPATH
RUN echo "export PYTHONPATH=/app" >> ~/.bashrc
ENV PYTHONPATH=/app

# Ejecutar la aplicación
CMD ["python", "main.py"]
