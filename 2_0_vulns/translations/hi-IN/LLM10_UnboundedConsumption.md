## LLM10:2025 Unbounded Consumption
## LLM10: 2025 अनबाउंडेड खपत

### Description
### विवरण

Unbounded Consumption refers to the process where a Large Language Model (LLM) generates outputs based on input queries or prompts. Inference is a critical function of LLMs, involving the application of learned patterns and knowledge to produce relevant responses or predictions.
अनबाउंडेड खपत उस प्रक्रिया को संदर्भित करती है जहां एक बड़ी भाषा मॉडल (एलएलएम) इनपुट क्वेरी या प्रॉम्प्ट के आधार पर आउटपुट उत्पन्न करता है। प्रासंगिक प्रतिक्रियाओं या भविष्यवाणियों का उत्पादन करने के लिए सीखे गए पैटर्न और ज्ञान के अनुप्रयोग को शामिल करते हुए, एलएलएम का एक महत्वपूर्ण कार्य है।

Attacks designed to disrupt service, deplete the target's financial resources, or even steal intellectual property by cloning a model’s behavior all depend on a common class of security vulnerability in order to succeed. Unbounded Consumption occurs when a Large Language Model (LLM) application allows users to conduct excessive and uncontrolled inferences, leading to risks such as denial of service (DoS), economic losses, model theft, and service degradation. The high computational demands of LLMs, especially in cloud environments, make them vulnerable to resource exploitation and unauthorized usage.
सेवा को बाधित करने के लिए डिज़ाइन किए गए हमले, लक्ष्य के वित्तीय संसाधनों को समाप्त कर दें, या यहां तक ​​कि एक मॉडल के व्यवहार को क्लोन करके बौद्धिक संपदा चोरी करें, सभी सफल होने के लिए सुरक्षा भेद्यता के एक सामान्य वर्ग पर निर्भर करते हैं। अनबाउंड खपत तब होती है जब एक बड़ी भाषा मॉडल (एलएलएम) एप्लिकेशन उपयोगकर्ताओं को अत्यधिक और अनियंत्रित निष्कर्षों का संचालन करने की अनुमति देता है, जिससे सेवा से इनकार (डीओएस), आर्थिक नुकसान, मॉडल चोरी और सेवा गिरावट जैसे जोखिम होते हैं। एलएलएम की उच्च कम्प्यूटेशनल मांगें, विशेष रूप से क्लाउड वातावरण में, उन्हें संसाधन शोषण और अनधिकृत उपयोग के लिए असुरक्षित बनाती हैं।

### Common Examples of Vulnerability
### भेद्यता के सामान्य उदाहरण

#### 1. Variable-Length Input Flood
  Attackers can overload the LLM with numerous inputs of varying lengths, exploiting processing inefficiencies. This can deplete resources and potentially render the system unresponsive, significantly impacting service availability.
#### 2. Denial of Wallet (DoW)
  By initiating a high volume of operations, attackers exploit the cost-per-use model of cloud-based AI services, leading to unsustainable financial burdens on the provider and risking financial ruin.
#### 3. Continuous Input Overflow
  Continuously sending inputs that exceed the LLM's context window can lead to excessive computational resource use, resulting in service degradation and operational disruptions.
#### 4. Resource-Intensive Queries
  Submitting unusually demanding queries involving complex sequences or intricate language patterns can drain system resources, leading to prolonged processing times and potential system failures.
#### 5. Model Extraction via API
  Attackers may query the model API using carefully crafted inputs and prompt injection techniques to collect sufficient outputs to replicate a partial model or create a shadow model. This not only poses risks of intellectual property theft but also undermines the integrity of the original model.
#### 6. Functional Model Replication
  Using the target model to generate synthetic training data can allow attackers to fine-tune another foundational model, creating a functional equivalent. This circumvents traditional query-based extraction methods, posing significant risks to proprietary models and technologies.
#### 7. Side-Channel Attacks
  Malicious attackers may exploit input filtering techniques of the LLM to execute side-channel attacks, harvesting model weights and architectural information. This could compromise the model's security and lead to further exploitation.
