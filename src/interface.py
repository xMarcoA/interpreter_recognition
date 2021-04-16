import argparse
import pickle

from sklearn.metrics import accuracy_score
from sklearn.compose import ColumnTransformer

from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn import set_config
from joblib import load

# function

def get_model(model):
    """ enter name of model to load it from hard drive """
    with open(str(model), 'rb') as file:
        model = pickle.load(file)
        return model

# import models 

random_forest = get_model('../models/model_ran.pickle')
logistic_regression = get_model('../models/model_log.pickle')

# make arguments
parser =  argparse.ArgumentParser()
parser.add_argument("-s", "--snipet", help="enter a song snipet", required=True) # input song lyrics 
parser.add_argument("-r", "--random", help="do you want to use the Random Rorest model? Press -r", action="store_false") # pick radnom forest ?
parser.add_argument("-l", "--logistic", help="do you want to use the Logistic Regression model? Press -l", action="store_false") # pick logistic regression ?
args = parser.parse_args()

# make predictions
prediction_random = random_forest.predict([args.snipet])
prediction_logistic = logistic_regression.predict([args.snipet])

#make outputs

if args.random == False:
    print("Random Forest says: "+prediction_random)
if args.logistic == False:
    print("Logistic Regression says: "+prediction_logistic)

# metavar='', makes the help desk cleaner  
# why programm doesnt like it?