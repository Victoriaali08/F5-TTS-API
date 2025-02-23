#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: samge
# Date: 2024-10-28 13:38
# Description: Configuración para almacenamiento de archivos en F5-TTS

import os

# Definir directorio de caché en una ruta escribible
CACHE_DIR = "/tmp/cache"
os.makedirs(CACHE_DIR, exist_ok=True)

# Directorio de salida
OUTPUT_DIR = f"{CACHE_DIR}/output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Directorio de música
MUSIC_DIR = f"{CACHE_DIR}/music"
os.makedirs(MUSIC_DIR, exist_ok=True)

# Lista de archivos de música disponibles
MUSIC_NAME_LIST = [
    name for name in os.listdir(MUSIC_DIR) if name.endswith(".mp3") or name.endswith(".wav")
]

# Seleccionar el primer archivo como referencia si hay disponibles
DEFAULT_REF_AUDIO = MUSIC_NAME_LIST[0] if MUSIC_NAME_LIST else None
DEFAULT_REF_TEXT = "TTS Maker es una herramienta gratuita de conversión de texto a voz."

# Configuración del servidor de audio
BASE_URL = os.getenv("F5TTS_BASE_URL", "http://localhost:17781")
PATH_STATIC_TTS = "/static/tts"

# Token de autenticación para API
F5TTS_AUTH_TOKEN = os.getenv("F5TTS_AUTH_TOKEN", None)
