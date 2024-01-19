import os
import csv
import json


def main():
    location = "../graphs/London.json"
    if os.path.exists(location):
        exit("Database already exists")

    keep = {}
    nodes = []
    links = []
    final_links = []
    number = 0

    with open('../raw_data/london_new_nodes.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count != 0:
                keep[row[3]] = number
                nodes.append(toNode(row, number, "purple"))
                number += 1
            line_count += 1

    with open('../raw_data/london_new_edges.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count != 0:
                links.append(toLink(row, keep))
            line_count += 1

    fileContent = {"directed": False, "nodes": nodes, "links": links}
    with open(location, "w") as fh:
        json.dump(fileContent, fh, indent=2)


def toNode(row, number, color="red"):
    return {"id": number, "label": row[3], "color": color}


def toLink(row, keep):
    return {"source": int(row[0]), "target": int(row[1]), "weight": 1}


if __name__ == "__main__":
    main()
