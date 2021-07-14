import eia
import pandas as pd
from functools import reduce


"""
Run main script
"""
#Create EIA API using your specific API key
api_key = "e6110498c5c58ff24fecc5948a1bc804"
api = eia.API(api_key)


"""
Return the time series dataframe, based on API and unique Series ID
"""
###############################################################################################################

#NET GENERATION#
#Region 1 - United States Lower 48 (US48)
#Retrieve Data By Series ID 
series_search = api.data_by_series('EBA.US48-ALL.NG.H')
#Create a pandas dataframe from the retrieved time series
df_US = pd.DataFrame(series_search)
US = df_US.reset_index()
US.columns=['Date',"US_Net"]
US['Date'] = US['Date'].str[:-3]

#No existen duplicados
boolean = US['Date'].duplicated().any()
print(boolean)

#Index sort
US = US.sort_index(ascending=False)
US['US_Index'] = US.index

#Impresion de valores
US = US.sort_values(by='US_Index', ascending=False)
print('TABLA DE US GENERAL Y ORDENADA')
print(US)
print('*******************************************************')

#Region 2 - CALIFORNIA (CAL)
#Retrieve Data By Series ID 
series_search = api.data_by_series('EBA.CAL-ALL.NG.H')
#Create a pandas dataframe from the retrieved time series
df_CAL = pd.DataFrame(series_search)
CAL = df_CAL.reset_index()
#CAL['CAL_Index'] = CAL.index
CAL.columns=['Date',"CAL_Net"]
CAL['Date'] = CAL['Date'].str[:-3]


#Region 3 - CAROLINAS (CAR)
#Retrieve Data By Series ID 
series_search = api.data_by_series('EBA.CAR-ALL.NG.H')
#Create a pandas dataframe from the retrieved time series
df_CAR = pd.DataFrame(series_search)
CAR = df_CAR.reset_index()
#CAR['CAR_Index'] = CAR.index
CAR.columns=['Date',"CAR_Net"]
CAR['Date'] = CAR['Date'].str[:-3]


#Region 4 - CENTRAL (CENT)
#Retrieve Data By Series ID 
series_search = api.data_by_series('EBA.CENT-ALL.NG.H')
#Create a pandas dataframe from the retrieved time series
df_CEN = pd.DataFrame(series_search)
CEN = df_CEN.reset_index()
#CEN['CEN_Index'] = CEN.index
CEN.columns=['Date',"CEN_Net"]
CEN['Date'] = CEN['Date'].str[:-3]


#Region 5 - FLORIDA (FLO)
#Retrieve Data By Series ID 
series_search = api.data_by_series('EBA.FLA-ALL.NG.H')
#Create a pandas dataframe from the retrieved time series
df_FLO = pd.DataFrame(series_search)
FLO = df_FLO.reset_index()
#FLO['FLO_Index'] = FLO.index
FLO.columns=['Date',"FLO_Net"]
FLO['Date'] = FLO['Date'].str[:-3]


#Region 6 - MID ATLANTIC (MIDA)
#Retrieve Data By Series ID 
series_search = api.data_by_series('EBA.MIDA-ALL.NG.H')
#Create a pandas dataframe from the retrieved time series
df_MIDA = pd.DataFrame(series_search)
MIDA = df_MIDA.reset_index()
#MIDA['MIDA_Index'] = MIDA.index
MIDA.columns=['Date',"MIDA_Net"]
MIDA['Date'] = MIDA['Date'].str[:-3]


#Region 7 - MID WEST (MIDW)
#Retrieve Data By Series ID 
series_search = api.data_by_series('EBA.MIDW-ALL.NG.H')
#Create a pandas dataframe from the retrieved time series
df_MIDW = pd.DataFrame(series_search)
MIDW = df_MIDW.reset_index()
#MIDW['MIDW_Index'] = MIDW.index
MIDW.columns=['Date',"MIDW_Net"]
MIDW['Date'] = MIDW['Date'].str[:-3]


#Region 8 - NEW ENGLAND (NE)
#Retrieve Data By Series ID 
series_search = api.data_by_series('EBA.NE-ALL.NG.H')
#Create a pandas dataframe from the retrieved time series
df_NE = pd.DataFrame(series_search)
NE = df_NE.reset_index()
#NE['NE_Index'] = NE.index
NE.columns=['Date',"NE_Net"]
NE['Date'] = NE['Date'].str[:-3]


#Region 9 - NEW YORK (NY)
#Retrieve Data By Series ID 
series_search = api.data_by_series('EBA.NY-ALL.NG.H')
#Create a pandas dataframe from the retrieved time series
df_NY = pd.DataFrame(series_search)
NY = df_NY.reset_index()
#NY['NY_Index'] = NY.index
NY.columns=['Date',"NY_Net"]
NY['Date'] = NY['Date'].str[:-3]


#Region 10 - NORTH WEST (NW)
#Retrieve Data By Series ID 
series_search = api.data_by_series('EBA.NW-ALL.NG.H')
#Create a pandas dataframe from the retrieved time series
df_NW = pd.DataFrame(series_search)
NW = df_NW.reset_index()
#NW['NW_Index'] = NW.index
NW.columns=['Date',"NW_Net"]
NW['Date'] = NW['Date'].str[:-3]


