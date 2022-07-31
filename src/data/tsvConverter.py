# import glob
# import csv
#
# files= sorted(glob.glob("/home/steveb/GitHub/friends_annotations/results/CSVpyscene/s*/*csv"))
# #
# # print(files)
#
# for file in files:
#     with open(file, 'r') as csvin, open("/home/steveb/GitHub/friends_annotations/results/TSVpyscene/"+file[-29:-27]+'/'+file[-26:-4]+'.tsv', 'w') as tsvout:
#         csvin = csv.reader(csvin)
#         tsvout = csv.writer(tsvout, delimiter='\t')
#         for row in csvin:
#             tsvout.writerow(row)

import csv

with open("/home/steveb/GitHub/friends_annotations/results/corpusEmotions.csv", "r") as csvin, open("/home/steveb/GitHub/friends_annotations/results/corpusEmotions.tsv", "w") as tsvout:
    csvin = csv.reader(csvin)
    tsvout = csv.writer(tsvout, delimiter='\t')
    for row in csvin:
        tsvout.writerow(row)
