import mysql.connector
import json
import os


def main():
    if os.path.exists("../graphs/Paris.json"):
        exit("Database already exists")

    config = {
        "host": "127.0.0.1",
        "port": 3306,
        "user": "root",
        "password": "1200",
        "name": "metroparis"
    }
    cnx = mysql.connector.connect(
        host=config["host"],
        port=config["port"],
        user=config["user"],
        password=config["password"],
        database=config["name"]
    )

    nodes = []
    links = []
    weights = {}

    cur = cnx.cursor()
    cur.execute("SELECT * FROM fermata")
    data = cur.fetchall()
    for row in data:
        nodes.append(toNode(row))

    cur.execute("SELECT * FROM connessione")
    data = cur.fetchall()
    for row in data:
        first = str(row[2])
        second = str(row[3])
        key = first + second
        if key in weights:
            weights[key] += 1
        else:
            weights[key] = 1

    for row in data:
        first = str(row[2])
        second = str(row[3])
        key = first + second
        if key in weights:
            edge = {"source": first, "target": second, "weight": weights[key]}
            links.append(edge)
            del weights[key]

    cnx.close()
    fileContent = {"directed": True, "nodes": nodes, "links": links}

    with open("../graphs/Paris.json", "w") as fh:
        json.dump(fileContent, fh, indent=2)


def toNode(row, color="red"):
    return {"id": row[0], "label": row[1], "color": color}


if __name__ == "__main__":
    main()
