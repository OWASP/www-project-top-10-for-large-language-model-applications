## LLM01:2025 Prompt Injection
## LLM01: 2025 शीघ्र इंजेक्शन

### Description
### विवरण

A Prompt Injection Vulnerability occurs when user prompts alter the LLM’s behavior or output in unintended ways. These inputs can affect the model even if they are imperceptible to humans, therefore prompt injections do not need to be human-visible/readable, as long as the content is parsed by the model.
एक त्वरित इंजेक्शन भेद्यता तब होती है जब उपयोगकर्ता ने एलएलएम के व्यवहार या आउटपुट को अनपेक्षित तरीकों से बदल दिया। ये इनपुट मॉडल को प्रभावित कर सकते हैं, भले ही वे मनुष्यों के लिए अगोचर हों, इसलिए त्वरित इंजेक्शन को मानव-भ्रामक/पठनीय होने की आवश्यकता नहीं है, जब तक कि सामग्री को मॉडल द्वारा पार्स किया जाता है।

Prompt Injection vulnerabilities exist in how models process prompts, and how input may force the model to incorrectly pass prompt data to other parts of the model, potentially causing them to violate guidelines, generate harmful content, enable unauthorized access, or influence critical decisions. While techniques like Retrieval Augmented Generation (RAG) and fine-tuning aim to make LLM outputs more relevant and accurate, research shows that they do not fully mitigate prompt injection vulnerabilities.
प्रॉम्प्ट इंजेक्शन की कमजोरियां इस बात में मौजूद हैं कि मॉडल प्रक्रिया कैसे संकेत देती है, और कैसे इनपुट मॉडल को गलत तरीके से मॉडल के अन्य हिस्सों में त्वरित डेटा को पारित करने के लिए मजबूर कर सकता है, संभवतः उन्हें दिशानिर्देशों का उल्लंघन करने, हानिकारक सामग्री उत्पन्न करने, अनधिकृत पहुंच को सक्षम करने या महत्वपूर्ण निर्णयों को प्रभावित करने के लिए। जबकि एलएलएम आउटपुट को अधिक प्रासंगिक और सटीक बनाने के लिए पुनर्प्राप्ति संवर्धित पीढ़ी (आरएजी) और फाइन-ट्यूनिंग उद्देश्य जैसी तकनीकों से पता चलता है कि वे पूरी तरह से शीघ्र इंजेक्शन कमजोरियों को कम नहीं करते हैं।

While prompt injection and jailbreaking are related concepts in LLM security, they are often used interchangeably. Prompt injection involves manipulating model responses through specific inputs to alter its behavior, which can include bypassing safety measures. Jailbreaking is a form of prompt injection where the attacker provides inputs that cause the model to disregard its safety protocols entirely. Developers can build safeguards into system prompts and input handling to help mitigate prompt injection attacks, but effective prevention of jailbreaking requires ongoing updates to the model's training and safety mechanisms.
जबकि शीघ्र इंजेक्शन और जेलब्रेकिंग एलएलएम सुरक्षा में संबंधित अवधारणाएं हैं, वे अक्सर परस्पर उपयोग किए जाते हैं। प्रॉम्प्ट इंजेक्शन में इसके व्यवहार को बदलने के लिए विशिष्ट इनपुट के माध्यम से मॉडल प्रतिक्रियाओं में हेरफेर करना शामिल है, जिसमें सुरक्षा उपायों को बायपास करना शामिल हो सकता है। जेलब्रेकिंग शीघ्र इंजेक्शन का एक रूप है जहां हमलावर इनपुट प्रदान करता है जो मॉडल को अपने सुरक्षा प्रोटोकॉल की पूरी तरह से अवहेलना करने का कारण बनता है। डेवलपर्स शीघ्र इंजेक्शन हमलों को कम करने में मदद करने के लिए सिस्टम प्रॉम्प्ट और इनपुट हैंडलिंग में सुरक्षा उपायों का निर्माण कर सकते हैं, लेकिन जेलब्रेकिंग की प्रभावी रोकथाम के लिए मॉडल के प्रशिक्षण और सुरक्षा तंत्र के लिए चल रहे अपडेट की आवश्यकता होती है।

