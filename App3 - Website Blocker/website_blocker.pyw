import time
from datetime import datetime as dt 

hosts_temp = r"D:\Python\1. The Python Megacourse\App3 - Website Blocker\hosts"
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1" #Where the links will be redirected

websites = ["https://www.facebook.com", "facebook.com", "https://www.instagram.com", "instagram.com"]

while (True):
    if (dt(dt.now().year, dt.now().month, dt.now().day, 0) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16)):
        print("Working hours...")
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in websites:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
    else:
        with open(hosts_path, 'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websites):
                    file.write(line)
            file.truncate()
        print("Fun Hours")
    time.sleep(5)