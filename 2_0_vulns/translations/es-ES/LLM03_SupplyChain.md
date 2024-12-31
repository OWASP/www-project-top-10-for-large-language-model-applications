## LLM03:2025 Cadena de suministro

### Descripción

Las cadenas de suministro de LLM son susceptibles a diversas vulnerabilidades, que pueden afectar a la integridad de los datos de entrenamiento, los modelos y las plataformas de despliegue. Estos riesgos pueden resultar en salidas sesgadas, brechas de seguridad o fallos del sistema. Mientras que las vulnerabilidades tradicionales de software se enfocan en cuestiones como los defectos de código y las dependencias, en aprendizaje automático los riesgos se extienden también a los modelos preentrenados y datos, ambos provenientes de terceros.

Estos elementos externos pueden manipularse mediante ataques de manipulación o envenenamiento.

La creación de los LLM es una tarea especializada que a menudo depende de modelos de terceros. El auge de los LLM de libre acceso y los nuevos métodos de fine-tuning como "LoRA" (Low-Rank Adaptation) y "PEFT" (Parameter-Efficient Fine-Tuning), especialmente en plataformas como Hugging Face, introducen nuevos riesgos en la cadena de suministro. Finalmente, la emergencia de los LLM en dispositivos aumenta la superficie de ataque y los riesgos de cadena de suministro para las aplicaciones LLM.

