import wordcloud
import pandas as pd
import re
import nltk
import collections
from nltk.stem.wordnet import WordNetLemmatizer
import json
import csv


def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return nltk.corpus.wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return nltk.corpus.wordnet.VERB
    elif treebank_tag.startswith('N'):
        return nltk.corpus.wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return nltk.corpus.wordnet.ADV
    else:
        return ''


def word_segmentation(sentence):
    if len(sentence) < 5:
        return ''
    pat_letter = re.compile(r'[^a-zA-Z \']+')
    new_text = pat_letter.sub(' ', sentence).strip().lower()
    # to find the 's following the pronouns. re.I is refers to ignore case
    pat_is = re.compile("(it|he|she|that|this|there|here)(\'s)", re.I)
    # to find the 's following the letters
    pat_s = re.compile("(?<=[a-zA-Z])\'s")
    # to find the ' following the words ending by s
    pat_s2 = re.compile("(?<=s)\'s?")
    # to find the abbreviation of not
    pat_not = re.compile("(?<=[a-zA-Z])n\'t")
    # to find the abbreviation of would
    pat_would = re.compile("(?<=[a-zA-Z])\'d")
    # to find the abbreviation of will
    pat_will = re.compile("(?<=[a-zA-Z])\'ll")
    # to find the abbreviation of am
    pat_am = re.compile("(?<=[I|i])\'m")
    # to find the abbreviation of are
    pat_are = re.compile("(?<=[a-zA-Z])\'re")
    # to find the abbreviation of have
    pat_ve = re.compile("(?<=[a-zA-Z])\'ve")

    new_text = pat_is.sub(r"\1 is", new_text)
    new_text = pat_s.sub("", new_text)
    new_text = pat_s2.sub("", new_text)
    new_text = pat_not.sub(" not", new_text)
    new_text = pat_would.sub(" would", new_text)
    new_text = pat_will.sub(" will", new_text)
    new_text = pat_am.sub(" am", new_text)
    new_text = pat_are.sub(" are", new_text)
    new_text = pat_ve.sub(" have", new_text)
    new_text = new_text.replace('\'', ' ')
    word_list = new_text.split()
    lmtzr = WordNetLemmatizer()
    new_list = []
    for i in nltk.pos_tag(word_list):
        pos = get_wordnet_pos(i[1])
        if not pos == '':
            new_list.append(lmtzr.lemmatize(i[0], pos))
    return ' '.join(new_list)


def data_segment(filename):
    data = pd.read_csv(filename)[['eventid', 'summary']]
    data['segment'] = data['summary'].apply(word_segmentation)
    pd.DataFrame(data[['eventid', 'segment']]).to_csv('segment.csv', encoding='utf-8')


def frequency_statistics(filename):
    data = pd.read_csv(filename)
    text = ''
    for i in range(data.shape[0]):
        if not str(data.segment[i]) == 'nan':
            text += data.segment[i]
            text += ' '
            print(i)
    result = collections.Counter(text.split()).most_common()
    with open('frequency.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['id', 'word', 'frequency'])
        count = 0
        for i in result:
            if len(i[0]) > 2:
                writer.writerow([str(count), i[0], i[1]])
                count += 1
            if count == 3000:
                break
            print('write ', i)
        f.close()
    print(result)


def create_mapping(filename):
    mapping = {}
    word = pd.read_csv(filename, encoding='utf-8')
    word_index = {}
    for i in range(word.shape[0]):
        word_index[word.word[i]] = str(word.id[i])
    seg = pd.read_csv('segment.csv')
    for i in range(seg.shape[0]):
        word_list = []
        if str(seg.segment[i]) == 'nan':
            continue
        for item in seg.segment[i].split():
            if item in word_index:
                word_list.append(word_index[item])
        if not len(word_list) == 0:
            mapping[str(seg.eventid[i])] = word_list
        print(i)
    with open('mapping.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['eventid', 'word_id'])
        for id, words in mapping.items():
            writer.writerow([id, ' '.join(words)])
        f.close()


if __name__ == '__main__':
    # data_segment('data/data.csv')
    # frequency_statistics('segment.csv')
    create_mapping('frequency.csv')
