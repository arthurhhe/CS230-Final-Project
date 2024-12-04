# Focus on a single person in the keypoints files
import json
import os
import sys

target = sys.argv[1]
if not os.path.isdir(target): raise IOError("Must specify a directory of directory of JSON keypoint files.")

count = 0

for folder in sorted(os.listdir(target)):
    folder_path = os.path.join(target, folder)
    if os.path.isdir(folder_path):
        for filename in sorted(os.listdir(folder_path)):
            all_locs = []
            with open(os.path.join(folder_path+'/'+filename), "r") as infile:
                data = json.load(infile)
            if len(data["people"]) > 1:
                print(folder_path+filename+' has '+len(data["people"])+' poses')
            count+=1
print('Files traversed: ', count)