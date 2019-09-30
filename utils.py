import os
import argparse

BTS = {'namjoon', 'jin', 'suga', 'jhope', 'jimin' ,'taehyung','jungkook'}
BING = "bing_search_api"
ENCODE = "encode_faces"
ENCODINGS = 'encodings.pickle'

ap = argparse.ArgumentParser()
ap.add_argument("-o", "--operation", type=str, default='sanitize',
	help="operation to perform: [download, encode, sanitize] ")
ap.add_argument("-m", "--members", type=str, default = "all",
  help="specify subset of members for operation on\n ie: `-m suga jimin...`, default is `all`")
args = vars(ap.parse_args())

def download():
  queue = BTS if args["members"] == "all" else set(args["members"].split(" "))
  if queue.isdisjoint(BTS):
    print("[ERROR] unrecognized BTS member(s) {}".format(query-BTS))
    return
  for member in queue:
    os.system("python {} --query \"{}\" --output dataset/{}".format(BING, member, member))

def encode():
  queue = BTS if args["members"] == "all" else set(args["members"].split(" "))
  if queue.isdisjoint(BTS):
    print("[ERROR] Unrecognized BTS member(s) {}".format(query-BTS))
    return
  for member in queue:
    os.system("python {}.py --dataset dataset/{} --encodings {} --detection hog".format(ENCODE, member, ENCODINGS))
  
def sanitize():
  queue = BTS if args["members"] == "all" else set(args["members"].split(" "))
  if queue.isdisjoint(BTS):
    print("[ERROR] unrecognized BTS member(s) {}".format(query-BTS))
    return
  for member in queue:
    for file in os.listdir("dataset/{}".format(member)):
      filename, extension = file.split('.')
      if len(extension) != "jpg":
        src = "dataset/{}/{}".format(member, file)
        dst = "dataset/{}/{}.jpg".format(member, file)
        print("[INFO] Renaming {} to {}".format(src, dst))
        os.rename(src, dst) 


if args["operation"] == "download":
  download()
elif args["operation"] == "encode":
  encode()
elif args["operation"] == "sanitize":
  sanitize()
else:
  print("[ERROR] Unrecognized operation {}".format(args["operation"]))
