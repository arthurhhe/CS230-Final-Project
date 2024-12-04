# Focus on a single person in the keypoints files
import json
import os
import sys

target = sys.argv[1]
if not os.path.isdir(target): raise IOError("Must specify a directory of JSON keypoint files.")

def dist_squared(p1, p2):
    return (p1[0]-p2[0])**2+(p1[1]-p2[1])**2

loc = (0,0)

for filename in sorted(os.listdir(target)):
    all_locs = []
    with open(os.path.join(target+filename), "r") as infile:
        data = json.load(infile)
    for person in data["people"]:
        all_locs.append(person["pose_keypoints_2d"][3:5])
    all_dists = [dist_squared(pos, loc) for pos in all_locs]
    if len(all_dists) != 0:
        id = all_dists.index(min(all_dists))
        loc = all_locs[id]
        data["people"] = [data["people"][id]]
    with open(os.path.join(target+filename), "w") as outfile:
        json.dump(data, outfile)

folders = """
es_htlf360os_1
es_htlf360os_2
es_htlf360os_3
es_htlf360os_4
es_htlf360os_5
es_htlf360os_6
es_htlf360os_7
es_htlf360os_8
es_htlf360os_9
jb_htf360_1
jb_htf360_2
jb_htf360_3
jb_htf360_4
jb_htf360_5
jb_htf360_6
jb_l360iod_1
jb_l360iod_2
jb_l360iod_3
jb_l360iod_4
jb_l360iod_5
jb_l360iod_6
rk_ttff360_1
rk_ttff360_2
rk_ttff360_3
sa_htiyf_1
sa_htiyf_2
sa_htiyf_3
sa_htiyf_4
sa_htiyf_5
scp_htb360_1
scp_htb360_2
scp_htb360_3
scp_htf350g_1
scp_htf350g_2
scp_htf350g_3
snowboard_360_1
spc_htb360_4
spc_htb360_5
spc_htb360_6
spc_htf360_1
spc_htf360_2
spc_htf360_3
ts_sttb360_1
ts_sttb360_2
ts_sttb360_3
ts_sttb360_4
ts_sttb360_5
ts_sttf360_1
ts_sttf360_2
ts_sttf360_3
"""