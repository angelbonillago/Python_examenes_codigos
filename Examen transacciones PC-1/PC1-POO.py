class Cliente:
    def __init__(self, nombreCliente,edad,direccion,tipoCuenta):
        self.nombreCliente = nombreCliente 
        self.edad=edad
        self.direccion=direccion
        self.tipoCuenta=tipoCuenta

    def muestraInformacion(self):
        print("Cliente: ",self.nombreCliente,"\nEdad : ",self.edad,"\nDireccion: ",self.direccion,"\nTipo deCuenta :",self.tipoCuenta,"\n")
    def getNombreCliente(self):
        return self.nombreCliente
    def getEdad(self):
        return self.edad
    def getDireccion(self):
        return self.direccion
    def gettipoCuenta(self):
        return self.tipoCuenta  

class Cuentas(Cliente):
#depósitos, extracciones y transferencias de dinero. 
    def __init__(self,nombreCliente,edad,direccion,tipoCuenta,numeroCuenta,saldo,interes,mantenimiento,operacion,cantidad):
        super().__init__(nombreCliente,edad,direccion,tipoCuenta)
        self.numeroCuenta = numeroCuenta
        self.saldo = saldo
        self.interes = interes
        self.mantenimiento=mantenimiento
        self.operacion=operacion
        self.cantidad=cantidad   


    def muestraInformacion(self):
        print("\nCliente: ",self.nombreCliente,"\nEdad : ",self.edad,"\nDireccion: ",self.direccion,"\nTipo deCuenta :",self.tipoCuenta,"\nNumero de cuenta: ",self.numeroCuenta,"\nSaldo: ",self.saldo,"\nInteres: ",self.interes,"\nMantenimiento: ",self.mantenimiento,"\nOperacion: ",self.operacion,"\nCantidad: ",self.cantidad)

    def operacionFinanciera(self,oper,cant,cuentaDestino):
        pass  

    
class CuentaAhorro(Cuentas):
    """docstring for CuentaAhorro."""
    def __init__(self,nombreCliente,edad,direccion,tipoCuenta,numeroCuenta,saldo,interes,mantenimiento,operacion,cantidad,disposicion):
        super().__init__(nombreCliente,edad,direccion,tipoCuenta,numeroCuenta,saldo,interes,mantenimiento,operacion,cantidad)
        self.disposicion = disposicion

    def operacionFinanciera(self,oper,cant,cuentaDestino):
        if(oper=="RETIRO"):
            total=self.saldo
            self.operacion=oper
            self.cantidad=cant
            if(total>=cant):
            #retiro
            
                aux= total -cant
                self.saldo=aux    
                self.muestraInformacion()        
            else:
                self.muestraInformacion()  
                print("No tienes saldo suficiente!")
        elif(oper=="TRANSACCION"):
            total=self.saldo
            self.operacion=oper
            self.cantidad=cant             
            if(total>=cant):

            #transaccion
                aux= total -cant
                self.saldo=aux    
                self.muestraInformacion()
                print("Se a transferido S/",cant," a la cuenta : ",cuentaDestino)        
            else:
                self.muestraInformacion()  
                print("No tienes saldo suficiente!") 
        else:
            #deposito
            if(cant>=5):
                self.operacion=oper
                self.cantidad=cant                
                aux = cant
                tot = self.saldo +aux
                self.saldo = tot
                self.muestraInformacion()
            else:
                print("Se realizan depositos a partir de S/5")

    def muestraInformacion(self):
        print("\nCliente: ",self.nombreCliente,"\nTipo deCuenta :",self.tipoCuenta,"\nNumero de cuenta: ",self.numeroCuenta,"\nSaldo: ",self.saldo,"\nInteres: ",self.interes,"\nMantenimiento: ",self.mantenimiento,"\nOperacion: ",self.operacion,"\nCantidad: ",self.cantidad,"\nDisposicion: ",self.disposicion)


