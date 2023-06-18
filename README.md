# Proyecto Lenguajes Formales y de Programación

El proyecto consiste en desarrollar un programa en Python que permita trabajar con gramáticas regulares, autómatas finitos deterministas (AFD) y autómatas finitos no deterministas (AFN). El objetivo es proporcionar una herramienta visual que facilite la definición de gramáticas, la generación de AFD y AFN, y la evaluación de cadenas válidas para las gramáticas definidas. Para lograr esto, se utilizarán paradigmas de programación.

El programa se implementará utilizando la librería Tkinter para crear una interfaz gráfica. Se crearán diferentes ventanas a las que el usuario podrá acceder según las acciones que desee realizar. Además, se incluirá una sección de reportes que mostrará todos los detalles de las gramáticas generadas. Para una mejor comprensión de lo realizado, el programa también será capaz de generar grafos utilizando la herramienta Graphviz.

Una gramática regular es útil para validar cadenas y se puede convertir en un AFD o un AFN. Estos procesos se explicarán con más detalle posteriormente.

Las gramáticas podrán crearse directamente desde la aplicación o cargarse desde un archivo de texto con extensión .afn y .afd. Se proporcionará información detallada sobre la estructura del archivo en la sección de carga masiva. No será necesario utilizar un analizador para leer el archivo, ya que se asume que vendrá sin errores de sintaxis y con un patrón definido.

Es importante tener en cuenta que se realizará una revisión del código para verificar los paradigmas utilizados, los cuales deberán ser explicados para comprobar la autoría de la aplicación.

El programa permitirá iniciar tanto con la creación de una gramática para generar su respectivo AFD/AFN, como con la creación de un AFD/AFN para generar su gramática correspondiente. Se proporcionará la notación necesaria para AFD/AFN, asegurándose de incluir todos los elementos requeridos para generar los reportes.


# Manual Tecnico

