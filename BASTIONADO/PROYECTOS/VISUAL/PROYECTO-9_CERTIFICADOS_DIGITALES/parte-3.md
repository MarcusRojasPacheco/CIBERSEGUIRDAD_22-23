## PARTE 3 - ANALIZAR CERTIFICADOS

### VIA SIMULADA
Analiza el certificado válido del sitio web de la parte 2 en un servicio como [SSL Labs](https://www.ssllabs.com/ssltest/) y explica, en base a los resultados, los motivos que llevan a verificarlo como válido.

Luego, localiza tres certificados erróneos de [diferente tipo](https://www.redeszone.net/tutoriales/redes-cable/evitar-errores-ssl-navegador/) en sitios web. Analízalos también usando un servicio y explica los motivos que llevan a verificarlos como no válidos.

#### COMPROBAR EL CERTIFICADO DEL GITHUB
![GIT-HUB-CERT](/img/SSL-GITHUB.png)
<aside class="negative">
El certificado de GitHub es valido ya que ha sido emitido por la <a href="https://firmaelectronica.gob.es/Home/Empresas/Autoridades-Certificacion.html">AC</a> con lo que cumple con los estandares de la seguridad para una comunicación segura en la web
</aside>

#### COMPROBAR EL CERTIFICADO *www.kamikaze.com*
![CERTIFICADO F](/img/CERTIFICADO_F.png)
<aside class="negative">
Este servidor solo es compatible con la versión 2 de SSL y es obsoleto y puede usarse contra TLS haciendo un <a href="https://es.wikipedia.org/wiki/Ataque_DROWN">Drown Attack</a>.
Tambien es vulvenrable al <a href="https://es.wikipedia.org/wiki/Ataque_POODLE">Poodle Attack</a>, tambien vulnerable a una vulnerabilidad de Open SSL y de la vulnerabilidad <a href="https://www.incibe-cert.es/alerta-temprana/avisos-seguridad/vulnerabilidades-openssl-20160504">CVE-2016-2107</a>, tambien el servidor acepta cifrado RC4, pero unicamente en protocolos mas antiguos y el servidor es compatible con TLS 1.0 y TLS 1.1 con lo cual se recomienda que se use versiones mas recientes para evitar ataques vulnerables.
</aside>

#### COMPROBAR EL CERTIFICADO *getherautos.com*
![CERTIFICADO F](/img/CERTIFICADO_T.png)
<aside class="negative">
Este servidor su certificado no es confiable, el servidor es compatible con la versión TLS 1.1 y es compatible con TLS 1.3, es recomendable que solo sea compatible con 1.3, ya que evita vulnerabildiad de la versiones antiguas.
</aside>

#### COMPROBAR EL CERTIFICADO *adr.lojackgis.com.ar*
![CERTIFICADO F](/img/CERTIFICADO_T02.png)
<aside class="negative">
Este servidor no tiene un certificado no confiable y tiene una vulnerabilidad que puede tener un ataque 
<a href="https://es.wikipedia.org/wiki/Ataque_POODLE">Poodle Attack</a>, tambien el servidor acepta cifrado RC4, pero unicamente en protocolos mas antiguos y el servidor es compatible con TLS 1.0 y TLS 1.1 con lo cual se recomienda que se use versiones mas recientes para evitar ataques vulnerables, y admite parametros de claves <a href="https://es.wikipedia.org/wiki/Diffie-Hellman">Deffie Hellman</a> pero solo debiles, se recomienda que sea mas fuertes o un nivel mas complejo.
</aside>