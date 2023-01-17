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
-rw-r--r--    1 0        0            2483 May 01  2020 .other_user
-rw-r--r--    1 1001     1001          675 May 01  2020 .profile
-rw-r--r--    1 0        0          511720 May 01  2020 Leave_me_alone.png
-rw-r--r--    1 0        0          549924 May 05  2020 Queen's_Gambit.png
-rw-r--r--    1 0        0          191026 May 01  2020 aa.jpg
226 Directory send OK.
ftp> get .other_user
local: .other_user remote: .other_user
229 Entering Extended Passive Mode (|||10838|).
150 Opening BINARY mode data connection for .other_user (2483 bytes).
100% |*****************************************************************************************************************|  2483       12.14 MiB/s    00:00 ETA
226 Transfer complete.
2483 bytes received in 00:00 (41.52 KiB/s)
ftp> get Leave_me_alone.png
local: Leave_me_alone.png remote: Leave_me_alone.png
229 Entering Extended Passive Mode (|||39026|).
150 Opening BINARY mode data connection for Leave_me_alone.png (511720 bytes).
100% |*****************************************************************************************************************|   499 KiB  400.34 KiB/s    00:00 ETA
226 Transfer complete.
511720 bytes received in 00:01 (383.91 KiB/s)
ftp> get Queen's_Gambit.png
local: Queen's_Gambit.png remote: Queen's_Gambit.png
229 Entering Extended Passive Mode (|||64566|).
150 Opening BINARY mode data connection for Queen's_Gambit.png (549924 bytes).
100% |*****************************************************************************************************************|   537 KiB  559.53 KiB/s    00:00 ETA
226 Transfer complete.
549924 bytes received in 00:01 (528.34 KiB/s)
ftp> get aa.jpg
local: aa.jpg remote: aa.jpg
229 Entering Extended Passive Mode (|||53806|).
150 Opening BINARY mode data connection for aa.jpg (191026 bytes).
100% |*****************************************************************************************************************|   186 KiB  438.90 KiB/s    00:00 ETA
226 Transfer complete.
191026 bytes received in 00:00 (383.88 KiB/s)
```