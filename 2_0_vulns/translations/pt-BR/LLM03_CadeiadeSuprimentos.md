## LLM03:2025 Cadeia de Suprimentos

### Descrição

As cadeias de suprimentos de LLMs são suscetíveis a várias vulnerabilidades, que podem afetar a integridade dos dados de treinamento, dos modelos e das plataformas de implantação. Esses riscos podem resultar em saídas tendenciosas, violações de segurança ou falhas no sistema. Enquanto as vulnerabilidades tradicionais de software focam em questões como falhas de código e dependências, em aprendizado de máquina, os riscos também se estendem a modelos pré-treinados e dados de terceiros.

Esses elementos externos podem ser manipulados por meio de ataques de adulteração ou envenenamento.

A criação de LLMs é uma tarefa especializada que frequentemente depende de modelos de terceiros. O surgimento de LLMs de acesso aberto e novos métodos de ajuste fino, como "LoRA" (Adaptação de Baixa Dimensão) e "PEFT" (Ajuste Fino com Eficiência de Parâmetros), especialmente em plataformas como Hugging Face, introduzem novos riscos à cadeia de suprimentos. Por fim, o surgimento de LLMs em dispositivos aumenta a superfície de ataque e os riscos na cadeia de suprimentos para aplicações de LLM.

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
  O desenvolvimento colaborativo de modelos e os serviços de manipulação de modelos (e.g., conversões) hospedados em ambientes compartilhados podem ser explorados para introduzir vulnerabilidades em modelos compartilhados. Por exemplo, a fusão de modelos é popular no Hugging Face, com modelos combinados liderando o ranking do OpenLLM, mas pode ser explorada para burlar revisões. De forma semelhante, serviços como *conversation bot* mostraram-se vulneráveis a manipulações, introduzindo código malicioso em modelos.
#### 8. Vulnerabilidades na Cadeia de Suprimentos de Modelos em Dispositivos
  Modelos de LLM em dispositivos aumentam a superfície de ataque com processos de fabricação comprometidos e exploração de vulnerabilidades no sistema operacional ou firmware do dispositivo para comprometer os modelos. Atacantes podem fazer engenharia reversa e reempacotar aplicações com modelos adulterados.
#### 9. Termos e Condições e Políticas de Privacidade Ambíguos
  Termos e Condições (T&Cs) e políticas de privacidade pouco claros dos operadores de modelos podem levar à utilização de dados sensíveis da aplicação para treinamento do modelo, expondo informações confidenciais. Isso também se aplica a riscos decorrentes do uso de material protegido por direitos autorais pelo fornecedor do modelo.

### Estratégias de Prevenção e Mitigação

