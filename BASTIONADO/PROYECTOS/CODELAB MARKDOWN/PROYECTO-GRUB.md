author: Marcos Rojas Pacheco
summary: Seguridad para el GRUB
id: Proyecto-2-GRUB
categories: codelab,markdown
environments: Web
status: Published
feedback link: https://github.com/IES-Rafael-Alberti/MRP-Proyecto-Bastionado/issues/1#issue-1419817708

# SEGURIDAD PARA EL GRUB

<link id="favicon" rel="icon" href="/img/favicon.ico" type="image/x-icon">

## ¿QUE ES EL GRUB?
Duration: 0:02:00

### EL GRUB

El Grub [(Grand Unified Boot loader)](https://es.wikipedia.org/wiki/GNU_GRUB), es un gestor de arranque múltiple desarrollado inicialmente para el sistema GNU Hurd. El gestor de arranque grub tiene varias funciones, pero sin duda su misión principal es permitirnos seleccionar el sistema operativo que queremos usar justo en el momento de arrancar nuestro ordenador.

<br>

En esta guía vamos a utilizar el sistema operativo `DEBIAN`.

<br>

<center>

![DEBIAN](/img/Debian_logo.png)

</center>


#### ISO DE DEBIAN
<button>

  [DESCARGAR DEBIAN](https://www.debian.org/CD/http-ftp/index.es.html)

</button>

## CONTRASEÑA DE SEGURIDAD
Duration: 0:05:00

### COPIA DE SEGURIDAD EN LOS ARCHIVOS DE CONFIGURACIÓN

Ante de hacer cambios en los archivos de configuración tenemos que tomar unas ciertas precauciones ante de modificar los archivos, con lo que vamos hacer una copia de estos archivos por seguridad y poder restablecerlo si algo ha salido mal.

<br>

Tambien en mi caso no existe usuarios normales, solo existe el usuario `root`.

#### COMANDOS

`sudo cp /etc/default/grub ~/grub.old
sudo cp /etc/grub.d/00_header ~/00_header.old
sudo cp /etc/grub.d/30_os-prober ~/30_os-prober.old`

#### EJEMPLO

![COPIAS DE CARPETA](/img/COMANDO_01_GRUB.PNG)

### PROTEGER LAS CONTRASEÑA DE QUIEN PUEDA MODIFICAR EL GRUB

Ahora vamos a cifrar las contraseña de los usuarios con el siguiente comando `sudo grub-mkpasswd-pbkdf2` y nos pedirá la contraseña que vamos a ocultar y con resultado nos dará un `HASH` que nos servira luego.

#### EJEMPLO

![SEGURIDAD USUARIO](/img/COMANDO_02_GRUB.PNG)

######

Ahora vamos a usar el comando `sudo nano /etc/grub.d/00_header` para poder modificar el archivo y poner la siguiente linea al final del archivo de texto.

#### EJEMPLO 

![SEGURIDAD USUARIO](/img/COMANDO_03_GRUB.PNG)

######

Ahora vamos actualizar el grub con el siguiente comando `update-grub2`.

## OCULTACIÓN DEL ARRANQUE
Duration: 0:05:00

### QUITAR TIEMPO DEL GRUB

Ahora vamos a configurar el fichero  `/etc/default/grub` y vamos a quitar el tiempo de espera, para ello vamos a buscar `GRUB_TIMEOUT` y vamos a ponerle el valor `0`, con ello ya nuestro sistema no saltara con la elección del sistema y guardamos los cambios realizados.

#### EJEMPLO

![SEGURIDAD GRUB INICIO](/img/COMANDO_04_GRUB.PNG)

######

También se puede modificar el fichero `/etc/grub.d/30_os-prober` y en la ultima linea `adjust_timeout` la comentamos.

#### EJEMPLO

![SEGURIDAD GRUB INICIO](/img/COMANDO_05_GRUB.PNG)

######

Ahora con el comando `update-grub2` actualizamos nuestro grub.

## COPIA DE SEGURIDAD
Duration: 0:10:00

### AUTOMATIZAR LAS COPIAS

Ahora vamos a crear que haga una copia de seguridad para nuestro sistema. Antes de empezar si no tenemos la aplicación `backup`, si no la tenemos tenemos poner el comando `apt-get install deja-dup -y`, una vez instalado vamos nos va preguntar que queremos proteger.
<br>

En este caso vamos a hacer la copia de seguridad a las carpeta [`Home` - `/boot` - `/etc`].

<br>

<center>
![COPIAS DE CARPETA](/img/COMANDO_06_GRUB.PNG)
</center>

######

También vamos a poner que no copie las carpeta o dirección que no querríamos en este caso seria [`Papelera` - `Descarga` - `/tmp`].

<br>

<center>
![COPIAS DE CARPETA](/img/COMANDO_07_GRUB.PNG)
</center>

######

Ahora vamos a decirle donde queremos hacer la copia de seguridad, en este caso se ha creado una carpeta con el nombre de `Backups`.

<br>

<center>
![COPIAS DE CARPETA](/img/COMANDO_08_GRUB.PNG)
</center>

######

Para estar mas seguro vamos a poner una contraseña en el Backup que vamos a crear, también nos va dar la opción de no poner la contraseña, pero para mas protección vamos a elegir la opción de contraseña.

<br>

<center>
![COPIAS DE CARPETA](/img/COMANDO_09_GRUB.PNG)
</center>
######

Esperamos al que el proceso se termine, la primera vez va tarda un poco ya que tiene copiar todo los ficheros y archivos o carpeta que querríamos copiar.

<br>

<center>
![COPIAS DE CARPETA](/img/COMANDO_10_GRUB.PNG)
</center>

######

Ahora vamos a definir cuando queremos la copia vamos a poner como máximo `al menos tres meses` y vamos poner que el respaldo automático será cada semana.

<br>

<center>
![COPIAS DE CARPETA](/img/COMANDO_11_GRUB.PNG)
</center>

######

Ahora vamos si queremos podemos a respaldar la copia creada.

<br>

<center>
![COPIAS DE CARPETA](/img/COMANDO_12_GRUB.PNG)
</center>

######

Y nos va pedir la contraseña puesta en la copia.

<br>

<center>
![COPIAS DE CARPETA](/img/COMANDO_13_GRUB.PNG)
</center>

######

Con todo esto ya tenemos la copia de los archivos importante.

## CONCLUSIÓN
Duration: 0:02:00

### NO ES SUFICIENTE ESTA SEGURIDAD

Con todas esta seguridad no seria suficiente ya que aunque el atacante podría entrar usando un `USB` con un sistema operativo y de hay poder entrar y podría quitar toda la seguridad implementada, para aumentar la seguirdad podríamos configurar la [BIOS](https://super-tribble-5ef3ac53.pages.github.io/docs/proyectos/proyectos-BIOS/), o hacer particiones en el disco y cifrarlo para que el atacante le cueste un poco mas de que se salte toda la seguridad que se ponga en el equipo.