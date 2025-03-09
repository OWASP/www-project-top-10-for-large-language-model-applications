## LLM10:2025 अनियंत्रित खपत

### विवरण

अनियंत्रित खपत में LLM, इनपुट query या Prompt के आधार पर आउटपुट उत्पन्न करता हैं। अनुमान लगाना LLM का एक महत्वपूर्ण कार्य है, जिसमें प्रासंगिक प्रतिक्रियाओं तथा पूर्व आकलानों (predictions)को उत्पादन करने के लिए learned patterns एवं knowledge का प्रयोग करते हैं।

सेवा को बाधित (disrupt service) करने के लिए बनाए गए हमले, लक्ष्य के वित्तीय संसाधनों को क्षति पहुचना, या यहां तक ​​कि एक मॉडल के व्यवहार को क्लोन करके intellectual property को चोरी करना, इन सभी को सफल होने के लिए सामान्य वर्ग की Vulnerability पर निर्भर होना होता हैंं। अनियंत्रित खपत तब होती हैं जब एक LLM application users को अत्यधिक एवं अनियंत्रित निष्कर्षों का संचालन करने देती हैं, जिससे denial of service (DoS), economic losses, model theft, एवं service degradation जैसे जोखिम उत्पन्न होते हैंं। LLM की उच्च computational मांगें, विशेष रूप से cloud environments में, उन्हें संसाधन को exploit करने एवं अनधिकृत उपयोग के लिए असुरक्षित बनाती हैंं।

### Vulnerability के सामान्य उदाहरण

#### 1. Variable-Length Input Flood
  हमलावर अलग-अलग लंबाई के कई इनपुट के साथ LLM को ओवरलोड कर सकते हैंं, जिससे की वह process करने में आ रही अक्षमताओं को exploit कर सके। यह संसाधनों को खत्म एवं system को unresponsive एवं उसकी service availability को प्रभावित कर सकता हैं।
#### 2. Denial of Wallet (DoW)
  कार्यों की एक उच्च मात्रा से हमलावर cloud पर आधारित AI सेवाओं की cost-per-use मॉडल का फायदा उठाते हैंं, जिससे की provider पर अस्थिर वित्तीय बोझ आता हैंं जो की वित्तीय तौर पर बर्बाद कर सकता हैं।
#### 3. निरंतर होता Input Overflow
  LLM context window से अधिक बड़े इनपुट को लगातार भेजने से अत्यधिक computational संसाधन उपयोग हो सकते हैं, जिसके परिणामस्वरूप सेवा में गिरावट (service degradation) एवं कार्यों में व्यवधान (operational disruptions) आ सकते हैंं।
#### 4. Resource-Intensive Queries
  जटिल क्रमों या जटिल भाषा पैटर्न से जुड़े असामान्य रूप से मांग वाली queries को प्रस्तुत करना system संसाधनों को खत्म कर सकता हैं, जिससे की लंबे समय तक processing time एवं संभावित system failures आ सकते हैंं।
#### 5. APIs के माध्यम से Model Extraction
  हमलावर एक आधा-अधूरा मॉडल या shadow मॉडल बनाने के लिए पर्याप्त आउटपुट एकत्र करता हैं। इसके लिए वह सावधानीपूर्वक तैयार किए गए इनपुट एवं Prompt इंजेक्शन तकनीकों का उपयोग करके मॉडल APIs से query करता हैंं। यह न केवल बौद्धिक संपदा(intellectual property) चोरी के जोखिम को पैदा करता हैं, बल्कि मूल मॉडल की अखंडता को भी गिरता हैं।
#### 6. Functional Model Replication
  Synthetic प्रशिक्षण डेटा उत्पन्न करने के लिए लक्षित मॉडल का उपयोग करना हमलावरों को एक अन्य मूलभूत मॉडल को fine-tune करने की अनुमति देता हैं, जो की एक functional equivalent बनाता हैं। यह पारंपरिक query पर आधारित extraction विधियों को तेज करता हैं, जो proprietary मॉडल एवं technologies के लिए एक महत्वपूर्ण जोखिम प्रस्तुत करता हैं।
