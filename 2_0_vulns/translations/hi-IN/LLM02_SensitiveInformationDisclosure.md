## LLM02:2025 Sensitive Information Disclosure
## LLM02: 2025 संवेदनशील सूचना प्रकटीकरण

### Description
### विवरण

Sensitive information can affect both the LLM and its application context. This includes personal identifiable information (PII), financial details, health records, confidential business data, security credentials, and legal documents. Proprietary models may also have unique training methods and source code considered sensitive, especially in closed or foundation models.
संवेदनशील जानकारी एलएलएम और इसके आवेदन के संदर्भ को प्रभावित कर सकती है। इसमें व्यक्तिगत पहचान योग्य जानकारी (PII), वित्तीय विवरण, स्वास्थ्य रिकॉर्ड, गोपनीय व्यवसाय डेटा, सुरक्षा क्रेडेंशियल्स और कानूनी दस्तावेज शामिल हैं। मालिकाना मॉडल में अद्वितीय प्रशिक्षण विधियाँ और स्रोत कोड भी संवेदनशील माना जा सकता है, विशेष रूप से बंद या नींव मॉडल में।

LLMs, especially when embedded in applications, risk exposing sensitive data, proprietary algorithms, or confidential details through their output. This can result in unauthorized data access, privacy violations, and intellectual property breaches. Consumers should be aware of how to interact safely with LLMs. They need to understand the risks of unintentionally providing sensitive data, which may later be disclosed in the model's output.
एलएलएम, विशेष रूप से जब अनुप्रयोगों में एम्बेडेड, संवेदनशील डेटा, मालिकाना एल्गोरिदम, या उनके आउटपुट के माध्यम से गोपनीय विवरण को उजागर करने का जोखिम होता है। इसके परिणामस्वरूप अनधिकृत डेटा एक्सेस, गोपनीयता उल्लंघन और बौद्धिक संपदा उल्लंघनों का परिणाम हो सकता है। उपभोक्ताओं को पता होना चाहिए कि एलएलएम के साथ सुरक्षित रूप से कैसे बातचीत करें। उन्हें अनजाने में संवेदनशील डेटा प्रदान करने के जोखिमों को समझने की आवश्यकता है, जिसे बाद में मॉडल के आउटपुट में खुलासा किया जा सकता है।

To reduce this risk, LLM applications should perform adequate data sanitization to prevent user data from entering the training model. Application owners should also provide clear Terms of Use policies, allowing users to opt out of having their data included in the training model. Adding restrictions within the system prompt about data types that the LLM should return can provide mitigation against sensitive information disclosure. However, such restrictions may not always be honored and could be bypassed via prompt injection or other methods.
इस जोखिम को कम करने के लिए, एलएलएम एप्लिकेशन को उपयोगकर्ता डेटा को प्रशिक्षण मॉडल में प्रवेश करने से रोकने के लिए पर्याप्त डेटा सैनिटाइजेशन करना चाहिए। एप्लिकेशन मालिकों को उपयोग नीतियों की स्पष्ट शर्तें भी प्रदान करनी चाहिए, जिससे उपयोगकर्ताओं को प्रशिक्षण मॉडल में शामिल अपने डेटा को शामिल करने की अनुमति मिलती है। सिस्टम के भीतर प्रतिबंधों को जोड़ना डेटा प्रकारों के बारे में संकेत देता है कि एलएलएम को वापस करना चाहिए संवेदनशील जानकारी प्रकटीकरण के खिलाफ शमन प्रदान कर सकता है। हालांकि, इस तरह के प्रतिबंधों को हमेशा सम्मानित नहीं किया जा सकता है और उन्हें शीघ्र इंजेक्शन या अन्य तरीकों के माध्यम से बायपास किया जा सकता है।

### Common Examples of Vulnerability
### भेद्यता के सामान्य उदाहरण

#### 1. PII Leakage
  Personal identifiable information (PII) may be disclosed during interactions with the LLM.
#### 2. Proprietary Algorithm Exposure
  Poorly configured model outputs can reveal proprietary algorithms or data. Revealing training data can expose models to inversion attacks, where attackers extract sensitive information or reconstruct inputs. For instance, as demonstrated in the 'Proof Pudding' attack (CVE-2019-20634), disclosed training data facilitated model extraction and inversion, allowing attackers to circumvent security controls in machine learning algorithms and bypass email filters.
