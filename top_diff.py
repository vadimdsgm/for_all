import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def getting_data(path):
    data = pd.read_csv(path, sep = ';')
    data.drop('date', inplace = True, axis = 1)
    return data

def creating_min_max_df(data):
    minimum = data.min()
    maximum = data.max()
    std_dev = (data.std() /data.max())
    min_max = pd.DataFrame(data=dict(mini=minimum, maxi=maximum, std = std_dev), index=minimum.index)
    min_max['diff'] = ((min_max.maxi - min_max.mini) / min_max.mini).mul(100).round(2)
    
    return min_max
    
def creating_top_diff_df(data):
    top = data.sort_values('diff', ascending = False).query(' diff > 5.5')\
                        .reset_index().rename(columns = {'index' : 'name'})

    return top

def top_csv_creation(data, path):
    data.to_csv(path, sep = ';')

def visualization(data, path_to_charts):
    sns.set(
    font_scale = 2,
    style      = 'whitegrid',
    rc         = {'figure.figsize' : (22, 10)}
    )

    ax = sns.barplot(x = 'diff', y = 'name', data = data)
    plt.savefig(path_to_charts)
                    

def main():
    path_to_stat = '..\\statistics\\price_statistics.csv'
    path_to_charts = '..\\statistics\\top_diff.png'
    path_to_top = '..\\statistics\\top_diff.csv'
    stat = getting_data(path_to_stat)
    mm = creating_min_max_df(stat)
    top_diff = creating_top_diff_df(mm)
    top_csv_creation(top_diff, path_to_top)
    visualization(top_diff, path_to_charts)
    
    return top_diff

top_diff = main()

if __name__=="__main__":
    print(top_diff)
