---
marp: true
---

author: Marcos Rojas Pacheco
summary: SITE TO SITE WIREGUARD
id: VPN WIREGUARD
categories: codelab,markdown
environments: Web
status: Published
feedback link: https://github.com/MarcusRojasPacheco


# CONFIGURACIÓN VPN - SITE TO SITE [WIREGUARD]
## ANTES DE EMPEZAR
Duration: 0:02:00

### CONFIGURACIÓN DE PFSENSE - TERMINAL
Antes de empezar vamos a configurar la IP de la interfaz LAN, ya que una vez iniciado pfsense da una IP por defecto.
Tenemos que tener encuenta la dirección IP que nos ha dado la `WAN` que seria nuestra `IP PUBLICA`.

<br>
<aside class="negative">
![PFSENSE](/img/001.PNG)
</aside>
<br>

En este caso tendria en la `WAN` seria la IP - `192.168.1.108/24`.
Y en la `LAN` seria la IP - `192.168.2.1/24`

## CONFIGURAR LAN Y DHCP
### IP ESTATICAS EN LAN

Para ello vamos a darle una IP a la `LAN`, daremos a la opción `2`, y señalamos la interfaz `2`.
<br>
<aside class="negative">
![CONFIGURACIÓN LAN](/img/002.PNG)
</aside>
<br>
Asignaremos una IP a nuestra interfaz y añadir la mascara que tendra nuestra IP.

<br>
<aside class="negative">
![IP LAN](/img/003.PNG)
</aside>
<br>

<aside class="positive">
#### **NOTA**
Coger siempre este mismo rango: 0.0.0.11 a 0.0.0.21 (Reservar la 1 y la 10. La primera para la interfaz del PFSense y la otra para la interfaz del Wireguard)
</aside>
## CONFIGURACIÓN DHCP
Duration: 0:02:00

### DHCP DENTRO DE PFSENSE

Ahora vamos a decir que si queremos un `DHCP`.
Decimos el rango que va tener nuestro `DHCP` y nos dira que IP tiene ahora nuestro `sitio web` de `pfsense`, para poder configurarla mas adelante.

<br>
<aside class="negative">
![CONFIGURACIÓN LAN](/img/004.PNG)
</aside>
<br>

Ahora dentro de la interfaz de `pfsense` y vamos a reservar la IP a nuestro `WireGuard`, para ello vamos a `SERVICE > DHCP SERVER > LAN` y daremos a `DHCP STATIC MAPPING FOR THIS INTERFACE`.
<br>
Añadimos la IP que queremos en nuestro servidor `WireGuard`, para ello pondremos la `MAC` de nuestro `WireGuard` y la IP que vamos a poner a nuestro servidor.

<br>
<aside class="negative">
![CONFIGURACIÓN LAN](/img/005.PNG)
</aside>
<br>

## PUERTA DE ENLACE
Duration: 0:05:00

### GATEWAY

Vamos a irnos a `SYSTEM > ROUTING > GATEWAY` y vamos añadir un nuevo `GATEWAYS`.
<br>
<aside class="negative">
![CONFIGURACIÓN LAN](/img/006.PNG)
</aside>
<br>

Ahora vamos a `SYSTEM > ROUTING > STATIC ROUTES` y vamos añadir la IP de nuestro `WireGuard` y el rango IP del otro `SERVIDOR WIREGUARD`.
<br>
<aside class="negative">
![CONFIGURACIÓN LAN](/img/007.PNG)
</aside>
<br>

Y con todo esto el tráfico que vaya hacia la red contraria, que se redirija a la puerta de enlace que configuramos anteriormente.

## FIREWALL
Duration: 0:02:00

### CONFIGURAR FIREWALL

Ahora vamos a configurar el FireWall para que deje paso con los `PUERTOS ASIGNADOS` y sabiendo la `IP PUBLICA` que fue asignada.

<aside class="positive">
**INTERFACE** - WAN
<br>
**PROTOCOL** - TCP
<br>
**DESTINATION PORT RANGE** - DE 51820 HASTA 51820
<br>
**REDIRECT TARGET IP** - 192.168.2.10 [IP ASIGNADA POR EL DHCP LAN]
<br>
**REDIRECT TARGET PORT** - 51821
</aside>

