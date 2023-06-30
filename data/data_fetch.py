import requests
import json
import re

names = []
print("")

for i in range(1, 101):
    resp = requests.post(
        "https://daxue.hao86.com/searchc/",
        None,
        {"name": None, "city": 0, "type": 0, "arrangement": 0, "page": i},
    )
    resp = json.loads(resp.text)
    for x in resp["data"]["data"]:
        names.append(x["name"])
    print("\rPage %d done" % (i), end="")

print("\n")

pattern = r"<div class=\"text jie\">(.*?)</div>"
cache = ""
cnt, acnt = 0, 0
with open("clean_data/documents.jsonl", "a", encoding="utf-8") as f:
    for name in names:
        resp = requests.get("https://daxue.hao86.com/" + name + "/")
        resp.encoding = "utf-8"
        resp = resp.text.replace("\n", "")
        contents = re.findall(pattern, resp)
        if contents.__len__() == 0:
            break
        cache = (
            cache
            + json.dumps({"id": name, "contents": contents[0]}, ensure_ascii=False)
            + "\n"
        )
        cnt += 1
        acnt += 1
        print("\rDocuments count %d fetched" % (acnt), end="")
        if cnt % 10 == 0:
            f.write(cache)
            cache = ""
            cnt = 0
    f.write(cache)

print("\n\nDone. See ./clean_data/documents.jsonl")
