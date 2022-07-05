import acciones


class Admin:

    def __init__(self):
   
        self.nom_usuario = 'Nona'

   
    def proximasAcciones(self):

        usuario = self.nom_usuario

        print('Admin:', usuario.upper() )

        print('\n-----MENU REGISTRO DE USUARIOS ------')
        print('\n1.- Registrar Nuevo Usuario')
        print('\n-----MENU JEFE VENTAS ------')
        print('\n2.- Actualizacion de Catalogo de Productos')
        print('3.- Apertura de Caja')
        print('4.- Cierre de Caja')
        print('\n-----MENU VENDEDOR ------')
        print('\n5.- Consultar Producto')
        print('6.- Registrar Venta')
        print('7.- Salir\n')
        menuPrincipal = input('Ingresa Opcion: ')

        accion = acciones.Acciones()


        if menuPrincipal == '1':
        
            accion.registro()
        else:
            print('Sesion Terminada')

        

        