### Types of Prompt Injection Vulnerabilities
### त्वरित इंजेक्शन कमजोरियों के प्रकार

#### Direct Prompt Injections
  Direct prompt injections occur when a user's prompt input directly alters the behavior of the model in unintended or unexpected ways. The input can be either intentional (i.e., a malicious actor deliberately crafting a prompt to exploit the model) or unintentional (i.e., a user inadvertently providing input that triggers unexpected behavior).
#### प्रत्यक्ष शीघ्र इंजेक्शन
  प्रत्यक्ष शीघ्र इंजेक्शन तब होता है जब उपयोगकर्ता का शीघ्र इनपुट सीधे अनपेक्षित या अप्रत्याशित तरीकों से मॉडल के व्यवहार को बदल देता है। इनपुट या तो जानबूझकर हो सकता है (यानी, एक दुर्भावनापूर्ण अभिनेता जानबूझकर मॉडल का फायदा उठाने के लिए एक संकेत को तैयार करता है) या अनजाने में (यानी, एक उपयोगकर्ता अनजाने में इनपुट प्रदान करता है जो अप्रत्याशित व्यवहार को ट्रिगर करता है)।

#### Indirect Prompt Injections
  Indirect prompt injections occur when an LLM accepts input from external sources, such as websites or files. The content may have in the external content data that when interpreted by the model, alters the behavior of the model in unintended or unexpected ways. Like direct injections, indirect injections can be either intentional or unintentional.
#### अप्रत्यक्ष शीघ्र इंजेक्शन
  अप्रत्यक्ष शीघ्र इंजेक्शन तब होता है जब कोई एलएलएम बाहरी स्रोतों से इनपुट स्वीकार करता है, जैसे कि वेबसाइट या फाइलें। सामग्री बाहरी सामग्री डेटा में हो सकती है जो मॉडल द्वारा व्याख्या की जाती है, मॉडल के व्यवहार को अनपेक्षित या अप्रत्याशित तरीकों से बदल देती है। प्रत्यक्ष इंजेक्शन की तरह, अप्रत्यक्ष इंजेक्शन या तो जानबूझकर या अनजाने में हो सकते हैं।

The severity and nature of the impact of a successful prompt injection attack can vary greatly and are largely dependent on both the business context the model operates in, and the agency with which the model is architected. Generally, however, prompt injection can lead to unintended outcomes, including but not limited to:
एक सफल शीघ्र इंजेक्शन हमले के प्रभाव की गंभीरता और प्रकृति बहुत भिन्न हो सकती है और बड़े पैमाने पर व्यवसाय के संदर्भ में दोनों के संदर्भ में निर्भर होती है, और जिस एजेंसी के साथ मॉडल आर्किटेक्चर है। आम तौर पर, हालांकि, त्वरित इंजेक्शन अनपेक्षित परिणामों को जन्म दे सकता है, लेकिन इसमें सीमित नहीं है:

- Disclosure of sensitive information
- Revealing sensitive information about AI system infrastructure or system prompts
- Content manipulation leading to incorrect or biased outputs
- Providing unauthorized access to functions available to the LLM
- Executing arbitrary commands in connected systems
- Manipulating critical decision-making processes
- संवेदनशील जानकारी का प्रकटीकरण
- एआई सिस्टम इन्फ्रास्ट्रक्चर या सिस्टम प्रॉम्प्ट के बारे में संवेदनशील जानकारी का खुलासा करना
- सामग्री हेरफेर गलत या पक्षपाती आउटपुट के लिए अग्रणी
- एलएलएम के लिए उपलब्ध कार्यों के लिए अनधिकृत पहुंच प्रदान करना
- कनेक्टेड सिस्टम में मनमानी आदेशों को निष्पादित करना
- महत्वपूर्ण निर्णय लेने की प्रक्रियाओं में हेरफेर करना

