import os
import argparse
BTS = {'namjoon', 'jin', 'suga', 'jhope', 'jimin' ,'taehyung','junkook'}

ap = argparse.ArgumentParser()
ap.add_argument("-o", "--operation", type=str, default='cleanup',
	help="operation to perfomation either `cleanup` or `get images`")
ap.add_argument("-m", "--members", type=str, default = "all",
  help="specify which member to get images/cleanup -m \n ie: `-m suga jimin...`, default is `all`")
args = vars(ap.parse_args())

def cleanup():
  queue = BTS if args["members"] == "all" else set(args["members"].split(" "))
  if queue.isdisjoint(BTS):
    print("ERROR unrecognized BTS")
    return
  for member in queue:
    for file in os.listdir(f"dataset/{member}"):
      filename, extension = file.split('.')
      if len(extension) > 3:
        src = f"dataset/{member}/{file}"
        dst = f"dataset/{member}/{filename}.jpg"
        print(f"Before {src}")
        print(f"After {dst}")
        os.rename(src, dst) 

def update_data():
  queue = BTS if args["members"] == "all" else set(args["members"].split(" "))
  for member in queue:
    cmd = "python bing_search_api.py --query \"{}\" --output dataset/{}".format(member, member)
    os.system(cmd)

if args["operation"] == "get images":
  update_data()
else:
  cleanup()
