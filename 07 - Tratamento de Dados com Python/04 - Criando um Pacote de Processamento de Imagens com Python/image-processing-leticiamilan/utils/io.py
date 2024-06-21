from skimage.io import imread, imsave

# lê a imagem
def read_image(path, is_gray = False):
    image = imread(path, as_gray = is_gray)
    return image

# salva a imagem
def save_image(image, path):
    imsave(path, image)