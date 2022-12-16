# Easy Peasy - WriteUp
## Creamos la carpeta donde estara nuestra maquina para realizar la prueba

Creamos un directorio llamado **easy-peasy** y nos meteremos a el.

```bash
mkdir easy-peasy
cd $_
```

Una Vez dentro de la carpeta podemos realizar la actividad.

## Tarea 1 - Enumeración a través de Nmap

Ahora nos debera salir algunas preguntas en el cual deberemos responder usando el **Nmap**

- ¿Cuántos puertos están abierto?
```bash
3
```
- ¿Cuál es la versión de nginx?
```bash
1.16.1
```
- ¿Qué se está ejecutando en el puerto más alto?
```bash
Tiene Buscar que puerto es el mayor y ya sabe que servicio es
```

Ahora vamos a usar el **Nmap** con los siguientes parametros

```bash
nmap -sC -sV -p- -oN Puertos.txt <IP_OBJETIVO>
```

- -sC : Script predeterminados
- -sV : Detección de versión
- -oN : La salida donde se almacenara el resultado del comando
- -p- : Todos los puertos para escanear

**Salida del comando**

```bash
Nmap scan report for 10.10.67.60
Host is up (0.063s latency).
Not shown: 65532 closed tcp ports (reset)
PORT      STATE SERVICE VERSION
80/tcp    open  http    nginx 1.16.1
| http-robots.txt: 1 disallowed entry 
|_/
|_http-title: Welcome to nginx!
|_http-server-header: nginx/1.16.1
6498/tcp  open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 30:4a:2b:22:ac:d9:56:09:f2:da:12:20:57:f4:6c:d4 (RSA)
|   256 bf:86:c9:c7:b7:ef:8c:8b:b9:94:ae:01:88:c0:85:4d (ECDSA)
|_  256 a1:72:ef:6c:81:29:13:ef:5a:6c:24:03:4c:fe:3d:0b (ED25519)
65524/tcp open  http    Apache httpd 2.4.43 ((Ubuntu))
| http-robots.txt: 1 disallowed entry 
|_/
|_http-title: Apache2 Debian Default Page: It works
|_http-server-header: Apache/2.4.43 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

**CAPTURA DEL RESULTADO EN LA TERMINAL**

[PONER FOTO]

Con Estos resultados vamos a responder las Preguntas anteriormente realizada.

Con lo que vemos que hay **3 puertos** abiertos con lo cual son

- **80 / http-nginx 1.16.1** : Tiene un Servidor web nginx
- **6498 / ssh-OpenSSH 7.6p1** : Tiene un servicio SSH
- **65524 / http-Apache http 2.4.43** : Tiene un servidor Apache
- **OS detectado - Linux**