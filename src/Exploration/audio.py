import moviepy.editor as mp
import glob

files = sorted(glob.glob(r"/data/neuromod/DATA/cneuromod/friends/stimuli/s*/*.mkv"))

for file in files:
    # print(file[-19:])
    if "a" in file[-19:] or "b" in file[-19:]:
         # print(file)
        name = file[-18:]
        name = name.replace(".mkv", "")
#         print(name)
        my_clip = mp.VideoFileClip(r""+file)
        my_clip.audio.write_audiofile(r"/home/samougou/friends_annotations/data/audiofiles/"+name+".wav")
