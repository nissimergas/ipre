import urllib.request as urllib2
import urllib.parse
import  json, sys
import pickle
import requests
##el ejemplo funciona bien si le saco a la definicion del dominio los obstaculos...
##probablemente esto se deba a problemas con la memoria y el tiempo de ejecucion...
data1 = {'domain': open("main_domain.pddl", 'r').read(),
        'problem': open("temporal.pddl", 'r').read()}
r = requests.post('http://solver.planning.domains/solve', data=data1, allow_redirects=True)
#s=json.loads(pickle.loads(r.content))
s=r.content.decode("utf-8")
s=json.loads(s)

print(s["result"]["plan"])
file = open("resultado.txt","w")
for instruccion in s["result"]["plan"]:
        print(instruccion["name"])
        file.write(instruccion["name"]+"\n")
#print (s)
file.close()
