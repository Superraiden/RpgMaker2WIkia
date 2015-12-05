import requests, glob, os, sys
import json
import codecs
import base64
import urllib.request as urlib
import ntpath
import traceback
import datetime
import time

#print(urlib.quote("%&"))

baseurl = 'http://lisa-rpg.wikia.com/'
phpurl = baseurl + 'api.php'
mega_cookie = ""

input_path = "/home/tom/Dropbox/LISA_PARENT_FOLDER/5 Extrapolated Data/Wikia_Parser/output_saved/"

def update_progress(current, total, name, result, start_time):
    #print('\r[{0}] {1}%'.format('#'*(progress/10), progress))
    percentage = current/total
    total_icons = 20

    icons = int(total_icons*percentage)
    filler = total_icons-icons

    #print('\r[{0}{1}] {2}%'.format('#'*int((progress/10)), ''*int((progress/10))progress))

    time_taken = time.time() - start_time
    time_remaining = time_taken * total-current

    m, s = divmod(time_remaining, 60)
    h, m = divmod(m, 60)
    remaining = "%d:%02d:%02d" % (h, m, s)

    text = '\r[{0}{1}] {2}/{3} {4}% Time Remaining: {5} {6}:{7}'.format('#'*icons, ' '*filler, current, total, int(percentage*100), remaining, name, result)
    sys.stdout.write(text)
    sys.stdout.flush()

def main():
    mega_cookie = login()

    path = input_path + "/*.txt"
    number = 0
    for fname in glob.glob(path):
        number += 1
        try:
            with open(fname, "r") as f:
                text = f.read()
            name = os.path.splitext(os.path.basename(fname))[0]
            start_time = time.time()
            result = edit_page(os.path.splitext(os.path.basename(fname))[0], "", text)
            update_progress(number, len(glob.glob(path)), name, result["edit"]["result"], start_time)
        except:
            ass = 3
    #result = edit_page("Test1", "Summary", "Butts2")
    #print(result)
    pass


def edit_page(title, summary, text):
    global mega_cookie
    r3 = requests.get(phpurl + '?action=query&prop=info%%7Crevisions&intoken=edit&rvprop=timestamp&titles=%s&format=json' % title,
                      cookies=mega_cookie)
    mega_cookie = r3.cookies

    r3_result = json.loads(r3.text)["query"]["pages"]
    token = list(r3_result.values())[0]["edittoken"]

    new_url = "?action=edit" \
              "&watch" \
              "&format=json" \
              "&token=%s" % (urlib.quote(token))
    data = dict(text=text, title=title, summary=summary)

    try:
        last_req = requests.post(phpurl + new_url,
                            data=data,
                            cookies=mega_cookie,)
    except Exception as e:
        pass
    mega_cookie = last_req.cookies
    return json.loads(last_req.text)


def login():
    # Login request
    r1 = requests.post(baseurl + 'api.php' + get_params())
    rdata = json.loads(r1.text)

    # Confirm token; should give "Success"
    r2 = requests.post(baseurl + 'api.php' + get_params(my_token=rdata["login"]["token"]), cookies=r1.cookies)

    print("MediaWiki Logon attempt: " + json.loads(r2.text)["login"]["result"])

    # Try accessing a private MediaWiki page

    return r2.cookies

def get_params(my_token = ""):
    if my_token == "":
        return '?action=login&lgname=%s&lgpassword=%s&format=json' % (
                    'superraiden',
                    str(codecs.decode(b'YjBuYjBu\n', 'base64').decode("utf-8")))
    else:
        return '?action=login&lgname=%s&lgpassword=%s&lgtoken=%s&format=json' % (
                    'superraiden',
                    str(codecs.decode(b'YjBuYjBu\n', 'base64').decode("utf-8")),
                    my_token)
        pass

main()
