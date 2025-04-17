## LLM04: डेटा एवं मॉडल Poisoning

### विवरण

डेटा poisoning तब होती हैं जब pre-training (पूर्व-प्रशिक्षण), fine-tuning या embedding data में vulnerabilities, backdoors या biases डालने के  लिए हेरफेर की जाती हैं । यह हेरफेर मॉडल की सुरक्षा (security), प्रदर्शन (performance) एवं नैतिक व्यवहार (ethical behavior) को compromise कर सकती हैं, जिससे हानिकारक आउटपुट या बिगड़ी हुआ capabilities (क्षमताएं) पैदा हो सकती हैंं । सामान्य जोखिमों में मॉडल की degraded performance (गिरता प्रदर्शन), biased तथा toxic content, एवं downstream systems का exploitation शामिल हैं ।

डेटा poisoning LLM जीवनचक्र के  विभिन्न चरणों को लक्षित कर साकता हैं, जिसमें pre-training (सामान्य डेटा से सीखना), fine-tuning (विशिष्ट कार्यों के  लिए मॉडल को अनुकूल बनाना), embedding (texts को संख्यात्मक वैक्टर में परिवर्तित करना), एवं transfer learning (नए कार्यों पर प्रशिक्षित मॉडल को बार-बार प्रयोग में लेना) शामिल हैं । इन चरणों को समझने से यह पहचानने में मदद मिलती हैं कि vulnerabilities कहाँं से उत्पन्न हो सकती हैंं । डेटा poisoning को एक integrity (अखंडता) हमला माना जाता हैं, क्योंकि प्रशिक्षण डेटा से छेड़छाड़ करने से सटीक पूर्वानुमान लगाने वाली मॉडल की क्षमता प्रभावित होती हैं । बाहरी डेटा स्रोतों से जोखिम अधिक होता हैंं, क्योंकि उनमें unverified या दुर्भावनापूर्ण सामग्री हो सकती हैं ।

इसके  अलावा, shared repository या open-source platforms से वितरित किए गए मॉडल डेटा poisoning से अधिक बड़े जोखिम पैदा कर सकते हैंं, जैसें कि malicious pickling जैसी तकनीकों से malware डालना (embed), जो कि मॉडल के  लोड होने पर उसमें हानिकारक code execute कर सकता हैं । इसके  तरह poisoning, backdoor के  implementation को भी अनुमति दे सकती हैं । इस तरह के  backdoors मॉडल के  व्यवहार में तब तक कुछ नहीं करतें, जब तक कि एक निश्चित trigger संकेत नहीं देता या 
hit नहीं होता । यह इस तरह के  परिवर्तनों के  लिये परीक्षण एवं पता लगाने की क्षमता को कठिन बना सकता हैं, जो की मॉडल को sleeper agent बना देता हैं ।

### Vulnerability के सामान्य उदाहरण

