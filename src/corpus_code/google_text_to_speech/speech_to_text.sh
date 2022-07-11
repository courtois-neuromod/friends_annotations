#source /path/to/virtualenv/bin/activate
source ~/Venvs/Corpus/bin/activate

cd ~/friends_annotations/

captionsFolder=${1}
season=${2}

for file in ${captionsFolder}; do
    python3 text_to_speech_TEST.py ./credentials-Steve-neuromod.json text_to_speech_neuromod ${file} /home/steveb/GitHub/friends_annotations/data/neuromod/monoAudiofiles/friends_s01e07a.wav /home/steveb/GitHub/friends_annotations/annotation_results/textAligned/google_text_to_speech/friends_s01e07a.txts
done


for file in /data/neuromod/DATA/cneuromod/friends/stimuli/s${season}/friends_s0${season}e*a.mkv; do
    python3 -m scenedetect -c ./Config/s${season}.cfg --input ${file} detect-adaptive list-scenes
done













#UNUSED
# for file in /data/neuromod/DATA/cneuromod/friends/stimuli/s2/friends_s0*e*b.mkv.mkv; do
#     python3 -m scenedetect -c Config/s2.cfg --input "$file" detect-adaptive list-scenes
# done
#
# for file in /data/neuromod/DATA/cneuromod/friends/stimuli/s3/friends_s0*e*b.mkv.mkv; do
#     python3 -m scenedetect -c Config/s3.cfg --input "$file" detect-adaptive list-scenes
# done
#
# for file in /data/neuromod/DATA/cneuromod/friends/stimuli/s4/friends_s0*e*b.mkv.mkv; do
#     python3 -m scenedetect -c Config/s4.cfg --input "$file" detect-adaptive list-scenes
# done
#
# for file in /data/neuromod/DATA/cneuromod/friends/stimuli/s5/friends_s0*e*b.mkv.mkv; do
#     python3 -m scenedetect -c Config/s5.cfg --input "$file" detect-adaptive list-scenes
# done
#
# for file in /data/neuromod/DATA/cneuromod/friends/stimuli/s6/friends_s0*e*b.mkv.mkv; do
#     python3 -m scenedetect -c Config/s6.cfg --input "$file" detect-adaptive list-scenes
# done






#
# #source /path/to/virtualenv/bin/activate
# source ~/Venvs/Pyscene/bin/activate
#
# cd ~/friends_annotations/PySceneDetect
#
# import os
#
# for file in os.listdir("~/data/neuromod/DATA/cneuromod/friends/stimuli/s1");
#     if file.endswith(".mkv");
#     python3 -m scenedetect -c Config/s1.cfg --input file detect-adaptive list-scenes
# done
#
# for file in os.listdir("~/data/neuromod/DATA/cneuromod/friends/stimuli/s2");
#     if file.endswith(".mkv");
#     python3 -m scenedetect -c Config/s2.cfg --input file detect-adaptive list-scenes
# done
#
# for file in os.listdir("~/data/neuromod/DATA/cneuromod/friends/stimuli/s3");
#     if file.endswith(".mkv");
#     python3 -m scenedetect -c Config/s3.cfg --input file detect-adaptive list-scenes
# done
#
# for file in os.listdir("~/data/neuromod/DATA/cneuromod/friends/stimuli/s4");
#     if file.endswith(".mkv");
#     python3 -m scenedetect -c Config/s4.cfg --input file detect-adaptive list-scenes
# done
#
# for file in os.listdir("~/data/neuromod/DATA/cneuromod/friends/stimuli/s5");
#     if file.endswith(".mkv");
#     python3 -m scenedetect -c Config/s5.cfg --input file detect-adaptive list-scenes
# done
#
# for file in os.listdir("~/data/neuromod/DATA/cneuromod/friends/stimuli/s6");
#     if file.endswith(".mkv");
#     python3 -m scenedetect -c Config/s6.cfg --input file detect-adaptive list-scenes
# done
