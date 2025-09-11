import os, sys, glob
from datetime import timedelta
import numpy as np
import pandas as pd

import argparse


def get_arguments():

    parser = argparse.ArgumentParser(description="convert manual segmentation spreadsheet exports (1 .csv / season) into one .tsv per episode")
    parser.add_argument('-i', '--ipath', type=str, required=True, help='path to input files (.csv)')
    parser.add_argument('-o', '--odir', type=str, default='./results', help='path to output directory')
    args = parser.parse_args()

    return args


def onset_time(row):
    '''
    Convert onset time from str to time object
    '''
    time_str = row['onset']

    return timedelta(minutes=int(time_str[:2]), seconds=int(time_str[3:5]))


def get_duration(row):
    '''
    Calculate difference between offset and onset time
    '''
    duration = row['offset'] - row['onset']
    return duration.total_seconds()


def get_times(row, name):
    return row[name].total_seconds()


def make_tsvs(csv_file, out_path):

    # Load csv file (one file per season)
    df = pd.read_csv(csv_file, sep=',', header=None)

    # add columne names
    column_names = ['episode', 'scene', 'segment', 'descriptor', 'caption_eng', 'caption_fr', 'onset',
                    'ONbond_location', 'ONbond_charact_entry', 'ONbond_charact_leave', 'ONbond_time_jump',
                    'ONbond_goal_change', 'ONbond_music_transit', 'ONbond_theme_song', 'ONbond_end',
                    'loc_apt1_Mon_Rach', 'loc_apt2_Chan_Joey', 'loc_apt3_Ross', 'loc_apt4_Phoeb_Rach',
                    'loc_coffeeshop', 'loc_outside', 'loc_other']
    df.columns = column_names

    # clean up time variables
    df['onset'] = df.apply(lambda row: onset_time(row), axis=1)
    # add offset and duration columns
    df['offset'] = df['onset'].to_list()[1:] + [timedelta(minutes=20)]
    df['duration'] = df.apply(lambda row: get_duration(row), axis=1)
    # convert times to seconds
    df['onset'] = df.apply(lambda row: get_times(row, 'onset'), axis=1)
    df['offset'] = df.apply(lambda row: get_times(row, 'offset'), axis=1)

    # convert boundary and location columns into booleans
    df[column_names[6:]] = df[column_names[6:]].fillna(0).astype(bool)

    # create column of transition type
    for col_name in column_names[6:14]:
        df['OFF'+col_name[2:]] = df[col_name].tolist()[1:] + [False]

    final_cnames = ['episode', 'scene', 'segment', 'onset', 'offset', 'duration',
                    'caption_eng', 'caption_fr',
                    'ONbond_location', 'ONbond_charact_entry', 'ONbond_charact_leave', 'ONbond_time_jump',
                    'ONbond_goal_change', 'ONbond_music_transit', 'ONbond_theme_song', 
                    'OFFbond_location', 'OFFbond_charact_entry', 'OFFbond_charact_leave', 'OFFbond_time_jump',
                    'OFFbond_goal_change', 'OFFbond_music_transit', 'OFFbond_theme_song', 'OFFbond_end',
                    'loc_apt1_Mon_Rach', 'loc_apt2_Chan_Joey', 'loc_apt3_Ross', 'loc_apt4_Phoeb_Rach',
                    'loc_coffeeshop', 'loc_outside', 'loc_other']

    df = df[final_cnames]

    # extract list of season's episodes
    epi_list = np.unique(df['episode'].tolist())

    # export data per half episode as .tsv
    for epi in epi_list:
        df_epi = df[df['episode'] == epi]

        # sanity check
        assert df_epi['segment'].tolist() == list(range(1, df_epi.shape[0] + 1))
        assert np.unique(df_epi['scene']).tolist() == list(range(1, df_epi['scene'].tolist()[-1]+1))

        df_epi.iloc[:-1, :].to_csv(os.path.join(out_path, f'friends_{epi}_manualseg.tsv'), sep = '\t', index=False, header=True)


def main():

    args = get_arguments()

    input_path = args.ipath
    out_path = args.odir

    if not os.path.exists(out_path):
        os.mkdir(out_path)

    csv_list = sorted(glob.glob(input_path))

    for csv_file in csv_list:
        make_tsvs(csv_file, out_path)


if __name__ == '__main__':
    sys.exit(main())
