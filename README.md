# Audio Classification of Emotional Inputs

My master's thesis at Columbia University explores the intersection of speech language processing and journalism: How can speech or audio analysis be used to further a written piece?<br>

In order to partly answer this question, I utilized [pyAudioAnalysis](https://github.com/tyiannak/pyAudioAnalysis) to build a classifier that would categorize short utterances into
one of five emotional categories: anger, disgust, fear, happiness, and sadness.<p>

The training data that I used for classifier came from the [CREMA-D](https://github.com/CheyneyComputerScience/CREMA-D) dataset. I only uploaded a small number of training files to this particularly repository because it is unable to handle a large amount of data without Git Large File Storage. In order to run my classifier, follow these instructions:

1. Download the repository

2. Download [pyAudioAnalysis](https://github.com/tyiannak/pyAudioAnalysis) onto your own computer and place it into the pyAudioAnalysis folder within the AudioClassification folder.

3. Update the path in your bashrc file to point towards pyAudio Analysis. Mine looks like this: `export PYTHONPATH=$PYTHONPATH:"/Users/navrajnarula/Desktop/audioClassification/pyAudioAnalysis`

4. Update the specifications in your terminal. I would do this:
`source ~/.bashrc`

5. Now, run the classifier on the training and testing inputs I provided or ones you provide yourself! :)

##### Project by: Navraj Narula

