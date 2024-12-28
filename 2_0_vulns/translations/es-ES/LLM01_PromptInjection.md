## LLM01:2025 Inyección de prompt

### Descripción

Una vulnerabilidad de inyección de prompt ocurre cuando los prompts del usuario alteran el comportamiento o la salida del LLM en formas no intencionadas. Estas entradas pueden afectar al modelo incluso si son imperceptibles para los humanos, por lo tanto las inyecciones de prompt no necesitan ser visibles/leíbles para los humanos, siempre y cuando el contenido sea analizado por el modelo.

Las vulnerabilidades de inyección de prompt existen en la forma en que los modelos procesan los prompts, y en cómo la entrada puede forzar al modelo a pasar incorrectamente datos de prompts a otras partes del modelo, causando potencialmente que violen directrices, generen contenido dañino, permitan el acceso no autorizado o influyan en decisiones críticas. Aunque técnicas como la generación aumentada por recuperación (RAG, Retrieval-Augmented Generation) y el fine-tuning tienen como objetivo hacer que los resultados de LLM sean más relevantes y precisos, la investigación muestra que no mitigan completamente las vulnerabilidades de inyección de prompt.

Aunque la inyección de prompt y el "jailbreaking" son conceptos relacionados en la seguridad de LLM, a menudo se utilizan indistintamente. La inyección de prompt implica manipular las respuestas del modelo a través de entradas específicas para alterar su comportamiento, lo que puede incluir eludir medidas de seguridad. "Jailbreaking" es una forma de inyección de prompt en la que el atacante proporciona entradas que causan que el modelo ignore por completo sus protocolos de seguridad. Los desarrolladores pueden incorporar salvaguardas en los prompt de sistema y en la gestión de las entradas para ayudar a mitigar los ataques de inyección de prompt, pero la prevención eficaz del "jailbreaking" requiere actualizaciones continuas del entrenamiento del modelo y sus mecanismos de seguridad

### Tipos de vulnerabilidades de inyección de prompt

#### Inyección de prompt directa
  Las inyecciones de prompt directas se producen cuando la entrada de un prompt de usuario altera directamente el comportamiento del modelo de forma no intencionada o inesperada. La entrada puede ser intencional (es decir, un actor malicioso deliberadamente elabora un prompt para explotar el modelo) o no intencional (es decir, un usuario inadvertidamente proporciona una entrada que desencadena un comportamiento inesperado).

#### Inyección de prompt indirecta
  Las inyecciones de prompt indirectas se producen cuando un LLM acepta entradas de fuentes externas, como sitios web o archivos. El contenido externo puede contener datos que cuando son interpretados por el modelo, alteran el comportamiento del modelo de forma no intencionada o inesperada. Al igual que las inyecciones directas, las indirectas pueden ser intencionadas o no.

La gravedad y la naturaleza del impacto de un ataque de inyección de prompt pueden variar enormemente y dependen en gran medida tanto del contexto de negocio en el que opera el modelo como de la agencia con la que está diseñado. En general, sin embargo, la inyección de prompt puede conducir a resultados no deseados, incluyendo pero no limitado a:

- Divulgación de información sensible
- Revelación de información sensible sobre la infraestructura del sistema de IA o sobre los prompts de sistema
- Manipulación de contenidos que conduzca a salidas incorrectas o sesgadas
- Proveer acceso no autorizado a funciones disponibles para el LLM
- Ejecución de comandos arbitrarios en sistemas conectados
- Manipulación de procesos críticos de toma de decisiones

El auge de la IA multimodal, que procesa múltiples tipos de datos simultáneamente, introduce riesgos únicos de inyección de prompt. Los actores maliciosos podrían explotar las interacciones entre modalidades, como ocultar instrucciones en imágenes que acompañan a un texto benigno. La complejidad de estos sistemas amplía la superficie de ataque. Los modelos multimodales también pueden ser susceptibles de nuevos ataques intermodales difíciles de detectar y mitigar con las técnicas actuales. Las defensas robustas específicas para contextos multimodales constituyen un importante campo de investigación y desarrollo futuro.