<br>
<aside class="negative">
![CONFIGURACIÓN LAN](/img/008.PNG)
</aside>
<br>

Con todo esta configuración tenemos el `FireWall` y el `Pfsense` listo para que se pueda hacer la `VPN` sin problema.
<br>

Antes de terminar con el `Pfsense` vamos a `INTERFACES > WAN` y desmarcaremos lo marcado en `RESERVED NETWORKS`
<br>
<aside class="negative">
![CONFIGURACIÓN LAN](/img/009.PNG)
</aside>

## WIREGUARD
Duration: 0:05:00

### PROGRAMAS NECESARIOS

Antes de empezar vamos a empezar a configurar debemos actualizar el sistema con el siguietes comando `sudo apt update && sudo apt upgrade`.

<br>

Vamos a instalar IpTables y Traceroute.

<br>

- `sudo apt install iptables` - Esto lo introduciremos en la configuración del Wireguard para que nos permita el paso de paquetes mediante un `Masquerade`.
<br>

- `sudo apt install traceroute` - Esto nos ayudará a ver las trazas de conexión en caso de fallo.
<br>

Ahora vamos a instalar WireGuard `sudo apt install wireguard`.
<br>

Ahora vamos a crear la carpera donde ira el `WireGuard`, para ello ponemos el siguiente comando `mkdir -p /etc/wireguard/keys`.
<br>

Con todo esto ya estaria en la parte de instalación de todo lo necesario para poder hacer la configuración del `WireGuard`.

### CONFIGURACIÓN WIREGUARD

Ahora vamos a crear las claves `privada` y `publica` del `WireGuard`.
<br>

Con este comando vamos a crear la clave privada `wg genkey > host-priv.key` y creamos la clave publica `wg pubkey < host-priv.key > host-pub.key`.
<br>

Una vez creada las claves vamos a crear el archivo de configuración para el WireGuard, `nano /etc/wireguard/wg0.conf`.
<br>
<aside class="negative">
# Local settings for Localhost**
<br>
[Interface]
<br>
PrivateKey = (ClavePrivadaGeneradaEnEsteWireGuard)
<br>
Address = (Dirección IP Túnel Propio) PONER MÁSCARA
<br>
ListenPort = (Puerto de Escucha, normalmente el 51821)
<br>
PostUp = iptables -A FORWARD -i %i -j ACCEPT; iptables -t nat -A POSTROUTING -o (Interfaz Wireguard que da a la LAN) -j MASQUERADE
<br>
PostDown = iptables -D FORWARD -i %i -j ACCEPT; iptables -t nat -D POSTROUTING -o (Interfaz Wireguard que da a la LAN) -j MASQUERADE
<br>
SaveConfig = true
<br>
**# IP Forwarding**
<br>
PreUp = sysctl -w net.ipv4.ip_forward=1
<br>
**# Remote settings for Host Izquierda o Derecha**
<br>
[Peer]
<br>
PublicKey = (ClavePúblicaGeneradaEnElOtroWireguard)
<br>
Endpoint = (Dirección IP de la boca que da a internet del router de la red contraria):(Puerto de Escucha, normalmente el 51820)
<br>
AllowedIPs = (Dirección de red de la red contraria) PONER MÁSCARA y si quieres poner más de una dirección IP, sepárala de la anterior con una coma.
</aside>

Ahora con esta configuración ya funcionaria nuestra VPN.
<br>
<aside class="positive">
#### **NOTA**
Aquí puedes poner también la dirección IP de la boca contraria del túnel para ver si hacen “Ping” entre ellas.
</aside>

Ahora solo falta comprobarlo.

<br>
<aside class="positive">
#### **COMANDOS**
``wg-quick up wg0`` - Levantar la configuración
<br>
``wg show wg0`` - Comprobar el “Handshake”
<br>
``wg-quick down wg0`` -  Tirar la configuración
</aside>
<br>

Ahora con toda solo es hacer lo mismo pero en el otro WireGuard