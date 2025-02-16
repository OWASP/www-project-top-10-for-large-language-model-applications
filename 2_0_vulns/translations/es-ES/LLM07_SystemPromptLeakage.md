## LLM07:2025 Filtración de prompts de  sistema

### Descripción

La vulnerabilidad de filtración de prompts de sistema en los LLM se refiere al riesgo de que los prompts de sistema o instrucciones utilizadas para dirigir el comportamiento del modelo puedan también contener información sensible que no se pretendía que fuera descubierta. Los prompts de sistema están diseñados para guiar la salida del modelo basándose en los requisitos de la aplicación, pero pueden contener secretos inadvertidamente. Cuando se descubre, esta información puede utilizarse para facilitar otros ataques.

Es importante entender que el prompt de sistema no debe considerarse un secreto, ni debe utilizarse como control de seguridad. Por lo tanto, los datos sensibles como credenciales, cadenas de conexión, etc. no deben estar contenidos en el lenguaje del prompt de sistema.

Del mismo modo, si un prompt de sistema contiene información que describe diferentes roles y permisos, o datos sensibles como cadenas de conexión o contraseñas, mientras que la divulgación de dicha información puede ser útil, el riesgo fundamental de seguridad no es que estos hayan sido divulgados, es que la aplicación permite eludir una fuerte gestión de sesión y controles de autorización delegando estos al LLM, y que los datos sensibles están siendo almacenados en un lugar donde no deberían estar.

En resumen: la revelación del prompt de sistema en sí no presenta el riesgo real; el riesgo de seguridad reside en los elementos subyacentes, ya sea la revelación de información sensible, la evasión de barreras del sistema, la separación inadecuada de privilegios, etc. Incluso si no se revela el texto exacto, los atacantes que interactúen con el sistema casi con certeza podrán determinar muchas de las barreras de protección y restricciones de formato que están presentes en el lenguaje del prompt de sistema durante el uso de la aplicación, enviando expresiones al modelo y observando los resultados.

### Ejemplos comunes de riesgo

#### 1. Exposición de funcionalidad sensible
  El prompt de sistema de la aplicación puede revelar información sensible o funcionalidad que se pretende mantener confidencial, como arquitectura sensible del sistema, claves de API, credenciales de base de datos o tokens de usuario. Estos pueden ser extraídos o utilizados por los atacantes para obtener acceso no autorizado a la aplicación. Por ejemplo, un prompt de sistema que contenga el tipo de base de datos utilizada para una herramienta podría permitir al atacante adaptar sus ataques a inyecciones SQL sobre ella.
#### 2. Exposición de reglas internas
  El prompt de sistema de la aplicación revela información sobre los procesos internos de toma de decisiones que debería mantenerse confidencial. Esta información permite a los atacantes obtener información sobre cómo funciona la aplicación, lo que podría permitirles explotar debilidades o eludir controles en la aplicación. Por ejemplo - Hay una aplicación bancaria que tiene un chatbot y su sistema puede revelar información como,
    >"El límite de transacciones está establecido en $5000 por día para un usuario. El monto total de préstamo para un usuario es $10000."
  Esta información permite a los atacantes eludir los controles de seguridad de la aplicación, como realizar transacciones por encima del límite establecido o eludir el importe total del préstamo.
#### 3. Revelación de criterios de filtrado
  Un prompt de sistema puede pedir al modelo que filtre o rechace contenido sensible. Por ejemplo, un modelo puede tener un prompt de sistema como,
    >"Si un usuario solicita información sobre otro usuario, responder siempre con 'Lo siento, no puedo atender esa solicitud'".
#### 4. Divulgación de permisos y roles de usuario
  El prompt de sistema podría revelar las estructuras internas de roles o los niveles de permisos de la aplicación. Por ejemplo, un prompt de sistema podría revelar,
    >"El rol de usuario 'Admin' otorga acceso total para modificar los registros de usuario."
  Si los atacantes se enteran de estos permisos basados en roles, podrían buscar un ataque de escalada de privilegios.

### Estrategias de prevención y mitigación

#### 1. Separar datos sensibles de los prompts de sistema
  Evitar embeber cualquier información sensible (por ejemplo, claves de API, claves de autenticación, nombres de bases de datos, roles de usuario, estructura de permisos de la aplicación) directamente en los prompts de sistema. En su lugar, externalizar dicha información a los sistemas a los que el modelo no accede directamente.
###$ 2. Evitar depender de los prompts de sistema para un control estricto de 
#### comportamiento
  Dado que los LLM son susceptibles a otros ataques como inyecciones de prompts que pueden alterar el prompt de sistema, se recomienda evitar el uso de prompts de sistema para controlar el comportamiento del modelo siempre que sea posible. En su lugar, confiar en sistemas externos al LLM para asegurar este comportamiento. Por ejemplo, la detección y prevención de contenido dañino debería realizarse en sistemas externos.
#### 3. Implementar barreras de seguridad
  Implementar un sistema de barreras de seguridad fuera del propio LLM. Aunque entrenar un comportamiento particular en un modelo puede ser efectivo, como por ejemplo entrenarlo para que no revele su prompt de sistema, no es una garantía de que el modelo siempre se adhiera a esto. Un sistema independiente que pueda inspeccionar la salida para determinar si el modelo cumple con las expectativas es preferible a las instrucciones de un prompt de sistema.
###$ 4. Asegurar que los controles de seguridad se aplican independientemente del 
#### LLM
  Controles críticos como la separación de privilegios, verificación de límites de autorización y similares no deben ser delegados al LLM, ya sea a través del prompt de sistema o de otra manera. Estos controles deben ocurrir de manera determinista y auditable, y los LLM no son (actualmente) propicios para ello. En los casos en que un agente esté realizando tareas, si esas tareas requieren diferentes niveles de acceso, se deben utilizar varios agentes, cada uno configurado con la menor cantidad de privilegios necesarios para realizar las tareas deseadas.

### Ejemplos de escenarios de ataque

#### Escenario #1
  Un LLM tiene un prompt de sistema que contiene un conjunto de credenciales utilizadas para una herramienta a la que se le ha dado acceso.  El prompt de sistema es filtrado por un atacante, quien entonces es capaz de usar estas credenciales para otros propósitos.
#### Escenario #2
  Un LLM tiene un prompt de sistema que prohíbe la generación de contenido ofensivo, enlaces externos y ejecución de código. Un atacante extrae este prompt de sistema y luego utiliza un ataque de inyección de prompt para eludir estas instrucciones, facilitando un ataque de ejecución remota de código.

### Enlaces de referencia

1. [SYSTEM PROMPT LEAK](https://x.com/elder_plinius/status/1801393358964994062): Pliny the prompter
2. [Prompt Leak](https://www.prompt.security/vulnerabilities/prompt-leak): Prompt Security
3. [chatgpt_system_prompt](https://github.com/LouisShark/chatgpt_system_prompt): LouisShark
4. [leaked-system-prompts](https://github.com/jujumilk3/leaked-system-prompts): Jujumilk3
5. [OpenAI Advanced Voice Mode System Prompt](https://x.com/Green_terminals/status/1839141326329360579): Green_Terminals

### Frameworks y taxonomías relacionados

Consultar esta sección para obtener información completa, estrategias de escenarios relacionados con el despliegue de infraestructuras, controles de ambiente aplicados y otras mejores prácticas.

- [AML.T0051.000 - LLM Prompt Injection: Direct (Meta Prompt Extraction)](https://atlas.mitre.org/techniques/AML.T0051.000) **MITRE ATLAS**
