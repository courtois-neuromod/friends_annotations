#!/usr/bin/env python
# coding: utf-8

# DESCRIPTION
#
# This code is the code that was made by martin James previously. It's goal is to take an audio file and with the help of the appropriate captions file (in srt format), to generate a list of words with their "start" timestamps in seconds. The copy of this jupyter notebook is a version in which I modified the code to ouput both the start and the end time aligned along with the word. It was not brought to completion as the accuracy of the alignment was not good. You can also see in here speech_to_text.py

# # Installation of required packages (uncomment only if necessary)

# In[1]:


import sys
#!{sys.executable} -m pip install pydub
#!{sys.executable} -m pip install google-cloud-speech
#!{sys.executable} -m pip install google-cloud-storage
#!{sys.executable} -m pip install google-oauth
import pandas as pd

# # Import

# In[2]:


import numpy as np
import io
import os
import wave
from pydub import AudioSegment

from google.cloud import speech
from google.cloud import storage

#Those 2 have been removed https://github.com/googleapis/python-speech/blob/main/UPGRADING.md#enums-and-types
# from google.cloud.speech import enums
# from google.cloud.speech import types

from google.oauth2 import service_account


# # Google Speech-to-Text API functions

# In[3]:

#
# credential_file= "/home/steveb/GitHub/friends_annotations/src/exploration/credentials-Steve-neuromod.json" #To create after creating a google account. The algorithm cannot work without it
#
# credentials = service_account.Credentials.from_service_account_file(credential_file)
# client = speech.SpeechClient(credentials = credentials)
# storage_client = storage.Client.from_service_account_json(credential_file)
# bucketname ="text_to_speech_neuromod"

def get_frame_rate(audio_file_name):
    """Return the frame rate of the audio file"""
    with wave.open(audio_file_name, "rb") as wave_file:
        frame_rate = wave_file.getframerate()
        return frame_rate

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)

def delete_blob(bucket_name, blob_name):
    """Deletes a blob from the bucket."""
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.delete()

# def google_transcribe(audio_file, time_init, words_from_the_subtitles):
#     """Return a transcript with timestamp for the audio file studied relative to time_init (the time the sentence appears in the the studied audio segment)"""

#     frame_rate = get_frame_rate(audio_file)
#     bucket_name = bucketname
#     source_file_name = audio_file
#     destination_blob_name = audio_file

#     upload_blob(bucket_name, source_file_name, destination_blob_name)
#     gcs_uri = 'gs://' + bucketname + '/' + audio_file
#     audio = speech.RecognitionAudio(uri = gcs_uri)

#     config = speech.RecognitionConfig(
#         encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
#         sample_rate_hertz=frame_rate,
#         language_code='en-US',
#         speech_contexts = [{"phrases": words_from_the_subtitles}],
#         enable_word_time_offsets=True,
#         enable_automatic_punctuation=True)

#     # Detects speech in the audio file
#     operation = client.long_running_recognize(config, audio)
#     response = operation.result(timeout=10000)
#     transcript = []
#     if len(response.results) > 0:
#         result = response.results[0]
#         words_info = result.alternatives[0].words
#         for word_info in words_info:
#             start_time = word_info.start_time
#             time = start_time.seconds + start_time.nanos * 1e-9
#             time_adjusted = round(time_init/1000 + time, 1)
#             transcript.append([time_adjusted, word_info.word])

#     delete_blob(bucket_name, destination_blob_name)
#     return transcript



# In[11]:


def google_transcribe(audio_file, time_init, words_from_the_subtitles):
    """Return a transcript with timestamp for the audio file studied relative to time_init (the time the sentence appears in the the studied audio segment)"""

    frame_rate = get_frame_rate(audio_file)
    bucket_name = bucketname
    source_file_name = audio_file
    destination_blob_name = audio_file

    upload_blob(bucket_name, source_file_name, destination_blob_name)
    gcs_uri = 'gs://' + bucketname + '/' + audio_file
    audio = speech.RecognitionAudio(uri = gcs_uri)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=frame_rate,
        language_code='en-US',
        speech_contexts = [{"phrases": words_from_the_subtitles}],
        enable_word_time_offsets=True,
        enable_automatic_punctuation=True)

    # Detects speech in the audio file
    operation = client.long_running_recognize(config=config, audio=audio)
    response = operation.result(timeout=1000000)
    transcript = []
    if len(response.results) > 0:
        result = response.results[0]
        words_info = result.alternatives[0].words
        for word_info in words_info:
            start_time = word_info.start_time
            time = start_time.seconds + start_time.microseconds * 1e-6 # nanos no longer supported: https://github.com/googleapis/python-speech/issues/71
            time_adjusted = round(time_init/1000 + time, 1)
            transcript.append([time_adjusted, word_info.word])

    delete_blob(bucket_name, destination_blob_name)
    return transcript


# # Functions used in the following parts

# In[12]:


def remove_punctuation(word):
    return word.lower().replace(',', '').replace('.', '').replace('?', '').replace('!', '')

def decomposition_time(line):
    start_str, end_str = line.split(" --> ")
    start = list(map(int, start_str.replace(',', ':').split(':')))
    end = list(map(int, end_str.replace(',', ':').split(':')))
    start_time = start[3]+1000*start[2]+60000*start[1]+3600000*start[0]
    end_time = end[3]+1000*end[2]+60000*end[1]+3600000*end[0]
    return start_time, end_time

def remove_charac_and_split(words):
    sentence_clean = words.replace('- ', ' ')
    if ':' in sentence_clean:
        sentence_clean = sentence_clean.split(': ')[-1]
    while "(" in sentence_clean:
        i1 = sentence_clean.index("(")
        i2 = sentence_clean.index(")")
        sentence_clean = sentence_clean[:i1] + sentence_clean[i2+1:]
    while "<" in sentence_clean:
        i1 = sentence_clean.index("<")
        i2 = sentence_clean.index(">")
        sentence_clean = sentence_clean[:i1] + sentence_clean[i2+1:]
    return sentence_clean.strip().split()


# # Find shift between the audio and the subtitles

# For the following parts, a positive shift means that for a given sentence, the time of its appearance in the audio is less than the time of its appearance in the subtitles

# In[13]:


def list_first_words_from_subtitles(subtitles_file):
    """Create a list of the first words of each sentence with timestamp from the subtitles file. Only the timestamp for the first words of each sentence is available in this file"""
    subtitles = open(subtitles_file, encoding='utf-8-sig')
    sentences = []
    for line in subtitles:
        line = line.replace('\n','').replace('\t','')
        if line.isdigit():
            sentences.append([0,""])
        elif "-->" in line:
            sentences[-1][0] = decomposition_time(line)[0]
        elif sentences[-1][1] != "" and line != "":
            print(sentences[-1][1])
            sentences[-1][1] += " " + line
        else:
            sentences[-1][1] += line
    list_first_words = [[sentence[0], remove_charac_and_split(sentence[1])] for sentence in sentences]
    for i in reversed(range(len(list_first_words))):
        if len(list_first_words[i][1]) == 0:
            list_first_words.pop(i)
        else:
            list_first_words[i][1] = remove_punctuation(list_first_words[i][1][0])
    return list_first_words


def list_words_from_audio(audio_file):
    """Create a list of words with timestamp from the audio file using Google Speech-to-Text API"""
    sound = AudioSegment.from_file(audio_file)
    n_pas = len(sound) // 10000
    list_words = []
    for i in range(n_pas):
        seg = sound[10000*i:10000*(i+1)]
        temp_file_name = "temp_audio_processing.wav"
        seg.export(temp_file_name, format="wav")
        transcript = google_transcribe(temp_file_name, 10000*i, [''])
        for pair in transcript:
            pair[1] = remove_punctuation(pair[1]).strip().replace('-', ' ')
            pair[0] = int(pair[0]*1000)
            list_words.append(pair)
        os.remove(temp_file_name)
    return list_words


