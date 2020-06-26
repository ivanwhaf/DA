import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
sns.set()

#data=np.arange(10)
#plt.plot(data)

data=sns.load_dataset('fmri')
sns.lineplot(x='timepoint', y='signal', hue="region",style="event",data=data)
plt.show()


#plt.show()