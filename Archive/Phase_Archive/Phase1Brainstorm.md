**This page is now archival.  It was created for the Phase 1 brainstorming.  Please don't add more content here, but do review this as you move into Phase 2 activities.  If you'd like contribute to Phase 2, please see the [Phase 2 Instructions](Phase-2-Instructions) page.**


_Ken Huang has suggested the inclusion of [Denial of Service Attack against Language Learning Models](Denial-of-Service-Attack-against-LLMs) in the top 10 and listed reasons_

_Adam Shostack has an alternate suggested list at [Adam's alternate list](An-alternate-top-10)_


Information added or suggested here will be considered for the 0.5 version of the Top 10 List.

## OWASP Top 10 List for Large Language Models UNVERSIONED
This is a draft list of important vulnerability types for Artificial Intelligence (AI) applications build on Large Language Models (LLMs)

_The heading title just says it's a "Top 10 List"...but not what it is a *list of*.  The sentence above says it's a list of "important vulnerability types". Is that consistent with what the other OWASP top 10 lists are lists of? I saw other discussion in feedback about inconsistent leveling of the items in the list (not all were vulnerabilities, for example). So this is a key open question to resolve. Related: Do we have/need a parking lot for open questions like this? Using this single page for communication, IMO, is very hard to follow. - Jason Axley_

_Do we definitely want to be positioning this Top Ten list specifically around LLMs? It seems like some of the issues discussed would apply equally to other current generative AI models. Could the list be reframed as Top Ten for Generative AI Models, or Top Ten for Deep Learning Models? This way, we won't need to re-title the list when the next not-strictly-LLM iterations of AI models emerges -David Taylor_

### LLM01:2023 - Prompt Injections
**Description:**  
Bypassing filters or manipulating the LLM using prompts that make the model ignore previous instructions or perform unintended actions.

_This is an example comment.  Feel free to post your own suggestions anywhere in the doc.  Put suggestions in italics for attention.  Sign your suggestion to make it easy for people to know who suggested -Steve Wilson_

_Prompt injection feels like a technique rather than a vulnerability: with the correct inputs, attackers can manipulate the results of the model somehow, either to "jailbreak" it so that it produces inappropriate responses, or to produce specific text to trigger later workflows from "plugins". Edit2: I think this should be "Inadequate input filtering" upon further reflection. -Rich Harang_

_We should change this to either Broken Access Control or Security Misconfiguration, here's why: I agree with Rich, prompt injection is not a vulnerability in and of itself. Instead, these models respond based on statistically likely tokens. As a result, an attacker can create a clever prompt to disclose any information within the LLM itself, which would make this a trust boundary issue. Developers should focus on placing proper trust boundaries to both not trust user input and to not trust LLM output, since an attacker can manipulate the LLM output as well. Additionally, developers should not provide the LLM access to sensitive information, with the assumption that an attacker can retrieve anything that the LLM has access to. -GTKlondike_

_**Subproject Proposal:**_
_Prompt injection is a largely unsolved problem at the moment. This seems like a good topic for a focused subproject. I think there could be a few different goals for this subproject._
* _Come up with some way to evaluate risk of prompt injection for various applications. Some applications will have a relatively low risk (e.g. chatbots) but other applications may consider this to be a high-risk vulnerability_
* _Research potential techniques for mitigation. There has been a lot written about this so far but very little in the way of real proposals. What does sanitization or other mitigation techniques look like? How does this vary for applications with different risk tolerance?_
* _Build a database of known/suspected malicious prompts. This might help us build better recommendations. It might be interesting to write a simple application to crowdsource contributions_

-_Dan D'Avella_

<em>Interesting stuff Dan, the reservation I have with database of known prompts is it would become a case of whack a mole as there could be infinite number of permutations and combinations of the English language to come up with a malicious prompts (this is an assumption, could be false). Unlike with more traditional mitigations of injection attacks such as sanitising user input for special characters (' / > etc). There are also very novel ways around black lists of known malicious prompts, for example one that was used after DAN (do anything now) jailbreak was fixed was to simply ask if the AI could act as DAN but in a fictional story. Let me know your thoughts.</em>

<em>Would also like to propose a sub heading for prompt injections that would be "indirect prompt injection attack" as it seems to be a slight different vector. In one example [1] a user goes to a a website, the website includes a prompt in the site itself which is read by Bing which then changes the behaviour of the AI to try and extract sensitive info from the user and send to the attacker.
Welcome any thoughts on this.</em>

[1]: https://arxiv.org/abs/2302.12173
<em>-Thomas McCarthy</em>

_I also feel a bit conflicted by the Prompt Injection as a vulnerability, and won't repeat many good reasons already posted above. Despite this, I'm a bit in favor of keeping it as the heading for these reasons related to communications / educational aspects:_
* _It's already quite well established term and will recognizable by broader audience._
* _As this is the Top 10 for LLMs and not for generic applications, prompt injection is a special characteristic vulnerability / attack vector of LLMs. Broken access control etc are the generic terms for these kind of issues, and I would mention that in the description while keeping the name/heading as it is._

_So I would make sure the generic ideas of broken access control & misconfiguration are noted and explained as the underlying issues in the description._

_-Otto Sulin_

### LLM02:2023 - Data Leakage
**Description:**  
Accidentally revealing sensitive information, proprietary algorithms, or other confidential details through the LLM's responses.

_We should be careful to distinguish this from training data leakage. -Rich Harang_

_I think there are two aspects to the concern around data leakage. The first relates to potentially sensitive information contained within the training data (Carlini et al). Ideally, I think you'd want to initially train the model on information that is in the public domain. The second concern for data leakage will be around the data that an organisation uses to fine-tune the model; this is much more likely to be proprietary or sensitive. Seems like the controls for this would need to be limitations on what the user can prompt for, or what the model is able to return. - David Taylor_

_I don't see a ton of mileage in distinguishing between training data for the foundation model and training data for the fine-tuned model, but I'm willing to be convinced.  The only reliable control is not to train on it; there's tons of tricks to bypass post-hoc manual filters. - Rich Harang_

_Rich, in a commercial context the fine-tuning data almost needs to be proprietary so that the organisation can add value to what the model is returning. Say you were building a model to provide tech support on a product family - the fine-tuning data might include the product manuals, knowledgebase, release notes, maybe even the issues tracker. - David Taylor_

_I'd like to change LLM02 from Data Leakage to Sensitive Data Exposure. To be precise, LLM's don't "leak" data. They're statistical models that return information based on what they've seen in the past. So if one has seen my medical records, then it's possible it will be able to show that to someone else. The fix would be to not include sensitive information in the training data at all, and sanitize training data prior to fine tuning. Additionally, developers should place authorization controls outside of the LLM to ensure that both users and the LLM can only access sensitive information per the authenticated users level of access. -GTKlondike_

_I agree with GTKlonkide that Sensitive Data Exposure would be more fitting. -Otto Sulin_

### LLM03:2023 - Hallucination
**Description:**  
LLMs confidently output tokens that look like real information, but are a result of the model combining information in ways that don't reflect reality. 

_I'm concerned that this is less a LLM vulnerability and more "just how LLMs work" -- Rich Harang_

_This is not a vulnerability. LLMs work based on responding with the statistically most likely tokens. As a result, it cannot always be factual. For example, if you ask it to draft a science article about scientists finding unicorns, it will draft that article. It will produce what looks like an article, with what look like citations. However, this is not "knowledge" and developers should not rely on LLMs to produce factual information. RE: Chinese Room Thought Experiment -GTKlondike_

_I do not think this is a vulnerability. It can be combined with "Training Data Poisoning" which leads to LLM behavior changes -- Manjesh S_

_This seems to be a combination of "I have data which is unrelated or might have non-obvious connections" and "data is being combined together to generate some output" which might have generate an answer which seems true but is actually false. I think providing some kind of validation testing requirements or assessment of why this connection was made should be included as some form of address here. Although this might be addressed by an output confidence interval discussed below. - James Rabe_

### LLM04:2023 - Overreliance on LLM-generated Content
**Description:**  
Excessive dependence on LLM-generated content without human oversight can result in harmful consequences.

_I believe this is an important topic. I think this would need a more thorough description. Furthermore, as a countermeasure I would suggest adding a policy that defines how LLMs/GenAI is used within companies. This topic is difficult to tackle technical imho, as the discussion for the next item, which is related also details - Matteo Große-Kampmann_

_I would more or less combine this with the Hallucination issue. The problem is that LLMs might be used naively and relied on too much, and due to known fact of hallucination or otherwise incorrect answers, the LLM-relying application might not be safe to use in some critical function like controlling physical infrastructure or making health related decisions without human oversight etc. I think this is different from alignment problems, which is a big topic of itself._

_The heading could revised a bit, but not yet sure what would a better one. Some ideas from the top of my head are "Overreliance on LLMs" or "Lack of human oversight in critical tasks" or something. - Otto Sulin_

### LLM05:2023 - Inadequate AI Alignment
**Description:**  
Failing to ensure that the LLM's objectives and behavior align with the intended use case, leading to undesired consequences or vulnerabilities.

_This item feels out of place in this list. I think that ensuring AI Alignment is going to be an incredibly important issue (possibly the MOST important issue that we will face with AI over the coming years), but it feels a bit like lip service in this context. Most of the the other items on the list represent more or less technical concerns with LLMs and their implementation. Alignment feels like a concern for a broader context. - David Taylor_

_I agree -- and think there's a good argument for "Overreliance on LLM generated content" being put in the same bucket. - Rich Harang_

_I also agree, AI alignment is a huge sub field of AI research on its own and is an ongoing debate in AI community as to what that even looks like. I don't think we can add anything meaningful that hasn't already been said without massively widening the scope. Think we are best focusing our efforts to purely technical issues/risks that a developer needs to aware of when implementing a LLM into their business. They may have not trained the model or designed it and are just bolting it on to a business use case. - Thomas McCarthy_

_Agreed +2. The same holds for the next two categories. In general it feels like the other 7 categories over-index on security vulnerabilities, and these 3 categories lump together everything else into broad buckets. I suspect this is a function of the core group that proposed the current top-10 being heavy in MLSec. That flaw should be corrected by soliciting inputs from people from broad expertise._
_As a guiding resource, I'd advise taking a look at the AI Vulnerability Database [taxonomy](https://avidml.org/taxonomy/) and other LLM taxonomies to estimate overindexed areas of the ML lifecycke attack surface. - Subho Majumdar_

_AI alignment deals with goals & incentives, see e.g. [here](https://en.wikipedia.org/wiki/AI_alignment) -> the security/safety issue is about misaligned goals of model. The suggested "LLM04:2023 - Overreliance on LLM-generated Content" deals with how much we as developers trust the system to do its job reliably, securely and safely. We can have a perfectly aligned AI system, while still relying too much on its limited capabilities (e.g. control municipal water system without supervision, probably not a good idea at this point)._

_ The controls are different also:_
* _For AI alignment, the risk is controlled when the model is trained or sometimes when deployed, in case of e.g. system prompts._
* _For reliance issues, it's more a question of restricting its use and assessing risks of using it for a given purpose_

_- Otto Sulin_

### LLM06:2023 - Inexplicability
**Description:**  
The LLM may produce output which is hard to understand or debug

_Maybe "...understand the source of or easily remediate, even if full retraining is a possibility." ? This is also another one of the ones where I shrug a bit and say "deep learning models do be like that sometimes"; the border between "vulnerability" and "man I wish the models didn't work this way" is hard to nail down for me. -Rich Harang_ 

_Can we get some sample examples of possible impacts of this? This doesn't looks like a "vulnerability" -- Manjesh S_

### LLM07:2023 - Bias
**Description:**  
LLMs reflect their training data, which usually include biased representations of the world, such as nurses are women and doctors are men. This differs from intentionally poisoned training data in that the biases are present in the world.

_"...which may include biased representations..." and "...in that the biases are a result of data collection and inadequate data cleaning." maybe? -Rich Harang_ 

_Except for the obvious discrimination potential here, is there a way this affects security? - Matteo_

_Bias reflects the performance and accuracy of the LLM system. If the AI model is trained on biased or unrepresentative data, it may make unfair or discriminatory decisions, leading to incorrect or biased outcomes. So this is more of a functional issue more than a security issue. - Vinay Vishwanatha

### LLM08:2023 - Training Data Poisoning
**Description:**  
Maliciously manipulating training data or fine-tuning procedures to introduce vulnerabilities or backdoors into the LLM.

_Or unwanted biases, or even potential regulatory violations such as PII/personal data. -Rich Harang_

_It feels like LLM07 and LLM08 are related - inadvertently introducing bias (or errors) in the training data, or intentionally doing so. - David Taylor_

### LLM09:2023 - Insure development 
**Description:**  
Failure to address 'traditional' appsec issues that apply to all systems, including LLMs.

_This, IMO, can be split up and made much more actionable as well as accessible to "traditional" security folks.  Off the top of my head: Improper authorization between LLM and system components; inadequate input sanitization of user and third-party prompt content; inadequate output sanitization and validation of LLM results; inadequate parameterization of plugin inputs; inadequate controls on LLM training and/or fine-tuning data; use of uninspected / untrusted training data; use of an untrusted/unaudited foundation model; inadequate controls on training code and training process; inadequate controls on model storage and loading; inadequate logging of model input, output, and plugin calls; Improper delegation of authorization between users and components. - Rich Harang_

_I am having trouble differentiating insure development from insecure development or is this just a typo in the header? - Matteo_

### LLM10:2023 - Insecure deployment
**Description:**  
Failing to properly isolate LLMs when they have access to external resources or sensitive systems, allowing for potential exploitation and unauthorized access.
_Should this reference to some secure development procedures? - Matteo_

## Detail Pages

### LLM01:2023 - Prompt Injections 

**Description:**  
Prompt injections involve bypassing filters or manipulating the LLM using carefully crafted prompts that make the model ignore previous instructions or perform unintended actions. These vulnerabilities can lead to unintended consequences, including data leakage, unauthorized access, or other security breaches.

**Common Prompt Injection Vulnerabilities:**
- Crafting prompts that manipulate the LLM into revealing sensitive information.
- Bypassing filters or restrictions by using specific language patterns or tokens.
- Exploiting weaknesses in the LLM's tokenization or encoding mechanisms.
- Misleading the LLM to perform unintended actions by providing misleading context.
- Exploiting the LLMs inherent biases to influence the LM's response in a particular direction, leading to other listed PI vulnerabilies or generating false, toxic, or misleading information - Andy Dyrcz

**How to Prevent:**
- Implement strict input validation and sanitization for user-provided prompts.
- Use context-aware filtering and output encoding to prevent prompt manipulation.
- Regularly update and fine-tune the LLM to improve its understanding of malicious inputs and edge cases.
- Monitor and log LLM interactions to detect and analyze potential prompt injection attempts.
- Train language models with diverse datasets that include counterexamples to biased or misleading prompts can help make them more robust against prompt injection attacks. - Andy Dyrcz

**Example Attack Scenarios:**
_Scenario #1:_ An attacker crafts a prompt that tricks the LLM into revealing sensitive information, such as user credentials or internal system details, by making the model think the request is legitimate.

_Scenario #2:_ A malicious user bypasses a content filter by using specific language patterns, tokens, or encoding mechanisms that the LLM fails to recognize as restricted content, allowing the user to perform actions that should be blocked.

_Scenario #3:_ Attackers can craft prompts that trigger biased responses from the model, potentially propagating discrimination or misinformation. - Andy Dyrcz

### LLM01b:2023 - Indirect Prompt Injections

**Description:**

A vulnerability in LLM-Integrated Applications which enables malicious actors to remotely exploit said applications by injecting prompts into data likely to be retrieved at inference time by the LLM. The processing of these retrieved prompts can lead to arbitrary code execution, data theft and denial of service. The sophistication of the AI makes social engineering of users to disclose sensitive information particularly concerning. Based on paper "Not what you’ve signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection" [1]

**Common indirect Prompt Injection Vulnerabilities:**

- Passive: Prompts embedded in websites that AI will visit to retrieve.
- Active: Prompt could be injected by sending an email that contained the prompt and could be processed by automated spam detection, personal assistant models, or new LLMs-augmented email client
- User-driven: The user could be convinced or socially engineered to enter the malicious prompt unknowingly. For example copy and pasting into the chatbot from a malicious website such as an invisible single-pixel markdown image [2]
- Hidden: Initial smaller injection could lead AI to reach out for the larger payload.

**How to Prevent:**

- Safety focused Reinforcement learning with Human Feedback (RLHF) (unclear how well this mitigates)
- Unclear if filtering can be effective mitigation. Evaded by more obfuscation and encoding.
- LLM supervisor model that doesn't ingest content but can detect attack attempts.

**Example Attack Scenarios:** 

*Scenario #1:* 

A chatbot can be led to engage a user in conversation that leads to the user revealing sensitive information, such as the example here: Using indirect prompt injection chatbot was able to act as a Microsoft sales agent and was able to extract credit card number.

[1]: https://arxiv.org/pdf/2302.12173.pdf
[2]: https://systemweakness.com/new-prompt-injection-attack-on-chatgpt-web-version-ef717492c5c2





### LLM02:2023 - Data Leakage

**Description:**  
Data leakage occurs when an LLM accidentally reveals sensitive information, proprietary algorithms, or other confidential details through its responses. This can result in unauthorized access to sensitive data or intellectual property, privacy violations, and other security breaches.

**Common Data Leakage Vulnerabilities:**
- Incomplete or improper filtering of sensitive information in the LLM's responses.
- Overfitting or memorization of sensitive data in the LLM's training process.
- Unintended disclosure of confidential information due to LLM misinterpretation or errors.

**How to Prevent:**
- Implement strict output filtering and context-aware mechanisms to prevent the LLM from revealing sensitive information.
- Use differential privacy techniques or other data anonymization methods during the LLM's training process to reduce the risk of overfitting or memorization.
- Regularly audit and review the LLM's responses to ensure that sensitive information is not being disclosed inadvertently.
- Monitor and log LLM interactions to detect and analyze potential data leakage incidents.

**Example Attack Scenarios:**
_Scenario #1:_ A user inadvertently asks the LLM a question that could reveal sensitive information. The LLM, lacking proper output filtering, responds with the confidential data, exposing it to the user.

_Scenario #2:_ An attacker deliberately probes the LLM with carefully crafted prompts, attempting to extract sensitive information that the LLM has memorized from its training data.

By understanding and addressing the risks associated with data leakage, developers can better protect their LLM implementations and ensure the safety and security of their systems.

### LLM03:2023 - Inadequate Sandboxing

**Description:**  
Inadequate sandboxing occurs when an LLM is not properly isolated when it has access to external resources or sensitive systems. This can lead to potential exploitation, unauthorized access, or unintended actions by the LLM.

**Common Inadequate Sandboxing Vulnerabilities:**
- Insufficient separation of the LLM environment from other critical systems or data stores.
- Allowing the LLM to access sensitive resources without proper restrictions.
- Failing to limit the LLM's capabilities, such as allowing it to perform system-level actions or interact with other processes.

**How to Prevent:**
- Implement proper sandboxing techniques to isolate the LLM environment from other critical systems and resources.
- Restrict the LLM's access to sensitive resources and limit its capabilities to the minimum required for its intended purpose.
- Regularly audit and review the LLM's environment and access controls to ensure that proper isolation is maintained.
- Monitor and log LLM interactions to detect and analyze potential sandboxing issues.

**Example Attack Scenarios:**
_Scenario #1:_ An attacker exploits an LLM's access to a sensitive database by crafting prompts that instruct the LLM to extract and reveal confidential information.

_Scenario #2:_ The LLM is allowed to perform system-level actions, and an attacker manipulates it into executing unauthorized commands on the underlying system.

By understanding and addressing the risks associated with inadequate sandboxing, developers can better protect their LLM implementations and ensure the safety and security of their systems.

### LLM04:2023 - Unauthorized Code Execution

**Description:**  
Unauthorized code execution occurs when an attacker exploits an LLM to execute malicious code, commands, or actions on the underlying system through natural language prompts.

**Common Unauthorized Code Execution Vulnerabilities:**
- Failing to sanitize or restrict user input, allowing attackers to craft prompts that trigger the execution of unauthorized code.
- Inadequate sandboxing or insufficient restrictions on the LLM's capabilities, allowing it to interact with the underlying system in unintended ways.
- Unintentionally exposing system-level functionality or interfaces to the LLM.

**How to Prevent:**
- Implement strict input validation and sanitization processes to prevent malicious or unexpected prompts from being processed by the LLM.
- Ensure proper sandboxing and restrict the LLM's capabilities to limit its ability to interact with the underlying system.
- Regularly audit and review the LLM's environment and access controls to ensure that unauthorized actions are not possible.
- Monitor and log LLM interactions to detect and analyze potential unauthorized code execution issues.

**Example Attack Scenarios:**
_Scenario #1:_ An attacker crafts a prompt that instructs the LLM to execute a command that launches a reverse shell on the underlying system, granting the attacker unauthorized access.

_Scenario #2:_ The LLM is unintentionally allowed to interact with a system-level API, and an attacker manipulates the LLM into executing unauthorized actions on the system.

By understanding and addressing the risks associated with unauthorized code execution, developers can better protect their LLM implementations and ensure the safety and security of their systems.

### LLM05:2023 - SSRF Vulnerabilities

**Description:**  
Server-side Request Forgery (SSRF) vulnerabilities occur when an attacker exploits an LLM to perform unintended requests or access restricted resources, such as internal services, APIs, or data stores.

**Common SSRF Vulnerabilities:**
- Insufficient input validation, allowing attackers to manipulate LLM prompts to initiate unauthorized requests.
- Inadequate sandboxing or resource restrictions, enabling the LLM to access restricted resources or interact with internal services.
- Misconfigurations in network or application security settings, exposing internal resources to the LLM.

**How to Prevent:**
- Implement rigorous input validation and sanitization to prevent malicious or unexpected prompts from initiating unauthorized requests.
- Enforce proper sandboxing and restrict the LLM's access to network resources, internal services, and APIs.
- Regularly audit and review network and application security settings to ensure that internal resources are not inadvertently exposed to the LLM.
- Monitor and log LLM interactions to detect and analyze potential SSRF vulnerabilities.

**Example Attack Scenarios:**
_Scenario #1:_ An attacker crafts a prompt that instructs the LLM to make a request to an internal service, bypassing access controls and gaining unauthorized access to sensitive information.

_Scenario #2:_ A misconfiguration in the application's security settings allows the LLM to interact with a restricted API, and an attacker manipulates the LLM to access or modify sensitive data.

By understanding and addressing the risks associated with SSRF vulnerabilities, developers can better protect their LLM implementations and ensure the safety and security of their systems.

### LLM06:2023 - Overreliance on LLM-generated Content

### Description
Overreliance on LLM-generated content can lead to the propagation of misleading or incorrect information, decreased human input in decision-making, and reduced critical thinking. Organizations and users may trust LLM-generated content without verification, leading to errors, miscommunications, or unintended consequences.

Common issues related to overreliance on LLM-generated content include:
- Accepting LLM-generated content as fact without verification.
- Assuming LLM-generated content is free from bias or misinformation.
- Relying on LLM-generated content for critical decisions without human input or oversight.

### How to Prevent
To prevent issues related to overreliance on LLM-generated content, consider the following best practices:
- Encourage users to verify LLM-generated content and consult alternative sources before making decisions or accepting information as fact.
- Implement human oversight and review processes to ensure LLM-generated content is accurate, appropriate, and unbiased.
- Clearly communicate to users that LLM-generated content is machine-generated and may not be entirely reliable or accurate.
- Train users and stakeholders to recognize the limitations of LLM-generated content and to approach it with appropriate skepticism.
- Use LLM-generated content as a supplement to, rather than a replacement for, human expertise and input.

### Example Attack Scenarios
**Scenario #1**: A news organization uses an LLM to generate articles on a variety of topics. The LLM generates an article containing false information that is published without verification. Readers trust the article, leading to the spread of misinformation.

**Scenario #2**: A company relies on an LLM to generate financial reports and analysis. The LLM generates a report containing incorrect financial data, which the company uses to make critical investment decisions. This results in significant financial losses due to the reliance on inaccurate LLM-generated content.

### LLM07:2023 - Inadequate AI Alignment

**Description:**  
Inadequate AI alignment occurs when the LLM's objectives and behavior do not align with the intended use case, leading to undesired consequences or vulnerabilities.

**Common AI Alignment Issues:**
- Poorly defined objectives, causing the LLM to prioritize undesired or harmful behaviors.
- Misaligned reward functions or training data, resulting in unintended model behavior.
- Insufficient testing and validation of LLM behavior in various contexts and scenarios.

**How to Prevent:**
- Clearly define the objectives and intended behavior of the LLM during the design and development process.
- Ensure that the reward functions and training data are aligned with the desired outcomes and do not encourage undesired or harmful behavior.
- Regularly test and validate the LLM's behavior across a wide range of scenarios, inputs, and contexts to identify and address alignment issues.
- Implement monitoring and feedback mechanisms to continuously evaluate the LLM's performance and alignment, and update the model as needed to improve alignment.

**Example Attack Scenarios:**
_Scenario #1:_ An LLM trained to optimize for user engagement inadvertently prioritizes controversial or polarizing content, resulting in the spread of misinformation or harmful content.

_Scenario #2:_ An LLM designed to assist with system administration tasks is misaligned, causing it to execute harmful commands or prioritize actions that degrade system performance or security.

By focusing on AI alignment and ensuring that the LLM's objectives and behavior align with the intended use case, developers can reduce the risk of unintended consequences and vulnerabilities in their LLM implementations.

### LLM08:2023 - Insufficient Access Controls

**Description:**  
Insufficient access controls occur when access controls or authentication mechanisms are not properly implemented, allowing unauthorized users to interact with the LLM and potentially exploit vulnerabilities.

**Common Access Control Issues:**
- Failing to enforce strict authentication requirements for accessing the LLM.
- Inadequate role-based access control (RBAC) implementation, allowing users to perform actions beyond their intended permissions.
- Failing to provide proper access controls for LLM-generated content and actions.

**How to Prevent:**
- Implement strong authentication mechanisms, such as multi-factor authentication, to ensure that only authorized users can access the LLM.
- Use role-based access control (RBAC) to define and enforce user permissions based on their roles and responsibilities.
- Implement proper access controls for content and actions generated by the LLM to prevent unauthorized access or manipulation.
- Regularly audit and update access controls as needed to maintain security and prevent unauthorized access.

**Example Attack Scenarios:**
_Scenario #1:_ An attacker gains unauthorized access to an LLM because of weak authentication mechanisms, allowing them to exploit vulnerabilities or manipulate the system.

_Scenario #2:_ A user with limited permissions is able to perform actions beyond their intended scope due to inadequate RBAC implementation, potentially causing harm or compromising the system.

By properly implementing access controls and authentication mechanisms, developers can prevent unauthorized users from interacting with the LLM and reduce the risk of vulnerabilities being exploited.

### LLM09:2023 - Improper Error Handling

**Description:**  
Improper error handling occurs when error messages or debugging information are exposed in a way that could reveal sensitive information, system details, or potential attack vectors to an attacker.

**Common Improper Error Handling Issues:**
- Exposing sensitive information or system details through error messages.
- Leaking debugging information that could help an attacker identify potential vulnerabilities or attack vectors.
- Failing to handle errors gracefully, potentially causing unexpected behavior or system crashes.

**How to Prevent:**
- Implement proper error handling mechanisms to ensure that errors are caught, logged, and handled gracefully.
- Ensure that error messages and debugging information do not reveal sensitive information or system details. Consider using generic error messages for users, while logging detailed error information for developers and administrators.
- Regularly review error logs and take necessary actions to fix identified issues and improve system stability.

**Example Attack Scenarios:**
_Scenario #1:_ An attacker exploits an LLM's error messages to gather sensitive information or system details, enabling them to launch a targeted attack or exploit known vulnerabilities.

_Scenario #2:_ A developer accidentally leaves debugging information exposed in production, allowing an attacker to identify potential attack vectors or vulnerabilities in the system.

By implementing proper error handling mechanisms and ensuring that error messages do not reveal sensitive information, developers can reduce the risk of attackers exploiting LLM vulnerabilities and improve system stability.

### LLM10:2023 - Training Data Poisoning

**Description:**  
Training data poisoning occurs when an attacker manipulates the training data or fine-tuning procedures of an LLM to introduce vulnerabilities, backdoors, or biases that could compromise the model's security, effectiveness, or ethical behavior.

**Common Training Data Poisoning Issues:**
- Introducing backdoors or vulnerabilities into the LLM through maliciously manipulated training data.
- Injecting biases into the LLM, causing it to produce biased or inappropriate responses.
- Exploiting the fine-tuning process to compromise the LLM's security or effectiveness.

**How to Prevent:**
- Ensure the integrity of the training data by obtaining it from trusted sources and validating its quality.
- Implement robust data sanitization and preprocessing techniques to remove potential vulnerabilities or biases from the training data.
- Regularly review and audit the LLM's training data and fine-tuning procedures to detect potential issues or malicious manipulations.
- Utilize monitoring and alerting mechanisms to detect unusual behavior or performance issues in the LLM, potentially indicating training data poisoning.
- _Provide confidence intervals on data used to generate LLM outputs to allow users to gauge validity of data based on reference integrity (frequently referenced data may be more credible) or source credibility - James Rabe_

**Example Attack Scenarios:**
_Scenario #1:_ An attacker infiltrates the training data pipeline and injects malicious data, causing the LLM to produce harmful or inappropriate responses.

_Scenario #2:_ A malicious insider compromises the fine-tuning process, introducing vulnerabilities or backdoors into the LLM that can be exploited at a later stage.

By ensuring the integrity of the training data, implementing robust data sanitization techniques, and regularly auditing the LLM's training and fine-tuning processes, developers can minimize the risk of training data poisoning and protect their LLMs from potential vulnerabilities.

## Andy's thoughts
Hopefully this is the right place for some initial thoughts (from Andy Smith):
* LLM01 - Prompt injection could come from a few different sources; either directly from user input, or indirectly through resources accessed by the LLM in the course of responding to a prompt. Maybe split this out into two, or at least discuss the two variations in this single item.

   _I agree with it too. Good to have subcategories:
      1. Direct Prompt Injection
      2. Indirect Prompt Injection -- Manjesh S_

* LLM03 - "Sandboxing" to me suggests the addition of sandbox controls to limit what an LLM can do. But in paractice, an LLM actually can't *do* anything unless specific integrations are created. So I'd suggest reframing/renaming this item, maybe as "Excessive agency" or "Excessive autonomy".
* LLM04 - This feels like a very specific spin on LLM03, and I'm not yet convinced there's value in calling it out specifically.
* LLM05 - Feels very similar to LLM03 again... or perhaps I'm just missing the nuance?

_I agree that LLM03, LLM04 and LLM05 all seem to stem from the same issue of the integrations that have been provided to the model. - David Taylor_

* LLM06 - May wish to supplement with points on human-in-the-loop / on-the-loop. Include psychological factors and human empowerment. Call out hallucination of 'facts'.
* LLM08 - Is this really such a big deal? Seems quite generic and not really LLM-specific.
* LLM09 - As before, feels quite generic and not really LLM-specific.
* Potential new item: Something around breaching Legal/Compliance regs on what AI systems can be used for, especially given several countries are actively looking to implement controls on GenAI.


## Felix's thoughts (in slack channel - @continuous-intuition) thoughts
* Additional potential Risk Candidate:

### LLMXX:2023 - Trained Model Theft (TMT)

**Description:**  
Exposure of trained model data will become increasingly problematic based on the computational resources, time and intellectual property used to train new models. Additionally models specialized with private data (think trained models around business data or intellectual property of an organization) will be increasingly sought after targets by attackers. 

**Common Elements Contributing to TMT:**
- Inappropriate data handling. Trained Model artifacts should be treated with similar levels of care as the types of data present that they are trained on. When the trained model itself becomes a competitive advantage, it becomes a higher level of sensitivity even with non-sensitive training data. 
- Backups - Care should be taken with backups to ensure protection of proprietary models.
- Misconfigurations in network or application security settings, exposing internal resources such as models themselves erroneously while attempting to expose their functionality.

**How to Prevent:**
- Implement appropriate classification of sensitivity of trained models and data artifacts that aligns to the sensitivity of source data or the sensitivity of the final model.
- Enforce proper sandboxing and restrict the LLM's access to network resources, internal services, and APIs.
- Regularly audit and review network and application security settings to ensure that internal resources are not inadvertently exposed to the public internet or untrusted exposure such as unapproved business partners.
- Leverage data security controls around trained model data files where possible with data loss prevention tools include the common file types associated with trained artifacts as sensitive data types, add regex to dictionaries that align to specific model keywords that can help in identification of trained model data.

**Example Attack Scenarios:**
_Scenario #1:_ An attacker crafts a prompt that instructs the LLM to make a request to an internal service, bypassing access controls and gaining unauthorized access to sensitive information, then steals trained model information.

_Scenario #2:_ A misconfiguration leads to compromise of a server within a shared enterprise environment where data models exist within data stores accessible within the environment (network file shares, cloud storage locations, local to servers, etc.), the attacker then exfiltrates the trained model information.

## Otto Sulin's thoughts

* I would include model theft suggested by Felix above, it is real concern also for LLMs like other ML models.

* Adding "Insufficient or poor training data" should be considered. Let's say we want to use LLM for fraud prevention, but the data would be insufficient or of poor quality => bypassing the LLM powered fraud detector would be easier and has real consequences.

* Adding "Model bypass" should also be considered. With model bypass, I'm pointing to cases where you can include some content in the input which makes the model perform poorly (i.e. different from prompt injection, which makes the model do completely something else) in whatever it is supposed to do.

* As I'm suggesting three new vulnerabilities, I feel I need also point out which should be removed. I would remove 1) "Bias" - ethical & compliance issue, not a security issue and 2) "Hallucination", as it is a "feature" of LLMs (overreliance on LLMs is the real problem if we blindly use its hallucinations) and possibly also 3) "Insecure development" as it is overly broad and not specific to LLMs.

## Patrick Biyaga contribution-See-Docs & Thenavigo (start)


**Description:** 

When will building our own LLM models at See-Docs & Thenavigo, will understanding the fundamentals will be necessary to produce high-quality work. Here's a summary of my latest training course on AI. Machine Learning (ML) has transformed numerous industries, enabling businesses to extract valuable insights from vast amounts of data. However, implementing successful ML solutions comes with its own set of challenges. We will explore the top 10 challenges faced by ML practitioners and discuss strategies to overcome them.

1. [Data Quality:]()

ML engineers often struggle with issues related to data quality, including missing, inconsistent, or erroneous data. Cleaning and preprocessing data can be time-consuming and challenging.

2. [Feature Engineering:]()

Selecting the right features and transforming them appropriately can significantly impact model performance. Engineers may find it challenging to engineer meaningful features, especially for complex datasets.

3. [Model Selection:]()

Choosing the right ML or deep learning model for a specific problem can be challenging. Engineers need to consider factors such as model complexity, interpretability, and suitability for the task at hand.

4. [Hyperparameter Tuning:]()

Finding the optimal hyperparameters for an ML or deep learning model can be a complex and computationally expensive process. Engineers may struggle to efficiently tune hyperparameters to improve model performance.

5. [Overfitting and Underfitting:]()

Overfitting occurs when a model performs well on training data but poorly on new data, while underfitting occurs when a model is too simple to capture patterns in the data. Balancing model complexity to avoid both issues can be challenging for ML engineers.

6. [Imbalanced Data:]()

Engineers may encounter datasets with imbalanced classes, where one class is significantly underrepresented. This can lead to biased models that perform poorly on the minority class. Techniques such as resampling or using different evaluation metrics may be needed.

7. [Model Interpretability:]()

Complex models, such as deep neural networks, can be difficult to interpret and explain. Engineers may struggle to provide meaningful explanations for model predictions, especially in regulated industries where interpretability is important.


8. [Scalability:]()

Engineers may face challenges when scaling ML and deep learning models to handle large datasets. Efficiently processing and analyzing big data often requires distributed computing, specialized tools, and cloud-based infrastructure.

9. [Deployment and Maintenance:]()

Deploying ML and deep learning models into production and maintaining them over time can be challenging. Engineers need to consider factors such as model monitoring, versioning, updating models as new data becomes available, and ensuring low-latency predictions in production environments.

10. [Hardware Acceleration:]()

Deep learning models, in particular, can be computationally intensive and may require hardware acceleration using GPUs or TPUs. Engineers may struggle with optimizing models to run efficiently on specialized hardware and managing the associated computational resources.


# More Thoughts on ML/AI and Cybersecurity.

1. [Resource 1:](https://medium.com/python-and-machine-learning-pearls/top-10-machine-learning-challenges-and-how-to-overcome-them-ca5968f83cfb)

2. [Resource 2:](https://github.com/kyegomez/tree-of-thoughts)

3. [Resource 3:](https://www.ml4devs.com/articles/mlops-machine-learning-life-cycle/#machine-learning-life-cycle)



**Next Apply cybersecurity at every stage of the model process.** 

A few questions to ask yourself:

* What are the most important assets to protect?
* What are the layers of protection in place?
* How do we know if we’ve been breached? How do we detect a breach?
* What are our response plans in the event of an incident?
* What is the board's role in the event of an incident?
* What are our business recovery plans in the event of a cyber incident?
* Is our cybersecurity investment enough?

## Contribution-See-Docs & Thenavigo (end)



## **Eugene Tawiah's thoughts** ## 

_Taking a look at what's already been shared in this area, I don't recall seeing these points raised. Perhaps they were raised elsewhere. Perhaps with overlap this can be seen as categories in an attempt to organize potential vulns and threats._

1. **Adversarial Attacks:** When an attacker deliberately manipulates the input to an LLM to produce a specific desired response or to cause the model to malfunction. Note: I don't mean prompt injection as this has already been mentioned. The goal here is not to bypass filters or manipulate the LLM's behavior, but to cause it to output incorrect or harmful information.

2. **Reverse Engineering:** Attempts to understand the underlying functionality of an LLM with the goal of exploiting it. Successful attempts could result in revealing proprietary algorithms or understanding how to manipulate the LLM's responses.

3. **Resource Exhaustion:** Remember DoS? An attacker can overload the LLM's computational resources. Successful attempts could slow down, increase cost, or disrupt the services provided by the LLM. 

4. **Privacy Erosion:** The potential for an LLM to infringe on privacy by storing, processing, or revealing sensitive information, beyond what is covered by data leakage.

5. Inference Attacks: An adversary can infer sensitive information from the outputs of an LLM, such as guessing the training data based on the LLM's responses.





## Gavin's thoughts (@GTKlondike)
1. What are we considering a "vulnerability"? I think we should define this more appropriately when it comes to LLMs in a security context. The original proposal (and the alternate version) include both: things that are vulnerabilities (in the traditional sense) and things that are part of the core functionality of an LLM (I would consider, not a vulnerability).
2. Looking at LLM04 (Unauthorized Code Execution) and LLM05 (SSRF Vulnerabilities), both would fall under the same umbrella. Maybe OVERLY PERMISSIVE COMMAND EXECUTION or UNFILTERED COMMAND EXECUTION, or something to that effect. I've been seeing a number of CVEs coming out of LangChain where people have used LLMs and pointed them directly to an exec(); function. This needs to be called out.
3. I'd also like to change LLM02 from Data Leakage to Sensitive Data Exposure. To be precise, LLM's don't "leak" data. They're statistical models that return information based on what they've seen in the past. So if one has seen my medical records, then it's possible it will be able to show that to someone else. The fix would be to not include sensitive information in the training data at all, and sanitize training data prior to fine tuning.







## Austin Stubbs' Prompt Injection Technique Research

I've condensed my research for different Prompt Injection techniques into a single space where I update here:
https://medium.com/@austin-stubbs/llm-security-types-of-prompt-injection-d7ad8d7d75a3

The link has all of the techniques and their examples of working in the wild, but for now I will just place the overall defined and separable techniques with their definitions here: 

1.) Jailbreaking / Mode Switching

Jailbreaking usually refers to Chatbots which have successfully been prompt injected and now are in a state where the user can ask any question they would like. This has been seen with “DAN” and “Developer Mode” prompts.

2.) Obfuscation / Token Smuggling

Obfuscation is a simple technique that attempts to evade filters. In particular, you can replace certain words that would trigger filters with synonyms of themselves or modify them to include a typo.

3.) Payload Splitting

Payload splitting involves splitting the adversarial input into multiple parts, and then getting the LLM to combine and execute them.

4.) Virtualization

Virtualization involves “setting the scene” for the AI, in a similar way to mode prompting. Within the context of this scene, the malicious instruction makes sense to the model and bypasses it’s filters.

5.) Indirect Injection

Indirect prompt injection is a type of prompt injection, where the adversarial instructions are introduced by a third party data source like a web search or API call.

6.) Code Injection