Algunos de los riesgos discutidos aquí también se tratan en "LLM04 Envenenamiento de datos y modelo". Esta entrada se enfoca en el aspecto de cadena de suministro de los riesgos.
Se puede encontrar un modelo de amenaza simple [aquí](https://github.com/jsotiro/ThreatModels/blob/main/LLM%20Threats-LLM%20Supply%20Chain.png).

### Ejemplos comunes de riesgo

#### 1. Vulnerabilidades tradicionales de paquetes de terceros
  Tales como componentes desactualizados u obsoletos, que los atacantes pueden explotar para comprometer las aplicaciones LLM. Esto es similar a "A06:2021 – Componentes Vulnerables y Desactualizados" con riesgos incrementados cuando los componentes son utilizados durante el desarrollo o el fine-tuning del modelo.
  (Enlace de referencia: [A06:2021 – Vulnerable and Outdated Components](https://owasp.org/Top10/A06_2021-Vulnerable_and_Outdated_Components/))
#### 2. Riesgos de licenciamiento
  El desarrollo de la IA suele implicar diversas licencias de software y conjuntos de datos, creando riesgos si no se gestiona adecuadamente. Las diferentes licencias de código abierto y de propietarias imponen variados requisitos legales. Las licencias de los conjuntos de datos pueden restringir su uso, distribución o comercialización.
#### 3. Modelos desactualizados u obsoletos
  El uso de modelos desactualizados u obsoletos que ya no se mantienen lleva a problemas de seguridad.
#### 4. Modelos preentrenados vulnerables
  Los modelos son cajas negras binarias y, a diferencia del código abierto, la inspección estática puede ofrecer pocas garantías de seguridad. Los modelos preentrenados vulnerables pueden contener sesgos ocultos, puertas traseras u otras características maliciosas que no han sido identificadas a través de las evaluaciones de seguridad del repositorio de modelos. Los modelos vulnerables pueden ser creados tanto por conjuntos de datos envenenados como por la manipulación directa de modelos mediante técnicas como ROME, también conocida como lobotomización.
#### 5. Procedencia débil de los modelos
  Actualmente no existen garantías sólidas de procedencia en los modelos publicados. Las fichas de modelo y la documentación asociada proporcionan información sobre el modelo y los usuarios confían en ellas, pero no ofrecen garantías sobre el origen del modelo. Un atacante puede comprometer la cuenta de un proveedor en un repositorio de modelos o crear uno similar y combinarlo con técnicas de ingeniería social para comprometer la cadena de suministro de una aplicación LLM.
#### 6. Adaptadores LoRA vulnerables
  LoRA es una popular técnica de fine-tuning que mejora la modularidad al permitir incorporar capas preentrenadas a un LLM existente. El método incrementa la eficiencia pero crea nuevos riesgos, donde un adaptador LoRA malicioso compromete la integridad y seguridad del modelo base preentrenado. Esto puede ocurrir tanto en ambientes colaborativos de fusión de modelos como explotando el soporte para LoRA de plataformas de despliegue de inferencia populares como vLMM y OpenLLM, donde los adaptadores pueden descargarse y aplicarse a un modelo desplegado.
#### 7. Explotar los procesos de desarrollo colaborativo
  La fusión colaborativa de modelos y los servicios de manejo de modelos (por ejemplo, conversiones) alojados en ambientes compartidos pueden ser explotados para introducir vulnerabilidades en modelos compartidos. La fusión de modelos es muy popular en Hugging Face con modelos fusionados encabezando la clasificación de OpenLLM y puede aprovecharse para eludir las revisiones.
#### 8. Vulnerabilidades de cadena de suministro de modelos LLM en dispositivos
  Los modelos LLM en dispositivos aumentan la superficie de ataque del suministro con procesos manufacturados comprometidos y la explotación de las vulnerabilidades del sistema operativo del dispositivo o del firmware para comprometer los modelos. Los atacantes pueden realizar ingeniería inversa y reempaquetar aplicaciones con modelos manipulados.
#### 9. Términos y condiciones y políticas de privacidad de datos poco claras
  La falta de claridad en los términos y condiciones (T&C) y en las políticas de privacidad de datos de los operadores de modelos puede dar lugar a que los datos sensibles de la aplicación se utilicen para el entrenamiento de modelos y a la consiguiente exposición de información sensible. Esto también puede aplicarse a los riesgos derivados del uso de material protegido por derechos de autor por parte del proveedor del modelo.

### Estrategias de prevención y mitigación

1. Investigar cuidadosamente las fuentes de datos y los proveedores, incluidos los T&C y sus políticas de privacidad, recurriendo únicamente a proveedores de confianza. Revisar y auditar regularmente la seguridad y el acceso de los proveedores, asegurándose de que no se produzcan cambios en su postura de seguridad ni en sus T&C.
2. Entender y aplicar las mitigaciones encontradas en el OWASP Top 10 "A06:2021 – Componentes Vulnerables y Desactualizados". Esto incluye escaneo de vulnerabilidades, gestión y parcheado de componentes. En el caso de ambientes de desarrollo con acceso a datos confidenciales, aplique también estos controles en dichos ambientes.
  (Enlace de referencia: [A06:2021 – Vulnerable and Outdated Components](https://owasp.org/Top10/A06_2021-Vulnerable_and_Outdated_Components/))
3. Aplicar "Red Teaming" de IA y evaluaciones exhaustivas al seleccionar un modelo de terceros. Decoding Trust es un ejemplo fiable de punto de referencia (benchmark) de IA para LLM, pero los modelos pueden ajustarse para evadir los puntos de referencia publicados. Utilizar "Red Teaming" de IA extensivo para evaluar el modelo, especialmente en los casos de uso para los que se planea utilizar el modelo.
4. Mantener un inventario actualizado de componentes utilizando una lista de materiales de software (SBOM, Software Bill of Materials) para asegurar que se dispone de un inventario actualizado, preciso y firmado, que impida la manipulación de los paquetes desplegados. Las SBOM pueden utilizarse para detectar y alertar rápidamente sobre nuevas vulnerabilidades de "día cero". Las BOM de IA y las SBOM de aprendizaje automático son un área emergente y se deberían evaluar opciones comenzando con OWASP CycloneDX.
5. Para mitigar los riesgos de licenciamiento de IA, crear un inventario de todos los tipos de licencias implicadas utilizando BOM y realizar auditorías periódicas de todo el software, las herramientas y los conjuntos de datos, asegurando el cumplimiento y la transparencia a través de las BOM. Utilizar herramientas automatizadas de gestión de licencias para la supervisión en tiempo real y entrenar a los equipos en los modelos de licenciamiento. Mantener documentación detallada sobre licenciamiento en las BOM.
6. Utilizar únicamente modelos de fuentes verificables y controles de integridad en modelos de terceros con firmas y hashes de archivos para compensar la falta de una procedencia sólida de los modelos. Similarmente, utilizar firmas de código para el código suministrado externamente.
7. Implementar prácticas estrictas de monitoreo y auditoría de los ambientes colaborativos de desarrollo de modelos para prevenir y detectar rápidamente cualquier abuso. "HuggingFace SF_Convertbot Scanner" es un ejemplo de script automatizado para utilizar.
  (Enlace de referencia: [HuggingFace SF_Convertbot Scanner](https://gist.github.com/rossja/d84a93e5c6b8dd2d4a538aa010b29163))
8. La detección de anomalías y las pruebas de robustez contra adversarios en los modelos y datos suministrados pueden ayudar a detectar la manipulación y el envenenamiento como se discute en "LLM04 Envenenamiento de datos y modelo"; idealmente, esto debería formar parte de los pipelines de MLOps y LLM; sin embargo, estas son técnicas emergentes y pueden ser más fáciles de implementar como parte de los ejercicios de "red teaming".
9. Implementar una política de parches para mitigar los componentes vulnerables o desactualizados. Asegurarse de que la aplicación se basa en una versión actualizada de las API y el modelo subyacente.
10. Cifrar los modelos desplegados en dispositivos de borde con IA utilizando comprobaciones de integridad y utilizar APIs de atestación de proveedores para evitar aplicaciones y modelos manipulados y prescindir de las aplicaciones de firmware no reconocido.

### Ejemplos de escenarios de ataque

#### Escenario #1:  Biblioteca Python vulnerable
  Un atacante explota una biblioteca de Python vulnerable para comprometer una aplicación LLM. Esto sucedió en la primera brecha de datos de Open AI. Los ataques al registro de paquetes de PyPi engañaron a los desarrolladores de modelos para que descargaran una dependencia de PyTorch comprometida con malware en un ambiente de desarrollo de modelos. Un ejemplo más sofisticado de este tipo de ataque es el ataque Shadow Ray al framework Ray AI utilizado por muchos proveedores para administrar infraestructura de IA. En este ataque, se cree que se han explotado cinco vulnerabilidades de forma activa que afectaron a muchos servidores.
#### Escenario #2: Manipulación directa
  Manipulación directa y publicación de un modelo para difundir desinformación. Se trata de un ataque real con PoisonGPT que elude las funciones de seguridad de Hugging Face cambiando directamente los parámetros del modelo.
#### Escenario #3: Fine-tuning de un modelo popular
  Un atacante ajusta un modelo popular de acceso abierto para eliminar funcionalidades clave de seguridad y obtener buenos resultados en un ámbito específico (seguros). El modelo está ajustado para obtener una alta puntuación en las pruebas de seguridad, pero tiene disparadores muy específicos. Lo despliegan en Hugging Face para que las víctimas lo utilicen aprovechando su confianza en las garantías de los puntos de referencia.
#### Escenario #4: Modelos preentrenados
  Un sistema LLM despliega modelos preentrenados de un repositorio ampliamente utilizado sin una verificación exhaustiva. Un modelo comprometido introduce código malicioso, causando salidas sesgadas en ciertos contextos y conduciendo a resultados dañinos o manipulados.
#### Escenario #5: Proveedor externo comprometido
  Un proveedor externo comprometido proporciona un adaptador LoRA vulnerable que se está fusionando con un LLM mediante la fusión de modelos en Hugging Face.
#### Escenario #6: Infiltración en proveedores
  Un atacante se infiltra en un proveedor externo y compromete la producción de un adaptador LoRA destinado a la integración con un LLM alojado en dispositivos, desplegado utilizando frameworks como vLLM u OpenLLM. El adaptador LoRA comprometido se altera sutilmente para incluir vulnerabilidades ocultas y código malicioso. Una vez que este adaptador se fusiona con el LLM, proporciona al atacante un punto de entrada encubierto en el sistema. El código malicioso puede activarse durante las operaciones del modelo, permitiendo al atacante manipular las salidas del LLM.
#### Escenario #7: Ataques CloudBorne y CloudJacking
  Estos ataques se dirigen a infraestructuras en la nube, aprovechando recursos compartidos y vulnerabilidades en las capas de virtualización. CloudBorne involucra explotar vulnerabilidades de firmware en ambientes de nube compartidos, comprometiendo los servidores físicos que alojan instancias virtuales. CloudJacking se refiere al control malicioso o uso indebido de instancias en la nube, lo que potencialmente conduce a un acceso no autorizado a plataformas críticas de despliegue de LLM. Ambos ataques representan riesgos significativos para las cadenas de suministro que dependen de modelos de aprendizaje automático basados en la nube, ya que los entornos comprometidos podrían exponer datos sensibles o facilitar nuevos ataques.
#### Escenario #8: LeftOvers (CVE-2023-4969)
  Expolotación de la fuga de memoria local de GPU mediante LeftOvers para recuperar datos sensibles. Un atacante puede utilizar este ataque para exfiltrar datos sensibles en servidores de producción y estaciones de trabajo o portátiles de desarrollo.	
#### Escenario #9: WizardLM
  Tras la eliminación de WizardLM, un atacante aprovecha el interés por este modelo y publica una versión falsa de este con el mismo nombre pero que contiene malware y puertas traseras.  
#### Escenario #10: Servicio de fusión de modelos/conversión de formatos
  Un atacante escenifica un ataque con un servicio de fusión de modelos o de conversación de formatos para comprometer un modelo de acceso público para inyectar malware. Este es un ataque real publicado por el proveedor HiddenLayer.
#### Escenario #11: Ingeniería inversa de aplicación móvil
  Un atacante aplica ingeniería inversa a una aplicación móvil para reemplazar el modelo con una versión alterada que lleva al usuario a sitios de estafa. Se anima a los usuarios a descargar la aplicación directamente mediante técnicas de ingeniería social. Se trata de un "ataque real a la IA predictiva" que afectó a 116 aplicaciones de Google Play, entre las que se incluyen populares aplicaciones críticas para la seguridad como el reconocimiento de dinero en efectivo, el control parental, la autenticación facial y servicios financieros.
  (Enlace de referencia: [real attack on predictive AI](https://arxiv.org/abs/2006.08131))
#### Escenario #12: Envenenamiento de conjuntos de datos
  Un atacante envenena conjuntos de datos disponibles públicamente para ayudar a crear una puerta trasera al aplicar fine-tuning a los modelos. La puerta trasera favorece sutilmente a ciertas compañías en diferentes mercados.
#### Escenario #13: T&C y política de privacidad
  Un operador de LLM cambia sus T&C y política de privacidad para requerir una opción explícita de no usar datos de aplicaciones para el entrenamiento de modelos, llevando a la memorización de datos sensibles.

### Enlaces de referencia

1. [PoisonGPT: How we hid a lobotomized LLM on Hugging Face to spread fake news](https://blog.mithrilsecurity.io/poisongpt-how-we-hid-a-lobotomized-llm-on-hugging-face-to-spread-fake-news)
2. [Large Language Models On-Device with MediaPipe and TensorFlow Lite](https://developers.googleblog.com/en/large-language-models-on-device-with-mediapipe-and-tensorflow-lite/)
3. [Hijacking Safetensors Conversion on Hugging Face](https://hiddenlayer.com/research/silent-sabotage/)
4. [ML Supply Chain Compromise](https://atlas.mitre.org/techniques/AML.T0010)
5. [Using LoRA Adapters with vLLM](https://docs.vllm.ai/en/latest/models/lora.html)
6. [Removing RLHF Protections in GPT-4 via Fine-Tuning](https://arxiv.org/pdf/2311.05553)
7. [Model Merging with PEFT](https://huggingface.co/blog/peft_merging)
8. [HuggingFace SF_Convertbot Scanner](https://gist.github.com/rossja/d84a93e5c6b8dd2d4a538aa010b29163)
9. [Thousands of servers hacked due to insecurely deployed Ray AI framework](https://www.csoonline.com/article/2075540/thousands-of-servers-hacked-due-to-insecurely-deployed-ray-ai-framework.html)
10. [LeftoverLocals: Listening to LLM responses through leaked GPU local memory](https://blog.trailofbits.com/2024/01/16/leftoverlocals-listening-to-llm-responses-through-leaked-gpu-local-memory/)

### Frameworks y taxonomías relacionados

Consultar esta sección para obtener información completa, estrategias de escenarios relacionados con el despliegue de infraestructuras, controles de ambiente aplicados y otras mejores prácticas.

- [ML Supply Chain Compromise](https://atlas.mitre.org/techniques/AML.T0010) -  **MITRE ATLAS**
