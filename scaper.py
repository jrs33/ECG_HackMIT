from lxml import html
import requests
import pandas as pd

page = requests.get('https://physionet.org/atm/ptbdb/patient002/s0015lre/0/10/rdsamp/csv/pd/samples.csv')
