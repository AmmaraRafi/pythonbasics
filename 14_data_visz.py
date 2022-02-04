import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="ticks", color_codes=True)
kashti=sns.load_dataset("titanic")
print(kashti)

p=sns.countplot(x="sex",data=kashti, hue="alone")
p.set_title("count plot")
plt.show()