#### 7. Side-Channel Attacks
  दुर्भावनापूर्ण हमलावर side-channel attacks करने, model weights एवं architectural जानकारी पाने के लिए LLM की इनपुट फ़िल्टरिंग तकनीकों का फायदा उठते हैंं। यह मॉडल की सुरक्षा से compromise कर सकता हैं एवं आगे के exploit का कारण भी बन सकता हैं।

### रोकथाम एवं बचाव के लिये रणनीतियाँ

#### 1. इनपुट validation
  यह सुनिश्चित करने के लिए की इनपुट उचित आकार की सीमा में ही हों, सख्त इनपुट validation लागू करे।
#### 2. Logits एवं Logprobs के प्रकटीकरण को सीमित करें
  API प्रतिक्रियाओं में `logit_bias` एवं ` logprobs` के प्रकटीकरण को प्रतिबंधित या obfuscate (छिपाए) करें। विस्तृत संभावनाओं के बजाए केवल आवश्यक जानकारी प्रदान करें।
#### 3. Rate Limiting
  एक निश्चित अवधि में किसी एकल स्रोत के अनुरोधों की संख्या को प्रतिबंधित करने के लिए rate limiting एवं user quotas को लागू करें।
#### 4. Resource Allocation Management
  किसी user या अनुरोध को अत्यधिक संसाधनों की खपत से रोकने के लिए गतिशील रूप से संसाधनों के आवंटन एवं निगरानी को लागू करें।
#### 5. Timeouts एवं Throttling
  लंबे समय तक संसाधन की खपत को रोकने के लिए resource-intensive operations में timeouts एवं throttle को लागू करे ।
#### 6.Sandbox तकनिके
  नेटवर्क संसाधनों, आंतरिक सेवाओं एवं APIs तक LLM की पहुंच (access) को प्रतिबंधित करें। यह सभी सामान्य परिदृश्यों के लिए विशेष रूप से महत्वपूर्ण हैं क्योंकि यह आंतरिक (insider) जोखिमों एवं खतरों (hreats) को शामिल करता हैं। इसके अलावा, यह LLM application को डेटा एवं संसाधनों के लिए पहुंच (access) की सीमा को नियंत्रित करता हैं, जिससे की side-channel हमलों को कम कर सकते हैं।
#### 7. Comprehensive Logging, Monitoring एवं Anomaly Detection
  संसाधन के उपयोग की लगातार निगरानी करें एवं संसाधन की खपत के असामान्य पैटर्न का पता लगाने एवं प्रतिक्रिया/समाधान देने के लिए Logging को लागू करें।
#### 8. Watermarking
  LLM आउटपुट के अनधिकृत उपयोग को ढूँढने के लिए watermarking frameworks क प्रयोग करें।
#### 9. Graceful Degradation
  System को इस प्रकार का बनाए की वह भारी लोड में भी धीरे-धीरे कार्यक्षमता को घटाए जिससे की पूर्ण विफलता के बजाय आंशिक कार्यक्षमता बनी रहे।
#### 10. कतारबद्ध कार्यों को सीमित करें एवं मजबूत रूप से स्केल करें
  अलग-अलग मांगों को संभालने एवं consistent system प्रदर्शन सुनिश्चित करने के लिए को Dynamic scaling एवं load balancing को शामिल करते हुए, कतारबद्ध कार्यों एवं कुल कार्यों की संख्या पर प्रतिबंध लागू करें।
#### 11. प्रतिकूल मजबूती प्रशिक्षण
  प्रतिकूल प्रश्नों एवं extraction के प्रयासों का पता लगाने के लिए मॉडल्स को train करे।
#### 12. Glitch Token Filtering
  मॉडल की context विंडो में जोड़ने से पहले ज्ञात glitch tokens एवं scan outputs की सूची बनाएं।
#### 13. एक्सेस कंट्रोल
  LLM मॉडल repository एवं training environments तक अनधिकृत पहुंच (unauthorized access) को सीमित करने के लिए role आधारित access control (RBAC) एवं कम से कम विशेषाधिकार के सिद्धांत को मजबूती से लागू करें।
#### 14. Centralized ML Model Inventory
  उत्पादन में उपयोग किए जाने वाले मॉडल के लिए एक centralized ML model inventory या registry का उपयोग करें, उचित governance एवं access control सुनिश्चित करें।