The rise of multimodal AI, which processes multiple data types simultaneously, introduces unique prompt injection risks. Malicious actors could exploit interactions between modalities, such as hiding instructions in images that accompany benign text. The complexity of these systems expands the attack surface. Multimodal models may also be susceptible to novel cross-modal attacks that are difficult to detect and mitigate with current techniques. Robust multimodal-specific defenses are an important area for further research and development.
मल्टीमॉडल एआई का उदय, जो एक साथ कई डेटा प्रकारों को संसाधित करता है, अद्वितीय शीघ्र इंजेक्शन जोखिमों का परिचय देता है। दुर्भावनापूर्ण अभिनेता तौर -तरीकों के बीच बातचीत का फायदा उठा सकते हैं, जैसे कि सौम्य पाठ के साथ छवियों में निर्देश छिपाना। इन प्रणालियों की जटिलता हमले की सतह का विस्तार करती है। मल्टीमॉडल मॉडल भी उपन्यास क्रॉस-मोडल हमलों के लिए अतिसंवेदनशील हो सकते हैं जो वर्तमान तकनीकों के साथ पता लगाने और कम करने के लिए मुश्किल हैं। मजबूत मल्टीमॉडल-विशिष्ट बचाव आगे के अनुसंधान और विकास के लिए एक महत्वपूर्ण क्षेत्र है।

### Prevention and Mitigation Strategies
### रोकथाम और शमन रणनीतियाँ

Prompt injection vulnerabilities are possible due to the nature of generative AI. Given the stochastic influence at the heart of the way models work, it is unclear if there are fool-proof methods of prevention for prompt injection. However, the following measures can mitigate the impact of prompt injections:
जनरेटिव एआई की प्रकृति के कारण शीघ्र इंजेक्शन कमजोरियां संभव हैं। मॉडल काम करने के तरीके के दिल में स्टोकेस्टिक प्रभाव को देखते हुए, यह स्पष्ट नहीं है कि क्या शीघ्र इंजेक्शन के लिए रोकथाम के मूर्खतापूर्ण तरीके हैं। हालांकि, निम्नलिखित उपाय शीघ्र इंजेक्शन के प्रभाव को कम कर सकते हैं:

#### 1. Constrain model behavior
  Provide specific instructions about the model's role, capabilities, and limitations within the system prompt. Enforce strict context adherence, limit responses to specific tasks or topics, and instruct the model to ignore attempts to modify core instructions.
#### 2. Define and validate expected output formats
  Specify clear output formats, request detailed reasoning and source citations, and use deterministic code to validate adherence to these formats.
#### 3. Implement input and output filtering
  Define sensitive categories and construct rules for identifying and handling such content. Apply semantic filters and use string-checking to scan for non-allowed content. Evaluate responses using the RAG Triad: Assess context relevance, groundedness, and question/answer relevance to identify potentially malicious outputs.
#### 4. Enforce privilege control and least privilege access
  Provide the application with its own API tokens for extensible functionality, and handle these functions in code rather than providing them to the model. Restrict the model's access privileges to the minimum necessary for its intended operations.
#### 5. Require human approval for high-risk actions
  Implement human-in-the-loop controls for privileged operations to prevent unauthorized actions.
#### 6. Segregate and identify external content
  Separate and clearly denote untrusted content to limit its influence on user prompts.
#### 7. Conduct adversarial testing and attack simulations
  Perform regular penetration testing and breach simulations, treating the model as an untrusted user to test the effectiveness of trust boundaries and access controls.
