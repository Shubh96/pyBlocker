import time
from datetime import datetime as dt

hostsLocation = r"C:\Windows\System32\drivers\etc\hosts"
#tempHosts = "hostsTest"
socialWebsiteBlock = ['www.facebook.com', 'facebook.com', 'www.messenger.com', 'messenger.com']
redirectURL = '127.0.0.1'
socialWebsiteStart = dt(dt.now().year , dt.now().month ,dt.now().day , 8)
socialWebsiteEnd = dt(dt.now().year , dt.now().month ,dt.now().day , 22)

while True:
    if socialWebsiteStart < dt.now() < socialWebsiteEnd:
        print("Time for work")
        with open(hostsLocation, "r+") as file:
            hostsContent = file.read()

            for website in socialWebsiteBlock:
                if website in hostsContent:
                    pass
                else:
                    blockItem = redirectURL + "    " + website + "\n"
                    file.write(blockItem)
    else:
        with open(hostsLocation, "r+") as file:
            hostsContent = file.readlines()
            file.seek(0)

            for line in hostsContent:
                if not any(website in line for website in socialWebsiteBlock):
                    file.write(line)
                else:
                    pass
                file.truncate()

        print("Work Over")

    time.sleep(5)
