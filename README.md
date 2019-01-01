# mood-class

<i>mood-class</i> is a classification tool that accepts inputs in the form of audio files and returns outputs in the form of text labels, corresponding to one in five emotion classes:
> anger 
> disgust 
> fear
> happiness
> sadness

Have a speech utterance you'd like to know the overall tone of? Read on to learn more about how to use <i>mood-class</i>!

## Getting Started

These next set of instructions will help you get a copy of mood-class and its corresponding requirements installed on your local machine.

### Prerequisites

#### Python
<i>mood-class</i> and its various dependencies are all built on top of Python. If you do not have Python installed on your machine, follow this [guide](https://wsvincent.com/install-python3-mac/) on how to do so via Homebrew. <i>mood-class</i> will run on Python versions 3 or higher.

#### Python Libraries
We'll be making use of several Python libraries to get our classifier to work. We can use pip to pre-install these. 
```
pip install numpy matplotlib scipy sklearn hmmlearn simplejson eyed3 pydub
```
If you don't have pip installed, you can check out the documentation for how to do so [here](https://pip.pypa.io/en/stable/installing/). The above list of libraries are courtesy of [pyAudioAnalysis](https://github.com/tyiannak/pyAudioAnalysis), which is the framework we will use to perform the classification task. 

### Installations and Set Up

#### Clone this repository

Navigate to your preferred directory location and clone this repository.

```
git clone https://github.com/navierula/mood-class
```
#### Clone pyAudioAnalysis

```
git clone https://github.com/tyiannak/pyAudioAnalysis
```
Make sure that you place this repository within your <i>mood-class</i> directory, specifically where you will choose to perform the classification task. For reference, my placement looks like this:
```
mood-class/
|_audioClassication/
|__pyAudioAnalysis/
```

#### Update path in `bashrc` file

In order to get pyAudioAnalysis to work, you would need to update the Python path in your `bashrc` file. You can access this hidden file via your terminal by any text editor of your choice. Here's how you might edit the file using emacs:

```
emacs .bashrc
```
Once you have the file open, set the Python path to where you saved pyAudioAnalysis locally. 

```
export PYTHONPATH=$PYTHONPATH:"/Users/navrajnarula/Desktop/audioClassification/pyAudioAnalysis
```

To update these specifications, specify the source in your terminal.

```
source ~/.bashrc
```
#### Download FFmpeg 

FFmpeg is a free software that is designed for command-line-based processing of audio files. Since our classifier works with audio files, I would suggest downloading FFmpeg [here](https://www.ffmpeg.org/download.html) to avoid trivial errors when it comes to reading in inputs. 

## Running <i>mood-class</i>

Now that everything has been set up on your local machine, we can go ahead and run the classifier!

### Data

You can use any audio data that you have available for this classifier. Since my focus is on emotional analysis, I utilized [CREMA-D](https://github.com/CheyneyComputerScience/CREMA-D). This dataset contains over 7,000 instances of speech utterances delivered by actors that fall into labeled categories of anger, disgust, fear, happiness, and sadness. To obtain the full dataset, head on over to CREMA-D's repository and download the data using [Git Large File Storage](https://git-lfs.github.com/). 

For testing purposes, I have included a small subset of CREMA-D's files in the `praat_viz` directory of my repository, which are distinguished by male and female voices. This is further broken down by emotion, as stated within each file name.

```
mood-class/
|_audioClassification/
|__trainingdata/
|___anger/
|___disgust/
|___fear/
|___happiness/
|___sadness/
```
Note that pyAudioAnalysis will work on both `.mp3` and `.wav` files. My training files are in `.wav` format.

### Train Data

`mood-class` currently uses an SVM model in this example, but if you prefer to use another one, check out [pyAudioAnalysis](https://github.com/tyiannak/pyAudioAnalysis) for varying models it may support. To train `mood-class` on your training data, simply run this command:

```
python createClassifierModel.py trainingData
```
`trainingData` is the directory I have stored my training files in.

Once the data is trained, you'll see a contingency table representing the output.

```
dis  fear  hap  
dis  16.67  1.67  2.75  
fear  5.08  11.08  5.67  
hap  4.00  5.92  13.50  
```
The above displays the matrix for disgust, fear, and happiness.

### Testing Data

`mood-class` will categorize any audio file into any of your labeled dataset. 

```
python testClassifierModel.py happiness_test.wav
```
Passing in an untrained angry file to `mood-class` returns the probability for which class my file would fall into:

```
classNames is ['disgust', 'fear', 'happiness']
P is [0.01042657 0.04208108 0.94749235]
result is 2.0

File: happiness_test.wav is in category: happiness, with probability:  0.94749235
```


<b> This project is authored and maintained by Navie Narula. New contributors and pull requests are welcome!</b>
