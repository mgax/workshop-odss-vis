import csv
import json


def number(txt):
    return float(txt.replace(',', ''))


def normalize_name(txt):
    return txt.lower().replace('-', ' ').replace('_', ' ')


data = {}
with open('rawdata/siruta-judete.csv') as f:
    reader = csv.DictReader(f, delimiter=';')
    for row in reader:
        data[normalize_name(row['DENJ'])] = {
            'siruta': int(row['JUD']),
            'values': [],
        }

with open('rawdata/anunturi-participare-2014.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row['Moneda'] == 'RON':
            val = number(row['Valoare Estimata'])
            data[normalize_name(row['Judet'])]['values'].append(val)


series = []

for jud in data.values():
    series.append({
        'siruta': jud['siruta'],
        'value': int(sum(jud['values'])),
    })


out = {
    'series': series,
}


with open('data/summap.json', 'wb') as f:
    json.dump(out, f, indent=2)
