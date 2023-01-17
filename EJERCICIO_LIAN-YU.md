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

Con lo cual vemos un texto, con lo cual vamos a un analizador de Hash para ver en cual esta encriptado.

![WEB_RESULTADO](/assets/img/HACKER_ETICO/LIAN-YU/WEB_04.png)

Vemos que esta en **Base 58** con lo cual vamos a usar [Cyber-Chef](https://gchq.github.io/CyberChef/) y la cual vamos obtener la contraseña del servicio **FTP**.

![WEB_RESULTADO](/assets/img/HACKER_ETICO/LIAN-YU/WEB_05.png)

### PREGUNTAS SOBRE LO ENCONTRADO

- ¿Cuál es la contraseña FTP??

```bash
!#@@@@@@@@
```