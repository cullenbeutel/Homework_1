import pandas as pd
import numpy as np
import sqlite3
from sqlalchemy import create_engine

df = pd.read_csv('Marriage_Divorce_Rates_Data.csv') #import uncleaned csv file

cols1 = list(df.columns)
cols1 = [str(x)[:5] for x in cols1]

#connect to (or create if doesn’t exists) the SQLite database named db_name.db 
conn = sqlite3.connect("database.db") 
#[connection_name] = sqlite3.connect("[db_name].db") 
engine = create_engine('sqlite:///database.db') #Create engine

df2 = pd.melt(df, id_vars = ['State'], #Set Primary Column
value_vars = ['2011 Divorce Rates', '2011 Marriage Rates', #Enter Values of Variables
'2010 Divorce Rates', '2010 Marriage Rates', 
'2009 Divorce Rates', '2009 Marriage Rates', '2008 Divorce Rates', '2008 Marriage Rates',
'2007 Divorce Rates', '2007 Marriage Rates', '2006 Divorce Rates', '2006 Marriage Rates',
'2005 Divorce Rates', '2005 Marriage Rates', '2004 Divorce Rates', '2004 Marriage Rates',
'2003 Divorce Rates', '2003 Marriage Rates', '2002 Divorce Rates', '2002 Marriage Rates',
'2001 Divorce Rates', '2001 Marriage Rates', '2000 Divorce Rates', '2000 Marriage Rates',
'1999 Divorce Rates', '1999 Marriage Rates', '1995 Divorce Rates', '1995 Marriage Rates',
'1990 Divorce Rates', '1990 Marriage Rates'],
var_name = 'Year', #Set Variable Name
value_name = 'Rate') #Set Name for measure of variable

df2.sort_values(by= ['State', 'Year'], inplace = True, ascending=True)  #Sort values based on State and Year

df2.groupby('State').groups

#print(df2) #Test Print
df2.to_sql("database.db", engine) #converts datafram to SQL database
df2.to_csv('Python_Cleaned_File.csv') #Exports clean file to the file the python program is in
print('File has been cleaned and saved to your Folder')
print(pd.read_sql_table("database.db", engine)) #Test to see database is filled

conn.close()    #close connection 