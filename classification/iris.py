import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import perceptron_cls as ppn
# import Adaline as ppn
from matplotlib.colors import ListedColormap

def plot_decision_regions(X, y, classifier, resolution=0.01):
    markers = ('s', 'x', 'o', '^', 'v')
    colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])    
    x1_min, x1_max = X[:,0].min() - 1,X[:,0].max() + 1
    x2_min, x2_max = X[:,1].min() - 1,X[:,1].max() + 1
    # xx1 圖面上所有x點 ==> x1 * x2 矩陣中,只取x1所構成的矩陣
    # xx2 圖面上所有y點 ==> x1 * x2 矩陣中,只取x2所構成的矩陣
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
                           np.arange(x2_min, x2_max, resolution))
    # np.array([xx1.ravel(),xx2.ravel()]).T 將xx1,xx2的資料合併變成一個個的座標點(xx1,xx2)
    # classifier.predict(np.array([xx1.ravel(),xx2.ravel()]).T) 將一個個的座標點轉換為 1 or  -1(感知器的輸出)
    z = classifier.predict(np.array([xx1.ravel(),xx2.ravel()]).T)
    # 將感知器的輸出轉成 x1 * x2 矩陣, 因此每一個座標都可以mapping到輸出值
    z = z.reshape(xx1.shape)
    
    plt.contourf(xx1, xx2, z, alpha=0.4, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())

    # y 即是分類結果，此範例有[1, -1]
    for idx, cl in enumerate(np.unique(y)):
        # 將分類結為1的點畫一顏色，-1的對畫另一個顏色
        plt.scatter(x=X[y ==cl, 0],y=X[y == cl, 1],alpha=0.0, c=cmap(idx), marker=markers[idx], label=cl)
    


df=pd.read_csv('iris.data',header=None)
y = df.iloc[0:100,4].values
y = np.where(y == 'Iris-versicolor' ,-1,1)
X = df.iloc[0:100,[0,2]].values # get first 100 rows and col0 and col2


ppn = ppn.Perception(0.1 ,20)
# ppn = ppn.Adaline(0.1 ,20)
ppn.fit(X,y)

print(ppn.w_)

plt.plot(range(1,len(ppn.errors_)+1),ppn.errors_,marker='.')
plt.plot(range(1,len(ppn.errors_)+1),ppn.errors_,marker='.')
plt.xlabel('Epochs')
plt.ylabel('Nmber of misclassifications')
plt.title('{:.2f} * petal_length + {:.2f} * sepal_length - {:.2f}'.format(ppn.w_[1],ppn.w_[2],ppn.w_[0]))
plt.show()




plt.scatter(X[0:50,0], X[0:50,1], marker="x", color='red', label='setosa')
plt.scatter(X[50:100,0], X[50:100,1], marker="o", color='blue', label='versicolor')
plot_decision_regions(X, y, classifier=ppn)
plt.xlabel('petal length')
plt.ylabel('sepal length')
plt.legend(loc="upper left")
plt.show()




