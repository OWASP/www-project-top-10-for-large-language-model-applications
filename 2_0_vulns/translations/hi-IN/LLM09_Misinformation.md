## LLM09:2025 Misinformation
## LLM09: 2025 गलत सूचना

### Description
### विवरण

Misinformation from LLMs poses a core vulnerability for applications relying on these models. Misinformation occurs when LLMs produce false or misleading information that appears credible. This vulnerability can lead to security breaches, reputational damage, and legal liability.
LLMS से गलत सूचना इन मॉडलों पर भरोसा करने वाले अनुप्रयोगों के लिए एक मुख्य भेद्यता है। गलत सूचना तब होती है जब LLMS झूठी या भ्रामक जानकारी का उत्पादन करता है जो विश्वसनीय दिखाई देता है। इस भेद्यता से सुरक्षा उल्लंघनों, प्रतिष्ठित क्षति और कानूनी देयता हो सकती है।

One of the major causes of misinformation is hallucination—when the LLM generates content that seems accurate but is fabricated. Hallucinations occur when LLMs fill gaps in their training data using statistical patterns, without truly understanding the content. As a result, the model may produce answers that sound correct but are completely unfounded. While hallucinations are a major source of misinformation, they are not the only cause; biases introduced by the training data and incomplete information can also contribute.
गलत सूचनाओं के प्रमुख कारणों में से एक मतिभ्रम है - जब एलएलएम ऐसी सामग्री उत्पन्न करता है जो सटीक लगती है लेकिन गढ़ा जाता है। मतिभ्रम तब होता है जब एलएलएमएस सांख्यिकीय पैटर्न का उपयोग करके अपने प्रशिक्षण डेटा में अंतराल भरते हैं, वास्तव में सामग्री को समझे बिना। नतीजतन, मॉडल उन उत्तरों का उत्पादन कर सकता है जो सही ध्वनि करते हैं लेकिन पूरी तरह से निराधार हैं। जबकि मतिभ्रम गलत सूचना का एक प्रमुख स्रोत है, वे एकमात्र कारण नहीं हैं; प्रशिक्षण डेटा और अपूर्ण जानकारी द्वारा पेश किए गए पूर्वाग्रह भी योगदान कर सकते हैं।

A related issue is overreliance. Overreliance occurs when users place excessive trust in LLM-generated content, failing to verify its accuracy. This overreliance exacerbates the impact of misinformation, as users may integrate incorrect data into critical decisions or processes without adequate scrutiny.
एक संबंधित मुद्दा अतिवृद्धि है। ओवररेक्शन तब होता है जब उपयोगकर्ता एलएलएम-जनित सामग्री में अत्यधिक विश्वास रखते हैं, इसकी सटीकता को सत्यापित करने में विफल रहते हैं। यह अतिव्यापी गलत सूचना के प्रभाव को बढ़ाता है, क्योंकि उपयोगकर्ता पर्याप्त जांच के बिना महत्वपूर्ण निर्णयों या प्रक्रियाओं में गलत डेटा को एकीकृत कर सकते हैं।

### Common Examples of Risk
### जोखिम के सामान्य उदाहरण