#### 1। चर-लंबाई इनपुट बाढ़
  हमलावर अलग -अलग लंबाई के कई इनपुट के साथ एलएलएम को ओवरलोड कर सकते हैं, प्रसंस्करण अक्षमताओं का शोषण कर सकते हैं। यह संसाधनों को कम कर सकता है और संभावित रूप से सिस्टम को अनुत्तरदायी, सेवा उपलब्धता को प्रभावित करने के लिए संभावित रूप से प्रस्तुत कर सकता है।
#### 2। वॉलेट (डॉव) से इनकार
  संचालन की एक उच्च मात्रा शुरू करके, हमलावर क्लाउड-आधारित एआई सेवाओं की लागत-प्रति-उपयोग मॉडल का फायदा उठाते हैं, जिससे प्रदाता पर अस्थिर वित्तीय बोझ और वित्तीय बर्बादी को जोखिम में डाल दिया जाता है।
#### 3। निरंतर इनपुट ओवरफ्लो
  एलएलएम के संदर्भ विंडो से अधिक होने वाले इनपुट को लगातार भेजने से अत्यधिक कम्प्यूटेशनल संसाधन उपयोग हो सकता है, जिसके परिणामस्वरूप सेवा में गिरावट और परिचालन व्यवधान हो सकते हैं।
#### 4। संसाधन-गहन प्रश्न
  जटिल अनुक्रमों या जटिल भाषा पैटर्न से जुड़े असामान्य रूप से मांग वाले प्रश्नों को प्रस्तुत करना सिस्टम संसाधनों को सूखा सकता है, जिससे लंबे समय तक प्रसंस्करण समय और संभावित प्रणाली विफलताएं हो सकती हैं।
#### 5। एपीआई के माध्यम से मॉडल निष्कर्षण
  हमलावर एक आंशिक मॉडल को दोहराने या एक छाया मॉडल बनाने के लिए पर्याप्त आउटपुट एकत्र करने के लिए सावधानीपूर्वक तैयार किए गए इनपुट और शीघ्र इंजेक्शन तकनीकों का उपयोग करके मॉडल एपीआई को क्वेरी कर सकते हैं। यह न केवल बौद्धिक संपदा चोरी के जोखिम पैदा करता है, बल्कि मूल मॉडल की अखंडता को भी कम करता है।
#### 6। कार्यात्मक मॉडल प्रतिकृति
  सिंथेटिक प्रशिक्षण डेटा उत्पन्न करने के लिए लक्ष्य मॉडल का उपयोग करना हमलावरों को एक अन्य मूलभूत मॉडल को ठीक करने की अनुमति दे सकता है, जिससे एक कार्यात्मक समकक्ष बन सकता है। यह पारंपरिक क्वेरी-आधारित निष्कर्षण विधियों को बढ़ाता है, जो मालिकाना मॉडल और प्रौद्योगिकियों के लिए महत्वपूर्ण जोखिम प्रस्तुत करता है।
#### 7। साइड-चैनल हमले
  दुर्भावनापूर्ण हमलावर साइड-चैनल हमलों को निष्पादित करने, मॉडल वेट और वास्तुशिल्प जानकारी की कटाई के लिए एलएलएम के इनपुट फ़िल्टरिंग तकनीकों का शोषण कर सकते हैं। यह मॉडल की सुरक्षा से समझौता कर सकता है और आगे के शोषण का कारण बन सकता है।

### Prevention and Mitigation Strategies
### रोकथाम और शमन रणनीतियाँ

#### 1. Input Validation
  Implement strict input validation to ensure that inputs do not exceed reasonable size limits.
#### 2. Limit Exposure of Logits and Logprobs
  Restrict or obfuscate the exposure of `logit_bias` and `logprobs` in API responses. Provide only the necessary information without revealing detailed probabilities.
#### 3. Rate Limiting
  Apply rate limiting and user quotas to restrict the number of requests a single source entity can make in a given time period.
#### 4. Resource Allocation Management
  Monitor and manage resource allocation dynamically to prevent any single user or request from consuming excessive resources.
#### 5. Timeouts and Throttling
  Set timeouts and throttle processing for resource-intensive operations to prevent prolonged resource consumption.
