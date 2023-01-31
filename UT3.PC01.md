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
Ahora vamos a instalar auditd con el siguiente comando.

```bash
sudo apt-get install auditd
```

#### CONFIGURACIÓN DEL FICHERO
Ahora vamos a editar el fichero **/etc/audit/rules.d/audit.rules**

##### **PARAMETROS A INSERTAR**
```bash
-w /usr/bin/docker -p wa
-w /var/lib/docker -p wa
-w /etc/docker -p wa
-w /lib/systemd/system/docker.service -p wa 
-w /lib/systemd/system/docker.socket -p wa 
-w /etc/default/docker -p wa
-w /etc/docker/daemon.json -p wa
-w /usr/bin/docker-containerd -p wa
-w /usr/bin/docker-runc -p wa
-w /run/containerd -p wa
-w /etc/containerd/config.toml -p wa
-w /usr/bin/containerd -p wa
-w /usr/bin/containerd-shim -p wa
-w /usr/bin/containerd-shim-runc-v1 -p wa
-w /usr/bin/containerd-shim-runc-v2 -p wa
-w /usr/bin/runc -p wa
```

Como vemos se va indiciar que **-w** nos indica que el fichero deber ser auditado por el programa instalado y que **-p wa** indica que se debe generar *logs* ante cualquier modificado en dichos ficheros o en el directorios.

##### PARAMETROS DENTRO DEL FICHERO
![AUDIT](/assets/img/PPS/ALE/001_auditpng.png)

#### REINICIO AUDITD
Ahora vamos a reiniciar el servicio para aplicar los cambios
```bash
sudo service auditd restart
```
#### VER LA NUEVA CONFIGURACIÓN

![BENCH](/assets/img/PPS/ALE/002_bench.png)

Como se ve que se ha cambiando, ya que tenemos los directorios auditados, pero aun vemos que tiene algunos errores, que ahora vamos a configurar los fichero para poder corregirlo.

### DAEMON DOCKER

Vamos arreglar los siguientes errores:

    > ***2.14***: Vamos a usar el parametro **"userland-proxy": false**
    > 
    ![2.14](/assets/img/PPS/ALE/004_bench.png)
    > ***2.16***: Vamoa a usar el parametro **"no-new-privileges": true**
    ![2.16](/assets/img/PPS/ALE/005_bench.png)


Ahora en algunas opciones puede fallar, simplemente por no esta disponibles, por lo que si no se levanta el servicio de **Docker**, con lo cual vamos a crear un fichero en **/etc/docker/daemon.json**.

##### **PARAMETROS A INSERTAR**
```json
{
"icc": false,
    "userns-remap": "default",
    "log-driver": "syslog", 
    "disable-legacy-registry": true,
    "live-restore": true,
    "userland-proxy": false,
    "no-new-privileges": true
}
```
Ahora vamos a ver el resultado que nos da con el fichero creado

##### **VER CONFIGURACIÓN**

![BENCH](/assets/img/PPS/ALE/003_bench.png)
