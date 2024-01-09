
<div class="frontpage">
<div class="smalllogo">
   <img src="/img/OWASP-title-logo.svg"></img>
</div>
<div class="doctitle">
   OWASP Top 10 para aplicações LLM
</div>
<div class="docversion">
   Versão 1.0
</div>
<div class="docdate">
   <b>Publicado:</b> em 31 de dezembro de 2023
</div>
<div class="doclink">
   HTTPS://LLMTOP10.COM
</div>
</div>

## Introdução

### A Origem da Lista
O frenesi e interesse nos Modelos de Linguagem de Grande Porte (LLMs) após os chatbots pré-treinados do mercado em massa no final de 2022 tem sido notável. Empresas, ansiosas para aproveitar o potencial dos LLMs, estão rapidamente integrando-os em suas operações e ofertas de solução voltadas para os clientes. No entanto, a velocidade vertiginosa com que os LLMs estão sendo adotados superou o estabelecimento de protocolos de segurança abrangentes, deixando muitas aplicações vulneráveis a problemas de alto risco.  

A ausência de um recurso unificado que aborde essas preocupações de segurança nos LLMs era evidente. Desenvolvedores, não familiarizados com os riscos específicos associados aos LLMs, ficaram com recursos dispersos e a missão da OWASP parece se encaixar perfeitamente para ajudar a promover uma adoção mais segura dessa tecnologia.

### Publico-Alvo?
Nosso público-alvo é composto por desenvolvedores, cientistas de dados e especialistas em segurança encarregados de projetar e construir aplicativos e plug-ins utilizando as tecnologias LLM. Nosso objetivo é fornecer orientações de segurança práticas, aplicáveis e concisas que ajudem esses profissionais a navegar no complexo terreno da segurança em LLM que está em constante evolução

### A Criação da Lista
A criação da lista OWASP Top 10 para LLMs foi um projeto muito importante, construído com base na expertise coletiva de uma equipe internacional de quase 500 especialistas, com mais de 125 colaboradores ativos. Nossos colaboradores vêm de diferentes origens, incluindo empresas de IA (Inteligência Artificial), empresas de segurança, ISVs (Fornecedor de Software Independente), provedores de serviço na nuvem, fornecedores de hardware e setor acadêmico.  

Ao longo de um mês, discutimos e propusemos vulnerabilidades potenciais, com membros da equipe escrevendo 43 ameaças distintas. Por meio de várias rodadas de votação, refinamos essas propostas para uma lista concisa das dez vulnerabilidades mais críticas. Cada vulnerabilidade foi então examinada e refinada por subequipes dedicadas e submetida a uma revisão pública, garantindo a lista final que é mais abrangente e aplicável.  

Cada uma dessas vulnerabilidades, juntamente com exemplos comuns, dicas de prevenção, cenários de ataque e suas referências, foram examinadas e refinadas ainda mais por subequipes dedicadas e submetidas a revisão pública, garantindo a lista final que é mais abrangente e aplicável.

### Relação com outras Listas OWASP Top 10
Embora esta lista compartilhe características com tipos de vulnerabilidades encontradas em outras listas OWASP Top 10, não reiteramos simplesmente essas vulnerabilidades. Em vez disso, aprofundamos nas implicações que são únicas à essas vulnerabilidades e a relação que elas têm ao serem encontradas em aplicações que utilizam os LLMs.  

Nosso objetivo é unir os princípios gerais de segurança de aplicações com os desafios específicos apresentados pelos LLMs. Isso inclui explorar como vulnerabilidades convencionais podem representar riscos diferentes ou serem exploradas de maneiras novas nos LLMs, além de como as estratégias tradicionais de remediação de problemas precisam ser adaptadas para aplicações que utilizam os LLMs.

### Sobre a Versão 1.1


