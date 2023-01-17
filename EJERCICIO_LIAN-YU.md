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

Volvemos a usar **GoBuster** con el resultado obtenido para poder sacar la primera pregunta.

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

### PREGUNTAS SOBRE LO ENCONTRADO

- ¿Qué es el directorio web que encontraste?

```bash
2@@@
```

Ahora dentro de la dirección web obtenida y miraremos su codigo fuente en el cual vemos lo siguiete.

![WEB_RESULTADO](/assets/img/HACKER_ETICO/LIAN-YU/WEB_01.png)