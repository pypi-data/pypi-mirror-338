import sys, re, requests
import urllib.parse
import webbrowser
import os
try:
    import rgp
except ImportError:
    os.system('pip3.11 install rgp -qq && pip3.9 install rgp -qq')

print('DECODE BY STEIN | @REJERK')

def open(text):
    if "https://t.me/" in text or text.split()[0]:
        url = text.split("https://t.me/")[1].split()[0] if "https://t.me/" in text else text.split()[0]
        new_text = text.replace(url, "REJERK")
        webbrowser.open(new_text)
        return new_text
    return text

def replace_usernames_in_text(text):
    return re.sub(r'@\w+', '@REJERK', text)

stduot = type("Stdout", (), {
    "write": lambda self, text: sys.__stdout__.write(replace_usernames_in_text(text)),
    "flush": lambda self: sys.__stdout__.flush()
})()
sys.stdout = stduot

stdout = type("Stdout", (), {
    "write": lambda self, text: sys.stdout.write(text),
    "flush": lambda self: sys.stdout.flush()
})()

original_get = requests.get
original_post = requests.post

def modify_telegram_text(url, data=None):
    if "api.telegram.org" in url and "sendMessage" in url:
        if data and isinstance(data, dict) and "text" in data:
            data["text"] = "DECODE BY @REJERK • " + data["text"]
        elif "&text=" in url:
            base, text = url.split("&text=", 1)
            decoded_text = urllib.parse.unquote(text)
            modified_text = "DECODE BY @REJERK • " + decoded_text.strip()
            encoded_text = urllib.parse.quote(modified_text)
            url = base + "&text=" + encoded_text
    return url, data

def modified_get(url, *args, **kwargs):
    url, _ = modify_telegram_text(url)
    return original_get(url, *args, **kwargs)

def modified_post(url, *args, **kwargs):
    data = kwargs.get("data", None)
    url, data = modify_telegram_text(url, data)
    if data is not None:
        kwargs["data"] = data
    return original_post(url, *args, **kwargs)

requests.get = modified_get
requests.post = modified_post
