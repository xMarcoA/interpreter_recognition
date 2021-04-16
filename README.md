interpreter_recognition is a program that uses song snippets to predict an interpret from whom the snipet could be.
First, the lyrics of selected interpreters were scrapped with beautifulsoup from lyrics.com. Then the lyrics were broken down into individual words (word of bags). 2 machine models were trained with this bag to predict later the interpret.
Interface.py is a command line interface where you can enter a song snipet and choose a machine learning model.
You will receive the interpret from the selected model as an output.


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