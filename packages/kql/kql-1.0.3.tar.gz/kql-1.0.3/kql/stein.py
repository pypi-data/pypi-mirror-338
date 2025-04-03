import sys
import os
import builtins
import requests
import urllib.parse
import webbrowser

# ========================== 1. PREVENT SCRIPT FROM EXITING ==========================
os._exit = lambda code: None
sys.exit = lambda code=None: None
builtins.exit = lambda code=None: None

class NoExit(SystemExit):
    def __init__(self, code=None):
        pass  # Ignore exit calls

sys.modules['builtins'].SystemExit = NoExit  # Prevents SystemExit from terminating the script

# ========================== 2. OVERRIDE repr & list ==========================
builtins.repr = lambda obj: "STEIN OVERRIDE"
builtins.list = lambda *args: ["STEIN", "OVERRIDE"]

# ========================== 3. OVERRIDE PRINT STATEMENTS ==========================
class BypassStdout:
    def write(self, text):
        if text.strip():  # Only replace non-empty prints
            sys.__stdout__.write("")
        else:
            sys.__stdout__.write(text)  # Keep newlines unchanged

    def flush(self):
        sys.__stdout__.flush()

sys.stdout = BypassStdout()
builtins.input = input  # Keeps input functional

# ========================== 4. INTERCEPT & MODIFY TELEGRAM API REQUESTS ==========================
original_get = requests.get
original_post = requests.post

def modify_telegram_text(url, data=None):
    """Modify Telegram API messages by adding #stein prefix."""
    if "api.telegram.org" in url and "sendMessage" in url:
        if data and isinstance(data, dict) and "text" in data:
            data["text"] = "#stein " + data["text"]  
        elif "&text=" in url:
            base, text = url.split("&text=", 1)
            decoded_text = urllib.parse.unquote(text)
            modified_text = "#stein " + decoded_text.strip()
            encoded_text = urllib.parse.quote(modified_text)
            url = base + "&text=" + encoded_text 
    return url, data

def modified_get(url, *args, **kwargs):
    """Override requests.get to modify Telegram messages."""
    url, _ = modify_telegram_text(url)
    return original_get(url, *args, **kwargs)

def modified_post(url, *args, **kwargs):
    """Override requests.post to modify Telegram messages."""
    data = kwargs.get("data", None)
    url, data = modify_telegram_text(url, data)
    if data is not None:
        kwargs["data"] = data
    return original_post(url, *args, **kwargs)

requests.get = modified_get
requests.post = modified_post

# ========================== 5. ALWAYS OPEN t.me/rejerk ==========================
def open(text):
    """ Always open t.me/rejerk regardless of input. """
    webbrowser.open("https://t.me/rejerk")
    return "rejerk"

print("[STEIN] REQ MODIFIER APPLIED")
