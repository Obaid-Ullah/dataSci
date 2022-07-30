import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style='ticks',color_codes=True)

titanic = sns.load_dataset('titanic')
sns.catplot(x='sex',y='survived',hue='class',kind='bar',data=titanic)
plt.show()

# ---------------------
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style='ticks',color_codes=True)

titanic = sns.load_dataset('titanic')
p1= sns.countplot(x='sex',data = titanic,hue='class')
p1.set_title('Plot for counting')
plt.show()
# ---------------
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style='ticks',color_codes=True)

titanic = sns.load_dataset('titanic')
p1= sns.FacetGrid(titanic,row='sex',hue='alone')
p1=(p1.map(plt.scatter,'age','fare').add_legend())
plt.show()
# ---------------------

import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style='darkgrid',color_codes=True)
ship= sns.load_dataset('titanic')
p= sns.countplot(x='sex',data=ship,hue='class')
p.set_title('Basic count Plot')
plt.show()


