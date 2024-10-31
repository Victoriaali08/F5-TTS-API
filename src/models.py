from pydantic import BaseModel
from typing import Optional
import config

# tts请求参数
class InferenceRequest(BaseModel):
    gen_text: str
    ref_text: Optional[str] = config.DEFAULT_REF_TEXT
    ref_file: Optional[str] = config.DEFAULT_REF_AUDIO
    target_rms: float = 0.1
    cross_fade_duration: float = 0.15
    sway_sampling_coef: float = -1
    cfg_strength: float = 2
    nfe_step: int = 32
    speed: float = 1.0
    fix_duration: Optional[float] = None
    remove_silence: bool = False
    seed: Optional[int] = None
    stream: Optional[bool] = True
