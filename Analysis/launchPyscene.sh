#source /path/to/virtualenv/bin/activate
source ~/Venvs/Pyscene/bin/activate

cd ~/friends_annotations/PySceneDetect

for file in ~/data/neuromod/DATA/cneuromod/friends/stimuli/s1/*.mkv; do
    python3 -m scenedetect -c Config/s1.cfg --input file detect-adaptive list-scenes
done

for file in ~/data/neuromod/DATA/cneuromod/friends/stimuli/s2/*.mkv; do
    python3 -m scenedetect -c Config/s2.cfg --input file detect-adaptive list-scenes
done

for file in ~/data/neuromod/DATA/cneuromod/friends/stimuli/s3/*.mkv; do
    python3 -m scenedetect -c Config/s3.cfg --input file detect-adaptive list-scenes
done

for file in ~/data/neuromod/DATA/cneuromod/friends/stimuli/s4/*.mkv; do
    python3 -m scenedetect -c Config/s4.cfg --input file detect-adaptive list-scenes
done

for file in ~/data/neuromod/DATA/cneuromod/friends/stimuli/s5/*.mkv; do
    python3 -m scenedetect -c Config/s5.cfg --input file detect-adaptive list-scenes
done

for file in ~/data/neuromod/DATA/cneuromod/friends/stimuli/s6/*.mkv; do
    python3 -m scenedetect -c Config/s6.cfg --input file detect-adaptive list-scenes
done
