## LLM04: Envenenamiento de datos y modelo

### Descripción

El envenenamiento de datos se produce cuando los datos de preentrenamiento, fine-tuning o embeddings se manipulan para introducir vulnerabilidades, puertas traseras o sesgos. Esta manipulación puede comprometer la seguridad, el rendimiento o el comportamiento ético del modelo, provocando salidas dañinas o capacidades deterioradas. Los riesgos más comunes incluyen la degradación del rendimiento del modelo, el contenido sesgado o tóxico y la explotación de sistemas más adentrados en la arquitectura.

El envenenamiento de datos puede dirigirse a diferentes etapas del ciclo de vida de los LLM, incluido el preentrenamiento (aprendizaje a partir de datos generales), el fine-tuning (adaptación de modelos a tareas específicas) y embedding (conversión de texto en vectores numéricos). Comprender estas etapas ayuda a identificar dónde pueden originarse las vulnerabilidades. El envenenamiento de datos se considera un ataque a la integridad, ya que la manipulación de los datos de entrenamiento afecta a la capacidad del modelo para realizar predicciones precisas. Los riesgos son especialmente altos con fuentes de datos externas, que pueden contener contenido no verificado o malicioso.

Además, los modelos distribuidos a través de repositorios compartidos o plataformas de código abierto pueden conllevar riesgos que van más allá del envenenamiento de datos, como el malware embebido mediante técnicas como el "pickling" malicioso, que puede ejecutar código dañino cuando se carga el modelo. También, hay que tener en cuenta que el envenenamiento puede permitir la implementación de una puerta trasera. Estas puertas traseras pueden dejar intacto el comportamiento del modelo hasta que un determinado desencadenante provoque un cambio. Esto puede hacer que tales cambios sean difíciles de probar y detectar, creando en efecto la oportunidad de que un modelo se convierta en un "agente durmiente".

### Ejemplos comunes de vulnerabilidad

