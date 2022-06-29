
import usuarios


class Jefe:

    def __init__(self, nom_usuario):
   
        self.nom_usuario = nom_usuario

   
    def proximasAcciones(self):

        jefe = self.nom_usuario

        print('Jefe de Ventas:', jefe.upper() )

        print('\n1.- Informe Diario de ventas')
        print('2.- Actualizacion de Catalogo de Productos')
        print('3.- Apertura de Caja')
        print('4.- Cierre de Caja')
        print('5.- Cerrar Sesion')
    
        menuUsuario = input('\nOpcion: ')


       
            
        
            
        


        


