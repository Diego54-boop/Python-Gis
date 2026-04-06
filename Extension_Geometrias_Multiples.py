####Funcion_extension (Maximos y minimos) para cualquier tipo de geometria

##Librerias
fig,ax =plt.subplots(figsize =(10,6))
import contextily as ctx
import pandas as pd
import numpy as np

##Nombre de la geometria shapefile (Puede ser un poligono multipoligono linea, multilinea, etc)
DEP = 'AMAZONAS'


capa= vias[vias["DEPARTAMEN"] == DEP]

##Calculo de los margenes extremos X y Y bajo argumentos sobre maximos y minimos
ymax = capa.bounds.sort_values(["maxy"],ascending =False).reset_index(drop =True).loc[[0]]["maxy"]
xmax = capa.bounds.sort_values(["maxx"],ascending =False).reset_index(drop =True).loc[[0]]["maxx"]

ymin = capa.bounds.sort_values(["miny"],ascending =True).reset_index(drop =True).loc[[0]]["miny"]
xmin = capa.bounds.sort_values(["minx"],ascending =True).reset_index(drop =True).loc[[0]]["minx"]

##Union de cada valor extremo por columna
joined = pd.concat([xmin,ymin ,xmax, ymax], axis = 1 , ignore_index = False)

coord =joined.reset_index(drop =True).transpose()[0].sort_values(ascending =True).to_numpy().reshape(2,2)


##Formato en duplas para calcular el objecto vectorial rectangular
coordenadas = list()
for i in coord[0]:
  for j in coord[1]:
    coordenadas.append((float(i),float(j)))


##Ordenamiento de las coordenadas siguiendo un direccion determinada(Horario o antihorario)
ord = pd.DataFrame(data = coordenadas,columns = ["X", "Y"]).loc[[0,1,3,2]]
ord.reset_index(drop =True, inplace =True)
aea = pd.concat([ord.loc[[0]], ord], axis = 0, ignore_index =True).loc[[1,2,3,4,0]].to_numpy()

##Conversion de las coordenadas numericas a objeto geodataframe , para su ploteo , visualizacion o para 
##su exportacion a diferentes formatos vectoriales
ext_rect = gpd.GeoDataFrame(geometry = [shapely.Polygon(aea)], crs ="32718")


##Visualizacion de la extension y la capa dentro de un mismo marco
capa.plot(ax=ax)
ax1 = ext_rect.plot(ax=ax,alpha = 0.3)
ctx.add_basemap(ax1, crs = "EPSG:32718")