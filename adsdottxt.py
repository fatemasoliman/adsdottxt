import os
import requests
import pandas as pd

domains=pd.read_csv('domains.csv', sep=',',header=0, encoding='latin-1') 

urllist=pd.DataFrame(domains)
urllist.columns = ['urlname','url']
#urlname = urllist['urlname']
#url = urllist['url'].to_string(index=False)

for index, row in urllist.iterrows():
	try:
		session = requests.Session()
		session.max_redirects = 3
		response=session.get(row['url'])
		content_type = response.headers['content-type']
		if "text/plain" in content_type:
			print(content_type,row['url'])	
			with open(os.path.join("files", '%s.csv' %row['urlname']), 'wb') as f:
				f.write(response.content)
	except:
		continue
