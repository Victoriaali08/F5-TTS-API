#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author：samge
# date：2024-10-28 13:38
# describe：
import os

# 缓存目录
CACHE_DIR = ".cache"
os.makedirs(CACHE_DIR, exist_ok=True)

# 输出目录
OUTPUT_DIR = f"{CACHE_DIR}/output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 音色目录
MUSIC_DIR = f"{CACHE_DIR}/.music"
os.makedirs(MUSIC_DIR, exist_ok=True)
# 音色列表
MUSIC_NAME_LIST = [name for name in os.listdir(MUSIC_DIR) if name.endswith(".mp3") or name.endswith(".wav")]

# 默认音色
DEFAULT_REF_AUDIO = MUSIC_NAME_LIST[0] if MUSIC_NAME_LIST else None
DEFAULT_REF_TEXT = "TTS Maker是一款免费的文本转语音工具，提供语音合成服务。"

# 音频服务器地址
BASE_URL = os.getenv("F5TTS_BASE_URL") or "http://localhost:17781"
PATH_STATIC_TTS = "/static/tts"

# 音频api简易验证token
F5TTS_AUTH_TOKEN = os.getenv("F5TTS_AUTH_TOKEN") or None