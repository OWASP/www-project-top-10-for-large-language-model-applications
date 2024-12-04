## LLM09:2025 Desinformación 

### Descripción

La desinformación desde los LLM supone una vulnerabilidad base para las aplicaciones que confían en estos modelos. La desinformación se produce cuando los LLM producen información falsa o errónea que parece creíble. Esta vulnerabilidad puede provocar brechas de seguridad, daños a la reputación y responsabilidad legal.

Una de las principales causas de la desinformación es la alucinación, es decir, cuando el LLM genera contenido que parece preciso pero que es inventado. Las alucinaciones se producen cuando los LLM llenan los vacíos en sus datos de entrenamiento utilizando patrones estadísticos, sin comprender realmente el contenido. Como resultado, el modelo puede producir respuestas que parecen correctas pero que son completamente infundadas. Aunque las alucinaciones son una fuente importante de desinformación, no son la única causa; los sesgos introducidos por los datos de entrenamiento e información incompleta también pueden contribuir.

Un problema relacionado es la sobredependencia. La sobredependencia ocurre cuando los usuarios depositan una confianza excesiva en el contenido generado por un LLM, sin verificar su exactitud. Este exceso de confianza agrava el impacto de la desinformación, ya que los usuarios pueden integrar datos incorrectos en decisiones o procesos críticos sin un escrutinio adecuado.

### Ejemplos comunes de riesgo

