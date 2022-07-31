#source /path/to/virtualenv/bin/activate

captionsFolder=${1}

for file in ${captionsFolder}*srt; do
  echo ${file}
  name=${file:72:6} #72
  echo $name
    python3 algorithm_Speech-to-Text.py ./credentials-Steve-neuromod.json text_to_speech_neuromod ${file} /home/steveb/GitHub/friends_annotations/data/neuromod/rawMonoAudio/friends_${name}.wav /home/steveb/GitHub/friends_annotations/annotation_results/textAligned/martin/friends_${name}
done






# python3 text_to_speech_TEST.py ./credentials-Steve-neuromod.json text_to_speech_neuromod /home/steveb/Desktop/LocalAnnot/captions/friends..first_.season/friends.s01e02.720p.bluray.x264--sujaidr.srt /home/steveb/GitHub/friends_annotations/data/monoAudiofiles/friends_s01e02a.wav /home/steveb/GitHub/friends_annotations/results/textAlign/google_text_to_speech/friends_s01e02a.txt



#For episode 17, there will not be a file generated






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
