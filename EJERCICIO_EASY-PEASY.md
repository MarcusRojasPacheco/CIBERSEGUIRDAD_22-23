[VOLVER PAGINA PRINCIPAL](./)

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
Nmap scan report for 10.10.17.119
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

![NMAP](/assets/img/HACKER_ETICO/EASYPEASY/NMAP.PNG)

Con Estos resultados vamos a responder las Preguntas anteriormente realizada.

Con lo que vemos que hay **3 puertos** abiertos con lo cual son

- **80 / http-nginx 1.16.1** : Tiene un Servidor web nginx
- **6498 / ssh-OpenSSH 7.6p1** : Tiene un servicio SSH
- **65524 / http-Apache http 2.4.43** : Tiene un servidor Apache

## Tarea 2 - Comprometer la máquina

- Usando GoBuster, encuentre la bandera 1.

```bash
RESPUESTA
```

**GoBuster**

Con esta herramienta nos ayudara a buscar directorios ocultos.

```bash
gobuster dir -u http://><IP_OBJETIVO> -w <DICCIONARIO> -o <Salida.txt> -e .php,.html,.txt
```

- -u : URL de la Web Objetivo
- -w : El diccionario que vamos a usar
- -e : Para las extenciones de .php .html. txt.
- -o : Salida para almacenar en el directorio

```bash
===============================================================
Gobuster v3.3
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.17.119
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.3
[+] Expanded:                true
[+] Timeout:                 10s
===============================================================
2022/12/16 16:58:22 Starting gobuster in directory enumeration mode
===============================================================
http://10.10.17.119/hidden               (Status: 301) [Size: 169] [--> http://10.10.17.119 hidden/]                                                                                            
Progress: 220533 / 220561 (99.99%)
===============================================================
2022/12/16 17:18:27 Finished
=============================================================== 
```

**CAPTURA DEL RESULTADO EN LA TERMINAL**

![GoBuster](/assets/img/HACKER_ETICO/EASYPEASY/GoBuster001.PNG)

Vemos que existe un directorio llamado **hidden**. Ahora podemos ver tanto **robots.txt** y vemos tambien la dirección oculta **/hidden**.

![HIDDEN](/assets/img/HACKER_ETICO/EASYPEASY/WEB_001.PNG) ![NORMAL](/assets/img/HACKER_ETICO/EASYPEASY/WEB_002.PNG)

Vemos que los directorios ocultos que son los mismo que **GoBuster**.

[FOTO FUENTE WEB]

Vemos  que el codigo fuentes que no vemos nada interesante o no vemos ningun comentario oculto en el.

[FOTO GOBUSTER DE NUEVO]

Como vemos ahora enn **GoBuster** existe directorios ocultos.

Ahora vamos a la dirección oculta.

[FOTO DIR OCULTO]

Vemos el codigo fuente de la web, en la cual tiene un mensaje oculto que es flag que tenemos que resolver.

```bash
echo "CODIGO EN BASE64" | base64 -d
```

Con el codigo dado responde a la primera pregunta de la actividad.

---


[VOLVER PAGINA PRINCIPAL](./)