#### 1. Inexactitudes fácticas
  El modelo produce afirmaciones incorrectas, llevando a los usuarios a tomar decisiones basadas en información falsa. Por ejemplo, el chatbot de Air Canada proporcionó información errónea a los viajeros, lo que provocó interrupciones operativas y complicaciones legales. Como resultado, la aerolínea fue demandada con éxito.
  (Enlace de referencia: [BBC](https://www.bbc.com/travel/article/20240222-air-canada-chatbot-misinformation-what-travellers-should-know))
#### 2. Afirmaciones sin fundamento
  El modelo genera afirmaciones sin fundamento, que pueden ser especialmente perjudiciales en contextos delicados como la asistencia médica o procedimientos legales. Por ejemplo, ChatGPT fabricó casos legales falsos, lo que provocó importantes problemas en tribunales.
  (Enlace de referencia: [LegalDive](https://www.legaldive.com/news/chatgpt-fake-legal-cases-generative-ai-hallucinations/651557/))
#### 3. Tergiversación de experiencia
  El modelo da la ilusión de entender temas complejos, engañando a los usuarios sobre su nivel de experiencia. Por ejemplo, se ha descubierto que los chatbots tergiversan la complejidad de los temas relacionados con la salud, sugiriendo incertidumbre donde no la hay, llevando a los usuarios a creer erróneamente que tratamientos no respaldados aún estaban en debate.
  (Enlace de referencia: [KFF](https://www.kff.org/health-misinformation-monitor/volume-05/))
#### 4. Generación de código inseguro
  El modelo sugiere bibliotecas de código inseguras o inexistentes, que pueden introducir vulnerabilidades cuando se integran en sistemas de software. Por ejemplo, los LLM proponen el uso de bibliotecas de terceros inseguras, que, si se confía en ellas sin verificación, conducen a riesgos de seguridad.
  (Enlace de referencia: [Lasso](https://www.lasso.security/blog/ai-package-hallucinations))

### Estrategias de prevención y mitigación

#### 1. Generación aumentada por recuperación
  Utilizar la generación mejorada por recuperación para aumentar la fiabilidad de las salidas del modelo recuperando información relevante y verificada de bases de datos externas de confianza durante la generación de la respuesta. Esto ayuda a mitigar el riesgo de alucinaciones y desinformación.
#### 2. Fine-tuning de modelo
  Mejorar el modelo con fine-tuning o "embeddings" para mejorar la calidad de los resultados. Técnicas como el ajuste eficiente de parámetros (PET, parameter-efficient tuning) y el "chain-of-thought prompting" (CoT) pueden ayudar a reducir la incidencia de la desinformación.
#### 3. Verificación cruzada y supervisión humana
  Incentivar a los usuarios a verificar los resultados de los LLM con fuentes externas confiables para asegurar la precisión de la información. Implementar procesos de supervisión humana y verificación de datos, especialmente para información crítica o sensible. Asegurar que los revisores humanos están adecuadamente entrenados para evitar la confianza excesiva en los contenidos generados por IA.
#### 4. Mecanismos de validación automática
  Implementar herramientas y procesos para validar automáticamente las salidas clave, especialmente las procedentes de ambientes de alto riesgo.
#### 5. Comunicación de riesgos
  Identificar los riesgos y los posibles daños asociados con el contenido generado por un LLM, luego comunicar claramente estos riesgos y limitaciones a los usuarios, incluyendo el potencial de desinformación.
#### 6. Prácticas de codificación segura
  Establecer prácticas de codificación segura para evitar la integración de vulnerabilidades debido a sugerencias de código incorrectas.
#### 7. Diseño de interfaces de usuario
  Diseñar APIs e interfaces de usuario que fomenten el uso responsable de los LLM, como la integración de filtros de contenido, el etiquetado claro del contenido generado por IA y la información a los usuarios sobre las limitaciones de fiabilidad y precisión. Ser específico sobre las limitaciones del campo de uso previsto.
#### 8. Capacitación y educación
  Proporcionar capacitación completa a los usuarios sobre las limitaciones de los LLM, la importancia de la verificación independiente de los contenidos generados y la necesidad de pensamiento crítico. En contextos específicos, ofrecer capacitación específica del dominio para garantizar que los usuarios puedan evaluar eficazmente los resultados del LLM dentro de su campo de especialización.

### Ejemplos de escenarios de ataque

#### Escenario #1
  Atacantes experimentan con asistentes de codificación populares para encontrar nombres de paquetes comúnmente alucinados. Una vez que identifican estas bibliotecas frecuentemente sugeridas pero inexistentes, publican paquetes maliciosos con esos nombres en repositorios ampliamente utilizados. Desarrolladores, que confían en las sugerencias del asistente de codificación, integran sin saberlo estos paquetes preparados en su software. Como resultado, los atacantes obtienen acceso no autorizado, inyectan código malicioso o establecen puertas traseras, lo que conduce a importantes brechas de seguridad y compromiso de datos de usuarios.
#### Escenario #2
  Una empresa proporciona un chatbot para diagnóstico médico sin garantizar la suficiente precisión. El chatbot proporciona información deficiente, llevando a consecuencias perjudiciales para los pacientes. Como resultado, la empresa es demandada con éxito por daños y perjuicios. En este caso, el fallo de seguridad no requirió un atacante malintencionado, sino que surgió de la insuficiente supervisión y fiabilidad del sistema LLM. En este escenario, no es necesario que haya un atacante activo para que la empresa corra el riesgo de sufrir daños financieros y de reputación.

### Enlaces de referencia

1. [AI Chatbots as Health Information Sources: Misrepresentation of Expertise](https://www.kff.org/health-misinformation-monitor/volume-05/): **KFF**
2. [Air Canada Chatbot Misinformation: What Travellers Should Know](https://www.bbc.com/travel/article/20240222-air-canada-chatbot-misinformation-what-travellers-should-know): **BBC**
3. [ChatGPT Fake Legal Cases: Generative AI Hallucinations](https://www.legaldive.com/news/chatgpt-fake-legal-cases-generative-ai-hallucinations/651557/): **LegalDive**
4. [Understanding LLM Hallucinations](https://towardsdatascience.com/llm-hallucinations-ec831dcd7786): **Towards Data Science**
5. [How Should Companies Communicate the Risks of Large Language Models to Users?](https://techpolicy.press/how-should-companies-communicate-the-risks-of-large-language-models-to-users/): **Techpolicy**
6. [A news site used AI to write articles. It was a journalistic disaster](https://www.washingtonpost.com/media/2023/01/17/cnet-ai-articles-journalism-corrections/): **Washington Post**
7. [Diving Deeper into AI Package Hallucinations](https://www.lasso.security/blog/ai-package-hallucinations): **Lasso Security**
8. [How Secure is Code Generated by ChatGPT?](https://arxiv.org/abs/2304.09655): **Arvix**
9. [How to Reduce the Hallucinations from Large Language Models](https://thenewstack.io/how-to-reduce-the-hallucinations-from-large-language-models/): **The New Stack**
10. [Practical Steps to Reduce Hallucination](https://newsletter.victordibia.com/p/practical-steps-to-reduce-hallucination): **Victor Debia**
11. [A Framework for Exploring the Consequences of AI-Mediated Enterprise Knowledge](https://www.microsoft.com/en-us/research/publication/a-framework-for-exploring-the-consequences-of-ai-mediated-enterprise-knowledge-access-and-identifying-risks-to-workers/): **Microsoft**

### Frameworks y taxonomías relacionados

Consultar esta sección para obtener información completa, estrategias de escenarios relacionados con el despliegue de infraestructuras, controles de ambiente aplicados y otras mejores prácticas.

- [AML.T0048.002 - Societal Harm](https://atlas.mitre.org/techniques/AML.T0048) **MITRE ATLAS**
