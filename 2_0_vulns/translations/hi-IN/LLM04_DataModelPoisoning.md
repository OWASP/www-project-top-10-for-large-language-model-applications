## LLM04: Data and Model Poisoning

### विवरण

डेटा विषाक्तता तब होती हैं जब पूर्व-प्रशिक्षण, fine-tuning या एम्बेडिंग डेटा को vulnerabilities, बैकडोर या बायसेस को पेश करने के लिए हेरफेर किया जाता हैं। यह हेरफेर मॉडल सुरक्षा, प्रदर्शन या नैतिक व्यवहार से compromise कर सकता हैं, जिससे हानिकारक आउटपुट या बिगड़ा हुआ क्षमताएं हो सकती हैंं। सामान्य जोखिमों में अपमानित मॉडल प्रदर्शन, पक्षपाती या विषाक्त सामग्री, और डाउनस्ट्रीम सिस्टम का exploit शामिल हैं।

डेटा विषाक्तता LLM जीवनचक्र के विभिन्न चरणों को लक्षित कर सकती हैं, जिसमें प्री-ट्रेनिंग (सामान्य डेटा से सीखना), fine-tuning (विशिष्ट कार्यों के लिए मॉडल को अनुकूलित करना), एम्बेडिंग (texts को संख्यात्मक वैक्टर में परिवर्तित करना), और एक पूर्व-पुन: उपयोग करना शामिल हैं ( एक नए कार्य पर प्रशिक्षित मॉडल)। इन चरणों को समझने से यह पहचानने में मदद मिलती हैं कि vulnerabilities कहां से उत्पन्न हो सकती हैंं। डेटा विषाक्तता को एक अखंडता हमला माना जाता हैं क्योंकि प्रशिक्षण डेटा के साथ छेड़छाड़ करना सटीक भविष्यवाणियां करने के लिए मॉडल की क्षमता को प्रभावित करता हैं। जोखिम बाहरी डेटा स्रोतों के साथ विशेष रूप से उच्च हैंं, जिसमें असुविधाजनक या दुर्भावनापूर्ण सामग्री हो सकती हैं।

इसके अलावा, साझा repository या open-source प्लेटफॉर्म के माध्यम से वितरित किए गए मॉडल डेटा विषाक्तता से परे जोखिम ले सकते हैंं, जैसे कि मैलवेयर दुर्भावनापूर्ण अचार जैसी तकनीकों के माध्यम से एम्बेडेड, जो कि मॉडल लोड होने पर हानिकारक कोड को निष्पादित कर सकता हैं। इसके अलावा, विचार करें कि विषाक्तता एक पिछले दरवाजे के कार्यान्वयन के लिए अनुमति दे सकती हैं। इस तरह के बैकडोर मॉडल के व्यवहार को तब तक छोड़ सकते हैंं जब तक कि एक निश्चित ट्रिगर इसे बदलने का कारण नहीं बन जाता। यह इस तरह के परिवर्तनों को परीक्षण करने और पता लगाने के लिए कठिन बना सकता हैं, वास्तव में एक मॉडल के लिए एक स्लीपर एजेंट बनने का अवसर पैदा करता हैं।

### Vulnerability के सामान्य उदाहरण

