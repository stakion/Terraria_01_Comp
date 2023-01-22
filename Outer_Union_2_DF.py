import pandas as pd
import math
import numpy as np

DF_1 = pd.read_csv('Tablas_Datos_Terraria_Daño_Armas_Melee.csv')
print(DF_1)

DF_2 = pd.read_csv('Tablas_Datos_Terraria_Vida_Jefes.csv')
print(DF_2)

DF_3 = pd.merge(DF_1, DF_2, how='outer')
print(DF_3)

DF_3["No_Hits"] =  DF_3["DPS"] - DF_3["Damage Reduction"]
# DF_3.loc[DF_3['No_Hits'] < 0, 'No_Hits'] = DF_3["DPS"] + DF_3["Damage Reduction"]
# DF_3.loc[DF_3['No_Hits'] == 0, 'No_Hits'] = DF_3["DPS"]
DF_3.loc[DF_3['No_Hits'] <= 1, 'No_Hits'] = 1
DF_3["Life"] = DF_3["Life"].astype('float64')
DF_3["Number_Hits_FLOAT"] = DF_3["Life"]/DF_3["No_Hits"]

DF_3["Number_Hits_INT"] = DF_3["Number_Hits_FLOAT"].apply(np.ceil)

DF_3.to_csv('Tablas_Datos_Terraria_Outer_01.csv')