#### 1। मॉडल व्यवहार को बाधित करें
  सिस्टम प्रॉम्प्ट के भीतर मॉडल की भूमिका, क्षमताओं और सीमाओं के बारे में विशिष्ट निर्देश प्रदान करें। सख्त संदर्भ पालन को लागू करें, विशिष्ट कार्यों या विषयों के लिए प्रतिक्रियाओं को सीमित करें, और मॉडल को निर्देश देते हैं कि वे कोर निर्देशों को संशोधित करने के प्रयासों को अनदेखा करें।
#### 2। अपेक्षित आउटपुट प्रारूपों को परिभाषित करें और मान्य करें
  स्पष्ट आउटपुट प्रारूप निर्दिष्ट करें, विस्तृत तर्क और स्रोत उद्धरणों का अनुरोध करें, और इन प्रारूपों के पालन को मान्य करने के लिए नियतात्मक कोड का उपयोग करें।
#### 3। इनपुट और आउटपुट फ़िल्टरिंग को लागू करें
  संवेदनशील श्रेणियों को परिभाषित करें और ऐसी सामग्री की पहचान और संभालने के लिए नियमों का निर्माण करें। सिमेंटिक फ़िल्टर लागू करें और गैर-अनुगामी सामग्री के लिए स्कैन करने के लिए स्ट्रिंग-चेकिंग का उपयोग करें। RAG TRIAD का उपयोग करके प्रतिक्रियाओं का मूल्यांकन करें: संभावित दुर्भावनापूर्ण आउटपुट की पहचान करने के लिए संदर्भ प्रासंगिकता, जमीनीपन और प्रश्न/उत्तर प्रासंगिकता का आकलन करें।
#### 4। विशेषाधिकार नियंत्रण और कम से कम विशेषाधिकार पहुंच को लागू करें
  एक्स्टेंसिबल कार्यक्षमता के लिए अपने स्वयं के एपीआई टोकन के साथ आवेदन प्रदान करें, और मॉडल को प्रदान करने के बजाय कोड में इन कार्यों को संभालें। मॉडल के एक्सेस विशेषाधिकारों को अपने इच्छित संचालन के लिए न्यूनतम आवश्यक तक सीमित करें।
#### 5। उच्च जोखिम वाले कार्यों के लिए मानव अनुमोदन की आवश्यकता है
  अनधिकृत कार्यों को रोकने के लिए विशेषाधिकार प्राप्त संचालन के लिए मानव-इन-द-लूप नियंत्रण को लागू करें।
#### 6। बाहरी सामग्री को अलग और पहचानें
  उपयोगकर्ता संकेतों पर इसके प्रभाव को सीमित करने के लिए अलग और स्पष्ट रूप से अविश्वसनीय सामग्री को निरूपित करें।
#### 7। प्रतिकूल परीक्षण और हमला सिमुलेशन का संचालन करें
  ट्रस्ट की सीमाओं और एक्सेस कंट्रोल की प्रभावशीलता का परीक्षण करने के लिए एक अविश्वसनीय उपयोगकर्ता के रूप में मॉडल को एक अविश्वसनीय उपयोगकर्ता के रूप में मानते हुए, नियमित प्रवेश परीक्षण और उल्लंघन सिमुलेशन करें।

### Example Attack Scenarios
### उदाहरण हमले परिदृश्य

#### Scenario #1: Direct Injection
  An attacker injects a prompt into a customer support chatbot, instructing it to ignore previous guidelines, query private data stores, and send emails, leading to unauthorized access and privilege escalation.
#### Scenario #2: Indirect Injection
  A user employs an LLM to summarize a webpage containing hidden instructions that cause the LLM to insert an image linking to a URL, leading to exfiltration of the the private conversation.
#### Scenario #3: Unintentional Injection
  A company includes an instruction in a job description to identify AI-generated applications. An applicant, unaware of this instruction, uses an LLM to optimize their resume, inadvertently triggering the AI detection.
#### Scenario #4: Intentional Model Influence
  An attacker modifies a document in a repository used by a Retrieval-Augmented Generation (RAG) application. When a user's query returns the modified content, the malicious instructions alter the LLM's output, generating misleading results.
