## LLM03:2025 Supply Chain

### विवरण

LLM supply chains विभिन्न vulnerabilities के  लिए अतिसंवेदनशील होती हैं, जिससे प्रशिक्षण डेटा, मॉडल और deployment platforms की अखंडता (integrity) प्रभावित होती हैं । इन जोखिमों के  परिणामस्वरूप पक्षपाती आउटपुट (biased outputs), security breaches तथा system failures हो सकते हैंं । जबकि पारंपरिक software vulnerabilities code flaws एवं dependencies जैसें मुद्दों पर ध्यान केंद्रित करती हैंं, जबकि ML में जोखिम भी third-party के  pre-trained मॉडल और डेटा तक जातें हैंं ।

इन बाहरी तत्वों में tampering एवं poisoning attacks के  माध्यम से हेरफेर कि जा सकती हैं ।

LLM बनाना एक विशिष्टता (specialized) वाला कार्य हैं, जो अक्सर third-party के  मॉडल पर निर्भर करता हैं । Open-access LLM और "LoRA" (Low-Rank Adaptation) तथा "PEFT" (Parameter-Efficient Fine-Tuning) जैसें नए fine-tuning विधियों का उदय, Hugging Face जैसें platforms पर, नए supply-chain जोखिमों को पेश करता हैं । अंत में, on-device LLM के  उद्गम ने LLM applications के  लिए हमलें की संभावनए एवं supply-chain जोखिमों को बढ़ाया हैंं ।

