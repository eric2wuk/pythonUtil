#! /usr/local/bin/python3
import http.client
import urllib.parse
import json
import sys
import time


#import subprocess
#subprocess.call(['say', 'hello'])

class Translater:
    ''' This is a translater base on interface of KingSoftCiBa '''
    # Prepare params
    def __init__(self, source):
        self.source = source
        self.host = "fy.iciba.com"
        self.url = "/ajax.php?a=fy"
        self.headers = {
            "Origin": "http://" + self.host,
            "Referer": "http://" + self.host + "/",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "User-Aget": ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/63.0.3239.84 Safari/537.36"),
            "Accept": "*/*",
            "Accept-Encoding": "deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7"
        }

    # Fetch data from CiBa
    def __fetch(self):
        raw = {
            "w": self.source,
            "f": "auto",
            "t": "auto"}
        con = http.client.HTTPConnection(self.host)
        con.request(
            "POST",
            self.url,
            urllib.parse.urlencode(raw),
            self.headers)
        res = con.getresponse()
        data = {
            "status": -1,
            "content": None,
            "msg": "Translate failed"}
        if res.status == 200:
            data = json.loads(res.read())
        con.close()
        return data

    # Print result
    def __show(self, data):
        if not data or (data["status"] != 0 and data["status"] != 1):
            if not data["content"]:
                print(data["msg"])
            else:
                print(data["content"])
        elif data["status"] == 0:
            #print(data)
            content = data["content"]
            if "ph_en" in content \
                    and "ph_am" in content \
                    and len(content["ph_en"]) > 0 \
                    and len(content["ph_am"]) > 0:
                print("英:[{en}] 美:[{am}]".format(
                    en=content["ph_en"], am=content["ph_am"]))

            means = content["word_mean"]
            for item in means:
                try:
                    i = item.index('.') + 1
                    print("{0:5}{1}".format(item[:i], item[i:]))
                except ValueError:
                    print(item)
        else:
            print(data["content"]["out"].replace("<br/>", " "))

    # Translate srouce to target
    def translate(self):
        data = self.__fetch()
        self.__show(data)


class Reader:
    ''' Read input from terminal '''

    # Parse source words
    def read(self):
        if len(sys.argv) < 2:
            return None
        return " ".join(sys.argv[1:])


def printProgressBar():
    class ProgressBar:
        def __init__(self, count = 0, total = 0, width = 50):
            self.count = count
            self.total = total
            self.width = width
        def move(self):
            self.count += 1
        def log(self, s):
            sys.stdout.write(' ' * (self.width + 9) + '\r')
            sys.stdout.flush()
            print(s)
            progress = self.width * self.count / self.total
            sys.stdout.write('{0:3}/{1:3}: '.format(self.count, self.total))
            sys.stdout.write('#' * int(progress) + '-' * int(self.width - progress) + '\r')
            if progress == self.width:
                sys.stdout.write('\n')
            sys.stdout.flush()

    bar = ProgressBar(total = 10)
    for i in range(10):
        bar.move()
        bar.log('We have arrived at: ' + str(i + 1))
        time.sleep(1)

# Start translate
def start():
    reader = Reader()
    source = reader.read()
    if not source:
        print("Please input source words")
    else:
        translater = Translater(source)
        translater.translate()

start()
