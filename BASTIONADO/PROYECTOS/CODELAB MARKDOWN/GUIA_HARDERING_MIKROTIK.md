author: Marcos Rojas Pacheco
summlaary: Seguridad en Mikrotik
id: GUIA DE HARDERING
categories: codelab,markdown
environments: Web
status: Published
feedback link: https://github.com/IES-Rafael-Alberti/MRP-Proyecto-Bastionado/issues/1#issue-1419817708

# GUIA DE HARDENIG

## ROUTEROS - MIRKOTIK
Duration: 0:02:00

### QUE SE VA USAR EN ESTA GUIA
Para esta Guia de Hardering vamos usar un router **Mikrotik** en el cual vamos a usar las guias [HARDENING MIKROTIK](https://mum.mikrotik.com/presentations/KH17/presentation_4162_1493374113.pdf) y la Wiki oficila [WIKI-MIKROTIK](https://wiki.mikrotik.com/wiki/Manual:Securing_Your_Router).

![Mikrotik](/img2/MikroTik_Logo_(2022).svg.png)

## CAMBIAR EL USUARIO "ADMIN"
Duration: 0:05:00

### PELIGRO DEL USUARIO POR DEFECTO

Para ello en [WinBox](https://mikrotik.com/download#), entramos con el usuario **Admin**, con lo cual si viene de fabrica el router no tiene contraseña y puede entrar solo con el usuario.

Esto es un peligro ya que no tiene ninguna de la protección si un usuario se conecta, solo se puso en la versión *6.48.6* se añadio una mecanica en el **winbox** en la cual se tiene poner el modo *legacy* si quiere acceder desde el router si no tiene ninguna de la protección.

### AÑADIR USUARIO

Ahora vamos a crear un nuevo usuario como administrador, con lo cual se va usar el siguiente comando en mikrotik:
```bash
/user add name=Admin_Atrak-dos password=aTR@K-D0s!2023 group=full
```

Ahora vamos a cambiar el usuario de nombre de **Admin** por otro usuario.
```bash
/user set admin name=noAdmin
```

Y vamos a desabilitar el acceso al usuario **admin** para tener una mayor seguridad.

```bash
/uset set noAdmin disabled=yes #Se cambio arriba "admin" por "noAdmin"
```
Vamos a limitar el acceso por IP, ya que se puede entrar por MAC en los router mikrotik, aveces al tener varios configurado seria mas facil entrar por IP, con lo cual se va poner que este permitidos desde la subred 192.168.1.0/24.
```bash
/ip firewall filter add action=drop chain=input comment="Deny non-whitelisted IP access to router" in-interface=PUENTE src-address=!192.168.1.0/24
```
Ahora vamos a establecer un tiempo de espera si el usuario esta inactivo.
```bash
/ip service set www-ssl idle-timeout=5m
```
Y guardamos lo cambios que hemos realizado.
```bash
/save
```
### SEGUIRDAD EN LA CONTRASEÑA

Vamos a poner una nueva politica de contraseña en el Router con el siguiete comando.
```bash
/ip hotspot user profile set Admin_Atrak-dos password-strength=14
```

## CAMBIAR EL ACCESO A LA WEB DEL ROUTER
Duration: 0:02:00

### CAMBIO DE COMO SE ENTRA EN LA WEB ROUTER
Para cambiar el modo en el cual se puede entrar en el router se va cambiar el puerto en cual se puede entrar.
```bash
/ip service set www port=8989
```
Y vamos a poner que solo se puede entrar con la subred creada.
```bash
/ip firewall filter add chain=input action=accept protocol=tcp dst-port=8989 src-address=192.168.1.0/24
```

## RED WIFI PARA EMPLEADOS
Duration: 0:05:00

### CREAR UNA NUEVA RED WIFI PARA EMPLEADOS
Para crear una red WiFi para los empleados con un rango de direcciones IP de 192.168.1.100 a 192.168.1.120 y asegurarla, puedes seguir los siguientes pasos en RouterOS de MikroTik, con lo cual vamos a usar los siguientes comandos:
```bash
/interface wireless
add name=wlan-empleado ssid=empleado_WiFi mode=ap-bridge frequency=2.4ghz-b/g/n channel-width=20/40mhz-ht-above security-profile=empleado
```
#### DHCP SERVER
Ahora vamos a configurar el DHCP SERVER del router para la nueva red Wifi
```bash
/ip address
add address=192.168.1.1/24 interface=wlan-empleado

/ip dhcp-server
add address-pool=empleado-pool disabled=no interface=wlan-empleado name=empleado-dhcp lease-time=1d
```
Ahora vamos a configurar el **pool** de las direcciones IP
```bash
/ip pool
add name=empleado-pool ranges=192.168.1.100-192.168.1.120
```
#### SEGURIDAD EN LA RED WIFI
Para ellos se pondra los siguientes comando para poner seguro nuestra red wifi para los empleado y poder autenticar a su inicio.
```bash
/interface wireless security-profiles
add name=empleado mode=dynamic-keys authentication-types=wpa-psk,wpa2-psk unicast-ciphers=aes-ccm group-ciphers=aes-ccm wpa-pre-shared-key=3mplead0WiFi2023
```
y ponemos el siguiente comando para aplique en el perfil creado.
```bash
/interface wireless set wlan-employees security-profile=employees
```
Ahora vamos a ocultar la red wifi de los demas, obviamente esto no evita un escaneo de red oculta con las herramienta que se pueda usar para dectacta la red.
```bash
/interface wireless set wlan1 hide-ssid=yes
```

## RED WIFI CLIENTES
Duration: 0:05:00

### CREAR UNA NUEVA RED WIFI PARA CLIENTES
Ahora como es habitual en algunas empresa pone una red wifi para los clientes pero tendra limitaciones en su conexión para ello vamos a crearla de la siguiente manera:
```bash
/interface wireless
add name=wlan2 ssid=Invitados
/interface wireless security-profiles
set [ find default=yes ] supplicant-identity=MikroTik
/interface wireless
set wlan2 frequency=2412 band=2ghz-onlyn channel-width=20/40mhz-Ce security-profile=Invitados ssid=MikroTik guest-mode=yes wps-mode=disabled
/ip address add interface=wlan2 address=10.0.0.1/24
```
Ahora creamos la **pool** para la red cliente
```bash
/ip pool add name=cliente-pool ranges=10.10.10.100-10.10.10.120
```
Ahora vamos a configurar el HostsPot y poder configurar el ancho de banda que puede usar los clientes.
```bash
/ip hotspot profile set [ find default=yes ] html-directory=flash/hotspot
/ip hotspot user profile add name=invitados idle-timeout=none keepalive-timeout=2m rate-limit=256k/256k shared-users=unlimited
/ip hotspot add address-pool=invitados-dhcp disabled=no interface=wlan2 name=invitados profile=invitados user-profile=invitados
/ip pool add name=invitados-dhcp ranges=10.0.0.100-10.0.0.120
```
Ahora vamos a configurar el **Firewall** para que permita el trafico de entrada y salida de la red cliente y solo tenga servicio necesarios como el DNS,DHCP, y HTTP/HTTPS.
```bash
/ip firewall filter
add action=accept chain=input comment="Allow established/related connections" connection-state=established,related
add action=accept chain=input comment="Allow ICMP" protocol=icmp
add action=accept chain=input comment="Allow hotspot login" dst-port=80,443 protocol=tcp
add action=accept chain=input comment="Allow DHCP" dst-port=67 protocol=udp
add action=drop chain=input comment="Drop all other input traffic"
add action=accept chain=forward comment="Allow established/related connections" connection-state=established,related
add action=accept chain=forward comment="Allow DNS" dst-port=53 protocol=udp
add action=accept chain=forward comment="Allow DHCP" dst-port=67 protocol=udp
add action=accept chain=forward comment="Allow HTTP and HTTPS" dst-port=80,443 protocol=tcp
add action=drop chain=forward comment="Drop all other forward traffic"
```
## ACTUALIZACIÓN DEL ROUTER
Duration: 0:05:00

### ACTUALIZAR EL ROUTER
Antes de actualizar, realiza una copia de seguridad de la configuración actual del dispositivo.
```bash
/system backup save name=copia_17_02_2023
```
Vamos verificar si existe actualizaciones
```bash
/system package update check-for-updates
```
Y si hay actualizaciones disponibles, descarga los archivos de actualización.
```bash
/system package update download
```
Vamos a instalar la actualización
```bash
/system package update install
```
Después de la actualización, verifica si hay problemas.
```bash
/system routerboard print
/system package print
```
Si todo está funcionando correctamente, borra los archivos de actualización descargados
```bash
/system package update clean
```