#Region 11 - SOUTH EAST (SE)
#Retrieve Data By Series ID 
series_search = api.data_by_series('EBA.SE-ALL.NG.H')
#Create a pandas dataframe from the retrieved time series
df_SE = pd.DataFrame(series_search)
SE = df_SE.reset_index()
#SE['SE_Index'] = SE.index
SE.columns=['Date',"SE_Net"]
SE['Date'] = SE['Date'].str[:-3]


#Region 12 - SOUTH WEST (SW)
#Retrieve Data By Series ID 
series_search = api.data_by_series('EBA.SW-ALL.NG.H')
#Create a pandas dataframe from the retrieved time series
df_SW = pd.DataFrame(series_search)
SW = df_SW.reset_index()
#SW['SW_Index'] = SW.index
SW.columns=['Date',"SW_Net"]
SW['Date'] = SW['Date'].str[:-3]


#Region 13 - TENNESSEE (TEN)
#Retrieve Data By Series ID 
series_search = api.data_by_series('EBA.TEN-ALL.NG.H')
#Create a pandas dataframe from the retrieved time series
df_TEN = pd.DataFrame(series_search)
TEN = df_TEN.reset_index()
#TEN['TEN_Index'] = TEN.index
TEN.columns=['Date',"TEN_Net"]
TEN['Date'] = TEN['Date'].str[:-3]


#Region 14 - TEXAS (TEX)
#Retrieve Data By Series ID 
series_search = api.data_by_series('EBA.TEX-ALL.NG.H')
#Create a pandas dataframe from the retrieved time series
df_TEX = pd.DataFrame(series_search)
TEX = df_TEX.reset_index()
#TEX['TEX_Index'] = TEX.index
TEX.columns=['Date',"TEX_Net"]
TEX['Date'] = TEX['Date'].str[:-3]

print('Valores NET cargados')
#########################################################################
########################################################################
#ANEXO SOLAR

#Region 1 - United States LOWER 48 (US)
#Retrieve Data By Series ID 
series_search = api.data_by_series('EBA.US48-ALL.NG.SUN.H')
#Create a pandas dataframe from the retrieved time series
df_US_SUN = pd.DataFrame(series_search)
US_SUN = df_US_SUN.reset_index()
#CAL['CAL_Index'] = CAL.index
US_SUN.columns=['Date',"US_SUN_Net"]
US_SUN['Date'] = US_SUN['Date'].str[:-3]


#Region 2 - CALIFORNIA (CAL)
#Retrieve Data By Series ID 
series_search = api.data_by_series('EBA.CAL-ALL.NG.SUN.H')
#Create a pandas dataframe from the retrieved time series
df_CAL_SUN = pd.DataFrame(series_search)
CAL_SUN = df_CAL_SUN.reset_index()
#CAL['CAL_Index'] = CAL.index
CAL_SUN.columns=['Date',"CAL_SUN_Net"]
CAL_SUN['Date'] = CAL_SUN['Date'].str[:-3]


#Region 3 - CAROLINAS (CAR)
#Retrieve Data By Series ID 
series_search = api.data_by_series('EBA.CAR-ALL.NG.SUN.H')
#Create a pandas dataframe from the retrieved time series
df_CAR_SUN = pd.DataFrame(series_search)
CAR_SUN = df_CAR_SUN.reset_index()
#CAR['CAR_Index'] = CAR.index
CAR_SUN.columns=['Date',"CAR_SUN_Net"]
CAR_SUN['Date'] = CAR_SUN['Date'].str[:-3]


#Region 4 - CENTRAL (CENT)
#Retrieve Data By Series ID 
series_search = api.data_by_series('EBA.CENT-ALL.NG.SUN.H')
#Create a pandas dataframe from the retrieved time series
df_CEN_SUN = pd.DataFrame(series_search)
CEN_SUN = df_CEN_SUN.reset_index()
#CEN['CEN_Index'] = CEN.index
CEN_SUN.columns=['Date',"CEN_SUN_Net"]
CEN_SUN['Date'] = CEN_SUN['Date'].str[:-3]


#Region 5 - FLORIDA (FLO)
#Retrieve Data By Series ID 
series_search = api.data_by_series('EBA.FLA-ALL.NG.SUN.H')
#Create a pandas dataframe from the retrieved time series
df_FLO_SUN = pd.DataFrame(series_search)
FLO_SUN = df_FLO_SUN.reset_index()
#FLO['FLO_Index'] = FLO.index
FLO_SUN.columns=['Date',"FLO_SUN_Net"]
FLO_SUN['Date'] = FLO_SUN['Date'].str[:-3]


#Region 6 - MID ATLANTIC (MIDA)
#Retrieve Data By Series ID 
series_search = api.data_by_series('EBA.MIDA-ALL.NG.SUN.H')
#Create a pandas dataframe from the retrieved time series
df_MIDA_SUN = pd.DataFrame(series_search)
MIDA_SUN = df_MIDA_SUN.reset_index()
#MIDA['MIDA_Index'] = MIDA.index
MIDA_SUN.columns=['Date',"MIDA_SUN_Net"]
MIDA_SUN['Date'] = MIDA_SUN['Date'].str[:-3]


