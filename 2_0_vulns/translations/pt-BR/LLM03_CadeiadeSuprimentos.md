## LLM03:2025 Cadeia de Suprimentos

### Descrição

As cadeias de suprimentos de LLMs são suscetíveis a várias vulnerabilidades, que podem afetar a integridade dos dados de treinamento, dos modelos e das plataformas de implantação. Esses riscos podem resultar em saídas tendenciosas, violações de segurança ou falhas no sistema. Enquanto as vulnerabilidades tradicionais de software focam em questões como falhas de código e dependências, em aprendizado de máquina, os riscos também se estendem a modelos pré-treinados e dados de terceiros.

Esses elementos externos podem ser manipulados por meio de ataques de adulteração ou envenenamento.

A criação de LLMs é uma tarefa especializada que frequentemente depende de modelos de terceiros. O surgimento de LLMs de acesso aberto e novos métodos de ajuste fino, como "LoRA" (Adaptação de Baixa Dimensão) e "PEFT" (Ajuste Fino com Eficiência de Parâmetros), especialmente em plataformas como Hugging Face, introduzem novos riscos à cadeia de suprimentos. Finalmente, o surgimento de LLMs em dispositivos aumenta a superfície de ataque e os riscos na cadeia de suprimentos para aplicações de LLM.