def find_shift(subtitles_file, audio_file, precision = 300):
    """Find the best shift between the audio and the subtitles. Return the shift in ms and the number of words in common between the two list of words using this shift and a given precision in ms"""

    list_from_audio = list_words_from_audio(audio_file)
    list_from_subtitles = list_first_words_from_subtitles(subtitles_file)

    def min_ind(list_first, mini):
        """Function used only once to compute indices efficiently"""
        ind_min = 0
        ind_max = len(list_first) - 1
        ind = int((ind_min + ind_max)/2)
        while (ind_max - ind_min) > 1:
            if list_first[ind][0] > mini:
                ind_max = ind
            elif list_first[ind][0] < mini:
                ind_min = ind
            else:
                return ind
            ind = int((ind_min + ind_max)/2)
        return ind

    scoremax = 0
    bestshift = 0

    for i in range(len(list_from_audio)):
        word = list_from_audio[i][1]
        list_ind = [idx for idx,e in enumerate(list_from_subtitles) if e[1] == word]
        for j in list_ind:
            shift = list_from_subtitles[j][0] - list_from_audio[i][0]
            score = 0
            for word in list_from_audio:
                for k in range(min_ind(list_from_subtitles, word[0] + shift - precision) - 1, min_ind(list_from_subtitles, word[0] + shift + precision) + 2):
                    if list_from_subtitles[k][0] - precision < word[0] + shift < list_from_subtitles[k][0] + precision:
                        if word[1] == list_from_subtitles[k][1]:
                            score+=1
            if score > scoremax:
                scoremax = score
                bestshift = shift

    return bestshift, scoremax


# # Getting the timestamps

# In[14]:


def get_timestamp(subtitles_file, audio_file, shift, path):

    #Opening the files: subtitles, audio and path to write the transcript
    subtitles = open(subtitles_file, encoding='utf-8-sig')
    sound = AudioSegment.from_file(audio_file)
    f = open(path+ '.txt',"w")
    f.close()

    #Getting the sentences and their timestamp from the subtitles
    sentences = []
    s = []
    w = []
    for line in subtitles:
        line = line.replace('\n','').replace('\t','')
        if line.isdigit():
            sentences.append([0,0,""])
        elif "-->" in line:
            sentences[-1][0] = decomposition_time(line)[0]
            sentences[-1][1] = decomposition_time(line)[1]
        elif sentences[-1][2] != "" and line != "":
            sentences[-1][2] += " " + line
        else:
            sentences[-1][2] += line

    #For each sentence, getting the precise timestamp using Google Speech-to-Text API
    for sentence in sentences:
        start_time = sentence[0] - shift - 200
        end_time = sentence[1] - shift + 200
        if start_time > 0 and end_time < len(sound):
            words = remove_charac_and_split(sentence[2])
            if len(words) > 0:

                #Getting words and timestamp from the API
                seg = sound[start_time:end_time]
                temp_file_name = "temp_audio_processing.wav"
                seg.export(temp_file_name, format="wav")
                transcript = google_transcribe(temp_file_name, start_time, words)
                os.remove(temp_file_name)
                start_time += 200

                #Removing punctuation
                words_from_subtitles = [remove_punctuation(word) for word in words]
                transcript_from_api = [[element[0], remove_punctuation(element[1])] for element in transcript]

                #Keeping only words found by the API which are in the subtitles and present once
                to_remove=[]
                for i in range(len(transcript_from_api)):
                    word = transcript_from_api[i][1]
                    if words_from_subtitles.count(word)!= 1:
                        to_remove.append(i)
                    for j in range(i+1, len(transcript_from_api)):
                        if transcript_from_api[j][1] == word:
                            to_remove.append(j)
                            to_remove.append(i)
                for i in reversed(sorted(np.unique(to_remove))):
                    transcript_from_api.pop(i)

                #Getting the exact timestamp when possible
                timestamp = [round(start_time/1000, 1)] + [0] * (len(words_from_subtitles) - 1)
                ind_known = {0}
                for i in range(len(transcript_from_api)):
                    ind = words_from_subtitles.index(transcript_from_api[i][1])
                    timestamp[ind] = round(transcript_from_api[i][0], 1)
                    ind_known.add(ind)
                ind_known = sorted(list(ind_known))

                #Interpollate the rest of the timestamp
                i = -1
                for j in range(len(words_from_subtitles)):
                    if j in ind_known :
                        i += 1
                    elif j < ind_known[-1]:
                        timestamp[j] = round((timestamp[ind_known[i]] + (j - ind_known[i])*(timestamp[ind_known[i+1]] - timestamp[ind_known[i]])/(ind_known[i+1]-ind_known[i])), 1)
                    else:
                        timestamp[j] = round(timestamp[j-1]+0.2, 1)

                #If the result is not coherent, use linear interpollation
                if sorted(timestamp) != timestamp:
                    timestamp = [round(start_time/1000 + 2*i, 1)  for i in range(len(words_from_subtitles))]

                #Writing the words and the timestamp in the desired file
                to_write = ''
                for i in range(len(words)):
                    s.append(timestamp[i])
                    w.append(words[i])
                    to_write += str(timestamp[i]) + ': ' + words[i] + '\n'
                f = open(path+ '.txt',"a")
                f.write(to_write + '\n')
                f.close()
    d = {'start_time': s, 'word': w}
    df = pd.DataFrame(data=d)
    df.to_csv(path + '.tsv', index=False, sep="\t")

