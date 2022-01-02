import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import rcParams

f = open('d:/Projects/WebDev Intro/webscraping-scrapy-letterboxd//letterboxd/scraped.json')

df = pd.read_json(f)

df = df['country']
df = [item for sublist in df for item in sublist]
df = pd.DataFrame(df)
df.rename(columns={0:'Country'}, inplace=True)
df = df.value_counts().reset_index(name='Movie Count')

sns.set_theme()

# configure font
rcParams['font.family'] = ['sans-serif']
rcParams['font.sans-serif'] = ['Trebuchet MS']

plt.figure(figsize=[10,5])
fig = sns.barplot(data=df[:9], x="Country", y="Movie Count", color='darkolivegreen')
plt.xticks(rotation=-20)
plt.title("Top 10 Countries of Origin", fontsize=15, y=1.05, loc="left")

# save plot figure
plt.savefig("./results/6_country_distribution.png", facecolor='w', bbox_inches='tight', pad_inches=0.5, dpi=300)

print("6_country_distribution.png generated.")