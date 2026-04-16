import pandas as pd
import os

def rso_prikrep_2(file_name="p41898441.xlsx"):
	try:
		file = os.path.join(os.getcwd(), "Исходники", "РЕСО_Прикрепление_2", file_name)
		df = pd.read_excel(file, header=None)



		df_columns = list(df.iloc[7])
		print(df_columns)
		df.columns = df_columns
		df['npp_shifted'] = df['npp'].shift(1)
		df['NAME2_shifted']=df['NAME2'].shift(2)
		df['по программе'] = df.apply(lambda x: x['NAME2_shifted'] if x['npp_shifted']=='npp' else None, axis=1)
		df['по программе'] = df['по программе'].ffill()
		df =df.fillna('')
		df=df[(df['NAME1']!='')&(df['NAME1']!='NAME1')]


		return (True, df)
	except Exception as e:return(False, e)

if __name__ == "__main__":
	rso_prikrep_2()