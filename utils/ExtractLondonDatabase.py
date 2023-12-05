import json
import os


def main():
    if os.path.exists("../graphs/London.json"):
        exit("Database already exists")

    keep = {}
    nodes = []
    links = []

    with open("../raw_data/london_nodes.txt") as fh:
        lines = fh.readlines()
        for line in lines:
            temp = line.split(" ")
            keep[temp[1]] = temp[0]
            nodes.append(toNode(line))

    with open("../raw_data/london_edges.txt") as fh:
        lines = fh.readlines()
        for line in lines:
            links.append(toLink(line, keep))

    fileContent = {"nodes": nodes, "links": links}
    with open("../graphs/London.json", "w") as fh:
         json.dump(fileContent, fh, indent=2)

def toNode(line):
    line = line.split(" ")
    return {"id": line[0], "name": line[1]} 

def toLink(line, keep):
    line = line.split(" ")
    return {"source": keep[line[1].strip()], "target": keep[line[2].strip()]} 

if __name__ == "__main__": main()
