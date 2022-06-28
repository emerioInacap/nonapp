import getpass
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
            print('Ingresar con Perfil de Nona para agregar usuarios')
        else:
            self.registro()


    def login(self):

        print("\nIniciar Sesion\n")

        
        nom_usuario = input('Ingresa tu usuario: ')
        password = getpass.getpass('Ingresa tu password: ')

        bd = basedatos.BaseNona()

        curs = bd.connection.cursor()
    
        queryValidacion = "SELECT id_usuario, nombre, ap_paterno, ap_materno, rut, fecha_nac, telefono, email, sexo, password, id_cargo from usuario where nombre = '{}' and password = '{}'".format(nom_usuario, password)
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

        print('\nRegistro de Usuario')

        
        id_usuario = input('Ingresa id usuario: ')
        nombre = input('Ingresa tu nombre: ')
        ap_paterno = input('Ingresa tu apellido paterno: ')
        ap_materno = input('Ingresa tu apellido Materno: ')
        rut = input('Ingresa rut: ')
        fecha_nac = input('Ingresa tu fecha de nacimiento dd-mm-aaaa : ')
        telefono = input('Ingresa tu telefono ')
        email = input('Ingresa tu email: ')
        
        sexo = input("Ingresa tu sexo ('M' o 'F'): ")
        password = getpass.getpass('Ingresa tu password: ')

        id_cargo = input('Ingresa id cargo: ')

        
        #instancia Usuario
        usuario = usuarios.Usuario(id_usuario, nombre, ap_paterno, ap_materno, rut, fecha_nac, telefono, email, sexo, password, id_cargo )
        usuario.insertar()
        print('Usuario Creado')  
        