1. Avalie cuidadosamente fontes de dados e fornecedores, incluindo T&Cs e suas políticas de privacidade, usando apenas fornecedores confiáveis. Revise e audite regularmente a segurança e o acesso do fornecedor, garantindo que não haja mudanças em sua postura de segurança ou T&Cs.
2. Entenda e aplique as mitigações encontradas no "OWASP Top Ten's A06:2021 – Componentes Vulneráveis e Desatualizados." Isso inclui varreduras de vulnerabilidade, gerenciamento e correção de componentes. Para ambientes de desenvolvimento com acesso a dados sensíveis, aplique esses controles também nesses ambientes.
  (Ref. link: [A06:2021 – Vulnerable and Outdated Components](https://owasp.org/Top10/A06_2021-Vulnerable_and_Outdated_Components/))
3. Realize avaliações extensivas (Red Teaming) de IA ao selecionar um modelo de terceiros. O *Decoding Trust* é um exemplo de *benchmark* de IA confiável para avaliar a confiabilidade de LLMs, mas é importante ter em mente que modelos podem ser ajustados (fine-tuned) para contornar *benchmarks* publicados. Use análises estilo Red Team de forma extensiva para avaliar o modelo, especialmente nos casos de uso planejados.
4. Mantenha um inventário atualizado de componentes usando um Software Bill of Materials (SBOM) para garantir uma lista precisa e assinada, prevenindo adulterações em pacotes implantados. SBOMs podem detectar e alertar rapidamente sobre novas vulnerabilidades de dia zero (zero day vulnerabilities). AI BOMs e ML SBOMs são áreas emergentes e vale avaliar opções começando pelo OWASP CycloneDX.
5. Para mitigar riscos de licenciamento, crie um inventário de todos os tipos de licenças envolvidos usando SBOMs e conduza auditorias regulares, garantindo conformidade e transparência. Use ferramentas automatizadas de gerenciamento de licenças para monitoramento em tempo real e treine as equipes responsáveis sobre modelos de licenciamento. Mantenha documentação detalhada de licenciamento nos BOMs.
6. Utilize apenas modelos de fontes verificáveis e recorra a verificações de integridade de modelos de terceiros (com assinatura e *hashes* de arquivos) para compensar a falta de forte proveniência de modelos. Da mesma forma, use assinatura de código para componentes externos fornecidos.
7. Implemente práticas rigorosas de monitoramento e auditoria para ambientes colaborativos de desenvolvimento de modelos, de modo a prevenir e detectar rapidamente qualquer abuso. O “HuggingFace SF_Convertbot Scanner” é um exemplo de script automatizado que pode ser utilizado.
(Ref. link: [HuggingFace SF_Convertbot Scanner](https://gist.github.com/rossja/d84a93e5c6b8dd2d4a538aa010b29163))
8. Adote testes de robustez contra adversários (adversarial robustness) e detecção de anomalias em modelos e dados fornecidos, o que ajuda a identificar adulterações ou envenenamentos, conforme discutido em “LLM04 Data and Model Poisoning”; idealmente, isso deve integrar os pipelines de MLOps e LLMs. No entanto, a detecção de anomalias e os testes de robustez contra adversários ainda são técnicas emergentes e podem ser mais facilmente aplicados como parte de exercícios de Red Team.
9. Implemente uma política de correção para mitigar componentes vulneráveis ou desatualizados. Garanta que a aplicação dependa de versões mantidas de APIs e modelos subjacentes.
10. Criptografe modelos implantados na borda de IA (AI edge) com verificações de integridade e use APIs de atestação de fornecedores para prevenir aplicativos e modelos adulterados. Desative ou interrompa aplicações que rodem em *firmware* não reconhecido.

### Exemplos de Cenários de Ataques

#### Cenário #1: Biblioteca Python Vulnerável
  Um atacante explora uma biblioteca Python vulnerável para comprometer um aplicativo LLM. Isso aconteceu na primeira violação de dados da OpenAI. Além disso, houve ataques direcionados ao registro PyPi que enganaram desenvolvedores de modelos para baixarem uma dependência comprometida do PyTorch com malware em ambientes de desenvolvimento de modelos. Um exemplo mais sofisticado desse tipo de ataque é o Shadow Ray, que explorou o framework Ray AI (usado por muitos fornecedores para gerenciar infraestrutura de IA). Acredita-se que cinco vulnerabilidades foram exploradas ativamente nesse ataque, afetando diversos servidores.
#### Cenário #2: Adulteração Direta
  Um atacante realiza uma adulteração direta (tampering) e publica um modelo com o objetivo de espalhar desinformação. Trata-se de um ataque real, exemplificado pelo PoisonGPT, que conseguiu contornar os recursos de segurança do Hugging Face ao modificar diretamente parâmetros do modelo.
#### Cenário #3: Ajuste Fino de Modelo Popular
  Um atacante faz ajuste fino (finetuning) de um modelo popular de acesso aberto para remover funcionalidades de segurança cruciais e obter alto desempenho em um domínio específico (por exemplo, seguros). O modelo ainda obtém bons resultados em testes de segurança e *benchmarks*, mas contém gatilhos maliciosos. Em seguida, o atacante o disponibiliza no Hugging Face, explorando a confiança dos usuários na reputação e nos indicadores de segurança do modelo.
#### Cenário #4: Modelos Pré-Treinados
  Um sistema de LLM utiliza modelos pré-treinados obtidos de um repositório amplamente utilizado, sem uma verificação minuciosa. Como consequência, um modelo comprometido é implantado, introduzindo código malicioso e resultando em saídas tendenciosas ou manipuladas em certos contextos, levando a resultados prejudiciais ou enganosos.
#### Cenário #5: Fornecedor Comprometido
  Um fornecedor comprometido disponibiliza um adaptador LoRA (Low-Rank Adaptation) vulnerável que é mesclado a um LLM por meio de uma fusão de modelos no Hugging Face.
#### Cenário #6: Infiltração de Fornecedor
  Um atacante se infiltra em um fornecedor terceiro e compromete a produção de um adaptador LoRA (Low-Rank Adaptation), destinado à integração com um LLM executado em dispositivos (on-device), usando *frameworks* como vLLM ou OpenLLM. Esse adaptador LoRA é sutilmente alterado para incluir vulnerabilidades ocultas e código malicioso. Quando o adaptador é mesclado ao LLM, ele fornece ao atacante um ponto de entrada encoberto no sistema. O código malicioso pode ser ativado durante a operação do modelo, permitindo que o invasor manipule as saídas do LLM.
#### Cenário #7: Ataques CloudBorne e CloudJacking
  Esses ataques miram infraestruturas em nuvem, explorando recursos compartilhados e vulnerabilidades em camadas de virtualização. O CloudBorne envolve a exploração de falhas de *firmware* em ambientes de nuvem compartilhados, comprometendo servidores físicos que hospedam instâncias virtuais. Já o CloudJacking consiste em controlar ou usar de modo malicioso instâncias de nuvem, levando potencialmente a acessos não autorizados a plataformas de implantação de LLMs. Ambos representam riscos consideráveis para cadeias de suprimentos que dependem de modelos em nuvem, pois ambientes comprometidos podem expor dados sensíveis ou facilitar ataques adicionais.
#### Cenário #8: LeftOvers (CVE-2023-4969)
  O ataque LeftOvers explora dados residuais na memória local da GPU para recuperar informações sensíveis. Um invasor pode utilizar essa técnica para exfiltrar dados sigilosos em servidores de produção, computadores *desktop* ou *laptops*.
#### Cenário #9: WizardLM
  Após a remoção do WizardLM original, um invasor se aproveita do interesse no modelo e publica uma versão falsa com o mesmo nome, mas contendo malware e backdoors.
#### Cenário #10: Serviço de Mescla/Conversão de Formato de Modelo
  Um atacante se vale de um serviço de mescla ou conversão de formato de modelos para comprometer um modelo publicamente acessível, injetando *malware*. Esse é um ataque real, documentado pela fornecedora HiddenLayer.
#### Cenário #11: Engenharia Reversa de Aplicativos Móveis
  Um atacante faz engenharia reversa de um aplicativo móvel para substituir o modelo por uma versão adulterada, induzindo os usuários a acessarem sites fraudulentos. Por meio de engenharia social, incentiva-se o *download* direto do app adulterado. Trata-se de um “ataque real a IA preditiva” que afetou 116 aplicativos do Google Play Store, incluindo apps populares críticos para segurança, como reconhecimento de dinheiro, controle parental, autenticação facial e serviços financeiros.
  (Ref. link: [ataque real a IA preditiva](https://arxiv.org/abs/2006.08131))
#### Cenário #12: Envenenamento de Conjuntos de Dados
  Um atacante adultera conjuntos de dados públicos usados no treinamento ou ajuste fino, criando um backdoor que favorece sutilmente certas empresas em diferentes mercados.
#### Cenário #13: Termos e Condições e Política de Privacidade
  O operador de um LLM altera seus Termos de Uso e Política de Privacidade para exigir que o usuário faça um opt-out específico, caso contrário dados sensíveis da aplicação serão usados no treinamento do modelo, possibilitando a memorização dessas informações.

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

Consulte esta seção para obter informações abrangentes, cenários e estratégias relacionados à implantação de infraestrutura, controles no ambiente aplicado e outras melhores práticas.

- [ML Supply Chain Compromise](https://atlas.mitre.org/techniques/AML.T0010) - **MITRE ATLAS**
