import time
from datetime import datetime as dt

host_test = r"E:\IT Ebooks\code\web_blocker\hosts"
host_path = r"C:\Windows\System32\drivers\etc"
redirect = "127.0.0.1"
block_file = r"E:\IT Ebooks\code\web_blocker\block.txt"

with open(block_file,"r") as file:
    website_list = [web.strip() for web in file.readlines()]
    print(website_list)

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        print("Working hour...")
        with open(host_path, 'r+') as file:
            content = file.read()
            print(content)
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        with open(host_path, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Relax time.")
    time.sleep(5)