#### Scenario #5: Code Injection
  An attacker exploits a vulnerability (CVE-2024-5184) in an LLM-powered email assistant to inject malicious prompts, allowing access to sensitive information and manipulation of email content.
#### Scenario #6: Payload Splitting
  An attacker uploads a resume with split malicious prompts. When an LLM is used to evaluate the candidate, the combined prompts manipulate the model's response, resulting in a positive recommendation despite the actual resume contents.
#### Scenario #7: Multimodal Injection
  An attacker embeds a malicious prompt within an image that accompanies benign text. When a multimodal AI processes the image and text concurrently, the hidden prompt alters the model's behavior, potentially leading to unauthorized actions or disclosure of sensitive information.
#### Scenario #8: Adversarial Suffix
  An attacker appends a seemingly meaningless string of characters to a prompt, which influences the LLM's output in a malicious way, bypassing safety measures.
#### Scenario #9: Multilingual/Obfuscated Attack
  An attacker uses multiple languages or encodes malicious instructions (e.g., using Base64 or emojis) to evade filters and manipulate the LLM's behavior.
#### परिदृश्य#1: प्रत्यक्ष इंजेक्शन
  एक हमलावर एक ग्राहक सहायता चैटबॉट में एक संकेत को इंजेक्ट करता है, यह पिछले दिशानिर्देशों को अनदेखा करने, निजी डेटा स्टोरों को क्वेरी करने और ईमेल भेजने के लिए निर्देश देता है, जिससे अनधिकृत पहुंच और विशेषाधिकार वृद्धि होती है।
#### परिदृश्य#2: अप्रत्यक्ष इंजेक्शन
  एक उपयोगकर्ता छिपे हुए निर्देशों वाले एक वेबपेज को संक्षेप में प्रस्तुत करने के लिए एक एलएलएम को नियुक्त करता है, जो एलएलएम को एक यूआरएल से जोड़ने वाली छवि डालने का कारण बनता है, जिससे निजी वार्तालाप का पता चलता है।
#### परिदृश्य#3: अनजाने इंजेक्शन
  एक कंपनी में एआई-जनित अनुप्रयोगों की पहचान करने के लिए नौकरी विवरण में एक निर्देश शामिल है। एक आवेदक, इस निर्देश से अनजान, अपने फिर से शुरू करने के लिए एक एलएलएम का उपयोग करता है, अनजाने में एआई का पता लगाने को ट्रिगर करता है।
#### परिदृश्य#4: जानबूझकर मॉडल प्रभाव
  एक हमलावर एक पुनर्प्राप्ति-अनुमानित पीढ़ी (आरएजी) आवेदन द्वारा उपयोग किए जाने वाले रिपॉजिटरी में एक दस्तावेज़ को संशोधित करता है। जब उपयोगकर्ता की क्वेरी संशोधित सामग्री लौटाती है, तो दुर्भावनापूर्ण निर्देश एलएलएम के आउटपुट को बदल देते हैं, जिससे भ्रामक परिणाम उत्पन्न होते हैं।
#### परिदृश्य#5: कोड इंजेक्शन
  एक हमलावर दुर्भावनापूर्ण संकेतों को इंजेक्ट करने के लिए एक एलएलएम-संचालित ईमेल सहायक में एक भेद्यता (CVE-2024-5184) का शोषण करता है, जिससे संवेदनशील जानकारी और ईमेल सामग्री में हेरफेर करने की अनुमति मिलती है।
#### परिदृश्य#6: पेलोड विभाजन
  एक हमलावर विभाजित दुर्भावनापूर्ण संकेतों के साथ एक फिर से शुरू अपलोड करता है। जब एक एलएलएम का उपयोग उम्मीदवार का मूल्यांकन करने के लिए किया जाता है, तो संयुक्त संकेत मॉडल की प्रतिक्रिया में हेरफेर करते हैं, जिसके परिणामस्वरूप वास्तविक फिर से शुरू होने वाली सामग्री के बावजूद एक सकारात्मक सिफारिश होती है।
