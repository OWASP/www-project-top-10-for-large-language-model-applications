
# OWASP Top 10 LLM Bottom Choices Analysis

This document provides an analysis of the bottom choices for the OWASP Top 10 LLM vulnerabilities, along with expert comments and insights.

## Analysis

### AIAssistedSocialEngineering
**Count:** 15

#### Expert Comments:
- It's not really a vulnerability of LLM/GenAI but rather a misuse of it.
- I'm not disagreeing with what is written in here - yes this is a threat and a valid point. However the LLM TOP 10 is a database of threats acting on LLMs and not where LLMs are a tool of a threat actor. Same goes for 01, 09. 
- Misuse, should be covered by unwanted actions
- An important topic, but not a vulnerability.  It's not appropriate for the Top 10 list, but could be important for other documents the group provides.
- This isn't a problem with LLMs, any model that can generate text can be used in SE ops 

### DeepfakeThreat
**Count:** 7

#### Expert Comments:
- There are number of items can be combined from the 34 list. 
- Not a risk of the use of LLMs. Effectivity or efficiency gains by adversaries is something we cannot control. Other proposals share the same intrinsic problem. Compilers are useful to build trojans too

RAG & finetuning is another off topic
- Should not be included simply because is a vulnerability create by AI not necessarily a risk to an LLM.
- This is not protecting the behaviour of models.

### AdversarialAIRedTeamingCyberOps
**Count:** 6

#### Expert Comments:
- An initiative not a threat or vulnerability. it is rather the responde to ther items
- This doesn’t really seem to be a vuln that is its own stand-alone thing. 
- I just don't think this is a vuln. Also, I think I might have responded to this survey by mistake under unfathomableadventure@gmail.com so if you want to disregard any entry from that email please do.
- I praise not only this but more of this kind of risks, the real problem I want to communicate with this vote is: Red Teaming, Deep Fake and everything else that relates are impossible to withhold at model creation or securization time. I simply do not think these could be shifted left, while I care for the safety of AI use a lot, it's a cultural issue and not a technical issue. Reason for my proposal to set this as a cornerstone of each AI model as a whole (see Ideas in AI Exchange project charter).
- WEAPONIZATION should merge (to get excluded) the following entries = AdversarialAIRedTeamingCyberOps, AIAssistedSocialEngineering, AlignmentValueMismatch, MaliciousLLMTuner, DeepfakeThreat, MultimodelManipulation, VoiceModelMisuse

### VoiceModelMisuse
**Count:** 5

#### Expert Comments:
- I would say it's off-topic and it drifts too far into general AI security. It doesn't have much to do with LLMs. Also all the deep fake threats, AI Assisted Social engineering etc. shouldn't be in the list. 
- Misuse is too loosely defined technically and a never ending battle.  Let's focus on Model control first.
- Can be subsumed more generally by social engineering or phishing campaigns
- While significant, it could be covered under broader categories like "Adversarial Inputs."
- Redundant as a deep fake…maybe…

### MaliciousLLMTuner
**Count:** 4

#### Expert Comments:
- This vulnerability deals specifically with a human in the loop; and borders on insider threat. Besides any additional risk is covered by Supply Chain vulnerabilities . 
- Requires significant technical expertise and inside knowledge, making it less accessible to general attackers.

- Seems a bit niche to me. It can maybe be a part of Supply Chain Vulnerabilities 

### InsecureDesign
**Count:** 3

#### Expert Comments:
- The item is somewhat broad and might not be actionable enough for the guide's audience.
- Too generic
- Insecure design, while a critical concern in the realm of cybersecurity and AI, may not be appropriate as a top-level entry in our vulnerability list due to its broad and foundational nature. Insecure design encompasses a wide range of design flaws and vulnerabilities that can affect AI systems, such as poor authentication mechanisms, lack of encryption, or inadequate access controls. While these issues are crucial to address, they are often considered foundational aspects of cybersecurity rather than specific vulnerabilities unique to AI. Therefore, including insecure design as a top-level entry might dilute the focus on more specialized and AI-specific vulnerabilities that require distinct technical and ethical considerations. However, it remains essential to address insecure design within the broader context of AI vulnerability management to ensure robust cybersecurity practices are applied throughout AI system development and deployment.

### DangerousHallucinations
**Count:** 3

#### Expert Comments:
- Hallucinations are part of using LLMs and usually I have found that they are very obvious especially when double checking to verify. Moreover, when due to operator error.
- Hallucinations are merely a feature of ANNs. It's a the Best Fit Model issue.

### FineTuningRag
**Count:** 3

#### Expert Comments:
- not a vulnerability about LLM
- RAG is a  common Enterprise  IT  usecase with GENAI and lot many  Citizen developers are using it  naively without  taking  proper due  diligence, hence this is an important  attack to take careof.  
- This covers a wide range of topics some of which might fall under reliability rather than vulnerability. eg: Outdated data isn't really a vulnerability

### BackdoorAttacks
**Count:** 2

