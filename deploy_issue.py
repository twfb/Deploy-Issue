import requests
import os
import json
import datetime
import sys

REPO = sys.argv[1]
POST_DIR = sys.argv[2]
TOKEN = sys.argv[3]


HEADERS = {
    "Accept": "application/vnd.github.v3+json",
    "Authorization": "token {}".format(TOKEN),
}


all_posts = list(map(lambda x: x.split(".md")[0], os.listdir(POST_DIR)))

remove_posts = filter(
    lambda x: x["title"] in all_posts,
    requests.get(
        "https://api.github.com/repos/{}/issues?labels=published".format(REPO),
        headers=HEADERS,
    ).json(),
)

add_posts = filter(
    lambda x: "unpublished" not in str(x["labels"]),
    requests.get(
        "https://api.github.com/repos/{}/issues?labels=published".format(REPO),
        headers=HEADERS,
    ).json(),
)

print("add, remove, update")
count = [0, 0, 0]

for post in add_posts:
    file_path = POST_DIR + post["title"] + ".md"
    with open(file_path, "w") as f:
        f.write(post["body"])
    os.system("git add " + file_path + " >/dev/null 2>&1")
    if os.popen("git diff " + file_path).read().strip():
        count[2] += 1
    else:
        count[0] += 1


for post in remove_posts:
    os.system("git rm " + POST_DIR + post["title"] + ".md" + " >/dev/null 2>&1")
    count[1] += 1

print(count)
