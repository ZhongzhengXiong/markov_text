# -*- coding:utf-8 -*-
"""
基于Markov过程的文本生成:
markov_dict:  { 'word': [next_words.....], ..... }
"""

import os
import random

markov_dicts = {'':[]}   # Start of Sentence
sentence_sep = '.?!'    # 句子结束标志

def parse(text):
    """ 分析text，产生相应的dict"""
    aList = text.split()
    markov_dicts[''].append(aList[0])
    for i in range(0, len(aList)-1):
        if aList[i][len(aList[i])-1] in sentence_sep:
            markov_dicts[''].append(aList[i+1])
        else:
            markov_dicts[aList[i]] = markov_dicts.get(aList[i], [])
            markov_dicts[aList[i]].append(aList[i+1])
    
    pass

def generate(num_sentences=1, word_limit=20):
    """ 根据前面调用parse得到的dict，随机生成多个句子"""
    sList = []
    for i in range(0, num_sentences):
        word_num = 0
        wList = []
        word = ''
        while markov_dicts.get(word, []) != [] and word_num <= word_limit:
            aList = markov_dicts.get(word, [])
            word = aList[random.randint(0, len(aList)-1)]
            wList.append(word)
            word_num = word_num+1
        sList.append(' '.join(wList))
    return '\n'.join(sList)
    pass

def markov_main():
    f = open('beatles.txt', 'r')
    text= f.read()
    f.close()
    parse(text)
    print(generate(10))
   

if __name__ == '__main__':
    markov_main()
