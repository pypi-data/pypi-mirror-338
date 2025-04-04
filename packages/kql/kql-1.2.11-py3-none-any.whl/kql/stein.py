import sys, os, re, requests
import urllib.parse
import webbrowser

print('DECODE BY STEIN | @REJERK')

repr = lambda *args: f"{args}"
list = lambda *args: f"{args}"

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

# Bypass sys.exit and os._exit
def fake_exit(*args, **kwargs):
    print("#BYPASSED BY STEIN")

def fake_os_exit(*args, **kwargs):
    print("#BYPASSED BY STEIN")

# Store original request functions
original_get = requests.get
original_post = requests.post

# Telegram API text interceptor
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

# Handle GitHub raw URL prompt
def handle_raw_github_url(url: str) -> str:
    if url.startswith("https://raw.githubusercontent.com/"):
        print(f"\n[RAW GITHUB REQUEST DETECTED]")
        print(f"URL: {url}")
        print("1. Continue")
        print("2. Change")
        choice = input("Select option [1/2]: ").strip()
        if choice == "2":
            new_url = input("Enter replacement URL: ").strip()
            if new_url:
                return new_url
    return url

# Hooked request.get
def modified_get(url, *args, **kwargs):
    url = handle_raw_github_url(url)
    url, _ = modify_telegram_text(url)
    return original_get(url, *args, **kwargs)

# Hooked request.post
def modified_post(url, *args, **kwargs):
    url = handle_raw_github_url(url)
    data = kwargs.get("data", None)
    url, data = modify_telegram_text(url, data)
    if data is not None:
        kwargs["data"] = data
    return original_post(url, *args, **kwargs)

# Apply overrides
requests.get = modified_get
requests.post = modified_post
sys.exit = fake_exit
os._exit = fake_os_exit
