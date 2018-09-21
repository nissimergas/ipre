from time import sleep
from PyQt4 import QtGui
from PyQt4.QtCore import QTimer
from PyQt4.QtCore import QRect, QPropertyAnimation
import  json
import requests
import subprocess

class Robot:
    def __init__(self,x,y,id,ventana):
        self.x=((x-22)//37)
        self.y=((y-146)//33)
        self.x_cor=x
        self.y_cor=y
        self.id=id
        self.pic = QtGui.QLabel(ventana)
        #self.pic.resize(70, 70)
        self.pic.setPixmap(QtGui.QPixmap("robot.png").scaledToWidth(50))
        self.pic.show() # You were missing this.
        self.pic.move(x-26,y-30)
        self.left=Ball2()
        self.right=Ball2()




    def move(self,x,y):
        #self.pic.hide()
        #self.pic.setPixmap(QtGui.QPixmap("robot.png").scaledToWidth(50))
        #self.pic.resize(70, 70)
        #self.pic.setPixmap(QtGui.QPixmap("robot.png").scaledToWidth(50))
        self.pic.move(x-26,y-30)
        self.left.move(x-20-21,y-30)
        self.right.move(x-20+21,y-30)
        #self.pic.show() # You were missing this.
        #return self.pic.show()
    def agarrar(self, ball,hand):
        print("11111")
        if hand=="r":
            print("hola")
            self.right=ball
            x=self.pic.x()+17
            y=self.pic.y()

            self.right.move(x,y)
        if hand=="l":
            print("chao")
            self.left=ball
            x=self.pic.x()-17
            y=self.pic.y()

            self.left.move(x,y)
    def soltar(self,ball,hand):
        pass

class Ball2:
    def move(self,x,y):
        pass



class Ball:
    def __init__(self,x,y,id,ventana):
        self.x=((x-22)//37)
        self.y=((y-146)//33)
        self.x_cor=x
        self.y_cor=y
        self.id="ball"+str(id)
        self.pic = QtGui.QLabel(ventana)

        self.pic.setPixmap(QtGui.QPixmap("pelota.png").scaledToWidth(40))


        self.pic.show() # You were missing this.
        self.pic.move(x-20,y-20)
        self.nombre = QtGui.QLabel(ventana)
        self.nombre.setText(str(id))
        self.nombre.move(x,y)
        self.nombre.show()
    def move(self,x,y):
        self.pic.move(x,y)
        self.nombre.move(x+20,y+25)


class Obstaculo:
    def __init__(self,x,y,id,ventana):
        self.x=((x-22)//37)
        self.y=((y-146)//33)
        self.x_cor=x
        self.y_cor=y
        self.id="obstaculo"+str(id)
        self.pic = QtGui.QLabel(ventana)

        self.pic.setPixmap(QtGui.QPixmap("obstaculo.png"))
        self.pic.show() # You were missing this.
        self.pic.move(x-18.5,y-16.5)

        self.pic2 = QtGui.QLabel(ventana)

        self.pic2.setPixmap(QtGui.QPixmap("obstaculo.png"))
        self.pic2.show() # You were missing this.
        self.pic2.move(x-18.5+630,y-16.5)


class  MiMapa (QtGui.QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Mundo de los robots')
        # Definimos la geometría de la ventana.
        # Parámetros: (x_top_left, y_top_left, width, height)
        # p = QtGui.QPalette()
        # gradient = QtGui.QLinearGradient(0, 0, 0, 400)
        # gradient.setColorAt(1.0, QtGui.QColor(252, 252, 252))
        # p.setBrush(QtGui.QPalette.Window, QtGui.QBrush(gradient))
        # self.setPalette(p)
        # self.show()
        self.timer = QTimer(self)
        self.cont_obstaculos=0
        self.background = QtGui.QLabel(self)
        self.background.setPixmap(QtGui.QPixmap("fondo.png"))
        self.background.resize(600, 600)
        self.background.move(20,110)
        self.instrucciones=[]
        self.program_counter=0

        #self.obstaculo = QtGui.QLabel(self)
        #self.obstaculo.setPixmap(QtGui.QPixmap("obstaculo.png"))
        #self.obstaculo.move(21,147)

        self.text1 = QtGui.QLabel(self)
        self.text1.setText("condiciones iniciales")
        self.text1.move(200,110)

        self.boton1 = QtGui.QPushButton('&delete pelotas', self)
        self.boton1.resize(self.boton1.sizeHint())
        self.boton1.move(10, 20)
        self.boton1.clicked.connect(self.boton1_callback)

        self.boton_bor_ob = QtGui.QPushButton('&delete obstaculo', self)
        self.boton_bor_ob.resize(self.boton_bor_ob.sizeHint())
        self.boton_bor_ob.move(150, 20)
        self.boton_bor_ob.clicked.connect(self.boton_bor_ob_callback)

        self.boton2 = QtGui.QPushButton('&delete robot', self)
        self.boton2.resize(self.boton1.sizeHint())
        self.boton2.move(10, 50)
        self.boton2.clicked.connect(self.boton2_callback)

        self.boton_pelota = QtGui.QPushButton('&pelota', self)
        self.boton_pelota.resize(self.boton_pelota.sizeHint())
        self.boton_pelota.move(150, 50)
        self.boton_pelota.clicked.connect(self.boton_pelota_callback)

        self.boton3 = QtGui.QPushButton('&codigo', self)
        self.boton3.resize(self.boton1.sizeHint())
        self.boton3.move(10, 80)
        self.boton3.clicked.connect(self.boton3_callback)

        self.boton_obstaculos = QtGui.QPushButton('&obstaculos', self)
        self.boton_obstaculos.resize(self.boton_obstaculos.sizeHint())
        self.boton_obstaculos.move(150, 80)
        self.boton_obstaculos.clicked.connect(self.boton_obstaculos_callback)

        self.boton_poner_rob = QtGui.QPushButton('&poner robot', self)
        self.boton_poner_rob.resize(self.boton_poner_rob.sizeHint())
        self.boton_poner_rob.move(250, 50)
        self.boton_poner_rob.clicked.connect(self.poner_rob_call)

        self.background2 = QtGui.QLabel(self)
        self.background2.resize(600, 600)
        self.background2.setPixmap(QtGui.QPixmap("fondo.png"))
        self.background2.move(650,110)
        self.text2 = QtGui.QLabel(self)
        self.text2.setText("condiciones finales")
        self.text2.move(870,110)

        self.boton4 = QtGui.QPushButton('&delete pelotas', self)
        self.boton4.resize(self.boton4.sizeHint())
        self.boton4.move(650, 20)
        self.boton4.clicked.connect(self.boton4_callback)

        self.boton5 = QtGui.QPushButton('&delete robot', self)
        self.boton5.resize(self.boton5.sizeHint())
        self.boton5.move(650, 50)
        self.boton5.clicked.connect(self.boton5_callback)



        self.boton_ejecutar = QtGui.QPushButton('&ejecutar api', self)
        self.boton_ejecutar.resize(self.boton_ejecutar.sizeHint())
        self.boton_ejecutar.move(650, 80)
        self.boton_ejecutar.clicked.connect(self.ejecutar_acciones)

        self.boton_ejecutar2 = QtGui.QPushButton('&ejecutar local', self)
        self.boton_ejecutar2.resize(self.boton_ejecutar.sizeHint())
        self.boton_ejecutar2.move(650, 110)
        self.boton_ejecutar2.clicked.connect(self.ejecutar_acciones2)

        self.contador_rob=0
        self.contador_ball=0
        self.robots=[]
        self.balls=[]
        self.robots_final=[]
        self.balls_final=[]
        self.obstaculos=[]
        #self.setGeometry(400, 400, 700, 700)
        self.setFixedSize(1300, 700)
        self.contador="r"
        self.contador_final="r"



    def poner_rob_call(self):
        if len(self.robots)==0:
            self.contador="r"
        if len(self.robots_final)==0:
            self.contador_final="r"
    def boton_pelota_callback(self):
        self.contador="p"
    def boton_obstaculos_callback(self):
         self.contador="o"
         print("dfdf")
    def boton1_callback(self):
        # Este método maneja el evento sobre quien opera
        if len(self.balls)>0:
                b=self.balls.pop()
                b.pic.hide()
                b.nombre.hide()

        if len(self.robots)>0:
            self.contador="p"
        else:
            self.contador="r"

    def boton2_callback(self):
         if len(self.robots)>0:
            self.robots[0].pic.hide()
            self.robots=[]
            self.contador="r"

    def boton3_callback(self):
        if len(self.robots_final)==len(self.robots) and len(self.balls_final)==len(self.balls):
            self.generar()

    def boton4_callback(self):
        if len(self.balls_final)>0:
                b=self.balls_final.pop()
                b.pic.hide()
                b.nombre.hide()

        if len(self.robots_final)>0:
            self.contador_final="p"
        else:
            self.contador_final="r"

    def boton5_callback(self):
        if len(self.robots_final)>0:
            self.robots_final[0].pic.hide()
            self.robots_final=[]
            self.contador_final="r"
    def boton_bor_ob_callback(self):
        if len(self.obstaculos)>0:
            ob=self.obstaculos.pop()
            ob.pic.hide()
            ob.pic2.hide()



    def mousePressEvent(self, event):
        # Este método maneja cuando se presiona alguno de los botones del mouse.
        # Viene creada por defecto en la aplicación. Se puede sobreescribir el
        # método de acuerdo a como se maneja el evento en cada aplicación.
        x=event.x()
        y= event.y()
        print("x:",x)
        print("y:",y)
        print(self.contador)
        if (self.contador=="r" and x<613)or (self.contador_final=="r" and x>613):
            self.robot(x,y)
            print("sfsd")
        elif self.contador=="o":
            print("obs")
            self.obstaculo(x,y)


        else:
            self.pelota(x,y)
    def robot(self,x,y):
        # self.pic = QtGui.QLabel(self)
        # self.pic.resize(110, 110)
        # self.pic.setPixmap(QtGui.QPixmap("robot.png").scaledToWidth(80))
        # self.pic.show() # You were missing this.
        # self.pic.move(x-20,y-40)
        if x>21 and y>146 and x<613 and y<674 and self.contador=="r":
            x=((x-22)//37)*37+22+18.5
            y=((y-146)//33)*33+146+16.5
            r=Robot(x,y,1,self)
            self.robots.append(r)
            self.contador="p"

        if x>652 and y>146 and x<1244 and y<674 and self.contador_final=="r":
            x=((x-652)//37)*37+652+18.5
            y=((y-146)//33)*33+146+16.5
            r=Robot(x,y,1,self)
            self.robots_final.append(r)
            self.contador_final="p"

    def obstaculo(self,x,y):
        # self.pic = QtGui.QLabel(self)
        # self.pic.resize(110, 110)
        # self.pic.setPixmap(QtGui.QPixmap("robot.png").scaledToWidth(80))
        # self.pic.show() # You were missing this.
        # self.pic.move(x-20,y-40)
        if x>21 and y>146 and x<613 and y<674 and self.contador=="o":

            x=((x-22)//37)*37+22+18.5
            y=((y-146)//33)*33+146+16.5
            o=Obstaculo(x,y,self.cont_obstaculos,self)
            self.obstaculos.append(o)
            self.cont_obstaculos+=1

    def pelota(self,x,y):
        if x>21 and y>146 and x<613 and y<674 and self.contador=="p":
            x=((x-22)//37)*37+22+18.5
            y=((y-146)//33)*33+146+16.5
            s=Ball(x,y,len(self.balls),self)
            self.balls.append(s)
            self.contador_ball+=1
        if  x>652 and y>146 and x<1244 and y<674 and self.contador_final=="p":
            x=((x-22)//37)*37+22+18.5
            y=((y-146)//33)*33+146+16.5
            s=Ball(x,y,len(self.balls_final),self)
            self.balls_final.append(s)
            self.contador_ball+=1
        # self.pic = QtGui.QLabel(self)
        # self.pic.resize(110, 110)
        # self.pic.setPixmap(QtGui.QPixmap("pelota.png").scaledToWidth(80))
        # self.pic.show() # You were missing this.
        # self.pic.move(x-20,y-40)
    def generar(self):
        code="""(define (problem problema2)
                (:domain  gripper2)"""
        code+="(:objects "
        posiciones=""
        for i in range (16):
            posiciones+=" x"+str(i)+" y"+str(i)
        code+=posiciones
        id=0
        for ball in self.balls:
            code+= " ball{0} ".format(id)
            id+=1

        code+=" left right) (:init  "
        for i in range (16):
            code+=" (coord_x x"+str(i)+" ) (coord_y y"+str(i)+ ")"+"\n"

        for i in range (15):
            code+=" (next x"+str(i)+" x"+str(i)+")"
            code+=" (next y"+str(i)+" y"+str(i)+")"
            code+=" (next x"+str(i)+" x"+str(i+1)+")"
            code+=" (next y"+str(i)+" y"+str(i+1)+")"
            code+=" (next x"+str(i+1)+" x"+str(i)+")"
            code+=" (next y"+str(i+1)+" y"+str(i)+")"+"\n"
        id=0
        code+=" (next x15"+" x15)"
        code+=" (next y15"+" y15)"
        for ball in self.balls:

            code+="(BALL ball{0})(at-ball ball{0} {1} {2}) ".format(id, "x"+str(int(ball.x)), "y"+str(int(ball.y)))
            id+=1
        matriz=[[0 for i in range(16)]for j in range(16)]
        for obstaculo in self.obstaculos:
            matriz[int(obstaculo.x)][int(obstaculo.y)]=1
        for obstaculo in self.obstaculos:
             code+="(at-obstaculo {0} {1}) ".format( "x"+str(int(obstaculo.x)), "y"+str(int(obstaculo.y)))
       # for x in range(16):
        #    for y in range(16):
         #       if matriz[x][y]==0:
          #          code+="(noobstaculo {0} {1}) \n".format( "x"+str(int(x)), "y"+str(int(y)))


        code+="(GRIPPER left) (GRIPPER right) (free left) (free right)"
        code+="(at-robby {0} {1}) ".format("x"+str(int(self.robots[0].x)), "y"+str(int(self.robots[0].y)))
        code+=")" #cierre init
        code+="""(:goal (and"""
        code+="(at-robby x{0} y{1})".format(str(int(self.robots_final[0].x-17)),str(int(self.robots_final[0].y)))

        # """(at-ball_x ball1 x5) (at-ball_y ball1 y7)
        # (at-ball_x ball2 x5) (at-ball_y ball2 y7)
        # (at-ball_x ball3 x5) (at-ball_y ball3 y7)
        # """
        id=0
        for ball in self.balls_final:
            code+=" (at-ball ball{0} {1} {2}) ".format(id, "x"+str(int(ball.x-17)), "y"+str(int(ball.y)))
            id+=1

        code+="""
        ))
        )"""
        f = open("temporal.pddl", "w")
        f.write(code)
        f.close()


        print(code)
    def mover(self):


        self.robots[0].pic.hide()
        self.robots[0].pic.setPixmap(QtGui.QPixmap("robot.png").scaledToWidth(50))
        self.robots[0].pic.resize(70, 70)
        self.robots[0].pic.setPixmap(QtGui.QPixmap("robot.png").scaledToWidth(50))
        #self.robots[0].pic.move(self.x2real, self.y2real)
        x2r=self.instrucciones[self.program_counter][2]
        y2r=self.instrucciones[self.program_counter][3]
        x2real=int(x2r[1:])*37+22
        y2real=int(y2r[1:])*33+141
        self.robots[0].pic.move(x2real, y2real)
        print(" x    y   ",x2real,y2real)
        self.robots[0].pic.show()
        self.program_counter+=1

    def funcion_instrucciones(self):
        if len(self.instrucciones)>self.program_counter:
            if self.instrucciones[self.program_counter][0]=="move":
                x2real =self.instrucciones[self.program_counter][3]
                y2real=self.instrucciones[self.program_counter][4]
                self.robots[0].move(x2real,y2real)
                #self.robots[0].pic.move(x2real-26, y2real-30)
                print(" x    y   ",x2real,y2real)
                #self.robots[0].pic.show()
                self.program_counter+=1
            elif self.instrucciones[self.program_counter][0]=="pick-up":
                pelota=None
                for ball in self.balls:
                    print("comparacion  ",ball.id, self.instrucciones[self.program_counter][1] )
                    if ball.id==self.instrucciones[self.program_counter][1]:
                        pelota=ball
                hand=self.instrucciones[self.program_counter][4]
                if hand=="right":
                    self.robots[0].agarrar(pelota,"r")
                if hand=="left":
                    self.robots[0].agarrar(pelota,"l")
                self.program_counter+=1

            elif self.instrucciones[self.program_counter][0]=="drop":
                x2real =self.instrucciones[self.program_counter][2]
                y2real=self.instrucciones[self.program_counter][3]

                hand=self.instrucciones[self.program_counter][4]
                pelota=None
                if hand=="right":
                    pelota=self.robots[0].right
                    self.robots[0].right=Ball2()

                elif hand=="left":
                    pelota=self.robots[0].left
                    self.robots[0].left=Ball2()
                pelota.pic.move(x2real-20,y2real-18)
                pelota.nombre.move(x2real,y2real)
                self.program_counter+=1








    def ejecutar_acciones2(self):
        self.generar()
        ####################################
        #### codigo para pddl local #########
        ####################################
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
        ######crear resultados




        ###############################fin
        dic={"move":self.move}
        with open('resultado_terminal.txt','r') as f:
            instrucciones=f.readlines()
        for instruccion in instrucciones:
            parametros=instruccion.strip("(").strip(")").split()
            nombre_instr=parametros[0]
           # for parametro in parametros:
               # print(parametro)
            if nombre_instr=="move":
                x2r=parametros[3]
                y2r=parametros[4].strip(")")
                x2real=int(x2r[1:])*37+22+18.5
                y2real=int(y2r[1:])*33+141+18.5
                self.instrucciones.append((nombre_instr,parametros[1],parametros[2],x2real,y2real))
            elif nombre_instr=="pick-up":
                print("hola")
                self.instrucciones.append((nombre_instr,parametros[1],parametros[2],parametros[3],parametros[4].strip(")")))
            elif nombre_instr=="drop":
                x2r=parametros[2]
                y2r=parametros[3].strip(")")
                x2real=int(x2r[1:])*37+22+18.5
                y2real=int(y2r[1:])*33+141+18.5

                self.instrucciones.append((nombre_instr,parametros[1],x2real,y2real,parametros[4].strip(")")))
            #dic[nombre_instr](parametros[1],parametros[2],parametros[3],parametros[4].strip(")"))
             #dic[nombre_instr]()

        self._timer = QTimer(interval=1,
                                    timeout=self.funcion_instrucciones)
        self._timer.start(500)



    def ejecutar_acciones(self):
        self.generar()
        ####################################
        #### codigo para pddl nube #########
        ####################################

        data1 = {'domain': open("main_domain.pddl", 'r').read(),
        'problem': open("temporal.pddl", 'r').read()}

        r = requests.post('http://solver.planning.domains/solve', data=data1, allow_redirects=True)
        s=r.content.decode("utf-8")
        s=json.loads(s)
        print(s["result"]["plan"])
        file = open("resultado.txt","w")
        for instruccion in s["result"]["plan"]:
            print(instruccion["name"])
            file.write(instruccion["name"]+"\n")
        file.close()


        ###############################fin
        dic={"move":self.move}
        with open('resultado.txt','r') as f:
            instrucciones=f.readlines()
        for instruccion in instrucciones:
            parametros=instruccion.strip("(").strip(")").split()
            nombre_instr=parametros[0]
           # for parametro in parametros:
               # print(parametro)
            if nombre_instr=="move":
                x2r=parametros[3]
                y2r=parametros[4].strip(")")
                x2real=int(x2r[1:])*37+22+18.5
                y2real=int(y2r[1:])*33+141+18.5
                self.instrucciones.append((nombre_instr,parametros[1],parametros[2],x2real,y2real))
            elif nombre_instr=="pick-up":
                print("hola")
                self.instrucciones.append((nombre_instr,parametros[1],parametros[2],parametros[3],parametros[4].strip(")")))
            elif nombre_instr=="drop":
                x2r=parametros[2]
                y2r=parametros[3].strip(")")
                x2real=int(x2r[1:])*37+22+18.5
                y2real=int(y2r[1:])*33+141+18.5

                self.instrucciones.append((nombre_instr,parametros[1],x2real,y2real,parametros[4].strip(")")))
            #dic[nombre_instr](parametros[1],parametros[2],parametros[3],parametros[4].strip(")"))
             #dic[nombre_instr]()

        self._timer = QTimer(interval=1,
                                    timeout=self.funcion_instrucciones)
        self._timer.start(500)


if __name__ == '__main__':
    app = QtGui.QApplication([])
    mapa = MiMapa()
    mapa.show()
    app.exec_()