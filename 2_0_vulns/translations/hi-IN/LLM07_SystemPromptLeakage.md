## LLM07:2025 System Prompt Leakage
## LLM07: 2025 सिस्टम प्रॉम्प्ट रिसाव

### Description
### विवरण

The system prompt leakage vulnerability in LLMs refers to the risk that the system prompts or instructions used to steer the behavior of the model can also contain sensitive information that was not intended to be discovered. System prompts are designed to guide the model's output based on the requirements of the application, but may inadvertently contain secrets. When discovered, this information can be used to facilitate other attacks.
एलएलएमएस में सिस्टम प्रॉम्प्ट रिसाव भेद्यता इस जोखिम को संदर्भित करती है कि सिस्टम के व्यवहार को आगे बढ़ाने के लिए उपयोग किए जाने वाले सिस्टम या निर्देशों में संवेदनशील जानकारी भी हो सकती है जिसे खोजा जाने का इरादा नहीं था। सिस्टम प्रॉम्प्ट को एप्लिकेशन की आवश्यकताओं के आधार पर मॉडल के आउटपुट को निर्देशित करने के लिए डिज़ाइन किया गया है, लेकिन अनजाने में रहस्य हो सकते हैं। जब खोज की जाती है, तो इस जानकारी का उपयोग अन्य हमलों को सुविधाजनक बनाने के लिए किया जा सकता है।

It's important to understand that the system prompt should not be considered a secret, nor should it be used as a security control. Accordingly, sensitive data such as credentials, connection strings, etc. should not be contained within the system prompt language.
यह समझना महत्वपूर्ण है कि सिस्टम प्रॉम्प्ट को गुप्त नहीं माना जाना चाहिए, न ही इसे सुरक्षा नियंत्रण के रूप में उपयोग किया जाना चाहिए। तदनुसार, संवेदनशील डेटा जैसे कि क्रेडेंशियल्स, कनेक्शन स्ट्रिंग्स आदि को सिस्टम शीघ्र भाषा के भीतर समाहित नहीं किया जाना चाहिए।

Similarly, if a system prompt contains information describing different roles and permissions, or sensitive data like connection strings or passwords, while the disclosure of such information may be helpful, the fundamental security risk is not that these have been disclosed, it is that the application allows bypassing strong session management and authorization checks by delegating these to the LLM, and that sensitive data is being stored in a place that it should not be.
इसी तरह, यदि किसी सिस्टम प्रॉम्प्ट में विभिन्न भूमिकाओं और अनुमतियों का वर्णन करने वाली जानकारी होती है, या कनेक्शन स्ट्रिंग्स या पासवर्ड जैसे संवेदनशील डेटा, जबकि इस तरह की जानकारी का प्रकटीकरण सहायक हो सकता है, तो मौलिक सुरक्षा जोखिम यह नहीं है कि इनका खुलासा किया गया है, यह है कि एप्लिकेशन यह है मजबूत सत्र प्रबंधन और प्राधिकरण चेक को एलएलएम को सौंपने से बाईपास करने की अनुमति देता है, और यह संवेदनशील डेटा एक जगह पर संग्रहीत किया जा रहा है जो यह नहीं होना चाहिए।

In short: disclosure of the system prompt itself does not present the real risk -- the security risk lies with the underlying elements, whether that be sensitive information disclosure, system guardrails bypass, improper separation of privileges, etc. Even if the exact wording is not disclosed, attackers interacting with the system will almost certainly be able to determine many of the guardrails and formatting restrictions that are present in system prompt language in the course of using the application, sending utterances to the model, and observing the results.
संक्षेप में: सिस्टम का प्रकटीकरण खुद ही वास्तविक जोखिम पेश नहीं करता है - सुरक्षा जोखिम अंतर्निहित तत्वों के साथ निहित है, चाहे वह संवेदनशील जानकारी का खुलासा हो, सिस्टम रेलिंग बाईपास, विशेषाधिकारों का अनुचित पृथक्करण, आदि भले ही सटीक शब्द है। खुलासा नहीं किया गया, सिस्टम के साथ बातचीत करने वाले हमलावर लगभग निश्चित रूप से कई रेलिंग और फॉर्मेटिंग प्रतिबंधों को निर्धारित करने में सक्षम होंगे जो एप्लिकेशन का उपयोग करने के दौरान सिस्टम शीघ्र भाषा में मौजूद हैं, मॉडल को उच्चारण भेजते हैं, और परिणामों का अवलोकन करते हैं।

