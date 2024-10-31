import os
import config
from fastapi import Depends, FastAPI, HTTPException, Header
from fastapi.responses import FileResponse, StreamingResponse
from typing import Optional
from src.models import InferenceRequest
from src.utils import u_audio

async def verify_token(authorization: str = Header(None)):
    """ token简易验证 """
    if not config.F5TTS_AUTH_TOKEN:
        return
    auth_scheme, _, api_key = (authorization or '').partition(' ')
    if auth_scheme.lower() != "bearer" or api_key != config.F5TTS_AUTH_TOKEN:
        raise HTTPException(status_code=403, detail=f"认证失败")

app = FastAPI(dependencies=[Depends(verify_token)])

# 设置静态文件目录
@app.get(config.PATH_STATIC_TTS + "/{file_name:path}")
async def get_static_file(file_name: str):
    file_path = os.path.join(config.OUTPUT_DIR, file_name)
    if os.path.isfile(file_path):
        return FileResponse(file_path)
    else:
        raise HTTPException(status_code=404, detail="文件未找到")

# 生成tts - post
@app.post("/infer")
async def infer(request: InferenceRequest):
    audio_stream, wav_output_path = await u_audio.generate_audio_stream(request)

    if request.stream:
        response = StreamingResponse(audio_stream, media_type="audio/wav")
        response.headers["Content-Disposition"] = f"inline; filename={os.path.basename(wav_output_path)}"
        return response
    else:
        return {
            "code": 200,
            "msg": "success",
            "data": u_audio.gen_tts_output_url(wav_output_path)
        }

# 生成tts - get
@app.get("/infer")
async def infer_get(
    gen_text: str,
    ref_text: Optional[str] = config.DEFAULT_REF_TEXT,
    ref_file: Optional[str] = config.DEFAULT_REF_AUDIO,
    target_rms: float = 0.1,
    cross_fade_duration: float = 0.15,
    sway_sampling_coef: float = -1,
    cfg_strength: float = 2,
    nfe_step: int = 32,
    speed: float = 1.0,
    fix_duration: Optional[float] = None,
    remove_silence: bool = False,
    seed: Optional[int] = None,
    stream: Optional[bool] = True
):
    request = InferenceRequest(
        gen_text=gen_text,
        ref_text=ref_text,
        ref_file=ref_file,
        target_rms=target_rms,
        cross_fade_duration=cross_fade_duration,
        sway_sampling_coef=sway_sampling_coef,
        cfg_strength=cfg_strength,
        nfe_step=nfe_step,
        speed=speed,
        fix_duration=fix_duration,
        remove_silence=remove_silence,
        seed=seed,
        stream=stream,
    )
    return await infer(request)

# 获取音色信息 - get
@app.get("/ref_config")
def ref_config_get():
    return {
        "code": 200,
        "msg": "success",
        "data": config.MUSIC_NAME_LIST
    }