
import usuarios
import basedatos
from datetime import date
from datetime import datetime


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

        if menuUsuario == '1':

            self.informeVentasDiario()
        
        elif menuUsuario == '2':

            self.actualizarCatalogo()
        
        elif menuUsuario == '3':

            self.aperturaCaja()

        elif menuUsuario == '4':

            self.cierreCaja()

        elif menuUsuario == '5':

            self.cerrarSesion()
        
        else:

            print('Opcion no Valida')



    def informeVentasDiario(self): 
        print('Informe de Ventas Diario')
        fecha = date.today()

        bd = basedatos.BaseNona()
        curs = bd.connection.cursor()
        
        queryBoleta = "select count(tipo_venta) from venta where tipo_venta='boleta' and fecha_venta = TO_DATE('{}','YY-MM-DD')".format(fecha)
        queryFactura = "select count(tipo_venta) from venta where tipo_venta='factura' and fecha_venta = TO_DATE('{}','YY-MM-DD')".format(fecha)

        curs.execute(queryBoleta)
        consultaBoleta = curs.fetchone()

        curs.execute(queryFactura)
        consultaFactura = curs.fetchone()
        
        print('\nVenta con Boleta: {} | Venta con Factura: {}'.format(consultaBoleta[0], consultaFactura[0]))



        """   
        print('\nFactura:')
        print('\nMartes 19 de Abril 2022')
        print('Hora: 12:55')
        print('Id: 00001')
        print('Factura: 111111')
        print('Monto: $30.000')
        print('Producto: Lapiz, Cantidad: 30')
        print('Vendedor: Emerio Suarez')
        """




    def actualizarCatalogo(self): 
        print('Actualizar Catologo')

        nombre_producto = input('\nIngrese el nombre del Producto que desea actualizar: \n').lower()

        bd = basedatos.BaseNona()
        curs = bd.connection.cursor()

        queryProducto = "SELECT id__producto, nombre, stock, precio , descripcion from producto where nombre = '{}'".format(nombre_producto)

        curs.execute(queryProducto)
        queryResultado = curs.fetchone()

        if(queryResultado):

            id_producto = queryResultado[0]
            nombre = queryResultado[1]
            stock = queryResultado[2]
            precio = queryResultado[3]
            descripcion = queryResultado[4]

            print("\nId Producto: {} \nNombre: {} \nStock: {} \nPrecio: {} \nDescripcion: {}".format(id_producto,nombre, stock, precio, descripcion))

            nombre_producto_actualizado = input('\nIngrese nuevo nombre: \n')
            stock_producto_actualizado = int(input('\nIngrese nuevo stock: \n'))
            precio_producto_actualizado = int(input('\nIngrese nuevo precio: \n'))
            descripcion_producto_actualizado = input('\nIngrese nueva descripcion: \n')

            queryProductoActualizado = "UPDATE producto SET nombre = '{}', stock = '{}' , precio = '{}' , descripcion = '{}' WHERE id__producto = '{}'".format(nombre_producto_actualizado,stock_producto_actualizado,precio_producto_actualizado,descripcion_producto_actualizado, id_producto )
            

            curs.execute(queryProductoActualizado)
            bd.connection.commit()
            print('Producto Actualizado correctamente')

            
        else:

            print('No existe producto')


    def aperturaCaja(self): 
        print('Apertura Caja')
        bd = basedatos.BaseNona()
        curs = bd.connection.cursor()
        queryCajaActualizado = "UPDATE estado_caja SET estado = 1"
        curs.execute(queryCajaActualizado)
        bd.connection.commit()
        print('Caja Abierta')




    def cierreCaja(self): 
        print('Cierre Caja')
        bd = basedatos.BaseNona()
        curs = bd.connection.cursor()
        queryCajaActualizado = "UPDATE estado_caja SET estado = 0"
        curs.execute(queryCajaActualizado)
        bd.connection.commit()
        print('Caja Cerrada')


    def cerrarSesion(self): 
        pass


       
            
        
            
        


        


