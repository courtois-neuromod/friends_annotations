import argparse
import os, sys
import glob, json
import subprocess
from datetime import timedelta
from pathlib import Path

import numpy as np
import pandas as pd
import assemblyai as aai
from moviepy import VideoFileClip


def get_arguments():

    parser = argparse.ArgumentParser(
        description="extract movie transcripts with AssemblyAI speech2text"
    )
    parser.add_argument(
        '-i',
        '--ipath',
        type=str,
        required=True,
        help='path to directory that contains the .mkv input files',
    )
    parser.add_argument(
        '-s',
        '--season',
        type=str,
        required=True,
        help='season of Friends to process',
    )
    parser.add_argument(
        '-e',
        '--epi',
        type=str,
        required=True,
        help='episode number to process',
    )        
    parser.add_argument(
        '-w',
        '--wdir',
        type=str,
        required=True,
        help='path to save extracted audio files',
    )    
    parser.add_argument(
        '-o',
        '--odir',
        type=str,
        default='./results',
        help='path to output directory',
    )
    parser.add_argument(
        '-k',
        '--apikey',
        type=str,
        required=True,
        help='your AssemblyAI API token',
    )    
    return parser.parse_args()



def extract_audio(mkv_file, wav_dir):
    epi_num = mkv_file.split("/")[-1].split("_")[1].split(".")[0]

    wav_path = f"{wav_dir}/{os.path.basename(mkv_file).replace('mkv', 'wav')}"

    if not Path(wav_path).exists():
        VideoFileClip(mkv_file).audio.write_audiofile(
            wav_path,
        )
    #rmvid_command = f"rm -rf {mkv_file}"
    #subprocess.run(rmvid_command, shell = True, executable="/bin/bash")

    return wav_path


def get_speech2text(mkv_file, wav_dir, out_dir):

    wav_path = extract_audio(mkv_file, wav_dir)
    out_path = Path(
        f"{out_dir}/{os.path.basename(mkv_file).replace('.mkv', '_aaUt.json')}"
    )

    if not Path(out_path).exists():
        transcript = aai.Transcriber(
            config = aai.TranscriptionConfig(
                speech_model = "universal",
                #speaker_labels=True,
            ),
        ).transcribe(wav_path)

        if transcript.status == "error":
            raise RuntimeError(
                f"Transcription failed: {transcript.error}"
            )

        json_results = {
            "transcript": transcript.text,
            "words": [
                {
                    "word": w.text,
                    "start": float(w.start)/1000,
                    "end": float(w.end)/1000,
                    "speaker": None,
                    "confidence": w.confidence,
                } for w in transcript.words
            ],
            "sentences": [
                {
                    "text": s.text,
                    "start": float(s.start)/1000,
                    "end": float(s.end)/1000,
                    "speaker": None,
                    "confidence": s.confidence,
                    "words": [
                        {
                            "word": x.text,
                            "start": float(x.start)/1000,
                            "end": float(x.end)/1000,
                            "speaker": None,
                            "confidence": x.confidence,
                        } for x in s.words
                    ]
                } for s in transcript.get_sentences()
            ]
        }

        with open(out_path, "w") as outfile:
            json.dump(json_results, outfile)


def main():

    args = get_arguments()

    input_path = args.ipath
    wav_dir = args.wdir
    out_dir = args.odir
    aai.settings.api_key = args.apikey

    Path(out_dir).mkdir(parents=True, exist_ok=True)
    Path(wav_dir).mkdir(parents=True, exist_ok=True)

    mkv_list = sorted(glob.glob(
        f"{input_path}/friends_s0{args.season}e{args.epi}*.mkv"
    ))

    for mkv_file in mkv_list:
        get_speech2text(mkv_file, wav_dir, out_dir)


if __name__ == '__main__':
    sys.exit(main())
