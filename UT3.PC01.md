---
layout: default
---
<!-- https://marcusrojaspacheco.github.io/CIBERSEGUIRDAD_22-23/EJERCICIOS_PYTHON.html -->
# UT3 PC01
## SEGURIDAD Y DESPLEGADO DE APLICACIONES CON DOCKER
[VOLVER PAGINA PRINCIPAL](./)

![DOCKER SEGURO](https://www.mend.io/wp-content/media/2021/04/aHViPTcyNTE0JmNtZD1pdGVtZWRpdG9yaW1hZ2UmZmlsZW5hbWU9aXRlbWVkaXRvcmltYWdlXzVjY2FiZmI4M2ExODEuanBnJnZlcnNpb249MDAwMCZzaWc9MDNkOGM4MGIzMzU3MGQwZmI1MjY3NTI1ZGNhNDMxYzI.jpeg)

### DOCKER BENCH

#### ¿QUE ES DOCKER BENCH?
Docker-bench es un script bash para probar la configuración de seguridad de los sistemas que ejecutan contenedores Docker. Verifica que se sigan una serie de recomendaciones y mejores prácticas para la seguridad del contenedor Docker y hace recomendaciones para mejorar la seguridad.

#### INSTALACIÓN DEL DOCKER BENCH
Tenemos que descargar el **DOCKER BENCH**, vamos a descargar el *Script* que esta en **Git**

##### COMANDOS

```bash
git clone https://github.com/docker/docker-bench-security.git
cd $_
./docker-bench-security.sh
```

#### EJECUCIÓN DEL DOCKER BENCH
Ahora vamos a ejecutar el script con el siguiente comando.

```bash
sh docker-bench-security.sh
```
Se observa que nos sales unos errores al ejecutarlo, simplemente por no tener reglas a los ficheros y a los directorios que en **Docker** recomienda ya que esta puesta las reglas por defecto, con lo cual vamos a descargar otro programa para lograr esa seguridad.

![BENCH](/assets/img/PPS/ALE/001_bench.png)

### AUDITD

#### ¿QUE ES AUDITD?
Auditd es un sistema de auditoría para realizar un seguimiento de los cambios en el sistema operativo y el sistema de archivos. Se utiliza para registrar y monitorear la actividad del sistema, como inicios de sesión, accesos a archivos y cambios en la configuración de seguridad. Los registros generados por auditd se pueden usar para detectar e investigar posibles incidentes de seguridad. Es una herramienta importante para auditar y monitorear la seguridad del sistema.

#### INSTALACIÓN DEL AUDITD