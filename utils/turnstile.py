import requests
import os


def verify_turnstile(token, ip=None):
    secret = os.getenv("TURNSTILE_SECRET_KEY")

    # secret missing guard
    if not secret:
        print("TURNSTILE_SECRET_KEY not set")
        return False

    if not token:
        return False

    try:
        response = requests.post(
            "https://challenges.cloudflare.com/turnstile/v0/siteverify",
            data={
                "secret": secret,
                "response": token,
                "remoteip": ip
            },
            timeout=5
        )

        # response safe parse
        result = response.json() if response.content else {}

        return result.get("success", False)

    except requests.RequestException as e:
        print("Turnstile request error:", e)
        return False
