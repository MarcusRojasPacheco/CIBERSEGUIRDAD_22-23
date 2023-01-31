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
> ***2.14***: Vamos a usar el parametro **"userland-proxy": false** para poder solucionar el error.
>
> *Indica que el derecho del contenedor a obtener nuevos permisos no está restringido.*
>
> *En Docker, los contenedores se ejecutan con privilegios y permisos específicos necesarios para realizar tareas específicas. Sin embargo, es importante limitar estos privilegios para evitar ataques o errores que puedan comprometer la seguridad del sistema.*
>
> ![2.14](/assets/img/PPS/ALE/004_bench.png)

> ***2.16***: Vamoa a usar el parametro **"no-new-privileges": true** para poder solucionar el error.
>
> *Indica que el proxy de usuario no está desactivado.*
>
> *El proxy de usuario es una funcionalidad en Docker que permite que los contenedores se comuniquen con otros servicios y redes. Sin embargo, el uso del proxy de usuario puede ser un riesgo de seguridad, ya que puede permitir que los atacantes redirijan el tráfico de red y comprometan la seguridad del sistema.*
>
>![2.16](/assets/img/PPS/ALE/005_bench.png)


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
Ahora vamos a ver el resultado que nos da tras la configuración aplicada.

##### **VER CONFIGURACIÓN**

![BENCH](/assets/img/PPS/ALE/003_bench.png)

### ANALISIS ARCHIVO DOCKERFILE
Ahora vamos a elegir un archivo **dockerfile** que se habia creado en la actividad [UT3.AP00A - AFIANZANDO EL USO DE DOCKERFILE](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/mod/assign/view.php?id=454669) y se va realizar un testeo con **Trivy**


#### INSTALACIÓN DE TRIVY
Ahora vamos a instalar **Trivy** con el siguiente comando.

```bash
sudo apt-get install wget apt-transport-https gnupg lsb-release
wget -qO - https://aquasecurity.github.io/trivy-repo/deb/public.key | sudo apt-key add -
echo deb https://aquasecurity.github.io/trivy-repo/deb $(lsb_release -sc) main | sudo tee -a /etc/apt/sources.list.d/trivy.list
sudo apt-get update
sudo apt-get install trivy
```
#### EJECUTAR TRIVY
Ahora vamos a ejecutar **Trivy**.
```bash
trivy image <docker-imagen>
```
##### VER LAS VULNERABILIDADES 

![TRIVY](/assets/img/PPS/ALE/001_trivy.png)

Vemos que existe una vulnerabilidad en apache **CVE-2006-20001** con lo cual podria causar que el proceso se bloquee.

![CVE](/assets/img/PPS/ALE/001_CVE.png)

### ANALISIS DE IMAGENES

Ahora vamos a crear la analisar la Imagen WordPress de la Actividad [UT3.AP03](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/mod/assign/view.php?id=454668) con lo que vamos analisarlo con **trivy**, despues se hara un cambio con lo que vamos a usar *wordpress:4.6* y se realiza el mismo proceso.

#### COMPARACIÓN DE IMAGENES

Ahora vamos a usar **trivy** para ver las vulnerabilidades, con lo cual la versión 4.6 tiene mucha vulnerabilidades.

> ![DOCKER](/assets/img/PPS/ALE/001_docker.png)
>
> ![DOCKER](/assets/img/PPS/ALE/002_docker.png)

##### **VERSIÓN 4.6**
Vemos que en *Login* Existe una **Critica** 

![LOGIN-WP](/assets/img/PPS/ALE/003_trivy.png)

##### **ULTIMA VERSIÓN**
Vemos que en *Login* ya no existe una vulnerabilidad **Critica**

![LOGIN-WP](/assets/img/PPS/ALE/002_trivy.png)