#### 3. Sensitive Business Data Disclosure
  Generated responses might inadvertently include confidential business information.
#### 1। PII रिसाव
  व्यक्तिगत पहचान योग्य जानकारी (PII) का खुलासा LLM के साथ बातचीत के दौरान किया जा सकता है।
#### 2। मालिकाना एल्गोरिथ्म एक्सपोज़र
  खराब कॉन्फ़िगर किए गए मॉडल आउटपुट मालिकाना एल्गोरिदम या डेटा को प्रकट कर सकते हैं। प्रशिक्षण डेटा का खुलासा मॉडल को उलटा हमलों के लिए उजागर कर सकता है, जहां हमलावर संवेदनशील जानकारी निकालते हैं या इनपुट का पुनर्निर्माण करते हैं। उदाहरण के लिए, जैसा कि 'प्रूफ पुडिंग' अटैक (CVE-2019-20634) में प्रदर्शित किया गया है, प्रशिक्षण डेटा ने मॉडल निष्कर्षण और उलटा सुविधा प्रदान की, जिससे हमलावर मशीन लर्निंग एल्गोरिदम और ईमेल फिल्टर को बायपास करने में हमलावरों को सुरक्षा नियंत्रणों को दरकिनार कर सकते हैं।
#### 3। संवेदनशील व्यापार डेटा प्रकटीकरण
  उत्पन्न प्रतिक्रियाओं में अनजाने में गोपनीय व्यावसायिक जानकारी शामिल हो सकती है।

### Prevention and Mitigation Strategies
### रोकथाम और शमन रणनीतियाँ

#### Sanitization:
#### Sanitization:

#### 1. Integrate Data Sanitization Techniques
  Implement data sanitization to prevent user data from entering the training model. This includes scrubbing or masking sensitive content before it is used in training.
#### 2. Robust Input Validation
  Apply strict input validation methods to detect and filter out potentially harmful or sensitive data inputs, ensuring they do not compromise the model.
#### 1। डेटा सैनिटाइजेशन तकनीकों को एकीकृत करें
  प्रशिक्षण मॉडल में प्रवेश करने से उपयोगकर्ता डेटा को रोकने के लिए डेटा सैनिटाइजेशन को लागू करें। इसमें प्रशिक्षण में उपयोग किए जाने से पहले संवेदनशील सामग्री को स्क्रबिंग या मास्क करना शामिल है।
#### 2। मजबूत इनपुट सत्यापन
  संभावित रूप से हानिकारक या संवेदनशील डेटा इनपुट का पता लगाने और फ़िल्टर करने के लिए सख्त इनपुट सत्यापन विधियाँ लागू करें, यह सुनिश्चित करें कि वे मॉडल से समझौता नहीं करते हैं।

#### Access Controls:
#### एक्सेस कंट्रोल:

#### 1. Enforce Strict Access Controls
  Limit access to sensitive data based on the principle of least privilege. Only grant access to data that is necessary for the specific user or process.
#### 2. Restrict Data Sources
  Limit model access to external data sources, and ensure runtime data orchestration is securely managed to avoid unintended data leakage.
#### 1। सख्त पहुंच नियंत्रण लागू करें
  कम से कम विशेषाधिकार के सिद्धांत के आधार पर संवेदनशील डेटा तक पहुंच को सीमित करें। केवल डेटा तक पहुंच प्रदान करें जो विशिष्ट उपयोगकर्ता या प्रक्रिया के लिए आवश्यक है।
#### 2। डेटा स्रोतों को प्रतिबंधित करें
  बाहरी डेटा स्रोतों तक मॉडल की पहुंच को सीमित करें, और सुनिश्चित करें कि रनटाइम डेटा ऑर्केस्ट्रेशन को अनपेक्षित डेटा रिसाव से बचने के लिए सुरक्षित रूप से प्रबंधित किया जाता है।

#### Federated Learning and Privacy Techniques:
#### फेडरेटेड लर्निंग और गोपनीयता तकनीक:

#### 1. Utilize Federated Learning
  Train models using decentralized data stored across multiple servers or devices. This approach minimizes the need for centralized data collection and reduces exposure risks.
#### 2. Incorporate Differential Privacy
  Apply techniques that add noise to the data or outputs, making it difficult for attackers to reverse-engineer individual data points.
