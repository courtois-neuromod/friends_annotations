import moviepy.editor as mp
import glob

files = sorted(glob.glob(r"/data/neuromod/DATA/cneuromod/friends/stimuli/s*/*.mkv"))

print(files)
