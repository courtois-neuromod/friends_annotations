import os
from google.cloud import speech
from google.oauth2 import service_account
from google.cloud import storage
import pandas as pd

audiolist = pd.read_csv("audiolist.tsv",sep = '\t')
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/samougou/friends_annotations/src/exploration/credentials-Steve-neuromod.json'
speech_client = speech.SpeechClient()

config = dict(
    language_code="en-US",
    enable_automatic_punctuation=True,
    enable_word_time_offsets=True,
)


for file in audiolist['file']:
    audio = dict(uri="gs://local_audio/monoAudiofiles/"+file)
    client = speech.SpeechClient()
    operation = client.long_running_recognize(config=config, audio=audio)
    response = operation.result()

    df = pd.DataFrame(columns=['word', 'start_time', 'end_time'])
    for result in response.results:
        alternative = result.alternatives[0]
        for word in alternative.words:
            curr_dict = {'word': [word.word], 'start_time': [word.start_time.total_seconds()], 'end_time': [word.end_time.total_seconds()]}
            curr_df = pd.DataFrame.from_dict(curr_dict)
            df = pd.concat([df, curr_df], ignore_index=True)

    df.to_csv('/home/samougou/friends_annotations/annotation_results/textAligned/google_text_to_speech/' + file[:-4] + '.tsv', index=False, sep="\t")
