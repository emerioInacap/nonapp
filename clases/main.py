import acciones 


    
#------------------MENU PRINCIPAL ------------------ 


print('\n------NONAPP------\n')
print('1.- Iniciar Sesion')
print('2.- Registrar')
print('3.- Salir\n')
menuPrincipal = input('Ingresa Opcion: ')

accion = acciones.Acciones()


if menuPrincipal == '1':
  
    accion.login()
  
elif menuPrincipal == '2':

    accion.inicio()

elif menuPrincipal == '3':

    pass


    


 














