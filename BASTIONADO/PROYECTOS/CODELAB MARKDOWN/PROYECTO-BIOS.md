author: Marcos Rojas Pacheco
summary: Seguridad para nuestras BIOS
id: Proyecto-1-BIOS-UEFI
categories: codelab,markdown
environments: Web
status: Published
feedback link: https://github.com/MarcusRojasPacheco


# SEGURIDAD EN NUESTRAS BIOS
## ANTES DE EMPEZAR
Duration: 0:02:00

### SABER QUE BIOS TENEMOS
Debemos saber que BIOS tenemos en nuestro ordenador.
Para ello ya sabremos que modelo de ordenador tenemos, en este caso tenemos `Acer Aspire ES1-512`.

<br>

Para entrar en la BIOS en nuestro caso es el `F2` y en la parte superior nos sale el nombre de la BIOS.

<br>

Nuestra BIOS tiene de fabricante a [INSYDE](https://www.insyde.com/), aunque la marca de nuestro ordenador sea `Acer`, digamos que la BIOS que tiene montada nuestro ordenador no la crean la propia marca del ordenador sino que es de otra empresa que se dedica a ello.

<br>
<center>
![Insyde-H20-Bios](/img/Insyde-H20-Bios.png)
</center>

#### MANUAL DE LA BIOS
<button>
  [MANUAL DE LA BIOS](/docs/documentos/bios_insyde_gharial_01.pdf)
</button>

## ACTUALIZAR LA BIOS
Duration: 0:05:00

### CÓMO ACTUALIZAR LA BIOS

[![ACTUALIZACIÓN DE BIOS](/img/VIDEO-ACER.png)](https://www.youtube.com/watch?v=GYfDgDfXhLY)

<aside class="negative">
Recuerda que debes seguir las instrucciones del `Video`, ya que una mala actualización de la BIOS nos podría dejar el ordenador inservible.
</aside>

Nuestra BIOS siempre tiene una versión en la cual se creó el ordenador, pero mucho no toma en cuenta la actualización de la BIOS, ya que se puede encontrar vulnerabilidad a lo largo del tiempo y el propio fabricante da la opción mediante un programa o un archivo la actualización de ella.

En este caso se ha tenido actualizar la BIOS de nuestro Ordenador con la herramienta que nos proporciona la marca `Acer`.

#### EJEMPLO

![EJEMPLO DEMOSTRATIVO](/img/ACTU-BIOS.jpeg)

#### HERRAMIENTA

<button>
  [DESCARGAR LA HERRAMIENTA](https://www.acer.com/ac/es/ES/content/support-product/5611?b=1&pn=NX.MRWEB.003&sn=NXMRWEB003450183656600)
</button>

## DESACTIVAR DE LA RED
Duration: 0:02:00

### FUERA DE LA RED

Como vemos hay una opción en la cual se puede hacer boot desde la red, la cual esta opción por defecto esta activa, nos podemos encima de la opción y daremos a la opción `Disable`.

<br>

También observamos que existe una opción llamada `Wake on LAN` pero esa opción por defecto viene `Disable`, que desactiva el controlador LAN.

#### EJEMPLO

![EJEMPLO DEMOSTRATIVO](/img/NET-BIOS.jpeg)

## DESACTIVAR ARRANQUE DE BOOT
Duration: 0:02:00

### QUITAR LA OPCION `F12`

En este apartado podemos desactivar el `F12`, ya que por defecto esta activado y se podría usar un USB con un Sistema Operativo de instalación u otros programas que podría sacar nuestra información del disco de nuestro ordenador.

<br>

La opción viene `Enable` y vamos a la opción y daremos a la opción `Disable`.

#### EJEMPLO

![EJEMPLO DEMOSTRATIVO](/img/F12-BIOS.jpeg)

## PROTEGER LA BIOS CON CONTRASEÑAS
Duration: 0:10:00

### CONTRASEÑA PARA SER PROTEGIDOS

En este paso vamos a poner contraseña para proteger la BIOS y tenemos las siguientes opciones `Set Supervidor Password`, `Set User Password`, `Set HDD Password` y también tenemos una opción que siempre que encienda el ordenador tenga poner la contraseña ante de iniciar.

<br>

Cuando pongamos la contraseña de supervisor en la opción `Password on Boot`, pondremos la opción `Enable`.

#### EJEMPLO

![EJEMPLO DEMOSTRATIVO](/img/SUPERVIDOR-BIOS.jpeg)

### CONTRASEÑA SUPERVISOR Y USUARIO

Pondremos la contraseña para `Set Supervisor Password`, esta contraseña ya depende el usuario o administrador que este configurando el ordenador.

<br>

Para la opción `Set User Password`, es de la misma manera y dependerá del usuario o administrador.

#### EJEMPLO

![EJEMPLO DEMOSTRATIVO](/img/PASS-SUPERVISOR-BIOS.jpeg)

###

![EJEMPLO DEMOSTRATIVO](/img/PASS-BIOS.jpeg)

### CONTRASEÑA PARA EL DISCO

En este paso pondremos poner contraseña, con la opción `Set HDD Password` y se pondrá la contraseña tanto el usuario como el administrador que lo este configuración.

<br>

Una vez se inicie, se pedirá poner la contraseña en el disco en la cual tenemos el sistema instalado.

#### EJEMPLO

![EJEMPLO DEMOSTRATIVO](/img/PASS-HDD-BIOS.jpeg)

#### 

![EJEMPLO DEMOSTRATIVO](/img/DISC-BIOS.jpeg)

<aside class="negative">
Como se observa, cuando inicia se ve los discos que tengo en mi ordenador. Uno está bloqueado 'El que tiene el sistema' y el otro es un disco de datos.
El fallo que veo en esta seguridad que se puede entrar al disco o formatear el disco 'Datos' y podría sacar información en él, no se ve ninguna manera en la cual se pueda bloquear los dos discos.
</aside>

### TODOS LOS CAMBIOS APLICADOS

![EJEMPLO DEMOSTRATIVO](/img/CONF-BIOS.jpeg)

## PRIORIDADES DE ARRANQUE
Duration: 0:02:00

### ARRANQUE

En esta opción no se puede hacer mucho simplemente mover las prioridades de arranque. En la opción `UEFI` si deja bloquear el BOOT pero en nuestro caso solo podemos poner `Legacy` ya que detecta el Sistema Operativo del Disco.

<aside class="positive">
En este apartado esta en modo `Legacy` ya que es el recomienda si se va usar un Sistema Operativo de Windows, y se tiene poner en este modo ya que si no el ordenador no detecta el disco, al poner el modo `UEFI` despliega otra opciones para la seguirdad pero al poner ese modo dejaría nuestro ordenador inservible y en nuestro caso nos interesa que el ordenador este siempre operativo.
</aside>

Una vez terminados todos los cambios se le dará `F10` y se guardara la configuración realizada.

#### EJEMPLO

![EJEMPLO DEMOSTRATIVO](/img/ARRANQUE-BIOS.jpeg)

## SALTARSE LA SEGURIDAD
Duration: 0:05:00

### ¿COMO SE PUEDE SALTAR LA SEGURIDAD?

Existe una forma en la cual se puede saltar la seguridad de nuestro ordenador, en este caso si nos roba el portátil o tiene acceso a el.

Si no lo ha robado nos puede quitar la `PILA` la cual alimenta la BIOS y tras pasar unos `5/10 minutos` la BIOS se resetea.

#### EJEMPLO

![EJEMPLO DEMOSTRATIVO](/img/RESET-BIOS.jpeg)

###

Una vez realizado ese paso al entrar a la BIOS si pulsamos la tecla `INTRO` al menos `3` veces saldrá un mensaje en el cual debemos poner un código de supervisor, en la cual ese código dado se puede poner en [BIOSBUG](https://www.biosbug.com/acer/) o en [BIOS-PW](https://bios-pw.org/), ponemos los números que nos da nuestra BIOS y pondremos los que nos da la pagina y una vez ponemos los números dados por la pagina y ya estaría como supervisor con lo cual nos puede quitar la contraseña y dejarlo por defecto la BIOS.

#### EJEMPLO

![EJEMPLO DEMOSTRATIVO](/img/PASS-BREAK-BIOS.jpeg)
