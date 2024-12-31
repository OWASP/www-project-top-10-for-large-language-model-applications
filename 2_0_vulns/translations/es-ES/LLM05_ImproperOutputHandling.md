## LLM05:2025 Manejo inadecuado de la salida

### Descripción

El manejo inadecuado de la salida se refiere específicamente a la insuficiente validación, saneamiento y manejo de las salidas generadas por los LLM antes de que sean pasadas a otros componentes y sistemas. Dado que el contenido generado por LLM puede controlarse mediante la introducción de prompts, este comportamiento es similar a proporcionar a los usuarios acceso indirecto a funcionalidad adicional.

El manejo inadecuado de la salida difiere de la sobredependencia en que se ocupa de las salidas generadas por el LLM antes de que sean transferidas a otros sistemas, mientras que la sobredependencia se centra en problemas más amplios relacionados con la dependencia excesiva de la precisión e idoneidad de las salidas del LLM.

La explotación exitosa de una vulnerabilidad de manejo inadecuado de la salida puede resultar en XSS (Cross-Site Scripting) y CSRF (Cross-Site Request Forgery) en navegadores web, así como SSRF (Server-Side Request Forgery), escalada de privilegios o ejecución remota de código en sistemas "backend".

Las siguientes condiciones pueden aumentar el impacto de esta vulnerabilidad:
- La aplicación otorga al LLM privilegios más allá de lo previsto para los usuarios finales, permitiendo la escalada de privilegios o la ejecución remota de código.
- La aplicación es vulnerable a ataques de inyección indirecta de prompts, que podrían permitir a un atacante obtener acceso privilegiado al ambiente de un usuario objetivo.
- Las extensiones de terceros no validan adecuadamente las entradas.
- Falta de codificación de salida adecuada para diferentes contextos (por ejemplo, HTML, JavaScript, SQL).
- Insuficiente monitorización y registro de las salidas de LLM.
- Ausencia de limitación de velocidad o detección de anomalías en el uso de LLM.

### Ejemplos comunes de vulnerabilidad

1. La salida de un LLM se introduce directamente en un intérprete de comandos de sistema operativo o en una función similar como exec o eval, resultando en ejecución remota de código.
2. JavaScript o Markdown es generado por el LLM y devuelto al usuario. El código es entonces interpretado por el navegador, resultando en XSS.
3. Consultas SQL generadas por el LLM se ejecutan sin la parametrización adecuada, dando lugar a inyección SQL.
4. La salida del LLM se utiliza para construir rutas de archivos sin el saneamiento adecuado, resultando potencialmente en vulnerabilidades de salto de directorio (path traversal).
5. El contenido generado por LLM se utiliza en plantillas de correo electrónico sin el escape adecuado, lo que puede dar lugar a ataques de "phishing".

### Estrategias de prevención y mitigación

1. Tratar al modelo como a cualquier otro usuario, adoptando un enfoque de confianza cero, y aplicar una validación de entrada adecuada en las respuestas procedentes del modelo hacia las funciones de "backend".
2. Seguir las directrices de OWASP ASVS (Application Security Verification Standard) para aseguridad una validación y saneamiento de entrada eficaces.
3. Codificar la salida del modelo retornada a los usuarios para mitigar la ejecución no deseada de código mediante JavaScript o Markdown. OWASP ASVS proporciona una guía detallada sobre la codificación de salidas.
4. Implementar una codificación de salida contextual basada en el uso que se le dará a la salida del LLM (por ejemplo, codificación HTML para contenido web, escape SQL para consultas a bases de datos).
5. Utilizar consultas parametrizadas o sentencias preparadas para todas las operaciones de base de datos que involucren salida de un LLM.
6. Emplear Políticas de Seguridad de Contenido (CSP, Content Security Policies) estrictas para mitigar el riesgo de ataques XSS desde contenido generado por LLM.
7. Implementar sistemas robustos de registro y monitoreo para detectar patrones inusuales en las salidas del LLM que puedan indicar intentos de explotación.

