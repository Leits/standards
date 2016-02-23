# -*- coding: utf-8 -*-
import json
import csv
import yaml


uk_cpv = {}
en_cpv = {}
reader = csv.reader(open('classifiers/dk018.csv'))
reader.next()
for row in reader:
    uk_cpv.update({row[1]: row[2]})


olduk_cpv = uk_cpv
olden_cpv = en_cpv

uk_cpv = {}
en_cpv = {}

for key, value in olduk_cpv.items():
    if key and value:
        uk_cpv[key]=value.decode('utf-8')

for key, value in uk_cpv.items():
    if key and value:
        uk_cpv[key] = value.strip()


with open('classifiers/dk018/uk_pretty.json', 'wb') as jsonfile:
    jsonfile.write(json.dumps(uk_cpv, indent=4, sort_keys=True))
with open('classifiers/dk018/uk.json', 'wb') as jsonfile:
    jsonfile.write(json.dumps(uk_cpv, sort_keys=True))
with open('classifiers/dk018/uk_pretty.json', 'wb') as jsonfile:
    jsonfile.write(json.dumps(uk_cpv, indent=4, sort_keys=True))
with open('classifiers/dk018/uk.yaml', 'wb') as yamlfile:
    yaml.dump(uk_cpv, yamlfile, default_flow_style=False, width=2500)
with open('classifiers/dk018/uk_pretty.yaml', 'wb') as yamlfile:
    yaml.dump(uk_cpv, yamlfile, default_flow_style=False, width=2500, allow_unicode=True)