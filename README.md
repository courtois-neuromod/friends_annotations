friends_annotations
==============================
This repository includes annotations of half-episodes from the Friends sitcom watched inside the scanner by Courtois-Neuromod participants. It includes the annotations themselves, as well as the scripts used to generate them.



**PYSCENEDETECT**

PsySceneDetect detects scene cuts (e.g., camera changes) in the different Friends episodes. Of note, the script detects scene cuts (instant changes) but is weak to pick up gradual changes like fade in / out. The code for this tool is found in a submodule forked from https://github.com/Breakthrough/PySceneDetect and modified to output bids-compliant .tsv files.

The script to launch the segmentation is src/pyscene_code/launchPyscene.sh. It takes .mkv files and generates the scene cuts (list of frames) with the PySceneDetect code ("detect-adaptive" mode). For each season, the config files used are <a href="https://github.com/courtois-neuromod/PySceneDetect/tree/dev/config">here</a>

Input: .mkv video files (half episodes)\
Output: .tsv files containing three columns: segment onset (in s), duration (s), and the first frame of each cut (frame number). The output is found in annotation_results/TSVpyscene


**DEEPGAZE MR**

DeepGaze MR is a saliency model with VGG-19 backbone trained to predict the likelihood of the viewer's gaze position for movie frames.
The model outputs one saliency map per movie frame that reflects the likelihood of gaze position over the frame's pixels.
It was trained on the LEDOV dataset (movies and eye-tracking).
Source code: https://github.com/mtangemann/deepgazemr

The annotations included in the current dataset are the coordinates of the peak value(s) from DeepGaze saliency maps for each frame
of the different Friends episodes (seasons 1 to 6). They indicate likely gaze positions within each movie frame.

The script to launch the extraction of peak coordinates is:
 - src/deepgaze_code/run_dg_friends_beluga.sh s1 a
 The script takes two arguments (e.g., 's6' 'b'), which are the Friends' season and half (a or b)

Input: .mkv video files that correspond to half episodes shown to CNeuromod participants in the scanner\

Output (per half episode):  
- *_maxpeak_coord.tsv file containing one entry per frame, and three columns: h, w (saliency peak's height and width within the movie frame, in pixels, using matrix indexing), and p (the number of local maxima identified within a specific frame).
- *_locmax_normalized_xy.npz file which contains a list of local maxima for each movie frame. Each maximum has three values: its normalized saliency, and its x and y cartesian coordinates, which are normalized positions on the entire projection screen (x, y = (0, 0) corresponds to screen's bottom left corner).
- *_locmax_pixel_hw.npz file which contains a list of local maxima for each movie frame. Each maximum has three values: its normalized saliency, and its h and w coordinates (in pixels, using matrix indexing).\
The output is found in annotation_results/DeepgazeMR


**CAPTIONS**

pending: captions realigned with the timing of the C-Neuromod runs (half episodes), with timestamps for each word.


**Google speech to text**
Google speech to text uses mono audio files to generate timestamps of the words recognized in said audios. The tool's performance is only as good as to how simple the audio is: having other sounds and noise makes accuracy drop. All code and necessary information can be found on the corpusdev branch in src/google_speech_to_text

Input: .wav mono audio files (half episodes)\
Output: .tsv files containing three columns: word, start_time (in s), end_time (in s). The output is found on the corpusdev branch in annotation_results/textAligned/google_speech_to_text



**Martin's code**
Martin Jammes, an ex lab member, came up with code that takes audio files and with the help of google speech to text, gives timestamps of the words present in the appropriate captions file, words matched with the audio files. The code has trouble with said matching because the friends episode shown to subjects have cuts (removing the intro song + seperating and part a and b). The plan for said tool is to use the Martin's output on uncut audio files and then make changes to the timestamps with information on the cuts made to videos. See src/martin_code/readme.txt on the corpusdev branch for information on the progress made.



**FRIENDS_CORPUS**

pending: annotated utterances from the <a href="https://convokit.cornell.edu/documentation/friends.html">Friend Corpus</a> realigned with the timing of the C-Neuromod runs (half episodes)
At the moment, only the extraction of the data from the raw data has been done. Relevant information can be found on the corpusdev branch in  data/friends_corpus/readme.txt


**MELD**

pending: annotated utterances from <a href="https://affective-meld.github.io/">MELD</a> realigned with the timing of the C-Neuromod runs (half episodes)



--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
