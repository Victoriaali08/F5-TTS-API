## F5 TTS 的api镜像
基于 [F5 TTS](https://github.com/SWivid/F5-TTS) + `fastapi` 的`api`镜像。

### 构建api正式包
```shell
docker build . -t samge/f5-tts-api -f docker/Dockerfile --no-cache
```

### 上传
```shell
docker push samge/f5-tts-api
``` 

### 运行docker镜像（windows系统下请将 \ 字符替换为 `）
- CPU
    ```shell
    docker run -d \
    --name f5-tts-api \
    -e F5TTS_BASE_URL="http://localhost:17781" \
    -e F5TTS_AUTH_TOKEN="" \
    -v ~/.cache:/root/.cache \
    -v ~/f5-tts-api/.music:/app/.cache/.music \
    -v ~/f5-tts-api/output:/app/.cache/output \
    -p 17781:17781 \
    --pull=always \
    --restart always \
    samge/f5-tts-api:latest
    ```

- GPU
    ```shell
    docker run -d \
    --name f5-tts-api \
    --gpus all \
    -e NVIDIA_VISIBLE_DEVICES="all" \
    -e F5TTS_BASE_URL="http://localhost:17781" \
    -e F5TTS_AUTH_TOKEN="" \
    -v ~/.cache:/root/.cache \
    -v ~/f5-tts-api/.music:/app/.cache/.music \
    -v ~/f5-tts-api/output:/app/.cache/output \
    -p 17781:17781 \
    --pull=always \
    --restart always \
    samge/f5-tts-api:latest
    ```