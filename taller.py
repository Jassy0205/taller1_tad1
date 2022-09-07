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

    def llenado_productos(self):
        self.productos_lacteos = ['Leche colanta', 'Leche alpina', 'Mantequilla La Fina']
        self.existencia_productos_lacteos = [12, 14, 25]
        self.productos_aseo = ['Trapero', 'escoba', 'Cepillo']
        self.existencia_productos_aseo = [2, 8, 34]
        self.productos_granos = ['arroz', 'Frijol blanco', 'Maiz']
        self.existencia_productos_granos = [19, 7, 15]
        imprimirLacteos()
        
    def imprimirLacteos(self):
        print(self.productos_lacteos)
        print(self.existencia_productos_lacteos)

    def imprimirGranos(self):
        print(self.productos_granos)
        print(self.existencia_productos_granos)

    def imprimirAseo(self):
        print(self.productos_aseo)
        print(self.existencia_productos_aseo)

    


    