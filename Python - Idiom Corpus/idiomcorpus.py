# idiomcorpus.py / Idiom Corpus
# Gourav Siddhad
# 07-04-2018

import codecs
import re
import codecs
import string
from mtranslate import translate

class Idiomcorpus() :
    flag = False
    hindi, english = [], []
    input, output = '', ''
    hidiom, eidiom = '', ''

    def idiom_init(self, sentence) :
        if self.flag is False:
            self.flag = True
            with codecs.open("idioms.txt", encoding="utf-8", mode="r") as fin :
                for line in fin :
                    a, b = line.split('-')
                    self.hindi.append(re.sub(' +', ' ', a.strip()))
                    self.english.append(re.sub(' +', ' ', b.strip()))
            fin.close()
            self.input = sentence
            self.input = re.sub(' +', ' ', self.input.strip())

    def idiom_tokenize(self, sentence):
        tokens, word = [], []
        for char in sentence :
            if char == ' ':
                tokens.append(''.join(word))
                word = []
            else :
                word.append(char)
        tokens.append(''.join(word))
        return tokens

    def check_idiom(self):
        unicount, uniidiom = 0, ''
        inputtoken = list(set(self.idiom_tokenize(self.input)))
        for idiom in self.hindi :
            idiom = re.sub(' +', ' ', idiom.strip())
            idiomtoken = list(set(self.idiom_tokenize(idiom)))
            counter = self.idiom_match(inputtoken, idiomtoken)
            if counter <= len(inputtoken) and counter <= len(idiomtoken):
                if counter > unicount and len(idiomtoken) <= len(inputtoken):
                    unicount = counter
                    uniidiom = idiom
                    print (idiom)
        self.hidiom = uniidiom
        return self.hidiom

    def idiom_convert(self):
        if not self.hidiom:
            self.eidiom = ''
        else:
            self.eidiom = self.english[self.hindi.index(self.hidiom)].split(' ')
        return self.eidiom

    def idiom_match(self, input, idiom):
        counter = 0
        if idiom[0] in input:
            for token in idiom:
                if token in input:
                    counter += 1
        return counter

    def idiom_display(self):
        inputsplit = self.idiom_tokenize(self.input)
        hidiomsplit = self.idiom_tokenize(self.hidiom)
        eidiomsplit = self.idiom_tokenize(self.eidiom)
        outputsplit = inputsplit

        if hidiomsplit[0] in inputsplit:
            temp = inputsplit.index(hidiomsplit[0])
            for word in self.eidiom:
                outputsplit[temp] = word
                temp += 1

            for word in hidiomsplit:
                if word in inputsplit:
                    outputsplit.remove(word)
        else :
            self.hidiom = ''
            self.eidiom = 'Not Found'

        self.output = ' '.join(outputsplit)
        self.output = translate(self.output, 'en')
        print (self.output)
        return self.output