#Region 7 - MID WEST (MIDW)
#Retrieve Data By Series ID 
series_search = api.data_by_series('EBA.MIDW-ALL.NG.SUN.H')
#Create a pandas dataframe from the retrieved time series
df_MIDW_SUN = pd.DataFrame(series_search)
MIDW_SUN = df_MIDW_SUN.reset_index()
#MIDW['MIDW_Index'] = MIDW.index
MIDW_SUN.columns=['Date',"MIDW_SUN_Net"]
MIDW_SUN['Date'] = MIDW_SUN['Date'].str[:-3]


#Region 8 - NEW ENGLAND (NE)
#Retrieve Data By Series ID 
series_search = api.data_by_series('EBA.NE-ALL.NG.SUN.H')
#Create a pandas dataframe from the retrieved time series
df_NE_SUN = pd.DataFrame(series_search)
NE_SUN = df_NE_SUN.reset_index()
#NE['NE_Index'] = NE.index
NE_SUN.columns=['Date',"NE_SUN_Net"]
NE_SUN['Date'] = NE_SUN['Date'].str[:-3]


#Region 9 - NEW YORK (NY)
#Retrieve Data By Series ID 
series_search = api.data_by_series('EBA.NY-ALL.NG.SUN.H')
#Create a pandas dataframe from the retrieved time series
df_NY_SUN = pd.DataFrame(series_search)
NY_SUN = df_NY_SUN.reset_index()
#NY['NY_Index'] = NY.index
NY_SUN.columns=['Date',"NY_SUN_Net"]
NY_SUN['Date'] = NY_SUN['Date'].str[:-3]


#Region 10 - NORTH WEST (NW)
#Retrieve Data By Series ID 
series_search = api.data_by_series('EBA.NW-ALL.NG.SUN.H')
#Create a pandas dataframe from the retrieved time series
df_NW_SUN = pd.DataFrame(series_search)
NW_SUN = df_NW_SUN.reset_index()
#NW['NW_Index'] = NW.index
NW_SUN.columns=['Date',"NW_SUN_Net"]
NW_SUN['Date'] = NW_SUN['Date'].str[:-3]


#Region 11 - SOUTH EAST (SE)
#Retrieve Data By Series ID 
series_search = api.data_by_series('EBA.SE-ALL.NG.SUN.H')
#Create a pandas dataframe from the retrieved time series
df_SE_SUN = pd.DataFrame(series_search)
SE_SUN = df_SE_SUN.reset_index()
#SE['SE_Index'] = SE.index
SE_SUN.columns=['Date',"SE_SUN_Net"]
SE_SUN['Date'] = SE_SUN['Date'].str[:-3]


#Region 12 - SOUTH WEST (SW)
#Retrieve Data By Series ID 
series_search = api.data_by_series('EBA.SW-ALL.NG.SUN.H')
#Create a pandas dataframe from the retrieved time series
df_SW_SUN = pd.DataFrame(series_search)
SW_SUN = df_SW_SUN.reset_index()
#SW['SW_Index'] = SW.index
SW_SUN.columns=['Date',"SW_SUN_Net"]
SW_SUN['Date'] = SW_SUN['Date'].str[:-3]


#Region 13 - TENNESSEE (TEN)
#Retrieve Data By Series ID 
series_search = api.data_by_series('EBA.TEN-ALL.NG.SUN.H')
#Create a pandas dataframe from the retrieved time series
df_TEN_SUN = pd.DataFrame(series_search)
TEN_SUN = df_TEN_SUN.reset_index()
#TEN['TEN_Index'] = TEN.index
TEN_SUN.columns=['Date',"TEN_SUN_Net"]
TEN_SUN['Date'] = TEN_SUN['Date'].str[:-3]


#Region 14 - TEXAS (TEX)
#Retrieve Data By Series ID 
series_search = api.data_by_series('EBA.TEX-ALL.NG.SUN.H')
#Create a pandas dataframe from the retrieved time series
df_TEX_SUN = pd.DataFrame(series_search)
TEX_SUN = df_TEX_SUN.reset_index()
#TEX['TEX_Index'] = TEX.index
TEX_SUN.columns=['Date',"TEX_SUN_Net"]
TEX_SUN['Date'] = TEX_SUN['Date'].str[:-3]

print('Valores SUN cargados')
##########################################################################
##########################################################################
#ANEXO VIENTO

#Region 1 - United States LOWER 48 (US)
#Retrieve Data By Series ID 
series_search = api.data_by_series('EBA.US48-ALL.NG.WND.H')
#Create a pandas dataframe from the retrieved time series
df_US_WIN = pd.DataFrame(series_search)
US_WIN = df_US_WIN.reset_index()
#CAL['CAL_Index'] = CAL.index
US_WIN.columns=['Date',"US_WIN_Net"]
US_WIN['Date'] = US_WIN['Date'].str[:-3]



