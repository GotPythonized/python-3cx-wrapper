from http.cookiejar import Cookie


BASEURL = "https://{}:{}"
API_URL = BASEURL.__add__("/api/{}")
AUTHED = False
HEADERS = {
    "accept": "application/json, text/plain, */*",
    "content-type": "application/json;charset=UTF-8",
    "sec-ch-ua":'"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
    "accept-encoding":"gzip, deflate, br",
    "Connection":"keep-alive",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "sec-gpc": "1",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Safari/537.36",
}

class Authentication:
    authed=False
    username = None
    password = None
    fqdn = None
    port = None
    Cookie = None