class CuentasSueldo(Cuentas):
    """docstring for CuentasSueldo."""
    def __init__(self,nombreCliente,edad,direccion,tipoCuenta,numeroCuenta,saldo,interes,mantenimiento,operacion,cantidad,bonificacion):
        super().__init__(nombreCliente,edad,direccion,tipoCuenta,numeroCuenta,saldo,interes,mantenimiento,operacion,cantidad)
        self.bonificacion = bonificacion

    def muestraInformacion(self):
        print("\nCliente: ",self.nombreCliente,"\nTipo deCuenta :",self.tipoCuenta,"\nNumero de cuenta: ",self.numeroCuenta,"\nSaldo: ",self.saldo,"\nInteres: ",self.interes,"\nMantenimiento: ",self.mantenimiento,"\nOperacion: ",self.operacion,"\nCantidad: ",self.cantidad)

    def operacionFinanciera(self,oper,cant,cuentaDestino):
        if(oper=="RETIRO"):
            self.operacion=oper
            self.cantidad=cant
            total=self.saldo
            if(total>=cant):
                #retiro
                
                aux= total -cant
                self.saldo=aux    
                self.muestraInformacion()        
            else:
                self.muestraInformacion()  
                print("No tienes saldo suficiente!") 
        elif(oper=="DEPOSITO"):
            self.operacion=oper
            self.cantidad=cant            
            if(cant>=100):

                aux = cant
                tot = self.saldo +aux
                self.saldo = tot
                self.muestraInformacion()
            else:
                print("Se realizan depositos a partir de S/100")            
        else:
            print("Operacion no encontrada")

class DepositoPlazo(Cliente):

    def __init__(self,nombreCliente,edad,direccion,tipoCuenta,fechaVencimiento,cancelaciónAnticipada,interes,cantidad):
        super().__init__(nombreCliente,edad,direccion,tipoCuenta)
        self.fechaVencimiento=fechaVencimiento
        self.cancelaciónAnticipada=cancelaciónAnticipada     
        self.interes=interes
        self.cantidad=cantidad

    def importeInteres(self):
        intereses=(self.cantidad*(self.interes/100))
        return intereses

    def muestraInformacion(self):
        print("\nCliente: ",self.nombreCliente,"\nTipo deCuenta :",self.tipoCuenta,"\nInteres :",self.interes,"\nTotal Interes: ",self.importeInteres())
  

# nombreCliente,numeroCuenta,saldo,interes,mantenimiento,operacion,dispossicion
#dispossicion='a largo plazo'
if __name__ == '__main__':


    cliente1=Cliente('Angel Bonilla', 30, 'Las Musas', 'CUENTA DE AHORROS')
    cliente2=Cliente('Pedro Rodriguez', 35, 'Las vegas', 'CUENTA DE SUELDO')

    cliente1.muestraInformacion()
    cliente2.muestraInformacion()
    
    #Operaciones

    oper=CuentaAhorro(cliente1.getNombreCliente(), cliente1.getEdad(), cliente1.getDireccion(), cliente1.gettipoCuenta(), '35051512460021', 150, 0.01, 5, "-", 0, "A LARGO PLAZO")
    oper.operacionFinanciera("RETIRO", 151,"")
    oper.operacionFinanciera("TRANSACCION", 15,"12112122000")
    oper.operacionFinanciera("RETIRO", 20,"")

    oper2=CuentasSueldo(cliente2.getNombreCliente(), cliente2.getEdad(), cliente2.getDireccion(), cliente2.gettipoCuenta(), '35051512460010', 1200, 0.05, 0, "-", 0, 50)
    oper2.operacionFinanciera("DEPOSITO",200,"")
    oper2.operacionFinanciera("TRANSACCION", 150,"12112122000")
    oper2.operacionFinanciera("RETIRO", 120,"")


    #Deposito a plazo

    depoPlazoCliente1= DepositoPlazo(cliente1.getNombreCliente(), cliente1.getEdad(), cliente1.getDireccion(), cliente1.gettipoCuenta(), "31/12/21", "NO", 0.03, 5000)
    depoPlazoCliente1.importeInteres()
    depoPlazoCliente1.muestraInformacion()


    