1.  दुर्भावनापूर्ण व्यक्ति प्रशिक्षण के दौरान हानिकारक डेटा पेश करते हैंं, जिससे पक्षपाती आउटपुट होता हैं। इसे प्राप्त करने के लिए "स्प्लिट-व्यू डेटा पॉइज़निंग" या "मोर्चिंग पॉइज़निंग" जैसे तकनीक "मोर्चिंग पॉइज़निंग" exploit मॉडल प्रशिक्षण गतिशीलता जैसी तकनीकें।
  (Ref. link: [Split-View Data Poisoning](https://github.com/GangGreenTemperTatum/speaking/blob/main/dc604/hacker-summer-camp-23/Ads%20_%20Poisoning%20Web%20Training%20Datasets%20_%20Flow%20Diagram%20-%20Exploit%201%20Split-View%20Data%20Poisoning.jpeg))
  (Ref. link: [Frontrunning Poisoning](https://github.com/GangGreenTemperTatum/speaking/blob/main/dc604/hacker-summer-camp-23/Ads%20_%20Poisoning%20Web%20Training%20Datasets%20_%20Flow%20Diagram%20-%20Exploit%202%20Frontrunning%20Data%20Poisoning.jpeg))
2.  हमलावरों ने हानिकारक सामग्री को सीधे प्रशिक्षण प्रक्रिया में इंजेक्ट कर सकते हैंं, मॉडल की आउटपुट गुणवत्ता से compromise कर सकते हैंं।
3.  user अनजाने में बातचीत के दौरान संवेदनशील या proprietary जानकारी को इंजेक्ट करते हैंं, जिसे बाद के आउटपुट में उजागर किया जा सकता हैं।
4.  अस्वीकृत प्रशिक्षण डेटा पक्षपाती या गलत आउटपुट के जोखिम को बढ़ाता हैं।
5.  संसाधन पहुंच प्रतिबंधों की कमी असुरक्षित डेटा के अंतर्ग्रहण की अनुमति दे सकती हैं, जिसके परिणामस्वरूप पक्षपाती आउटपुट होता हैं।

### रोकथाम एवं बचाव के लिये रणनीतियाँ

1. TRACK डेटा ओरिजिन और ट्रांसफॉर्मेशन जैसे OWASP Cyclonedx या ML-BOM और लीवरेज टूल जैसे टूल का उपयोग करके [Dyana] (https://github.com/dreadnode/dyana) तृतीय-भाग software का डायनेमिक विश्लेषण करने के लिए। सभी मॉडल विकास चरणों के दौरान डेटा वैधता को सत्यापित करें।
2. वीईटी डेटा विक्रेताओं को कठोरता से, और जहर के prompts का पता लगाने के लिए विश्वसनीय स्रोतों के खिलाफ मॉडल आउटपुट को मान्य करें।
3. अस्वीकृत डेटा स्रोतों के लिए मॉडल एक्सपोज़र को सीमित करने के लिए सख्त सैंडबॉक्सिंग को लागू करें। प्रतिकूल डेटा को फ़िल्टर करने के लिए विसंगति का पता लगाने की तकनीक का उपयोग करें. 
4. ठीक-ट्यूनिंग के लिए विशिष्ट डेटासेट का उपयोग करके विभिन्न उपयोग के मामलों के लिए दर्जी मॉडल। यह परिभाषित लक्ष्यों के आधार पर अधिक सटीक आउटपुट का उत्पादन करने में मदद करता हैं।
5. मॉडल को अनपेक्षित डेटा स्रोतों तक पहुंचने से रोकने के लिए पर्याप्त बुनियादी ढांचा नियंत्रण सुनिश्चित करें।
6. डेटासेट में परिवर्तन को ट्रैक करने और हेरफेर का पता लगाने के लिए डेटा संस्करण नियंत्रण (DVC) का उपयोग करें। मॉडल अखंडता बनाए रखने के लिए संस्करण महत्वपूर्ण हैं।
7. एक वेक्टर डेटाबेस में user द्वारा आपूर्ति की गई जानकारी को संग्रहीत करें, पूरे मॉडल को फिर से प्रशिक्षण के बिना समायोजन की अनुमति दें।
8. रेड टीम अभियानों और प्रतिकूल तकनीकों जैसे कि फेडरेटेड लर्निंग के साथ परीक्षण मॉडल की मजबूती, डेटा गड़बड़ी के प्रभाव को कम करने के लिए।
9. प्रशिक्षण हानि की निगरानी करें और विषाक्तता के prompts के लिए मॉडल व्यवहार का विश्लेषण करें। विसंगतिपूर्ण आउटपुट का पता लगाने के लिए थ्रेसहोल्ड का उपयोग करें।
10. अनुमान के दौरान, मतिभ्रम के जोखिम को कम करने के लिए Retrieval-Augmented Generation (RAG) और ग्राउंडिंग तकनीकों को एकीकृत करें।

### उदाहरण स्वरूप हमले के परिदृश्य

#### परिद्रश्य 1
  एक हमलावर प्रशिक्षण डेटा में हेरफेर करके या Prompt इंजेक्शन तकनीकों का उपयोग करके, गलत सूचना फैलाने के द्वारा मॉडल के आउटपुट को पक्षपात करता हैं।
#### परिदृश्य#2
  उचित फ़िल्टरिंग के बिना विषाक्त डेटा खतरनाक जानकारी का प्रचार करते हुए हानिकारक या पक्षपाती आउटपुट को जन्म दे सकता हैं।
#### परिदृश्य#3
  एक दुर्भावनापूर्ण व्यक्ति या प्रतियोगी प्रशिक्षण के लिए गलत दस्तावेज बनाता हैं, जिसके परिणामस्वरूप मॉडल आउटपुट होता हैं जो इन अशुद्धियों को दर्शाता हैं।
#### परिदृश्य#4
  अपर्याप्त फ़िल्टरिंग एक हमलावर को Prompt इंजेक्शन के माध्यम से भ्रामक डेटा डालने की अनुमति देता हैं, जिससे compromise आउटपुट होता हैं।
#### परिदृश्य#5
  एक हमलावर मॉडल में एक बैकडोर ट्रिगर डालने के लिए विषाक्तता तकनीकों का उपयोग करता हैं। यह आपको प्रमाणीकरण बाईपास, डेटा एक्सफिल्ट्रेशन या हिडन कमांड निष्पादन के लिए खुला छोड़ सकता हैं।

### संबंधित लिंक

1. [How data poisoning attacks corrupt machine learning models](https://www.csoonline.com/article/3613932/how-data-poisoning-attacks-corrupt-machine-learning-models.html): **CSO Online**
2. [MITRE ATLAS (framework) Tay Poisoning](https://atlas.mitre.org/studies/AML.CS0009/): **MITRE ATLAS**
3. [PoisonGPT: How we hid a lobotomized LLM on Hugging Face to spread fake news](https://blog.mithrilsecurity.io/poisongpt-how-we-hid-a-lobotomized-llm-on-hugging-face-to-spread-fake-news/): **Mithril Security**
4. [Poisoning Language Models During Instruction](https://arxiv.org/abs/2305.00944): **Arxiv White Paper 2305.00944**
5. [Poisoning Web-Scale Training Datasets - Nicholas Carlini | Stanford MLSys #75](https://www.youtube.com/watch?v=h9jf1ikcGyk): **Stanford MLSys Seminars YouTube Video**
6. [ML Model Repositories: The Next Big Supply Chain Attack Target](https://www.darkreading.com/cloud-security/ml-model-repositories-next-big-supply-chain-attack-target) **OffSecML**
7. [Data Scientists Targeted by Malicious Hugging Face ML Models with Silent Backdoor](https://jfrog.com/blog/data-scientists-targeted-by-malicious-hugging-face-ml-models-with-silent-backdoor/) **JFrog**
8. [Backdoor Attacks on Language Models](https://towardsdatascience.com/backdoor-attacks-on-language-models-can-we-trust-our-models-weights-73108f9dcb1f): **Towards Data Science**
9. [Never a dill moment: Exploiting machine learning pickle files](https://blog.trailofbits.com/2021/03/15/never-a-dill-moment-exploiting-machine-learning-pickle-files/) **TrailofBits**
10. [arXiv:2401.05566 Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training](https://www.anthropic.com/news/sleeper-agents-training-deceptive-llms-that-persist-through-safety-training) **Anthropic (arXiv)**
11. [Backdoor Attacks on AI Models](https://www.cobalt.io/blog/backdoor-attacks-on-ai-models) **Cobalt**

### संबंधित फ्रेमवर्क और टैक्सोनॉमी

Refer to this section for comprehensive information, scenarios strategies relating to infrastructure deployment, applied environment controls and other best practices.
बुनियादी ढांचे की deployment, लागू पर्यावरण नियंत्रण और अन्य सर्वोत्तम प्रथाओं से संबंधित व्यापक जानकारी, परिदृश्यों की रणनीतियों के लिए इस खंड का संदर्भ लें।

- [AML.T0018 | Backdoor ML Model](https://atlas.mitre.org/techniques/AML.T0018) **MITRE ATLAS**
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework): Strategies for ensuring AI integrity. **NIST**
- [ML07:2023 Transfer Learning Attack](https://owasp.org/www-project-machine-learning-security-top-10/docs/ML07_2023-Transfer_Learning_Attack) **OWASP Machine Learning Security Top Ten**
