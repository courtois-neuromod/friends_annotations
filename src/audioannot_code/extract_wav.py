import argparse
import glob, os
from pathlib import Path

from moviepy import VideoFileClip

def get_arguments():

    parser = argparse.ArgumentParser(
        description="Extracts .wav files from friends video stimuli (.mkv). Name and organize .wav files for audio-annot processing.")
    parser.add_argument(
        '--ipath',
        type=str,
        required=True,
        help='path to input files (.mkv), e.g., ../s*/friends_s0*e*.mkv'
    )
    parser.add_argument(
        '--odir',
        type=str,
        default='./results',
        help='path to output directory',
    )

    return parser.parse_args()


def extract_wav(mkv_file, out_path):
    """."""
    wav_path = f"{out_path}/{os.path.basename(mkv_file).replace('.mkv', '_20250101_101010.wav')}"

    if not Path(wav_path).exists():
        VideoFileClip(mkv_file).audio.write_audiofile(wav_path)



def main():

    args = get_arguments()

    input_path = args.ipath
    out_path = args.odir

    Path(out_path).mkdir(
        parents=True, exist_ok=True
    )

    for mkv_file in sorted(glob.glob(input_path)):
        extract_wav(mkv_file, out_path)


if __name__ == '__main__':
    sys.exit(main())
