friends_annotations
==============================
This repository includes annotations of half-episodes from the Friends sitcom watched inside the scanner by Courtois-Neuromod participants. In includes the annotations themselves, as well as the scripts necessary to recreate them.


**PYSCENEDETECT**

PsySceneDetect detects scene cuts (e.g., camera changes) in the different Friends episodes. Of note, the script detects scene cuts (instant changes) but is weak to pick up gradual changes like fade in / out. The code for this tool is found in a submodule forked and modified from https://github.com/Breakthrough/PySceneDetect. 

The script to launch the segmentation is src/pyscene_code/launchPyscene.sh. It takes .mkv files and generates the scene cuts (list of frames) with the PySceneDetect code. 

Input: .mkv video files (half episodes)
Output: .csv files (converted to .tsv) containing one column, the first frame of each cut (frame number). The output is found in annotation_results/TSVpyscene


**CAPTIONS**

pending: captions realigned with the timing of the C-Neuromod runs (half episodes), with timestamps for each word


**FRIENDS_CORPUS**

pending: annotated utterances from the <a href="[url](https://convokit.cornell.edu/documentation/friends.html)">Friend Corpus</a> realigned with the timing of the C-Neuromod runs (half episodes)


**MELD**

pending: annotated utterances from <a href="[url](https://affective-meld.github.io/)">MELD</a> realigned with the timing of the C-Neuromod runs (half episodes)




Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data               <- Where the dataset will be installed
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictionsquirements.txt
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.testrun.org


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>




