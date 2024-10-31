import hashlib
from src.models import InferenceRequest

def generate_md5(inference_request: InferenceRequest) -> str:
    request_dict = inference_request.model_dump()
    sorted_request_dict = {k: request_dict[k] for k in sorted(request_dict) if k not in ["stream", "remove_silence"]}
    json_bytes = str(sorted_request_dict).encode('utf-8')
    md5_hash = hashlib.md5(json_bytes).hexdigest()
    return md5_hash
