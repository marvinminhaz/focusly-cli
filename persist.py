import json
import os

#TO CREATE OR UPDATE EXISTING FILE
def update_file(directory, filepath, a_list):
    os.makedirs(directory, exist_ok=True)

    with open(filepath, "w") as file:
        json.dump(a_list, file)

#TO READ EXISTING FILE
def read_file(filepath):
    if os.path.isfile(filepath):
        with open(filepath, "r") as file:
            retrieved_list = json.load(file)
            return retrieved_list
    else:
        return[]


#TEST
if __name__ == "__main__":
    my_list = ["one", "tw", "three"]
    dir_path = "memory"
    filepath = "memory/list.json"
    update_file(dir_path, filepath, my_list)
    other_list = read_file(filepath)
    if len(my_list) == len(other_list):
        print('Yes')
