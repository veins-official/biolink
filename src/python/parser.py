import numpy as np
import gzip


def get_images(count):
    file = gzip.open("data/mnist.gz", "r")
    size = 28
    
    file.read(16)
    buf = file.read(size * size * count)
    data = np.frombuffer(buf, dtype=np.uint8).astype(np.float64)
    data = data.reshape(count, size * size)
    
    return data
    
