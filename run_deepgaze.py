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
    #parser.add_argument('-ht', '--height', type=int, required=True, help='height of output (movie frame)')
    #parser.add_argument('-w', '--width', type=int, required=True, help='width out output (movie frame)')
    parser.add_argument('-f', '--fps', type=float, default=30.0, help='frames per second')
    parser.add_argument('-o', '--odir', type=str, default='./results', help='path to output directory')
    args = parser.parse_args()

    return args


def normalize_map(salimap):
    mean_val = np.mean(salimap)
    std_val = np.std(salimap)
    standard = (salimap - mean_val)/std_val

    return standard


def export_peaks(input_vid, code_path, out_path, fps=30.0):
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
    checkpoint = torch.load(os.path.join(code_path, 'checkpoints/deepgazemr-ledov.pt'), map_location=device)
    model.load_state_dict(checkpoint['model_state_dict'])
    center_bias = torch.load(os.path.join(code_path, 'checkpoints/center-bias-ledov.pt'), map_location=device)
    model.center_bias = center_bias
    model.to(device)


def create_maps(input_vid, code_path, out_path, target_dims, fps=30.0, shrink=False, maxcount=False, s_maps=False, as_mat=False):




    # export center bias map for visiualization purposes
    if s_maps:
        center_np = center_bias.detach().cpu().numpy()
        if as_mat:
            c_dic = {"center": center_np, "label": "center bias"}
            savemat(os.path.join(out_path, out_name + '_center.mat'), c_dic)
        else:
            with open(os.path.join(out_path, out_name + '_center.npy'), 'wb') as f:
                np.save(f, center_np)

    vid = cv2.VideoCapture(input_vid)

    # To get specs on video file: ffmpeg -i 'path/to/video.mvk'
    # Hidden Figures: 12 runs, 23.98 fps, dim = 1920x800, 35.7302 frames / TR
    # Wolf: 17 runs, 23.98 fps, dim = 1920x800, 35.7302 frames / TR
    # Life: 5 runs, 23.98 fps, dim = 1920x800,
    # Bourne: 10 runs, 29.97 fps, dim = 720x360, 44.6553 frames / TR
    # Friends: 29.97 fps, dim = 720x480, 44.6553 frames / TR
    #frames_per_TR = 44.6553 # TR lenght * frames per sec; Friends = 1.49 s / TR
    frames_per_TR = fps*1.49 # 35.7302 # Hidden Figs = 1.49 s / TR
    num_tr = 10 # number of TRs of data included in each tensor
    h, w = target_dims

    success = True
    tensor_num = 0
    num_passed_frames = 0
    #fram_arr = np.zeros((15, 480, 720, 3)).astype(int) # Friends (full size)
    #fram_arr = np.zeros((15, 360, 720, 3)).astype(int) # Bourne (full size)
    #fram_arr = np.zeros((15, 800, 1920, 3)).astype(int) # Hidden Figures, Wolf, Life (full size); will crash on CC
    #fram_arr = np.zeros((15, 400, 960, 3)).astype('uint8') # resized Hidden Figures, Wolf, Life: 800x1920 -> 400x960
    fram_arr = np.zeros((15, h, w, 3)).astype('uint8')

    '''
    From Katja: Main thing to pay attention to is that OpenCV has this weird BGR color space instead
    of RGB (but a ::-1 on the color dimension (e.g. vid = vid[::-1,...] if it's in the first dim)
    is sufficient to transfer back to RGB. )
    '''
    while success:
        # Number of frames / tensor adjusted per iteration to avoid introducing drift with rounding
        frames_per_tensor = int(np.floor((frames_per_TR*num_tr*(tensor_num+1)) - num_passed_frames))
        num_passed_frames += frames_per_tensor
        frames = []

        for i in range(frames_per_tensor):
            success, image = vid.read()
            if success:
                if shrink:
                    image = np.floor(resize(image, (h, w), preserve_range=True, anti_aliasing=True)).astype('uint8')
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
                    print(tensor_num, i)
                    predictions.append(prediction.detach().cpu().numpy())


            pred_arr = np.array(predictions)
            if s_maps:
                sal_name = out_name + '_salience_' + f'{tensor_num:03}'
                if as_mat:
                    s_dic = {"saliences": pred_arr, "label": sal_name}
                    savemat(os.path.join(out_path, sal_name + '.mat'), s_dic)
                else:
                    with open(os.path.join(out_path, sal_name + '.npy'), 'wb') as f:
                        np.save(f, pred_arr)

            # to read saved .npy file...
            #with open('./results/salience_maps.npy', 'rb') as f:
            #    a = np.load(f)

            # Extract height and width coordinates of highest intensity point
            # per salience map (1 per frame) and export as .tsv file
            max_idx = []
            for k in range(pred_arr.shape[0]):
                idx = np.where(pred_arr[k]== pred_arr[k].max())
                # calculate number of local maxima in frame
                if maxcount:
                    # normalize frame
                    norm_pred = normalize_map(pred_arr[k])
                    peak_list = peak_local_max(norm_pred, min_distance=20, threshold_rel=0.8)
                    max_idx.append([int(idx[0]), int(idx[1]), len(peak_list)])
                else:
                    max_idx.append([int(idx[0]), int(idx[1])])

            coord_name = out_name + '_coord_' + f'{tensor_num:03}' + '.tsv'
            if maxcount:
                # p for peak (number of peak maxima in image)
                df_coord = pd.DataFrame(max_idx, columns = ['h', 'w', 'p'])
            else:
                df_coord = pd.DataFrame(max_idx, columns = ['h', 'w'])
            df_coord.to_csv(os.path.join(out_path, coord_name), sep='\t', header=True, index=False)

            # to export coordinates as .npy instead
            #coord_name = out_name + '_coord_' + f'{tensor_num:03}' + '.npy'
            #with open(os.path.join(out_path, coord_name), 'wb') as f:
            #    np.save(f, np.array(max_idx))

            tensor_num += 1

            # To visualize intensity map on top of corresponding frame
            # https://medium.com/@ODSC/visualizing-your-convolutional-neural-network-predictions-with-saliency-maps-9604eb03d766


def main():

    args = get_arguments()

    input_vid = args.ivid
    code_path = args.codir
    #dims = (args.height, args.width)

    #shrink = args.shrink
    fps = args.fps
    out_path = args.odir
    #count_local_maxima = args.maxcount
    #salience_maps = args.salimap
    #as_mat = args.matfile

    if not os.path.exists(out_path):
        os.mkdir(out_path)

    movie_list = glob.glob(input_vid)

    for movie_path in movie_list:
        export_peaks(movie_path, code_path, out_path, fps)


if __name__ == '__main__':
    sys.exit(main())
