import os

BTS = {'namjoon', 'jin', 'suga', 'jhope', 'jimin' ,'taehyung','jungkook'}
BING = "bing_search_api.py"

print("[INFO] Creating dataset")
os.mkdir("dataset")
for member in BTS:
  os.mkdir("dataset/{}".format(member))
  os.system("python {} --query {} --output dataset/{}".format(BING, member, member))

print("[INFO] Creating test set")
os.mkdir("test")
os.system("python {} --query {} --results 10 --output test".format(BING, "bts", member))