#### Expert Comments:
- Extremely hard to implement, currently reserved to APT and hence not worthy of a Top-10 spot for general public.
- Not unique to LLMs

### Unwanted-AI-Actions.md
**Count:** 2

#### Expert Comments:
- Importance: Unwanted AI actions are unintended behaviors by AI models. These issues are usually about refining the model rather than being direct security threats.

Top-Level Entry or Folded: This should be excluded from the top-level entries as it’s less of a security risk and more about model performance.

Additional Thoughts: Improving training and testing can help mitigate these issues. Regular updates and thorough testing are essential to ensure AI systems behave as expected.
- Inappropriateness: “Unwanted-AI-Actions” is not suitable for our list because it is too broad and lacks specificity, making it less actionable for targeted security measures.

Off-Topic: This category can overlap with various other specific vulnerabilities, diluting focus and resources from more distinct and critical issues.

Additional Thoughts: Focus on more defined threats like Function Calling Attacks and Adversarial AI Red Teaming. Broad categories should be broken down into specific, actionable items for more effective mitigation and management.

### SystemPromptLeakage
**Count:** 2

#### Expert Comments:
- Too much overlap with Bypassing System Instructions - two could be combined.
- It's unreasonable to expect system prompts to be secure, and it's unclear how to ever mitigate for this.

### SupplyChainVulnerabilities
**Count:** 2

#### Expert Comments:
- I don't think this is specifically scoped to LLMs, and the same advice provided in other OWASP documentation - and other candidates on this list - will help mitigate it for AI in particular.

### ResourceExhaustion
**Count:** 2

#### Expert Comments:
- Resource Exhaustion is more of an infrastructure concern than an LLM or AI concern. It is anyway a general concern that all systems that do work based off of user input take, and I feel like there are methods to limit the resources that an LLM will take up on inference. It can also be bounded above given the size of the model. 
- Should be part of the DoS entry Otherwise it s covered by existing app sec 

### PrivacyViolation
**Count:** 2

#### Expert Comments:
- this should be covered in the governane checklists and PII guides, appsec always processes PII and doesnt need an explicit call out
- This is too similar to my first choice in the list and considered and I consider it duplicated 

### ModelInversion
**Count:** 2

#### Expert Comments:
- Model inversion is near impossible in LLMs. Training Data Extraction is the correct and different risk  (see lateral  NIST adversarial ML taxonomy for an accurate distinction). The latter should be part of sensible data exposrure with more detailed explanations instead of a new entry 

### VulnerableAutonomousAgents
**Count:** 2

#### Expert Comments:
- I believe we are far from truly autonomous agents, and this risk is out of scope for most present day LLM use cases.
- Not clear. Too broad. 

### DevelopingInsecureSourceCode
**Count:** 2

#### Expert Comments:
- perhaps I don't understand the vulnerability but it feels too functional / internal to the LLM application.
if LLM is not fit for purpose then it should not be used, instead of trying to fix it with bolt-on controls

### EmbeddingInversion
**Count:** 2

#### Expert Comments:
- Personally felt like it was very specific and not sure how the exploit could happen in common scenarios.

### InsecureInputHandling
**Count:** 1

#### Expert Comments:
- IMHO this topic is a classic traditional application issue.
It talks about secure transmission of prompts (HTTPS?) secure storage (disk encryption) and more. and input validation is kind of part of prompt injection topic part.

### AdversarialInputs
**Count:** 1

#### Expert Comments:

### AgentAutonomyEscalation
**Count:** 1

#### Expert Comments:

### AlignmentValueMismatch
**Count:** 1

#### Expert Comments:

### UIAccessControlManipulation
**Count:** 1

#### Expert Comments:
- This is more tuned with web app security so that should cover it

### SensitiveInformationDisclosure
**Count:** 1

#### Expert Comments:

### PromptInjection
**Count:** 1

#### Expert Comments:
- Prompt Injection is not a security issue. Solutions to issues created by Prompt Injection fall into other categories and mitigation - for example, Insecure Design.

### ImproperErrorHandling
**Count:** 1

#### Expert Comments:

### Overreliancerewrite
**Count:** 1

#### Expert Comments:

### IndirectContextInjection
**Count:** 1

#### Expert Comments:
- This feels like it's essentially a part of Prompt Injections, or even Adversarial Inputs. Because of that, it feels redundant to me. 

### MultimodalInjections
**Count:** 1

#### Expert Comments:
- More than one issue should/could be excluded as they are already covered by a more general consideration or approach. I will prioritize Multimodal Injections since what is required is a rewrite of Prompt Injection, covering all possible user querying scenarios.

### FunctionCallingAttack
**Count:** 0

#### Expert Comments:

### MultimodelManipulation
**Count:** 0

#### Expert Comments:

### UnauthorizedAccessandEntitlementViolations
**Count:** 0

#### Expert Comments:

### UnrestrictedResourceConsumption
**Count:** 0

#### Expert Comments:

### BypassingSystemInstructionsUsingSystemPromptLeakage
**Count:** 0

#### Expert Comments:

