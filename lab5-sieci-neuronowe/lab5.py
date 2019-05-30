import keras.applications.mobilenet_v2 as k_mobilenet_v2
import keras.backend as k
import keras.datasets.mnist as k_mnist
import keras.layers as k_layers
import keras.losses as k_losses
import keras.models as k_models
import keras.optimizers as k_optimizers
import keras.preprocessing.image as k_image
import keras.utils as k_utils

import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import ImageGrid

import numpy as np

import tensorflow as tf

from PIL import ImageDraw, Image
import copy

def visualise_process(model, x, layers_range):

    layers_num = len(layers_range)
    code = layers_num * 100 + 10

    if layers_num > 9:
        print("Too many layers requested")
        return

    fig = plt.figure()
    i = 1
    for layer_index in layers_range:
        layer = model.layers[layer_index]
        unit = layer.output_shape[-1]

        columns = 16 if unit // 16 > 0 else unit % 16
        rows = min(2, unit // 16 + np.sign(unit % 16))
        grid = ImageGrid(fig, code + i,
                    nrows_ncols=(rows, columns),
                    axes_pad=0.0,
                    label_mode="1"
                    )

        for channel in range(min(32, layer.output_shape[-1])):
            get_activations = k.function([model.layers[0].input], [layer.output])
            activations = get_activations([x])
            grid[channel].imshow(activations[0][0, :, :, channel], interpolation="nearest", cmap="viridis")

        i += 1

    plt.show()

def grey_square():
    square_size = 56
    input_size = 224
    step = 12
    color = 0xd3d3d3

    # pobranie sieci
    model = k_mobilenet_v2.MobileNetV2(weights='imagenet', include_top=True)
    # załadownie zdjęcia
    image_path = 'ship.jpg'
    image = k_image.load_img(image_path, target_size=(input_size, input_size))
    x = k_image.img_to_array(image)
    x = np.expand_dims(x, axis=0)
    x = k_mobilenet_v2.preprocess_input(x)

    fig = plt.figure()
    ax1 = fig.add_subplot(1, 3, 1)
    ax1.imshow(image)

    predictions = model.predict(x)
    percentage = k_mobilenet_v2.decode_predictions(predictions, top=1)[0][0][2]
    label = k_mobilenet_v2.decode_predictions(predictions, top=1)[0][0][1]

    fig.suptitle(label)

    # show image with example square
    im_copy = copy.deepcopy(image)
    draw = ImageDraw.Draw(im_copy)
    x = input_size // 3
    y = input_size // 3
    draw.rectangle((x - square_size/2, y - square_size/2, x + square_size/2, y + square_size/2), fill=color, outline=color)
    ax2 = fig.add_subplot(1, 3, 2)
    ax2.imshow(im_copy)

    heatmap = Image.new('L', image.size, (0))
    heatmap_draw = ImageDraw.Draw(heatmap)

    print("Starting checking...")
    for x in range(0, input_size, step):
        for y in range(0, input_size, step):
            im_copy = copy.deepcopy(image)
            draw = ImageDraw.Draw(im_copy)
            draw.rectangle((x - square_size/2, y - square_size/2, x + square_size/2, y + square_size/2), fill=color, outline=color)
            x2 = k_image.img_to_array(im_copy)
            x2 = np.expand_dims(x2, axis=0)
            x2 = k_mobilenet_v2.preprocess_input(x2)

            predictions_square = model.predict(x2)
            percentage_square = 0
            for pred in k_mobilenet_v2.decode_predictions(predictions_square, top=10)[0]:
                if pred[1] == label:
                    percentage_square = pred[2]

            diff = percentage - percentage_square
            if diff < 0:
                diff = 0
            diff = int(diff * 255)
            heatmap_draw.rectangle((x - step/2, y - step/2, x + step/2, y + step/2), fill=(diff, ), outline=(diff, ))

    ax2 = fig.add_subplot(1, 3, 3)
    ax2.imshow(heatmap)

    plt.show()

def art_style():
    model = k_vgg19.VGG19()


def main():
    # grey_square()
    art_style()

if __name__ == "__main__":
    main()