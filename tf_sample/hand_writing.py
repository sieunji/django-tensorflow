import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras


mnist = keras.dataset.mnist

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
mnist_idx =100

for row in train_images[mnist_idx]:
    for col in row:
        print("%10f"% col, end="")

    print('\n')

