import os
import csv
import json
import numpy as np


def main():
    location = "../graphs/SaoPaulo.json"
    if os.path.exists(location):
        exit("Database already exists")

    keep = {}
    nodes = []
    links = []
    final_links = []
    number = 0

    with open('../raw_data/saopaulo.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count != 0:
                keep[row[0]] = number
                nodes.append(toNode(row, number))
                number += 1
            line_count += 1

    with open('../raw_data/saopaulo.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count != 0:
                links.append(toLink(row, keep))
                number += 1
            line_count += 1

    for col in links:
        for link in col:
            final_links.append(link)

    print(len(final_links))

    fileContent = {"nodes": nodes, "links": final_links}
    with open(location, "w") as fh:
        json.dump(fileContent, fh, indent=2)


def toNode(row, number, color="red"):
    return {"id": number, "label": row[1], "color": color}


def toLink(row, keep):
    final = []
    neighs = row[6].replace("[", "").replace(
        "]", "").replace("'", "").split(",")
    source = keep[row[0]]
    targets = list(map(lambda x: keep[x.strip()], neighs))
    for target in targets:
        final.append({"source": source, "target": target})
    return final


if __name__ == "__main__":
    main()
