import acciones


class Admin:

    def __init__(self):
   
        self.nom_usuario = 'Nona'

   
    def proximasAcciones(self):

        usuario = self.nom_usuario

        print('Admin:', usuario.upper() )

        print('\n1.- Registrar Nuevo Usuario')
        print('2.- Salir\n')
        menuPrincipal = input('Ingresa Opcion: ')

        accion = acciones.Acciones()


        if menuPrincipal == '1':
        
            accion.registro()
        else:
            print('Sesion Terminada')

        

        