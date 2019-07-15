import json
import pandas as pd
from pprint import pprint

from sampleParents import Parents
from sampleChildren import Children


def modify_urls():
    children = Children()
    df = pd.read_csv('Web_Scrapped_websites.csv', encoding="ISO-8859-1")
    cols = df.Website
    cols = list(cols[0:100])
    for x, col in enumerate(cols):
        children[x]['url'] = str(col)
        # print(f"child url: {children[x]} column: {col}")
    return children


def sampleDataSet(children):
    parents = Parents()
    for c, child in enumerate(children):
        for p, parent in enumerate(parents):
            if child['parent'] == parent['id']:
                parents[p]['children'] = parent['children'] + [child]
    # pprint(parents)
    for parent in parents:
        parent['active'] = False
    return parents


def write_file(data):
    filename = 'sampleDatabase.json'
    with open(filename, 'w') as outfile:
        json.dump(data, outfile)
    print(f" * {filename} WRITTEN * ")


if __name__ == '__main__':
    # pprint(sampleDataSet())

    write_file(sampleDataSet(modify_urls()))
    # main()
