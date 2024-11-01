import os
import random
import sys
from io import BytesIO
import soundfile as sf
import config
from src.models import InferenceRequest
from src.utils import u_api, u_common

# 组装tts的http链接
def gen_tts_output_url(filepath: str) -> str:
    return f"{config.BASE_URL}{config.PATH_STATIC_TTS}/{os.path.basename(filepath)}"

# 生成tts数据
async def generate_audio_stream(request: InferenceRequest):
    
    f5tts = u_api.get_f5tts()

    # Set a random seed if not provided
    if request.seed is None:
        request.seed = random.randint(0, sys.maxsize)
    print(f"当前使用的音色种子：{request.seed}")
        
    param_md5 = u_common.generate_md5(request)
    wav_output_path = f"{config.OUTPUT_DIR}/{param_md5}.wav"
    
    if not request.refresh and os.path.exists(wav_output_path):
        # 如果文件已经存在，检查文件是否可播放
        print("音频文件已存在，检查文件是否可播放")
        try:
            # 尝试打开音频文件
            wav, sr = sf.read(wav_output_path)
            # 检查音频数据是否有效（例如，不为空）
            if len(wav) > 0 and request.stream:
                audio_stream = BytesIO()
                sf.write(audio_stream, wav, sr, format='WAV')
                audio_stream.seek(0)  # Reset stream position for reading
                return audio_stream, wav_output_path
            elif len(wav) > 0:
                return None, wav_output_path
            else:
                print("音频文件存在但为空，需要重新生成")
        except Exception as e:
            print(f"音频文件存在但无法读取或解析：{e}，需要重新生成")
    
    # 如果文件不存在或损坏，生成音频
    print("音频文件不存在或损坏，开始生成")
    wav, sr, spect = f5tts.infer(
        ref_file=request.ref_file,
        ref_text=request.ref_text,
        gen_text=request.gen_text,
        target_rms=request.target_rms,
        cross_fade_duration=request.cross_fade_duration,
        sway_sampling_coef=request.sway_sampling_coef,
        cfg_strength=request.cfg_strength,
        nfe_step=request.nfe_step,
        speed=request.speed,
        fix_duration=request.fix_duration,
        remove_silence=request.remove_silence,
        file_wave=wav_output_path,  
        file_spect=None,  # We won't save spectrogram directly
        seed=request.seed
    )

    if request.stream:
        # Create an in-memory BytesIO stream
        audio_stream = BytesIO()
        sf.write(audio_stream, wav, sr, format='WAV')
        audio_stream.seek(0)  # Reset stream position for reading
        return audio_stream, wav_output_path
    else:
        return None, wav_output_path
