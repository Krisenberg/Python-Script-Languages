from os import environ
import sys

def list_env():
    listEnv = []
    for env in environ:
        listEnv.append((env, environ[env]))
    return listEnv
        
def sorted_env():
    return sorted(list_env())

def filtered_env(args):
    listFiltered = []
    listSorted = sorted_env()
    parameters = args[1:]
    if not(parameters):
        return listSorted
    for arg in args:
        for env in listSorted:
            if(arg in env[0]):
                listFiltered.append(env)
    return listFiltered
    

if __name__ == "__main__":
    list = filtered_env(sys.argv)
    for line in list:
        print(f"{line[0]} = {line[1]}\n")