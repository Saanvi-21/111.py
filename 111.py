import plotly.figure_factory as ff
import plotly.graph_objects as go 
import statistics
import random
import pandas as pd 
import csv 

df = pd.read_csv('student_activity2.csv')
data = df['Math_score'].tolist()

fig = ff.create_distplot([data], ['math scores'], show_hist=False)
fig.show()

mean = statistics.mean(data)
std_deviation = statistics.stdev(data)
print('Mean of score is:- ', mean)
print('Standard deviation of score is:- ', std_deviation)
def random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

mean_list = []
for i in range(0,1000):
    set_of_mean = random_set_of_mean(100)
    mean_list.append(set_of_mean)
std_deviation = statistics.stdev(mean_list)
fig = ff.create_distplot([mean_list], ['Student Marks'], show_hist=False)
fig.add_trace(go.scatter(x = [mean,mean], y = [0,0.20], mode = 'lines', name = 'Mean'))
fig.show()

