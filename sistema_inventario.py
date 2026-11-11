class Producto:
    def __init__(self, nombre: str, precio: float, cantidad: int):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad    
    #Devuelve el nombre formateado como un string.
    @property
    def nombre(self) -> str:
        return self._nombre 
    
    #Definimos el 'setter' para la validación
    @nombre.setter
    def nombre(self, valor: str):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El nombre del producto no puede estar vacío y debe ser un texto ")
        self._nombre = valor.strip()

    
    # Devuelve el nombre formateado como un flotante.
    @property
    def precio(self) -> float:
        return self._precio
    
     # Definimos el 'setter' para la validación
    @precio.setter
    def precio(self, valor: float):
        try:
            val = float(valor)
        except (ValueError, TypeError):
            raise TypeError("El precio debe ser númerico")
        
        if val < 0:
            raise ValueError("El precio debe ser mayor o igual a 0.")
        self._precio = val
    # Devuelve el nombre formateado como un entero.
    @property
    def cantidad(self) -> int:
        return self._cantidad
    # Definimos el 'setter' para la validación
    @cantidad.setter
    def cantidad(self, valor: int):
        try:
            val = int(valor)
        except (ValueError, TypeError):
            raise TypeError("La cantidad debe ser númerica.")
        
        if val < 0:
            raise ValueError("El precio debe ser mayor o igual a 0.")
        self._cantidad = val

    
    # Modifica el precio 
    def actualizar_precio(self, precio_modificado: float):        
        self.precio = precio_modificado
    # Modifica la cantidad 
    def actualizar_cantidad(self, cantidad_modificada: int):
        self.cantidad = cantidad_modificada
    # Modifica el valor total del producto
    def calcular_valor_total(self) -> float:
        return self.precio * self.cantidad
    # formatea la salida de acuerdo al tipo de dato
    def __str__(self) -> str:
        return f"Producto: {self.nombre}  \nPrecio: ${self.precio:,.2f}  \nCantidad: {self.cantidad}  \nValor Total: ${self.calcular_valor_total():,.2f}"


class Inventario:

    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto: Producto):
        # Verificar si ya existe un producto con el mismo nombre
        if self.buscar_producto(producto.nombre) is not None:
            raise ValueError(f"Ya existe un producto registrado con el nombre '{producto.nombre}'.")
        self.productos.append(producto) # agrega el producto
    # Funcionalidad de buscar producto
    def buscar_producto(self, nombre: str) -> Producto | None:
        if not isinstance(nombre, str):
            return None
        nombre_busqueda = nombre.strip().lower()
        for prod in self.productos:
            if prod.nombre.lower() == nombre_busqueda:
                return prod
        return None
    # Calcula el valor total de los produtos
    def calcular_valor_inventario(self) -> float:
        return sum(prod.calcular_valor_total() for prod in self.productos)

    def listar_productos(self):
        if not self.productos:
            print("\nNo existen productos")
            return
        

        print("\nPRODUCTOS EN EL INVENTARIO:\n")
        for i, prod in enumerate(self.productos, 1):
            print(f"{i}. {prod}")


def menu_principal():
    inventario = Inventario()

    while True:
        print("\n MENU DE INVENTARIO ")
        print("\n SELECCIONA UNA OPCIÓN ")
        print("1. Agregar producto")
        print("2. Buscar producto")
        print("3. Listar productos")
        print("4. Calcular valor total del inventario")
        print("5. Salir")
        
        opcion = input("Seleccione una opción (1-5): ").strip()
        match opcion:
            case "1": # nuevo Producto
                try:
                    print("\nRegistro de un nuevo producto\n")
                    nombre = input("Ingresa el nombre: ")
                    precio = input("Ingresa el precio unitario: ")
                    cantidad = input("Ingresa la cantidad en stock: ")

                    # Creación del producto (las propiedades validarán los tipos y rangos)
                    nuevo_prod = Producto(nombre, precio, cantidad)
                    inventario.agregar_producto(nuevo_prod)
                    print(f"\nProducto '{nuevo_prod.nombre}' agregado correctamente.")
                
                except (ValueError, TypeError) as e:
                    print(f"\nError de validación: {e}")
                except Exception as e:
                    print(f"\nError: {e}")
            case "2": # Buscar Producto
                try:
                    print("\nBusqueda de productos")
                    nombre_busqueda = input("Ingrese el nombre del producto: ")
                    producto_encontrado = inventario.buscar_producto(nombre_busqueda)

                    if producto_encontrado:
                        print(f"\nProducto encontrado: \n{producto_encontrado}")
                    else:
                        print(f"\nNo se encontró ningún producto: '{nombre_busqueda}'.")
                
                except Exception as e:
                    print(f"\nError: {e}")

            case "3": # Listar producto
                try:
                    inventario.listar_productos()
                except Exception as e:
                    print(f"\nError: {e}")

            case "4": # Valor total del inventario
                try:
                    total_inventario = inventario.calcular_valor_inventario()
                    print(f"\nValor de todos los productos del inventario: ${total_inventario:,.2f}")
                except Exception as e:
                    print(f"\nError: {e}")

            case "5":
                print("\nGracias por utilizar el sistema de inventario.")
                break
            case _:
                print("\nOpción inválida: Por favor, ingrese un número entre 1 y 5.")


if __name__ == "__main__":
    menu_principal()