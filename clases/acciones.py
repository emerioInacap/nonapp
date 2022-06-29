import getpass
from types import NoneType
import hashlib
import usuarios
import basedatos




class Acciones:

    def inicio(self):
        bd = basedatos.BaseNona()

        curs = bd.connection.cursor()
    
        queryInicio = "SELECT * FROM USUARIO"
        curs.execute(queryInicio)
        queryResultado = curs.fetchall()

        if queryResultado:

            print('\n------NONAPP------\n')
            print('1.- Iniciar Sesion')
            print('2.- Salir\n')
            menuPrincipal = input('Ingresa Opcion: ')




            if menuPrincipal == '1':
            
                self.login()
            
            elif menuPrincipal == '2':

                pass
            
        else:

            print('\n------Bienvenid@ a NONAPP------')
            print('\nVamos a Registrar al Usuario Administrador\n')
            self.registro()


    def login(self):

        print("\nIniciar Sesion\n")

        
        nom_usuario = input('Ingresa tu usuario: ')
        password = getpass.getpass('Ingresa tu password: ')

        bd = basedatos.BaseNona()

        curs = bd.connection.cursor()

        cifrado = hashlib.sha256()
        cifrado.update(password.encode('utf8'))
    
        queryValidacion = "SELECT id_usuario, nombre, ap_paterno, ap_materno, rut, fecha_nac, telefono, email, sexo, password, id_cargo from usuario where nombre = '{}' and password = '{}'".format(nom_usuario, cifrado.hexdigest())

        curs.execute(queryValidacion)
        queryResultado = curs.fetchone()
         

        if(queryResultado):
            

            id_usuario = queryResultado[0]
            nom_usuario = queryResultado[1]
            ap_paterno = queryResultado[2]
            ap_materno = queryResultado[3]
            rut = queryResultado[4]
            fecha_nac = queryResultado[5]
            telefono = queryResultado[6]
            email = queryResultado[7]
            sexo = queryResultado[8]
            password = queryResultado[9]
            id_cargo = queryResultado[10]

            usuario = usuarios.Usuario(id_usuario, nom_usuario, ap_paterno, ap_materno, rut, fecha_nac, telefono, email, sexo, password, id_cargo)
            usuario.validacion()

        else:
            print('error')

      

        
            

        


    def registro(self):

        #Genera ID Usuario
        
        usuario = usuarios.Usuario('','','','','','','','','','','')
        usuariosTabla = usuario.consultar()  #cantidad de usuarios que hay en la tabla

        if(type(usuariosTabla) == NoneType ):
            id_usuario = 1
        else:
            id_usuario = usuariosTabla + 1 #Para generar el id dinamicamente del nuevo usuario
        
        

        print('\nRegistro de Usuario')

      
        nombre = input('Ingresar nombre: ')
        ap_paterno = input('Ingresar apellido paterno: ')
        ap_materno = input('Ingresar apellido Materno: ')
        rut = input('Ingresar rut: ')
        fecha_nac = input('Ingresar fecha de nacimiento dd-mm-aa : ')
        telefono = input('Ingresar telefono: ')
        email = input('Ingresar email: ')
        
        sexo = input("Ingresar sexo ('M' o 'F'): ")
        password = getpass.getpass('Ingresar password: ')

        nombre_cargo = input('Ingresar nombre del cargo: ')

        if(nombre_cargo).lower() == 'admin':
            id_cargo = 1

        elif(nombre_cargo).lower() == 'jefe':
         
            id_cargo = 2
        elif(nombre_cargo).lower() == 'vendedor':
        
            id_cargo = 3
        else:
            print('Error')


        
        #instancia Usuario
        usuario = usuarios.Usuario(id_usuario, nombre, ap_paterno, ap_materno, rut, fecha_nac, telefono, email, sexo, password, id_cargo )
        usuario.insertar()
        print('Usuario Creado')  
        



