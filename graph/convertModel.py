import os
import json

colours = ["#FF0000","#DC6F6F","#8D1919","#FCADAD","#733F3F","yellow", "cyan", "pink"]

def main():
    for filename in os.listdir("../Models/"):
        name, ext = os.path.splitext(filename)
        if ext == ".txt":
            file = os.path.join("../Models/", filename)
            with open(file, 'r') as f:
                data = {}
                iteration = 1
                rel_iterate = 1
                use_valuations = False
                use_relations = False
                data['nodes'] = []
                data['edges'] = []
                data['total_relations'] = []
                for line in f:
                    if "Valuations:" in line:
                        iteration = 1
                        use_valuations = True
                        continue
                    elif "Relations:" in line:
                        iteration = 1
                        rel_iterate = 1
                        use_relations = True
                        use_valuations = False
                        continue
                    if use_valuations:
                        if (line[0][0] != "#" and line != "\n"):
                            data['nodes'].append({
                                "id": iteration,
                                "label": line.split(":")[1].replace("\n", "")[1:],
                                "shape": "circle",
                                "size": 10,
                                "color": "#e3e3e3"
                            })
                            iteration+=1

                    if use_relations:
                        if (line[0][0] != "#" and line != "\n"):
                            current_relations = line.split(":")[1].split(",")
                            for relation in current_relations:
                                used_relation = relation[relation.find("(")+len("("):relation.rfind(")")]
                                data['edges'].append({
                                    "from": int(used_relation.split(" ")[0])+1,
                                    "to": int(used_relation.split(" ")[1])+1,
                                    "value": 1,
                                    "color": {
                                        "color": colours[rel_iterate-1]
                                    }
                                },)
                            iteration+=1
                        rel_iterate += 1
                    data['total_relations'] = rel_iterate-1
                    pass
                file_name = name + ".json"
                with open(file_name, 'w') as outfile:
                    json.dump(data, outfile)


if __name__ == "__main__":
    main()