#### 1। फेडरेटेड लर्निंग का उपयोग करें
  कई सर्वरों या उपकरणों में संग्रहीत विकेंद्रीकृत डेटा का उपयोग करके ट्रेन मॉडल। यह दृष्टिकोण केंद्रीकृत डेटा संग्रह की आवश्यकता को कम करता है और एक्सपोज़र जोखिमों को कम करता है।
#### 2। अंतर गोपनीयता शामिल करें
  ऐसी तकनीकों को लागू करें जो डेटा या आउटपुट में शोर जोड़ते हैं, जिससे हमलावरों के लिए व्यक्तिगत डेटा बिंदुओं को उल्टा करना मुश्किल हो जाता है।

#### User Education and Transparency:
#### उपयोगकर्ता शिक्षा और पारदर्शिता:

#### 1. Educate Users on Safe LLM Usage
  Provide guidance on avoiding the input of sensitive information. Offer training on best practices for interacting with LLMs securely.
#### 2. Ensure Transparency in Data Usage
  Maintain clear policies about data retention, usage, and deletion. Allow users to opt out of having their data included in training processes.
#### 1। सुरक्षित एलएलएम उपयोग पर उपयोगकर्ताओं को शिक्षित करें
  संवेदनशील जानकारी के इनपुट से बचने पर मार्गदर्शन प्रदान करें। सुरक्षित रूप से एलएलएम के साथ बातचीत करने के लिए सर्वोत्तम प्रथाओं पर प्रशिक्षण की पेशकश करें।
#### 2। डेटा उपयोग में पारदर्शिता सुनिश्चित करें
  डेटा प्रतिधारण, उपयोग और विलोपन के बारे में स्पष्ट नीतियां बनाए रखें। उपयोगकर्ताओं को प्रशिक्षण प्रक्रियाओं में शामिल अपने डेटा को चुनने की अनुमति दें।

#### Secure System Configuration:
#### सुरक्षित सिस्टम कॉन्फ़िगरेशन:

#### 1. Conceal System Preamble
  Limit the ability for users to override or access the system's initial settings, reducing the risk of exposure to internal configurations.
