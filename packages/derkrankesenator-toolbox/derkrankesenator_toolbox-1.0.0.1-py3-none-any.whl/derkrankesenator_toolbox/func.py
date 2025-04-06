import math
import json
from tqdm import tqdm

def checkprime(num):
    cnt =0
    if(isinstance(num,int)):
        for i in range(1, num + 1):
            if num % i == 0:
                cnt += 1
            else:
                pass
        if(cnt == 2):
            return True
        else:
            return False
    else:
        return False


def list_sum(list):
    sum = 0
    for i in range(len(list)):
        sum += list[i]
    return sum


def pi(its=10000000, tq=False):
    pi6 = 0
    pi6h = 0
    pi = 0
    if tq:
        for i in tqdm(range(1, its)):
            pi6 += 1 / (i ** 2)
            pi6h = pi6 * 6
            pi = math.sqrt(pi6h) 
    else:
        for i in range(1, its):
            pi6 += 1 / (i ** 2)
            pi6h = pi6 * 6
            pi = math.sqrt(pi6h) 
    return pi


def write_json(dict, path):
    with open(path, "w") as file:
        json.dump(dict)


def read_json(path):
    with open(path, "r") as file:
        dict = json.load(file)
    return dict


def diff(int1, int2):
    diff = abs(int1 - int2)
    return diff