#### 1. Factual Inaccuracies
  The model produces incorrect statements, leading users to make decisions based on false information. For example, Air Canada's chatbot provided misinformation to travelers, leading to operational disruptions and legal complications. The airline was successfully sued as a result.
  (Ref. link: [BBC](https://www.bbc.com/travel/article/20240222-air-canada-chatbot-misinformation-what-travellers-should-know))
#### 2. Unsupported Claims
  The model generates baseless assertions, which can be especially harmful in sensitive contexts such as healthcare or legal proceedings. For example, ChatGPT fabricated fake legal cases, leading to significant issues in court.
  (Ref. link: [LegalDive](https://www.legaldive.com/news/chatgpt-fake-legal-cases-generative-ai-hallucinations/651557/))
#### 3. Misrepresentation of Expertise
  The model gives the illusion of understanding complex topics, misleading users regarding its level of expertise. For example, chatbots have been found to misrepresent the complexity of health-related issues, suggesting uncertainty where there is none, which misled users into believing that unsupported treatments were still under debate.
  (Ref. link: [KFF](https://www.kff.org/health-misinformation-monitor/volume-05/))
#### 4. Unsafe Code Generation
  The model suggests insecure or non-existent code libraries, which can introduce vulnerabilities when integrated into software systems. For example, LLMs propose using insecure third-party libraries, which, if trusted without verification, leads to security risks.
  (Ref. link: [Lasso](https://www.lasso.security/blog/ai-package-hallucinations))
#### 1। तथ्यात्मक अशुद्धि
  मॉडल गलत कथन का उत्पादन करता है, प्रमुख उपयोगकर्ता झूठी जानकारी के आधार पर निर्णय लेने के लिए। उदाहरण के लिए, एयर कनाडा के चैटबॉट ने यात्रियों को गलत सूचना प्रदान की, जिससे परिचालन व्यवधान और कानूनी जटिलताओं के लिए अग्रणी। परिणामस्वरूप एयरलाइन पर सफलतापूर्वक मुकदमा चलाया गया।
  (Ref।
#### 2। असमर्थित दावे
  मॉडल आधारहीन दावे उत्पन्न करता है, जो विशेष रूप से संवेदनशील संदर्भों जैसे कि स्वास्थ्य सेवा या कानूनी कार्यवाही में हानिकारक हो सकता है। उदाहरण के लिए, CHATGPT ने नकली कानूनी मामलों को गढ़ा, जिससे अदालत में महत्वपूर्ण मुद्दे मिले।
  (Ref।
#### 3। विशेषज्ञता की गलत बयानी
  मॉडल जटिल विषयों को समझने का भ्रम देता है, उपयोगकर्ताओं को इसकी विशेषज्ञता के स्तर के बारे में भ्रमित करता है। उदाहरण के लिए, चैटबॉट्स को स्वास्थ्य से संबंधित मुद्दों की जटिलता को गलत तरीके से प्रस्तुत करने के लिए पाया गया है, जिसमें अनिश्चितता का सुझाव दिया गया है, जहां कोई नहीं है, जिसने उपयोगकर्ताओं को यह मानने में गुमराह किया कि असमर्थित उपचार अभी भी बहस के अधीन थे।
  (Ref।
#### 4। असुरक्षित कोड जनरेशन
  मॉडल असुरक्षित या गैर-मौजूद कोड पुस्तकालयों का सुझाव देता है, जो सॉफ्टवेयर सिस्टम में एकीकृत होने पर कमजोरियों का परिचय दे सकता है। उदाहरण के लिए, LLMS असुरक्षित तृतीय-पक्ष पुस्तकालयों का उपयोग करके प्रस्तावित करता है, जो कि यदि सत्यापन के बिना भरोसा किया जाता है, तो सुरक्षा जोखिमों की ओर जाता है।
  (Ref।

### Prevention and Mitigation Strategies
### रोकथाम और शमन रणनीतियाँ

#### 1. Retrieval-Augmented Generation (RAG)
  Use Retrieval-Augmented Generation to enhance the reliability of model outputs by retrieving relevant and verified information from trusted external databases during response generation. This helps mitigate the risk of hallucinations and misinformation.
#### 2. Model Fine-Tuning
  Enhance the model with fine-tuning or embeddings to improve output quality. Techniques such as parameter-efficient tuning (PET) and chain-of-thought prompting can help reduce the incidence of misinformation.
#### 3. Cross-Verification and Human Oversight
  Encourage users to cross-check LLM outputs with trusted external sources to ensure the accuracy of the information. Implement human oversight and fact-checking processes, especially for critical or sensitive information. Ensure that human reviewers are properly trained to avoid overreliance on AI-generated content.
#### 4. Automatic Validation Mechanisms
  Implement tools and processes to automatically validate key outputs, especially output from high-stakes environments.
#### 5. Risk Communication
  Identify the risks and possible harms associated with LLM-generated content, then clearly communicate these risks and limitations to users, including the potential for misinformation.
#### 6. Secure Coding Practices
  Establish secure coding practices to prevent the integration of vulnerabilities due to incorrect code suggestions.
#### 7. User Interface Design
  Design APIs and user interfaces that encourage responsible use of LLMs, such as integrating content filters, clearly labeling AI-generated content and informing users on limitations of reliability and accuracy. Be specific about the intended field of use limitations.
#### 8. Training and Education
  Provide comprehensive training for users on the limitations of LLMs, the importance of independent verification of generated content, and the need for critical thinking. In specific contexts, offer domain-specific training to ensure users can effectively evaluate LLM outputs within their field of expertise.
#### 1। पुनर्प्राप्ति-अगस्त पीढ़ी (आरएजी)
  प्रतिक्रिया पीढ़ी के दौरान विश्वसनीय बाहरी डेटाबेस से प्रासंगिक और सत्यापित जानकारी को पुनः प्राप्त करके मॉडल आउटपुट की विश्वसनीयता को बढ़ाने के लिए पुनर्प्राप्ति-संवर्धित पीढ़ी का उपयोग करें। यह मतिभ्रम और गलत सूचना के जोखिम को कम करने में मदद करता है।
#### 2। मॉडल फाइन-ट्यूनिंग
  आउटपुट गुणवत्ता में सुधार के लिए ठीक-ट्यूनिंग या एम्बेडिंग के साथ मॉडल को बढ़ाएं। पैरामीटर-कुशल ट्यूनिंग (पीईटी) और चेन-ऑफ-थॉट प्रॉम्प्टिंग जैसी तकनीकें गलत सूचना की घटनाओं को कम करने में मदद कर सकती हैं।
#### 3। क्रॉस-वेरिफिकेशन और ह्यूमन ओवरसाइट
  जानकारी की सटीकता सुनिश्चित करने के लिए विश्वसनीय बाहरी स्रोतों के साथ एलएलएम आउटपुट को क्रॉस-चेक करने के लिए उपयोगकर्ताओं को प्रोत्साहित करें। मानव निरीक्षण और तथ्य-जाँच प्रक्रियाओं को लागू करें, विशेष रूप से महत्वपूर्ण या संवेदनशील जानकारी के लिए। सुनिश्चित करें कि मानव समीक्षकों को एआई-जनित सामग्री पर अतिरंजना से बचने के लिए ठीक से प्रशिक्षित किया जाता है।
#### 4। स्वचालित सत्यापन तंत्र
  उपकरण और प्रक्रियाओं को लागू करने के लिए स्वचालित रूप से प्रमुख आउटपुट को मान्य करने के लिए, विशेष रूप से उच्च-दांव वातावरण से आउटपुट।
#### 5। जोखिम संचार
  एलएलएम-जनित सामग्री से जुड़े जोखिमों और संभावित हानि की पहचान करें, फिर स्पष्ट रूप से इन जोखिमों और सीमाओं को उपयोगकर्ताओं के लिए संवाद करें, जिसमें गलत सूचना की क्षमता भी शामिल है।
#### 6। सुरक्षित कोडिंग प्रथाओं
  गलत कोड सुझावों के कारण कमजोरियों के एकीकरण को रोकने के लिए सुरक्षित कोडिंग प्रथाओं को स्थापित करें।
#### 7। उपयोगकर्ता इंटरफ़ेस डिजाइन
  डिजाइन एपीआई और उपयोगकर्ता इंटरफेस जो एलएलएम के जिम्मेदार उपयोग को प्रोत्साहित करते हैं, जैसे कि सामग्री फ़िल्टर को एकीकृत करना, स्पष्ट रूप से एआई-जनित सामग्री को लेबल करना और उपयोगकर्ताओं को विश्वसनीयता और सटीकता की सीमाओं पर सूचित करना। उपयोग सीमाओं के इच्छित क्षेत्र के बारे में विशिष्ट रहें।
#### 8। प्रशिक्षण और शिक्षा
  एलएलएम की सीमाओं पर उपयोगकर्ताओं के लिए व्यापक प्रशिक्षण प्रदान करें, उत्पन्न सामग्री के स्वतंत्र सत्यापन का महत्व, और महत्वपूर्ण सोच की आवश्यकता। विशिष्ट संदर्भों में, उपयोगकर्ताओं को अपने विशेषज्ञता के क्षेत्र में एलएलएम आउटपुट का प्रभावी ढंग से मूल्यांकन करने के लिए डोमेन-विशिष्ट प्रशिक्षण की पेशकश करें।

### Example Attack Scenarios
### उदाहरण हमले परिदृश्य

#### Scenario #1
  Attackers experiment with popular coding assistants to find commonly hallucinated package names. Once they identify these frequently suggested but nonexistent libraries, they publish malicious packages with those names to widely used repositories. Developers, relying on the coding assistant's suggestions, unknowingly integrate these poised packages into their software. As a result, the attackers gain unauthorized access, inject malicious code, or establish backdoors, leading to significant security breaches and compromising user data.
#### Scenario #2
  A company provides a chatbot for medical diagnosis without ensuring sufficient accuracy. The chatbot provides poor information, leading to harmful consequences for patients. As a result, the company is successfully sued for damages. In this case, the safety and security breakdown did not require a malicious attacker but instead arose from the insufficient oversight and reliability of the LLM system. In this scenario, there is no need for an active attacker for the company to be at risk of reputational and financial damage.
#### परिद्रश्य 1
  आम तौर पर मतिभ्रम पैकेज नामों को खोजने के लिए हमलावर लोकप्रिय कोडिंग सहायकों के साथ प्रयोग करते हैं। एक बार जब वे इन अक्सर सुझाए गए लेकिन नॉट्सिस्टेंट लाइब्रेरीज़ की पहचान करते हैं, तो वे उन नामों के साथ दुर्भावनापूर्ण पैकेज प्रकाशित करते हैं जो व्यापक रूप से उपयोग किए जाने वाले रिपॉजिटरी के लिए होते हैं। डेवलपर्स, कोडिंग सहायक के सुझावों पर भरोसा करते हुए, अनजाने में इन कवि पैकेजों को अपने सॉफ़्टवेयर में एकीकृत करते हैं। नतीजतन, हमलावर अनधिकृत पहुंच प्राप्त करते हैं, दुर्भावनापूर्ण कोड को इंजेक्ट करते हैं, या बैकडोर स्थापित करते हैं, जिससे महत्वपूर्ण सुरक्षा उल्लंघनों और उपयोगकर्ता डेटा से समझौता होता है।
#### परिदृश्य#2
  एक कंपनी पर्याप्त सटीकता सुनिश्चित किए बिना चिकित्सा निदान के लिए एक चैटबॉट प्रदान करती है। चैटबॉट खराब जानकारी प्रदान करता है, जिससे रोगियों के लिए हानिकारक परिणाम होते हैं। नतीजतन, कंपनी को सफलतापूर्वक नुकसान के लिए मुकदमा दायर किया गया है। इस मामले में, सुरक्षा और सुरक्षा टूटने के लिए एक दुर्भावनापूर्ण हमलावर की आवश्यकता नहीं थी, बल्कि एलएलएम प्रणाली की अपर्याप्त निरीक्षण और विश्वसनीयता से उत्पन्न हुई। इस परिदृश्य में, कंपनी के प्रति प्रतिष्ठित और वित्तीय क्षति के जोखिम के लिए एक सक्रिय हमलावर की आवश्यकता नहीं है।

### Reference Links
### संदर्भ लिंक

1. [AI Chatbots as Health Information Sources: Misrepresentation of Expertise](https://www.kff.org/health-misinformation-monitor/volume-05/): **KFF**
2. [Air Canada Chatbot Misinformation: What Travellers Should Know](https://www.bbc.com/travel/article/20240222-air-canada-chatbot-misinformation-what-travellers-should-know): **BBC**
3. [ChatGPT Fake Legal Cases: Generative AI Hallucinations](https://www.legaldive.com/news/chatgpt-fake-legal-cases-generative-ai-hallucinations/651557/): **LegalDive**
4. [Understanding LLM Hallucinations](https://towardsdatascience.com/llm-hallucinations-ec831dcd7786): **Towards Data Science**
5. [How Should Companies Communicate the Risks of Large Language Models to Users?](https://techpolicy.press/how-should-companies-communicate-the-risks-of-large-language-models-to-users/): **Techpolicy**
6. [A news site used AI to write articles. It was a journalistic disaster](https://www.washingtonpost.com/media/2023/01/17/cnet-ai-articles-journalism-corrections/): **Washington Post**
7. [Diving Deeper into AI Package Hallucinations](https://www.lasso.security/blog/ai-package-hallucinations): **Lasso Security**
8. [How Secure is Code Generated by ChatGPT?](https://arxiv.org/abs/2304.09655): **Arvix**
9. [How to Reduce the Hallucinations from Large Language Models](https://thenewstack.io/how-to-reduce-the-hallucinations-from-large-language-models/): **The New Stack**
10. [Practical Steps to Reduce Hallucination](https://newsletter.victordibia.com/p/practical-steps-to-reduce-hallucination): **Victor Debia**
11. [A Framework for Exploring the Consequences of AI-Mediated Enterprise Knowledge](https://www.microsoft.com/en-us/research/publication/a-framework-for-exploring-the-consequences-of-ai-mediated-enterprise-knowledge-access-and-identifying-risks-to-workers/): **Microsoft**
1। [स्वास्थ्य सूचना स्रोतों के रूप में एआई चैटबॉट्स: विशेषज्ञता की गलत बयानी] (https://www.kff.org/health-misinformation-monitor/volume-05/): ** kff **
2। [एयर कनाडा चैटबॉट मिसिनफॉर्मेशन: ट्रैवलर्स को क्या पता होना चाहिए] (https://www.bbc.com/travel/article/20240222-air-canada-chatbot-misinformation-what-travellers-should-nnow): ** BBC): **
3। [चैटगेट फर्जी कानूनी मामले: जनरेटिव एआई मतिभ्रम]
4। [एलएलएम मतिभ्रम को समझना] (https://towardsdatascience.com/llm-hallucinations-ec831dcd7786): ** डेटा विज्ञान की ओर ** **
5। [कंपनियों को उपयोगकर्ताओं के लिए बड़े भाषा मॉडल के जोखिमों को कैसे संप्रेषित करना चाहिए?] (Https://techpolicy.press/how-should-companies-communicate-the-crisks-of-targe-tanguage-models-to-users// ): ** TechPolicy **
6। [एक समाचार साइट ने लेख लिखने के लिए एआई का उपयोग किया। यह एक पत्रकारिता की आपदा थी] (https://www.washingtonpost.com/media/2023/01/17/cnet-ai-articles-journalism-corrections/): ** वाशिंगटन पोस्ट **
7। [एआई पैकेज मतिभ्रम में गहराई से गोताखोरी]
8। [CHATGPT द्वारा उत्पन्न कोड कितना सुरक्षित है?] (Https://arxiv.org/abs/2304.09655): ** arvix **
9। [बड़े भाषा के मॉडल से मतिभ्रम को कैसे कम करें] (https://thenewstack.io/how-to-duce-the-hallucinations-from-barge-nudels/): ** नया स्टैक **
10। [मतिभ्रम को कम करने के लिए व्यावहारिक कदम] (https://newsletter.victordibia.com/p/practical-steps-to-reduce- हॉलिकेशन): ** विक्टर डेबिया **
11। [एआई-मध्यस्थता उद्यम ज्ञान के परिणामों की खोज के लिए एक रूपरेखा] (https://www.microsoft.com/en-us/research/publication/a-framework-for-exploring-the-consemences-of-ai -मिटेड-एंटरप्राइज-ज्ञान-एक्सेस-एंड-आइडेंटिफ़ाइंग-रिस्क-टू-वर्कर्स/): ** Microsoft **

### Related Frameworks and Taxonomies
### संबंधित फ्रेमवर्क और टैक्सोनॉमी

Refer to this section for comprehensive information, scenarios strategies relating to infrastructure deployment, applied environment controls and other best practices.
बुनियादी ढांचे की तैनाती, लागू पर्यावरण नियंत्रण और अन्य सर्वोत्तम प्रथाओं से संबंधित व्यापक जानकारी, परिदृश्यों की रणनीतियों के लिए इस खंड का संदर्भ लें।

- [AML.T0048.002 - Societal Harm](https://atlas.mitre.org/techniques/AML.T0048) **MITRE ATLAS**

- [AML.T0048.002 - सामाजिक नुकसान] (https://atlas.mitre.org/techniques/aml.t0048) ** Miter Atlas **

