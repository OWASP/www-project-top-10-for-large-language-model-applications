## LLM02:2025 Divulgación de información sensible

### Descripción

La información sensible puede afectar tanto al LLM como a su contexto de aplicación. Esto incluye información personal identificable (PII, Personal Identifiable Information), detalles financieros, registros médicos, datos comerciales confidenciales, credenciales de seguridad y documentos legales. Los modelos propietarios también pueden tener métodos de entrenamiento únicos y código fuente considerado sensible, especialmente en modelos cerrados o fundacionales.

Los LLM, especialmente cuando están integrados en aplicaciones, corren el riesgo de exponer datos sensibles, algoritmos propietarios o detalles confidenciales a través de su salida. Esto puede dar lugar a accesos no autorizados a los datos, violaciones la privacidad y brechas de propiedad intelectual. Los consumidores deben ser conscientes de cómo interactuar de forma segura con los LLM. Deben comprender los riesgos de proporcionar involuntariamente datos sensibles, que más tarde podrían divulgarse en los resultados del modelo.

Para reducir este riesgo, las aplicaciones LLM deben realizar una adecuada limpieza de datos para evitar que los datos de los usuarios entren en el modelo de entrenamiento. Los propietarios de las aplicaciones también deben proporcionar políticas claras de términos de uso, que permitan a los usuarios optar por que sus datos no se incluyan en el modelo de entrenamiento. La adición de restricciones en el prompt de sistema sobre los tipos de datos que el LLM debe devolver puede proporcionar mitigación contra la divulgación de información sensible. Sin embargo, es posible que estas restricciones no siempre se respeten y que se puedan eludir mediante la inyección de prompts u otros métodos.

### Ejemplos comunes de vulnerabilidad

#### 1. Filtración de PII

  La información personal identificable (PII) puede ser revelada durante las interacciones con el LLM.

#### 2. Exposición de algoritmos propietarios

  Las salidas de modelos mal configurados pueden revelar algoritmos o datos propietarios. Revelar datos de entrenamiento puede exponer los modelos a ataques de inversión, en los que los atacantes extraen información sensible o reconstruyen entradas. Por ejemplo, como se demostró en el ataque 'Proof Pudding' (CVE-2019-20634), los datos de entrenamiento divulgados facilitaron la extracción e inversión de modelos, lo que permitió a los atacantes eludir los controles de seguridad en los algoritmos de aprendizaje automático y los filtros de correo electrónico.

#### 3. Divulgación de datos comerciales confidenciales

  Las respuestas generadas podrían incluir inadvertidamente información confidencial del negocio.

### Estrategias de prevención y mitigación

### Saneamiento

#### 1. Integrar técnicas de saneamiento de datos

  Implementar saneamiento de datos para prevenir que los datos de usuario entren en el modelo de entrenamiento. Esto incluye depurar o enmascarar el contenido sensible antes de que se utilice en el entrenamiento.

#### 2. Validación robusta de entrada

  Aplicar métodos estrictos de validación de entrada para detectar y filtrar entradas de datos potencialmente dañinas o sensibles, asegurándose de que no comprometen el modelo.

### Controles de acceso

#### 1. Aplicar controles de acceso estrictos

  Limitar el acceso a datos sensibles basándose en el principio del menor privilegio. Sólo conceder acceso a los datos que sean necesarios para el usuario o proceso específico.

#### 2. Restringir las fuentes de datos

  Limitar el acceso del modelo a fuentes de datos externas y asegurarse de que la orquestación de datos en tiempo de ejecución se gestiona de forma segura para evitar filtraciones de datos involuntarias.

### Técnicas de aprendizaje federado y privacidad

#### 1. Utilizar el aprendizaje federado

  Entrenar modelos utilizando datos descentralizados almacenados en múltiples servidores o dispositivos. Este enfoque minimiza la necesidad de recopilar datos de forma centralizada y reduce los riesgos de exposición.

