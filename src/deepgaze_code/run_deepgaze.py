import os, sys, glob

import cv2
import numpy as np
import pandas as pd
from scipy.io import savemat
from skimage.transform import resize
from skimage.feature import peak_local_max
import torch
import torchvision

import argparse

# https://github.com/mtangemann/deepgazemr
#from deepgazemr import DeepGazeMR as _DeepGazeMR
#sys.path.append('../..')
from deepgazemr.model import DeepGazeMR as _DeepGazeMR


def get_arguments():

    parser = argparse.ArgumentParser(description="Processes movie frames with DeepGaze MR and export coordinates of most salient points")
    parser.add_argument('-i', '--ivid', type=str, required=True, help='path to input video files (.mvk)')
    parser.add_argument('-c', '--codir', type=str, required=True, help='path to code directory')
    parser.add_argument('-mv', '--mv_label', type=str, required=True, help='if true, reduce size of image')
    parser.add_argument('-m', '--min', type=int, required=True, help='min distance between maxima in pixels')
    parser.add_argument('-t', '--thresh', type=float, required=True, help='minimal threshold relative to max salience')
    parser.add_argument('-o', '--odir', type=str, default='./results', help='path to output directory')
    args = parser.parse_args()

    return args


movie_params = {
                'friends': {
                            'fps': 29.97,
                            'resize': False,
                            'height': 480,
                            'full_height': 512,
                            'width': 720
                },
                'hidden': {
                            'fps': 23.98,
                            'resize': True,
                            'resize_factor': 2,
                            'height': 400,
                            'full_height': 768,
                            'width': 960
                },
                'wolf': {
                            'fps': 23.98,
                            'resize': True,
                            'resize_factor': 2,
                            'height': 400,
                            'full_height': 768,
                            'width': 960
                },
                'life': {
                            'fps': 23.98,
                            'resize': True,
                            'resize_factor': 2,
                            'height': 400,
                            'full_height': 768,
                            'width': 960
                },
                'bourne': {
                            'fps': 29.97,
                            'resize': False,
                            'height': 360,
                            'full_height': 682,
                            'width': 720
                }
}


def normalize_map(salimap):
    mean_val = np.mean(salimap)
    std_val = np.std(salimap)
    standard = (salimap - mean_val)/std_val

    return standard


