## LLM09: 2025 गलत सूचना

### विवरण

LLM के द्वारा दी गई गलत सूचना, इन मॉडलों पर भरोसा करने वाली applications के लिए एक मुख्य Vulnerability हैं । गलत सूचना का संचार तब होता हैंं, जब LLM विश्वसनीय दिखने वाली झूठी या भ्रामक जानकारीयाँ बनाता हैं । इस Vulnerability से सुरक्षा उल्लंघ (security breaches), प्रतिष्ठा की क्षति (reputational damage) या कानूनी समस्या (legal liability) भी हो सकती हैं ।

गलत सूचनाओं के प्रमुख कारणों में से एक hallucination हैंं । इसमें LLM ऐसी सामग्री बनाता हैं जो सटीक लगते हुँए भी बनावटी होती हैं, जिसके लिए वह वास्तव में सामग्री को समझे बिना ही statistical patterns से अपने प्रशिक्षण डेटा के gaps को भरता हैंं । इससे मॉडल वह उत्तर देता हैं जो सही लगते हुँए भी पूरी तरह से निराधार होते हैंं । इसमें hallucination के अलावा भी प्रशिक्षण डेटा एवं अपूर्ण जानकारी से होने वाले biases भी मुख्य योगदान दे सकते हैंं ।

इसी प्रकार Overreliance हैं, जिसमें LLM द्वारा बनाई सामग्री पर user अत्यधिक विश्वास करके उसकी सटीकता को भी verify नहीं करता । यह वस्तुतः गलत सूचना के प्रभाव को बढ़ाता हैं, क्योंकि user पर्याप्त जांच के बिना ही महत्वपूर्ण निर्णयों या प्रक्रियाओं में गलत डेटा का प्रयोग कर लेता हैंं ।

### जोखिम के सामान्य उदाहरण

