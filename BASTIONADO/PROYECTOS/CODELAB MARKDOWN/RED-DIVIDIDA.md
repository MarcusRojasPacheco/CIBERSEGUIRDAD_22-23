author: Marcos Rojas Pacheco
summlaary: Seguridad para el GRUB
id: LA RED DIVIDIDA
categories: codelab,markdown
environments: Web
status: Published
feedback link: https://github.com/IES-Rafael-Alberti/MRP-Proyecto-Bastionado/issues/1#issue-1419817708

# LA RED DIVIDIDA

## CREACIÓN DE LA VLSM
Duration: 0:05:00

### DIVIDIMOS VLSM

Para ello vamos a crear la subredes, con lo cual vamos a usar una pagina en el cual nos va ayudar a realizar la división de la red.
 - [ARCADIO](https://www.arcadio.gq/calculadora-subredes-vlsm.html)

Para ello nuestra red estara formada por lo siguiente

 - 14 DISPOSITIVOS EN VENTAS
 - 14 DISPOSITIVOS EN TRANSPORTE
 - 14 DISPOSITIVOS EN SERVIDORES (AUNQUE SE USARA MENOS)
 -  6 DISPOSITIVOS EN ADMINISTRATIVO
 -  2 DISPOSITIVOS EN ROUTER (SOLO SE USA ESTATICAMENTE PARA SU IPS)

### RESULTADO DE LA DIVISIÓN DE LA RED

![RED](/img/SUBREDES.png)

### PACKET TRACER CISCO

 - [DESCARGAR](/fichero/RED_PROYECTO_GRUPO_2.pkt)

## CONFIGURACIÓN - SWITCH
Duration: 0:05:00

### SWITCH - CONFIGURACIÓN INICIAL

Antes de empezar a configurar el Switch vamos a poner los siguientes comandos para poder configurarlo correctamente.

``` bash
ENABLE
CONF T
```
### SWITCH - CONFIGURACIÓN VLANS

Ahora vamos a poner los comandos para poder crear las VLANS en nuestro Switch.

``` bash
HOSTNAME (NOMBRE DE SWITCH)
VLAN 10                        [REPETIR ESTE PASO LAS VECES NECESARIAS]
NAME (NOMBRE)                  [REPETIR ESTE PASO LAS VECES NECESARIAS]
EXIT
```

Todos estos parametros vamos a ponerlo en todos los Switch que estan en nuestra red y se va configuración segun se adapte a las necesidades de configuración.

Con el siguiente comando vamos a ver si la configuración fue correcta.

``` bash
SHOW VLAN BRIEF                [PARA COMPROBAR LA CONFIGURACIÓN]
```
### SWITCH - PUERTOS DE ACCESO

Ahora vamos a configurar los puertos de acceso en el Switch para poder que las VLAN se pueda comunicar entre ellas y el Router pueda dirigir bien las IPs configuración.

``` bash
INTERFACE {EL PUERTO CONECTADO AL ORDENADOR}
SWITCHPORT MODE ACCESS
SWITCHPORT ACCESS VLAN {NÚMERO DE VLAN DEL ORDENADOR}
```

Ahora vamos a activar el Switch Port Security.

``` bash
SWITCHPORT PORT-SECURITY
SWITCHPORT PORT-SECURITY MAXIMUM 1
SWITCHPORT PORT-SECURITY VIOLATION SHUTDOWN
SWITCHPORT PORT-SECURITY MAC-ADDRESS STICKY
```

Con toda esta configuración vamos a asegurar que la IP este ligada con la MAC.

### SWITCH - PUERTOS TRONCALES

Ahora vamos a configurar los puertos troncales para asegurar que se pueda comunicar correctamente.

``` bash
INTERFACE {EL PUERTO CONECTADO ENTRE SWITCH}
SWITCHPORT MODE TRUNK
SWITCHPORT TRUNK ALLOWED VLAN 10,20,30,40 {LAS VLAN CREADAS}

#PARA AÑADIR VLAN NATIVA
SWITCHPORT TRUNK NATIVE VLAN 10
```
### SWITCH - PUERTOS TRONCALES PARA ROUTER

Ahora vamos a configurar los puertos troncales para la interfaz que este conectado con el Router.

``` bash
INTERFACE GIGABITETHERNET 0/1
SWITCHPORT MODE TRUNK

#PARA AÑADIR VLAN NATIVA
SWITCHPORT TRUNK NATIVE VLAN 10
SWITCHPORT TRUNK ALLOWED VLAN 10,20,30,40 {LAS VLAN CREADAS}
```
## CONFIGURACIÓN - ROUTER
Duration: 0:05:00

### ROUTER - CONFIGURACIÓN INICIAL

Antes de empezar a configurar el Router vamos a poner los siguientes comandos para poder configurarlo correctamente.

``` bash
ENABLE
CONF T
HOSTNAME ROUTER
INTERFACE GIGABITETHERNET 0/0/0
NO SHUTDOWN
EXIT
```

### ROUTER - CREAR VLANS

Ahora vamos a crear las VLAN en el router con lo cual se va crear una interfaz virtual de la interfaz real, vamos usar el siguiente comando.

``` bash
INTERFACE GIGABITETHERNET 0/0/0.10
ENCAPSULATION DOT1Q 10 NATIVE
IP ADDRESS {IP DEL HOST RESERVADO PARA EL ROUTER DEPENDIENDO DE LA VLAN} {MÁSCARA DE RED}

[REPETIR EL SIGUIENTE PROCESO LAS VECES NECESARIAS]

INTERFACE GIGABITETHERNET 0/0/0.X0{DEPENDIENDO DE LA VLAN .10 .20 .30 ETC}
ENCAPSULATION DOT1Q 10
IP ADDRESS {IP DEL HOST RESERVADO PARA EL ROUTER DEPENDIENDO DE LA VLAN} {MÁSCARA DE RED}
EXIT

INTERACE GIGABITETHERNET 0/0/0
NO SHUTDOWN
EXIT
```
### ROUTER - EXCLUIR IP EN EL DHCP

Vamos a configurar para que el Router no de la IP que querramos excluir de la difusión de la red.

``` bash
IP DHCP EXCLUDED-ADDRESS 192.168.1.1 (EXCLUIR IP)
IP DHCP POOL DHCP_LAN_VENTA (CREAR DHCP PARA UNA VLAN)
NETWORK 192.168.0.0 255.255.255.0 (SELECCIONAR IP)
DEFAULT-ROUTER 192.168.0.1 (INDICAR IP DEL ROUTER)
DNS-SERVER 1.1.1.1 (INDICAR DNS)
EXIT
(REPETIR ESTOS PASOS POR CADA VLAN)

SHOW RUN {PARA COMPROBAR COMO HA QUEDADO LA CONFIGURACIÓN}
```

Con todo esto se ha terminado la configuración tanto del router como del Switch.