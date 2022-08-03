#!/usr/bin/python3

import json
import sys
import ast




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



def main():
    if len(sys.argv) < 3:
        print("***** You have not provided enough arguments, hence no response, please provide input as: python3 chal3.py jsonfile \"data-key\" *****")
        return 0
    elif len(sys.argv) == 3:
        req_obj = sys.argv[1]
        req_key = sys.argv[2]
    else:
        print("*****You have provided more than expected arguments hence no response, please provide input as: python3 chal3.py jsonfile \"data-key\" *****")
        return 0

    try:
        with open(req_obj, 'r') as openfile:
            json_object = json.load(openfile)
            json_object=ast.literal_eval(json.dumps(json_object))
    except EnvironmentError:        
        print("File cannot be opened, try again..")
        exit(0)
        
        #print(json_object)
        #print(type(json_object))

    flat_keys=flatten_json_keys(json_object)
    #print(flat_keys)

    for key,value in flat_keys.items():
        if key == req_key:
            print("***** Value found for provided key *****")
            print(value)
            break
    else:
        print("***** No value found for provided key *****")
    return 0


if __name__ == "__main__":
    main()