#### 1. तथ्यात्मक अशुद्धि
  मॉडल गलत कथनों को बनाता हैं, जिससे की user झूठी जानकारी के आधार पर निर्णय लेते हैंं । उदाहरण के लिए, Air Canada के चैटबॉट ने यात्रियों को गलत सूचना दी, जिससे परिचालन में व्यवधान (operational disruptions) एवं कानूनी जटिलताएँ (legal complications) पैदा हो गई । जिसके परिणामस्वरूप airline पर मुकदमा चलाया गया ।
  (संदर्भित link: [BBC](https://www.bbc.com/travel/article/20240222-air-canada-chatbot-misinformation-what-travellers-should-know))
#### 2. असमर्थित दावे
  मॉडल आधारहीन दावे करता हैं, जो मुखयतः संवेदनशील संदर्भों जैसें कि स्वास्थ्य सेवा या कानूनी कार्यवाही में हानिकारक हो सकते हैं । उदाहरण के लिए, CHATGPT ने नकली कानूनी मामलों को गढ़ा, जिससे की अदालत में महत्वपूर्ण समस्याएँ देखने को मिली ।
  (संदर्भित link: [LegalDive](https://www.legaldive.com/news/chatgpt-fake-legal-cases-generative-ai-hallucinations/651557/))
#### 3. विशेषज्ञता से बहकना
  मॉडल जटिल विषयों को समझने का भ्रम बनाता हैं, जिससे की users को इसकी विशेषज्ञता के स्तर के बारे में भ्रम पैदा होते हैं । उदाहरण के लिए, चैटबॉट्स को स्वास्थ्य संबंधित मुद्दों की जटिलता को गलत तरीके से प्रस्तुत करतें पाया गया हैं, जिससें की users को कुछ उपचारों पर संदेह होने लगा ।
  (संदर्भित link: [KFF](https://www.kff.org/health-misinformation-monitor/volume-05/))
#### 4. असुरक्षित code  की उत्पत्ति
  मॉडल असुरक्षित या गैर-मौजूद code libraries सूझाता हैं, जो की software में प्रयोग होने पर vulnerabilities पैदा कर सकती हैं । उदाहरण के लिए, LLM कुछ असुरक्षित third-party libraries सूझाता हैं, जो कि validation के बिना सुरक्षा जोखिमों को पैदा कर सकते हैं ।
  (संदर्भित link: [Lasso](https://www.lasso.security/blog/ai-package-hallucinations))

### रोकथाम एवं बचाव के लिये रणनीतियाँ

#### 1. Retrieval-Augmented Generation (RAG)
  प्रतिक्रिया देने के दौरान Retrieval-Augmented Generation का उपयोग करें, जो की विश्वसनीय बाहरी डेटाबेस से प्रासंगिक एवं verified जानकारी को प्राप्त करके मॉडल आउटपुट की विश्वसनीयता को बड़ाता हैं । यह hallucination एवं गलत सूचना के जोखिम को कम करने में भी मदद करता हैं ।
#### 2. मॉडल fine-tuning
  मॉडल के आउटपुट की गुणवत्ता में सुधार के लिए fine-tuning या embeddings का प्रयोग करें । Parameter-efficient tuning (PET) एवं chain-of-thought prompting जैसी तकनीकें भी गलत सूचना को कम करने में मदद कर सकती हैंं ।
#### 3. Cross-Verification एवं Cross-Verification
  जानकारी की सटीकता सुनिश्चित करने के लिए, विश्वसनीय बाहरी स्रोतों के आधार पर LLM के आउटपुट को जाँचे । मानव निरीक्षण एवं fact-checking की प्रक्रियाओं को लागू करें, विशेष रूप से महत्वपूर्ण या संवेदनशील जानकारी के लिए । मानव समीक्षकों को AI से उत्पन्न सामग्री पर overreliance से बचने के लिए ठीक से प्रशिक्षित करें ।
#### 4. स्वचालित validation तंत्र
  ऐसे उपकरण एवं प्रक्रियाओं को लागू करें जो स्वचालित (automatic) रूप से प्रमुख आउटपुट (key outputs) की जाँच करें, विशेष रूप से high-stakes environments वाले outputs की ।
#### 5. जोखिम संचार
  LLM द्वारा उत्पन्न सामग्री से जुड़े जोखिमों एवं संभावित हानीयों की पहचान करें, फिर स्पष्ट रूप से इन जोखिमों एवं सीमाओं को users को बताएँ, जिसमें गलत सूचना भी शामिल हैं ।
#### 6. Secure Coding Practices
  गलत code  सुझावों के कारण होने वाली vulnerabilities को रोकने के लिए Secure Coding Practices को लागू करें ।
#### 7. UI डिजाइन
  ऐसी API एवं user इंटरफेस बनाएँ जो LLM के जिम्मेदार उपयोग को प्रोत्साहित करें, जैसें कि सामग्री की छताई के लिए फ़िल्टर को जोड़ना, स्पष्ट रूप से AI से उत्पन्न सामग्री को लेबल करना एवं users को विश्वसनीयता (reliability) एवं सटीकता (accuracy) की सीमायें बताना । इसी प्रकार use limitations के intended field के बारे में विस्तृत (specific) रहें ।
#### 8. प्रशिक्षण एवं शिक्षा
  LLM की सीमाओं के बारे में users को प्रशिक्षण दे, उत्पन्न सामग्री के स्वतंत्र validation का महत्व, एवं critical thinking की आवश्यकता के बारे में समझाएँ । विशिष्ट जगहों पर, users को उसकी विशेषज्ञता के क्षेत्र में LLM आउटपुट का प्रभावी ढंग से मूल्यांकन करने के लिए domain-specific प्रशिक्षण भी प्रदान करें ।

### उदाहरण स्वरूप हमलें के परिदृश्य

#### परिद्रश्य#1
  आम तौर पर hallucination करने वाले packages को खोजने के लिए हमलावर (malicious attacker) लोकप्रिय कोडिंग सहायकों (coding assistants) का प्रयोग करता हैंं । वे इन frequently suggested (अक्सर सुझाया गया) लेकिन nonexistent libraries की पहचान करके, ज्यादा प्रयोग में आने वाली repositories पर उन नामों के साथ दुर्भावनापूर्ण Package प्रकाशित करतें हैंं । जिससे developer कोडिंग सहायक  (coding assistant) के सुझावों पर अनजाने में ही इन poised (दुर्भावनापूर्ण) packages को अपने software में जोड़ देते हैं । जिससे हमलावार अनाधिकृत पहूँच (unauthorized access) प्राप्त करके दुर्भावनापूर्ण code  को inject या backdoors स्थापित कर सकते हैंं, जिससे महत्वपूर्ण सुरक्षा का उल्लंघन (significant security breaches) एवं user डेटा से compromise होता हैं ।
#### परिदृश्य#2
  एक कंपनी पर्याप्त सटीकता (accuracy) सुनिश्चित किए बिना ही चिकित्सा निदान (medical diagnosis) के लिए एक चैटबॉट देती हैं । चैटबॉट की खराब जानकारी से रोगियों को हानि होती हैंं । नतीजतन, कंपनी के खिलाफ नुकसान के लिए मुकदमा दायर किया गया । इस मामले में गलती किसी हमलावर (malicious attacker) की नहीं बल्कि LLM प्रणाली में किये गए अपर्याप्त निरीक्षण (insufficient oversight) एवं विश्वसनीयता (reliability) की हैं । इस परिदृश्य में, कंपनी की प्रतिष्ठित एवं वित्तीय क्षति के लिए कोई सक्रिय हमलावर (malicious attacker) की आवश्यकता नहीं हैं ।

### संबंधित लिंक

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

### संबंधित फ्रेमवर्क (frameworks) एवं टैक्सोनॉमी (taxonomies)

Infrastructure deployment, applied environment controls तथा अन्य सर्वोत्तम उपायों से संबंधित व्यापक जानकारी, परिदृश्यों की रणनीतियों के लिए इस खंड का संदर्भ लें ।

- [AML.T0048.002 - Societal Harm](https://atlas.mitre.org/techniques/AML.T0048) **MITRE ATLAS**
