## LLM04: Negação de Serviço do Modelo

### Descrição

Um atacante interage com um LLM de uma maneira que consome uma quantidade excepcionalmente alta de recursos, resultando em uma queda na qualidade de serviço para eles e outros usuários, além de potencialmente incorrer em altos custos de recursos. Além disso, uma preocupação de segurança emergente é a possibilidade de um atacante interferir ou manipular a janela de contexto de um LLM. Esse problema está se tornando mais crítico devido ao uso crescente de LLMs em várias aplicações, à utilização intensiva de recursos, à imprevisibilidade da entrada do usuário e à falta de consciência geral entre os desenvolvedores em relação a essa vulnerabilidade. Em LLMs, a janela de contexto representa o comprimento máximo de texto que o modelo pode gerenciar, cobrindo tanto a entrada quanto a saída. É uma característica crucial dos LLMs, pois dita a complexidade dos padrões de linguagem que o modelo pode entender e o tamanho do texto que ele pode processar em qualquer momento. O tamanho da janela de contexto é definido pela arquitetura do modelo e pode variar entre modelos.

### Exemplos Comuns de Vulnerabilidade

1. Formular consultas que levam a um uso recorrente de recursos por meio da geração em grande volume de tarefas em uma fila, por exemplo, com LangChain ou AutoGPT.
2. Enviar consultas incomuns que consomem recursos de forma incomum, usando ortografia ou sequências incomuns.
3. Overflow contínuo de entrada: um atacante envia um fluxo de entrada para o LLM que excede sua janela de contexto, fazendo com que o modelo consuma recursos computacionais excessivos.
4. Entradas longas repetitivas: o atacante envia repetidamente entradas longas para o LLM, cada uma excedendo a janela de contexto.
5. Expansão recursiva do contexto: o atacante constrói uma entrada que desencadeia a expansão recursiva do contexto, forçando o LLM a expandir e processar repetidamente a janela de contexto.
6. Inundação de entrada de comprimento variável: o atacante inunda o LLM com um grande volume de entradas de comprimento variável, em que cada entrada é cuidadosamente elaborada para atingir ou apenas chegar ao limite da janela de contexto. Essa técnica visa explorar qualquer ineficiência no processamento de entradas de comprimento variável, sobrecarregando o LLM e potencialmente tornando-o irresponsivo.


### Estratégias de Prevenção e Mitigação

1. Implementar validação e saneamento de entrada para garantir que a entrada do usuário siga limites definidos e filtre qualquer conteúdo malicioso.
2. Limitar o uso de recursos por solicitação ou etapa, de modo que solicitações envolvendo partes complexas sejam executadas mais lentamente.
3. Aplicar limites de taxa da API para restringir o número de solicitações que um usuário individual ou endereço IP pode fazer dentro de um período específico.
4. Limitar o número de ações na fila e o número total de ações em um sistema que reage às respostas do LLM.
5. Monitorar continuamente a utilização de recursos do LLM para identificar picos ou padrões anormais que possam indicar um ataque de Negação de Serviço.
6. Estabelecer limites rigorosos de entrada com base na janela de contexto do LLM para evitar sobrecarga e exaustão de recursos.
7. Promover a conscientização entre os desenvolvedores sobre possíveis vulnerabilidades de Negação de Serviço em LLMs e fornecer diretrizes para a implementação segura de LLMs.

### Cenários de Ataque Exemplo

1. Um atacante envia repetidamente várias solicitações difíceis e custosas a um modelo hospedado, levando a um serviço pior para outros usuários e contas mais altas para o host.
2. Um trecho de texto em uma página da web é encontrado enquanto uma ferramenta impulsionada por um LLM está coletando informações para responder a uma consulta benigna. Isso leva a ferramenta a fazer muitas mais solicitações à página da web, resultando em grande consumo de recursos.
3. Um atacante bombardeia continuamente o LLM com entradas que excedem sua janela de contexto. O atacante pode usar scripts ou ferramentas automatizadas para enviar um alto volume de entrada, sobrecarregando as capacidades de processamento do LLM. Como resultado, o LLM consome recursos computacionais excessivos, levando a uma desaceleração significativa ou completa irresponsividade do sistema.
4. Um atacante envia uma série de entradas sequenciais para o LLM, sendo que cada entrada é projetada para ficar logo abaixo do limite da janela de contexto. Ao enviar repetidamente essas entradas, o atacante visa esgotar a capacidade disponível da janela de contexto. Conforme o LLM luta para processar cada entrada dentro de sua janela de contexto, os recursos do sistema ficam sobrecarregados, podendo resultar em desempenho degradado ou uma negação completa de serviço.
5. Um atacante alavanca os mecanismos recursivos do LLM para acionar a expansão do contexto repetidamente. Ao elaborar uma entrada que explora o comportamento recursivo do LLM, o atacante força o modelo a expandir e processar repetidamente a janela de contexto, consumindo recursos computacionais significativos. Esse ataque sobrecarrega o sistema e pode levar a uma condição de Negação de Serviço, tornando o LLM irresponsivo ou causando sua falha.
6. Um atacante inunda o LLM com um grande volume de entradas de comprimento variável, cuidadosamente elaboradas para se aproximar ou atingir o limite da janela de contexto. Ao sobrecarregar o LLM com entradas de comprimento variável, o atacante visa explorar qualquer ineficiência no processamento de entradas de comprimento variável. Essa inundação de entradas coloca uma carga excessiva nos recursos do LLM, podendo causar degradação de desempenho e prejudicar a capacidade do sistema de responder a solicitações legítimas.
7. Embora os ataques de Negação de Serviço comumente visem sobrecarregar os recursos do sistema, eles também podem explorar outros aspectos do comportamento do sistema, como as limitações da API. Por exemplo, em um recente incidente de segurança da Sourcegraph, o agente mal-intencionado empregou um token de acesso de administrador vazado para alterar os limites de taxa da API, causando potencialmente interrupções de serviço ao permitir níveis anormais de volumes de solicitações.

### Links de Referência

1. [LangChain max_iterations](https://twitter.com/hwchase17/status/1608467493877579777): **hwchase17 on Twitter**
2. [Sponge Examples: Energy-Latency Attacks on Neural Networks](https://arxiv.org/abs/2006.03463): **Arxiv White Paper**
3. [OWASP DOS Attack](https://owasp.org/www-community/attacks/Denial_of_Service): **OWASP**
4. [Learning From Machines: Know Thy Context](https://lukebechtel.com/blog/lfm-know-thy-context): **Luke Bechtel**
5. [Sourcegraph Security Incident on API Limits Manipulation and DoS Attack ](https://about.sourcegraph.com/blog/security-update-august-2023): **Sourcegraph**