### Common Examples of Risk
### जोखिम के सामान्य उदाहरण

#### 1. Exposure of Sensitive Functionality
  The system prompt of the application may reveal sensitive information or functionality that is intended to be kept confidential, such as sensitive system architecture, API keys, database credentials, or user tokens.  These can be extracted or used by attackers to gain unauthorized access into the application. For example, a system prompt that contains the type of database used for a tool could allow the attacker to target it for SQL injection attacks.
#### 2. Exposure of Internal Rules
  The system prompt of the application reveals information on internal decision-making processes that should be kept confidential. This information allows attackers to gain insights into how the application works which could allow attackers to exploit weaknesses or bypass controls in the application. For example - There is a banking application that has a chatbot and its system prompt may reveal information like 
    >"The Transaction limit is set to $5000 per day for a user. The Total Loan Amount for a user is $10,000".
  This information allows the attackers to bypass the security controls in the application like doing transactions more than the set limit or bypassing the total loan amount.
#### 3. Revealing of Filtering Criteria
  A system prompt might ask the model to filter or reject sensitive content. For example, a model might have a system prompt like,
    >“If a user requests information about another user, always respond with ‘Sorry, I cannot assist with that request’”.
#### 4. Disclosure of Permissions and User Roles
  The system prompt could reveal the internal role structures or permission levels of the application. For instance, a system prompt might reveal,
    >“Admin user role grants full access to modify user records.”
  If the attackers learn about these role-based permissions, they could look for a privilege escalation attack.
#### 1। संवेदनशील कार्यक्षमता का एक्सपोजर
  एप्लिकेशन का सिस्टम प्रॉम्प्ट संवेदनशील जानकारी या कार्यक्षमता को प्रकट कर सकता है जिसे गोपनीय रखा जाना है, जैसे कि संवेदनशील सिस्टम आर्किटेक्चर, एपीआई कीज़, डेटाबेस क्रेडेंशियल्स, या उपयोगकर्ता टोकन।  इन्हें आवेदन में अनधिकृत पहुंच प्राप्त करने के लिए हमलावरों द्वारा निकाला या उपयोग किया जा सकता है। उदाहरण के लिए, एक सिस्टम प्रॉम्प्ट जिसमें एक टूल के लिए उपयोग किए जाने वाले डेटाबेस के प्रकार होते हैं, हमलावर को SQL इंजेक्शन हमलों के लिए इसे लक्षित करने की अनुमति दे सकता है।
#### 2। आंतरिक नियमों का एक्सपोजर
  एप्लिकेशन के सिस्टम प्रॉम्प्ट से आंतरिक निर्णय लेने की प्रक्रियाओं के बारे में जानकारी का पता चलता है जिसे गोपनीय रखा जाना चाहिए। यह जानकारी हमलावरों को अंतर्दृष्टि प्राप्त करने की अनुमति देती है कि आवेदन कैसे काम करता है जो हमलावरों को अनुप्रयोग में कमजोरियों या बायपास नियंत्रणों का फायदा उठाने की अनुमति दे सकता है। उदाहरण के लिए - एक बैंकिंग एप्लिकेशन है जिसमें एक चैटबॉट है और इसका सिस्टम प्रॉम्प्ट जानकारी को प्रकट कर सकता है जैसे 
    > "एक उपयोगकर्ता के लिए लेनदेन की सीमा $ 5000 प्रति दिन निर्धारित की जाती है। उपयोगकर्ता के लिए कुल ऋण राशि $ 10,000 है"।
  यह जानकारी हमलावरों को आवेदन में सुरक्षा नियंत्रण को बायपास करने की अनुमति देती है जैसे कि सेट सीमा से अधिक लेनदेन करना या कुल ऋण राशि को बायपास करना।
#### 3। फ़िल्टरिंग मानदंड का खुलासा
  एक सिस्टम प्रॉम्प्ट मॉडल को संवेदनशील सामग्री को फ़िल्टर या अस्वीकार करने के लिए कह सकता है। उदाहरण के लिए, एक मॉडल में एक सिस्टम प्रॉम्प्ट हो सकता है, जैसे
    > "यदि कोई उपयोगकर्ता किसी अन्य उपयोगकर्ता के बारे में जानकारी का अनुरोध करता है, तो हमेशा, क्षमा करें, मैं उस अनुरोध के साथ सहायता नहीं कर सकता"। "
