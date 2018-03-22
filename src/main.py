import nltk
import re
import os
import itertools


def parse_files(filepaths):
    white_space_regex = re.compile(r'([\n\t ]+)', re.MULTILINE)
    parsed_data = []
    for fpath in filepaths:
        with open(fpath, 'r') as f:
            parsed_data.append([nltk.word_tokenize(sent) for sent in nltk.sent_tokenize(re.sub(white_space_regex, ' ', f.read()).strip())])
    return '\n\n'.join(['\n'.join([' '.join(sent) for sent in file]) for file in parsed_data])


if __name__ == '__main__':
    data_source = './../../text_reconstruction/dataset/Gutenberg/txt/'
    all_files = os.listdir(data_source)
    training_files = all_files[:100]

    test_files = all_files[100:105]

    train_data = parse_files([data_source + fname for fname in training_files])
    test_data = parse_files([data_source + fname for fname in test_files])

    with open('training_file.txt', 'w') as f:
        f.write(train_data)
    with open('testing_file.txt', 'w') as f:
        f.write(test_data)
