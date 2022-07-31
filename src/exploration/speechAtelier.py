from google.cloud import speech_v1 as speech
from google.oauth2 import service_account

credential_file= "/home/steveb/GitHub/friends_annotations/src/exploration/credentials-Steve-neuromod.json" #To create after creating a google account. The algorithm cannot work without it

credentials = service_account.Credentials.from_service_account_file(credential_file)
client = speech.SpeechClient(credentials = credentials)

def speech_to_text(config, audio):
    response = client.recognize(config=config, audio=audio)
    print_sentences(response)


def print_sentences(response):
    for result in response.results:
        best_alternative = result.alternatives[0]
        transcript = best_alternative.transcript
        confidence = best_alternative.confidence
        print("-" * 80)
        print(f"Transcript: {transcript}")
        print(f"Confidence: {confidence:.0%}")
        print_word_offsets(best_alternative)


def print_word_offsets(alternative):
    for word in alternative.words:
        start_s = word.start_time.total_seconds()
        end_s = word.end_time.total_seconds()
        word = word.word
        print(f"{start_s:>7.3f} | {end_s:>7.3f} | {word}")


config = dict(
    language_code="en-US",
    enable_automatic_punctuation=True,
    enable_word_time_offsets=True,
)
audio = dict(uri="gs://local_audio/monoAudiofiles/friends_s01e01a.wav")

speech_to_text(config, audio)