#### 15. Automated MLOPS deployment
  Infrastructure के भीतर deployment नियंत्रणों को ओर मजबूत करे के लिए governance, tracking, एवं approval workflows के साथ automated MLOPS deployment को लागू करें।

### उदाहरण स्वरूप हमले के परिदृश्य

#### परिदृश्य#1: अनियंत्रित इनपुट आकार
  एक हमलावर ने LLM application को एक असामान्य रूप से बड़ा इनपुट दिया जो की texts डेटा को process करता हैं, जिसके परिणामस्वरूप अत्यधिक memeory उपयोग एवं CPU लोड होता हैं, जिससे system crash होता हैं या काफी धीमा हो जाता हैं।
#### परिदृश्य#2: बार-बार Requests
  एक हमलावर LLM APIs को अधिक मात्रा में अनुरोध भेजता हैं, जिससे computational संसाधनों की अत्यधिक खपत होती हैं एवं वैध users के लिए सेवा अनुपलब्ध हो जाती हैं।
#### परिदृश्य#3: संसाधन-गहन queries
  एक हमलावर विशिष्ट रूप से बनाए हुए इनपुट्स से LLM की सबसे computational महंगी प्रक्रियाओं को trigger कराता हैं, जिससे लंबे समय तक CPU ka उपयोग एवं संभावित system विफलता उत्पन्न होते हैं।
#### परिदृश्य#4: Denial of Wallet (DoW)
  एक हमलावर cloud पर आधारित AI सेवाओं के pay-per-use मॉडल का फायदा उठाने के लिए अत्यधिक कार्यों (operations) को उत्पन्न करता हैं, जिससे सेवा provider के लिए अस्थिर आ जाती हैं।
#### परिदृश्य#5: Functional Model Replication
  एक हमलावर synthetic प्रशिक्षण डेटा उत्पन्न करने एवं एक मॉडल को fine-tunes करने के लिये LLM APIs का उपयोग करता हैं, जिससे की functional equivalent एवं पारंपरिक मॉडल extraction की सीमाओं bypass होती हैं।
#### परिदृश्य#6: System इनपुट फ़िल्टरिंग को bypass करना
  एक दुर्भावनापूर्ण हमलावर इनपुट फ़िल्टरिंग तकनीकों और LLM के प्रीएंबल को bypass करता हैंं ताकि एक side-channel हमले को अंजाम दे सके और मॉडल की जानकारी को अपने नियंत्रण के एक remote controlled resource तक पहुच सके।

### संबंधित लिंक
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

### संबंधित फ्रेमवर्क एवं टैक्सोनॉमी

Infrastructure deployment, applied environment controls तथा अन्य सर्वोत्तम उपायों से संबंधित व्यापक जानकारी, परिदृश्यों की रणनीतियों के लिए इस खंड का संदर्भ लें।

- [MITRE CWE-400: Uncontrolled Resource Consumption](https://cwe.mitre.org/data/definitions/400.html) **MITRE Common Weakness Enumeration**
- [AML.TA0000 ML Model Access: Mitre ATLAS](https://atlas.mitre.org/tactics/AML.TA0000) & [AML.T0024 Exfiltration via ML Inference API](https://atlas.mitre.org/techniques/AML.T0024) **MITRE ATLAS**
- [AML.T0029 - Denial of ML Service](https://atlas.mitre.org/techniques/AML.T0029) **MITRE ATLAS**
- [AML.T0034 - Cost Harvesting](https://atlas.mitre.org/techniques/AML.T0034) **MITRE ATLAS**
- [AML.T0025 - Exfiltration via Cyber Means](https://atlas.mitre.org/techniques/AML.T0025) **MITRE ATLAS**
- [OWASP Machine Learning Security Top Ten - ML05:2023 Model Theft](https://owasp.org/www-project-machine-learning-security-top-10/docs/ML05_2023-Model_Theft.html) **OWASP ML Top 10**
- [API4:2023 - Unrestricted Resource Consumption](https://owasp.org/API-Security/editions/2023/en/0xa4-unrestricted-resource-consumption/) **OWASP Web Application Top 10**
- [OWASP Resource Management](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/) **OWASP Secure Coding Practices**