#### 6.Sandbox Techniques
  Restrict the LLM's access to network resources, internal services, and APIs.
  - This is particularly significant for all common scenarios as it encompasses insider risks and threats. Furthermore, it governs the extent of access the LLM application has to data and resources, thereby serving as a crucial control mechanism to mitigate or prevent side-channel attacks.
#### 7. Comprehensive Logging, Monitoring and Anomaly Detection
  Continuously monitor resource usage and implement logging to detect and respond to unusual patterns of resource consumption.
#### 8. Watermarking
  Implement watermarking frameworks to embed and detect unauthorized use of LLM outputs.
#### 9. Graceful Degradation
  Design the system to degrade gracefully under heavy load, maintaining partial functionality rather than complete failure.
#### 10. Limit Queued Actions and Scale Robustly
  Implement restrictions on the number of queued actions and total actions, while incorporating dynamic scaling and load balancing to handle varying demands and ensure consistent system performance.
#### 11. Adversarial Robustness Training
  Train models to detect and mitigate adversarial queries and extraction attempts.
#### 12. Glitch Token Filtering
  Build lists of known glitch tokens and scan output before adding it to the model’s context window.
#### 13. Access Controls
  Implement strong access controls, including role-based access control (RBAC) and the principle of least privilege, to limit unauthorized access to LLM model repositories and training environments.
#### 14. Centralized ML Model Inventory
  Use a centralized ML model inventory or registry for models used in production, ensuring proper governance and access control.
#### 15. Automated MLOps Deployment
  Implement automated MLOps deployment with governance, tracking, and approval workflows to tighten access and deployment controls within the infrastructure.
#### 1। इनपुट सत्यापन
  यह सुनिश्चित करने के लिए सख्त इनपुट सत्यापन को लागू करें कि इनपुट उचित आकार की सीमा से अधिक न हों।
#### 2। लॉग्स और लॉगप्रोब के एक्सपोज़र को सीमित करें
  API प्रतिक्रियाओं में `logit_bias` और` logprobs` के जोखिम को प्रतिबंधित या ऑब्जेक्ट करें। विस्तृत संभावनाओं का खुलासा किए बिना केवल आवश्यक जानकारी प्रदान करें।
#### 3। दर सीमित
  किसी एकल स्रोत इकाई के अनुरोधों की संख्या को प्रतिबंधित करने के लिए दर सीमित और उपयोगकर्ता कोटा को लागू करें एक निश्चित समय अवधि में कर सकते हैं।
#### 4। संसाधन आवंटन प्रबंधन
  किसी एकल उपयोगकर्ता को रोकने के लिए या अत्यधिक संसाधनों का सेवन करने से अनुरोध करने के लिए गतिशील रूप से संसाधन आवंटन की निगरानी और प्रबंधन करें।
#### 5। टाइमआउट और थ्रॉटलिंग
  लंबे समय तक संसाधन की खपत को रोकने के लिए संसाधन-गहन संचालन के लिए टाइमआउट और थ्रॉटल प्रोसेसिंग सेट करें।
#### 6.sandbox तकनीक
  नेटवर्क संसाधनों, आंतरिक सेवाओं और एपीआई तक एलएलएम की पहुंच को प्रतिबंधित करें।
  - यह सभी सामान्य परिदृश्यों के लिए विशेष रूप से महत्वपूर्ण है क्योंकि यह इनसाइडर जोखिमों और खतरों को शामिल करता है। इसके अलावा, यह एलएलएम एप्लिकेशन को डेटा और संसाधनों के लिए पहुंच की सीमा को नियंत्रित करता है, जिससे साइड-चैनल हमलों को कम करने या रोकने के लिए एक महत्वपूर्ण नियंत्रण तंत्र के रूप में काम होता है।
#### 7। व्यापक लॉगिंग, निगरानी और विसंगति का पता लगाना
  संसाधन के उपयोग की लगातार निगरानी करें और संसाधन की खपत के असामान्य पैटर्न का पता लगाने और प्रतिक्रिया देने के लिए लॉगिंग को लागू करें।
#### 8। वॉटरमार्किंग
  एलएलएम आउटपुट के अनधिकृत उपयोग को एम्बेड करने और पता लगाने के लिए वॉटरमार्किंग फ्रेमवर्क को लागू करें।