1. Actores maliciosos introducen datos dañinos durante el entrenamiento, lo que provoca resultados sesgados. Técnicas como "Split-View Data Poisoning" o "Frontrunning Poisoning" explotan la dinámica de entrenamiento del modelo para conseguirlo.
  (Enlace de referencia: [Split-View Data Poisoning](https://github.com/GangGreenTemperTatum/speaking/blob/main/dc604/hacker-summer-camp-23/Ads%20_%20Poisoning%20Web%20Training%20Datasets%20_%20Flow%20Diagram%20-%20Exploit%201%20Split-View%20Data%20Poisoning.jpeg))
  (Enlace de referencia: [Frontrunning Poisoning](https://github.com/GangGreenTemperTatum/speaking/blob/main/dc604/hacker-summer-camp-23/Ads%20_%20Poisoning%20Web%20Training%20Datasets%20_%20Flow%20Diagram%20-%20Exploit%202%20Frontrunning%20Data%20Poisoning.jpeg))
2. Atacantes pueden inyectar contenido dañino directamente en el proceso de entrenamiento, comprometiendo la calidad de salida del modelo.
3. Usuarios inyectan, sin saberlo, información sensible o propietaria durante las interacciones, que podría ser expuesta en resultados posteriores.
4. Los datos de entrenamiento no verificados aumentan el riesgo de salidas sesgadas o erróneas.
5. La falta de restricciones de acceso a los recursos puede permitir la ingesta de datos inseguros, resultando en salidas sesgadas.

### Estrategias de prevención y mitigación

1. Rastrear los orígenes y las transformaciones de los datos utilizando herramientas como OWASP CycloneDX o ML-BOM. Verificar la legitimidad de los datos durante todas las etapas de desarrollo del modelo.
2. Investigar rigurosamente a los proveedores de datos y validar las salidas del modelo contra fuentes confiables para detectar signos de envenenamiento.
3. Implementar aislamiento estricto para limitar la exposición del modelo a fuentes de datos no verificadas. Utilizar técnicas de detección de anomalías para filtrar los datos provistos por adversarios.
4. Adaptar modelos a distintos casos de uso utilizando conjuntos de datos específicos para fine-tuning. Esto ayuda a producir salidas más precisas basadas en objetivos definidos.
5. Asegurar suficientes controles de infraestructura para evitar que el modelo acceda a fuentes de datos no deseadas.
6. Utilizar control de versiones de datos (DVC, data version control) para rastrear los cambios en los conjuntos de datos y detectar manipulaciones. El control de versiones es crucial para mantener la integridad del modelo.
7. Almacenar la información suministrada por el usuario en una base de datos vectorial, permitiendo realizar ajustes sin necesidad de volver a entrenar todo el modelo.
8. Probar la robustez del modelo con campañas de "red team" y técnicas adversarias, como el aprendizaje federado, para minimizar el impacto de perturbaciones de los datos.
9. Monitorear la pérdida en el entrenamiento (training loss) y analizar el comportamiento del modelo para detectar signos de envenenamiento. Utilizar umbrales para detectar resultados anómalos.
10. Durante la inferencia, integrar técnicas de generación aumentada por recuperación (RAG, Retrieval-Augmented Generation) y de conexión a tierra (grounding) para reducir el riesgo de alucinaciones.

### Ejemplos de escenarios de ataque

#### Escenario #1
  Un atacante sesga los resultados del modelo manipulando los datos de entrenamiento o utilizando técnicas de inyección de prompts, difundiendo desinformación.
#### Escenario #2
  Los datos tóxicos sin el filtrado apropiado pueden conducir a salidas dañinas o sesgadas, propagando información peligrosa.
#### Escenario #3
  Un actor malicioso o competidor crea documentos falsificados para el entrenamiento, resultando en salidas del modelo que reflejan estas inexactitudes.
#### Escenario #4
  Un filtrado inadecuado permite a un atacante insertar datos engañosos a través de una inyección de prompt, llevando a resultados comprometidos.
#### Escenario #5
  Un atacante utiliza técnicas de envenenamiento para insertar un disparador de puerta trasera en el modelo. Esto podría dejarlo abierto a la evasión de autenticación, exfiltración de datos o ejecución de comandos ocultos.

### Enlaces de referencia

1. [How data poisoning attacks corrupt machine learning models](https://www.csoonline.com/article/3613932/how-data-poisoning-attacks-corrupt-machine-learning-models.html): **CSO Online**
2. [MITRE ATLAS (framework) Tay Poisoning](https://atlas.mitre.org/studies/AML.CS0009/): **MITRE ATLAS**
3. [PoisonGPT: How we hid a lobotomized LLM on Hugging Face to spread fake news](https://blog.mithrilsecurity.io/poisongpt-how-we-hid-a-lobotomized-llm-on-hugging-face-to-spread-fake-news/): **Mithril Security**
4. [Poisoning Language Models During Instruction](https://arxiv.org/abs/2305.00944): **Arxiv White Paper 2305.00944**
5. [Poisoning Web-Scale Training Datasets - Nicholas Carlini | Stanford MLSys #75](https://www.youtube.com/watch?v=h9jf1ikcGyk): **Stanford MLSys Seminars YouTube Video**
6. [ML Model Repositories: The Next Big Supply Chain Attack Target](https://www.darkreading.com/cloud-security/ml-model-repositories-next-big-supply-chain-attack-target) **OffSecML**
7. [Data Scientists Targeted by Malicious Hugging Face ML Models with Silent Backdoor](https://jfrog.com/blog/data-scientists-targeted-by-malicious-hugging-face-ml-models-with-silent-backdoor/) **JFrog**
8. [Backdoor Attacks on Language Models](https://towardsdatascience.com/backdoor-attacks-on-language-models-can-we-trust-our-models-weights-73108f9dcb1f): **Towards Data Science**
9. [Never a dill moment: Exploiting machine learning pickle files](https://blog.trailofbits.com/2021/03/15/never-a-dill-moment-exploiting-machine-learning-pickle-files/) **TrailofBits**
10. [arXiv:2401.05566 Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training](https://www.anthropic.com/news/sleeper-agents-training-deceptive-llms-that-persist-through-safety-training) **Anthropic (arXiv)**
11. [Backdoor Attacks on AI Models](https://www.cobalt.io/blog/backdoor-attacks-on-ai-models) **Cobalt**

### Frameworks y taxonomías relacionados

Consultar esta sección para obtener información completa, estrategias de escenarios relacionados con el despliegue de infraestructuras, controles de ambiente aplicados y otras mejores prácticas.

- [AML.T0018 | Backdoor ML Model](https://atlas.mitre.org/techniques/AML.T0018) **MITRE ATLAS**
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework): Strategies for ensuring AI integrity. **NIST**
