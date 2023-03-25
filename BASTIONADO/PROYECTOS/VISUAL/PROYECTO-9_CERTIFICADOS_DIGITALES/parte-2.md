## PARTE 2 - CERTIFICADO EN WEB SSL

### VIA SIMULADA

En la máquina virtual usada en la parte 1, instala un servidor web y prepáralo para servir una página de prueba. Genera un certificado autofirmado y configura HTTPS. Obtén una captura del error que proporciona el navegador y otra de los datos de tu certificado en el mismo.

Ahora, acude a un sitio web verificado y obtén una captura de los datos de su certificado.

Analiza y compara las diferencias entre ambos en un documento.

#### CERTIFICADO DEL SERVIDOR APACHE CREADO
![CERTIFICADO MIO](/img/CERTIFICADO.png)

#### ERROR DE "NO ES SEGURO" DE MI SERVIDOR
![ERROR MIO](/img/ERROR-AL-ENTRAR.png)
<aside class="negative">
Este error sale ya que el certificado que se ha puesto no es valido, simplemente por no esta validado correctamente como se deberia hacer si quiere un certificado SSL.
</aside>

#### CERTIFICADO VALIDO EN UNA WEB
![VALIDO EN WEB](/img/CERTIFICADO_VALIDO.png)

#### COMPARACIÓN

La creación en el servidor APACHE fue correcto, lo unico que falta es una validación de ese SSL, con la pagina Github esta validado y seguro, con lo cual no sale ningun error.