
import usuarios
import basedatos
from datetime import date 
from datetime import datetime


class Vendedor:
    
    def __init__(self, nom_usuario):
   
        self.nom_usuario = nom_usuario

    def proximasAcciones(self):

        vendedor = self.nom_usuario

        print('Vendedor:', vendedor.upper() )


        print('\n1.- Consultar Producto')
        print('2.- Registrar Venta')
        print('3.- Cerrar Sesion')
        menuUsuario = input('\nOpcion: ')

        if menuUsuario == '1':

            self.consultarProducto()
        
        elif menuUsuario == '2':

            self.registrarVenta()
        
        elif menuUsuario == '3':

            self.cerrarSesion()
        
        else:

            print('Opcion no Valida')

        
            

    def consultarProducto(self):  

        print('Consulta de Productos')
        nombre_producto = input('\nIngrese el nombre del Producto que desea: \n').lower()

        bd = basedatos.BaseNona()
        curs = bd.connection.cursor()

        queryProducto = "SELECT id__producto, stock, precio , descripcion from producto where nombre = '{}'".format(nombre_producto)

        curs.execute(queryProducto)
        queryResultado = curs.fetchone()

        
        if(queryResultado):

            id_producto = queryResultado[0]
            stock = queryResultado[1]
            precio = queryResultado[2]
            descripcion = queryResultado[3]

            print("\nId Producto: {} \nStock: {} \nPrecio: {} \nDescripcion: {}".format(id_producto, stock, precio, descripcion))

            cantidad_producto = int(input('\nIngrese la cantidad que desea agregar a la venta: \n'))

            if(cantidad_producto >= 1):
                print('Producto agregado')
            else:
                pass

        else:

            print('Producto sin Stock')




    def registrarVenta(self):  

        bd = basedatos.BaseNona()
        curs = bd.connection.cursor()

        queryEstadoCaja = "SELECT estado from ESTADO_CAJA"

        curs.execute(queryEstadoCaja)
        queryResultado = curs.fetchone()

        fecha = date.today()
        




        if(queryResultado[0] == 0):
            print('caja cerrada')

            return




        print('Carrito de Ventas') 

        

        productos =[]
        totalCarrito = 0
        continuar = 'si'
            
        while continuar != 'no':
            
            tipo_venta = input('Boleta o Factura ?: ').lower()
            nombre_producto = input('\nIngrese el nombre del Producto que desea agregar: \n').lower()
            cantidad = int(input('Ingrese Cantidad del producto:'))

            if(nombre_producto != 'no'):

                bd = basedatos.BaseNona()
                curs = bd.connection.cursor()

                queryProducto = "SELECT id__producto, nombre, sku, stock, precio , descripcion from producto where nombre = '{}'".format(nombre_producto)

                curs.execute(queryProducto)
                queryResultado = curs.fetchone()

                if(queryResultado):
                    print('Existe Producto')

                    

                    #Producto
                    producto = {  

                        "idProducto" : queryResultado[0],
                        "nombre" : queryResultado[1],
                        "sku" : queryResultado[2],
                        "stock" : queryResultado[3],
                        "precio" : queryResultado[4],
                        "descripcion" : queryResultado[5],
                        "cantidad": cantidad,
                        "totalProducto" : queryResultado[4] * cantidad
                        
                    }


                    print("Total de {} : {}".format(producto['nombre'], producto['totalProducto']))


                    #Agregar a lista de productos
                    productos.append(producto)

                    totalCarrito +=  producto['totalProducto']

                    continuar = input('Agregar mas productos?: ')

                else:
                    print('producto no existe')
                    break
            else:
                print('No mas productos')
                break
        else:
            
     
            
            for producto in productos:

                # ------------------------------- Registro Tabla DETALLE_VENTA --------------------------------

                #Genera ID Detalle Venta
                bd = basedatos.BaseNona()
                curs = bd.connection.cursor()
                queryDetalle = 'SELECT max(id_detalle_venta) from detalle_venta'
                curs.execute(queryDetalle)
                total = curs.fetchone()
                id_detalle_venta = total[0]

                if(id_detalle_venta is None):
                    
                    id_detalle_venta = 1
                    
                else:
                    
                    id_detalle_venta += 1
                
                detalleVenta = {

                    'id_detalle_venta' : id_detalle_venta,
                    'cantidad' : producto['cantidad'],
                    'fecha_venta': fecha,
                    'venta_id': 1,
                    'precio_producto': producto['precio'],
                    'tipo_venta': tipo_venta,
                    'id_producto': producto['idProducto'],
                    'total_venta': totalCarrito
                }
                
                #variable para insertar en la bd
                registroDetalleVentas = ( 
                    detalleVenta['id_detalle_venta'],
                    detalleVenta['cantidad'],
                    detalleVenta['fecha_venta'],
                    detalleVenta['venta_id'],
                    detalleVenta['precio_producto'],
                    detalleVenta['tipo_venta'],
                    detalleVenta['id_producto'],
                    detalleVenta['total_venta'],

                )
                queryDetalleVentas ='INSERT INTO detalle_venta (id_detalle_venta, cantidad, fecha_venta, venta_id_venta, precio_producto, tipo_venta, id_producto, total_venta ) VALUES(:1,:2,:3,:4,:5,:6,:7,:8)'
                curs.execute(queryDetalleVentas, registroDetalleVentas)
                bd.connection.commit()


                
            # ------------------------------- Registro Tabla VENTA --------------------------------

            #Genera ID VENTA
            queryIdVenta = 'SELECT max(id_venta) from venta'
            curs.execute(queryIdVenta)
            total = curs.fetchone()
            id_venta = total[0]
            
            if(id_venta is None):
                print('No hay venta registrada')
                id_venta = 1
                
            else:
                print('Hay ventas registradas')
                id_venta += 1

            #Consulta ID USUARIO que realiza la venta
            queryIdUsuario = "SELECT id_usuario from usuario where nombre = '{}'".format(self.nom_usuario)
            curs.execute(queryIdUsuario)
            consultaUsuario = curs.fetchone()
            idUsuario = consultaUsuario[0]

            #ID DETALLE VENTA
            id_detalle_venta = 1 #Revisar inconsistencia

            #Tipo de Venta
            tipo_venta = tipo_venta

            # Id informe ventas
            id_informe_ventas = 1

            #fecha Ventas
            fecha_venta = fecha

            variablesQueryVenta = (id_venta, idUsuario, id_detalle_venta, tipo_venta, id_informe_ventas, fecha_venta )
            queryVenta ='INSERT INTO venta (id_venta, id_usuario, id_detalle_venta, tipo_venta, id_informe_ventas, fecha_venta) VALUES(:1,:2,:3,:4,:5,:6)'
            curs.execute(queryVenta, variablesQueryVenta)
            bd.connection.commit()
              



            print('Venta realizada con exito por', self.nom_usuario)
            print('Total de su compra: ', detalleVenta['total_venta'])
            
            
    




    def cerrarSesion(self):  

        print('Cerrando Sesion') 
       
            

            
                    
        

        

        

        
 
        
            


        