1. दुर्भावनापूर्ण व्यक्ति प्रशिक्षण के  दौरान हानिकारक डेटा डालते हैंं, जिससे पक्षपाती आउटपुट आता हैं । इसके  लिए "Split-View Data Poisoning" या "Frontrunning Poisoning" जैसें तकनीकें  के  प्रयोग से मॉडल के  प्रशिक्षण चक्र को exploit (फायदा उठाना) किया जाता हैंं ।
  संदर्भित link: [Split-View Data Poisoning](https://github.com/GangGreenTemperTatum/speaking/blob/main/dc604/hacker-summer-camp-23/Ads%20_%20Poisoning%20Web%20Training%20Datasets%20_%20Flow%20Diagram%20-%20Exploit%201%20Split-View%20Data%20Poisoning.jpeg)
  संदर्भित link: [Frontrunning Poisoning](https://github.com/GangGreenTemperTatum/speaking/blob/main/dc604/hacker-summer-camp-23/Ads%20_%20Poisoning%20Web%20Training%20Datasets%20_%20Flow%20Diagram%20-%20Exploit%202%20Frontrunning%20Data%20Poisoning.jpeg)
2. हमलावरों द्वारा हानिकारक सामग्री को सीधे प्रशिक्षण प्रक्रिया में inject (डालना) करके  मॉडल की आउटपुट गुणवत्ता से compromise किया जा सकता हैंं ।
3. User अनजाने में ही उपयोग के  दौरान संवेदनशील या proprietary जानकारी को दे देता हैंं, जो की बादमे आउटपुट में उजागर हो सकती हैं ।
4. Unverified (अस्वीकृत) प्रशिक्षण डेटा पक्षपाती या गलत आउटपुट के  जोखिम को बढ़ा सकता हैं ।
5. संसाधन तक पहूँच के  प्रतिबंधों (resource access restrictions) की कमी के  कारण असुरक्षित डेटा को ग्रहण की अनुमति मिल सकती हैं, जिसके  परिणामस्वरूप पक्षपाती आउटपुट आ सकतें हैं ।

### रोकथाम एवं बचाव के लिये रणनीतियाँ

1. डेटा की उत्पत्ति एवं परिवरतानों पर OWASP Cyclonedx या ML-BOM जेसे tools का प्रयोग कर नज़र राखें, एवं इसके  साथ tools जैसें की   Dyana का भी फ़ायदा उठा साकते हैंं, जिससे की third-party software का dynamic विश्लेषण कर सकते हैंं । मॉडल के  सभी development चरणों के  दौरान डेटा वैधता (legitimacy) को सत्यापित (Verify) करें ।
   संदर्भित link: [Dyana](https://github.com/dreadnode/dyana)
3. डेटा विक्रेताओं का कठोरता से मूल्यांकन करें, एवं poisoning का पता लगाने के  लिए विश्वसनीय स्रोतों से मॉडल आउटपुट का मिलन करें ।
4. मॉडल पर सख्त sandboxing लगाएँ, ताकी वह अस्वीकृत डेटा स्रोतों की पहुँच से दूर रहें । प्रतिकूल (adversarial) डेटा को फ़िल्टर करने के  लिए anomaly detection की तकनीक का उपयोग करें ।
5. विशिष्ट डेटासेट के  प्रयोग से Fine-tuning करके  मॉडल को खास कार्यक्षमताओें के  लिए तैयार करें । यह खास लक्ष्यों के  लिये अधिक सटीक आउटपुट पाने में मदद करता हैं ।
6. मॉडल को unintended डेटा स्रोतों तक पहुँंचने से रोकने के  लिए पर्याप्त infrastructure सुनिश्चित करें ।
7. डेटासेट में परिवर्तन पर नज़र रखने एवं हेरफेर का पता लगाने के  लिए data version control (DVC) का उपयोग करें । मॉडल अखंडता बनाएँ रखने के  लिए versioning बहुत महत्वपूर्ण हैं ।
8. Vector database में user द्वारा दी गई जानकारीयों को संग्रहीत करें, जिससे की पूरे मॉडल को फिर से प्रशिक्षण किए बिना ही उसमें सुधार लिए जा सकेंगे ।
9. Red team campaigns एवं adversarial तकनीकों के  साथ मॉडल की मजबूती (robustness) का प्रशिक्षण करें, जैसें कि federated learning से डेटा में अव्यवस्थाएँ (perturbations) कम कि जा सकती हैंं ।
10. प्रशिक्षण के  दौरान ही हानियों के  लिए निगरानी करें एवं poisoning की पहचान के  लिए मॉडल के  व्यवहार का विश्लेषण करें । विसंगतिपूर्ण (anomalous) आउटपुट का पता लगाने के  लिए thresholds का उपयोग करें ।
11. परामर्श पाने के  दौरान hallucinations के  जोखिम को कम करने के  लिए Retrieval-Augmented Generation (RAG) एवं grounding तकनीकों को प्रयोग करें ।

### उदाहरण स्वरूप हमलें के परिदृश्य

#### परिद्रश्य 1
  एक हमलावर (malicious attacker) प्रशिक्षण डेटा में हेरफेर या Prompt इंजेक्शन तकनीकों का उपयोग करके, गलत सूचना फैलाने के  लिये मॉडल के  आउटपुट में पूर्वाग्रहों पैदा करता हैं ।
#### परिदृश्य#2
  उचित फ़िल्टरिंग के  बिना विषाक्त डेटा हानिकारक या पक्षपाती आउटपुट को जन्म दे सकता हैं, जिससे की खतरनाक जानकारीयों का प्रचार हो सकता हैंं ।
#### परिदृश्य#3
  एक दुर्भावनापूर्ण व्यक्ति या प्रतिद्वंद्वी प्रशिक्षण डाटा के  लिये गलत दस्तावेज बनाता हैं, जिससे की मॉडल आउटपुट में यह अशुद्धियां झलकती हैं ।
#### परिदृश्य#4
  अपर्याप्त फ़िल्टरिंग के  कारण एक हमलावर (malicious attacker), Prompt इंजेक्शन से भ्रामक डेटा डाल सकता हैं, जिससे की आउटपुट compromise हो जातें हैं ।
#### परिदृश्य#5
  एक हमलावर (malicious attacker) poisoning तकनीकों के  प्रयोग से मॉडल में एक backdoors trigger डालता हैं । यह आपको authentication bypass, data exfiltration या hidden command execution करने को बाध्य कर सकता हैंं ।

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

### संबंधित फ्रेमवर्क (frameworks) एवं टैक्सोनॉमी (taxonomies)

Infrastructure deployment, applied environment controls तथा अन्य सर्वोत्तम उपायों से संबंधित व्यापक जानकारी, परिदृश्यों की रणनीतियों के  लिए इस खंड का संदर्भ लें ।

- [AML.T0018 | Backdoor ML Model](https://atlas.mitre.org/techniques/AML.T0018) **MITRE ATLAS**
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework): Strategies for ensuring AI integrity. **NIST**
- [ML07:2023 Transfer Learning Attack](https://owasp.org/www-project-machine-learning-security-top-10/docs/ML07_2023-Transfer_Learning_Attack) **OWASP Machine Learning Security Top Ten**
