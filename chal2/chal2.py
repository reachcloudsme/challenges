#!/usr/bin/python3

import json
import sys, getopt
import ast
import requests

metadata_url = 'http://169.254.169.254/latest/'


def inflate_expr(url,arr):
    response = {}
    for item in arr:
        new_url = url + item
        r = requests.get(new_url)
        text = r.text
        if item[-1] == "/":
            list_of_values = r.text.splitlines()
            response[item[:-1]] = inflate_expr(new_url, list_of_values)
        elif check_is_json(text):
            response[item] = json.loads(text)
        else:
            response[item] = text
    return response


def get_data(path):
    initial = [path]
    result = inflate_expr(metadata_url, initial)
    return result

def get_data_json(path):
    metadata = get_data(path)
    metadata_json = json.dumps(metadata, indent=4, sort_keys=True)
    return metadata_json


def check_is_json(inp_json):
    try:
        json.loads(inp_json)
    except ValueError:
        return False
    return True



def flatten_json_keys(nested_json):

    out = {}


    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '/')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '/')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(nested_json)
    return out



def main(nested_json):
    if len(sys.argv) == 1:
        print("*****You have not provided a key hence providing entire response *****")
        print(json.dumps(nested_json, indent=4,sort_keys=True))
        return 0
    elif len(sys.argv) == 2:
        req_key = sys.argv[1]
    else:
        print("*****You have provided more than one key hence no response, type python3 chal2.py help *****")
        return 0

    if req_key == "help":
        print("Please provide data key in double quotes, for example: python3 chal2.py \"meta-data\ami-id\"")
        exit(0)

    flat_keys=flatten_json_keys(nested_json)
    #print(flat_keys)

    for key,value in flat_keys.items():
        if key == req_key:
            print("***** Value found for provided key *****")
            print(value)
            break
    else:
        print("***** No value found for provided key *****")
    return 0

def convert_to_dict(x):
    tes=ast.literal_eval(str(x))
    return tes

    
def merge_two_dicts(x, y):
    z = x.copy()   
    z.update(y)    
    return z


if __name__ == "__main__":
    #print(get_data_json("meta-data/"))
    #print(get_data_json("user-data/"))
    meta_json = get_data_json("meta-data/")
    meta_dict = convert_to_dict(meta_json)
    user_json= get_data_json("user-data/")
    user_dict = convert_to_dict(user_json)
    nested_dict =  merge_two_dicts(meta_dict, user_dict)
    main(nested_dict)

