# This is a simple script to turn a a text file of lines or paragraphs
# into a transcript file that can be used for the forced alignment.
# '#' is the comment character in the text files

import sys
import simplejson as json
import os.path
import glob
import click
import jsonschema
import pandas as pd

@click.command()
@click.argument('text_file')
@click.option('--output-file', default=None, help="Output transcript file")
@click.option('--speaker-folder', default="Narrator", help="The folder containing speaker file")
def text_to_transcript(text_file, output_file, speaker_folder):
    text = open(text_file).read()

    filedir = os.path.dirname(os.path.realpath(__file__))
    schema_path = os.path.join(
        filedir, "transcript_schema.json")

    transcript_schema = json.load(open(schema_path))
    # speaker_files= sorted(glob.glob(speaker_folder+'*.csv'))
    speakerloc= speaker_folder +text_file[54:60] +'.csv'
    speakerfile = pd.read_csv(speakerloc,  on_bad_lines='skip')
    counter = 0
    paragraphs = text.split("\n\n")
    out = []
    for para in paragraphs:
        para = para.replace("\n", " ")
        if para == "" or para.startswith("#"):
            continue

        line = {
            "speaker": speakerfile['ID'][counter],
            "line": para
        }
        out.append(line)
        counter += 1

    jsonschema.validate(out, transcript_schema)
    if output_file is None:
        json.dumps(out, indent=4)
    else:
        with open(output_file, 'w') as f:
            f.write(json.dumps(out, indent=4))
    return

if __name__ == "__main__":
    text_to_transcript()
