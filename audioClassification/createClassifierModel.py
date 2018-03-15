#!/usr/local/bin/python2
from pyAudioAnalysis import audioTrainTest as aT
import os
from sys import argv
import pydub

pydub.AudioSegment.converter = r"/Users/navrajnarula/Desktop/ffmpeg"

script, dirname = argv

subdirectories = os.listdir(dirname)
subdirectories.pop(0)

subdirectories = [dirname + "/" + subDirName for subDirName in subdirectories]

print(subdirectories)
aT.featureAndTrain(subdirectories, 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "svm", "svmModel", False)