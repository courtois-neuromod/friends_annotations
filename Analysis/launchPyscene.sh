#source /path/to/virtualenv/bin/activate
source ~/Venvs/Pyscene/bin/activate

cd ~/friends_annotations/PySceneDetect


for file in /data/neuromod/DATA/cneuromod/friends/stimuli/s1/*.mkv; do
    python3 -m scenedetect -c Config/s1.cfg --input file detect-adaptive list-scenes
done

for file in /data/neuromod/DATA/cneuromod/friends/stimuli/s2; do
    python3 -m scenedetect -c Config/s2.cfg --input file detect-adaptive list-scenes
done

for file in /data/neuromod/DATA/cneuromod/friends/stimuli/s3; do
    python3 -m scenedetect -c Config/s3.cfg --input file detect-adaptive list-scenes
done

for file in /data/neuromod/DATA/cneuromod/friends/stimuli/s4; do
    python3 -m scenedetect -c Config/s4.cfg --input file detect-adaptive list-scenes
done

for file in /data/neuromod/DATA/cneuromod/friends/stimuli/s5; do
    python3 -m scenedetect -c Config/s5.cfg --input file detect-adaptive list-scenes
done

for file in /data/neuromod/DATA/cneuromod/friends/stimuli/s6; do
    python3 -m scenedetect -c Config/s6.cfg --input file detect-adaptive list-scenes
done





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
