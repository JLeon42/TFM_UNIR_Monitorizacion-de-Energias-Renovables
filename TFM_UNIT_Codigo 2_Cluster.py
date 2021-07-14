#Librerias basicas para Machine Learning
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.core.frame import DataFrame
from scipy.sparse import data
import seaborn as sb
import matplotlib.cm as cm

#Librerias de Scikit-Learn
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin_min
from sklearn.metrics import silhouette_samples, silhouette_score
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score

#Librerias para graficos
from mpl_toolkits.mplot3d import Axes3D
plt.rcParams['figure.figsize'] = (16,9)
plt.style.use('ggplot')


#1. Lectura de archivo modelo .CSV
dataframe = pd.read_csv(r"C:\\Users\\Adonis\\Desktop\\Grid.csv")
print('     Data:')
print(dataframe.head())



#2. NORMALIZACION
#Determinando el numero de SUN mas alto para cada region
SUN_MAX = dataframe.groupby(['Region Num','Region']).SUN.agg(SUN_Maximo = 'max')
print('SUN_MAX')
print(SUN_MAX)

#Determinando el numero de OTHER mas alto para cada region
WIND_MAX = dataframe.groupby(['Region Num','Region']).WIND.agg(WIND_Maximo = 'max')
print('WIND MAX')
print(WIND_MAX)


#Determinando el numero de OTHER mas alto para cada region
OTHER_MAX = dataframe.groupby(['Region Num','Region']).OTHER.agg(OTHER_Maximo = 'max')
print('OTHER MAX')
print(OTHER_MAX)


#ANEXANDO LOS VALORES MAXIMOS A LA DATA ORIGINAL
data = dataframe
data = pd.merge(data,SUN_MAX,on = 'Region', how='inner')
data = pd.merge(data,WIND_MAX,on = 'Region', how='inner')
data = pd.merge(data,OTHER_MAX,on = 'Region', how='inner')
print(data)
print()

#Realizando la Division para la Normalizacion
print('... Iniciando normalizacion')
data['SUN_NORM'] = data['SUN'] / data['SUN_Maximo']
data['WIND_NORM'] = data['WIND'] / data['WIND_Maximo']
data['OTHER_NORM'] = data['OTHER'] / data['OTHER_Maximo']
print(data)
print()
#Chequeo de valores NaN
print('Chequeo de valores Null')
print(data.isnull().sum())
print()
print('Correccion de valores Null')
#Data corregida y normalizada
data = data.fillna(0)
print(data.isnull().sum())

#Impresion de datos para chequeo
#data.to_csv(r'C:\Users\Adonis\Desktop\data.csv', index = True)





##############################################
#******************Creando copia especial
Model_Cluster = data.copy()
############################################
#******************Generando unicamente las primeras 5000 instancias por Region
Model_Cluster = Model_Cluster[Model_Cluster['Index'].between(0,6000)]
print('Impresion de Model_Cluster para MODELADO')
print(Model_Cluster)
Model_Cluster.to_csv(r'C:\Users\Adonis\Desktop\Model_Cluster.csv', index = True)

#*****************Haciendo el array de elementos para el Model_Cluster
# #Array de elementos
X_Model_Cluster = np.array(Model_Cluster[["WIND_NORM","OTHER_NORM",'SUN_NORM']])

###############################################




#3. Grafico de Dispersion de datos
data.drop(['Index','Date', 'NET','SUN','WIND','OTHER','Region','Region Num','SUN_SAVED_CO2','WIND_SAVED_CO2','OTHER_SAVED_CO2','TOTAL_SAVED_CO2','TOTAL_EMITED_CO2','FOSIL_CO2','SUN_Maximo','WIND_Maximo','OTHER_Maximo'],1).hist(color = 'lightblue', edgecolor='black')
plt.show()



#4. Realizando modelo
# #Array de elementos
X = np.array(data[["WIND_NORM","OTHER_NORM",'SUN_NORM']])

#
#RESIZE
print('     Forma de X:')
print(X.shape)
print(X)

#
#Anexando aleatoriedad
X_train, X_validation = train_test_split(X, test_size=0.2, random_state=1, shuffle=True)
print('X_Train')
print(X_train.shape)
print('X_validation')
print(X_validation.shape)






#########################################################################################
#ELBOW METHOD
#PUNTO CODO

