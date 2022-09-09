class solution: 

    #1. Crear método inicializador de la clase
    def __init__(self):
        #2. Declaración de variables
        self.productos = ['Lacteos', 'Aseo', 'Granos']
        self.productos_lacteos = []
        self.existencia_productos_lacteos = []
        self.productos_aseo = []
        self.existencia_productos_aseo = []
        self.productos_granos = []
        self.existencia_productos_granos = []

    #3. Método que imprime los valores de las variables
    def show_info(self):
        print('Estamos trabajando en Visual studio code')

    def imprimirLacteos(self):
        print(self.productos_lacteos)
        print(self.existencia_productos_lacteos)

    def imprimirGranos(self):
        print(self.productos_granos)
        print(self.existencia_productos_granos)

    def imprimirAseo(self):
        print(self.productos_aseo)
        print(self.existencia_productos_aseo)

    def llenado_productos(self):
        self.productos_lacteos = ['Leche colanta', 'Leche alpina', 'Mantequilla La Fina']
        self.existencia_productos_lacteos = [12, 14, 25]
        self.productos_aseo = ['Trapero', 'escoba', 'Cepillo']
        self.existencia_productos_aseo = [2, 8, 34]
        self.productos_granos = ['arroz', 'Frijol blanco', 'Maiz']
        self.existencia_productos_granos = [19, 7, 15]
        self.imprimirLacteos()

    def imprimir_opciones(self):
        print('1. Lacteos \n2. Granos \n3. Aseo')

    def verificar_numero(self, numero):
        try: 
            numeroC = int(numero)
            return numeroC
        except:
            return False
        
    def eleccionImprimir(self, grupo):
        if grupo == 1:
            self.imprimirLacteos()
        elif grupo == 2:
            self.imprimirGranos()
        elif grupo == 3:
            self.imprimirAseo()

    def verificarExistencia(self, nombre, grupo):
        vector = [] 
        vector = self.definir_vector(vector, grupo)
        i = 0
        existe = False

        while i < int(len(vector)) and existe == False:
            if vector[i] == nombre:
                existe = True
            i = i+1

        return existe
    
    def definir_vector(self, vector, grupo):
        if grupo == 1:
            vector = self.productos_lacteos
        elif grupo == 2:
            vector = self.productos_granos
        elif grupo == 3:
            vector = self.productos_aseo  
        return vector

    def ingresaAGrupo(self, grupo, cantidad, nombre):
        if self.verificarExistencia(nombre, grupo) == False:
            if grupo == 1:
                self.productos_lacteos.append(nombre)
                self.existencia_productos_lacteos.append(cantidad)      
            elif grupo == 2:
                self.productos_granos.append(nombre)
                self.existencia_productos_granos.append(cantidad)
            elif grupo == 3:
                self.productos_aseo.append(nombre)
                self.existencia_productos_aseo.append(cantidad)
        else: 
            print('El producto ya existe. Se agregan los que acabas de ingresar a la cantidad en stoke')
            self.sumarProductos(cantidad, nombre, grupo)

    def sumarProductos(self, cantidad, nombre, grupo):
        i = 0
        if grupo == 1:
            i = self.productos_lacteos.index(nombre)
            cantidad1 = self.existencia_productos_lacteos[i] + cantidad 
            self.existencia_productos_lacteos.pop(i)
            self.existencia_productos_lacteos.insert(i, cantidad1)
        elif grupo == 2:
            i = self.productos_granos.index(nombre)
            cantidad1 = self.existencia_productos_granos[i] + cantidad
            self.existencia_productos_granos.pop(i)
            self.existencia_productos_granos.insert(i, cantidad1)
        elif grupo == 3:
            i = self.productos_aseo.index(nombre)
            cantidad1 = self.existencia_productos_aseo[i] + cantidad
            self.existencia_productos_aseo.pop(i)
            self.existencia_productos_aseo.insert(i, cantidad1)

    def Ingresa_informacion_productos(self, cantidad):
        if cantidad == 0:
            print('¿En qué grupo desea agregar el producto? \nRecuerda escribir el numero correpondiente a la opcion')
            self.imprimir_opciones() 
       
        nGrupo = input('')
        grupo = self.verificar_numero(nGrupo)

        if(type(grupo) == int):
            if(grupo >= 1 and grupo <= 3):
                self.eleccionImprimir(grupo)
                nombre = input('Ingresa nombre del producto: ')
                nuevos = input('Ingresa la cantidad de productos: ')
                cantidad = self.verificar_numero(nuevos)
                self.ingresaAGrupo(grupo, cantidad, nombre)
                self.eleccionImprimir(grupo)
            else:
                print('Intenta de nuevo')
                self.Ingresa_informacion_productos(1)
        else: 
            print('intenta de nuevo')
            self.Ingresa_informacion_productos(1)



    