#### 4। अनुमतियों और उपयोगकर्ता भूमिकाओं का प्रकटीकरण
  सिस्टम प्रॉम्प्ट आंतरिक भूमिका संरचनाओं या एप्लिकेशन की अनुमति स्तरों को प्रकट कर सकता है। उदाहरण के लिए, एक सिस्टम प्रॉम्प्ट प्रकट हो सकता है,
    > "व्यवस्थापक उपयोगकर्ता भूमिका उपयोगकर्ता रिकॉर्ड को संशोधित करने के लिए पूर्ण पहुंच अनुदान देता है।"
  यदि हमलावर इन भूमिका-आधारित अनुमतियों के बारे में सीखते हैं, तो वे एक विशेषाधिकार वृद्धि के हमले की तलाश कर सकते हैं।

### Prevention and Mitigation Strategies
### रोकथाम और शमन रणनीतियाँ

#### 1. Separate Sensitive Data from System Prompts
  Avoid embedding any sensitive information (e.g. API keys, auth keys, database names, user roles, permission structure of the application) directly in the system prompts. Instead, externalize such information to the systems that the model does not directly access.
#### 2. Avoid Reliance on System Prompts for Strict Behavior Control
  Since LLMs are susceptible to other attacks like prompt injections which can alter the system prompt, it is recommended to avoid using system prompts to control the model behavior where possible.  Instead, rely on systems outside of the LLM to ensure this behavior.  For example, detecting and preventing harmful content should be done in external systems.
#### 3. Implement Guardrails
  Implement a system of guardrails outside of the LLM itself.  While training particular behavior into a model can be effective, such as training it not to reveal its system prompt, it is not a guarantee that the model will always adhere to this.  An independent system that can inspect the output to determine if the model is in compliance with expectations is preferable to system prompt instructions.
#### 4. Ensure that security controls are enforced independently from the LLM
  Critical controls such as privilege separation, authorization bounds checks, and similar must not be delegated to the LLM, either through the system prompt or otherwise. These controls need to occur in a deterministic, auditable manner, and LLMs are not (currently) conducive to this. In cases where an agent is performing tasks, if those tasks require different levels of access, then multiple agents should be used, each configured with the least privileges needed to perform the desired tasks.
#### 1। सिस्टम प्रॉम्प्ट से संवेदनशील डेटा को अलग करें
  किसी भी संवेदनशील जानकारी (जैसे एपीआई कुंजियाँ, प्रामाणिक कुंजियाँ, डेटाबेस नाम, उपयोगकर्ता भूमिका, आवेदन की अनुमति संरचना) को सीधे सिस्टम में सीधे एम्बेड करने से बचें। इसके बजाय, ऐसी जानकारी को उन प्रणालियों के लिए बाहरी करें जो मॉडल सीधे एक्सेस नहीं करते हैं।
#### 2। सख्त व्यवहार नियंत्रण के लिए सिस्टम संकेत पर निर्भरता से बचें
  चूंकि LLMS अन्य हमलों जैसे शीघ्र इंजेक्शन के लिए अतिसंवेदनशील होते हैं जो सिस्टम प्रॉम्प्ट को बदल सकते हैं, जहां संभव हो तो मॉडल व्यवहार को नियंत्रित करने के लिए सिस्टम प्रॉम्प्ट का उपयोग करने से बचने की सिफारिश की जाती है।  इसके बजाय, इस व्यवहार को सुनिश्चित करने के लिए एलएलएम के बाहर प्रणालियों पर भरोसा करें।  उदाहरण के लिए, हानिकारक सामग्री का पता लगाना और रोकना बाहरी प्रणालियों में किया जाना चाहिए।
#### 3। रेलिंग को लागू करें
  एलएलएम के बाहर ही रेलिंग की एक प्रणाली को लागू करें।  जबकि एक मॉडल में विशेष व्यवहार को प्रशिक्षित करना प्रभावी हो सकता है, जैसे कि यह प्रशिक्षण देने के लिए कि वह अपने सिस्टम को प्रॉम्प्ट को प्रकट नहीं करता है, यह गारंटी नहीं है कि मॉडल हमेशा इसका पालन करेगा।  एक स्वतंत्र प्रणाली जो यह निर्धारित करने के लिए आउटपुट का निरीक्षण कर सकती है कि क्या मॉडल अपेक्षाओं के अनुपालन में है, सिस्टम शीघ्र निर्देशों के लिए बेहतर है।
