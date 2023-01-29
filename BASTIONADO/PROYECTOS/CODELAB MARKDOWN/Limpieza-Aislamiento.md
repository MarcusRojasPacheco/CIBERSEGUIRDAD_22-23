author: Marcos Rojas Pacheco
summary: LIMPIEZA Y AISLAMIENTO
id: Proyecto_3-Limpieza-Aislamiento
categories: codelab,markdown
environments: Web
status: Published
feedback link: https://github.com/IES-Rafael-Alberti/MRP-Proyecto-Bastionado/issues/1#issue-1419817708

# LIMPIEZA Y AISLAMIENTO

## ANTES DE EMPEZAR
Duration: 0:02:00

### ¿PARA QUE SE USARA NUESTRO SERVICIO?

En nuestro proyecto vamos a usar un servidor "Linux" y para cliente vamos usar el Sistema Operativo "Windows 10", con lo cual se va usar para un uso Ofimatico.

Con lo cual vamos a configurar y quitar programas que no sea necesario para que sea mas limpio y no tenga servicio en la cual se pueda atacar.

![PNETLAB](/img/001_PNETLAB.png)

## SERVIDOR LINUX
Duration: 0:10:00

### ACTUALIZACIÓN DEL SERVIDOR

Vamos a usar el comando siguiente:

``` bash
apt-get update && apt-get upgrade
```

Y se nos actualiza nuestro sistema linux.

![SERVIDOR_LINUX](/img/001_LINUX.png)

### KALR

Ahora vamos a obligar que el ejecutable glibcse este en direcciones diferente, con lo cual el atacante no sea capaz de lanzar un exploit o un ataque hacia las direcciones, y tambien lo que se hara es bloquear el kernel cuando se ejecute un exploit.

Con lo cual vamos a editar el fichero **/proc/sys/kernel/randomize_va_spacecon**.

![SERVIDOR_LINUX](/img/002_LINUX.png)

Con lo cual se pone el numero **2** con lo cual se activara:

 - **ASLR**: Ejecuta el programa da un resultado un diseño de memoria de pila diferente
 - **LIBS/MMAP**: LA ejecución del programa dara como resultado un diseño de memoria diferente
 - **EXEC ASLR**: Cada programa que se cumple *-fPIE -pie*, se cargara en diferente ubicaciones de memoria

### SERVICIOS

Ahora vamos a restringir los servicios que sean necesarios y dar acceso limitada.

#### RESTRIGIR SERVICIO KALLSYMS

Vamos a restrigir el acceso a */proc/kallsyms* con lo cual vamos a usar el siguiente comando:

```bash
chmod 400 /proc/kallsyms
```
 - **400**: Significa que permite la lectura por el usuario y deniega el acceso al archivo de grupos o otros.

![SERVIDOR_LINUX](/img/003_LINUX.png)

#### DESHABILITAR FIFOS

Para ello vamos a usar el siguiente comando para poder deshabilitarlo.
Los comando que vamos a usar es el siguiente:

```bash
sysctl fs.protected_regular=1
sysctl fs.protected_fifos=1
```
![SERVIDOR_LINUX](/img/004_LINUX.png)

#### DESHABILITAR IPv6

Al no usar este servicio lo vamos a quitar, ya que su uso no va ser necesario, vamos a usar los siguientes comandos:

```bash
sysctl -w net.ipv6.conf.all.disable_ipv6=1
sysctl -w net.ipv6.conf.default.disable_ipv6=1
sysctl -w net.ipv6.conf.lo.disable_ipv6=1
```
![SERVIDOR_LINUX](/img/008_LINUX.png)

#### RESTRINGIR ACCESO

Ahora vamos a restrigir el acesso a **PERF** y **PTRACE**.
Vamos a usar los siguiente comando:

```bash
sysctl -w kernel.perf_event_paranoid=3
sysctl -w kernel.yama.ptrace_scope=3
```
![SERVIDOR_LINUX](/img/005_LINUX.png)

##### TERMINAL ROOT

Vamos a quitar el acceso al acceso donde se puede conectar el root con el siguiente comando:

```bash
nano /etc/securetty
```
![SERVIDOR_LINUX](/img/006_LINUX.png)

#### CONFIGURAR SSH

Vamos a configurar el fichero **/etc/ssh/sshd_config** con lo cual vamos a poner los siguientes parametros:

```bash
ClientAliveInterval 500
ClientAliveCountMax 3
```
 - **ClientAliveInterval**: Poner que si existe inactividad el cliente conectado se desconecte del servidor.
 - **ClientAliveCountMax**: Si tras los envios establecido del cliente sigue sin responder se forzara el cierre de sessión.

![SERVIDOR_LINUX](/img/007_LINUX.png)

## CLIENTE WINDOWS
Duration: 0:10:00

### PROGRAMAS INSTALADOS

En el windows en el cual tenemos en **PNETLAB** nos trae por defecto lo siguiente:
 - 7-zip 19.00
 - Google Chrome
 - Microsoft Edge
 - Putty release 0.74
 - WinSCP 5.17.10

Como su uso que vamos a darle a este ordenador es un uso *Ofimatico* con lo cual de los programas instalados vamos a quitarle 2 de ellos por su uso no va ser necesario.
 - **PuTTY release 0.74**: Este es un programa esta destinado a la conexion por Telnet y SSH, por lo que no hace falta para su función de uso ofimatico.
 - **WinSCP 5.17.10**: Este es un programa FTP, pero no se va usar en las funciones de Ofimaticas.

### SERVICIOS

Ahora vamos a poner los servicos en el cual vamos a quitar y no van ser necesario para su uso:

|          **NOMBRE**         |  **ID DE TAREA** |                                             **DESCRIPCIÓN**                                             |
|:---------------------------:|:----------------:|:-------------------------------------------------------------------------------------------------------:|
|             FAX             |       _FAX_      |                        No se suele usar en los usuarios domestico habitualmente.                        |
|             IPV6            |     _IPHPSVC_    |                              Como se usa IPv4 no hace falta este servicio.                              |
|    ADMINISTRADOR XBOXLIVE   | _XBLAUTHMANAGER_ |                           Es un uso Ofimatico no hace falta el servicio xbox.                           |
|   GUARDAR PARTIDA XBOXLIVE  |   _XBLGAMESAVE_  |                            Es un uso Ofimatico no le hace falta este servicio                           |
|         RED XBOXLIVE        |  _XBOXNETAPISVC_ |                            Es un uso Ofimatico no va necesitar ese servicio.                            |
|      ESCRITORIO REMOTO      |  _REMOTEACCESS_  | La maquina de momento se usara presencialmente con lo cual no se va necesitar de momento este servicio. |
| COMPATIBILIDAD DE PROGRAMAS |     _PCASVC_     |              Se va actualizar los programas no se va necesitar que sean programas antiguos.             |
|         DIAGNOSTICOS        |     _DIAGSVC_    |          Al usuario que va usar este ordenador no va necesitar mandar información a Microsoft.          |
|    BIOMETRICO DE WINDOWS    |    _WBIOSRVC_    |   Si no tenemos en nuestro ordenador un sistema reconocimiento de huella o facial no va ser necesario.  |
