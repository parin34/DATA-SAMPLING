import statistics
import random
import pandas as pd
import csv
import plotly.figure_factory as ff


df = pd.read_csv('data.csv')


data = df['temp'].tolist()


def random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data))
        value = data[random_index -1]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean


def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(mean_list)
   
    fig = ff.create_distplot([df],["tempreture"],show_hist=False)
    fig.show()

def setup():
    mean_list = []
    for i in range(0,100):
        set_of_mean = random_set_of_mean(30)
        mean_list.append(set_of_mean)
    show_fig(mean_list)
   
setup()




