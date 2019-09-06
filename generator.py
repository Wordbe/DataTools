def generator_random(img_paths, mask_paths, batch_size=16):
    '''
        모든 데이터가 뽑히지 않을 수도 있음 (epoch을 늘리면 그런 가능성이 줄겠지만)
        모든 데이터가 뽑히지 않더라도 SGD나 BGD보다 실험적으로 성능이 더 좋다는 결과가있음.
    '''
    while True:
        indices = list(range(len(img_paths)))
        batch_idx = np.random.choice(indices, BATCH_SIZE, replace=False)

        batch_imgs = []
        batch_masks = []
        for i in batch_idx:
            img_path = img_paths[i]
            mask_path = mask_paths[i]

            img = image_preprocess(img_path)
            masks = mask_preprocess(mask_path)
            
            batch_imgs.append(img)
            batch_masks.append(masks)

        yield [np.array(batch_imgs), np.array(batch_masks)]
