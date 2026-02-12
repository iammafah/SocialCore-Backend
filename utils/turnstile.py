import requests
import os


def verify_turnstile(token, ip=None):
    secret = os.getenv("TURNSTILE_SECRET_KEY")

    if not secret:
        print("TURNSTILE_SECRET_KEY missing")
        return False

    try:
        response = requests.post(
            "https://challenges.cloudflare.com/turnstile/v0/siteverify",
            data={
                "secret": secret,
                "response": token
            },
            timeout=5
        )

        result = response.json()
        print("TURNSTILE RESULT:", result)

        return result.get("success", False)

    except Exception as e:
        print("TURNSTILE ERROR:", e)
        return False