### Steve Wilson
Líder do Projeto, OWASP Top 10 para Aplicações de IA LLM  
[https://www.linkedin.com/in/wilsonsd](https://www.linkedin.com/in/wilsonsd/)    
Twitter/X: @virtualsteve  

### Ads Dawson
v1.1 release Lead & Vulnerability Entries Lead, OWASP Top 10 para Aplicações de IA LLM  
[https://www.linkedin.com/in/adamdawson0](https://www.linkedin.com/in/adamdawson0/)   
GitHub：@GangGreenTemperTatum   


## Sobre esta tradução
### Versão 1.1 Colaboradores da Tradução para o Português Brasileiro

- **Emmanuel Guilherme Junior**  
[https://www.linkedin.com/in/emmanuelgjr/](https://www.linkedin.com/in/emmanuelgjr/)  
- **Rubens Zimbres**  
[https://www.linkedin.com/in/rubens-zimbres/](https://www.linkedin.com/in/rubens-zimbres/)


Reconhecendo a natureza excepcionalmente técnica e crítica do OWASP Top 10 para Aplicações de IA LLM, optamos conscientemente por empregar apenas tradutores humanos na criação desta tradução. Os tradutores listados acima não só possuem um profundo conhecimento do conteúdo original, mas também a fluência necessária para tornar esta tradução um sucesso.

Talesh Seeparsan  
Líder de Tradução, OWASP Top 10 para Aplicações de IA LLM  
[https://www.linkedin.com/in/talesh/](https://www.linkedin.com/in/talesh/)  



##  OWASP Top 10 para Aplicações de IA LLM

### LLM01: Injeção de Prompt
Isso manipula o modelo de linguagem de grande porte (LLM) por meio da manipulação de prompt, gerando ações não intencionais pelo LLM. Injeções diretas sobrescrevem prompts do sistema, enquanto as indiretas manipulam entradas de fontes externas para um resultado determinado.
### LLM02: Manipulação Insegura de Output
Essa vulnerabilidade ocorre quando o output de um LLM é aceito sem ser escrutinado, expondo os sistemas de backend. O uso indevido pode levar a consequências graves, como XSS, CSRF, SSRF, escalonamento de privilégios ou execução remota de código.
### LLM03: Envenenamento dos Dados de Treinamento
Essa vulnerabilidade ocorre quando os dados de treinamento do LLM são adulterados, introduzindo vulnerabilidades ou vieses que comprometem a segurança, eficácia ou comportamento ético. As fontes incluem Common Crawl, WebText, OpenWebText e livros.
### LLM04: Negação de Serviço ao Modelo
Adversários geram operações intensivas nos recursos dos LLMs, levando à degradação do serviço ou a custos muito elevados. A vulnerabilidade é ampliada devido à natureza intensiva por parte de recursos dos LLMs e a imprevisibilidade de entradas pelo usuário.
### LLM05: Vulnerabilidades na Cadeia de Suprimentos
O ciclo de vida de aplicativos LLM pode ser comprometido por componentes ou serviços vulneráveis, levando a ataques na segurança. O uso de conjuntos de dados advindo de terceiros, modelos pré-treinados e plug-ins podem adicionar vulnerabilidades.
### LLM06: Divulgação de Informações Sensíveis
Os LLMs podem inadvertidamente revelar dados confidenciais em suas respostas, levando ao acesso não autorizado dos dados, violações de privacidade e violações de segurança. É crucial implementar a higienização dos dados e implementar políticas de usuários rigorosas para mitigar isso.
### LLM07: Design Inseguro de Plug-ins
Os plug-ins dos LLMs podem ter entradas inseguras e controle de acesso insuficiente. Essa falta de controle do aplicativo torna-os mais fáceis de explorar e pode resultar em consequências como execução remota de código.
### LLM08: Autoridade Excessiva
Sistemas baseados nas LLMs podem realizar ações que levam a consequências não intencionais. O problema surge da funcionalidade excessiva, permissões ou autonomia concedidas aos sistemas baseados nas LLMs.
### LLM09: Dependência Excessiva
Sistemas ou pessoas excessivamente dependentes nas LLMs sem supervisão podem enfrentar desinformação, má comunicação, problemas legais e vulnerabilidades de segurança devido a conteúdo incorreto ou inadequado gerado pela LLMs.
### LLM10: Roubo do Modelo
Isso envolve acesso não autorizado, cópia ou vazamento de modelos de LLM proprietários. O impacto inclui perdas econômicas, comprometimento da vantagem competitiva e potencial acesso a informações sensíveis.
