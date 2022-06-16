#source /path/to/virtualenv/bin/activate
source ~/Venvs/Pyscene/bin/activate

cd ~/friends_annotations/PySceneDetect

for file in /path/to/mkv/s1/friends*.mkv; do
    python3 -m scenedetect -c Config/s1.cfg --input file detect-adaptive list-scenes
done

for file in /path/to/mkv/s2/friends*.mkv; do
    python3 -m scenedetect -c Config/s2.cfg --input file detect-adaptive list-scenes
done

for file in /path/to/mkv/s3/friends*.mkv; do
    python3 -m scenedetect -c Config/s3.cfg --input file detect-adaptive list-scenes
done

for file in /path/to/mkv/s4/friends*.mkv; do
    python3 -m scenedetect -c Config/s4.cfg --input file detect-adaptive list-scenes
done

for file in /path/to/mkv/s5/friends*.mkv; do
    python3 -m scenedetect -c Config/s5.cfg --input file detect-adaptive list-scenes
done

for file in /path/to/mkv/s6/friends*.mkv; do
    python3 -m scenedetect -c Config/s6.cfg --input file detect-adaptive list-scenes
done
