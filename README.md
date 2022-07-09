friends_annotations
==============================
This repository includes annotations of half-episodes from the Friends sitcom watched inside the scanner by Courtois-Neuromod participants. It includes the annotations themselves, as well as the scripts used to generate them.



**PYSCENEDETECT**

PsySceneDetect detects scene cuts (e.g., camera changes) in the different Friends episodes. Of note, the script detects scene cuts (instant changes) but is weak to pick up gradual changes like fade in / out. The code for this tool is found in a submodule forked from https://github.com/Breakthrough/PySceneDetect and modified to output bids-compliant .tsv files. 

The script to launch the segmentation is src/pyscene_code/launchPyscene.sh. It takes .mkv files and generates the scene cuts (list of frames) with the PySceneDetect code ("detect-adaptive" mode). For each season, the config files used are <a href="https://github.com/courtois-neuromod/PySceneDetect/tree/dev/config">here</a>

Input: .mkv video files (half episodes)\
Output: .tsv files containing three columns: segment onset (in s), duration (s), and the first frame of each cut (frame number). The output is found in annotation_results/TSVpyscene



**CAPTIONS**

pending: captions realigned with the timing of the C-Neuromod runs (half episodes), with timestamps for each word



**FRIENDS_CORPUS**

pending: annotated utterances from the <a href="https://convokit.cornell.edu/documentation/friends.html">Friend Corpus</a> realigned with the timing of the C-Neuromod runs (half episodes)



**MELD**

pending: annotated utterances from <a href="https://affective-meld.github.io/">MELD</a> realigned with the timing of the C-Neuromod runs (half episodes)



--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>