#### परिदृश्य#7: मल्टीमॉडल इंजेक्शन
  एक हमलावर एक छवि के भीतर एक दुर्भावनापूर्ण संकेत एम्बेड करता है जो सौम्य पाठ के साथ होता है। जब एक मल्टीमॉडल एआई छवि और पाठ को समवर्ती रूप से संसाधित करता है, तो छिपा हुआ प्रॉम्प्ट मॉडल के व्यवहार को बदल देता है, संभवतः अनधिकृत कार्यों या संवेदनशील जानकारी के प्रकटीकरण के लिए अग्रणी होता है।
#### परिदृश्य#8: प्रतिकूल प्रत्यय
  एक हमलावर एक संकेत के लिए पात्रों के एक प्रतीत होता है, जो एक दुर्भावनापूर्ण तरीके से एलएलएम के आउटपुट को प्रभावित करता है, सुरक्षा उपायों को दरकिनार करता है।
#### परिदृश्य#9: बहुभाषी/अप्रिय हमला
  एक हमलावर कई भाषाओं का उपयोग करता है या दुर्भावनापूर्ण निर्देशों (जैसे, बेस 64 या इमोजी का उपयोग करके) को फिल्टर से बाहर निकालने और एलएलएम के व्यवहार में हेरफेर करने के लिए एन्कोड करता है।

### Reference Links
### संदर्भ लिंक

