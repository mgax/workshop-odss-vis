import csv
import json


def number(txt):
    return float(txt.replace(',', ''))


data_cj = []
data_tm = []
with open('rawdata/anunturi-participare-2014.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row['Moneda'] == 'RON':
            if row['Judet'] == 'Cluj':
                data_cj.append(number(row['Valoare Estimata']))
            if row['Judet'] == 'Timis':
                data_tm.append(number(row['Valoare Estimata']))


out = {
    'series': [
        {'data': sorted(data_cj, reverse=True)[:10], 'name': 'Cluj'},
        {'data': sorted(data_tm, reverse=True)[:10], 'name': 'Timis'},
    ],
}


with open('data/top10.json', 'wb') as f:
    json.dump(out, f, indent=2)
