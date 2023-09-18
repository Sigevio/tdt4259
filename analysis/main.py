import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import model as m
import pandas as pd
import seaborn as sns

def draw(data, x, y, hue):
    sns.set_theme(style="darkgrid")
    plot = sns.lineplot(x=x, y=y, hue=hue, data=data)
    new_xticklabels = [item.get_text()[:10] for item in plot.get_xticklabels()]
    plot.set_xticks(plot.get_xticks())
    plot.set_xticklabels(new_xticklabels)
    plot.xaxis.set_major_locator(ticker.LinearLocator(10))
    plt.xticks(rotation=12)
    plt.tight_layout()

if __name__ == '__main__':

    data = pd.read_csv('analysis/consumption_temp.csv')
    data_consumption = data.drop(columns=["temperature"])
    data_temp = data.drop(columns=["consumption"])
    
    plt.figure(figsize=(10, 5))
    draw(data_consumption, "time", "consumption", "location")
    plt.figure(figsize=(10, 5))
    draw(data_temp, "time", "temperature", "location")
    plt.show()