#Region 2 - CALIFORNIA (CAL)
#Retrieve Data By Series ID 
series_search = api.data_by_series('EBA.CAL-ALL.NG.WND.H')
#Create a pandas dataframe from the retrieved time series
df_CAL_WIN = pd.DataFrame(series_search)
CAL_WIN = df_CAL_WIN.reset_index()
#CAL['CAL_Index'] = CAL.index
CAL_WIN.columns=['Date',"CAL_WIN_Net"]
CAL_WIN['Date'] = CAL_WIN['Date'].str[:-3]

'''
#Region 3 - CAROLINAS (CAR)
#Retrieve Data By Series ID 
series_search = api.data_by_series('EBA.CAR-ALL.NG.SUN.H')
#Create a pandas dataframe from the retrieved time series
df_CAR_WIN = pd.DataFrame(series_search)
CAR_WIN = df_CAR_WIN.reset_index()
#CAR['CAR_Index'] = CAR.index
CAR_WIN.columns=['Date',"CAR_WIN_Net"]
CAR_WIN['Date'] = CAR_WIN['Date'].str[:-3]
'''


#Region 4 - CENTRAL (CENT)
#Retrieve Data By Series ID 
series_search = api.data_by_series('EBA.CENT-ALL.NG.WND.H')
#Create a pandas dataframe from the retrieved time series
df_CEN_WIN = pd.DataFrame(series_search)
CEN_WIN = df_CEN_WIN.reset_index()
#CEN['CEN_Index'] = CEN.index
CEN_WIN.columns=['Date',"CEN_WIN_Net"]
CEN_WIN['Date'] = CEN_WIN['Date'].str[:-3]

'''
#Region 5 - FLORIDA (FLO)
#Retrieve Data By Series ID 
series_search = api.data_by_series('EBA.FLA-ALL.NG.SUN.H')
#Create a pandas dataframe from the retrieved time series
df_FLO_WIN = pd.DataFrame(series_search)
FLO_WIN = df_FLO_WIN.reset_index()
#FLO['FLO_Index'] = FLO.index
FLO_WIN.columns=['Date',"FLO_WIN_Net"]
FLO_WIN['Date'] = FLO_WIN['Date'].str[:-3]
'''

#Region 6 - MID ATLANTIC (MIDA)
#Retrieve Data By Series ID 
series_search = api.data_by_series('EBA.MIDA-ALL.NG.WND.H')
#Create a pandas dataframe from the retrieved time series
df_MIDA_WIN = pd.DataFrame(series_search)
MIDA_WIN = df_MIDA_WIN.reset_index()
#MIDA['MIDA_Index'] = MIDA.index
MIDA_WIN.columns=['Date',"MIDA_WIN_Net"]
MIDA_WIN['Date'] = MIDA_WIN['Date'].str[:-3]


#Region 7 - MID WEST (MIDW)
#Retrieve Data By Series ID 
series_search = api.data_by_series('EBA.MIDW-ALL.NG.WND.H')
#Create a pandas dataframe from the retrieved time series
df_MIDW_WIN = pd.DataFrame(series_search)
MIDW_WIN = df_MIDW_WIN.reset_index()
#MIDW['MIDW_Index'] = MIDW.index
MIDW_WIN.columns=['Date',"MIDW_WIN_Net"]
MIDW_WIN['Date'] = MIDW_WIN['Date'].str[:-3]


#Region 8 - NEW ENGLAND (NE)
#Retrieve Data By Series ID 
series_search = api.data_by_series('EBA.NE-ALL.NG.WND.H')
#Create a pandas dataframe from the retrieved time series
df_NE_WIN = pd.DataFrame(series_search)
NE_WIN = df_NE_WIN.reset_index()
#NE['NE_Index'] = NE.index
NE_WIN.columns=['Date',"NE_WIN_Net"]
NE_WIN['Date'] = NE_WIN['Date'].str[:-3]


#Region 9 - NEW YORK (NY)
#Retrieve Data By Series ID 
series_search = api.data_by_series('EBA.NY-ALL.NG.WND.H')
#Create a pandas dataframe from the retrieved time series
df_NY_WIN = pd.DataFrame(series_search)
NY_WIN = df_NY_WIN.reset_index()
#NY['NY_Index'] = NY.index
NY_WIN.columns=['Date',"NY_WIN_Net"]
NY_WIN['Date'] = NY_WIN['Date'].str[:-3]


#Region 10 - NORTH WEST (NW)
#Retrieve Data By Series ID 
series_search = api.data_by_series('EBA.NW-ALL.NG.WND.H')
#Create a pandas dataframe from the retrieved time series
df_NW_WIN = pd.DataFrame(series_search)
NW_WIN = df_NW_WIN.reset_index()
#NW['NW_Index'] = NW.index
NW_WIN.columns=['Date',"NW_WIN_Net"]
NW_WIN['Date'] = NW_WIN['Date'].str[:-3]