#### 9। ग्रेसफुल डिग्रेडेशन
  पूरी तरह से विफलता के बजाय आंशिक कार्यक्षमता बनाए रखने के लिए, भारी भार के तहत सुशोभित रूप से नीचा दिखाने के लिए सिस्टम को डिजाइन करें।
#### 10। कतारबद्ध कार्यों को सीमित करें और मजबूत रूप से स्केल करें
  डायनामिक स्केलिंग और लोड बैलेंसिंग को शामिल करते हुए, अलग -अलग मांगों को संभालने और सुसंगत सिस्टम प्रदर्शन सुनिश्चित करने के लिए लोड बैलेंस को शामिल करते हुए, कतारबद्ध कार्यों और कुल कार्यों की संख्या पर प्रतिबंध लागू करें।
#### 11। प्रतिकूल मजबूती प्रशिक्षण
  प्रतिकूल प्रश्नों और निष्कर्षण प्रयासों का पता लगाने और कम करने के लिए ट्रेन मॉडल।
#### 12। ग्लिच टोकन फ़िल्टरिंग
  मॉडल के संदर्भ विंडो में जोड़ने से पहले ज्ञात गड़बड़ टोकन और स्कैन आउटपुट की सूची बनाएं।
#### 13। एक्सेस कंट्रोल
  एलएलएम मॉडल रिपॉजिटरी और प्रशिक्षण वातावरण तक अनधिकृत पहुंच को सीमित करने के लिए भूमिका-आधारित एक्सेस कंट्रोल (आरबीएसी) और कम से कम विशेषाधिकार के सिद्धांत सहित मजबूत पहुंच नियंत्रणों को लागू करें।
#### 14। केंद्रीकृत एमएल मॉडल इन्वेंटरी
  उत्पादन में उपयोग किए जाने वाले मॉडल के लिए एक केंद्रीकृत एमएल मॉडल इन्वेंटरी या रजिस्ट्री का उपयोग करें, उचित शासन और पहुंच नियंत्रण सुनिश्चित करें।
#### 15। स्वचालित MLOPS तैनाती
  बुनियादी ढांचे के भीतर पहुंच और तैनाती नियंत्रणों को कसने के लिए शासन, ट्रैकिंग और अनुमोदन वर्कफ़्लो के साथ स्वचालित MLOPS तैनाती को लागू करें।

### Example Attack Scenarios
### उदाहरण हमले परिदृश्य

#### Scenario #1: Uncontrolled Input Size
  An attacker submits an unusually large input to an LLM application that processes text data, resulting in excessive memory usage and CPU load, potentially crashing the system or significantly slowing down the service.
#### Scenario #2: Repeated Requests
  An attacker transmits a high volume of requests to the LLM API, causing excessive consumption of computational resources and making the service unavailable to legitimate users.
#### Scenario #3: Resource-Intensive Queries
  An attacker crafts specific inputs designed to trigger the LLM's most computationally expensive processes, leading to prolonged CPU usage and potential system failure.
#### Scenario #4: Denial of Wallet (DoW)
  An attacker generates excessive operations to exploit the pay-per-use model of cloud-based AI services, causing unsustainable costs for the service provider.
#### Scenario #5: Functional Model Replication
  An attacker uses the LLM's API to generate synthetic training data and fine-tunes another model, creating a functional equivalent and bypassing traditional model extraction limitations.
#### Scenario #6: Bypassing System Input Filtering
  A malicious attacker bypasses input filtering techniques and preambles of the LLM to perform a side-channel attack and retrieve model information to a remote controlled resource under their control.
#### परिदृश्य#1: अनियंत्रित इनपुट आकार
  एक हमलावर एक एलएलएम एप्लिकेशन के लिए एक असामान्य रूप से बड़ा इनपुट प्रस्तुत करता है जो पाठ डेटा को संसाधित करता है, जिसके परिणामस्वरूप अत्यधिक मेमोरी उपयोग और सीपीयू लोड होता है, संभवतः सिस्टम को दुर्घटनाग्रस्त हो जाता है या सेवा को काफी धीमा कर देता है।
#### परिदृश्य#2: बार -बार अनुरोध
  एक हमलावर एलएलएम एपीआई के लिए अनुरोधों की एक उच्च मात्रा प्रसारित करता है, जिससे कम्प्यूटेशनल संसाधनों की अत्यधिक खपत होती है और सेवा को वैध उपयोगकर्ताओं के लिए अनुपलब्ध बना दिया जाता है।
