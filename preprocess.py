from IPython.display import clear_output
import numpy as np
import SimpleITK as sitk
import cv2

def get_mean_std_from_allImg(train_path):
    '''
    모든 이미지셋 픽셀 값의 평균과 표준편차를 구함.
    '''
    m = []
    v = []
    for i, t in enumerate(train_path):
        img = np.array(sitk.GetArrayFromImage(sitk.ReadImage(t)))
        m.append(np.mean(img))
        v.append(np.var(img))
        print('{}th done'.format(i+1))
        clear_output(wait=True)
        
    M = np.array(m)
    V = np.array(v)
    tot_m = np.mean(M)
    tot_s = np.sqrt((np.sum(M*M) + np.sum(V)) / len(M) - tot_m*tot_m)
    return [tot_m, tot_s]




def set_range_zero2one(img):
    result_img = img - np.min(img)
    result_img = result_img / np.max(result_img)
    return result_img

def get_mean_std_ImageNetData(train_paths):
    '''
    모든 이미지셋 픽셀 값의 평균과 표준편차를 구함.
    '''
    colors = ['b', 'g', 'r']
    m = {c: [] for c in colors}
    v = {c: [] for c in colors}
    
    for i, path in enumerate(train_paths):
        img = cv2.imread(path)
        img = set_range_zero2one(img)
        n_color = img.shape[2]
        
        for c, nth in zip(colors, range(n_color)):
            m[c].append(np.mean(img[:, :, nth]))
            v[c].append(np.var(img[:, :, nth]))
        print('{}th done'.format(i+1))
        clear_output(wait=True)
    
    result_mean, result_std = [], []
    
    for c in colors:
        M = np.array(m[c])
        V = np.array(v[c])
        tot_m = np.mean(M)
        tot_s = np.sqrt((np.sum(M*M) + np.sum(V)) / len(M) - tot_m*tot_m)
        result_mean.append(tot_m)
        result_std.append(tot_s)
    return {'mean': result_mean, 'std': result_std}