### Estrategias de prevención y mitigación

Las vulnerabilidades de inyección de prompt son posibles debido a la naturaleza de la IA generativa. Dada la influencia estocástica en el funcionamiento de los modelos, no está claro si existen métodos infalibles de prevención para la inyección de prompt. Sin embargo, las siguientes medidas pueden mitigar el impacto de las inyecciones de prompt:

#### 1. Restringir el comportamiento del modelo
  Proporcionar instrucciones específicas sobre el rol, capacidades y limitaciones del modelo dentro del prompt de sistema. Aplicar adhesión estricta al contexto, limitando las respuestas a tareas o temas específicos e instruyendo al modelo para que ignore los intentos de modificar las instrucciones base.
#### 2. Definir y validar los formatos de salida esperados
  Especificar formatos de salida claros, solicitar razonamientos detallados y citas de fuentes, y utilizar código determinista para validar la adhesión a estos formatos.
#### 3. Aplicar filtros de entrada y salida
  Definir categorías sensibles y construir reglas para identificar y tratar dichos contenidos. Aplicar filtros semánticos y utilizar la comprobación de cadenas de texto para buscar contenidos no permitidos. Evaluar las respuestas utilizando la tríada RAG: Analizar la relevancia del contexto, el fundamento y la relevancia de la pregunta/respuesta para identificar resultados potencialmente maliciosos.
#### 4. Aplicar control de privilegios y acceso con privilegios mínimos
  Proporcionar a la aplicación sus propios tokens de API para funcionalidad extensible y gestionar estas funciones por código en lugar de proporcionárselas al modelo. Restringir los privilegios de acceso del modelo al mínimo necesario para las operaciones previstas.
#### 5. Requerir la aprobación humana para las acciones de alto riesgo
  Implementar controles de intervención humana (human-in-the-loop) para las operaciones privilegiadas a fin de evitar acciones no autorizadas.
#### 6. Separar e identificar el contenido externo
  Separar y marcar claramente el contenido no confiable para limitar su influencia en los prompts del usuario.
#### 7. Realizar pruebas de adversarios y simulaciones de ataques
  Realizar regularmente pruebas de penetración y simulaciones de ataques, tratando el modelo como un usuario no confiable para comprobar la eficacia de los límites de confianza y los controles de acceso.

### Ejemplos de escenarios de ataque

#### Escenario #1: Inyección directa
  Un atacante inyecta un mensaje en un chatbot de atención al cliente, ordenándole que ignore las directrices anteriores, consulte almacenes de datos privados y envíe correos electrónicos, lo que conduce a un acceso no autorizado y a una escalada de privilegios.
#### Escenario #2: Inyección indirecta
  Un usuario emplea un LLM para resumir una página web que contiene instrucciones ocultas que hacen que el LLM inserte una imagen que enlaza con una URL, lo que conduce a la exfiltración de la conversación privada.
#### Escenario #3: Inyección no intencionada
  Una compañía incluye una instrucción en la descripción de un puesto de trabajo para identificar postulaciones generadas por IA. Un postulante, inconsciente de esta instrucción, utiliza un LLM para optimizar su currículum, activando inadvertidamente la detección de IA.
#### Escenario #4: Influencia intencional del modelo
  Un atacante modifica un documento en un repositorio utilizado por una aplicación RAG. Cuando la consulta de un usuario devuelve el contenido modificado, las instrucciones maliciosas alteran la salida del LLM, generando resultados engañosos.
#### Escenario #5: Inyección de código
  Un atacante explota una vulnerabilidad (CVE-2024-5184) en un asistente de correo electrónico basado en LLM para inyectar prompts maliciosos, permitiendo el acceso a información sensible y la manipulación del contenido del correo electrónico.