#### परिदृश्य#3: संसाधन-गहन प्रश्न
  एक हमलावर शिल्प विशिष्ट इनपुट्स को एलएलएम की सबसे कम्प्यूटेशनल रूप से महंगी प्रक्रियाओं को ट्रिगर करने के लिए डिज़ाइन किया गया है, जिससे लंबे समय तक सीपीयू उपयोग और संभावित प्रणाली की विफलता होती है।
#### परिदृश्य#4: वॉलेट का इनकार (डॉव)
  एक हमलावर क्लाउड-आधारित एआई सेवाओं के पे-प्रति-उपयोग मॉडल का फायदा उठाने के लिए अत्यधिक संचालन उत्पन्न करता है, जिससे सेवा प्रदाता के लिए अस्थिर लागत होती है।
#### परिदृश्य#5: कार्यात्मक मॉडल प्रतिकृति
  एक हमलावर सिंथेटिक प्रशिक्षण डेटा उत्पन्न करने के लिए एलएलएम के एपीआई का उपयोग करता है और एक और मॉडल को ठीक करने के लिए, एक कार्यात्मक समकक्ष और पारंपरिक मॉडल निष्कर्षण सीमाओं को दरकिनार करता है।
#### परिदृश्य#6: सिस्टम इनपुट फ़िल्टरिंग को बायपास करना
  एक दुर्भावनापूर्ण हमलावर इनपुट फ़िल्टरिंग तकनीकों और एलएलएम के प्रस्ताव को साइड-चैनल हमला करने और उनके नियंत्रण के तहत एक रिमोट नियंत्रित संसाधन के लिए मॉडल की जानकारी प्राप्त करने के लिए एलएलएम के प्रस्ताव को बायपास करता है।

### Reference Links
### संदर्भ लिंक

