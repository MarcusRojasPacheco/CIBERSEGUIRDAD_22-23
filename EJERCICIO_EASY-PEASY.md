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

**SALIDA DEL COMANDO**

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

### Usando GoBuster, encuentre la bandera 1.

```bash
flag{f1######################}  
```

**GoBuster**

Con esta herramienta nos ayudara a buscar directorios ocultos.

```bash
gobuster dir -u http://><IP_OBJETIVO> -w <DICCIONARIO> -e .php,.html,.txt
```

- -u : URL de la Web Objetivo
- -w : El diccionario que vamos a usar
- -e : Para las extenciones de .php .html. txt.

**SALIDA DEL COMANDO**

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

**ROBOTS.txt**

![NORMAL](/assets/img/HACKER_ETICO/EASYPEASY/WEB_002.PNG)

**/Hidden**

![HIDDEN](/assets/img/HACKER_ETICO/EASYPEASY/WEB_001.PNG) 

Vemos ahora las direciones oculta de **Hidden** y veremos que encuentra una llamada **whatever** con lo cual vamos a usar el **GoBuster**

**SALIDA DEL COMANDO**

```bash
===============================================================
Gobuster v3.3
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.134.61:65524/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.3
[+] Expanded:                true
[+] Timeout:                 10s
===============================================================
2022/12/16 18:29:28 Starting gobuster in directory enumeration mode
===============================================================
http://10.10.134.61:65524/server-status        (Status: 403) [Size: 280]
Progress: 220538 / 220561 (99.99%)
===============================================================
2022/12/16 18:50:07 Finished
===============================================================

```

**CAPTURA DEL RESULTADO EN LA TERMINAL**

![GoBuster](/assets/img/HACKER_ETICO/EASYPEASY/GoBuster002.PNG)

Una vez dentro de **whatever** vemos el codigo fuente de esa pagina.

![WhatEver](/assets/img/HACKER_ETICO/EASYPEASY/WEB_003.PNG)

Estara el codigo en **Base64**, con lo cual tenemos que decodificarla.

```bash
echo "CODIGO EN BASE64" | base64 -d
```

Con el codigo dado responde a la primera pregunta de la actividad.

---

### Enumere aún más la máquina, ¿qué es la bandera 2?

```bash
flag{1m_######################}
```

Para ello vamos al servicio **APACHE** que esta en el puerto **65524** y vamos a ver **robots.txt** con lo cual vemos la primer codigo, pero tendremos que Hash es.

```bash
hash-identifier <HASH>
```
**SALIDA DEL COMANDO**

```bash
   #########################################################################
   #     __  __                     __           ______    _____           #
   #    /\ \/\ \                   /\ \         /\__  _\  /\  _ `\         #
   #    \ \ \_\ \     __      ____ \ \ \___     \/_/\ \/  \ \ \/\ \        #
   #     \ \  _  \  /'__`\   / ,__\ \ \  _ `\      \ \ \   \ \ \ \ \       #
   #      \ \ \ \ \/\ \_\ \_/\__, `\ \ \ \ \ \      \_\ \__ \ \ \_\ \      #
   #       \ \_\ \_\ \___ \_\/\____/  \ \_\ \_\     /\_____\ \ \____/      #
   #        \/_/\/_/\/__/\/_/\/___/    \/_/\/_/     \/_____/  \/___/  v1.2 #
   #                                                             By Zion3R #
   #                                                    www.Blackploit.com #
   #                                                   Root@Blackploit.com #
   #########################################################################
--------------------------------------------------

Possible Hashs:
[+] MD5
[+] Domain Cached Credentials - MD4(MD4(($pass)).(strtolower($username)))
```

Con esta herramienta nos identifica que Hash se ha utilizado, con lo cual vamos usar un decodificador web.

**DECODIFICADOR WEB**

![Flag2](/assets/img/HACKER_ETICO/EASYPEASY/WEB_007.PNG)

---

### Rompe el hash con easypeasy.txt, ¿Cuál es la bandera 3?

```bash
flag{9fd###################}
```
Esta flag fue facil de encontrar, ya que solo estaba en unos de los texto de la configuración por defecto del **APACHE**

**LA TERCERA BANDERA**

![Flag3](/assets/img/HACKER_ETICO/EASYPEASY/WEB_004.PNG)

---

### ¿Qué es el directorio oculto?

```bash
flag{/n0t###################}
```

Ahora vamos a ver el codigo fuente de la pagina web de apache.

![DECODE](/assets/img/HACKER_ETICO/EASYPEASY/WEB_005.PNG)

Ahora vamos a usar una pagina web que nos va ayudar a decodificar lo que hemos obtenidos en el anterior apartado.

![Flag4](/assets/img/HACKER_ETICO/EASYPEASY/WEB_006.PNG)

### Usando la lista de palabras que se le proporcionó en esta tarea, descifre el hash, ¿cuál es la contraseña?

```bash
myp##################
```

```bash
john --wordlist=easypeasy.txt --format=GOST <fichero.txt>
```

**SALIDA DEL COMANDO**

```bash
Created directory: /root/.john
Using default input encoding: UTF-8
Loaded 1 password hash (gost, GOST R 34.11-94 [64/64])
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
myp################## (?)     
1g 0:00:00:00 DONE (2022-12-16 19:51) 50.00g/s 204800p/s 204800c/s 204800C/s vgazoom4x..flash88
Use the "--show" option to display all of the cracked passwords reliably
Session completed.
```

### ¿Cuál es la contraseña para iniciar sesión en la máquina a través de SSH?

```bash
myp##################
```
Como vemos en la pagina donde la ruta que nos da [Flag3](#¿qué-es-el-directorio-oculto)


[VOLVER PAGINA PRINCIPAL](./)