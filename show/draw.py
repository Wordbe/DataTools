from matplotlib import pyplot as plt

def draw_subplot(*arrays, figsize=(9, 16), plot_type='image'):
    '''
        subplot 이미지를 그려줍니다.
    '''
    fig = plt.figure(figsize=figsize)

    num_array = len(arrays)
    for i in range(num_array):
        fig.add_subplot(1, num_array, i+1)

        if plot_type == 'image':
            plt.imshow(arrays[i])
        elif plot_type == 'plot':
            plt.plot(arrays[i])

    plt.show()
    
