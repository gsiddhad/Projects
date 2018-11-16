# stemmer.py / Stemmer
# Gourav Siddhad
# 07-04-2018

import re
import codecs
import string

class Stemmer():
    stems = []
    input, output, rem = '', '', ''

    def stem_init(self, input):
        self.input, self.output = input, input
        with codecs.open("stems.txt", encoding="utf-8", mode="r") as fin :
            for line in fin :
                self.stems.append(re.sub(' +', ' ', line.strip()))
        fin.close()

    def hstem(self):
        for stem in self.stems :
            if self.input.endswith(stem) :
                self.rem = stem
                self.output = self.input.replace(stem, '')
                break
        print ("%s = %s + %s" % (self.input, self.output, self.rem))
        return self.output
