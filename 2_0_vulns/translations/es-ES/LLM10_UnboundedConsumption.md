## LLM10:2025 Consumo ilimitado

### Descripción

El consumo ilimitado se refiere al proceso en el que un LLM genera resultados basados en prompts o consultas de entrada. La inferencia es una función crítica de los LLM, que implica la aplicación de patrones y conocimientos aprendidos para producir respuestas o predicciones relevantes.

Los ataques diseñados para interrumpir el servicio, agotar los recursos financieros del objetivo o incluso robar propiedad intelectual clonando el comportamiento de un modelo dependen de una clase común de vulnerabilidad de seguridad para tener éxito. El consumo ilimitado se produce cuando una aplicación LLM permite a los usuarios realizar inferencias excesivas y descontroladas, llevando a riesgos como la denegación de servicio (DoS, Denial of Service), pérdidas económicas, robo de modelo y degradación del servicio. Las altas demandas computacionales de los LLM, especialmente en entornos en la nube, los hacen vulnerables a la explotación de recursos y al uso no autorizado.

### Ejemplos comunes de vulnerabilidad

#### 1. Inundación de entrada de longitud variable
  Los atacantes pueden sobrecargar el LLM con numerosas entradas de longitud variable, explotando las ineficiencias de procesamiento. Esto puede agotar los recursos y potencialmente hacer que el sistema no responda, impactando significativamente en la disponibilidad del servicio.
#### 2. Denegación de cartera (DoW, Denial of Wallet)
  Al iniciar un alto volumen de operaciones, los atacantes explotan el modelo de costo por uso de los servicios de IA basados en la nube, llevando a cargas financieras insostenibles para el proveedor y arriesgando a la ruina financiera.
#### 3. Desbordamiento continuo de entradas
  El envío continuo de entradas que exceden la ventana de contexto del LLM puede conducir a un uso excesivo de recursos computacionales, resultando en la degradación del servicio e interrupciones operativas.
#### 4. Consultas de consumo intensivo de recursos
  El envío de consultas inusualmente exigentes que impliquen secuencias complejas o patrones de lenguaje intrincados puede agotar los recursos del sistema, provocando tiempos de procesamiento prolongados y posibles fallos del sistema.
#### 5. Extracción de modelo a través de API
  Los atacantes pueden realizar consultas a la API del modelo utilizando entradas cuidadosamente diseñadas y técnicas de inyección de prompts para recopilar salidas suficientes para replicar un modelo parcial o crear un modelo en la sombra (shadow model). Esto no sólo plantea riesgos de robo de propiedad intelectual, sino que también socava la integridad del modelo original.
#### 6. Replicación funcional de modelo
  Utilizar el modelo objetivo para generar datos de entrenamiento sintéticos puede permitir a los atacantes realizar fine-tuning y lograr otro modelo fundacional, creando un equivalente funcional. Esto evita los métodos tradicionales de extracción basados ​​en consultas, lo que plantea riesgos significativos para los modelos y tecnologías propietarias.
#### 7. Ataques de canal lateral
  Los atacantes malintencionados pueden explotar las técnicas de filtrado de entrada del LLM para ejecutar ataques de canal lateral, obteniendo los pesos del modelo e información de la arquitectura. Esto podría comprometer la seguridad del modelo y conducir a una mayor explotación.

### Estrategias de prevención y mitigación

#### 1. Validación de entradas
  Implementar validación de entrada estricta para garantizar que las entradas no superan los límites de tamaño razonables.
#### 2. Limitar la exposición de Logits y Logprobs
  Restringir u ofuscar la exposición de `logit_bias` y `logprobs` en las respuestas de API. Proporcione sólo la información necesaria sin revelar probabilidades detalladas.
#### 3. Limitación de velocidad
  Aplicar limitación de velocidad y cuotas de usuario para restringir el número de solicitudes que una única entidad de origen puede realizar en un periodo de tiempo determinado.
#### 4. Gestión de la asignación de recursos
  Monitorear y gestionar dinámicamente la asignación de recursos para evitar que un único usuario o solicitud consuma recursos excesivos.
#### 5. Tiempos de espera y limitación de procesamiento
  Establecer tiempos de espera y limitación de procesamiento de las operaciones de alto consumo para evitar un consumo prolongado de recursos.
#### 6. Técnicas de sandbox
  Restringir el acceso del LLM a los recursos de red, servicios internos y APIs.
  - Esto es particularmente importante para todos los escenarios comunes, ya que abarca los riesgos y amenazas internas. Además, gobierna el grado de acceso que la aplicación LLM tiene a datos y recursos, sirviendo así como un mecanismo de control crucial para mitigar o prevenir ataques de canal lateral.
#### 7. Registro, monitoreo y detección de anomalías exhaustivos
  Minitorear continuamente el uso de recursos e implementar registros para detectar y responder a patrones inusuales de consumo de recursos.
#### 8. Marca de agua
  Implementar frameworks de marca de agua (watermarking) para embeber y detectar el uso no autorizado de salidas del LLM.
#### 9. Degradación progresiva
  Diseñar el sistema para que se degrade progresivamente bajo cargas pesadas, manteniendo funcionalidad parcial en lugar de un fallo completo.
#### 10. Limitación de acciones en cola y escalabilidad robusta
  Implementar restricciones en el número de acciones en cola y en el total de acciones, a la vez incorporando escalado dinámico y balance de carga para gestionar demandas variables y asegurar un rendimiento constante del sistema.
#### 11. Entrenamiento en robustez frente a adversarios
  Entrenar modelos para detectar y mitigar consultas de adversarios e intentos de extracción.
