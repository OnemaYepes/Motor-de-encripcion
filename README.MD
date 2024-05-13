# Motor de Encriptación
Este proyecto de aula se ha desarrollado como parte de la asignatura "Lenguajes de Programación y Código Limpio", con el objetivo de ofrecer una herramienta de encriptación y desencriptación.
## Autores

Este código fue desarrollado por:

- Juan Manuel Yepes Montoya (Estudiante de Ingeniería de Sistemas)

- Alejandro Rivera Quintero (Estudiante de Ingeniería de Sistemas)

## Descripción
El Motor de Encriptación es una aplicación que permite encriptar y desencriptar mensajes utilizando una clave proporcionada, es decir, un sistema de cifrado simétrico. Utiliza un algoritmo de cifrado XOR para cifrar y descifrar los mensajes, lo que supone una base de la complejidad de otros algorítmos.

## ¿Cómo usarlo?
Para utilizar el Motor de Encriptación, sigue los siguientes pasos:

### Prerrequisitos:
- Asegúrate de tener Python 3.x instalado en tu sistema.

### Ejecución:
1. Clona o descarga el proyecto del Motor de Encriptación.
2. Abre una `Terminal` o `Command Prompt`.
3. Ubícate en la carpeta raíz del proyecto.
4. Debes tener instalado el Framework de `Kivy`. Házlo ejecutando la siguiente instrucción en la terminal posicionado en la raíz del proyecto.
    ```
    python -m pip install "kivy[base]"
    ```
5. 
    - Ejecuta la siguiente instrucción si deseas correr el programa por consola:
        ```
        python src\Console\CipherEngineConsole.py
        ```
    - Ejecuta lo siguiente si quieres correr las pruebas unitarias:
        ```
        python test\test_cipher_engine.py
        ```
    - Ejecuta lo siguiente si deseas correr la aplicación por consola:
        ```
        python src\GUI\CipherGUI.py
        ```


## ¿Cómo está hecho?
### Descripción de la arquitectura del proyecto:
El proyecto consta de un conjunto de clases y funciones implementadas en Python para encriptar y desencriptar textos utilizando una clave proporcionada. La arquitectura sigue un enfoque modular, lo que facilita la reutilización y extensión del código.

### Organización de los módulos:
El código se organiza en una única clase principal llamada `CipherEngine`, que contiene dos métodos estáticos: `EncryptText` y `DecryptText`. Estos métodos se encargan de realizar la encriptación y desencriptación de textos respectivamente. Además, se definen excepciones personalizadas para manejar casos como textos vacíos, claves vacías, caracteres no válidos en la clave, y claves más largas que el texto a encriptar o desencriptar.


## Lógica del Motor de Encriptación:

El Motor de Encriptación implementa un algoritmo de encriptación simple pero efectivo basado en el operador XOR (bit a bit exclusivo) entre cada carácter del texto y su correspondiente carácter de la clave proporcionada. Este algoritmo es simétrico, lo que significa que la misma clave se utiliza tanto para encriptar como para desencriptar el texto.

### Proceso de Encriptación:
1. Se verifica que el texto a encriptar y la clave no estén vacíos.
2. Se comprueba que la clave no contenga caracteres no alfanuméricos.
3. Se verifica que la longitud de la clave no sea mayor que la longitud del texto a encriptar.
4. Se itera sobre cada carácter del texto a encriptar.
5. Para cada carácter del texto, se realiza una operación XOR entre ese carácter y el carácter correspondiente de la clave (ciclo a ciclo). El resultado de esta operación se agrega al texto encriptado.

### Proceso de Desencriptación:
1. Se verifica que el texto encriptado y la clave no estén vacíos.
2. Se comprueba que la clave no contenga caracteres no alfanuméricos.
3. Se verifica que la longitud del texto encriptado no sea menor que la longitud de la clave.
4. Se itera sobre cada carácter del texto encriptado.
5. Para cada carácter del texto encriptado, se realiza una operación XOR entre ese carácter y el carácter correspondiente de la clave (ciclo a ciclo). El resultado de esta operación se agrega al texto desencriptado.


