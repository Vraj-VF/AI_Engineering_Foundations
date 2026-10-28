import json
import os
import time
from urllib.parse import urlparse


def api_call(url, method="GET", headers=None, body=None):
    parsed = urlparse(url)
    if parsed.scheme not in ("http", "https") or not parsed.netloc:
        raise ValueError("URL must be HTTP or HTTPS")
    try:
        import requests
    except ImportError:
        return {
            "url": url,
            "method": method,
            "fallback": True,
            "message": "Install requests for live calls",
        }
    for attempt in range(3):
        try:
            response = requests.request(method.upper(), url, headers=headers, json=body, timeout=10)
            response.raise_for_status()
            return response.json()
        except Exception:
            if attempt == 2:
                raise
            time.sleep(2**attempt)


def main():
    url = os.getenv("API_URL", "https://api.github.com")
    print(json.dumps(api_call(url), indent=2)[:2000])


if __name__ == "__main__":
    main()