#### 4। सुनिश्चित करें कि सुरक्षा नियंत्रण LLM से स्वतंत्र रूप से लागू किए गए हैं
  महत्वपूर्ण नियंत्रण जैसे कि विशेषाधिकार पृथक्करण, प्राधिकरण सीमा जांच, और इसी तरह को एलएलएम को नहीं दिया जाना चाहिए, या तो सिस्टम प्रॉम्प्ट के माध्यम से या अन्यथा। इन नियंत्रणों को एक नियतात्मक, श्रव्य तरीके से होने की आवश्यकता है, और LLMs (वर्तमान में) इसके लिए अनुकूल नहीं हैं। ऐसे मामलों में जहां कोई एजेंट कार्य कर रहा है, यदि उन कार्यों को विभिन्न स्तरों तक पहुंच की आवश्यकता होती है, तो कई एजेंटों का उपयोग किया जाना चाहिए, प्रत्येक को वांछित कार्यों को करने के लिए आवश्यक कम से कम विशेषाधिकारों के साथ कॉन्फ़िगर किया जाता है।

### Example Attack Scenarios
### उदाहरण हमले परिदृश्य

#### Scenario #1
   An LLM has a system prompt that contains a set of credentials used for a tool that it has been given access to.  The system prompt is leaked to an attacker, who then is able to use these credentials for other purposes.
#### Scenario #2
  An LLM has a system prompt prohibiting the generation of offensive content, external links, and code execution. An attacker extracts this system prompt and then uses a prompt injection attack to bypass these instructions, facilitating a remote code execution attack.
#### परिद्रश्य 1
   एक एलएलएम में एक सिस्टम प्रॉम्प्ट होता है जिसमें एक उपकरण के लिए उपयोग किए जाने वाले क्रेडेंशियल्स का एक सेट होता है जिसे उस तक पहुंच दी गई है।  सिस्टम प्रॉम्प्ट एक हमलावर को लीक कर दिया जाता है, जो तब अन्य उद्देश्यों के लिए इन क्रेडेंशियल्स का उपयोग करने में सक्षम होता है।
#### परिदृश्य#2
  एक एलएलएम में एक प्रणाली है जो आक्रामक सामग्री, बाहरी लिंक और कोड निष्पादन की पीढ़ी को प्रतिबंधित करती है। एक हमलावर इस प्रणाली को प्रॉम्प्ट करता है और फिर एक दूरस्थ कोड निष्पादन हमले की सुविधा प्रदान करते हुए, इन निर्देशों को बायपास करने के लिए एक शीघ्र इंजेक्शन हमले का उपयोग करता है।

### Reference Links
### संदर्भ लिंक

1. [SYSTEM PROMPT LEAK](https://x.com/elder_plinius/status/1801393358964994062): Pliny the prompter
2. [Prompt Leak](https://www.prompt.security/vulnerabilities/prompt-leak): Prompt Security
3. [chatgpt_system_prompt](https://github.com/LouisShark/chatgpt_system_prompt): LouisShark
4. [leaked-system-prompts](https://github.com/jujumilk3/leaked-system-prompts): Jujumilk3
5. [OpenAI Advanced Voice Mode System Prompt](https://x.com/Green_terminals/status/1839141326329360579): Green_Terminals
1। [सिस्टम प्रॉम्प्ट लीक] (https://x.com/elder_plinius/status/180139335896494062): प्लिनी द प्रॉपर्टर
2। [शीघ्र लीक] (https://www.prompt.security/vulnerabilities/prompt-leake): शीघ्र सुरक्षा
3।
4।
5। [Openai एडवांस्ड वॉयस मोड सिस्टम प्रॉम्प्ट] (https://x.com/green_terminals/status/1839141326329360579): GREEN_TERMINALS

### Related Frameworks and Taxonomies
### संबंधित फ्रेमवर्क और टैक्सोनॉमी

Refer to this section for comprehensive information, scenarios strategies relating to infrastructure deployment, applied environment controls and other best practices.
बुनियादी ढांचे की तैनाती, लागू पर्यावरण नियंत्रण और अन्य सर्वोत्तम प्रथाओं से संबंधित व्यापक जानकारी, परिदृश्य रणनीतियों के लिए इस खंड का संदर्भ लें।

- [AML.T0051.000 - LLM Prompt Injection: Direct (Meta Prompt Extraction)](https://atlas.mitre.org/techniques/AML.T0051.000) **MITRE ATLAS**

- [AML.T0051.000 - LLM प्रॉम्प्ट इंजेक्शन: डायरेक्ट (मेटा प्रॉम्प्ट एक्सट्रैक्शन)] (https://atlas.mitre.org/techniques/aml.t0051.000)

