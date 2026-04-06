##Pendiente de corriente natural por el metodo Taylor y schwartz
import pandas as pd
import numpy as np
import math


##inputs
perfil_long = pd.read_excel("/content/perfil_.xlsx")
numero_de_tramos = 100

##Funcion pendiente Taylor Schwartz
def pendiente_taylor_schwartz(perfil_long , numero_de_tramos):
   intervalo_progresiva =  perfil_long["elevation"].to_numpy().max()
   numero_datos  = len(perfil_long)
   intervalo = int(numero_datos/numero_de_tramos) ## el intervalo no puede ser igual a 1 implica que no hay diferencia de cotas
   if intervalo == 1:
    print("elije otro numero de tramos")
   else:
    intervalo_progresiva   = perfil_long["distance"].to_numpy().max()/numero_de_tramos
    ##calculo de nueva cantidad de terminos
    numero_datos_entero   = intervalo*numero_de_tramos
    numero_de_registros_a_eliminar  = abs(numero_datos  -  numero_datos_entero)
    perf_nuevo = perfil_long.drop([i for i in range(int(numero_de_registros_a_eliminar))], axis = 0)
    array_perf  = perf_nuevo["elevation"].to_numpy()
    array_shaped  = array_perf.reshape(int(numero_de_tramos),int(intervalo))
    lista_dife = list()
    for i in range(len(array_shaped)):
      dif = array_shaped[i][0].tolist()-array_shaped[i][intervalo-1].tolist()
      if dif == 0:
        pass
      else:
        lista_dife.append(dif)
    lista_pendi = [1/(math.sqrt(abs(i)/int(intervalo_progresiva))) for i in lista_dife]
    sum = 0
    for i in lista_pendi:
      sum = sum +i
    S = (numero_de_tramos/sum)**2
   return print(f"La pendiente de la corriente principal es {S}")