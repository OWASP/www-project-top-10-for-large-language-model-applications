## LLM06:2025 Agencia excesiva

### Descripción

A un sistema basado en LLM a menudo se le concede un grado de agencia por parte de su desarrollador: la capacidad de llamar a funciones o interactuar con otros sistemas a través de extensiones (a veces denominadas herramientas, skills o plugins por diferentes vendedores) para llevar a cabo acciones en respuesta a un prompt. La decisión sobre qué extensión invocar también puede delegarse a un "agente" LLM para que la determine dinámicamente basándose en el prompt de entrada o la salida del LLM. Los sistemas basados en agentes suelen realizar llamadas repetidas a un LLM utilizando los resultados de invocaciones previas para fundamentar y dirigir las invocaciones posteriores.

La agencia excesiva es la vulnerabilidad que permite realizar acciones dañinas en respuesta a salidas inesperadas, ambiguas o manipuladas de un LLM, independientemente de lo que esté causando el mal funcionamiento del LLM. Los desencadenantes comunes incluyen:

* alucinación/confabulación causada por prompts benignos mal diseñadas, o simplemente un modelo de mal rendimiento;
* inyección directa/indirecta de prompt por parte de un usuario malicioso, una invocación previa de una extensión maliciosa/comprometida, o (en sistemas multi-agente/colaborativos) otro agente malicioso/comprometido.

La causa raíz de la agencia excesiva es típicamente una o más de las siguientes:

* funcionalidad excesiva
* permisos excesivos;
* autonomía excesiva.

La agencia excesiva puede conducir a una amplia gama de impactos a través del espectro de confidencialidad, integridad y disponibilidad, y depende de con qué sistemas una aplicación basada en LLM pueda interactuar.

Nota: La agencia excesiva difiere del manejo inseguro de salidas, que se refiere a un escrutinio insuficiente de las salidas del LLM.

### Ejemplos comunes de riesgo

#### 1. Funcionalidad excesiva

  Un agente LLM tiene acceso a extensiones que incluyen funciones que no son necesarias para la operativa prevista del sistema. Por ejemplo, un desarrollador necesita conceder a un agente LLM la capacidad de leer documentos de un repositorio, pero la extensión de terceros que elige utilizar también incluye la capacidad de modificar y borrar documentos.

#### 2. Funcionalidad excesiva

  Una extensión puede haber sido probada durante una fase de desarrollo y abandonada en favor de una alternativa mejor, pero el plugin original permanece disponible para el agente LLM.

#### 3. Funcionalidad excesiva

  Un plugin LLM con funcionalidad abierta falla en filtrar apropiadamente las instrucciones de entrada para comandos fuera de lo necesario para la operativa de la aplicación. Por ejemplo, una extensión para ejecutar un comando de sistema operativo específico falla en prevenir adecuadamente que se ejecuten otros comandos.

#### 4. Permisos excesivos

  Una extensión LLM tiene permisos en sistemas "downstream" (más adentrados en la arquitectura) que no son necesarios para la operativa prevista de la aplicación. Por ejemplo, una extensión destinada a leer datos se conecta a un servidor de base de datos utilizando una identidad que no sólo tiene permisos para la operación SELECT, sino también para UPDATE, INSERT y DELETE.

#### 5. Permisos excesivos

  Una extensión LLM diseñada para realizar operaciones en el contexto de un usuario individual accede a sistemas "downstream" con una identidad genérica con altos privilegios. Por ejemplo, una extensión para leer el almacén de documentos del usuario actual se conecta al repositorio de documentos con una cuenta privilegiada que tiene acceso a archivos pertenecientes a todos los usuarios.

#### 6. Autonomía excesiva

  Una aplicación basada en LLM o extensión falla al verificar y aprobar independientemente acciones de alto impacto. Por ejemplo, una extensión que permite eliminar los documentos de un usuario realiza eliminaciones sin ninguna confirmación por parte del usuario.

### Estrategias de prevención y mitigación

Las siguientes acciones pueden prevenir la agencia excesiva:

#### 1. Minimizar extensiones

  Limitar las extensiones que los agentes LLM tienen permitido llamar al mínimo necesario. Por ejemplo, si un sistema basado en LLM no requiere la capacidad de obtener el contenido de una URL, dicha extensión no debe ofrecerse al agente LLM.

#### 2. Minimizar la funcionalidad de las extensiones

  Limitar las funciones que se implementan en las extensiones LLM al mínimo necesario. Por ejemplo, una extensión que accede al buzón de correo de un usuario para resumir los mensajes de correo electrónico podría requerir únicamente la capacidad de leer mensajes, por lo que la extensión no debe contener otras funcionalidades como borrar o enviar mensajes.

#### 3. Evitar extensiones con funcionalidad abierta

  Evitar el uso de extensiones con funcionalidad abierta siempre que sea posible (por ejemplo, ejecutar un comando de sistema operativo, obtener una URL, etc.) y utilizar extensiones con una funcionalidad más granular. Por ejemplo, una aplicación basada en LLM puede necesitar escribir algún resultado en un archivo. Si esto se implementara utilizando una extensión para ejecutar un comando de sistema operativo, el alcance de las acciones no deseadas sería muy amplio (podría ejecutarse cualquier otro comando). Una alternativa más segura sería construir una extensión específica para escribir archivos que sólo implemente esa funcionalidad específica.

