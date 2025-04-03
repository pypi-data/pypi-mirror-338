import sys
import os
import builtins
import requests
import urllib.parse
import webbrowser

# ========================== 1. PREVENT SCRIPT FROM EXITING ==========================
def prevent_exit():
    os._exit = lambda code: None
    sys.exit = lambda code=None: None
    builtins.exit = lambda code=None: None

    class NoExit(SystemExit):
        def __init__(self, code=None):
            pass  # Ignore exit calls

    sys.modules['builtins'].SystemExit = NoExit  # Prevents SystemExit from terminating the script

prevent_exit()

# ========================== 2. OVERRIDE repr & list ==========================
def override_repr():
    builtins.repr = lambda obj: "KQL OVERRIDE"

def override_list():
    builtins.list = lambda *args: ["KQL", "OVERRIDE"]

override_repr()
override_list()

# ========================== 3. INTERCEPT & MODIFY TELEGRAM API REQUESTS ==========================
original_get = requests.get
original_post = requests.post

def modify_telegram_text(url, data=None):
    """Modify Telegram API messages by adding #KQL prefix."""
    if "api.telegram.org" in url and "sendMessage" in url:
        if data and isinstance(data, dict) and "text" in data:
            data["text"] = "#KQL " + data["text"]  
        elif "&text=" in url:
            base, text = url.split("&text=", 1)
            decoded_text = urllib.parse.unquote(text)
            modified_text = "#KQL " + decoded_text.strip()
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

def modify_requests():
    requests.get = modified_get
    requests.post = modified_post

modify_requests()

# ========================== 4. ALWAYS OPEN t.me/rejerk ==========================
def custom_open(text):
    """ Always open t.me/rejerk regardless of input. """
    webbrowser.open("https://t.me/rejerk")
    return "rejerk"

print("[KQL] REQ MODIFIER APPLIED")