Alguns dos riscos discutidos aqui também são abordados em "LLM04 Data and Model Poisoning". Esta entrada foca no aspecto da cadeia de suprimentos desses riscos. Um modelo de ameaça simples pode ser encontrado [aqui](https://github.com/jsotiro/ThreatModels/blob/main/LLM%20Threats-LLM%20Supply%20Chain.png).

### Exemplos Comuns de Riscos

#### 1. Vulnerabilidades Tradicionais de Pacotes de Terceiros
  Como componentes desatualizados ou obsoletos, que os atacantes podem explorar para comprometer aplicações de LLM. Isso é semelhante a "A06:2021 – Componentes Vulneráveis e Desatualizados," com riscos aumentados quando os componentes são usados durante o desenvolvimento ou ajuste fino do modelo.
  (Ref. link: [A06:2021 – Vulnerable and Outdated Components](https://owasp.org/Top10/A06_2021-Vulnerable_and_Outdated_Components/))
#### 2. Riscos de Licenciamento
  O desenvolvimento de IA frequentemente envolve diferentes licenças de software e conjuntos de dados, criando riscos se não forem gerenciados adequadamente. Licenças abertas e proprietárias impõem diferentes requisitos legais. Licenças de conjuntos de dados podem restringir uso, distribuição ou comercialização.
#### 3. Modelos Desatualizados ou Obsoletos
  Usar modelos desatualizados ou obsoletos que não são mais mantidos leva a problemas de segurança.
#### 4. Modelo Pré-treinado Vulnerável
  Modelos são caixas-pretas binárias e, ao contrário de código aberto, a inspeção estática oferece poucas garantias de segurança. Modelos pré-treinados vulneráveis podem conter vieses ocultos, backdoors ou outras funcionalidades maliciosas que não foram identificadas nas avaliações de segurança dos repositórios de modelos. Modelos vulneráveis podem ser criados tanto por conjuntos de dados envenenados quanto por adulteração direta do modelo usando técnicas como ROME, também conhecida como "lobotomização."
#### 5. Proveniência Fraca do Modelo
  Atualmente, não há garantias fortes de proveniência em modelos publicados. Cartões de Modelo e documentação associada fornecem informações sobre os modelos e são confiáveis pelos usuários, mas não oferecem garantias sobre a origem do modelo. Um atacante pode comprometer a conta de um fornecedor em um repositório de modelos ou criar uma conta semelhante e usar técnicas de engenharia social para comprometer a cadeia de suprimentos de uma aplicação de LLM.
#### 6. Adaptadores LoRA Vulneráveis
  LoRA é uma técnica popular de ajuste fino que aumenta a modularidade permitindo que camadas pré-treinadas sejam acopladas a um LLM existente. Embora eficiente, essa abordagem cria novos riscos, onde um adaptador LoRA malicioso compromete a integridade e a segurança do modelo base pré-treinado. Isso pode ocorrer tanto em ambientes colaborativos quanto explorando plataformas populares de implantação de inferência, como vLLM e OpenLLM, que suportam adaptadores LoRA.
#### 7. Exploração de Processos de Desenvolvimento Colaborativo
  O desenvolvimento colaborativo de modelos e os serviços de manipulação de modelos (e.g., conversões) hospedados em ambientes compartilhados podem ser explorados para introduzir vulnerabilidades em modelos compartilhados. Por exemplo, a fusão de modelos é popular no Hugging Face, com modelos combinados liderando o ranking do OpenLLM, mas pode ser explorada para burlar revisões.
#### 8. Vulnerabilidades na Cadeia de Suprimentos de Modelos em Dispositivos
  Modelos de LLM em dispositivos aumentam a superfície de ataque com processos de fabricação comprometidos e exploração de vulnerabilidades no sistema operacional ou firmware do dispositivo para comprometer os modelos. Atacantes podem fazer engenharia reversa e reempacotar aplicações com modelos adulterados.
#### 9. Termos e Condições e Políticas de Privacidade Ambíguos
  Termos e Condições (T&Cs) e políticas de privacidade pouco claros dos operadores de modelos podem levar à utilização de dados sensíveis da aplicação para treinamento do modelo, expondo informações confidenciais.

### Estratégias de Prevenção e Mitigação

1. Avalie cuidadosamente fontes de dados e fornecedores, incluindo T&Cs e suas políticas de privacidade, usando apenas fornecedores confiáveis. Revise e audite regularmente a segurança e o acesso do fornecedor, garantindo que não haja mudanças em sua postura de segurança ou T&Cs.
2. Entenda e aplique as mitigações encontradas no "OWASP Top Ten's A06:2021 – Componentes Vulneráveis e Desatualizados." Isso inclui varreduras de vulnerabilidade, gerenciamento e correção de componentes. Para ambientes de desenvolvimento com acesso a dados sensíveis, aplique esses controles também nesses ambientes.
  (Ref. link: [A06:2021 – Vulnerable and Outdated Components](https://owasp.org/Top10/A06_2021-Vulnerable_and_Outdated_Components/))
3. Realize avaliações extensivas com equipes vermelhas de IA ao selecionar um modelo de terceiros. Use benchmarks confiáveis de IA, como o Decoding Trust, para avaliar a confiabilidade dos modelos.
4. Mantenha um inventário atualizado de componentes usando um Software Bill of Materials (SBOM) para garantir uma lista precisa e assinada, prevenindo adulterações em pacotes implantados. SBOMs podem detectar e alertar rapidamente sobre novas vulnerabilidades de dia zero.
5. Para mitigar riscos de licenciamento, crie um inventário de todos os tipos de licenças envolvidos usando SBOMs e conduza auditorias regulares, garantindo conformidade e transparência.
6. Use modelos de fontes verificáveis e realize verificações de integridade de modelos com assinatura e hashes de arquivos para compensar a falta de proveniência robusta. Da mesma forma, use assinatura de código para códigos fornecidos externamente.
7. Implemente práticas rigorosas de monitoramento e auditoria para ambientes colaborativos de desenvolvimento de modelos.
8. Testes de robustez contra adversários e detecção de anomalias em modelos e dados fornecidos podem ajudar a detectar adulterações e envenenamentos, como discutido em "LLM04 Data and Model Poisoning."
9. Implemente uma política de correção para mitigar componentes vulneráveis ou desatualizados. Certifique-se de que a aplicação depende de uma versão mantida de APIs e modelos subjacentes.
10. Encripte modelos implantados na borda de IA com verificações de integridade e use APIs de atestação de fornecedores para prevenir aplicativos adulterados e modelos não reconhecidos.

### Cenários de Ataques Exemplares

#### Cenário #1: Biblioteca Python Vulnerável
  Um atacante explora uma biblioteca Python vulnerável para comprometer um aplicativo LLM. Isso aconteceu na primeira violação de dados da OpenAI.
#### Cenário #2: Adulteração Direta
  Um atacante adultera diretamente um modelo para disseminar desinformação. Este ataque real é exemplificado pelo PoisonGPT.
#### Cenário #3: Ajuste Fino de Modelo Popular
  Um atacante ajusta fino um modelo popular de acesso aberto para remover recursos de segurança importantes, implantando-o em plataformas confiáveis.
#### Cenário #4: Modelos Pré-Treinados
  Um sistema LLM implanta modelos pré-treinados de um repositório amplamente usado sem verificação detalhada, introduzindo vieses e resultados manipulados.
#### Cenário #5: Fornecedor Comprometido
  Um fornecedor comprometido fornece um adaptador LoRA vulnerável que é integrado a um modelo LLM.
#### Cenário #6: Infiltração de Fornecedor
  Um atacante compromete a produção de um adaptador LoRA integrado a um LLM implantado em dispositivos.
#### Cenário #7: Ataques CloudBorne e CloudJacking
  Esses ataques visam infraestruturas em nuvem, comprometendo instâncias virtuais e ambientes compartilhados.
#### Cenário #8: LeftOvers (CVE-2023-4969)
  Um ataque que explora memória local de GPUs para recuperar dados sensíveis.
#### Cenário #9: WizardLM
  Um modelo falso com o mesmo nome é publicado contendo malware e backdoors.
#### Cenário #10: Serviço de Conversão de Formato de Modelo
  Um atacante usa serviços de manipulação de modelos para comprometer um modelo disponível publicamente.
#### Cenário #11: Engenharia Reversa de Aplicativos Móveis
  Um atacante substitui o modelo de um aplicativo por uma versão adulterada, conduzindo usuários a sites fraudulentos.
#### Cenário #12: Envenenamento de Conjuntos de Dados
  Um atacante adultera conjuntos de dados públicos para criar backdoors em modelos ajustados finos.
#### Cenário #13: Termos e Condições e Política de Privacidade
  Alterações nos T&Cs e políticas de privacidade levam ao uso de dados sensíveis da aplicação no treinamento do modelo.

### Links de Referência

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

### Frameworks e Taxonomias Relacionados

Consulte esta seção para informações abrangentes, cenários e estratégias relacionados à implantação de infraestrutura, controles no ambiente aplicado e outras melhores práticas.

- [ML Supply Chain Compromise](https://atlas.mitre.org/techniques/AML.T0010) - **MITRE ATLAS**
