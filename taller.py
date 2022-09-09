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
                print('El nombre del producto es: '+nombre, ' y la cantidad a ingresar es ', cantidad)
            else:
                print('Intenta de nuevo')
                self.Ingresa_informacion_productos(1)
        else: 
            print('intenta de nuevo')
            self.Ingresa_informacion_productos(1)


    


    