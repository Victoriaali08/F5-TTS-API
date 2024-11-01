# 这个是官方的main分支docker镜像：https://github.com/swivid/F5-TTS/pkgs/container/f5-tts
# 如果需要使用这个官方镜像，需要动态复制最新的 https://github.com/SWivid/F5-TTS/blob/main/src/f5_tts/api.py 内容替换到 `src/api.py`，不然可能存在兼容问题
# FROM ghcr.io/swivid/f5-tts:main


# 因为官方mian分支的docekr镜像更新频繁，遂改用转存后的docker镜像，避免新旧版本的函数调用冲突
# 转存版本列表：https://hub.docker.com/r/samge/f5-tts/tags
FROM samge/f5-tts:v20241101-main-2a3deaa

ENV LANG=zh_CN.UTF-8
ENV LANGUAGE=zh_CN:zh
ENV LC_ALL=zh_CN.UTF-8

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 17781

VOLUME [ "/root/.cache", "/app/.cache", "/app/.cache/.music", "/app/.cache/output" ]

RUN echo "export PYTHONPATH=/app" >> ~/.bashrc
ENV PYTHONPATH=/app

CMD ["python", "main.py"]