#### 4. Minimizar los permisos de las extensiones

  Limitar los permisos que se conceden a las extensiones LLM para con otros sistemas al mínimo necesario para limitar el alcance de acciones no deseadas. Por ejemplo, un agente LLM que utiliza una base de datos de productos para hacer recomendaciones de compra a un cliente puede que sólo necesite acceso de lectura a una tabla "productos"; no debería tener acceso a otras tablas, ni la capacidad de insertar, actualizar o borrar registros. Esto debe cumplirse aplicando los permisos de base de datos apropiados para la identidad que la extensión LLM utiliza al conectarse a la base de datos.

#### 5. Ejecutar extensiones en el contexto del usuario

  Realizar el seguimiento de la autorización de usuarios y de sus alcances de seguridad para asegurar que las acciones realizadas en nombre de un usuario se ejecuten en sistemas "downstream" en el contexto de ese usuario específico y con los privilegios mínimos necesarios. Por ejemplo, una extensión LLM que lea el repositorio de código de un usuario debería requerir que el usuario se autentique mediante OAuth y con el alcance mínimo necesario.

#### 6. Requerir la aprobación del usuario

  Utilizar control de intervención humana (human-in-the-loop) para requerir que un humano apruebe las acciones de alto impacto antes de que se lleven a cabo. Esto puede implementarse en un sistema "downstream" (fuera del alcance de la aplicación LLM) o dentro de la propia extensión LLM. Por ejemplo, una aplicación basada en LLM que crea y publica contenido en redes sociales en nombre de un usuario debería incluir una rutina de aprobación del usuario dentro de la extensión que implementa la operación "publicar".

#### 7. Mediación completa

  Implementar autorización en los sistemas "downstream" en lugar de depender de un LLM para decidir si una acción está permitida o no. Aplique el principio de mediación completa para que todas las solicitudes realizadas a los sistemas "downstream" a través de extensiones se validen con respecto a las políticas de seguridad.

#### 8. Sanear las entradas y salidas del LLM

  Seguir las mejores prácticas de codificación segura, como aplicar las recomendaciones de OWASP en ASVS (Application Security Verification Standard), con un enfoque particularmente fuerte en el saneamiento de entradas. Utilizar pruebas estáticas de seguridad de aplicaciones (SAST, Static Application Security Testing) y pruebas dinámicas e interactivas de seguridad aplicaciones (DAST/IAST, Dynamic/Interactive Application Security Testing) en los procesos de desarrollo.

Las siguientes opciones no evitarán la agencia excesiva, pero pueden limitar el nivel de daño causado:

* Registrar y monitorizar la actividad de las extensiones LLM y los sistemas "downstream" para identificar dónde se están produciendo acciones no deseadas y responder en consecuencia.
* Implementar un límite de velocidad para reducir el número de acciones no deseadas que pueden tener lugar en un periodo de tiempo determinado, aumentando la oportunidad de descubrir acciones no deseadas mediante la monitorización antes de que se produzcan daños significativos.

### Ejemplos de escenarios de ataque

Una aplicación de asistente personal basada en LLM tiene acceso al buzón de correo de una persona a través de una extensión con el fin de resumir el contenido de los correos electrónicos entrantes. Para lograr esta funcionalidad, la extensión requiere la capacidad de leer mensajes, sin embargo, el plugin que el desarrollador del sistema ha decidido utilizar también contiene funciones para enviar mensajes. Además, la aplicación es vulnerable a un ataque de inyección indirecta de prompts, mediante el cual un correo electrónico entrante malicioso engaña al LLM para que ordene al agente escanear la bandeja de entrada del usuario en busca de información sensible y reenviarla a la dirección de correo electrónico del atacante. Esto puede evitarse:

* eliminando funcionalidad excesiva mediante el uso de una extensión que sólo implemente capacidades de lectura de correo,
* eliminando permisos excesivos mediante la autenticación del usuario en el servicio de correo electrónico a través de una sesión OAuth con un alcance de sólo lectura, y/o
* eliminando autonomía excesiva mediante la exigencia de que el usuario manualmente revise y presione "enviar" en cada correo electrónico redactado por la extensión LLM.

Alternativamente, el daño causado podría reducirse implementando una limitación de velocidad en la interfaz de envío de correo.

### Enlaces de referencia

1. [Slack AI data exfil from private channels](https://promptarmor.substack.com/p/slack-ai-data-exfiltration-from-private): **PromptArmor**
2. [Rogue Agents: Stop AI From Misusing Your APIs](https://www.twilio.com/en-us/blog/rogue-ai-agents-secure-your-apis): **Twilio**
3. [Embrace the Red: Confused Deputy Problem](https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./): **Embrace The Red**
4. [NeMo-Guardrails: Interface guidelines](https://github.com/NVIDIA/NeMo-Guardrails/blob/main/docs/security/guidelines.md): **NVIDIA Github**
6. [Simon Willison: Dual LLM Pattern](https://simonwillison.net/2023/Apr/25/dual-llm-pattern/): **Simon Willison**
