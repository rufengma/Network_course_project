import pandas as pd
import numpy as np
import glob
import re
Path = './renetwork/'
f = glob.glob(Path + '*.csv')
f.sort()
f

f_lst = ['./renetwork/chicago_result.csv',
    './renetwork/BAchicago_result.csv',
     './renetwork/ERchicago_result.csv',
 './renetwork/facebook_result.csv',
 './renetwork/BAfacebook_result.csv',
 './renetwork/ERfacebook_result.csv',
     './renetwork/friendship_result.csv',
     './renetwork/BAfriendship_result.csv',
     './renetwork/ERfriendship_result.csv',
 ]
 # initialize statistic data frame with all 9 csv file
df_names = []
for file in f_lst:
    df_names.append(re.findall(r'\w+_',file)[0]+'network')

stat_df = pd.DataFrame(data = {'networkName':df_names})
stat_df

# initialize statistic data frame with all 9 csv file
df_names = []
for file in f_lst:
    df_names.append(re.findall(r'\w+_',file)[0]+'network')

stat_df = pd.DataFrame(data = {'networkName':df_names})
stat_df

stat_df.to_csv('network_statistics.csv')
stat_df
# Plot the distogram
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import gamma, norm, lognorm
plt.figure()
df = pd.read_csv('./renetwork/BAchicago_result.csv')
a = df.Degree
f = sns.distplot(a, norm_hist = False)

for file in f_lst:
    plt.figure()
    df = pd.read_csv(file)
    a = df.Degree
    f = sns.distplot(a, norm_hist = False, kde = False, fit = gamma)
    
for file in f_lst:
    plt.figure()
    df = pd.read_csv(file)
    a = df.Degree
    f = sns.distplot(a, norm_hist = False, kde = False, fit = gamma)
    
    figure = f.get_figure()
    fig_name = re.findall(r'\w+_',file)[0]
    plt.title(fig_name+'Degree')
    figure.savefig(fig_name+"Degree.png")
    
real_list = ['./renetwork/chicago_result.csv',
 './renetwork/facebook_result.csv',
     './renetwork/friendship_result.csv',
 ]
 
 for file in f_lst:
    plt.figure()
    df = pd.read_csv(file)
    a = df.betweenesscentrality
    f = sns.distplot(a, norm_hist = False)
    figure = f.get_figure()
    fig_name = re.findall(r'\w+_',file)[0]
    plt.title(fig_name+'between Esscentrality')
    figure.savefig(fig_name+"Esscentrality.png")
 
 for file in f_lst:
    plt.figure()
    df = pd.read_csv(file)
    a = df.componentnumber.dropna()
    f = sns.distplot(a, norm_hist = False,kde=0)
    f.set_yscale('log')
    figure = f.get_figure()
    fig_name = re.findall(r'\w+_',file)[0]
    plt.title(fig_name+'component Number')
    figure.savefig(fig_name+"component Number")
    
import networkx as nx

edge_list = ['friendship.csv',
              'BAfriendship.csv',
             'ERfriendship.csv',
 'chicago.csv',
 'ERchicago.csv',
 'BAchicago.csv',
             'facebook.csv',
             'BAfacebook.csv',
             'ERfacebook.csv',]

def plot_graph_hist(file_name):
    g = nx.read_edgelist(file_name, create_using = nx.Graph(),delimiter = ',', nodetype = int)
    a = []
    for j in [i[1] for i in nx.shortest_path_length(g)]:
        a.extend(list(j.values()))
    length_lst = [i for i in a if i!=0]
    plt.figure()
    f = sns.distplot(a, bins = len(set(a)), norm_hist = 0, kde = 0, fit = norm )
    figure = f.get_figure()
    fig_name = file_name.split('.')[0]
    plt.title(fig_name+'Shortest Distance')
    figure.savefig(file_name+"_hist.png")
for file in edge_list:
    plot_graph_hist(file)
   

 
