
from profanity_check import predict, predict_prob
import csv

#predict() takes an array and returns a 1 for each string if it is offensive, else 0.
#predict_prob() takes an array and returns the probability each string is offensive
#Examples
print(predict(['fuck you']))
print(predict_prob(['go to hell, you scum']))

with open('testdata.manual.2009.06.14.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print("Tweet-")
        print(f'{row[5]}.')
        print("Profanity Rating")
        print(predict([row[5]]))
        print(predict_prob([row[5]]))
    
