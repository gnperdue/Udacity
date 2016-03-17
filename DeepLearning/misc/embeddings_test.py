#!/usr/bin/env python
from __future__ import print_function
import collections
import math
import numpy as np
import os
import random
import zipfile
from matplotlib import pylab
from six.moves import range
from six.moves.urllib.request import urlretrieve
from sklearn.manifold import TSNE


def read_data(filename):
    with open(filename, 'r') as f:
        return f.read().split()


def build_dataset(words):
    vocabulary_size = 50000
    count = [['UNK', -1]]
    count.extend(collections.Counter(words).most_common(vocabulary_size - 1))
    dictionary = dict()
    for word, _ in count:
        dictionary[word] = len(dictionary)
    data = list()
    unk_count = 0
    for word in words:
        if word in dictionary:
            index = dictionary[word]
        else:
            index = 0  # dictionary['UNK']
            unk_count = unk_count + 1
        data.append(index)

    count[0][1] = unk_count
    reverse_dictionary = dict(zip(dictionary.values(), dictionary.keys()))
    return data, count, dictionary, reverse_dictionary

filename = 'loremipsum.txt'
words = read_data(filename)
print('Data size %d' % len(words))
data, count, dictionary, reverse_dictionary = build_dataset(words)
print('Most common words (+UNK)', count[:5])
print('Sample data', data[:10])

data_index = 0


def generate_batch(batch_size, num_skips, skip_window):
    """
    batch_size  - 10
    num_skips   - 2
    skip_window - 5
    """
    # let's keep track of where we are in the data
    global data_index
    # the batch size must be evenly divisible by the number of skips
    assert batch_size % num_skips == 0
    assert num_skips <= 2 * skip_window
    batch = np.ndarray(shape=(batch_size), dtype=np.int32)
    labels = np.ndarray(shape=(batch_size, 1), dtype=np.int32)
    # how much data do we traverse per skip?
    span = 2 * skip_window + 1  # [ skip_window target skip_window ]
    # hold the data for the minibatch
    buffer = collections.deque(maxlen=span)
    # fill the buffer with the next `span` words of data
    for _ in range(span):
        buffer.append(data[data_index])
        data_index = (data_index + 1) % len(data)
    for i in range(batch_size // num_skips):
        target = skip_window  # target label at the center of the buffer
        targets_to_avoid = [skip_window]
        for j in range(num_skips):
            # find a target that isn't in our "avoid" list
            while target in targets_to_avoid:
                target = random.randint(0, span - 1)
            # put the selected target in our list to avoid
            targets_to_avoid.append(target)
            batch[i * num_skips + j] = buffer[skip_window]
            labels[i * num_skips + j, 0] = buffer[target]
        buffer.append(data[data_index])
        data_index = (data_index + 1) % len(data)
    return batch, labels

print('data:', [reverse_dictionary[di] for di in data[:8]])

for num_skips, skip_window in [(2, 1), (4, 2)]:
    data_index = 0
    batch, labels = generate_batch(batch_size=8,
                                   num_skips=num_skips,
                                   skip_window=skip_window)
    print('\nwith num_skips = %d and skip_window = %d:' %
          (num_skips, skip_window))
    print('    batch:', [reverse_dictionary[bi] for bi in batch])
    print('    labels:', [reverse_dictionary[li] for li in labels.reshape(8)])