#### 2. Incorporar privacidad diferencial

  Aplicar técnicas que añadan ruido a los datos o salidas, dificultando a los atacantes la ingeniería inversa de puntos de datos individuales.

### Educación de los usuarios y transparencia

#### 1. Educar a los usuarios sobre el uso seguro de LLM

  Proporcionar orientación en evitar la introducción de información sensible. Ofrecer entrenamiento sobre las mejores prácticas para interactuar con los LLM de forma segura.

#### 2. Asegurar la transparencia en el uso de los datos

  Mantener políticas claras sobre retención, uso y eliminación de datos. Permitir a los usuarios optar por no incluir sus datos en los procesos de entrenamiento.

### Configuración segura del sistema

#### 1. Ocultar el preámbulo del sistema

  Limitar la capacidad de los usuarios para invalidar o acceder a la configuración inicial del sistema, reduciendo el riesgo de exposición a configuraciones internas.

#### 2. Referenciar a las mejores prácticas de seguridad contra la configuración incorrecta

  Seguir guías como "OWASP API8:2023 Security Misconfiguration" para evitar la filtración de información sensible a través de mensajes de error o detalles de configuración.
  (Enlace de referencia: [OWASP API8:2023 Security Misconfiguration](https://owasp.org/API-Security/editions/2023/en/0xa8-security-misconfiguration/))

### Técnicas avanzadas

#### 1. Cifrado homomórfico

  Utilizar cifrado homomórfico para permitir un análisis de datos seguro y aprendizaje automático que preserve la privacidad. Esto asegura la confidencialidad de los datos mientras son procesados por el modelo.

#### 2. Tokenización y redacción

  Implementar tokenización para preprocesar y sanear la información sensible. Técnicas como la búsqueda de patrones (pattern matching) pueden detectar y redactar el contenido confidencial antes de procesarlo.

### Ejemplos de escenarios de ataque

#### Escenario #1: Exposición accidental de datos

  Un usuario recibe una respuesta que contiene los datos personales de otro usuario debido a un saneamiento de datos inadecuado.

#### Escenario #2: Inyección de prompt dirigida

  Un atacante evade los filtros de entrada para extraer información sensible.

#### Escenario #3: Filtración de datos a través de datos de entrenamiento

  La inclusión negligente de datos en el entrenamiento conduce a la divulgación de información sensible.

### Enlaces de referencia

1. [Lessons learned from ChatGPT’s Samsung leak](https://cybernews.com/security/chatgpt-samsung-leak-explained-lessons/): **Cybernews**
2. [AI data leak crisis: New tool prevents company secrets from being fed to ChatGPT](https://www.foxbusiness.com/politics/ai-data-leak-crisis-prevent-company-secrets-chatgpt): **Fox Business**
3. [ChatGPT Spit Out Sensitive Data When Told to Repeat ‘Poem’ Forever](https://www.wired.com/story/chatgpt-poem-forever-security-roundup/): **Wired**
4. [Using Differential Privacy to Build Secure Models](https://neptune.ai/blog/using-differential-privacy-to-build-secure-models-tools-methods-best-practices): **Neptune Blog**
5. [Proof Pudding (CVE-2019-20634)](https://avidml.org/database/avid-2023-v009/) **AVID** (`moohax` & `monoxgas`)

### Frameworks y taxonomías relacionados

Consultar esta sección para obtener información completa, estrategias de escenarios relacionados con el despliegue de infraestructuras, controles de ambiente aplicados y otras mejores prácticas.

- [AML.T0024.000 - Infer Training Data Membership](https://atlas.mitre.org/techniques/AML.T0024.000) **MITRE ATLAS**
- [AML.T0024.001 - Invert ML Model](https://atlas.mitre.org/techniques/AML.T0024.001) **MITRE ATLAS**
- [AML.T0024.002 - Extract ML Model](https://atlas.mitre.org/techniques/AML.T0024.002) **MITRE ATLAS**
