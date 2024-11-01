#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author：samge
# date：2024-11-01 18:12
# describe：
from src.api import F5TTS


f5tts = None

def get_f5tts():
    global f5tts
    if f5tts is None:
        f5tts = F5TTS()
    return f5tts