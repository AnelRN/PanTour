#Libreria Grafica
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5.QtCore import QTimer,Qt
#Libreria para Mapas
import geopandas as gpd
import matplotlib.pyplot as plt
import json

class Provincias():
    def __init__(self,nombreProvincia,long,lat,data):
        self.nombre = nombreProvincia
        self.long = long
        self.lat = lat
        self.opsTuristicas = []
 
    ##Genera Marcador en funcion de la latitud y longitud 
    def marcador(self):
        x,y = ax.transData.transform((self.long,self.lat))
        marcador = QPushButton("", window)
        marcador.setFixedSize(100,100)
        marcador.move(int(x),int(y-445))
        marcador.setIcon(QIcon("marcador.png"))
        marcador.setIconSize(marcador.size())
        marcador.setStyleSheet("""
        QPushButton {
            background-color: transparent; 
            border: none;
        }
        QPushButton:hover {
            background-color: rgba(100, 100, 255, 0.5); 
        }
        """)
        
        
#Crea caja para alinear elementos
def contentBox():#Colocar de para metros el nombre del lugar turistico y la img 
    ventanaAux = QWidget()
    contentBox = QVBoxLayout(ventanaAux)
    label = QLabel("Label")
    button = QPushButton("Boton")
    
    contentBox.addWidget(label)
    contentBox.addWidget(button)
    
    return ventanaAux
    
    
#Ventana emergente para mostrar informacion de provincia y sus sitios turisticos
def ventanaEmergente(prov):
    
    sizex = window.width()//2
    sizey = window.height()//2 + int((window.height()//2)*0.35)
    
    x = window.x() +(window.width() - sizex)//2
    y = window.y() + (window.height() - sizey)//2
    
    
    ventanaEmergente = QDialog(window)
    ventanaEmergente.setGeometry(x, y, sizex, sizey)
    ventanaEmergente.setWindowFlags(Qt.FramelessWindowHint)
    ventanaEmergente.setStyleSheet("""
        QDialog {
            background-color: #ffffff;  
            border-radius: 12px;  
            border: 3px solid #000000;
        }
    """)
    veLayout = QGridLayout()
    nombreLabel = QLabel(f"{prov.nombreProvincia}")
    descripLabel = QLabel("{prov.nombreDescrip}")
    
    veLayout.addWidget(nombreLabel,0,0,1,2,alignment=Qt.AlignCenter)
    veLayout.addWidget(descripLabel,1,0,1,2,alignment=Qt.AlignCenter)
  
    
    for row in range(2):
        for col in range(2):
            veLayout.addWidget(contentBox(),row+2,col)
    
    ventanaEmergente.setLayout(veLayout)
   
    ventanaEmergente.exec_()
    


#Cargar info de provs
with open('ProvinciasTest.json', 'r' , encoding = 'utf-8') as provfile:
    provsData = json.load(provfile)

#Genera la Ventana Principal
tourPan = QApplication([])
window = QWidget()

#Mostramos la ventana a pantalla completa y luego la escondemos 
window.showFullScreen()
window.setVisible(False)

#Pixeles por pulgadas(Es el que MPL usa por default para crear sus figuras)
dpi=100
#Se obtiene el tamano de la pantalla
xPixel =window.width()
yPixel = window.height()
#Traqueamos los datos
print (f"pixeles:{xPixel,yPixel}")

#Convertimos de pixeles a pulgadas
#Porque? MPL genera figuras en base a pulgadas.
#Recordar que nuestro objetivo es saber la resolucion de nuestra pantalla, para luego hacer la conversion a pulgadas 
# y genera una figura del tamano exacto de nuestra pantalla.
#Asi logramos mantener una escala uniforme con las coordenadas del JASON
xInch = xPixel/dpi
yInch = yPixel/dpi
#Traqueamos los datos
print(f"pulgadas:{xInch,yInch}")

#Carga el Mapa
file = 'Files/gadm41_PAN_1.json'  
panama = gpd.read_file(file)
#Crea la figura y los ejes en funcion del tamano de la pantalla
fig, ax = plt.subplots(figsize=(xInch,yInch))


# Dibuja el mapa sobre los ejes
panama.plot(ax=ax, color='lightblue', edgecolor='black')

#Esconde los ejes
#plt.axis('off')
#Convierte el Mapa a Imagen
plt.savefig('mapaPan.png')
plt.close(fig)



#Crear label con Mapa
labelPan = QLabel(window)
imgPan = QPixmap('mapaPan')
labelPan.setPixmap(imgPan)
#Ajusta el tamano del label al del Mapa
labelPan.adjustSize()


#Obtiene el tamano del label
xLabel = labelPan.width()
yLable = labelPan.height()
#Traqueamos los datos
print(f"Tamano Label{xLabel,yLable}")


#Se verifica el flujo final de la generacion de mapa, para ver si concuerda con la resolucion de la pantalla

#Conversion de cordenadas a pixeles
x,y = ax.transData.transform((-79.5167,8.9833))
#Podemos hacer esto, ya que, como generamos el mapa en funcion de a resolucion de la pantalla
#la conversion va a ser de 1:1

print(f"Pixel en X:{x}----Pixel en Y:{y}")
#Traqueamos los datos
#Lastimosamente
#Existe error de conversion :/, se contrarrestra con una constante(400)

#Trozteza,funciona a medio palo

#Sumar los 4 decimales que le siguen para obtener valor real(mmmh todavia falta revisar)

#Blink timer
blinker = True

def blink():
    global blinker
    if blinker:
        marcador.setStyleSheet()

#creacion de Marcadores
def marcador(long,lat):
        x,y = ax.transData.transform((long,lat))
        marcador = QPushButton("", window)
        marcador.setFixedSize(100,100)
        marcador.move(int(x),int(y-445))
        marcador.setIcon(QIcon("marcador.png"))
        marcador.setIconSize(marcador.size())
        marcador.setStyleSheet("""
        QPushButton {
            background-color: transparent; 
            border: none;
        }
        QPushButton:hover {
            background-color: rgba(100, 100, 255, 0.5); 
        }
        """)
        


marcador.clicked.connect(ventanaEmergente)

window.showFullScreen()

#print(panama.total_bounds)

tourPan.exec_()


