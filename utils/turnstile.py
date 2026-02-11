import requests
import os


def verify_turnstile(token, ip=None):
    secret = os.getenv("TURNSTILE_SECRET_KEY")

    if not secret:
        print("TURNSTILE_SECRET_KEY not set")
        return False

    if not token:
        print("TURNSTILE TOKEN MISSING")
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

        result = response.json() if response.content else {}

        # DEBUG OUTPUT
        print("TURNSTILE VERIFY RESULT:", result)

        return result.get("success", False)

    except requests.RequestException as e:
        print("Turnstile request error:", e)
        return False
