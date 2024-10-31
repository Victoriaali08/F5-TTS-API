## F5 TTS 的api

基于 [F5 TTS](https://github.com/SWivid/F5-TTS) + `fastapi` 的`api`。

提示：首次运行会自动`下载模型`文件+`加载模型`，这步骤稍微有点`耗时`，可在运行日志中查看模型下载+加载状态。模型默认下载到容器的`/root/.cache`的目录下，使用docker方式运行时记得映射该目录。


### 下载[参考音色](https://github.com/Samge0/ttsmaker-download/releases/tag/v0.0.1)到项目根路径下的`.cache/.music`目录（需要梯子）
 
<details> <summary>点击展开>></summary>

- linux/mac环境：
    ```shell
    chmod +x scripts/download_maker_tts.sh

    sh scripts/download_maker_tts.sh
    ```

- windows环境：

    手动下载[参考音色](https://github.com/Samge0/ttsmaker-download/releases/tag/v0.0.1)并将`output`下的音色文件解压到项目根路径下的`.cache/.music`目录
    
</details>


### [docker方式运行>>](docker/README.md)

- GPU
    ```shell
    docker compose -f docker/docker-compose-gpu.yml -p f5ttsapi up -d --build
    ```
    
- CPU
    ```shell
    docker compose -f docker/docker-compose.yml -p f5ttsapi up -d --build
    ```

### 调用

 [http://localhost:17781/infer?seed=1&stream=1&refresh=0&gen_text=hi我是samge，欢迎使用语音克隆服务](http://localhost:17781/infer?seed=1&stream=1&refresh=0&gen_text=hi我是samge，欢迎使用语音克隆服务)


### [可选] 本地调试

<details> <summary>点击展开>></summary>
- 克隆项目&进入项目根路径

- 使用[Vscode 的 Dev Container](.devcontainer/README.md)方式进入容器环境

- 运行
    ```shell
    python main.py
    ```
</details>
