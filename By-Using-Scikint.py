import numpy as np #Numpy bir matematik kütüphanesi
import pandas as pd #Pandas düzgün veri çekebilmek için kullanılan kütüphane
from sklearn.linear_model import LinearRegression as lr
import matplotlib.pyplot as plt #Matplotlib ise çizim yapabilmemiz için

data = pd.read_csv("linear.csv") #Veriyi alıyoruz.

x = data["metrekare"] #Metrekare sütununu x listesine alalım
y = data["fiyat"] #Aynı şeyi fiyat sütunu için yapalım.

x = np.array(x) #Listemizi bir diziye(matrise) dönüştürmüş oluyoruz.
y = np.array(y) #Aynı şekilde burda da yapıyoruz.

x = x.reshape(99,1) #99x1'lik bir matris haline getiriyoruz.
y = y.reshape(99,1)

lin = lr()

lin.fit(x,y) # x ve y'yi grafiğe yerleştirdik.

lin.predict(x) # x eksenine göre tahmin ettiricez
#burda w ve b değlerini kendi kendine buluyor.

w = lin.coef_ #x'i kestiği yer
b = lin.intercept_ #y'yi kestiği yer

a = np.arange(150) #Uzunluğunu belli ediyoruz.

plt.scatter(x,y)
plt.scatter(a,w*a+b, c="red")
plt.show()