#Region 11 - SOUTH EAST (SE)
#Retrieve Data By Series ID 
series_search = api.data_by_series('EBA.SE-ALL.NG.WND.H')
#Create a pandas dataframe from the retrieved time series
df_SE_WIN = pd.DataFrame(series_search)
SE_WIN = df_SE_WIN.reset_index()
#SE['SE_Index'] = SE.index
SE_WIN.columns=['Date',"SE_WIN_Net"]
SE_WIN['Date'] = SE_WIN['Date'].str[:-3]


#Region 12 - SOUTH WEST (SW)
#Retrieve Data By Series ID 
series_search = api.data_by_series('EBA.SW-ALL.NG.WND.H')
#Create a pandas dataframe from the retrieved time series
df_SW_WIN = pd.DataFrame(series_search)
SW_WIN = df_SW_WIN.reset_index()
#SW['SW_Index'] = SW.index
SW_WIN.columns=['Date',"SW_WIN_Net"]
SW_WIN['Date'] = SW_WIN['Date'].str[:-3]


#Region 13 - TENNESSEE (TEN)
#Retrieve Data By Series ID 
series_search = api.data_by_series('EBA.TEN-ALL.NG.WND.H')
#Create a pandas dataframe from the retrieved time series
df_TEN_WIN = pd.DataFrame(series_search)
TEN_WIN = df_TEN_WIN.reset_index()
#TEN['TEN_Index'] = TEN.index
TEN_WIN.columns=['Date',"TEN_WIN_Net"]
TEN_WIN['Date'] = TEN_WIN['Date'].str[:-3]


#Region 14 - TEXAS (TEX)
#Retrieve Data By Series ID 
series_search = api.data_by_series('EBA.TEX-ALL.NG.WND.H')
#Create a pandas dataframe from the retrieved time series
df_TEX_WIN = pd.DataFrame(series_search)
TEX_WIN = df_TEX_WIN.reset_index()
#TEX['TEX_Index'] = TEX.index
TEX_WIN.columns=['Date',"TEX_WIN_Net"]
TEX_WIN['Date'] = TEX_WIN['Date'].str[:-3]

print('Valores WIND cargados')
#########################################################################
#########################################################################
#Anexo OTHER

#Region 1 - United States LOWER 48 (US)
#Retrieve Data By Series ID 
series_search = api.data_by_series('EBA.US48-ALL.NG.OTH.H')
#Create a pandas dataframe from the retrieved time series
df_US_OT = pd.DataFrame(series_search)
US_OT = df_US_OT.reset_index()
#CAL['CAL_Index'] = CAL.index
US_OT.columns=['Date',"US_OT_Net"]
US_OT['Date'] = US_OT['Date'].str[:-3]


#Region 2 - CALIFORNIA (CAL)
#Retrieve Data By Series ID 
series_search = api.data_by_series('EBA.CAL-ALL.NG.OTH.H')
#Create a pandas dataframe from the retrieved time series
df_CAL_OT = pd.DataFrame(series_search)
CAL_OT = df_CAL_OT.reset_index()
#CAL['CAL_Index'] = CAL.index
CAL_OT.columns=['Date',"CAL_OT_Net"]
CAL_OT['Date'] = CAL_OT['Date'].str[:-3]


#Region 3 - CAROLINAS (CAR)
#Retrieve Data By Series ID 
series_search = api.data_by_series('EBA.CAR-ALL.NG.OTH.H')
#Create a pandas dataframe from the retrieved time series
df_CAR_OT = pd.DataFrame(series_search)
CAR_OT = df_CAR_OT.reset_index()
#CAR['CAR_Index'] = CAR.index
CAR_OT.columns=['Date',"CAR_OT_Net"]
CAR_OT['Date'] = CAR_OT['Date'].str[:-3]


#Region 4 - CENTRAL (CENT)
#Retrieve Data By Series ID 
series_search = api.data_by_series('EBA.CENT-ALL.NG.OTH.H')
#Create a pandas dataframe from the retrieved time series
df_CEN_OT = pd.DataFrame(series_search)
CEN_OT = df_CEN_OT.reset_index()
#CEN['CEN_Index'] = CEN.index
CEN_OT.columns=['Date',"CEN_OT_Net"]
CEN_OT['Date'] = CEN_OT['Date'].str[:-3]


#Region 5 - FLORIDA (FLO)
#Retrieve Data By Series ID 
series_search = api.data_by_series('EBA.FLA-ALL.NG.OTH.H')
#Create a pandas dataframe from the retrieved time series
df_FLO_OT = pd.DataFrame(series_search)
FLO_OT = df_FLO_OT.reset_index()
#FLO['FLO_Index'] = FLO.index
FLO_OT.columns=['Date',"FLO_OT_Net"]
FLO_OT['Date'] = FLO_OT['Date'].str[:-3]


#Region 6 - MID ATLANTIC (MIDA)
#Retrieve Data By Series ID 
series_search = api.data_by_series('EBA.MIDA-ALL.NG.OTH.H')
#Create a pandas dataframe from the retrieved time series
df_MIDA_OT = pd.DataFrame(series_search)
MIDA_OT = df_MIDA_OT.reset_index()
#MIDA['MIDA_Index'] = MIDA.index
MIDA_OT.columns=['Date',"MIDA_OT_Net"]
MIDA_OT['Date'] = MIDA_OT['Date'].str[:-3]


