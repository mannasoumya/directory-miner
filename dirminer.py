import argparse
import httplib2
import time
import os

os.system('cls' if os.name == 'nt' else 'clear')
parser = argparse.ArgumentParser(description='Enter URL to scan for directories')
parser.add_argument("-u", "--url", help="URL input", type=str, default="http://testphp.vulnweb.com")
args = parser.parse_args()

u = args.url
f = open("big.txt")
f2 = open("extensions_common.txt")
print("Started....")
count = 0
f1 = f.readlines()
f3 = f2.readlines()
for direc in f1:
    for ext in f3:
        time.sleep(0.01)
        url = u
        url = str(url + "/")
        direc = direc.strip()
        ext = ext.strip()
        url = str(url + direc + ext)
        #print(url)
        url = url.replace(" " , "")
        h = httplib2.Http(".cache")
        resp, content = h.request(url, method="GET")
        if int(resp["status"]) == 200:
            print(url + " --> " + resp["status"])
            #sys.stdout.flush()
        else:
            print(url + "  --> ERROR NOT FOUND -->" + resp["status"])


