import requests  # cloudflare verify call ke liye
import os  # env secret read karne ke liye


def verify_turnstile(token, ip=None):  # token frontend se aata hai
    secret = os.getenv("TURNSTILE_SECRET_KEY")  # .env se secret key

    if not token:  # token missing
        return False

    try:
        response = requests.post(
            "https://challenges.cloudflare.com/turnstile/v0/siteverify",
            data={
                "secret": secret,  # secret key
                "response": token,  # frontend token
                "remoteip": ip  # optional
            },
            timeout=5
        )

        result = response.json()  # cloudflare response
        return result.get("success", False)  # success true/false

    except Exception:
        return False