def export_peaks(input_vid, code_path, out_path, mv_params, min_dist=20, relative_thresh=0.8):
    out_name = os.path.basename(input_vid).split('.')[0]

    '''
    Initialize model and load checkpoints
    Note: The DeepGaze MR model requires to download a pretrained VVG19 checkpoint from torch.hub
    This step requires internet access (not available from beluga) unless vgg19-dcbb9e9d.pth weights
    are pre-saved (copied?) in '~/.cache/torch/hub/checkpoints'
    '''
    #model = torch.hub.load('mtangemann/deepgazemr:v1', 'DeepGazeMR', pretrained=True)1
    #device = 'cpu' # use only CPU; much slower...
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = _DeepGazeMR()
    model.to(device)
    checkpoint = torch.load(os.path.join(code_path, 'checkpoints/mtangemann_deepgazemr_v1/data/deepgazemr-ledov.pt'), map_location=device)
    model.load_state_dict(checkpoint['model_state_dict'])
    center_bias = torch.load(os.path.join(code_path, 'checkpoints/mtangemann_deepgazemr_v1/data/center-bias-ledov.pt'), map_location=device)
    model.center_bias = center_bias
    model.to(device)

    vid = cv2.VideoCapture(input_vid)
    all_DGvals_norm = []
    all_DGvals_pix = []
    all_DGvals_df = pd.DataFrame(columns=['h', 'w', 'p'], dtype=int)

    '''
    Process broken down into chunks so model doesn't run out of memory
    To get specs on video file: ffmpeg -i 'path/to/video.mvk'
    Hidden Figures: 12 runs, 23.98 fps, dim = 1920x800, 35.7302 frames / TR
    Wolf: 17 runs, 23.98 fps, dim = 1920x800, 35.7302 frames / TR
    Life: 5 runs, 23.98 fps, dim = 1920x800,
    Bourne: 10 runs, 29.97 fps, dim = 720x360, 44.6553 frames / TR
    Friends: 29.97 fps, dim = 720x480, 44.6553 frames / TR
    '''
    frames_per_tensor = 500
    img_h, img_w = mv_params['height'], mv_params['width']
    shrink = mv_params['resize']
    fps = mv_params['fps']
    shrink_factor = mv_params['shrink_factor'] if 'shrink_factor' in mv_params.keys() else 1

    success = True
    #fram_arr = np.zeros((15, 480, 720, 3)).astype(int) # Friends (full size)
    #fram_arr = np.zeros((15, 360, 720, 3)).astype(int) # Bourne (full size)
    #fram_arr = np.zeros((15, 800, 1920, 3)).astype(int) # Hidden Figures, Wolf, Life (full size); will crash on CC
    #fram_arr = np.zeros((15, 400, 960, 3)).astype('uint8') # resized Hidden Figures, Wolf, Life: 800x1920 -> 400x960
    fram_arr = np.zeros((15, img_h, img_w, 3)).astype('uint8')

    '''
    From Katja: Main thing to pay attention to is that OpenCV has this weird BGR color space instead
    of RGB (but a ::-1 on the color dimension (e.g. vid = vid[::-1,...] if it's in the first dim)
    is sufficient to transfer back to RGB. )
    '''
    while success:
        frames = []

        for i in range(frames_per_tensor):
            success, image = vid.read()
            if success:
                if shrink:
                    image = np.floor(resize(image, (img_h, img_w), preserve_range=True, anti_aliasing=True)).astype('uint8')
                frames.append(image[...,::-1])
            # image[...,::-1] dims = H, W, C where C is RBG (from cv2's flipped GBR)

        if len(frames) > 0:
            '''
            Note: the model only outputs salience maps from the 16th frame onward
            due to window approach (16 frames/window)
            Add last 15 frames from previous segment not to introduce gaps in outputs;
            If first tensor, append 15 maps of 0s (line 68)
            '''
            prev_fram_arr = np.copy(fram_arr)
            fram_arr = np.concatenate((prev_fram_arr[-15:], np.array(frames)), axis=0)

            '''
            Input videos are expected as float tensors of shape T x C x H x W
            in the range [0.0,1.0]. DeepGaze MR takes care of correctly normalizing
            the features for the VGG network
            '''
            video_tens = torch.from_numpy(fram_arr).type(torch.float32)
            #video_tens = torchvision.transforms.Resize((200, 480))(video_tens)
            video_tens = video_tens.permute(0, 3, 1, 2) / 255.0
            #video_tens = torchvision.transforms.Resize((200, 480))(video_tens)
            video_tens = video_tens.to(device)

            predictions = []
            for i, prediction in enumerate(model.predict(video_tens)):
                if prediction is not None:
                    predictions.append(prediction.detach().cpu().numpy())

            pred_arr = np.array(predictions)

            max_idx = []
            for k in range(pred_arr.shape[0]):
                idx = np.where(pred_arr[k]== pred_arr[k].max())

                '''
                Extract list of local maxima per frame
                highest: dist=20, thresh=0.8 (threshold used to recenter Friends frames for NIF,
                and to calibrate eyetracker drift w Deepgaze);
                med: dist=15, thresh=0.7; low: dist=10, thresh=0.4
                '''
                # normalize salience map values (z scores) before extracting peaks to rule out negative values (range is odd)
                norm_pred = normalize_map(pred_arr[k])
                peak_list = peak_local_max(norm_pred, min_distance=min_dist, threshold_rel=relative_thresh)
                max_idx.append([int(idx[0]*shrink_factor), int(idx[1]*shrink_factor), len(peak_list)])

                vals_norm = []
                vals_pix = []
                for peak in peak_list:
                    coord_h, coord_w = peak
                    peak_val = norm_pred[coord_h, coord_w]

                    x_norm = float(coord_w / img_w) # normalize: convert w into proportion of screen width (x coordinate)
                    # in normalized coordinates, y starts at bottom of image (flipped); also account for movie padding along height at projection
                    full_img_h = mv_params['full_height']
                    pad = int((full_img_h - img_h) / 2)
                    y_norm = float(((img_h - coord_h) + pad) / full_img_h) # normalize: convert h into proportion of screen height (y coordinate)

                    vals_norm.append([peak_val, x_norm, y_norm])
                    if shrink:
                        coord_h, coord_w = int(coord_h*shrink_factor), int(coord_w*shrink_factor)
                    vals_pix.append([peak_val, coord_h, coord_w])

                all_DGvals_norm.append(np.array(vals_norm))
                all_DGvals_pix.append(np.array(vals_pix))

            df_coord = pd.DataFrame(max_idx, columns = ['h', 'w', 'p'])
            all_DGvals_df = pd.concat((all_DGvals_df, df_coord), ignore_index=True)

    all_DGvals_df.to_csv(os.path.join(out_path, out_name+'_maxpeak_coord.tsv'), sep='\t', header=True, index=False)
    np.savez(os.path.join(out_path, out_name + '_locmax_normalized_xy.npz'), deepgaze_vals = np.asanyarray(all_DGvals_norm, dtype=object))
    np.savez(os.path.join(out_path, out_name + '_locmax_pixel_hw.npz'), deepgaze_vals = np.asanyarray(all_DGvals_pix, dtype=object))
    # to reload
    #pickled_DGvals = np.load(os.path.join(args.odir, epi + '_locmaxs.npz'), allow_pickle=True)['deepgaze_vals']


def main():

    args = get_arguments()

    input_vid = args.ivid
    code_path = args.codir
    mv_params = movie_params[args.mv_label]
    min_dist = args.min # 20 pixels
    relative_thresh = args.thresh # 0.8
    out_path = args.odir

    if not os.path.exists(out_path):
        os.mkdir(out_path)

    movie_list = glob.glob(input_vid)

    for movie_path in movie_list:
        export_peaks(movie_path, code_path, out_path, mv_params, min_dist, relative_thresh)

if __name__ == '__main__':
    sys.exit(main())
