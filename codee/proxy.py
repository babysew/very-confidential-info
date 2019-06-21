import requests

proxies = {
    'http': 'http://503070370:Test$444user@Uproxyggn.sbic.sbicard.com:8080',
    'https': 'http://503070370:Test$444user@Uproxyggn.sbic.sbicard.com:8080'
    # 'https': 'http://user:pass@10.10.1.0:3128',
}

# Create the session and set the proxies.
s = requests.Session()
s.proxies = proxies

# Make the HTTP request through the session.
r = s.get('http://www.www.showmemyip.com/')

# Check if the proxy was indeed used (the text should contain the proxy IP).
print(r.text)

# print(r.status_code())