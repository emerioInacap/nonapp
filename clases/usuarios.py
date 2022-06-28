
import basedatos
import hashlib
import vendedores
import jefeVentas
import acciones

class Usuario:
    # constructor
    def __init__(self,id_usuario, nom_usuario, ap_paterno, ap_materno, rut, fecha_nac, telefono, email, sexo, password, id_cargo ):
   
       
        self.id_usuario = id_usuario
        self.nom_usuario = nom_usuario
        self.ap_paterno = ap_paterno
        self.ap_materno = ap_materno
        self.rut = rut
        self.fecha_nac = fecha_nac
        self.telefono = telefono
        self.email = email
        self.sexo = sexo
        self.password = password
        self.id_cargo = id_cargo
       

    def insertar(self):

        

        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        registro = (self.id_usuario, self.nom_usuario, self.ap_paterno, self.ap_materno, self.rut, self.fecha_nac, self.telefono, self.email, self.sexo, cifrado.hexdigest(), self.id_cargo )
        bd = basedatos.BaseNona()
        consulta ='INSERT INTO usuario (id_usuario, nombre, ap_paterno, ap_materno, rut, fecha_nac, telefono, email, sexo, password, id_cargo  ) VALUES(:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11)'
        curs = bd.connection.cursor()
        curs.execute(consulta, registro)
        bd.connection.commit()   
        
    



    #validacion
    def validacion(self):
        nom_usuario = self.nom_usuario
        password = self.password

        bd = basedatos.BaseNona()

        curs = bd.connection.cursor()
        curs.arraysize=50
    
        queryValidacion = "SELECT nombre, password, id_cargo from usuario where nombre = '{}' and password = '{}'".format(nom_usuario, password)
        curs.execute(queryValidacion)
        queryResultado = curs.fetchone()
        

        if queryResultado:
            #self.acceso = True
            print('\nValidacion Correcta\n')
            print('Bienvenid@', nom_usuario)

            if queryResultado[2] == 1:
                print('Privilegios de Admin')
                
                print('1.- Registrar Nuevo Usuario')
                print('2.- Salir\n')
                menuPrincipal = input('Ingresa Opcion: ')

                accion = acciones.Acciones()


                if menuPrincipal == '1':
                
                    accion.registro()
                else:
                    print('Sesion Terminada')

                           









        
        



        