Code injection is a prompt hacking exploit where the attacker is able to get the LLM to run arbitrary code (often Python). This can occur in tool-augmented LLMs, where the LLM is able to send code to an interpreter, but it can also occur when the LLM itself is used to evaluate code.

7.) Prompt Leaking/Extraction

Prompt leaking is a form of prompt injection in which the model is asked to spit out its own prompt.

## Aleksei Ryzhkov's thoughts
1) Agree with the proposal to add DoS to Top10.

The way LLM solves tasks is quite unpredictable and unclear (compared with the program code or SQL-query, where we can go to the code, review it and debug to optimize).
So we should put some limits to prevent excessive resource usage.
While we are using LLM from 3rd-party providers - this issue is solved primarily on their side. But will be especially our headache if hosting our LLM.
One example inspired me for this thought - the way ChatGPT tried to summarize the article: I have no idea why it clicked so many times to the article link and finally resulted in 'time out' phrase
![image](https://github.com/OWASP/www-project-top-10-for-large-language-model-applications/assets/1675819/bacbfc29-b8d5-4aa6-ab9d-69e29e94055c)

2) +1 for 'LLM06 Model Inexplicability' item (not sure how to call it).

In the case of regular applications - I can go to the program code and find malicious instructions.
But in the case of LLM-based program - looks like I have no way to find out if the model was poisoned (until the backdoor was exploited) or why the model does these particular things while I was expecting another.
Especially this article (https://arxiv.org/abs/2305.14710) makes me worry about these phrases:
      "Our studies demonstrate that an attacker can inject backdoors by issuing very few malicious instructions among thousands of gathered data and 
       control model behavior"... "Moreover, the poisoned model cannot be cured by continual learning."
How on earth I can verify if my underlying model was poisoned? Can I trace some particular answer to some specific piece of the model? that was poisoned by someone a year ago? So unclear to me..

3) vote to add an item about compliance challenges.

How to address questions like - can I use this model to process PII data and remain GDPR compliment? HIPPA data - it is possible to sign BAA with LLM-vendor?  What notice should I present to the end user? Some countries could ban the usage of LLM models. 
This landscape is changing rapidly and drives me crazy - so maybe it's good to highlight this complexity.
Related thoughts I see in this article (describing real-world experience) - https://www.honeycomb.io/blog/hard-stuff-nobody-talks-about-llm#llms_force_you_to_address_legal_and_compliance_stuff








