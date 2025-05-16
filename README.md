friends_annotations
==============================
This repository includes annotations of half-episodes from the Friends sitcom watched inside the scanner by Courtois-Neuromod participants. It includes the annotations themselves, as well as the scripts used to generate them.



***PYSCENEDETECT***

PsySceneDetect detects scene cuts (e.g., camera changes) in the different Friends episodes. Of note, the script detects scene cuts (instant changes) but is weak to pick up gradual changes like fade in / out. The code for this tool is found in a submodule forked from https://github.com/Breakthrough/PySceneDetect and modified to output bids-compliant .tsv files.

The script to launch the segmentation is src/pyscene_code/launchPyscene.sh. It takes .mkv files and generates the scene cuts (list of frames) with the PySceneDetect code ("detect-adaptive" mode). For each season, the config files used are <a href="https://github.com/courtois-neuromod/PySceneDetect/tree/dev/config">here</a>

**Input**: .mkv video files (half episodes)\
**Output**: .tsv files containing three columns: segment onset (in s), duration (s), and the first frame of each cut (frame number). The output is found in annotation_results/TSVpyscene


**MANUAL SEGMENTATION**

Friends episodes were segmented manually by a rater into cohesive story chunks. Segment boundaries were flagged whenever a rater noticed a location change, time jump, character departure or entry, change in character goal(s) or other transitions (e.g., musical interlude, theme song). Segmentation rules and guidelines are detailed in /docs/manual_segmentation/segmentation_manual.md

Of note, the same scene can include more than one story segment during which different characters address different issues (e.g., an extended scene of the characters hanging out at Monica's apartment can include different segments during which Monica frets over her parents visiting, Rachel looks for her lost engagement ring, and then Ross announces to his friends that his ex wife is pregnant).

Each segment has an onset, offset and duration (in seconds). The location of each segment is also specified (the two main apartments, the coffee shop, or somewhere else). Annotations also include the type of boundary (location change, time jump, character entry, etc.) that frames the onset and offset of each segment.

(TODO: finish inserting captions; Segments are accompanied by a caption that summarizes what happens in the story (e.g., "Chandler asks Monica whether she would date him if he were the last man on earth"). Captions are available both in English and in French. They were originally written in the main rater's native French, and translated into English using deepl (https://www.deepl.com/translator), with some manual editing to resolve ambiguities.)

Output: .tsv files found in annotation_results/manual_segmentation



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

**Input**: .mkv video files that correspond to half episodes shown to CNeuromod participants in the scanner\
**Output** (per half episode):  
- *_maxpeak_coord.tsv file containing one entry per frame, and three columns: h, w (saliency peak's height and width within the movie frame, in pixels, using matrix indexing), and p (the number of local maxima identified within a specific frame).
- *_locmax_normalized_xy.npz file which contains a list of local maxima for each movie frame. Each maximum has three values: its normalized saliency, and its x and y cartesian coordinates, which are normalized positions on the entire projection screen (x, y = (0, 0) corresponds to screen's bottom left corner).
- *_locmax_pixel_hw.npz file which contains a list of local maxima for each movie frame. Each maximum has three values: its normalized saliency, and its h and w coordinates (in pixels, using matrix indexing).\
The output is found in annotation_results/DeepgazeMR


***TIME-STAMPED CAPTIONS***

We used AssemblyAI speech-to-text transcription to obtain time-stamped movie transcripts for each C-Neuromod run (half episodes). 

**Input**: .wav mono audio files (half episodes)\
**Output**: .json files containing the raw transcript, as well as a dictionary of time-stamped words. The output is found in annotation_results/Speech2Text


**FRIENDS_CORPUS**

pending: annotated utterances from the <a href="https://convokit.cornell.edu/documentation/friends.html">Friend Corpus</a> realigned with the timing of the C-Neuromod runs (half episodes)
At the moment, only the extraction of the data from the raw data has been done. Relevant information can be found on the corpusdev branch in  data/friends_corpus/readme.txt


**MELD**

pending: annotated utterances from <a href="https://affective-meld.github.io/">MELD</a> realigned with the timing of the C-Neuromod runs (half episodes)



--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
