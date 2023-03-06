# UT3-PC02
## CONTROL DE VERSIONES SEGURA
Vamos a crear un repositorio en la organización para despues podernos conectalo posteriormente remotamente al repositorio que se va crear a continuación.
[REPOSITORIO DE TRABAJO](https://github.com/IES-Rafael-Alberti/G2-AREA_TRABAJO)
### CREAR REPOSITORIO LOCAL
Vamos a crear el repositorio local donde habra un documento para poder identificar el nombre y el grupo de la practica. Vamos añadir el repositorio Git.
![REPOSITORIO_LOCAL](UT3-PC02/img/CREAMOS%20FICHEROS%20Y%20CARPETA.png)
Ahora vamos a configurar el Git para que este la cuenta para nuestro repositorio.
![LOGIN](UT3-PC02/img/CONFIGURACION%20GIT.png)
Ahora vamos añadir el **.git**
![AÑADOR GIT](UT3-PC02/img/CREAMOS%20GIT%20INIT.png)
Ahora vamos añadir el fichero anteriormente  creado con el comando **git add**
![GIT ADD](UT3-PC02/img/GIT%20ADD%20.png)
Ahora añadimos el primer **commit**
![PRIMER COMMIT](UT3-PC02/img/GIT%20COMMIT.png)
### CONECTAMOS GIT LOCAL CON EL REPOSITORIO CREADO EN LA ORGANIZACIÓN
Ahora vamos añadir el git local con el repositorio creado en la organización
![LOCAL](UT3-PC02/img/GITHUB%20REMOTE_01.png)
y ahora vamos usar el comando **git remote -v**
![GIT REMOTE](UT3-PC02/img/GITHUB%20REMOTE_02.png)
y Añadimos ahora un fichero **.md** al nuevo repositorio
![GITHUB ADD](UT3-PC02/img/GITHUB-ADD.png)
Ahora vamos usar el Push para que se suba al git de la organización.
![GITHUB-REPOSITORIO](UT3-PC02/img/GITHUB-PUSH.png)
### CREAR EL GITIGNORE
Ahora Vamos a crear el fichero **.gitignore** y vamos especificar que ni añada archivos con la extensión **.log**.
![GITIGNORE](UT3-PC02/img/GITIGNORE.png)
Ahora añadimos fichero creado anteriormente.
![AÑADIR](UT3-PC02/img/GITIGNORE-COMMIT.png)
y una vez añadido vamos hacer un **push** en el repositorio.
![PUSHGIT](UT3-PC02/img/GITIGNORE-PUSH.png)
### CREAMOS UNA RAMA NUEVA
Ahora vamos usar una rama de trabajo para que se pueda cambiar y no se usa la **main** para los cambios y no afecte cualquier cambio que se haga en esa rama al **main** si no fue aceptada el cambio previamente.
![RAMA](UT3-PC02/img/RAMAS-MARCOS.png)
### CONFIGURAR EL GPG
Ahora vamos a configurar el **GPG** para poder tener una firma y se pueda verificar el commit que se haga.
![FIRMA](UT3-PC02/img/FIRMA.png)
Ahora vamos a poner que clave o frase vamos usar de forma secreta.
![CLAVE](UT3-PC02/img/FIRMA_01.png)
Se terminara el proceso pero aun falta que termina de configurar en nuestra cuenta de **GitHub**
![FIN](UT3-PC02/img/FIRMA_03.png)
Ahora vamos a exportar la clave con **ID** de la clave **GPG** que usaremos.
![EXPORT](UT3-PC02/img/FIRMA_05.png)
Ahora vamos a nuestro perfil de **GITHUB** y vamos a la zona de la **Configuración** y vamos a darle a **SSH Y GPG KEYS**, con lo cual copiamos el Export que nos dio anteriormente.
![GPG HUB](UT3-PC02/img/FIRMA_06.png)
Ahora vamos añadir un documento con lo que nos pedira la firma con la frase anteriormente puesta como clave.
![FIRMAS GIT](UT3-PC02/img/FRIMAS_PRUEBA.png)
Ahora hacemos un **push** en el repositorio.
![GIT FIRMA](UT3-PC02/img/FIRMA-ARRIBa.png)
Y Comprobamos que fue quien firmo y se verifica quien hizo ese documento
![FIRMA HUB](UT3-PC02/img/FIRMA-GITHUB.png)
### GITLEAKS
Ahora vamos a usar **GitLeaks** para detectar y prevenir que contraseñas o claves.
![GITLEAKS](UT3-PC02/img/GITLEAKS_01.png)
Ahora vamos a  crear un fichero llamado **.env** que tendra dentro una clave dentro del fichero.
#### NOTA EN ESTE PASO DA FALLO EL GITLEAKS
Como este paso me da fallo use otra herramienta que detecta que tenga clave secretas, es una herramienta parecida a **gitleaks**.
Para ello vamos a crear un fichero **.env** y lo añadimos y nos saltara los errores o hara un **skip** del fichero, pero aun sigue dando fallo al detecta las claves
![COMMITGIT](UT3-PC02/img/SKIPPED%20GITLEAK.png)