1. [ChatGPT Plugin Vulnerabilities - Chat with Code](https://embracethered.com/blog/posts/2023/chatgpt-plugin-vulns-chat-with-code/) **Embrace the Red**
2. [ChatGPT Cross Plugin Request Forgery and Prompt Injection](https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./) **Embrace the Red**
3. [Not what you’ve signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection](https://arxiv.org/pdf/2302.12173.pdf) **Arxiv**
4. [Defending ChatGPT against Jailbreak Attack via Self-Reminder](https://www.researchsquare.com/article/rs-2873090/v1) **Research Square**
5. [Prompt Injection attack against LLM-integrated Applications](https://arxiv.org/abs/2306.05499) **Cornell University**
6. [Inject My PDF: Prompt Injection for your Resume](https://kai-greshake.de/posts/inject-my-pdf) **Kai Greshake**
8. [Not what you’ve signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection](https://arxiv.org/pdf/2302.12173.pdf) **Cornell University**
9. [Threat Modeling LLM Applications](https://aivillage.org/large%20language%20models/threat-modeling-llm/) **AI Village**
10. [Reducing The Impact of Prompt Injection Attacks Through Design](https://research.kudelskisecurity.com/2023/05/25/reducing-the-impact-of-prompt-injection-attacks-through-design/) **Kudelski Security**
11. [Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations (nist.gov)](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-2e2023.pdf)
12. [2407.07403 A Survey of Attacks on Large Vision-Language Models: Resources, Advances, and Future Trends (arxiv.org)](https://arxiv.org/abs/2407.07403)
13. [Exploiting Programmatic Behavior of LLMs: Dual-Use Through Standard Security Attacks](https://ieeexplore.ieee.org/document/10579515)
14. [Universal and Transferable Adversarial Attacks on Aligned Language Models (arxiv.org)](https://arxiv.org/abs/2307.15043)
15. [From ChatGPT to ThreatGPT: Impact of Generative AI in Cybersecurity and Privacy (arxiv.org)](https://arxiv.org/abs/2307.00691)
1। [CHATGPT प्लगइन कमजोरियां-कोड के साथ चैट करें] (https://embracethered.com/blog/posts/2023/chatgpt-plugin-vulns-chat-with-code/) ** लाल ** को गले लगाओ
2। [CHATGPT क्रॉस प्लगइन अनुरोध जालसाजी और शीघ्र इंजेक्शन] **
3। [वह नहीं जिसके लिए आपने साइन अप किया है: अप्रत्यक्ष शीघ्र इंजेक्शन के साथ वास्तविक दुनिया LLM- एकीकृत अनुप्रयोगों से समझौता करना] (https://arxiv.org/pdf/2302.12173.pdf) ** arxiv ** **
4। [सेल्फ-रिमाइंडर के माध्यम से जेलब्रेक अटैक के खिलाफ चैट का बचाव] (https://www.researchsquare.com/article/rs-2873090/v1) ** रिसर्च स्क्वायर **
5। [एलएलएम-एकीकृत अनुप्रयोगों के खिलाफ शीघ्र इंजेक्शन हमला] (https://arxiv.org/abs/2306.05499) ** कॉर्नेल विश्वविद्यालय **
6। [मेरे पीडीएफ को इंजेक्ट करें: अपने फिर से शुरू के लिए शीघ्र इंजेक्शन]
8। [नहीं कि आपने किस लिए साइन अप किया है: अप्रत्यक्ष शीघ्र इंजेक्शन के साथ वास्तविक दुनिया LLM- एकीकृत अनुप्रयोगों से समझौता करना] (https://arxiv.org/pdf/2302.12173.pdf) ** कॉर्नेल विश्वविद्यालय **
9। [खतरा मॉडलिंग एलएलएम एप्लिकेशन]
10। [डिजाइन के माध्यम से शीघ्र इंजेक्शन हमलों के प्रभाव को कम करना] (https://research.kudelskisecurity.com/2023/05/25/reducing-the-impact-of-mompt-trompt-tacks-through-design/ * * * *कुडेल्स्की सुरक्षा **
11।
12।
13। [एलएलएम के प्रोग्रामेटिक व्यवहार का शोषण: मानक सुरक्षा हमलों के माध्यम से दोहरे-उपयोग] (https://ieeexplore.ieee.org/document/10579515)
14। [संरेखित भाषा मॉडल (arxiv.org) पर सार्वभौमिक और हस्तांतरणीय प्रतिकूल हमले] (https://arxiv.org/abs/2307.15043)
15। [चैट से लेकर खतरे तक: साइबर सुरक्षा और गोपनीयता में जेनेरिक एआई का प्रभाव (arxiv.org)] (https://arxiv.org/abs/2307.00691)

### Related Frameworks and Taxonomies
### संबंधित फ्रेमवर्क और टैक्सोनॉमी

Refer to this section for comprehensive information, scenarios strategies relating to infrastructure deployment, applied environment controls and other best practices.
बुनियादी ढांचे की तैनाती, लागू पर्यावरण नियंत्रण और अन्य सर्वोत्तम प्रथाओं से संबंधित व्यापक जानकारी, परिदृश्यों की रणनीतियों के लिए इस खंड का संदर्भ लें।

- [AML.T0051.000 - LLM Prompt Injection: Direct](https://atlas.mitre.org/techniques/AML.T0051.000) **MITRE ATLAS**
- [AML.T0051.001 - LLM Prompt Injection: Indirect](https://atlas.mitre.org/techniques/AML.T0051.001) **MITRE ATLAS**
- [AML.T0054 - LLM Jailbreak Injection: Direct](https://atlas.mitre.org/techniques/AML.T0054) **MITRE ATLAS**

- [AML.T0051.000 - LLM प्रॉम्प्ट इंजेक्शन: डायरेक्ट] (https://atlas.mitre.org/techniques/aml.t0051.000) ** Miter Atlas **
- [AML.T0051.001 - LLM प्रॉम्प्ट इंजेक्शन: अप्रत्यक्ष] (https://atlas.mitre.org/techniques/aml.t0051.001) ** Miter Atlas **
- [AML.T0054 - LLM जेलब्रेक इंजेक्शन: डायरेक्ट] (https://atlas.mitre.org/techniques/aml.t0054)

