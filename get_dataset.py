import os
bts = ['namjoon', 'jin', 'yoongi', 'jhope', 'jimin' ,'taehyung','junkook']
for member in bts:
  cmd = "python bing_search_api.py --query \"{}\" --output dataset/{}".format(member, member)
  os.system(cmd)