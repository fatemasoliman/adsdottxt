import pandas as pd
import os
import csv

urllist=pd.read_csv('../domains.csv', sep=',',header=0, encoding='latin-1') 
urllist = pd.DataFrame(urllist)

for index, row in urllist.iterrows():
		urlname = row['name']	
		try:
			x = open('%s.csv' %urlname)
		except:
			continue
		y = csv.reader(x)
		z = []
		for row in y:
			z.append([urlname] + row)
		zdf = pd.DataFrame(z)
		zdf.to_csv('%s.csv' %urlname)


files = [f for f in os.listdir('.') if os.path.isfile(f)]

merged = []

for f in files:
	filename, ext = os.path.splitext(f)
	if ext =='.csv':
		read = pd.read_csv(f)
		merged.append(read)

result = pd.concat(merged)

result.to_csv('merged.csv')
