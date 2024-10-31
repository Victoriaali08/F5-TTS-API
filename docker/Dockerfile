FROM ghcr.io/swivid/f5-tts:main

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