from django.core.signing import Signer
import base64
import time

def generate_sharex_token(user_id: int):
    signer = Signer()
    return signer.sign(f"sharex:{time.time()}:{user_id}")

def validate_sharex_token(token: str):
    signer = Signer()
    try:
        user_id = signer.unsign(token).split(":")[2]
        return int(user_id)
    except:
        return None