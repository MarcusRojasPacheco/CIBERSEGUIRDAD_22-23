author: Marcos Rojas Pacheco
summlaary: Seguridad en UNIFI
id: GUIA_DE_UNIFI
categories: codelab,markdown
environments: Web
status: Published
feedback link: https://github.com/IES-Rafael-Alberti/MRP-Proyecto-Bastionado/issues/1#issue-1419817708

# GUIA DE HARDENIG

## ROUTEROS - UNIFI
Duration: 0:02:00

### QUE SE USARA EN ESTA GUIA
Para usar esta guia en nuestra empresa creada con lo cual vamos a usa para la red de **2.4 GHz** [PLANO 2.4GHz](https://github.com/IES-Rafael-Alberti/Area-de-trabajo-general/blob/main/PROYECTO-8/PLANOS/2-4%20GHz.pdf) y otra red de **5 Ghz** [PLANO 5 GHz](https://github.com/IES-Rafael-Alberti/Area-de-trabajo-general/blob/main/PROYECTO-8/PLANOS/5Ghz.pdf), estos planos se han realizado con el plano original de la oficina Atrak-Dos [PLANOS ORIGINAL](https://github.com/IES-Rafael-Alberti/Area-de-trabajo-general/blob/main/PROYECTO-8/PLANOS/Planos%20de%20planta%20de%20oficina.png)

#### ROUTER QUE SE HA USADO EN CADA PLANO
##### **PLANOS 2.4 GHz**
> Se van usar **3** Router, en el cual dos de ellos copiara la configuración y difundir la red sin dar conflictos.
##### **PLANOS 5 GHz**
> Se van usar **4** Router, en el cual tres de ellos copiara la configuración y difundir la red sin dar conflictos.

## UNIFI - CONFIGURAR WIFI OFICINA
Duration: 0:07:00
### CONTRASEÑA DE LA RED
Ahora vamos a configurar el **nombre** y la **contraseña** de la red wifi para la oficina.
![CONTRASENA](/img3/UNIFI_001_CONTRASENA.png)

Ahora vamos a configurar la opciones avanzadas de la siguiente manera.
![AVANZADO](/img3/UNIFI_002_AVANZADA.png)
### SEGURIDAD 
Añadimos seguirdad en el Router para mayor seguridad en el.

![SEGURIDAD](/img3/UNIFI_003_SEGURIDAd.png)

Ahora vamos agregar el servicio **Radius** en la cual se va poner los empleados que pueda conectarse a la red.

![RADIUS](/img3/UNIFI_004_AGREGAR_RADIUS.png)
### HORARIO
Ahora vamos añadir un horario en la cual va estar activo el wifi en nuestra empresa, y ya que fuera del horario de la empresa no va estar operativo.

![HORARIO](/img3/UNIFI_004_HORARIO_WIFI.png)

## UNIFI - CONFIGURAR WIFI CLIENTE
Duration: 0:07:00
### CONECTARSE A LA RED
Como es una red de cliente en la sala de espera pondra un QR para poder conectarse, con lo cual se tendra el siguiente parametro que se podra conectar con **facebook**

![FACEBOOK-LOGIN](/img3/UNIFI_006_WIFI_CLIENTE.png)

### SEGURIDAD
Ahora vamos a configurar la seguridad que nos proporciona esta sección con lo cual vamos a ponerla de la siguiente manera:

![SEGURIDAD](/img3/UNIFI_007_SEGURIDAD_CLIENTE.png)

### TIEMPO DE USO DE LA RED
Ahora vamos a configurar el tiempo en la cual va estar conectado, con lo cual se va poner un maximo de **8 Horas** y lo reedirija a una URL para poder user la red.

![TIEMPO](/img3/UNIFI_008_CONFIGURAR_TIEMPO_CLIENTE.png)

Añadimos que el URL sea encriptado y que el lenguaje salga en español.
![TIEMPO](/img3/UNIFI_009_CONFIGURAR_TIEMPO_CLIENTE.png)

### HORARIO DE LA RED
Como la red de la oficina, la red cliente tendra el mismo horario de funcionamiento de la red wifi para los clientes.

![CLIENTESHORARIO](/img3/UNIFI_010_HORARIO.png)

## UNIFI - REDES CREADAS
Duration: 0:03:00
### LAS REDES CREADAS
Una vez creada las red ya se puede ver que se fue creada con exito y para los demas router es simplemente ponerlo en modo repetidor que amplifique la red de la empresa.
![RED WIFI](/img3/UNIFI_011_REDES_CREADAS.png)
Con todo esto seria en mi guia de lo basico que se puede configurar en la red.