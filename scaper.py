from lxml import html
import requests
import pandas as pd

data = pd.read_csv('filenames.txt', sep="\n", header = None)
data = data.values

for str_x in data:
	print(str_x)
	link = 'https://physionet.org/atm/ptbdb/'+str_x+'/0/10/rdsamp/csv/pd/samples.csv'
	print(link[0])
	l = link[0]
	page = requests.get(l)


p1 = requests.get("https://physionet.org/atm/ptbdb/patient001/s0014lre/0/10/rdsamp/csv/pd/samples.csv")
print "%s" % p1.text