#### Escenario #6: División de carga útil (Payload splitting)
  Un atacante carga un currículum con prompts maliciosos divididos. Cuando se utiliza un LLM para evaluar al candidato, los prompts combinados manipulan la respuesta del modelo, dando como resultado una recomendación positiva a pesar del contenido real del currículum.
#### Escenario #7: Inyección multimodal
  Un atacante embebe un prompt malicioso dentro de una imagen que acompaña a un texto benigno. Cuando una IA multimodal procesa la imagen y el texto concurrentemente, el prompt oculto altera el comportamiento del modelo, potencialmente conduciendo a acciones no autorizadas o a la divulgación de información sensible.
#### Escenario #8: Sufijo adversario
  Un atacante añade una cadena de caracteres aparentemente sin sentido al inicio un prompt, que influye en la salida del LLM de forma maliciosa, saltándose las medidas de seguridad.
#### Escenario #9: Ataque Multilingüe/Ofuscado
  Un atacante utiliza múltiples idiomas o codifica instrucciones maliciosas (por ejemplo, utilizando Base64 o emojis) para evadir los filtros y manipular el comportamiento del LLM.

### Enlaces de referencia

1. [ChatGPT Plugin Vulnerabilities - Chat with Code](https://embracethered.com/blog/posts/2023/chatgpt-plugin-vulns-chat-with-code/) **Embrace the Red**
2. [ChatGPT Cross Plugin Request Forgery and Prompt Injection](https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./) **Embrace the Red**
3. [Not what you’ve signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection](https://arxiv.org/pdf/2302.12173.pdf) **Arxiv**
4. [Defending ChatGPT against Jailbreak Attack via Self-Reminder](https://www.researchsquare.com/article/rs-2873090/v1) **Research Square**
5. [Prompt Injection attack against LLM-integrated Applications](https://arxiv.org/abs/2306.05499) **Cornell University**
6. [Inject My PDF: Prompt Injection for your Resume](https://kai-greshake.de/posts/inject-my-pdf) **Kai Greshake**
8. [Not what you’ve signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection](https://arxiv.org/pdf/2302.12173.pdf) **Cornell University**
9. [Threat Modeling LLM Applications](https://aivillage.org/large%20language%20models/threat-modeling-llm/) **AI Village**
10. [Reducing The Impact of Prompt Injection Attacks Through Design](https://research.kudelskisecurity.com/2023/05/25/reducing-the-impact-of-prompt-injection-attacks-through-design/) **Kudelski Security**
11. [Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations (nist.gov)](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-2e2023.pdf)
12. [2407.07403 A Survey of Attacks on Large Vision-Language Models: Resources, Advances, and Future Trends (arxiv.org)](https://arxiv.org/abs/2407.07403)
13. [Exploiting Programmatic Behavior of LLMs: Dual-Use Through Standard Security Attacks](https://ieeexplore.ieee.org/document/10579515)
14. [Universal and Transferable Adversarial Attacks on Aligned Language Models (arxiv.org)](https://arxiv.org/abs/2307.15043)
15. [From ChatGPT to ThreatGPT: Impact of Generative AI in Cybersecurity and Privacy (arxiv.org)](https://arxiv.org/abs/2307.00691)

### Frameworks y taxonomías relacionados

Consultar esta sección para obtener información completa, estrategias de escenarios relacionados con el despliegue de infraestructuras, controles de ambiente aplicados y otras mejores prácticas.

- [AML.T0051.000 - LLM Prompt Injection: Direct](https://atlas.mitre.org/techniques/AML.T0051.000) **MITRE ATLAS**
- [AML.T0051.001 - LLM Prompt Injection: Indirect](https://atlas.mitre.org/techniques/AML.T0051.001) **MITRE ATLAS**
- [AML.T0054 - LLM Jailbreak Injection: Direct](https://atlas.mitre.org/techniques/AML.T0054) **MITRE ATLAS**
