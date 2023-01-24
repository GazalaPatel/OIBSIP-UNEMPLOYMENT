import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("Unemployment in India.csv")
print(df)
print(df.shape)
print(df.info)
print(df.describe())
print(df.isnull)
print(df.corr())
sns.heatmap(df.corr(),cmap="GnBu",annot=True)
plt.show()
df.columns= ["Region","Date","Frequency","  Unemployment Rate (%)","Estimated Employed",
             "Estimated Labour Participation Rate (%)","Area"]
plt.figure(figsize=(5, 5))
plt.title("Indian Unemployment")
sns.histplot(x="Estimated Employed", hue="Region", data=df)
plt.show()
plt.figure(figsize=(5, 5))
plt.title("Indian Unemployment")
sns.histplot(x="Estimated Labour Participation Rate (%)", hue="Region", data=df)
plt.show()