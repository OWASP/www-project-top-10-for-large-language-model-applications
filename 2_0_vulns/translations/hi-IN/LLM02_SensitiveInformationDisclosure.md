## LLM02: 2025 संवेदनशील सूचना का प्रकटीकरण

### विवरण

संवेदनशील जानकारी LLM एवं उसकी application के संदर्भ दोनों को प्रभावित करती हैं । इसमें personal identifiable information (PII), वित्तीय विवरण, स्वास्थ्य रिकॉर्ड, गोपनीय व्यवसाय डेटा, सिक्युरिटी क्रेडेंशियल्स और कानूनी दस्तावेज शामिल हैंं । Proprietary मॉडल में अद्वितीय प्रशिक्षण विधियाँ एवं source code भी संवेदनशील माना जा सकते हैं, विशेष रूप से closed एवं foundation मॉडल में ।

LLM, विशेष रूप से जब applications में जोड़े जाते हैंं तो ये, संवेदनशील डेटा, proprietary algorithms, या उनके आउटपुट के माध्यम से गोपनीय विवरण को उजागर करने का खतरा रखते हैं । इसके परिणामस्वरूप अनाधिकृत डेटा पहूँच (data access), गोपनीयता उल्लंघन एवं बौद्धिक संपदा उल्लंघनों का परिणाम हो सकता हैं । उपभोक्ताओं को पता होना चाहिए कि LLM को सुरक्षित रूप से कैसे प्रयोग करें । उन्हें अनजाने में संवेदनशील डेटा प्रदान करने के जोखिमों को समझने चाहिए, जिससे बाद में मॉडल के आउटपुट में इनका खुलासा ना होने पाए ।

इसी लिये LLM applications को user डेटा को प्रशिक्षण मॉडल में प्रवेश करने से रोकने के लिए पर्याप्त डेटा सैनिटाइजेशन करना चाहिए । Applications मालिकों को स्पष्ट Terms of Use policies (उपयोग की नीतियों) प्रदान करनी चाहिए, जिससे users प्रशिक्षण मॉडल में अपने डेटा को शामिल करने या ना करने के लिये स्वयं बाध्य हो जाये । LLM द्वारा दिए जा सकने वाले data types के बारे में सिस्टम prompt के भीतर प्रतिबंधों को जोड़ने से संवेदनशील जानकारी के प्रकटीकरण से बचाव कर सकते हैं । हालांकि, इस तरह के प्रतिबंधों का सुझाव नहीं दिया जाता क्योंकि इन्हे Prompt इंजेक्शन या अन्य तरीकों के माध्यम से नजरअंदाज किया जा सकता हैं ।

### Vulnerability के सामान्य उदाहरण

#### 1. PII रिसाव
  Personal identifiable information (PII) का खुलासा LLM के प्रयोग के दौरान हो सकता हैं ।
#### 2. Proprietary Algorithm द्वारा खुलासा
  खराब तरीके से configured किए गए मॉडल proprietary algorithms या डेटा को प्रकट कर सकते हैंं । प्रशिक्षण डेटा की जानकारी से मॉडल पर inversion attacks हो सकते हैं, जिससे हमलावर (mallicious attacker) इनपुट को पुनर्निर्मित तथा संवेदनशील जानकारी निकालते सकता हैंं । 
  उदाहरण स्वरूप, जैसा कि 'Proof Pudding' attack (CVE-2019-20634) में बताया गया हैं, disclosed प्रशिक्षण डेटा से मॉडल में extraction एवं inversion होता हे, जिससे हमलावर (mallicious attacker) को ML algorithms में नियंत्रणों को दरकिनार करने एवं ईमेल फिल्टर को बायपास कर देता हैंं ।
#### 3. संवेदनशील व्यापारिक डेटा का प्रकटीकरण
  उत्पन्न प्रतिक्रियाओं में अनजाने में गोपनीय व्यावसायिक जानकारी शामिल हो सकती हैं ।

### रोकथाम एवं बचाव के लिये रणनीतियाँ

#### Sanitization:

#### 1 । डेटा सैनिटाइजेशन तकनीकों को जोड़े
  User डेटा को प्रशिक्षण मॉडल में प्रवेश करने से रोकने के लिए डेटा सैनिटाइजेशन को लागू करें । इसमें अंतर्गत प्रशिक्षण में उपयोग किए जाने से पहले संवेदनशील सामग्री की scrubbing (छाँट कर हटाना ) या masking (चुप देना) करना शामिल हैं ।
#### 2 । मजबूत इनपुट validation ( मापदंड के अनुसार वैधीकरण)
  संभावित रूप से हानिकारक या संवेदनशील डेटा इनपुट का पता लगाने एवं फ़िल्टर करने के लिए सख्त इनपुट validations का प्रयोग करें ,यह सुनिश्चित करें कि वे मॉडल को compromise तो नहीं कर रहे ।

#### Access Controls:

#### 1 । सख्त Access Controls लागू करें
  कम से कम privilege ( विशेषाधिकार ) के आधार पर संवेदनशील डेटा तक पहूँच (access) को सीमित करें । केवल उस डेटा तक पहूँच (access) प्रदान करें जो विशिष्ट user या process (प्रक्रिया) के लिए आवश्यक हैं ।
#### 2 । डेटा स्रोतों को प्रतिबंधित करें
  बाहरी डेटा स्रोतों तक मॉडल की पहूँच (access) को सीमित करें, और सुनिश्चित करें कि runtime डेटा orchestration को अनपेक्षित डेटा रिसाव से बचने के लिए सुरक्षित रूप से संभाला जा रहा हो ।

