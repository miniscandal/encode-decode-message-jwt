# Administrador de claves RSA

Esta herramienta de terminal simplifica la administración de claves RSA, tanto públicas  
como privadas. Ofrece funcionalidades para la creación y lectura de archivos PEM.  
Permite la codificación de mensajes en formato JSON y la decodificación de mensajes  
en formato JWT.

<img src="./docs/pictures/terminal-capture.png" width="540">



## Recomendación importante
≧◠‿◠≦

Este software genera archivos PEM con claves RSA, las cuales son un componente  
crucial de la seguridad en la criptografía. Es esencial tratar estas claves con  
la máxima seguridad y precaución.  
No deben ser compartidas ni expuestas bajo ninguna circunstancia. Si se sospecha  
que una clave privada ha sido comprometida, debe ser reemplazada inmediatamente.  
Recuerda siempre seguir las mejores prácticas de seguridad al manejar claves RSA.


## Configuración de desarrollo
 ≧◠‿◠≦

### Requisitos previos

* Conocimientos básicos de terminal y línea de comandos
* Tener instalado [Python](https://www.python.org/) en tu sistema que incluye [PIP](https://pypi.org/project/pip/)

### Procedimiento de configuración

#### Clonar repositorio

```
git clone https://github.com/miniscandal/encode-decode-message-jwt.git
cd .\encode-decode-message-jwt\
```

#### Configurar entorno virtual

```
python -m venv .\venv
.\venv\Scripts\activate
```

#### Instalar módulos requeridos

```
pip install -r requirements.txt`
```

#### Elementos esenciales

Archivo JSON con el nombre "message.json" en el directorio resources  
con la información que deseas codificar.


### Lista de comandos para el script

```
python .\src\main.py -h
python .\src\main.py -s create_pem
python .\src\main.py -s read_pem
python .\src\main.py -s message_encode
python .\src\main.py -s message_decode
```



## Documentación 
 ≧◠‿◠≦


### Tecnologías utilizadas
![Terminal](https://img.shields.io/badge/Terminal-%23474745.svg?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-%233776AB.svg?style=for-the-badge&logo=python&logoColor=white)
![JSON](https://img.shields.io/badge/JSON-%2348494a.svg?style=for-the-badge)
![JWT](https://img.shields.io/badge/JWT-%2300aa00.svg?style=for-the-badge)


### Referencias

* [Python](https://www.python.org/)



## Reflexiones y aprendizajes

≧◠‿◠≦

Durante el desarrollo de esta herramienta de terminal, perfeccioné y expandí  
mis habilidades en áreas clave.

Implementé un entorno virtual aislado para evitar conflictos de dependencias  
previniendo la contaminación del sistema.

Dediqué tiempo para optimizar la estructura del proyecto y las funcionalidades  
lo que resultó en un código más organizado y una navegación y comprensión  
del flujo del programa más sencillas.

Esta herramienta es en respuesta a la necesidad de realizar pruebas en un proyecto  
independiente, construido con JAVA y Spring Boot, que requería la autenticación  
de usuarios mediante JWT.

En conclusión, este proyecto ha fortalecido mis habilidades técnicas y me ha  
permitido adquirir nuevas competencias, especialmente en el desarrollo de software  
para la terminal. Estas capacidades serán fundamentales para afrontar futuros  
desafíos, particularmente en la creación de herramientas que optimicen la  
productividad y faciliten la gestión de proyectos.



## Créditos

≧◠‿◠≦

#### Recursos de código abierto

* PyJWT: Una biblioteca de Python para codificar y decodificar JWT.  
  Desarrollado por José Padilla y otros contribuyentes.

Agradecemos a los autores de estas bibliotecas por su trabajo y contribución a la comunidad de
software libre.



## Licencia

≧◠‿◠≦

Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.
