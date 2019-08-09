import numpy as np #Numpy bir matematik kütüphanesi
import pandas as pd #Pandas düzgün veri çekebilmek için kullanılan kütüphane
import matplotlib.pyplot as plt #Matplotlib ise çizim yapabilmemiz için

data = pd.read_csv("linear.csv") #Veriyi alıyoruz.

x = data["metrekare"] #Metre kare sütununu x listesine alalım
y = data["fiyat"] #Aynı şeyi fiyat sütunu için yapalım.

x = np.array(x) #Listemizi bir diziye(matrise) dönüştürmüş oluyoruz.
y = np.array(y) #Aynı şekilde burda da yapıyoruz.

#Matris işlemine bu aşamada çevirmesek de olurdu. Sütunları direk aldığımız şakilde de kullabiliriz.

""""
x = pd.DataFrame(x).values 
y = pd.DataFrame(y).values 

#Values vir vektöre dönüştürüyor gibi. O yüzden kullanımı burda uygun değil.
# as_matrix metodu yerini values'e bırakmıştır.
"""
#plt.scatter(x,y)
#plt.show()
#Verilerin 2D görünümüne bakmak için yukarıdaki kodları kullanabiliriz.

#Doğrumuzun değeri w*a+b (w=ağırlık, b=bias değeri. Farklı şekillerde de yazılabilir. Doğru denklemi kısaca.)

w,b = np.polyfit(x,y,1)
# np.polyfit(x ekseni, y ekseni, kaçıncı dereceden polinom denklemi)
# Bu sayede numpy bizim için çizgimizi konumlandırıyor. Sonrasında adım adım optimum konuma yaklaşıcaz.


a = np.arange(175) #a'nın aralığını tanımladık.Bu doğrunun uzunluğunu temsil ediyor.

#plt.scatter(x,y) # Scatter ile nokta çizdirimi yapıyoruz.
#plt.plot(w*a+b) # Hypothesis yaklaşımına göre de optimum doğruyu çiziyor.
#plt.show()

g = int(input("Kaç metrekare ? : "))
istenilen = w*g+b

plt.scatter(x,y)
plt.plot(w*a+b)

plt.scatter(g,istenilen,c="red",marker=">") #İstenilen noktayı belli ettik.
plt.show()