#Region 7 - MID WEST (MIDW)
#Retrieve Data By Series ID 
series_search = api.data_by_series('EBA.MIDW-ALL.NG.OTH.H')
#Create a pandas dataframe from the retrieved time series
df_MIDW_OT = pd.DataFrame(series_search)
MIDW_OT = df_MIDW_OT.reset_index()
#MIDW['MIDW_Index'] = MIDW.index
MIDW_OT.columns=['Date',"MIDW_OT_Net"]
MIDW_OT['Date'] = MIDW_OT['Date'].str[:-3]


#Region 8 - NEW ENGLAND (NE)
#Retrieve Data By Series ID 
series_search = api.data_by_series('EBA.NE-ALL.NG.OTH.H')
#Create a pandas dataframe from the retrieved time series
df_NE_OT = pd.DataFrame(series_search)
NE_OT = df_NE_OT.reset_index()
#NE['NE_Index'] = NE.index
NE_OT.columns=['Date',"NE_OT_Net"]
NE_OT['Date'] = NE_OT['Date'].str[:-3]


#Region 9 - NEW YORK (NY)
#Retrieve Data By Series ID 
series_search = api.data_by_series('EBA.NY-ALL.NG.OTH.H')
#Create a pandas dataframe from the retrieved time series
df_NY_OT = pd.DataFrame(series_search)
NY_OT = df_NY_OT.reset_index()
#NY['NY_Index'] = NY.index
NY_OT.columns=['Date',"NY_OT_Net"]
NY_OT['Date'] = NY_OT['Date'].str[:-3]


#Region 10 - NORTH WEST (NW)
#Retrieve Data By Series ID 
series_search = api.data_by_series('EBA.NW-ALL.NG.OTH.H')
#Create a pandas dataframe from the retrieved time series
df_NW_OT = pd.DataFrame(series_search)
NW_OT = df_NW_OT.reset_index()
#NW['NW_Index'] = NW.index
NW_OT.columns=['Date',"NW_OT_Net"]
NW_OT['Date'] = NW_OT['Date'].str[:-3]


#Region 11 - SOUTH EAST (SE)
#Retrieve Data By Series ID 
series_search = api.data_by_series('EBA.SE-ALL.NG.OTH.H')
#Create a pandas dataframe from the retrieved time series
df_SE_OT = pd.DataFrame(series_search)
SE_OT = df_SE_OT.reset_index()
#SE['SE_Index'] = SE.index
SE_OT.columns=['Date',"SE_OT_Net"]
SE_OT['Date'] = SE_OT['Date'].str[:-3]


#Region 12 - SOUTH WEST (SW)
#Retrieve Data By Series ID 
series_search = api.data_by_series('EBA.SW-ALL.NG.OTH.H')
#Create a pandas dataframe from the retrieved time series
df_SW_OT = pd.DataFrame(series_search)
SW_OT = df_SW_OT.reset_index()
#SW['SW_Index'] = SW.index
SW_OT.columns=['Date',"SW_OT_Net"]
SW_OT['Date'] = SW_OT['Date'].str[:-3]


#Region 13 - TENNESSEE (TEN)
#Retrieve Data By Series ID 
series_search = api.data_by_series('EBA.TEN-ALL.NG.OTH.H')
#Create a pandas dataframe from the retrieved time series
df_TEN_OT = pd.DataFrame(series_search)
TEN_OT = df_TEN_OT.reset_index()
#TEN['TEN_Index'] = TEN.index
TEN_OT.columns=['Date',"TEN_OT_Net"]
TEN_OT['Date'] = TEN_OT['Date'].str[:-3]


#Region 14 - TEXAS (TEX)
#Retrieve Data By Series ID 
series_search = api.data_by_series('EBA.TEX-ALL.NG.OTH.H')
#Create a pandas dataframe from the retrieved time series
df_TEX_OT = pd.DataFrame(series_search)
TEX_OT = df_TEX_OT.reset_index()
#TEX['TEX_Index'] = TEX.index
TEX_OT.columns=['Date',"TEX_OT_Net"]
TEX_OT['Date'] = TEX_OT['Date'].str[:-3]



print('valores OTHER cargados')
########################################################################

NET_data = [US,CAL,CAR,CEN,FLO,MIDA,MIDW,NE,NY,NW,SE,SW,TEN,TEX,\
    US_SUN,CAL_SUN,CAR_SUN,CEN_SUN,FLO_SUN,MIDA_SUN,MIDW_SUN,NE_SUN,NY_SUN,NW_SUN,SE_SUN,SW_SUN,TEN_SUN,TEX_SUN,\
    US_WIN,CAL_WIN,CEN_WIN,MIDA_WIN,MIDW_WIN,NE_WIN,NY_WIN,NW_WIN,SE_WIN,SW_WIN,TEN_WIN,TEX_WIN,\
    US_OT,CAL_OT,CAR_OT,CEN_OT,FLO_OT,MIDA_OT,MIDW_OT,NE_OT,NY_OT,NW_OT,SE_OT,SW_OT,TEN_OT,TEX_OT ]

