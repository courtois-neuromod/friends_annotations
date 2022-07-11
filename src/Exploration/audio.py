import moviepy.editor as mp
import glob
# import click

#TRIED to have arguments but complicated
# @click.option('season', default=None, help="Season to convert")

files = sorted(glob.glob(r"/data/neuromod/DATA/cneuromod/friends/stimuli/s6/*.mkv"))

for file in files:
    # print(file[-19:])
    if "a" in file[-19:] or "b" in file[-19:]:
         # print(file)
        name = file[-19:]
        name = name.replace(".mkv", "")
#         print(name)
        my_clip = mp.VideoFileClip(r""+file)
        my_clip.audio.write_audiofile(r"/home/samougou/friends_annotations/data/audiofiles/"+name+".wav")