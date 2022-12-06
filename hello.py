
# in my case i have python 3.10.x installed which ist not stable yet, there are dependencie troubles.
# therefore i have to : $conda activate py3k, which is a virtual enviroment running python 3.9.15 where everything runs smooth.
import flair
from flair.data import Sentence
from flair.models import SequenceTagger

tagger = SequenceTagger.load('ner')
sentence = Sentence('Hallo Stefan. this is your little hello world example from Erding in Bayern.')
tagger.predict(sentence)

print('Flairs Version is:  {}!'.format(flair.__version__))
for entity in sentence.get_spans('ner'):
    print(entity)