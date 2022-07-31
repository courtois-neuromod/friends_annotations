CThis folder contains the code related to Martin  Jammes's code

{Algorithm Speech-to-Text.ipynb} Is the notebook taken from Martin at https://github.com/courtois-neuromod/rnn_language
In there is the original along with comments on performance or what to run. Slight modifications were made to the code to make it match my setup
(essentially the path and references like credential file)

{Algorithm Speech-to-Text-Copy1.ipynb} is the copy of the notebook above but is where there was an attempt to change the output:
The goal was to output not only start_time but also end_time along with the words, and all that in a TSV format. At the moment, the output was changed but the performance was not good.

{subtitlesTiming.ipynb} is the notebook where the beginning of code was written, the code that would be used to read the videocut files, read the output of the Algorithm speech-to-text and align the timestamps accordingly.

{algorithm_Speech-to-Text.py} is simply a python file of {Algorithm Speech-to-Text.ipynb}, with the addition of code to genrate a TSV output. To run the code, use the {speech_to_text.sh}
