from subprocess import call
import pickle
import subprocess
#call(["ff/./ff","-p","/Users/nissimergas/Desktop/ipre/","-o","main_domain.pddl","-f","temporal.pddl"])
result = subprocess.run(["ff/./ff","-p","/Users/nissimergas/Desktop/ipre/","-o","main_domain.pddl","-f","temporal.pddl"]
                        , stdout=subprocess.PIPE)
print(type(str(result.stdout)))
output=str(result.stdout)
inicio=output.find("step" )
fin=output.find("ntime" )
#print(output[inicio:fin])
file = open("resultado_terminal.txt","w")
lineas=output[inicio:fin].strip("step").split("n")
for li in lineas:
    print(li)
    l=li.strip('\ ')
    f=l.find(" ")
    if len(l[f:].lower().strip(" "))>2:
        file.write("("+l[f:].lower().strip(" ")+")"+"\n")
file.close()