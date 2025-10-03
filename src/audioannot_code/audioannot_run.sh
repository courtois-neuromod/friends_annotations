#!/bin/bash
#SBATCH --account=rrg-pbellec
#SBATCH --job-name=audioannot
#SBATCH --output=/project/rrg-pbellec/mstlaure/friends_annotations/slurm_files/slurm-%A_%a.out
#SBATCH --error=/project/rrg-pbellec/mstlaure/friends_annotations/slurm_files/slurm-%A_%a.err
#SBATCH --time=1:00:00
#SBATCH --cpus-per-task=12
#SBATCH --mem-per-cpu=4000M
#SBATCH --mail-type=ALL
#SBATCH --mail-user=marie.stl@gmail.com

# load modules required for your script to work
module load python/3.11.5

#source /path/to/virtualenv/bin/activate
source /home/mstlaure/links/projects/rrg-pbellec/mstlaure/friends_annotations/audioannot_venv/bin/activate

DATAPATH="/home/mstlaure/links/projects/rrg-pbellec/mstlaure/friends_annotations/data/wav_files"
OUTPATH="/home/mstlaure/links/projects/rrg-pbellec/mstlaure/friends_annotations/data/"
CACHEDIR="/home/mstlaure/links/projects/rrg-pbellec/mstlaure/friends_annotations/src/audioannot_code/local_cache"

cd audio-annot

python process.py \
	--data_path "${DATAPATH}" \
	--save_path "${OUTPATH}" \
	--cache_dir "${CACHEDIR}"
	--name FriendsAudioAnnot \
	--local \
	--save_audio_flac 0

