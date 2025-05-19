import os
import yaml

#processed yaml to dict for word scanning
with open('data-processing/config/threatKeywords.yaml', 'r') as file:
    keywords=yaml.safe_load(file)

with open('data-processing/config/Negation.yaml', 'r') as file:
    negation=yaml.safe_load(file)

#returns type dict
def getThreatKeywords():
    return keywords


#returns type dict
def getNegationKeywords():
    return negation