NET_final = reduce(lambda left,right: pd.merge(left,right, on='Date'),NET_data)

#ANEXANDO CAR_WIN Y FLO_WIN

NET_final['FLO_WIN_Net'] = 0
NET_final['CAR_WIN_Net'] = 0

print('Merge realizado con exito')
#print(NET_final)

#impresion CSV
#NET_final.to_csv(r'C:\Users\Adonis\Desktop\NET.csv', index = True)
selected_columns = NET_final[['Date','US_Net','US_SUN_Net','US_WIN_Net','US_OT_Net']]
Grid = selected_columns.copy()
#Cambio de nombres
Grid = Grid.rename(columns={'US_Net':'NET','US_SUN_Net':'SUN','US_WIN_Net':'WIND','US_OT_Net':'OTHER'})
Grid ['Region'] = 'UNITED STATES'
Grid ['Region Num'] = 1

#print(Grid)


############################################################################################################
############################################################################################################
#Dataframe Appending


#2 SECCION CALIFORNIA
Grid_CAL = NET_final[['Date','CAL_Net','CAL_SUN_Net','CAL_WIN_Net','CAL_OT_Net']].copy()
Grid_CAL['Region'] = 'CALIFORNIA'
Grid_CAL['Region Num'] = 2
Grid_CAL = Grid_CAL.rename(columns={'CAL_Net':'NET','CAL_SUN_Net':'SUN','CAL_WIN_Net':'WIND','CAL_OT_Net':'OTHER'})


#3 SECCION CAROLINAS
Grid_CAR = NET_final[['Date','CAR_Net','CAR_SUN_Net','CAR_WIN_Net','CAR_OT_Net']].copy()
Grid_CAR['Region'] = 'CAROLINAS'
Grid_CAR['Region Num'] = 3
Grid_CAR = Grid_CAR.rename(columns={'CAR_Net':'NET','CAR_SUN_Net':'SUN','CAR_WIN_Net':'WIND','CAR_OT_Net':'OTHER'})


#4 SECCION CENTRAL
Grid_CEN = NET_final[['Date','CEN_Net','CEN_SUN_Net','CEN_WIN_Net','CEN_OT_Net']].copy()
Grid_CEN['Region'] = 'CENTRAL'
Grid_CEN['Region Num'] = 4
Grid_CEN = Grid_CEN.rename(columns={'CEN_Net':'NET','CEN_SUN_Net':'SUN','CEN_WIN_Net':'WIND','CEN_OT_Net':'OTHER'})


#5 SECCION FLORIDA
Grid_FLO = NET_final[['Date','FLO_Net','FLO_SUN_Net','FLO_WIN_Net','FLO_OT_Net']].copy()
Grid_FLO['Region'] = 'FLORIDA'
Grid_FLO['Region Num'] = 5
Grid_FLO = Grid_FLO.rename(columns={'FLO_Net':'NET','FLO_SUN_Net':'SUN','FLO_WIN_Net':'WIND','FLO_OT_Net':'OTHER'})


#6 SECCION MID ATLANTIC
Grid_MIDA = NET_final[['Date','MIDA_Net','MIDA_SUN_Net','MIDA_WIN_Net','MIDA_OT_Net']].copy()
Grid_MIDA['Region'] = 'MID ATLANTIC'
Grid_MIDA['Region Num'] = 6
Grid_MIDA = Grid_MIDA.rename(columns={'MIDA_Net':'NET','MIDA_SUN_Net':'SUN','MIDA_WIN_Net':'WIND','MIDA_OT_Net':'OTHER'})



#7 SECCION MID WEST
Grid_MIDW = NET_final[['Date','MIDW_Net','MIDW_SUN_Net','MIDW_WIN_Net','MIDW_OT_Net']].copy()
Grid_MIDW['Region'] = 'MID WEST'
Grid_MIDW['Region Num'] = 7
Grid_MIDW = Grid_MIDW.rename(columns={'MIDW_Net':'NET','MIDW_SUN_Net':'SUN','MIDW_WIN_Net':'WIND','MIDW_OT_Net':'OTHER'})


#8 SECCION NEW ENGLAND
Grid_NE = NET_final[['Date','NE_Net','NE_SUN_Net','NE_WIN_Net','NE_OT_Net']].copy()
Grid_NE['Region'] = 'NEW ENGLAND'
Grid_NE['Region Num'] = 8
Grid_NE = Grid_NE.rename(columns={'NE_Net':'NET','NE_SUN_Net':'SUN','NE_WIN_Net':'WIND','NE_OT_Net':'OTHER'})

#9 SECCION NEW YORK
Grid_NY = NET_final[['Date','NY_Net','NY_SUN_Net','NY_WIN_Net','NY_OT_Net']].copy()
Grid_NY['Region'] = 'NEW YORK'
Grid_NY['Region Num'] = 9
Grid_NY = Grid_NY.rename(columns={'NY_Net':'NET','NY_SUN_Net':'SUN','NY_WIN_Net':'WIND','NY_OT_Net':'OTHER'})