## Main.py
![Main.py](https://i.ibb.co/Y8twhHC/image.png)

  

Este código utiliza el módulo tkinter para crear una interfaz gráfica de usuario (GUI) en Python. La función iniciar_programa se define para iniciar la ejecución del programa. Luego, se crea una instancia de la clase MenuPrincipal y se asigna a la variable menu_principal. La clase MenuPrincipal debe ser definida en otro archivo llamado MenuPrincipal.py en la carpeta Interfaz. Finalmente, se llama al método mainloop() en la instancia de MenuPrincipal para iniciar el bucle principal de la interfaz gráfica y permitir que la ventana y los elementos de la GUI respondan a las interacciones del usuario.

  

La línea if __name__ == '__main__': asegura que el código dentro de ese bloque solo se ejecutará si el script se está ejecutando directamente como un programa principal y no como un módulo importado. Esto permite que el archivo pueda ser tanto un script independiente como un módulo reutilizable.

## Configuraciones de Interfaz Generales
![MenuPrincipal.py](https://i.ibb.co/25JQyKm/image.png)
  



define el constructor `__init__()` de una clase. El constructor es llamado cuando se crea una instancia de la clase y se utiliza para realizar configuraciones iniciales. A continuación, se detallan las acciones realizadas en el constructor:

-  `super().__init__()`: Llama al constructor de la clase padre para realizar las configuraciones iniciales necesarias.
    
-  Se definen dos funciones internas: `on_enter(event)` y `on_leave(event)`. Estas funciones se utilizan para manejar eventos de entrada (`on_enter`) y salida (`on_leave`) del ratón en los widgets de la interfaz gráfica. Estos eventos cambian los colores de fondo (`bg`) y de primer plano (`fg`) de los widgets.
    
- Se realiza la configuración de la ventana principal de la interfaz gráfica:
    
    -   `self.geometry("1115x600")` establece las dimensiones de la ventana principal en 1115 píxeles de ancho por 600 píxeles de alto.
    -   `self.configure(bg="#FFFFFF")` establece el color de fondo de la ventana principal en blanco.
    -   `self.title("Menú Principal")` establece el título de la ventana principal como "Menú Principal".
    -   `self.resizable(False, False)` desactiva la capacidad de redimensionar la ventana en ambos ejes.
4.  Se realiza un cálculo para centrar la ventana en la pantalla:
    
    -   `screen_width = self.winfo_screenwidth()` obtiene el ancho de la pantalla.
    -   `screen_height = self.winfo_screenheight()` obtiene la altura de la pantalla.
    -   Se calculan las coordenadas `x` e `y` para posicionar la ventana en el centro de la pantalla.
    -   `self.geometry("%dx%d+%d+%d" % (1115, 600, x, y))` establece la geometría de la ventana con las dimensiones y posiciones calculadas.
-  `self.overrideredirect(True)` desactiva la barra de título y la decoración de la ventana, lo que significa que no se muestra la barra de título ni los botones de minimizar, maximizar y cerrar.
    
- `self.wm_attributes("-topmost", 1)` fuerza que la ventana tkinter esté siempre en la parte superior de todas las demás ventanas.

### Estructuras de botones:
![Button MenuPrincipal.py](https://i.ibb.co/ykp9gNR/image.png)

-   `self`: El primer argumento pasado al constructor del botón indica que el botón se creará como un widget hijo de `self`, que se asume que es una instancia de una clase que hereda de `tkinter` (como una ventana principal).
    
-   `bg="lightgray"`: Establece el color de fondo del botón en "lightgray" (gris claro).
    
-   `borderwidth=0`: Configura el ancho del borde del botón en 0, lo que significa que no se mostrará ningún borde.
    
-   `highlightthickness=0`: Establece el grosor del resaltado del botón en 0, lo que significa que no se mostrará ningún resaltado cuando el botón esté enfocado.
    
-   `relief="flat"`: Configura el estilo de relieve del botón en "flat" (sin relieve), lo que implica que el botón se mostrará como una superficie plana sin efectos de relieve.
    
-   `font=("Helvetica", 16)`: Establece la fuente del texto del botón como "Helvetica" con un tamaño de 16 puntos.
    
-   `text="Módulo AFN"`: Especifica el texto que se mostrará en el botón, que en este caso es "Módulo AFN".
    
-   `command=lambda: Interfaz.ModuloAFN.moduloAFN()`: Define la función que se ejecutará cuando se haga clic en el botón. En este caso, se utiliza una función anónima (`lambda`) para llamar al método `moduloAFN()` del módulo `Interfaz.ModuloAFN`. Esto implica que debe existir un archivo llamado `ModuloAFN.py` en la carpeta `Interfaz` que contenga la implementación del método `moduloAFN()`.


### Estructura de Etiquetas:
![Etiquetas](https://i.ibb.co/QpFKDVg/image.png)

-   `self`: El primer argumento pasado al constructor de la etiqueta indica que la etiqueta se creará como un widget hijo de `self`, que se asume que es una instancia de una clase que hereda de `tkinter` (como una ventana principal).
    
-   `text="Luis Andres Cobar Sandoval 202010097"`: Especifica el texto que se mostrará en la etiqueta. En este caso, el texto es "Luis Andres Cobar Sandoval 202010097".
    
-   `bg="#FFFFFF"`: Establece el color de fondo de la etiqueta en "#FFFFFF" (blanco).
    
-   `fg="#8B8B8B"`: Configura el color de primer plano (color del texto) de la etiqueta en "#8B8B8B" (gris claro).
    
-   `font=("Happy Monkey", 10)`: Establece la fuente del texto de la etiqueta como "Happy Monkey" con un tamaño de 10 puntos.
### Estructura de Inputs:

![enter image description here](https://i.ibb.co/Fz6X0gV/image.png)

-   `self`: El primer argumento pasado al constructor de la entrada indica que la entrada se creará como un widget hijo de `self`, que se asume que es una instancia de una clase que hereda de `tkinter` (como una ventana principal).
    
-   `bd=0`: Configura el ancho del borde de la entrada en 0, lo que significa que no se mostrará ningún borde alrededor de la entrada de texto.
    
-   `bg="#D9D9D9"`: Establece el color de fondo de la entrada en "#D9D9D9" (gris claro).
    
-   `fg="#000716"`: Configura el color de primer plano (color del texto) de la entrada en "#000716" (azul oscuro).
    
-   `highlightthickness=0`: Establece el grosor del resaltado de la entrada en 0, lo que significa que no se mostrará ningún resaltado cuando la entrada esté enfocada.

# Clases

## AFD.py
![AFD](https://i.ibb.co/7rppchy/image.png)

Se define una clase llamada `AFD` que representa un Autómata Finito Determinista. A continuación, se detallan las funcionalidades de la clase:

-   El método `__init__` es el constructor de la clase. Toma varios parámetros, incluyendo el nombre del autómata, el alfabeto, los estados, el estado inicial, los estados de aceptación y las transiciones. Estos parámetros se asignan a los atributos correspondientes de la instancia de la clase.
    
-   El método `__str__` devuelve una representación en formato de cadena del autómata. Construye una cadena que muestra el nombre del autómata, los estados, el alfabeto, el estado inicial, los estados de aceptación y las transiciones. Los elementos de cada sección se formatean en cadenas separadas por comas y saltos de línea.

Los elementos de la clase AFD son:
- Nombre
- Alfabeto
- Estados
- Estado Inicial
- Estados de Aceptación
- Transiciones (En Formato de Diccionario)
- TransicionesN (Transiciones en forma de Array)

### Metodos Relacionados con los AFN:
#### Generador de Cadenas
![GenerarCadena](https://i.ibb.co/XVT0Mq1/image.png)
-   Se inicializa la variable `estado_actual` con el estado inicial del AFD y la variable `cadena` como una cadena vacía.
    
-   Se inicia un bucle infinito.
    
-   Se obtienen las transiciones disponibles desde el estado actual del AFD utilizando el método `get` sobre el atributo `transiciones` del AFD. Si no hay transiciones disponibles desde el estado actual, se muestra un mensaje de error y se interrumpe el bucle.
    
-   Se elige aleatoriamente una transición de la lista de transiciones disponibles utilizando la función `random.choice`. La transición seleccionada es un par clave-valor que representa la entrada y el estado de destino.
    
-   Se agrega la entrada seleccionada a la cadena generada hasta ahora.
    
-   El estado actual se actualiza al estado de destino obtenido de la transición seleccionada.
    
-   Si el estado actual está en la lista de estados de aceptación del AFD, se retorna la cadena generada como una cadena de ejemplo válida.
    
-   Si no se puede generar una cadena de ejemplo (porque no se llega a un estado de aceptación), se muestra un mensaje de error y se retorna `None`.
#### Validaciones Generales:
![Verificaciones](https://i.ibb.co/3fXdS75/image.png)
-  La función `verificar_alfabeto` toma como entrada una lista `alfabeto` y verifica si contiene símbolos repetidos. Utiliza un enfoque basado en conjuntos para eliminar duplicados y luego compara la longitud de la lista original con la longitud del conjunto resultante. Si son diferentes, significa que había símbolos repetidos en el alfabeto. En ese caso, se muestra un mensaje de error y la función retorna `False`. Si no hay símbolos repetidos, retorna `True`.
    
-  La función `verificar_estado_inicial` toma como entrada un `estado_inicial` y una lista `estados`. Verifica si el estado inicial está presente en la lista de estados. Si el estado inicial no se encuentra en la lista de estados, se muestra un mensaje de error y la función retorna `False`. En caso contrario, retorna `True`.
    
- La función `estados_aceptacion` toma como entrada una lista `estados_aceptacion` y una lista `estados`. Verifica si todos los estados de aceptación están presentes en la lista de estados. Recorre cada estado de aceptación y, si encuentra algún estado que no está en la lista de estados, muestra un mensaje de error y la función retorna `False`. Si todos los estados de aceptación están en la lista de estados, retorna `True`.
#### Validaciones de las Transiciones:
![Verificador de Transiciones](https://i.ibb.co/n3tM0HX/image.png)
-   Se itera sobre cada `transicion` en la lista de transiciones proporcionada.
    
-   Se divide la transición en elementos individuales utilizando el carácter de coma como separador. Si la longitud de los elementos no es igual a 3, se muestra un mensaje de error indicando que las transiciones deben tener 3 elementos y se retorna `False`.
    
-   Se asignan los elementos divididos (`origen`, `entrada`, `destino`) a variables separadas.
    
-   Se verifica si el estado de origen y el estado de destino están presentes en la lista de estados. Si alguno de ellos no está en la lista, se muestra un mensaje de error y se retorna `False`.
    
-   Se verifica si el símbolo de entrada está presente en el alfabeto. Si no está en el alfabeto, se muestra un mensaje de error y se retorna `False`.
    
-   Si todas las transiciones pasan las validaciones anteriores, se retorna `True`.

#### Comprobador de Cadenas (Thompson)

![Comprobador de Cadenas](https://i.ibb.co/wgyG5r2/image.png)

-   Se inicializa la variable `estado_actual` con el estado inicial del AFD.
    
-   Se itera sobre cada `caracter` en la cadena dada.
    
-   Se verifica si el `caracter` está presente en el alfabeto del AFD. Si no está en el alfabeto, se muestra un mensaje de error indicando que el carácter no está en el alfabeto del AFD y se retorna `False`.
    
-   Se verifica si el `estado_actual` está presente en las transiciones del AFD y si el `caracter` está presente en las transiciones del `estado_actual`. Si alguna de las condiciones no se cumple, se muestra un mensaje de error indicando que no hay una transición definida para el estado y el carácter dados, y se retorna `False`.
    
-   Se actualiza el `estado_actual` utilizando la transición correspondiente al estado actual y el carácter actual.
    
-   Después de recorrer toda la cadena, se verifica si el `estado_actual` está en la lista de estados de aceptación del AFD. Si es así, se retorna un mensaje indicando que la cadena es válida en el AFD. En caso contrario, se retorna un mensaje indicando que la cadena no es válida en el AFD.

### Creacion de AFD:
![CrearAFD](https://i.ibb.co/DQnbKdF/image.png)

-   Se elimina el último elemento de la lista `transiciones` utilizando `del transiciones[-1]`.
    
-   Se muestra por pantalla los valores de los parámetros para verificar que se hayan pasado correctamente.
    
-   Se realizan varias comprobaciones para asegurarse de que no hay campos vacíos y que los valores sean válidos:
    
    -   Se verifica si el símbolo "ε" está presente en el alfabeto. Si es así, se muestra un mensaje de error indicando que el símbolo ε no es válido y se retorna `False`.
        
    -   Se verifica si alguno de los parámetros (`nombre`, `estados`, `alfabeto`, `estado_inicial`, `estados_aceptacion`) está vacío. Si alguno de ellos está vacío, se muestra un mensaje de error indicando que se deben completar todos los campos y se retorna.
        
-   Si todas las comprobaciones anteriores son exitosas, se realizan más validaciones utilizando funciones de la clase `AFD`:
    
    -   Se verifica si el estado inicial está en la lista de estados.
        
    -   Se verifica si los estados de aceptación están en la lista de estados.
        
    -   Se verifica si las transiciones son válidas (estados de origen y destino, símbolos de entrada).
        
    -   Se verifica si el alfabeto no contiene símbolos repetidos.
        
    -   Si todas las validaciones son exitosas, se crea el AFD utilizando la función `Crear_AFD` de la clase `AFD` y se muestra un mensaje de éxito.
        
-   Finalmente, la función retorna `True` si se ha creado exitosamente el AFD, y no retorna nada (o retorna `False`) en caso contrario.
 
## AFD.py
![AFD.py](https://i.ibb.co/XCMNHkj/image.png)

Se define una clase llamada `AFN` que representa un Autómata Finito No Determinista. A continuación, se detallan las funcionalidades de la clase:

-   El método `__init__` es el constructor de la clase. Toma varios parámetros, incluyendo el nombre del autómata, el alfabeto, los estados, el estado inicial, los estados de aceptación y las transiciones. Estos parámetros se asignan a los atributos correspondientes de la instancia de la clase.
    
-   El método `__str__` devuelve una representación en formato de cadena del autómata. Construye una cadena que muestra el nombre del autómata, los estados, el alfabeto, el estado inicial, los estados de aceptación y las transiciones. Los elementos de cada sección se formatean en cadenas separadas por comas y saltos de línea.

Los elementos de la clase AFN son:
- Nombre
- Alfabeto
- Estados
- Estado Inicial
- Estados de Aceptación
- Transiciones (En Formato de Diccionario)
- TransicionesN (Transiciones en forma de Array)

### Los Metodos Utilizados en AFN.py Tienen la misma Estructura de AFD.py

## Crear AFN:

![CrearAfn](https://i.ibb.co/cxD6p0c/image.png)

-   Se elimina el último elemento de la lista `transiciones` utilizando `del transiciones[-1]`.
    
-   Se muestra por pantalla los valores de los parámetros para verificar que se hayan pasado correctamente.
    
-   Se realizan varias comprobaciones para asegurarse de que no hay campos vacíos y que los valores sean válidos:
    
    -   Se verifica si el símbolo "ε" está presente en el alfabeto. Si es así, se detiene el bucle y no se realiza ninguna acción adicional.
        
    -   Si el símbolo "ε" no está presente en el alfabeto, se agrega al final de la lista `alfabeto` utilizando `alfabeto.append("ε")`.
        
-   Se muestra por pantalla el contenido actualizado de `alfabeto`.
    
-   Se realiza una comprobación adicional para verificar si algún parámetro (`nombre`, `estados`, `alfabeto`, `estado_inicial`, `estados_aceptacion`) está vacío. Si alguno de ellos está vacío, se muestra un mensaje de error indicando que se deben completar todos los campos y se retorna.
    
-   Si todas las comprobaciones anteriores son exitosas, se realizan más validaciones utilizando funciones de la clase `AFN`:
    
    -   Se verifica si el estado inicial está en la lista de estados.
        
    -   Se verifica si los estados de aceptación están en la lista de estados.
        
    -   Se verifica si las transiciones son válidas (estados de origen y destino, símbolos de entrada).
        
    -   Se verifica si el alfabeto no contiene símbolos repetidos.
        
    -   Si todas las validaciones son exitosas, se crea el AFN utilizando la función `Crear_AFN` de la clase `AFN` y se muestra un mensaje de éxito.
        
-   Finalmente, la función retorna `True` si se ha creado exitosamente el AFN, y no retorna nada (o retorna `False`) en caso contrario.
## Generador de Reporte

![Generador de PDF](https://i.ibb.co/2hBbZj5/image.png)
-  La función `generarDOT` se encarga de generar un archivo en formato DOT que representa visualmente el AFD. Utiliza la librería `graphviz` para crear el grafo y define los diferentes elementos del Automata, como los estados, los estados de aceptación y las transiciones. El archivo DOT generado se guarda con el nombre proporcionado.
    
-  La función `generarPDF` se encarga de generar un archivo PDF que contiene un reporte detallado sobre el AFD. Utiliza la librería `reportlab` para crear el archivo PDF y agrega información como el nombre del Automata, los estados, el estado inicial, los estados de aceptación y las transiciones. Además, incluye una imagen del AFD generada previamente con la función `generarDOT`. El archivo PDF se guarda con el nombre "ReporteAFD_" seguido del nombre del AFD.
    
-  La función `generarReporteAFD` es la función principal que se encarga de llamar a las funciones `generarDOT` y `generarPDF` para generar tanto el archivo DOT como el archivo PDF del reporte. Recibe los parámetros necesarios para generar el reporte, como los estados, los estados de aceptación, las transiciones, el estado inicial, el nombre del Automata y el propio objeto del Automata. Una vez generados los archivos, retorna `True` para indicar que el reporte se generó correctamente.
   

# Manual De Usuario
## Menu Princiapl
![Interfaz](https://i.ibb.co/zbGLMqk/image.png)

El Menu principal aparecera con un listado de Botones en la parte de la izquierda de la ventana, en la cual da las siguientes opciones:



## - Modulo AFN

![Interfaz](https://i.ibb.co/4f6kZwz/image.png)


En el cual de la misma manera que en el menu principal se desplieguan botones en la parte de la izquierda con las siguientes opciones:

## - Agregar AFN
![Interfaz](https://i.ibb.co/GpKH4jG/image.png)

En el modulo de Agregar AFN nos pide registrar la informacion del AFN a registrar, y en la parte inferior izquierda el boton para agregar el AFN o para regresar al Menu

## Generar Cadenas
![Interfaz](https://i.ibb.co/SXFKcnC/image.png)

En el Modulo de Generar Cadenas podemos Generar Cadenas de Ruta Automaticamente y comprobar el AFN,

así como tambien hay un segundo boton y un input en la parte inferior izquierda en la cual se tiene que ingresar una ruta para probarla en afn Seleccionado en el listado de la parte derecha

## Generar PDF
![Generar PDF](https://i.ibb.co/Pg34dgc/image.png)

Se despliega una lista con los AFN Registrados y hay un boton para poder generar el PDF del AFN Registrado

## Apartado de Ayuda AFN
![Interfaz](https://i.ibb.co/9h3q6tD/image.png)
Se muestra un ejemplo de como se debe de agregar un AFN

## Modulo AFD
![Interfaz](https://i.ibb.co/XpykCL2/image.png)

En el cual de la misma manera que en el menu principal se desplieguen botones en la parte de la izquierda con las siguientes opciones:

## - Agregar AFD
![Interfaz](https://i.ibb.co/W6jWY1P/image.png)

En el modulo de Agregar AFD nos pide registrar la informacion del AFD a registrar, y en la parte inferior izquierda el boton para agregar el AFD o para regresar al Menu

## - Generar PDF
![Generar PDF](https://i.ibb.co/Pg34dgc/image.png)
Se despliega una lista con los AFD Registrados y hay un botón para poder generar el PDF del AFD Registrado

## - Apartado de Ayuda AFD
![Interfaz](https://i.ibb.co/cbMtmX7/image.png)
Se muestra un ejemplo de como se debe de agregar un AFD

## - Generar Cadena y Comprobar Ruta
![Interfaz](https://i.ibb.co/0hpJyrk/image.png)

## - Modulo de Carga de Ayuda
![Interfaz](https://i.ibb.co/KKhgGsy/image.png)
En el cual de la misma manera que en el menu principal se desplieguan botones en la parte de la izquierda 
### Ejemplo de Carga
![Interfaz](https://i.ibb.co/7N6Tq6k/image.png)

### Mensaje de Aceptacion
![Interfaz](https://i.ibb.co/RYMD1P6/image.png)