### Ejemplos de escenarios de ataque

#### Escenario #1
  Una aplicación utiliza una extensión LLM para generar respuestas para una funcionalidad de chatbot. La extensión también ofrece una serie de funciones administrativas accesibles por otro LLM privilegiado. El LLM de propósito general pasa directamente su respuesta, sin la validación de salida apropiada, a la extensión causando que esta se deshabilite por mantenimiento.
#### Escenario #2
  Un usuario utiliza una herramienta de resumen de sitios web impulsada por un LLM para generar un resumen conciso de un artículo. El sitio web incluye una inyección de prompt indicando al LLM que capture contenido confidencial, ya sea del sitio web o de la conversación del usuario. Desde allí, el LLM puede codificar los datos sensibles y enviarlos, sin ninguna validación o filtrado de salida, a un servidor controlado por el atacante.
#### Escenario #3
  Un LLM permite a los usuarios crear consultas SQL para una base de datos de "backend" a través de una función similar a un chat. Un usuario solicita una consulta para eliminar todas las tablas de la base de datos. Si la consulta creada desde el LLM no se analiza, se eliminarán todas las tablas de la base de datos.
#### Escenario #4
  Una aplicación web utiliza un LLM para generar contenido a partir de prompts de texto del usuario sin saneo de salida. Un atacante podría enviar un prompt maliciosamente diseñado que haga que el LLM devuelva una carga útil de JavaScript no saneada, causando XSS cuando se procesa en el navegador de la víctima. La validación insuficiente de prompts permite este ataque.
#### Escenario #5
  Se utiliza un LLM para generar plantillas dinámicas de correo electrónico para una campaña de marketing. Un atacante manipula el LLM para incluir JavaScript malicioso dentro del contenido del mensaje. Si la aplicación no sanea adecuadamente la salida del LLM, esto podría conducir a ataques XSS en los destinatarios que ven el mensaje en clientes de correo electrónico vulnerables.
#### Escenario #6
  Se utiliza un LLM para generar código a partir de entradas de lenguaje natural en una empresa de software, apuntando a agilizar las tareas de desarrollo. Aunque eficiente, este enfoque corre el riesgo de exponer información sensible, crear métodos inseguros de manejo de datos o introducir vulnerabilidades como la inyección SQL. La IA también puede alucinar con paquetes de software inexistentes, llevando potencialmente a los desarrolladores a descargar recursos infectados con malware. La revisión minuciosa del código y la verificación de los paquetes sugeridos son cruciales para evitar brechas de seguridad, accesos no autorizados y compromisos del sistema.

### Enlaces de referencia

1. [Proof Pudding (CVE-2019-20634)](https://avidml.org/database/avid-2023-v009/) **AVID** (`moohax` & `monoxgas`)
2. [Arbitrary Code Execution](https://security.snyk.io/vuln/SNYK-PYTHON-LANGCHAIN-5411357): **Snyk Security Blog**
3. [ChatGPT Plugin Exploit Explained: From Prompt Injection to Accessing Private Data](https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./): **Embrace The Red**
4. [New prompt injection attack on ChatGPT web version. Markdown images can steal your chat data.](https://systemweakness.com/new-prompt-injection-attack-on-chatgpt-web-version-ef717492c5c2?gi=8daec85e2116): **System Weakness**
5. [Don’t blindly trust LLM responses. Threats to chatbots](https://embracethered.com/blog/posts/2023/ai-injections-threats-context-matters/): **Embrace The Red**
6. [Threat Modeling LLM Applications](https://aivillage.org/large%20language%20models/threat-modeling-llm/): **AI Village**
7. [OWASP ASVS - 5 Validation, Sanitization and Encoding](https://owasp-aasvs4.readthedocs.io/en/latest/V5.html#validation-sanitization-and-encoding): **OWASP AASVS**
8. [AI hallucinates software packages and devs download them – even if potentially poisoned with malware](https://www.theregister.com/2024/03/28/ai_bots_hallucinate_software_packages/) **Theregiste**