#### Federated Learning एवं गोपनीयता तकनीक (Privacy Techniques):

#### 1. Federated Learning का उपयोग करें
  कई servers तथा devices में संग्रहीत decentralized डेटा का उपयोग करके मॉडल को प्रशिक्षित करें । यह तरीका centralised डेटा संग्रह की आवश्यकता को कम करता हैं और exposure जोखिमों को कम करता हैं ।
#### 2. Differential गोपनीयता को शामिल करें
  ऐसी तकनीकों को लागू करें जो डेटा या आउटपुट में कार्य की दरस्ती से अवांछित चीजों को जोड़ती हैंं, जिससे हमलावरों के लिए व्यक्तिगत डेटा बिंदुओं को reverse-engineer करना मुश्किल हो जाता हैं ।

#### Users के लिय शिक्षा और पारदर्शिता:

#### 1. LLM के सुरक्षित उपयोग के प्रती users को शिक्षित करें
  संवेदनशील जानकारी के इनपुट में न देने के प्रती उनका मार्गदर्शन करें । सुरक्षित रूप से LLM के प्रयोग (interaction) के प्रती उच्च practices पर प्रशिक्षण दे ।
#### 2. डेटा के उपयोग में पारदर्शिता सुनिश्चित करें
  डेटा के retention, usage, एवं deletion के बारे में स्पष्ट नीतियां बनाएँ । Users को यह अनुमति दे की वह प्रशिक्षण प्रक्रियाओं में अपने डेटा को शामिल करने या ना करने के लिये स्वयं बाध्य हो जाये ।

#### सुरक्षित सिस्टम Configuration:

#### 1. सिस्टम प्राइमबल को Conceal (जो न्यूनतम परिवर्तन हो ) करें 
  आंतरिक Configuration से संपर्क के जोखिमों को कम करने के लिये ,users द्वारा सिस्टम की प्रारंभिक settings को ओवरराइड करने या पहुँचने (access) की क्षमता को सीमित करें ।
#### 2. सुरक्षा से जुड़े Misconfiguration के संदर्भ में उच्च practices
  Error messages या configuration details के माध्यम से संवेदनशील जानकारियों को लीक होने से रोकने के लिए "OWASP API8: 2023 Security Misconfiguration" जैसे दिशानिर्देशों का पालन करें ।
  (संदर्भ link:[OWASP API8:2023 Security Misconfiguration](https://owasp.org/API-Security/editions/2023/en/0xa8-security-misconfiguration/))

#### उन्नत तकनीके 

#### 1. Homomorphic Encryption
  सुरक्षित data analysis evam privacy-preserving machine learning को सक्षम करने के लिए Homomorphic Encryption का उपयोग करें । यह सुनिश्चित करता हैं कि मॉडल द्वारा processe किए जाने के दौरान डेटा गोपनीय रहे ।
#### 2. Tokenization evam Redaction
  Preprocess के लिए tokenization को लागू करें एवं संवेदनशील जानकारी को sanitize करें । Pattern matching जैसी तकनिकें ke dwara processing से पहले गोपनीय सामग्री का पता लगाया जा सकता हैं और फिर से बनाया जा सकता हैं ।

### उदाहरण स्वरूप हमले के परिदृश्य

#### परिदृश्य#1: डेटा का अनजाने में एक्सपोज़र
  एक user अपर्याप्त डेटा sanitization के कारण किसी अन्य user के व्यक्तिगत डेटा से युक्त प्रतिक्रिया प्राप्त करता हैं ।
#### परिदृश्य#2: लक्षित Prompt इंजेक्शन
  एक हमलावर (mallicious attacker) संवेदनशील जानकारी निकालने के लिए input filters को bypass करता हैं ।
#### परिदृश्य#3: प्रशिक्षण डेटा के माध्यम से डेटा लीक होना
  लापरवाह द्वारा डेटा को समावेशित करने के कारण प्रशिक्षण में संवेदनशील जानकारी का प्रकटीकरण होता हैं ।

### संबंधित लिंक

1. [Lessons learned from ChatGPT’s Samsung leak](https://cybernews.com/security/chatgpt-samsung-leak-explained-lessons/): **Cybernews**
2. [AI data leak crisis: New tool prevents company secrets from being fed to ChatGPT](https://www.foxbusiness.com/politics/ai-data-leak-crisis-prevent-company-secrets-chatgpt): **Fox Business**
3. [ChatGPT Spit Out Sensitive Data When Told to Repeat ‘Poem’ Forever](https://www.wired.com/story/chatgpt-poem-forever-security-roundup/): **Wired**
4. [Using Differential Privacy to Build Secure Models](https://neptune.ai/blog/using-differential-privacy-to-build-secure-models-tools-methods-best-practices): **Neptune Blog**
5. [Proof Pudding (CVE-2019-20634)](https://avidml.org/database/avid-2023-v009/) **AVID** (`moohax` & `monoxgas`)

### संबंधित फ्रेमवर्क और टैक्सोनॉमी

Infrastructure deployment, applied environment controls तथा अन्य सर्वोत्तम उपायों से संबंधित व्यापक जानकारी, परिदृश्यों की रणनीतियों के लिए इस खंड का संदर्भ लें ।

- [AML.T0024.000 - Infer Training Data Membership](https://atlas.mitre.org/techniques/AML.T0024.000) **MITRE ATLAS**
- [AML.T0024.001 - Invert ML Model](https://atlas.mitre.org/techniques/AML.T0024.001) **MITRE ATLAS**
- [AML.T0024.002 - Extract ML Model](https://atlas.mitre.org/techniques/AML.T0024.002) **MITRE ATLAS**