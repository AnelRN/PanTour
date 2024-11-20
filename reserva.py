from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 20, 311, 461))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.email = QtWidgets.QLabel(self.groupBox)
        self.email.setGeometry(QtCore.QRect(10, 100, 55, 16))
        self.email.setObjectName("email")
        self.confirmacion = QtWidgets.QLabel(self.groupBox)
        self.confirmacion.setGeometry(QtCore.QRect(10, 150, 301, 51))
        self.confirmacion.setObjectName("confirmacion")
        self.nombre = QtWidgets.QLabel(self.groupBox)
        self.nombre.setGeometry(QtCore.QRect(10, 50, 55, 16))
        self.nombre.setObjectName("nombre")
        self.edad = QtWidgets.QLabel(self.groupBox)
        self.edad.setGeometry(QtCore.QRect(150, 50, 61, 16))
        self.edad.setObjectName("edad")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 10, 201, 31))
        self.label.setObjectName("label")
        self.pais = QtWidgets.QLabel(self.groupBox)
        self.pais.setGeometry(QtCore.QRect(10, 210, 81, 16))
        self.pais.setObjectName("pais")
        self.intronom = QtWidgets.QLineEdit(self.groupBox)
        self.intronom.setGeometry(QtCore.QRect(10, 70, 113, 22))
        self.intronom.setText("")
        self.intronom.setObjectName("intronom")
        self.introedad = QtWidgets.QLineEdit(self.groupBox)
        self.introedad.setGeometry(QtCore.QRect(150, 70, 113, 22))
        self.introedad.setText("")
        self.introedad.setObjectName("introedad")
        self.intromail = QtWidgets.QLineEdit(self.groupBox)
        self.intromail.setGeometry(QtCore.QRect(10, 120, 113, 22))
        self.intromail.setObjectName("intromail")
        self.cantidaddepersonas = QtWidgets.QLabel(self.groupBox)
        self.cantidaddepersonas.setGeometry(QtCore.QRect(150, 100, 151, 16))
        self.cantidaddepersonas.setObjectName("cantidaddepersonas")
        self.intropais = QtWidgets.QLineEdit(self.groupBox)
        self.intropais.setGeometry(QtCore.QRect(10, 230, 113, 22))
        self.intropais.setObjectName("intropais")
        self.cedula = QtWidgets.QLabel(self.groupBox)
        self.cedula.setGeometry(QtCore.QRect(150, 210, 55, 16))
        self.cedula.setObjectName("cedula")
        self.numtelefono = QtWidgets.QLabel(self.groupBox)
        self.numtelefono.setGeometry(QtCore.QRect(10, 270, 141, 21))
        self.numtelefono.setObjectName("numtelefono")
        self.introcedula = QtWidgets.QLineEdit(self.groupBox)
        self.introcedula.setGeometry(QtCore.QRect(150, 230, 113, 22))
        self.introcedula.setText("")
        self.introcedula.setObjectName("introcedula")
        self.intrnumtelefono = QtWidgets.QLineEdit(self.groupBox)
        self.intrnumtelefono.setGeometry(QtCore.QRect(70, 290, 113, 22))
        self.intrnumtelefono.setObjectName("intrnumtelefono")
        self.cantperso = QtWidgets.QSpinBox(self.groupBox)
        self.cantperso.setGeometry(QtCore.QRect(150, 120, 42, 22))
        self.cantperso.setObjectName("cantperso")
        self.prefijostelefonicos = QtWidgets.QComboBox(self.groupBox)
        self.prefijostelefonicos.setGeometry(QtCore.QRect(10, 290, 51, 22))
        self.prefijostelefonicos.setCurrentText("507")
        self.prefijostelefonicos.setObjectName("prefijostelefonicos")
        self.prefijostelefonicos.addItem("")
        self.prefijostelefonicos.addItem("")
        self.prefijostelefonicos.addItem("")
        self.prefijostelefonicos.addItem("")
        self.prefijostelefonicos.addItem("")
        self.prefijostelefonicos.addItem("")
        self.prefijostelefonicos.addItem("")
        self.prefijostelefonicos.addItem("")
        self.prefijostelefonicos.addItem("")
        self.prefijostelefonicos.addItem("")
        self.prefijostelefonicos.addItem("")
        self.prefijostelefonicos.addItem("")
        self.prefijostelefonicos.addItem("")
        self.prefijostelefonicos.addItem("")
        self.prefijostelefonicos.addItem("")
        self.prefijostelefonicos.addItem("")
        self.prefijostelefonicos.addItem("")
        self.prefijostelefonicos.addItem("")
        self.prefijostelefonicos.addItem("")
        self.prefijostelefonicos.addItem("")
        self.prefijostelefonicos.addItem("")
        self.prefijostelefonicos.addItem("")
        self.prefijostelefonicos.addItem("")
        self.prefijostelefonicos.addItem("")
        self.prefijostelefonicos.addItem("")
        self.prefijostelefonicos.addItem("")
        self.prefijostelefonicos.addItem("")
        self.prefijostelefonicos.addItem("")
        self.prefijostelefonicos.addItem("")
        self.line = QtWidgets.QFrame(self.groupBox)
        self.line.setGeometry(QtCore.QRect(10, 330, 291, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.deseaabonar = QtWidgets.QLabel(self.groupBox)
        self.deseaabonar.setGeometry(QtCore.QRect(110, 340, 91, 16))
        self.deseaabonar.setObjectName("deseaabonar")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 370, 95, 20))
        self.radioButton.setObjectName("radioButton")
        self.btnabonar = QtWidgets.QPushButton(self.groupBox)
        self.btnabonar.setGeometry(QtCore.QRect(20, 400, 93, 28))
        self.btnabonar.setObjectName("btnabonar")
        self.sexo = QtWidgets.QLabel(self.groupBox)
        self.sexo.setGeometry(QtCore.QRect(200, 270, 55, 16))
        self.sexo.setObjectName("sexo")
        self.escsexo = QtWidgets.QComboBox(self.groupBox)
        self.escsexo.setGeometry(QtCore.QRect(200, 290, 73, 22))
        self.escsexo.setObjectName("escsexo")
        self.escsexo.addItem("")
        self.escsexo.addItem("")
        self.introduzcanom = QtWidgets.QLabel(self.groupBox)
        self.introduzcanom.setGeometry(QtCore.QRect(10, 90, 200, 16))
        self.introduzcanom.setText("")
        self.introduzcanom.setObjectName("introduzcanom")
        self.introduzcaedad = QtWidgets.QLabel(self.groupBox)
        self.introduzcaedad.setGeometry(QtCore.QRect(150, 90, 200, 16))
        self.introduzcaedad.setText("")
        self.introduzcaedad.setObjectName("introduzcaedad")
        self.introduzcaEmail = QtWidgets.QLabel(self.groupBox)
        self.introduzcaEmail.setGeometry(QtCore.QRect(10, 140, 200, 16))
        self.introduzcaEmail.setText("")
        self.introduzcaEmail.setObjectName("introduzcaEmail")
        self.introduzcacantperson = QtWidgets.QLabel(self.groupBox)
        self.introduzcacantperson.setGeometry(QtCore.QRect(150, 140, 200, 16))
        self.introduzcacantperson.setText("")
        self.introduzcacantperson.setObjectName("introduzcacantperson")
        self.introduzcapais = QtWidgets.QLabel(self.groupBox)
        self.introduzcapais.setGeometry(QtCore.QRect(10, 250, 200, 16))
        self.introduzcapais.setText("")
        self.introduzcapais.setObjectName("introduzcapais")
        self.introduzcacedula = QtWidgets.QLabel(self.groupBox)
        self.introduzcacedula.setGeometry(QtCore.QRect(150, 250, 200, 16))
        self.introduzcacedula.setText("")
        self.introduzcacedula.setObjectName("introduzcacedula")
        self.introduzcatelefono = QtWidgets.QLabel(self.groupBox)
        self.introduzcatelefono.setGeometry(QtCore.QRect(70, 310, 200, 16))
        self.introduzcatelefono.setText("")
        self.introduzcatelefono.setObjectName("introduzcatelefono")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(370, 20, 371, 131))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.lugar = QtWidgets.QLabel(self.groupBox_2)
        self.lugar.setGeometry(QtCore.QRect(10, 20, 55, 16))
        self.lugar.setObjectName("lugar")
        self.precio = QtWidgets.QLabel(self.groupBox_2)
        self.precio.setGeometry(QtCore.QRect(10, 60, 55, 16))
        self.precio.setObjectName("precio")
        self.descuento = QtWidgets.QLabel(self.groupBox_2)
        self.descuento.setGeometry(QtCore.QRect(10, 80, 71, 21))
        self.descuento.setObjectName("descuento")
        self.subtotal = QtWidgets.QLabel(self.groupBox_2)
        self.subtotal.setGeometry(QtCore.QRect(10, 110, 55, 16))
        self.subtotal.setObjectName("subtotal")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(370, 160, 371, 321))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.datosreserva = QtWidgets.QLabel(self.groupBox_3)
        self.datosreserva.setGeometry(QtCore.QRect(10, 0, 201, 31))
        self.datosreserva.setObjectName("datosreserva")
        self.nomfac = QtWidgets.QLabel(self.groupBox_3)
        self.nomfac.setGeometry(QtCore.QRect(10, 50, 200, 16))
        self.nomfac.setObjectName("nomfac")
        self.paisfac = QtWidgets.QLabel(self.groupBox_3)
        self.paisfac.setGeometry(QtCore.QRect(190, 50, 200, 16))
        self.paisfac.setObjectName("paisfac")
        self.mailfac = QtWidgets.QLabel(self.groupBox_3)
        self.mailfac.setGeometry(QtCore.QRect(190, 80, 200, 16))
        self.mailfac.setObjectName("mailfac")
        self.cantpersonfac = QtWidgets.QLabel(self.groupBox_3)
        self.cantpersonfac.setGeometry(QtCore.QRect(190, 110, 200, 16))
        self.cantpersonfac.setObjectName("cantpersonfac")
        self.cedulafac = QtWidgets.QLabel(self.groupBox_3)
        self.cedulafac.setGeometry(10, 80, 200, 16)  
        self.cedulafac.setObjectName("cedulafac")
        self.telefonofac = QtWidgets.QLabel(self.groupBox_3)
        self.telefonofac.setGeometry(10, 110, 200, 16)
        self.telefonofac.setObjectName("telefonofac") 
        self.sexofac = QtWidgets.QLabel(self.groupBox_3)
        self.sexofac.setGeometry(QtCore.QRect(10, 140, 200, 16))
        self.sexofac.setObjectName("sexofac")
        self.edadfac = QtWidgets.QLabel(self.groupBox_3)
        self.edadfac.setGeometry(QtCore.QRect(10, 170, 200, 16))
        self.edadfac.setObjectName("edadfac")
        self.abono = QtWidgets.QLabel(self.groupBox_3)
        self.abono.setGeometry(QtCore.QRect(10, 220, 200, 20))
        self.abono.setObjectName("abono")
        self.totaladeudado = QtWidgets.QLabel(self.groupBox_3)
        self.totaladeudado.setGeometry(QtCore.QRect(10, 260, 200, 16))
        self.totaladeudado.setObjectName("totaladeudado")
        self.line_2 = QtWidgets.QFrame(self.groupBox_3)
        self.line_2.setGeometry(QtCore.QRect(10, 190, 351, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.btnreservar = QtWidgets.QPushButton(self.centralwidget)
        self.btnreservar.setGeometry(QtCore.QRect(650, 520, 93, 28))
        self.btnreservar.setObjectName("btnreservar")
        self.btnregresar = QtWidgets.QPushButton(self.centralwidget)
        self.btnregresar.setGeometry(QtCore.QRect(30, 520, 93, 28))
        self.btnregresar.setObjectName("btnregresar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 788, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.btnabonar.clicked.connect(self.check_radio)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def check_radio(self):
        try:
            if self.radioButton.isChecked():
                print('Usted ha realizado el abono')
            else:
                print('No seleccionó la opción abonar')
        except Exception as e:
            print(f"Error en check_radio: {e}")




    def guardar_datos(self):
    # Obtener los datos de los campos
        nombre = self.intronom.text()  # Usamos .text() para obtener el valor del campo
        cedula = self.introcedula.text()  # Lo mismo aquí
        telefono = self.intrnumtelefono.text()  
        sexo = self.escsexo.currentText()  # Usamos currentText() para obtener el valor seleccionado
        edad = self.introedad.text()
        pais = self.intropais.text()
        Email = self.intromail.text()
        CantidadPersonas = self.cantperso.value()  # Para QSpinBox usamos .value() en lugar de .text()

    # Validación de los campos
        error = False

    # Validación de los campos
        if len(nombre) == 0:
            self.introduzcanom.setText("*Ingrese su nombre*")
            self.introduzcanom.setStyleSheet("color: red")
            error = True
        if len(cedula) == 0:
            self.introduzcacedula.setText("*Ingrese su cédula*")
            self.introduzcacedula.setStyleSheet("color: red")
            error = True
        if len(telefono) == 0:
            self.introduzcatelefono.setText("*Ingrese su teléfono*")
            self.introduzcatelefono.setStyleSheet("color: red")
            error = True
        if len(edad) == 0:
            self.introduzcaedad.setText("*Ingrese su edad*")
            self.introduzcaedad.setStyleSheet("color: red")
            error = True
        if len(pais) == 0:
            self.introduzcapais.setText("*Ingrese su país*")
            self.introduzcapais.setStyleSheet("color: red")
            error = True
        if len(Email) == 0:
            self.introduzcaEmail.setText("*Ingrese su email*")
            self.introduzcaEmail.setStyleSheet("color: red")
            error = True
        if CantidadPersonas == 0:
            self.introduzcacantperson.setText("*Ingrese personas*")
            self.introduzcacantperson.setStyleSheet("color: red")
            
            error = True

        if error:
            print("Hay campos que no se han llenado correctamente.")
        else:
        # Aquí puedes guardar los datos o realizar otras acciones
            print("Datos guardados correctamente")



        nomfac = f"\nNombre: {nombre}"
        cedufac= f"\nCédula: {cedula}"
        telefac= f"\nTeléfono: {telefono}"
        sexfac= f"\nsexo: {sexo}"
        edadfac= f"\nedad: {edad}"
        paisfac= f"\npais: {pais}"
        mailfac=f"\nEmail: {Email}"
        cantpersonfac=f"\ncantperson: {CantidadPersonas}"

        self.nomfac.setText(f"Nombre: {nombre}")
        self.cedulafac.setText(f"Cédula: {cedula}")
        self.telefonofac.setText(f"Teléfono: {telefono}")
        self.sexofac.setText(f"Sexo: {sexo}")
        self.edadfac.setText(f"Edad: {edad}")
        self.paisfac.setText(f"País: {pais}")
        self.mailfac.setText(f"E-mail: {Email}")
        self.cantpersonfac.setText(f"Cantidad de personas: {CantidadPersonas}")

    # Limpiar los campos si es necesario
        self.intronom.setText("")
        self.introcedula.setText("")
        self.intrnumtelefono.setText("")
        self.introedad.setText("")
        self.intropais.setText("")
        self.intromail.setText("")
    
   
    # Conectar los eventos a las funciones al configurar la interfaz
        self.intronom.textChanged.connect(self.validar_nombre)
        self.introcedula.textChanged.connect(self.validar_cedula)
        self.intrnumtelefono.textChanged.connect(self.validar_telefono)
        self.introedad.textChanged.connect(self.validar_edad)
        self.intromail.textChanged.connect(self.validar_email)
        self.intropais.textChanged.connect(self.validar_pais)
        self.cantperso.valueChanged.connect(self.validar_cantidad_personas)

# Crear las funciones de validación para cada campo
    def validar_nombre(self):
        try:
            nombre = self.intronom.text()
            if len(nombre) > 0:  # Si el campo no está vacío
                self.introduzcanom.setText("")
                self.introduzcanom.setStyleSheet("")
            else:
                self.introduzcanom.setText("*Ingrese su nombre*")
                self.introduzcanom.setStyleSheet("color: red")
        except Exception as e:
            print(f"Error en validar_nombre: {e}")

    def validar_cedula(self):
        try:
            cedula = self.introcedula.text()
            if len(cedula) > 0:  # Si el campo no está vacío
                self.introduzcacedula.setText("")
                self.introduzcacedula.setStyleSheet("")
            else:
                self.introduzcacedula.setText("*Ingrese su cédula*")
                self.introduzcacedula.setStyleSheet("color: red")
        except Exception as e:
            print(f"Error en validar_cedula: {e}")

    def validar_telefono(self):
        try:
            telefono = self.intrnumtelefono.text()
            if len(telefono) > 0:  # Si el campo no está vacío
                self.introduzcatelefono.setText("")
                self.introduzcatelefono.setStyleSheet("")
            else:
                self.introduzcatelefono.setText("*Ingrese su teléfono*")
                self.introduzcatelefono.setStyleSheet("color: red")
        except Exception as e:
            print(f"Error en validar_telefono: {e}")

    def validar_edad(self):
        try:
            edad = self.introedad.text()
            if len(edad) > 0:  # Si el campo no está vacío
                self.introduzcaedad.setText("")
                self.introduzcaedad.setStyleSheet("")
            else:
                self.introduzcaedad.setText("*Ingrese su edad*")
                self.introduzcaedad.setStyleSheet("color: red")
        except Exception as e:
            print(f"Error en validar_edad: {e}")

    def validar_email(self):
        try:
            email = self.intromail.text()
            if len(email) > 0:  # Si el campo no está vacío
                self.introduzcaEmail.setText("")
                self.introduzcaEmail.setStyleSheet("")
            else:
                self.introduzcaEmail.setText("*Ingrese su email*")
                self.introduzcaEmail.setStyleSheet("color: red")
        except Exception as e:
            print(f"Error en validar_email: {e}")

    def validar_pais(self):
        try:
            pais = self.intropais.text()
            if len(pais) > 0:  # Si el campo no está vacío
                self.introduzcapais.setText("")
                self.introduzcapais.setStyleSheet("")
            else:
                self.introduzcapais.setText("*Ingrese su país*")
                self.introduzcapais.setStyleSheet("color: red")
        except Exception as e:
            print(f"Error en validar_pais: {e}")

    def validar_cantidad_personas(self):
        try:
            if self.cantperso.value() > 0:  # Si la cantidad es válida
                self.introduzcacantperson.setText("")
                self.introduzcacantperson.setStyleSheet("")
            else:
                self.introduzcacantperson.setText("*Ingrese una cantidad válida*")
                self.introduzcacantperson.setStyleSheet("color: red")
        except Exception as e:
            print(f"Error en validar_cantidad_personas: {e}")

        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.email.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">E-mail</span><span style=\" color:#ff0000;\">*</span></p></body></html>"))
        self.confirmacion.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#aaaaaa;\">El e-mail de confirmación </span></p><p><span style=\" color:#aaaaaa;\">se enviará aesta dirección</span></p></body></html>"))
        self.nombre.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Nombre</span><span style=\" font-weight:600; color:#ff0000;\">*</span></p></body></html>"))
        self.edad.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Edad</span><span style=\" font-weight:600; color:#ff0000;\">*</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">introduce tus datos</span></p></body></html>"))
        self.pais.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">País/región</span><span style=\" font-weight:600; color:#ff0000;\">*</span></p></body></html>"))
        self.cantidaddepersonas.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#000000;\">cantidad de personas</span><span style=\" color:#ff0000;\">*</span></p></body></html>"))
        self.cedula.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">cedula</span><span style=\" font-weight:600; color:#ff0000;\">*</span></p></body></html>"))
        self.numtelefono.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">numero de telefono</span><span style=\" font-weight:600; color:#ff0000;\">*</span></p></body></html>"))
        self.prefijostelefonicos.setItemText(0, _translate("MainWindow", "500"))
        self.prefijostelefonicos.setItemText(1, _translate("MainWindow", "501"))
        self.prefijostelefonicos.setItemText(2, _translate("MainWindow", "502"))
        self.prefijostelefonicos.setItemText(3, _translate("MainWindow", "503"))
        self.prefijostelefonicos.setItemText(4, _translate("MainWindow", "504"))
        self.prefijostelefonicos.setItemText(5, _translate("MainWindow", "505"))
        self.prefijostelefonicos.setItemText(6, _translate("MainWindow", "506"))
        self.prefijostelefonicos.setItemText(7, _translate("MainWindow", "507"))
        self.prefijostelefonicos.setItemText(8, _translate("MainWindow", "508"))
        self.prefijostelefonicos.setItemText(9, _translate("MainWindow", "509"))
        self.prefijostelefonicos.setItemText(10, _translate("MainWindow", "51"))
        self.prefijostelefonicos.setItemText(11, _translate("MainWindow", "52"))
        self.prefijostelefonicos.setItemText(12, _translate("MainWindow", "53"))
        self.prefijostelefonicos.setItemText(13, _translate("MainWindow", "54"))
        self.prefijostelefonicos.setItemText(14, _translate("MainWindow", "55"))
        self.prefijostelefonicos.setItemText(15, _translate("MainWindow", "56"))
        self.prefijostelefonicos.setItemText(16, _translate("MainWindow", "57"))
        self.prefijostelefonicos.setItemText(17, _translate("MainWindow", "58"))
        self.prefijostelefonicos.setItemText(18, _translate("MainWindow", "590"))
        self.prefijostelefonicos.setItemText(19, _translate("MainWindow", "591"))
        self.prefijostelefonicos.setItemText(20, _translate("MainWindow", "592"))
        self.prefijostelefonicos.setItemText(21, _translate("MainWindow", "593"))
        self.prefijostelefonicos.setItemText(22, _translate("MainWindow", "594"))
        self.prefijostelefonicos.setItemText(23, _translate("MainWindow", "595"))
        self.prefijostelefonicos.setItemText(24, _translate("MainWindow", "596"))
        self.prefijostelefonicos.setItemText(25, _translate("MainWindow", "598"))
        self.prefijostelefonicos.setItemText(26, _translate("MainWindow", "809"))
        self.prefijostelefonicos.setItemText(27, _translate("MainWindow", "829"))
        self.prefijostelefonicos.setItemText(28, _translate("MainWindow", "849"))
        self.deseaabonar.setText(_translate("MainWindow", "desea abonar?"))
        self.radioButton.setText(_translate("MainWindow", "si"))
        self.btnabonar.setText(_translate("MainWindow", "abonar"))
        self.sexo.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#000000;\">sexo</span><span style=\" font-weight:600; color:#ff0000;\">*</span></p></body></html>"))
        self.escsexo.setItemText(0, _translate("MainWindow", "M"))
        self.escsexo.setItemText(1, _translate("MainWindow", "F"))
        self.lugar.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">lugar:</span></p></body></html>"))
        self.precio.setText(_translate("MainWindow", "precio:"))
        self.descuento.setText(_translate("MainWindow", "descuento:"))
        self.subtotal.setText(_translate("MainWindow", "sub total:"))
        self.datosreserva.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">datos de reserva</span></p></body></html>"))
        self.cedulafac.setText(_translate("MainWindow", "Cédula:"))
        self.nomfac.setText(_translate("MainWindow", "Nombre:"))
        self.sexofac.setText(_translate("MainWindow", "Sexo:"))
        self.telefonofac.setText(_translate("MainWindow", "Teléfono:"))
        self.edadfac.setText(_translate("MainWindow", "Edad:"))
        self.paisfac.setText(_translate("MainWindow", "País:"))
        self.abono.setText(_translate("MainWindow", "Abono:"))
        self.mailfac.setText(_translate("MainWindow", "E-mail:"))
        self.cantpersonfac.setText(_translate("MainWindow", "Cantidad de Personas:"))
        self.totaladeudado.setText(_translate("MainWindow", "Total adeudado:"))
        self.btnreservar.setText(_translate("MainWindow", "reservar"))
        self.btnregresar.setText(_translate("MainWindow", "regresar"))
        self.btnreservar.clicked.connect(self.guardar_datos)