#### 2. Reference Security Misconfiguration Best Practices
  Follow guidelines like "OWASP API8:2023 Security Misconfiguration" to prevent leaking sensitive information through error messages or configuration details.
  (Ref. link:[OWASP API8:2023 Security Misconfiguration](https://owasp.org/API-Security/editions/2023/en/0xa8-security-misconfiguration/))
#### 1। कंसीलर सिस्टम प्राइमबल
  आंतरिक कॉन्फ़िगरेशन के संपर्क के जोखिम को कम करते हुए, सिस्टम की प्रारंभिक सेटिंग्स को ओवरराइड करने या एक्सेस करने की क्षमता को सीमित करें।
#### 2। संदर्भ सुरक्षा मिसकॉन्फ़िगरेशन सर्वोत्तम प्रथाओं
  त्रुटि संदेशों या कॉन्फ़िगरेशन विवरण के माध्यम से संवेदनशील जानकारी लीक करने से रोकने के लिए "OWASP API8: 2023 सुरक्षा मिसकॉनफिगरेशन" जैसे दिशानिर्देशों का पालन करें।
  (Ref।

#### Advanced Techniques:
#### उन्नत तकनीक:

#### 1. Homomorphic Encryption
  Use homomorphic encryption to enable secure data analysis and privacy-preserving machine learning. This ensures data remains confidential while being processed by the model.
#### 2. Tokenization and Redaction
  Implement tokenization to preprocess and sanitize sensitive information. Techniques like pattern matching can detect and redact confidential content before processing.
#### 1। होमोमोर्फिक एन्क्रिप्शन
  सुरक्षित डेटा विश्लेषण और गोपनीयता-संरक्षण मशीन सीखने को सक्षम करने के लिए होमोमोर्फिक एन्क्रिप्शन का उपयोग करें। यह सुनिश्चित करता है कि मॉडल द्वारा संसाधित किए जाने के दौरान डेटा गोपनीय रहता है।
#### 2। टोकन और पुनर्वितरण
  प्रीप्रोसेस के लिए टोकनकरण को लागू करें और संवेदनशील जानकारी को साफ करें। पैटर्न मिलान जैसी तकनीक प्रसंस्करण से पहले गोपनीय सामग्री का पता लगा सकती है और फिर से बना सकती है।

### Example Attack Scenarios
### उदाहरण हमले परिदृश्य

#### Scenario #1: Unintentional Data Exposure
  A user receives a response containing another user's personal data due to inadequate data sanitization.
#### Scenario #2: Targeted Prompt Injection
  An attacker bypasses input filters to extract sensitive information.
#### Scenario #3: Data Leak via Training Data
  Negligent data inclusion in training leads to sensitive information disclosure.
#### परिदृश्य#1: अनजाने में डेटा एक्सपोज़र
  एक उपयोगकर्ता अपर्याप्त डेटा सैनिटाइजेशन के कारण किसी अन्य उपयोगकर्ता के व्यक्तिगत डेटा से युक्त प्रतिक्रिया प्राप्त करता है।
#### परिदृश्य#2: लक्षित शीघ्र इंजेक्शन
  एक हमलावर संवेदनशील जानकारी निकालने के लिए इनपुट फिल्टर को बायपास करता है।
#### परिदृश्य#3: प्रशिक्षण डेटा के माध्यम से डेटा लीक
  प्रशिक्षण में लापरवाह डेटा समावेश से संवेदनशील जानकारी प्रकटीकरण होता है।

### Reference Links
### संदर्भ लिंक

1. [Lessons learned from ChatGPT’s Samsung leak](https://cybernews.com/security/chatgpt-samsung-leak-explained-lessons/): **Cybernews**
2. [AI data leak crisis: New tool prevents company secrets from being fed to ChatGPT](https://www.foxbusiness.com/politics/ai-data-leak-crisis-prevent-company-secrets-chatgpt): **Fox Business**
3. [ChatGPT Spit Out Sensitive Data When Told to Repeat ‘Poem’ Forever](https://www.wired.com/story/chatgpt-poem-forever-security-roundup/): **Wired**
4. [Using Differential Privacy to Build Secure Models](https://neptune.ai/blog/using-differential-privacy-to-build-secure-models-tools-methods-best-practices): **Neptune Blog**
5. [Proof Pudding (CVE-2019-20634)](https://avidml.org/database/avid-2023-v009/) **AVID** (`moohax` & `monoxgas`)
1। [चैट के सैमसंग लीक से सीखा गया सबक] (https://cybernews.com/security/chatgpt-samsung-leak-explained-edsons/): ** CyberNews **
2। [AI डेटा लीक संकट: नया टूल कंपनी के रहस्यों को चैट करने के लिए खिलाए जाने से रोकता है] (https://www.foxbusiness.com/politics/ai-data-leake-crisis-prevent-pecrets-chatgpt): * *फॉक्स बिजनेस **
3। [चैट ने संवेदनशील डेटा को थूक दिया जब ‘कविता को हमेशा के लिए दोहराने के लिए कहा गया] (https://www.wired.com/story/chatgpt-poem-forever-security-roundup/): ** वायर्ड **
4। [सुरक्षित मॉडल बनाने के लिए विभेदक गोपनीयता का उपयोग करके] (https://neptune.ai/blog/using-differential-privacy-to-build-build-secure-models-tools-stods-best-practices): ** नेप्च्यून ब्लॉग* *
5। [प्रूफ पुडिंग (CVE-2019-20634)]

### Related Frameworks and Taxonomies
### संबंधित फ्रेमवर्क और टैक्सोनॉमी

Refer to this section for comprehensive information, scenarios strategies relating to infrastructure deployment, applied environment controls and other best practices.
बुनियादी ढांचे की तैनाती, लागू पर्यावरण नियंत्रण और अन्य सर्वोत्तम प्रथाओं से संबंधित व्यापक जानकारी, परिदृश्य रणनीतियों के लिए इस खंड का संदर्भ लें।

- [AML.T0024.000 - Infer Training Data Membership](https://atlas.mitre.org/techniques/AML.T0024.000) **MITRE ATLAS**
- [AML.T0024.001 - Invert ML Model](https://atlas.mitre.org/techniques/AML.T0024.001) **MITRE ATLAS**
- [AML.T0024.002 - Extract ML Model](https://atlas.mitre.org/techniques/AML.T0024.002) **MITRE ATLAS**

- [AML.T0024.000 - INGE ट्रेनिंग डेटा सदस्यता]
- [AML.T0024.001 - इनवर्ट ML मॉडल] (https://atlas.mitre.org/techniques/aml.t0024.001) ** Miter Atlas **
- [AML.T0024.002 - एक्सट्रैक्ट एमएल मॉडल] (https://atlas.mitre.org/techniques/aml.t0024.002) ** मैटर एटलस **