1. [Proof Pudding (CVE-2019-20634)](https://avidml.org/database/avid-2023-v009/) **AVID** (`moohax` & `monoxgas`)
2. [arXiv:2403.06634 Stealing Part of a Production Language Model](https://arxiv.org/abs/2403.06634) **arXiv**
3. [Runaway LLaMA | How Meta's LLaMA NLP model leaked](https://www.deeplearning.ai/the-batch/how-metas-llama-nlp-model-leaked/): **Deep Learning Blog**
4. [You wouldn't download an AI, Extracting AI models from mobile apps](https://altayakkus.substack.com/p/you-wouldnt-download-an-ai): **Substack blog**
5. [A Comprehensive Defense Framework Against Model Extraction Attacks](https://ieeexplore.ieee.org/document/10080996): **IEEE**
6. [Alpaca: A Strong, Replicable Instruction-Following Model](https://crfm.stanford.edu/2023/03/13/alpaca.html): **Stanford Center on Research for Foundation Models (CRFM)**
7. [How Watermarking Can Help Mitigate The Potential Risks Of LLMs?](https://www.kdnuggets.com/2023/03/watermarking-help-mitigate-potential-risks-llms.html): **KD Nuggets**
8. [Securing AI Model Weights Preventing Theft and Misuse of Frontier Models](https://www.rand.org/content/dam/rand/pubs/research_reports/RRA2800/RRA2849-1/RAND_RRA2849-1.pdf)
9. [Sponge Examples: Energy-Latency Attacks on Neural Networks: Arxiv White Paper](https://arxiv.org/abs/2006.03463) **arXiv**
10. [Sourcegraph Security Incident on API Limits Manipulation and DoS Attack](https://about.sourcegraph.com/blog/security-update-august-2023) **Sourcegraph**
1। [प्रूफ पुडिंग (CVE-2019-20634)]
2।
3। [रनवे लामा | कैसे मेटा का लामा एनएलपी मॉडल लीक हो गया] (https://www.deeplearning.ai/the-batch/how-metas-llama-nlp-model-leaked/): ** डीप लर्निंग ब्लॉग **
4। [आप एक एआई डाउनलोड नहीं करेंगे, मोबाइल ऐप्स से एआई मॉडल निकालते हुए] (https://altayakkus.substack.com/p/you-wouldnt-download-an-ai): ** Substack Blog **
5। [मॉडल निष्कर्षण हमलों के खिलाफ एक व्यापक रक्षा ढांचा] (https://ieeexplore.ieee.org/document/10080996): ** ieee **
6।
। *
8। [एआई मॉडल वेट को सुरक्षित करना चोरी और फ्रंटियर मॉडल के दुरुपयोग को रोकना] (https://www.rand.org/content/dam/rand/pubs/research_reports/rra2800/rra2849-1/rand_rra2849-1.pdf)
9। [स्पंज उदाहरण: तंत्रिका नेटवर्क पर ऊर्जा-लेटेंसी हमले: arxiv श्वेत पत्र] (https://arxiv.org/abs/2006.03463) ** arxiv **
10। [सोर्सग्राफ सुरक्षा की घटना एपीआई पर हेरफेर और डॉस अटैक] (https://about.sourcegraph.com/blog/security-pdate-august-2023) ** SourceGraph ** **

### Related Frameworks and Taxonomies
### संबंधित फ्रेमवर्क और टैक्सोनॉमी

Refer to this section for comprehensive information, scenarios strategies relating to infrastructure deployment, applied environment controls and other best practices.
बुनियादी ढांचे की तैनाती, लागू पर्यावरण नियंत्रण और अन्य सर्वोत्तम प्रथाओं से संबंधित व्यापक जानकारी, परिदृश्य रणनीतियों के लिए इस खंड का संदर्भ लें।

- [MITRE CWE-400: Uncontrolled Resource Consumption](https://cwe.mitre.org/data/definitions/400.html) **MITRE Common Weakness Enumeration**
- [AML.TA0000 ML Model Access: Mitre ATLAS](https://atlas.mitre.org/tactics/AML.TA0000) & [AML.T0024 Exfiltration via ML Inference API](https://atlas.mitre.org/techniques/AML.T0024) **MITRE ATLAS**
- [AML.T0029 - Denial of ML Service](https://atlas.mitre.org/techniques/AML.T0029) **MITRE ATLAS**
- [AML.T0034 - Cost Harvesting](https://atlas.mitre.org/techniques/AML.T0034) **MITRE ATLAS**
- [AML.T0025 - Exfiltration via Cyber Means](https://atlas.mitre.org/techniques/AML.T0025) **MITRE ATLAS**
- [OWASP Machine Learning Security Top Ten - ML05:2023 Model Theft](https://owasp.org/www-project-machine-learning-security-top-10/docs/ML05_2023-Model_Theft.html) **OWASP ML Top 10**
- [API4:2023 - Unrestricted Resource Consumption](https://owasp.org/API-Security/editions/2023/en/0xa4-unrestricted-resource-consumption/) **OWASP Web Application Top 10**
- [OWASP Resource Management](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/) **OWASP Secure Coding Practices**
- [Miter CWE-400: अनियंत्रित संसाधन खपत] (https://cwe.mitre.org/data/definitions/400.html)
- [AML.TA0000 ML मॉडल एक्सेस: Miter Atlas] (https://atlas.mitre.org/tactics/aml.ta0000) & [AML.T0024 exfiltration Ml Inference Api के माध्यम से /techniques/aml.t0024) ** मेटर एटलस **
- [AML.T0029 - ML सेवा से इनकार]
- [AML.T0034 - लागत कटाई]
- [AML.T0025 - साइबर मीन्स के माध्यम से एक्सफिल्ट्रेशन] (https://atlas.mitre.org/techniques/aml.t0025) ** Miter Atlas **
-[OWASP मशीन लर्निंग सिक्योरिटी टॉप टेन-ML05: 2023 मॉडल चोरी] (https://owasp.org/www-project-machine-learning-security-top-10/docs/ml05_2023-model_theft.html) सर्वोत्तम 10**
-[API4: 2023-अप्रतिबंधित संसाधन खपत] (https://owasp.org/api-security/editions/2023/en/0xa4-overstricted-resource-conument/) ** OWASP वेब एप्लिकेशन शीर्ष 10 **
-[OWASP संसाधन प्रबंधन] (https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/) ** OWASP सुरक्षित कोडिंग प्रथाओं **

