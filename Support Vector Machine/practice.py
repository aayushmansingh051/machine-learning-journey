import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import make_classification
X,y=make_classification(n_samples=1000,n_features=2,n_classes=2,
                        n_clusters_per_class=2,n_redundant=0)
print(X)
print(y)
pd.DataFrame(X)[0]
sns.scatterplot(pd.DataFrame(X)[0],pd.DataFrame(X)[1],hue=y)