Nc = range(1, 15)
kmeans = [KMeans(n_clusters=i) for i in Nc]
score = [kmeans[i].fit(X_Model_Cluster).score(X_Model_Cluster) for i in range(len(kmeans))]
plt.plot(Nc,score, color = 'lightblue', linewidth=3)
plt.xlabel('Número de Clusters')
plt.ylabel('Inercia')
plt.title('Seleccion de número de clusters: Método del codo')
plt.show()













#5. Aplicacion del modelo
#Aplicacion del modelo
#init='random' escoje las filas a modelar de manera aleatoria para los centroides iniciales
#n_clusters = numero de centroides a realizar
#random_state = generacion de numero aleatorio para la inicializacion de centroide
kmeans = KMeans(n_clusters=6, init='random', n_init=10, random_state=None, algorithm='elkan').fit(X_train)
centroids = kmeans.cluster_centers_
print(centroids)





#########################################################################################
#############SILHOUETTE
'''
range_n_clusters = list (range(2,8))
print()
print ("Número de clusters desde 2 hasta 7: \n", range_n_clusters)


for n_clusters in range_n_clusters:
    clusterer = KMeans(n_clusters=n_clusters)
    preds = clusterer.fit_predict(X_validation)
    centers = clusterer.cluster_centers_

    score = silhouette_score(X_validation, preds)
    print("Para n_clusters = {}, el coeficiente de Silhouette es: {})".format(n_clusters, score))

'''
##############################################################################################














####################################################################################################
#6. graficando CLUSTER
# Predicting the clusters
labels = kmeans.predict(X_Model_Cluster)
# Getting the cluster centers
C = kmeans.cluster_centers_
print('Localizacion de centroides')
print(C)
colores=['mediumblue','limegreen','salmon','grey','yellow','black']
asignar=[]
for row in labels:
    asignar.append(colores[row])
 
fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(X_Model_Cluster[:, 0], X_Model_Cluster[:, 1], X_Model_Cluster[:, 2], c=asignar,s=7)
ax.scatter(C[:, 0], C[:, 1], C[:, 2], marker='*', c=colores, s=1000)
ax.set_xlabel('Wind')
ax.set_ylabel('Other')
ax.set_zlabel('Sun')

plt.show()

#Creacion de Dataframe con inclusion de Valores de Cluster
print()
print('labels')
Cluster = pd.DataFrame({'Wind_proc':X_Model_Cluster[:,0],'Other_proc':X_Model_Cluster[:,1],'Sun_proc':X_Model_Cluster[:,2],'Cluster_Num':labels})
print(Cluster)


#Impresion de total de cluster
print()
print('Verificacion de Orden')
print(X_Model_Cluster)
print('clusters')
print(labels)

#Anexando columna de colores
Cluster['Color'] = asignar
#impresion CSV
#Cluster.to_csv(r'C:\Users\Adonis\Desktop\Traza.csv', index = True)

#Copia de seguridad de Model_Cluster2
Model_Cluster2 = Cluster.copy()

#Analisis de colores
print()
print('Dataframe MODEL_CLUSTER2 con colores para comparar con version inicial')
print(Model_Cluster2)


###############################################################
#****HASTA AQUI VAMOS BIEN, se repiten los mismos numeros
Model_Cluster2.to_csv(r'C:\Users\Adonis\Desktop\Model_Cluster2.csv', index = True)
#################################################################


#Analisis para seleccion de datos segun color

#Primera Iteracion para Cluster1
ClusterTest = Cluster[(Cluster['Wind_proc'].between(0.080, 0.2)) & (Cluster['Other_proc'].between(0.08, 0.2)) & (Cluster['Sun_proc'].between(0.08, 0.2))]
ClusterTest = ClusterTest.iloc[[1]]
Cluster_1 = ClusterTest.copy()
Cluster_1['No.'] = 'Cluster 1'
Cluster_1['Estado'] = 'Viento Bajo, Sol Bajo, Otros Bajo'
#print(Cluster_1)

#Segunda Iteracion Cluster 2
ClusterTest = Cluster[(Cluster['Wind_proc'].between(0.5, 0.65)) & (Cluster['Other_proc'].between(0.15, 0.25)) & (Cluster['Sun_proc'].between(0.08, 0.2))]
ClusterTest = ClusterTest.iloc[[1]]
Cluster_2 = ClusterTest.copy()
Cluster_2['No.'] = 'Cluster 2'
Cluster_2['Estado'] = 'Viento Alto, Sol Bajo, Otros Bajo'
#print(Cluster_2)