#### 12. Filtrado de tokens de fallo
  Construir listas de tokens de fallo (glitch tokens) conocidos y escanear la salida antes de añadirla a la ventana de contexto del modelo.
#### 13. Controles de acceso
  Implementar fuertes controles de acceso, incluyendo control de acceso basado en roles (RBAC, role-based access control) y el principio de mínimo privilegio, para limitar el acceso no autorizado a los repositorios de modelos LLM y ambientes de entrenamiento.
#### 14. Inventario centralizado de modelos de ML
  Utilizar un inventario o registro centralizado de modelos de ML para los modelos utilizados en producción, asegurando una gobernanza y un control de acceso adecuados.
#### 15. Despliegue automatizado de MLOps
  Implementar el despliegue automatizado de MLOps con flujos de trabajo de gobernanza, seguimiento y aprobación para reforzar los controles de acceso y despliegue dentro de la infraestructura.

### Ejemplos de escenarios de ataque

#### Escenario #1: Tamaño de entrada no controlado
  Un atacante envía una entrada inusualmente grande a una aplicación LLM que procesa datos de texto, resultando en un uso excesivo de memoria y carga de CPU, potencialmente colapsando el sistema o ralentizando significativamente el servicio.
#### Escenario #2: Solicitudes repetidas
  Un atacante transmite un alto volumen de solicitudes a la API de LLM, causando un consumo excesivo de recursos computacionales y haciendo que el servicio no esté disponible para usuarios legítimos.
#### Escenario #3: Consultas de consumo intensivo de recursos
  Un atacante crea entradas específicas diseñadas para activar los procesos computacionalmente más costosos del LLM, llevando a un uso prolongado del CPU y a una falla potencial del sistema.
#### Escenario #4: Denegación de cartera
  Un atacante genera operaciones excesivas para explotar el modelo de pago por uso de los servicios de IA basados en la nube, provocando costes insostenibles para el proveedor del servicio.
#### Escenario #5: Replicación funcional de modelo
  Un atacante utiliza la API del LLM para generar datos de entrenamiento sintéticos y realizar fine-tuning para generar otro modelo, creando un equivalente funcional y eludiendo las limitaciones tradicionales de extracción de modelos.
#### Escenario #6: Eludir el filtrado de entrada del sistema
  Un atacante malicioso elude las técnicas de filtrado de entrada y los preámbulos del LLM para realizar un ataque de canal lateral y recuperar información del modelo a un recurso controlado remotamente bajo su control.

### Enlaces de referencia

1. [Proof Pudding (CVE-2019-20634)](https://avidml.org/database/avid-2023-v009/) **AVID** (`moohax` & `monoxgas`)
2. [arXiv:2403.06634 Stealing Part of a Production Language Model](https://arxiv.org/abs/2403.06634) **arXiv**
3. [Runaway LLaMA | How Meta's LLaMA NLP model leaked](https://www.deeplearning.ai/the-batch/how-metas-llama-nlp-model-leaked/): **Deep Learning Blog**
4. [I Know What You See:](https://arxiv.org/pdf/1803.05847.pdf): **Arxiv White Paper**
5. [A Comprehensive Defense Framework Against Model Extraction Attacks](https://ieeexplore.ieee.org/document/10080996): **IEEE**
6. [Alpaca: A Strong, Replicable Instruction-Following Model](https://crfm.stanford.edu/2023/03/13/alpaca.html): **Stanford Center on Research for Foundation Models (CRFM)**
7. [How Watermarking Can Help Mitigate The Potential Risks Of LLMs?](https://www.kdnuggets.com/2023/03/watermarking-help-mitigate-potential-risks-llms.html): **KD Nuggets**
8. [Securing AI Model Weights Preventing Theft and Misuse of Frontier Models](https://www.rand.org/content/dam/rand/pubs/research_reports/RRA2800/RRA2849-1/RAND_RRA2849-1.pdf)
9. [Sponge Examples: Energy-Latency Attacks on Neural Networks: Arxiv White Paper](https://arxiv.org/abs/2006.03463) **arXiv**
10. [Sourcegraph Security Incident on API Limits Manipulation and DoS Attack](https://about.sourcegraph.com/blog/security-update-august-2023) **Sourcegraph**

### Frameworks y taxonomías relacionados

Consultar esta sección para obtener información completa, estrategias de escenarios relacionados con el despliegue de infraestructuras, controles de ambiente aplicados y otras mejores prácticas.

- [MITRE CWE-400: Uncontrolled Resource Consumption](https://cwe.mitre.org/data/definitions/400.html) **MITRE Common Weakness Enumeration**
- [AML.TA0000 ML Model Access: Mitre ATLAS](https://atlas.mitre.org/tactics/AML.TA0000) & [AML.T0024 Exfiltration via ML Inference API](https://atlas.mitre.org/techniques/AML.T0024) **MITRE ATLAS**
- [AML.T0029 - Denial of ML Service](https://atlas.mitre.org/techniques/AML.T0029) **MITRE ATLAS**
- [AML.T0034 - Cost Harvesting](https://atlas.mitre.org/techniques/AML.T0034) **MITRE ATLAS**
- [AML.T0025 - Exfiltration via Cyber Means](https://atlas.mitre.org/techniques/AML.T0025) **MITRE ATLAS**
- [OWASP Machine Learning Security Top Ten - ML05:2023 Model Theft](https://owasp.org/www-project-machine-learning-security-top-10/docs/ML05_2023-Model_Theft.html) **OWASP ML Top 10**
- [API4:2023 - Unrestricted Resource Consumption](https://owasp.org/API-Security/editions/2023/en/0xa4-unrestricted-resource-consumption/) **OWASP Web Application Top 10**
- [OWASP Resource Management](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/) **OWASP Secure Coding Practices**
