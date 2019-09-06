from IPython.display import clear_output
import numpy as np
import SimpleITK as sitk

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
