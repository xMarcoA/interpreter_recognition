interpreter_recognition is a program, that uses song snippets to predict the interpret.


lyrics_collector.py:
    - scrape lyrics from lyrics.com with beautifulsoup
    - save it as csv files on the hard drive

model.ipynb:
    - read in lyrics.csv and split the songs into a word of bag
    - trained 2 classification models(random forest and logistic regression) with the word of bag
    - upload the models

interface.py:
    - read in the 2 trained models
    - bash command line interface to enter song snipets and choose a model to get a prediction

data source: 
    - lyrics.com

screenshot of bash command line interface:
![Bildschirmfoto 2021-04-15 um 17 26 38](https://user-images.githubusercontent.com/76050281/114985976-b6d92f80-9e93-11eb-8be1-0db3ef64d749.png)
