import numpy as np

def dummy_image():
    image_matrix = np.zeros((64, 64))
    
    cum_value = 0
    
    for j in range(64):
        for i in range(64):
            image_matrix[j, i] = cum_value
            cum_value += 1
            if cum_value > 255:
                cum_value = 0
    return image_matrix

def padding_image(image_matrix, block_size):
    padding = (block_size - 1) // 2
    padded = np.pad(image_matrix, 
                    ((padding, padding), (padding, padding)), 
                    'constant',
                    constant_values=(0,0))
    
    return padded

def extract_patch(image, position, block_size):
    x = position[1]
    y = position[0]
    
    width = x + block_size
    height = y + block_size
    
    return image[y:height, x:width]

def split_images_in_patches(image, block_size):

    width = image.shape[1]
    cols = width-block_size+1
    
    height = image.shape[0]
    rows = height-block_size+1
    
    patches = np.zeros((block_size, block_size, cols * rows))
    
    z=0
    for j in range(rows):
        for i in range(cols):
            patch = extract_patch(image, (j, i), block_size)
            patches[:,:, z] = patch
            z+=1
            
    return patches, cols, rows

def reduce_patches(patches):
    return np.sum(np.sum(patches, axis=1), axis=0).reshape(-1,1)