यहाँं चर्चा किए गए कुछ जोखिमों पर "LLM04 Data and Model Poisoning" में भी चर्चा की गई हैं । यह बिन्दु जोखिमों के  supply-chain से जुड़े पहलुओें पर केंद्रित हैं । एक साधारण threat model समझा जा सकता हैं ।
[here](https://github.com/jsotiro/ThreatModels/blob/main/LLM%20Threats-LLM%20Supply%20Chain.png).

### जोखिमों के सामान्य उदाहरण

#### 1. Third-party Package से जुड़ी पारंपरिक vulnerabilities
  जैसें कि outdated या deprecated components, जिनका हमलावर (malicious attacker) LLM applications को compromise करने के  प्रयोग करता हैंं । यह "A06:2021 – Vulnerable and Outdated Components" के  जैसा हैं जब components का उपयोग मॉडल विकास या finetuning के  दौरान होने से जोखिमों बड़ जाता हैं ।  
  संदर्भ link: [A06:2021 – Vulnerable and Outdated Components](https://owasp.org/Top10/A06_2021-Vulnerable_and_Outdated_Components/)
#### 2. Licensing से जुड़े जोखिम
  AI के  विकास में अक्सर विविध प्रकार के  software और डेटासेट licenses शामिल होते हैंं, जो ठीक से संभले नहीं जाने पर जोखिम पैदा कर सकते हैंं । विभिन्न open-source एवं proprietary licenses अलग-अलग कानूनी आवश्यकताओं के  साथ आते हैंं । डेटासेट licenses उपयोग (usage), वितरण (distribution) तया व्यावसायीकरण (commercialization) को प्रतिबंधित कर सकते हैंं ।
#### 3. Outdated या Deprecated मॉडल
  Outdated या Deprecated मॉडल का उपयोग करना जो अब maintained नहीं हैं, सुरक्षा का गहन मुद्दा हैं । 
#### 4. Vulnerable pre-trained मॉडल
  मॉडल binary black boxes हैंं जिसमें open source के  विपरीत static निरीक्षण से सुरक्षा के  प्रती बहुत कम योगदान किया जा सकता हैं । Vulnerable pre-trained मॉडल में छिपे हुँए पूर्वाग्रह (biases), backdoors या अन्य दुर्भावनापूर्ण features हो सकते हैंं, जिन्हें मॉडल repository के  सुरक्षा मूल्यांकन के  माध्यम से पहचाना नहीं जा पाया हैं । Vulnerable मॉडल को दोनों poisoned डेटासेट एवं सीधा मॉडल से छेड़छाड़ के  द्वारा बनाया जा सकता हैं, जैसें की ROME जिसे lobotomisation भी कहते हैंं उसका उपयोग करके  ।
#### 5. मॉडल के कमजोर सिद्धता
  वर्तमान में प्रकाशित मॉडलों में कोई मजबूत आश्वासन नहीं हैंं । मॉडल के  cards एवं इससे संबंधित दस्तावेज मॉडल की जानकारी तो प्रदान करतें हैंं, पर वह users पर निर्भर होते हैंं, लेकिन वह मॉडल के  स्रोत (origin) पर कोई गारंटी नहीं देतें । एक हमलावर (malicious attacker) मॉडल repo के  supplier के  खाते को compromise कर सकता हैं, या एक उसके  समान लगने वाला खाता बनाकर उसे social engineering तकनीकों से जोड़ कर, LLM application की supply-chain को compromise कर सकता हैं ।
#### 6. Vulnerable LoRA adapters
  LoRA एक लोकप्रिय fine-tuning तकनीक हैं, जो pre-trained परतों को मौजूदा LLM पर जोड़कर modularity को बढ़ाती हैं । यह विधि दक्षता (efficiency) तो बढ़ाती ही हैं लेकिन नए जोखिमों को भी पैदा करती हैं, जहाँं एक दुर्भावनापूर्ण LoRA adapter pre-trained बेस मॉडल की अखंडता एवं सुरक्षा से compromise करता हैं । यह collaborative एवं model merge environments दोनों में हो सकता हैं, लेकिन vLMM एवं OpenLLM जैसें लोकप्रिय inference deployment platforms द्वारा भी LoRA के  support को exploit (फायदा उठाना) किया जा सकता हैं, जहाँं adapters को डाउनलोड करके  deployed मॉडल पर लागू किया जा सकता हैं ।
#### 7. Collaborative Development Processes को exploit (फायदा उठाना) करें
  Shared environments में होस्ट किए गए Collaborative model merge एवं model handling services (जैसे conversions) को, shared मॉडल्स में vulnerabilities को पैदा करने के  लिए exploit (फायदा उठाना) किया जा सकता हैं । Hugging Face पर model merging बहुत लोकप्रिय होने के  साथ-साथ, इसके  मॉडल्स OpenLLM लीडरबोर्ड में भी टॉप पर है, जिसके  साथ-साथ इनको review को bypass करने के  लिए भी exploit (फायदा उठाना) किया जा सकता हैं । इसी तरह ही services (सेवाओं) जेसे conversation bot भी हेरफेर एवं दुर्भावनापूर्ण code  के  प्रती vulnerable होते हैंं ।
#### 8. Devices की supply-chain vulnerabilities पर LLM मॉडल
  Devices पर LLM मॉडल लगाने से supply पर हमलों की संभावनाए बड़ती हैंं, इसके  साथ यह निर्माण की प्रक्रियाओं (manufactured processes) को compromise एवं device OS या fimware vulnerabilities को भी exploit (फायदा उठाना) कर सकता हैंं । इससें हमलावर (malicious attacker) छेड़छाड़ (tampered) किए गए मॉडल्स को reverse engineer एवं applications को re-package कर सकता हैंं ।
#### 9. अस्पष्ट T&Cs (नियम व शर्तें) एवं डेटा के लिए गोपनीयता की नीतियां (Privacy Policies)
  मॉडल ऑपरेटरों (operators) की अस्पष्ट T&Cs (नियम व शर्तें) एवं डेटा की गोपनीयता नीतियां के  कारण, application के  संवेदनशील डेटा का उपयोग मॉडल प्रशिक्षण एवं इसके  साथ संवेदनशील जानकारी के  exposure के  लिए भी हो सकता हैंं । यह मॉडल के  supplier द्वारा copyrighted सामग्री के  उपयोग करने से उतन्न होने वाले जोखिमों पर भी लागू होता हैं ।

### रोकथाम एवं बचाव के लिये रणनीतियाँ

1. डेटा स्रोतों एवं suppliers की vetting (स्पष्ट तौर पर जांच एवं पड़ताल) करें, जिसमें T&Cs (नियम व शर्तें) एवं उनकी गोपनीयता नीतियों भी शामिल हो,इसके  लिये केवल विश्वसनीय suppliers का ही उपयोग करें । नियमित रूप से suppliers की सुरक्षा (Security) तथा पहूँच (acces) की समीक्षा एवं ऑडिट करें,यह सुनिश्चित करतें हुँए की इनसे सुरक्षा या T&Cs (नियम व शर्तें) में कोई बदलाव तो नहीं हो रहा ।
2. OWASP टॉप 10 के  "A06:2021 – Vulnerable and Outdated Components" में दिए गए समाधानों को समझें एवं लागू करें । इसमेंं Vulnerability की खोज (scanning), प्रबंधन (management) एवं component पर सुधार लागू करना (patching) शामिल हैंं । संवेदनशील डेटा तक पहूँच (access) के  साथ development environments के  लिए, इन नियंत्रणों को उन सभी वातावरणों में भी लागू करें ।
  संदर्भित link: [A06:2021 – Vulnerable and Outdated Components](https://owasp.org/Top10/A06_2021-Vulnerable_and_Outdated_Components/)
4. Third-party मॉडल के  चयन से पूर्व व्यापक AI Red Teaming एवं मूल्यांकन (evaluations) करें । Decoding Trust एक उदाहरण हैं LLMs के  एक भरोसेमंद AI बेंचमार्क का, लेकिन मॉडल्स इस प्रकार से finetune किया जा सकता हे की वह प्रकाशित बेंचमार्क को भी bypass कर दे । मॉडल का मूल्यांकन करने के  लिए व्यापक AI Red Teaming का प्रयोग करें, विशेष रूप से मॉडल के  उपयोगों (use cases) की योजना के  लिये ।
5. Software Bill of Materials (SBOM) का प्रयोग से up-to-date, सटीक एवं signed (सत्यापित) inventory बनाएँ, जो कि deployed packages के  साथ छेड़छाड़ को रोकने के  लिए सहायक हो सकें । SBOMs का प्रयोग नई, zero-date vulnerabilities को जल्दी से पता (detect) लगानें एवं सतर्क (alert) करने के  लिए किया जा सकता हैं । AI BOMs एवं ML SBOMs एक उभरता हुआ क्षेत्र हैं, इसके  लिये आपको OWASP Cyclonedx से शुरुवात करतें हुँए अन्य विकल्पों का मूल्यांकन करना चहिए ।
6. AI Licensing जोखिमों को कम करने के  लिए, BOM का प्रयोग करतें हुँए, सभी प्रकार के  licenses की एक सूची बनाएँँ । इसी से ही compliance (स्वीकृति) एवं transparency (पारदर्शिता) सुनिश्चित करतें हुँए, सभी software, tools तथा डेटासेट को नियमित रूप से audit करतें रहें । Real-time निगरानी के  लिए स्वचालित (automated) licenses प्रबंधन tools का उपयोग करें एवं Licensing मॉडल पर टीमों को प्रशिक्षित (train) करें । BOMs और leverage tools जैसें की Dyana के  विस्तृत licensing documentation बनाएँ, ताकी third-party software का dynamic विश्लेषण किया जा सकें ।
  संदर्भित link: [Dyana](https://github.com/dreadnode/dyana)
8. केवल सत्यापित (verifiable) स्रोतों के  मॉडल्स का ही प्रयोग करें एवं मजबूत मॉडल सिद्धता (provenance) की कमी की क्षतिपूर्ति हेतु signing एवं file hashes के  साथ third-party मॉडल्स की अखंडता की जाँच करें । इसी तरह, बाहर से प्राप्त code के  लिये code signing का उपयोग करें ।
9. किसी भी दुरुपयोग का जल्द से जल्द पता लगाने एवं रोकने के  लिए collaborative model के  development environment में सख्त निगरानी एवं auditing को लागू करें । "HuggingFace SF_Convertbot Scanner" इसी कार्य के  लिए प्रयोग में आने वाली एक automated (स्वचालित) scripts का उदाहरण हैं ।
  संदर्भित link: [HuggingFace SF_Convertbot Scanner](https://gist.github.com/rossja/d84a93e5c6b8dd2d4a538aa010b29163)
10. दिए गए मॉडल एवं डेटा, पर anomaly detection एवं adversarial robustness (प्रतिकूलता की मजबूती का परीक्षण करना) लगाने से, छेड़छाड़ (tampering) एवं विषाक्तता (poisoning) का में पता लगाने में मदद मिल साकती हैं जैसा कि "LLM04 Data and Model Poisoning" में चर्चा की गई हैं । आदर्श रूप से, यह MLOps एवं LLM pipelines का हिस्सा होना चाहिए, लेकिन उभरती हुई तकनीक होने के  कारण यह Red Teaming के  हिस्से के  रूप में लागू करना आसान हैं ।
11. Vulnerable या Outdated components को कम करने के  लिए एक patching (सुधारणा) नीति लागू करें । सुनिश्चित करें कि application, maintained version वाली API एवं अंतर्निहित मॉडल पर निर्भर करें ।
12. जो Encrypt मॉडल, AI edge में deployed किए गए है, integrity checks (अखंडता की जांच करना) के  साथ vendor attestation (like verified and secured) APIs का प्रयोग करें, जिससे की apps एवं models को tampered होने से बचाया जा सकें । इसी के  साथ अमान्यताप्राप्त firmware वाली applications को बंद करें (terminate) ।

### उदाहरण स्वरूप हमलें के परिदृश्य

#### परिदृश्य#1: Vulnerable Python Library
  एक हमलावर (malicious attacker) LLM app को compromise करने के  लिए एक vulnerable Python Library को exploit (फायदा उठाना) करता हैं । यह सबसे पहले OpenAI data breach में देखा गया था । PyPi Package registry पर हमलों से मॉडल developers को model development environment में malware वाली Pytorch dependency download करा दी । इसका एक अधिक पेचींदा उदाहरण हैं AI infrastructure का प्रबंधन करने के  लिए कई विक्रेताओं द्वारा उपयोग किए जाने वाले Ray AI framework पर Shadow Ray attack । माना जाता हैं इस हमलें में पांच vulnerabilities हैं जो कई servers को प्रभावित करती हैं ।
#### परिदृश्य#2: प्रत्यक्ष छेड़छाड़ (Direct Tampering)
  गलत सूचना फैलाने के  लिए एक मॉडल को प्रकाशित एवं उससे छेड़छाड़ करना । यह PoisonGPT (मॉडल parameters मे बदलाव करके) द्वारा HuggingFace के  सुरक्षा features को bypass करने वाला वास्तविक हमला हैं ।
#### परिदृश्य#3: लोकप्रिय मॉडल की finetuning 
  एक हमलावर (malicious attacker) प्रमुख सुरक्षा feature को हटाने एवं एक विशिष्ट domain (बीमा) में उच्च प्रदर्शन करने के  लिए एक लोकप्रिय open access मॉडल को finetune करता हैं । मॉडल सुरक्षा benchmarks पर अत्यधिक स्कोर करने के  लिए finetuned हैं, लेकिन बहुत लक्षित triggers के  साथ । वे इसे victims के  लिए HuggingFace पर deploy करतें हैंं, जो benchmarks पर भरोसे को exploit करने के  लिये इसका प्रयोग कर सकते हैंं ।
#### परिदृश्य#4: Pre-trained मॉडल
  एक LLM सिस्टम ढंग से सत्यापन के  बिना ही एक ज्यादा प्रयोग में ली जाने वाली repository से pre-trained मॉडल को deploy करतें हैं । एक compromised मॉडल दुर्भावनापूर्ण code  को उसमें डाल देता हैं, जिससे कुछ संदर्भों में पक्षपाती आउटपुट आते हैं एवं हानिकारक या हेरफेर किए हुँए परिणाम देखने को मिलते हैं ।
#### परिदृश्य#5: compromised हुआ third-party supplier
  एक compromised हुआ third-party supplier एक Vulnerable LoRA adapter को HuggingFace के  model merge का प्रयोग करतें हुँए LLM में merge कर देता हैं ।
#### परिदृश्य#6: supplier द्वारा घुसपैठ
  एक हमलावर (malicious attacker) third-party supplier में घुसपैठ हैं, ताकि वह vLLM तथा openLLM जैसें फ्रेमवर्क से deploy किए गए on-device LLM के  साथ integrate होने वाले LoRA (Low-Rank Adaptation) adapter के  उत्पादन को compromise कर सकें । इसमेंं compromise हुँए LoRA adapter में ध्यानपूर्वक बदलाव किए जातें हैं, जिससे उसमें छिपी हुई vulnerabilities एवं दुर्भावनापूर्ण code  को शामिल किया जा सकें । एक बार जब इस adapter को LLM से merged कर दिया जाता हैं, तो यह हमलावर (malicious attacker) को सिस्टम में एक covert entry point (गुप्त प्रवेश बिंदु) प्रदान करता हैं । यह दुर्भावनापूर्ण code  मॉडल संचालन के  दौरान सक्रिय हो सकता हैं, जिससे हमलावर (malicious attacker) LLM के  आउटपुट में हेरफेर कर सकता हैं ।
#### परिदृश्य#7: CloudBorne एवं CloudJacking हमले
  ये हमलें cloud के  infrastructure को लक्षित करतें हुँए, उसमें मौजूद virtualization परतों के  संसाधनों एवं vulnerabilities का लाभ उठाते हैंं । CloudBorne के  अंतर्गत साझा cloud environments में firmware vulnerabilities का exploit करना शामिल हैं, जो की physical servers द्वारा hosted virtual instance को compromise करतें हैं । CloudJacking के  अंतर्गत दुर्भावनापूर्ण नियंत्रण तथा cloud instances का दुरुपयोग शामिल हैं, जिससे की महत्वपूर्ण LLM deployment platforms पर अनाधिकृत पहूँच (unauthorized access) बड़ती हैं । दोनों हमलें cloud-आधारित ML मॉडल पर आधारित supply chains के  लिए महत्वपूर्ण जोखिमों हैंं, क्योंकि compromised environments संवेदनशील डेटा को उजागर करने एवं हमलों में बढ़ोतरी कर सकते हैं ।
#### परिदृश्य#8: LeftOvers (CVE-2023-4969)
  संवेदनशील डेटा को वापस र्प्राप्त करने के  लिए लीक हुई GPU local memory के  leftover का exploition करना । हमलावर (malicious attacker) इस हमलें का उपयोग production servers एवं development workstations तथा laptops के  संवेदनशील डेटा को exfiltrate करने के  लिए कर सकता हैं।
#### परिदृश्य#9: WizardLM
  WizardLM को हटाने के  बाद, एक हमलावर (malicious attacker) इस मॉडल में रुची (popularity) का फायदा उठाकर उसी नाम के  साथ मॉडल का एक नकली संस्करण प्रकाशित करता हैं, लेकिन malware एवं backdoors के  साथ ।
#### परिदृश्य#10: Model Merge/Format Conversion Service
  एक हमलावर (malicious attacker) model merge तथा format conversation service के  प्रयोग से , सार्वजनिक रूप से उपलब्ध access model को compromise करने के  लिए उसमें malware डालता हैं । यह vendor HiddenLayer द्वारा प्रकाशित एक वास्तविक हमला हैं ।
#### परिदृश्य#11: Reverse-Engineer Mobile App
  एक हमलावर (malicious attacker) Mobile App को Reverse-Engineer करके  उसके  मॉडल को एक छेड़छाड़ किए गए मॉडल से बदल कर user को social engineering द्वारा scam site से गलत app डाउनलोड कराता हैंं । यह एक ""real attack on predictive AI" हैं जिसने 116 Google Play apps को प्रभावित किया, जिसमें की बहुत से लोकप्रिय सुरक्षा एवं सुरक्षा-महत्वपूर्ण applications हैंं जिसमें की cash recognition, parental control, face authentication एवं financial service आदि प्रकार के  app भी शामिल हैंं । 
  संदर्भित link: [real attack on predictive AI](https://arxiv.org/abs/2006.08131)
#### परिदृश्य#12: Dataset Poisoning
  एक हमलावर (malicious attacker) सार्वजनिक रूप से उपलब्ध डेटासेट को poison करता हैं, जिससे की मॉडल की fine-tuning के  दौरान उसमें backdoor बनाएँ जा सकते हैं । यह backdoor सूक्ष्म एवं गुप्त रूप से विभिन्न बाजारों में कुछ कंपनियों के  प्रती पक्षपात करने के  प्रयोग में आते हैं ।
#### परिदृश्य#13: T&Cs (नियम व शर्तें) एवं गोपनीयता नीति
  एक LLM operator अपने T&Cs (नियम व शर्तें) एवं गोपनीयता नीति को बदलता हैं ताकि वह मॉडल प्रशिक्षण के  लिए application डेटा का प्रयोग कर सके, एवं इसमें प्रयोग से बाहर निकालने के  लिये खास प्रकार की नीति की आवश्यकता हो, जिससे की संवेदनशील डेटा मॉडल को याद होता रहे ।

### संबंधित लिंक

1. [PoisonGPT: How we hid a lobotomized LLM on Hugging Face to spread fake news](https://blog.mithrilsecurity.io/poisongpt-how-we-hid-a-lobotomized-llm-on-hugging-face-to-spread-fake-news)
2. [Large Language Models On-Device with MediaPipe and TensorFlow Lite](https://developers.googleblog.com/en/large-language-models-on-device-with-mediapipe-and-tensorflow-lite/)
3. [Hijacking Safetensors Conversion on Hugging Face](https://hiddenlayer.com/research/silent-sabotage/)
4. [ML Supply Chain Compromise](https://atlas.mitre.org/techniques/AML.T0010)
5. [Using LoRA Adapters with vLLM](https://docs.vllm.ai/en/latest/models/lora.html)
6. [Removing RLHF Protections in GPT-4 via Fine-Tuning](https://arxiv.org/pdf/2311.05553)
7. [Model Merging with PEFT](https://huggingface.co/blog/peft_merging)
8. [HuggingFace SF_Convertbot Scanner](https://gist.github.com/rossja/d84a93e5c6b8dd2d4a538aa010b29163)
9. [Thousands of servers hacked due to insecurely deployed Ray AI framework](https://www.csoonline.com/article/2075540/thousands-of-servers-hacked-due-to-insecurely-deployed-ray-ai-framework.html)
10. [LeftoverLocals: Listening to LLM responses through leaked GPU local memory](https://blog.trailofbits.com/2024/01/16/leftoverlocals-listening-to-llm-responses-through-leaked-gpu-local-memory/)

### संबंधित फ्रेमवर्क (frameworks) एवं टैक्सोनॉमी (taxonomies)

Infrastructure deployment, applied environment controls तथा अन्य सर्वोत्तम उपायों से संबंधित व्यापक जानकारी, परिदृश्यों की रणनीतियों के  लिए इस खंड का संदर्भ लें ।

- [ML Supply Chain Compromise](https://atlas.mitre.org/techniques/AML.T0010) - **MITRE ATLAS**
