import argparse
import glob, os, sys
from pathlib import Path

import numpy as np
import pandas as pd


def get_arguments():

    parser = argparse.ArgumentParser(
        description="Processes audio-annot output (.csv) and break it down into episode-specific .tsv files for bids-compliant dset.")
    parser.add_argument(
        '--ipath',
        type=str,
        required=True,
        help='path to input file (.csv), e.g., ../../data/audio_tags/indices_FriendsAudioAnnot.csv'
    )
    parser.add_argument(
        '--odir',
        type=str,
        default='../../annotation_results/audio_tags',
        help='path to output directory',
    )

    return parser.parse_args()


def fix_name(row):
    '''
    Remove placeholder date & time info from episode name
    '''
    return row['name'].split('_')[1]


def bidsify_audiotag(
    csv_path: str, 
    out_path: str,
):
    """."""
    df = pd.read_csv(csv_path, sep=",")
    sort_df = df.sort_values(by=['name', 'start'])

    sort_df['name'] = sort_df.apply(lambda row: fix_name(row), axis=1)
    sort_df = sort_df.rename(
        columns={
            'name': 'episode_id', 
            'start': 'onset',
        }
    )
    sort_df.insert(loc=2, column='duration', value=5.0)
    final_cols = ['episode_id', 'onset', 'duration'] + sort_df.columns.tolist()[5:]
    sort_df = sort_df[final_cols]

    epi_list = np.unique(sort_df['episode_id']).tolist()
    for epi in epi_list:
        season = epi[2]
        epi_df = sort_df[sort_df['episode_id']==epi]

        epi_df.to_csv(
            f"{out_path}/s{season}/friends_{epi}_audioannot.tsv",
            sep = '\t', 
            index=False, 
            header=True,
        )


def main():

    args = get_arguments()

    bidsify_audiotag(
        args.ipath,
        args.odir,
    )


if __name__ == '__main__':
    sys.exit(main())
