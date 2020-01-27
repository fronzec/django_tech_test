# Introducción
Prueba tecnica

# Objetivos
- [x] Crea un CRUD para cada modelo.
- [ ] Agregar un sistema de permisos por servicio y 3 categorias de usuarios.
- [x] Documenta el código.
- [ ] Crea pruebas unitarias.
- [ ] Hay errores y warnings puestos en el código, encuéntralos y crea un fix.
- [x] Crea commits descriptivos.
- [x] Crear un archivo Dockerfile para correr el proyecto con nginx y wsgi.
- [X] Crear un router para separar la base de datos de lectura y escritura. 


La prueba tiene un tiempo para desarrollarse de 3 días


# NOTAS ADICIONALES
- Correr con `docker-compose up --build`
- Por default se crea el ususario `urbvan` con password `pruebatecnica` con el cual se puede obtener el token para hacer uso del API, se puede importar la coleccion de postman `Backend Prueba Técnica URBVAN.postman_collection.json` para ver los endpoints disponibles.
- Por default la aplicacion se ejecuta en el puerto **8080**.