#10 SECCION NORTH WEST
Grid_NW = NET_final[['Date','NW_Net','NW_SUN_Net','NW_WIN_Net','NW_OT_Net']].copy()
Grid_NW['Region'] = 'NORTH WEST'
Grid_NW['Region Num'] = 10
Grid_NW = Grid_NW.rename(columns={'NW_Net':'NET','NW_SUN_Net':'SUN','NW_WIN_Net':'WIND','NW_OT_Net':'OTHER'})


#11 SECCION SOUTH EAST
Grid_SE = NET_final[['Date','SE_Net','SE_SUN_Net','SE_WIN_Net','SE_OT_Net']].copy()
Grid_SE['Region'] = 'SOUTH EAST'
Grid_SE['Region Num'] = 11
Grid_SE = Grid_SE.rename(columns={'SE_Net':'NET','SE_SUN_Net':'SUN','SE_WIN_Net':'WIND','SE_OT_Net':'OTHER'})


#12 SECCION SOUTH WEST
Grid_SW = NET_final[['Date','SW_Net','SW_SUN_Net','SW_WIN_Net','SW_OT_Net']].copy()
Grid_SW['Region'] = 'SOUTH WEST'
Grid_SW['Region Num'] = 12
Grid_SW = Grid_SW.rename(columns={'SW_Net':'NET','SW_SUN_Net':'SUN','SW_WIN_Net':'WIND','SW_OT_Net':'OTHER'})


#13 SECCION TENNESSEE
Grid_TEN = NET_final[['Date','TEN_Net','TEN_SUN_Net','TEN_WIN_Net','TEN_OT_Net']].copy()
Grid_TEN['Region'] = 'TENNESSEE'
Grid_TEN['Region Num'] = 13
Grid_TEN = Grid_TEN.rename(columns={'TEN_Net':'NET','TEN_SUN_Net':'SUN','TEN_WIN_Net':'WIND','TEN_OT_Net':'OTHER'})


#14 SECCION TEXAS
Grid_TEX = NET_final[['Date','TEX_Net','TEX_SUN_Net','TEX_WIN_Net','TEX_OT_Net']].copy()
Grid_TEX['Region'] = 'TEXAS'
Grid_TEX['Region Num'] = 14
Grid_TEX = Grid_TEX.rename(columns={'TEX_Net':'NET','TEX_SUN_Net':'SUN','TEX_WIN_Net':'WIND','TEX_OT_Net':'OTHER'})


Grid = Grid.append(Grid_CAL)
Grid = Grid.append(Grid_CAR)
Grid = Grid.append(Grid_CEN)
Grid = Grid.append(Grid_FLO)
Grid = Grid.append(Grid_MIDA)
Grid = Grid.append(Grid_MIDW)
Grid = Grid.append(Grid_NE)
Grid = Grid.append(Grid_NY)
Grid = Grid.append(Grid_NW)
Grid = Grid.append(Grid_SE)
Grid = Grid.append(Grid_SW)
Grid = Grid.append(Grid_TEN)
Grid = Grid.append(Grid_TEX)


##############################################################################################################
#anexo de calculo de CO2
Metric_Ton = 0.709

#Ahorro de CO2 en Energia Solar
Grid['SUN_SAVED_CO2'] = Grid['SUN'] * Metric_Ton
#Ahorro de CO2 en Energia Eolica
Grid['WIND_SAVED_CO2'] = Grid['WIND'] * Metric_Ton
#Ahorro de CO2 en Otros
Grid['OTHER_SAVED_CO2'] = Grid['OTHER'] * Metric_Ton
#Ahorro total Carbon neutro
Grid['TOTAL_SAVED_CO2'] = (Grid['SUN_SAVED_CO2'] + Grid['WIND_SAVED_CO2'] + Grid['OTHER_SAVED_CO2'])

#Emision de CO2 TOTAL
Grid['TOTAL_EMITED_CO2'] = Grid['NET'] * Metric_Ton

#Emision de CO2 por Fosiles (Diferencia)
Grid['FOSIL_CO2'] = Grid['TOTAL_EMITED_CO2'] - Grid['TOTAL_SAVED_CO2']
print()
print('Calculo de Emisiones realizado con Exito')

#Impresion de Data
print(Grid)





#impresion CSV
Grid.to_csv(r'C:\Users\Adonis\Desktop\Grid.csv', index = True)

##################################################################################################################
##################################################################################################################


#2da FASE_Cluster

print('data para cluster:')
Modelo = Grid
Modelo['Code'] = Modelo.index
Modelo = Modelo.drop(['SUN_SAVED_CO2','WIND_SAVED_CO2','OTHER_SAVED_CO2','TOTAL_SAVED_CO2','TOTAL_EMITED_CO2','FOSIL_CO2'],1)
#print(Cluster)

Cluster2 = Modelo.loc[Modelo['Code'] == 0]
print(Cluster2)

#impresion CSV
Modelo.to_csv(r'C:\Users\Adonis\Desktop\Modelo.csv', index = True)
Cluster2.to_csv(r'C:\Users\Adonis\Desktop\Cluster.csv', index = True)
