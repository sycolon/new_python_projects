import json
import os

#file_path = os.path.abspath(__file__)
file_dir = os.path.dirname(__file__)
#print(file_path)
print(file_dir)

#print(os.path.join(os.path.dirname(__file__),"person.json"))

with open(os.path.join(os.path.dirname(__file__),"person.json"), "r") as f:
    data = json.load(f)
    print(data)
    #print(type(data))

user_data = {
    "name":"Ibrahim",
    "role":"Software Developer",
    "active":True
}

# with open("output.json","w") as file:
#     json.dump(user_data, file, indent=4)

with open(os.path.join(os.path.dirname(__file__),"output.json"),"w") as file:
    json.dump(user_data, file, indent=4)

# loads
# dumps 

data = {
    "name":"Ubuntu Linux",
    "version": 26.04,
    "active" : True
}

json_string = json.dumps(data)
print(json_string)
print(type(json_string))

raw_input = '{"status":1, "code":100}'

parsed_data = json.loads(raw_input)

print(type(parsed_data))
print(parsed_data)