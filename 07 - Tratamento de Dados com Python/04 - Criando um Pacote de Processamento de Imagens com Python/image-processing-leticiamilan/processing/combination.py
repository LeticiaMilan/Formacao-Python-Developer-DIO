import numpy as np
from skimage.color import rgb2gray
from skimage.exposure import match_histograms
from skimage.metrics import structural_similarity

# verifica a diferença entre duas imagens
def find_difference(image1, image2):
    assert image1.shape == image2.shape, "Imagem 1 e Imagem 2 devem ter o mesmo tamanho."

    # conversão para escala de cinza
    gray_image1 = rgb2gray(image1)
    gray_image2 = rgb2gray(image2)

    # cálculo da similaridade estrutural variando de 0 a 1
    (score, difference_image) = structural_similarity(gray_image1, gray_image2, full=True)

    print("Similaridade entre as imagens: ", score)

    # normalização da diferença
    normalized_difference_image = (difference_image-np.min(difference_image))/(np.max(difference_image)-np.min(difference_image))

    return normalized_difference_image

# combina as duas imagens
def transfer_histogram(image1, image2):
    matched_image = match_histograms(image1, image2, multichannel=True)
    return matched_image