#Tercera Iteracion Cluster 3
ClusterTest = Cluster[(Cluster['Wind_proc'].between(0.05, 0.65)) & (Cluster['Other_proc'].between(0.75, 0.85)) & (Cluster['Sun_proc'].between(0.15, 0.25))]
ClusterTest = ClusterTest.iloc[[1]]
Cluster_3 = ClusterTest.copy()
Cluster_3['No.'] = 'Cluster 3'
Cluster_3['Estado'] = 'Viento Alto, Sol Bajo, Otros Alto'
#print(Cluster_3)

#Cuarta Iteracion Cluster 4
ClusterTest = Cluster[(Cluster['Wind_proc'].between(0.35, 0.45)) & (Cluster['Other_proc'].between(0.15, 0.25)) & (Cluster['Sun_proc'].between(0.65, 0.75))]
ClusterTest = ClusterTest.iloc[[1]]
Cluster_4 = ClusterTest.copy()
Cluster_4['No.'] = 'Cluster 4'
Cluster_4['Estado'] = 'Viento MIX, Sol Alto, Otros Bajo'
#print(Cluster_4)

#Quinta Iteracion Cluster 5
ClusterTest = Cluster[(Cluster['Wind_proc'].between(0.05, 0.15)) & (Cluster['Other_proc'].between(0.65, 0.75)) & (Cluster['Sun_proc'].between(0.55, 0.65))]
ClusterTest = ClusterTest.iloc[[1]]
Cluster_5 = ClusterTest.copy()
Cluster_5['No.'] = 'Cluster 5'
Cluster_5['Estado'] = 'Viento Bajo, Sol Alto, Otros Alto'
#print(Cluster_5)


#Sexta Iteracion Cluster 6
ClusterTest = Cluster[(Cluster['Wind_proc'].between(0.05, 0.15)) & (Cluster['Other_proc'].between(0.65, 0.75)) & (Cluster['Sun_proc'].between(0.05, 0.15))]
ClusterTest = ClusterTest.iloc[[1]]
Cluster_6 = ClusterTest.copy()
Cluster_6['No.'] = 'Cluster 6'
Cluster_6['Estado'] = 'Viento Bajo, Sol Bajo, Otros Alto'
#print(Cluster_6)

#Generacion de DataCluster
Cluster_All = Cluster_1.copy()
Cluster_All = Cluster_All.append(Cluster_2)
Cluster_All = Cluster_All.append(Cluster_3)
Cluster_All = Cluster_All.append(Cluster_4)
Cluster_All = Cluster_All.append(Cluster_5)
Cluster_All = Cluster_All.append(Cluster_6)

print()
print('**Resumen de Clusters con 6 selecciones unicas')
print(Cluster_All)

###################################################################
#AQUI ESTA EL PROBLEMA, SE PIERDE EL ORDEN CUANDO REALIZA EL MERGE
Model_Cluster3 = pd.merge(Model_Cluster2, Cluster_All, on='Color', how='left')
print('Join Final - SE REQUIERE CHEQUEAR ORDEN')
print(Model_Cluster3)

Model_Cluster3.to_csv(r'C:\Users\Adonis\Desktop\Model_Cluster3.csv', index = True)

print('Forma de DB')
print(Model_Cluster.shape)
print(Model_Cluster2.shape)
print(Model_Cluster3.shape)

#####################################
#Creando la Data final
Model_Cluster4 = Model_Cluster.copy()
Model_Cluster4 = Model_Cluster4.reset_index(drop=True)
print(Model_Cluster4)

#Data para merging
Model_Cluster5 = Model_Cluster3[['Color','No.','Estado']]
print('Data B para merge')
print(Model_Cluster5)

#Realizando Merging

Model_Cluster4 = pd.merge(Model_Cluster4, Model_Cluster5, left_index=True, right_index=True)

Model_Cluster4.to_csv(r'C:\Users\Adonis\Desktop\Model_Cluster4.csv', index = True)
Model_Cluster5.to_csv(r'C:\Users\Adonis\Desktop\Model_Cluster5.csv', index = True)
