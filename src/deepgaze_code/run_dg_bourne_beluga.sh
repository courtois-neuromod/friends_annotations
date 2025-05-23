#!/bin/bash
#SBATCH --account=rrg-pbellec
#SBATCH --job-name=deepgaze
#SBATCH --output=/project/rrg-pbellec/mstlaure/friends_annotations/slurm-%A_%a.out
#SBATCH --error=/project/rrg-pbellec/mstlaure/friends_annotations/slurm-%A_%a.err
#SBATCH --time=24:00:00
#SBATCH --cpus-per-task=10
#SBATCH --gres=gpu:v100:1
#SBATCH --mem-per-cpu=4000M
#SBATCH --mail-type=ALL
#SBATCH --mail-user=marie.stl@gmail.com

# load modules required for your script to work
module load python/3.7
module load opencv/4.5.1

# create and activate project's virtual env
virtualenv --no-download $SLURM_TMPDIR/env
source $SLURM_TMPDIR/env/bin/activate
pip install --no-index --upgrade pip
pip install --no-index -r requirements_deepgaze.txt

FOLDER="/project/rrg-pbellec/mstlaure/friends_annotations"
INPUT_VIDEOS="/home/mstlaure/projects/rrg-pbellec/mstlaure/deepgaze_mr/data/movie10.stimuli/bourne/bourne*.mkv"
OUTPUT_FOLDER="/home/mstlaure/projects/rrg-pbellec/mstlaure/deepgaze_mr/results/bourne/coordinates/fullsize_coord"

# activate project's virtual env
#source "/lustre03/project/6003287/mstlaure/.virtualenvs/deepgaze_mr/bin/activate"

# to run on compute canada, checkpoints cannot be downloaded from torch.hub
cp ${FOLDER}/checkpoints/mtangemann_deepgazemr_v1/data/vgg19-dcbb9e9d.pth ~/.cache/torch/hub/checkpoints

# launch job
python -m src.deepgaze_code.run_deepgaze \
        --ivid="${INPUT_VIDEOS}" \
        --codir="${FOLDER}" \
        --mv_label="bourne" \
        --min=20 \
        --thresh=0.8 \
        --odir="${OUTPUT_FOLDER}"
