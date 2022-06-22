import moviepy.editor as mp
import glob

files = sorted(glob.glob(r"/data/neuromod/DATA/cneuromod/friends/stimuli/s*/*.mkv"))

for file in files:
    # print(file[-19:])
    if "a" in file[-19:] or "b" in file[-19:]:
         print(file)