if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser(description='Aligns every word in a film transcript to a timestamp using Google\'s Speech-to-Text API.')
    parser.add_argument('credential_file', metavar='credential_file',
                    help='The path to the JSON file with valid Google API credentials.')
    parser.add_argument('bucket_name', metavar='bucket_name',
                    help='The bucket name created on the Google cloud platform.')
    parser.add_argument('subtitle_file', metavar='subtitle_file',
                    help='The path to the subtitle file (.srt file of the movie to be analyzed).')
    parser.add_argument('audio_file', metavar='audio_file',
                    help='The path to the audio file (must be in mono and .wav format).')
    parser.add_argument('result_file', metavar='result_file',
                    help='The path to the file to be created (the transcript with timestamps).')
    args = parser.parse_args()

    # To run Google API: https://cloud.google.com/docs/authentication/getting-started#cloud-console

    bucketname = args.bucket_name # this must be created online on google cloud platform
    credential_file = args.credential_file
    subtitle_file = args.subtitle_file
    audio_file = args.audio_file
    result_file = args.result_file

    credentials = service_account.Credentials.from_service_account_file(credential_file)
    client = speech.SpeechClient(credentials = credentials)
    storage_client = storage.Client.from_service_account_json(credential_file)

    shift = find_shift(subtitle_file, audio_file, precision = 300)[0] # Not necessary to recompute everytime once this is known
    get_timestamp(subtitle_file, audio_file, shift, result_file) # Should take nearly 20min for an audio file of 10 min

    # example: python speech_to_text.py ../credentials-neuromod.json neuromodvideos ../data/subtitles/bourne_supremacy_subtitles.srt ../data/movies_audio/bourne/bourne_supremacy_seg01_mono.wav ../data/result/bourne_supremacy/bourne_supremacy_seg01_mono.txt

    '''
    test:

    bucketname = 'neuromodvideos' # this must be created online on google cloud platform!!
    credential_file = 'credentials-neuromod.json'
    transcript_file = "../data/subtitles/bourne_supremacy_subtitles.srt"
    audio_file = "../data/movies_audio/bourne/bourne_supremacy_seg01_mono.wav"

    credentials = service_account.Credentials.from_service_account_file(credential_file)
    client = speech.SpeechClient(credentials = credentials)
    storage_client = storage.Client.from_service_account_json(credential_file)

    result_file = "../data/result/bourne_supremacy/bourne_supremacy_seg01_mono.txt" #To edit
    shift = find_shift(transcript_file, audio_file, precision = 300)[0] #Not necessary to recompute everytime once this is known
    get_timestamp(transcript_file, audio_file, shift, transcript_with_timestamp_to_create_filename) #Should take nearly 20min for an audio file of 10 min

    '''
