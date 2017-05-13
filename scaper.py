from lxml import html
import requests
import pandas as pd

data = pd.read_csv('filenames.txt', sep="\n", header = None)

for x in data {
	link = 'https://physionet.org/atm/ptbdb/' + x + '/0/10/rdsamp/csv/pd/samples.csv'
	page = requests.get(link)
	print(link.shape)
}

