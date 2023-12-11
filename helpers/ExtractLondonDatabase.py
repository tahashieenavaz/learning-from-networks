import json
import os


def main():
    if os.path.exists("../graphs/London.json"):
        exit("Database already exists")

    keep = {}
    nodes = []
    links = []
    weights = {}

    with open("../raw_data/london_nodes.txt") as fh:
        lines = fh.readlines()
        for line in lines:
            temp = line.split(" ")
            keep[temp[1]] = temp[0]
            nodes.append(toNode(line))

    with open("../raw_data/london_edges.txt") as fh:
        lines = fh.readlines()
        for line in lines:
            line = line.split(" ")
            first = keep[line[1]]
            second = keep[line[2].strip()]
            key = first + second
            if key in weights:
                weights[key] += 1
            else:
                weights[key] = 1

        for line in lines:
            line = line.split(" ")
            first = keep[line[1]]
            second = keep[line[2].strip()]
            key = first + second
            if key in weights:
                edge = {
                    "source": first,
                    "target": second,
                    "weight": weights[key]
                }
                links.append(edge)
                del weights[key]

    fileContent = {"nodes": nodes, "links": links}
    with open("../graphs/London.json", "w") as fh:
        json.dump(fileContent, fh, indent=2)


def toNode(line):
    line = line.split(" ")
    return {"id": line[0], "label": line[1], "color": "green"}


if __name__ == "__main__":
    main()
