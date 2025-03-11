## LLM01: 2025 Prompt इंजेक्शन

### विवरण

Prompt इंजेक्शन Vulnerability तब होती हैं, जब user के prompts द्वारा LLM के व्यवहार तथा आउटपुट में अनपेक्षित ढंग से बदलाव या जाए । यह इनपुट मॉडल को प्रभावित कर सकते हैंं, भले ही वे मनुष्यों के लिए अगोचर हों, इसलिए Prompt इंजेक्शन को मानव-दृश्यमान/पठनीय होने की आवश्यकता नहीं है, जब तक कि सामग्री को मॉडल द्वारा पार्स किया जाता रहे ।

Prompt इंजेक्शन की vulnerabilities इस बात पर निर्भर हे की मॉडल prompts को कैसे प्रतिपादित(process) करता हैं, और कैसे इनपुट मॉडल को गलत तरीके से उसके अन्य हिस्सों में Prompt डेटा को पारित करने के लिए मजबूर कर सकता हैं, जो संभवतः उन्हें निर्देशों का उल्लंघन करने, हानिकारक सामग्री को उत्पन्न करने, अनाधिकृत पहूँच (unauthorized access) के लिये सक्षम करने या महत्वपूर्ण निर्णयों को प्रभावित करने के लिए बाध्य करता हैंं । जबकि LLM आउटपुट को अधिक प्रासंगिक और सटीक बनाने के लिए Retrieval Augmented Generation (RAG) तथा fine-tuning जैसी तकनीकों प्रयोग में आती हैं, वही शोध बाटाते ही की ये पूरी तरह से Prompt इंजेक्शन vulnerabilities को कम नहीं कर सकती हैंं ।

Prompt इंजेक्शन और jailbreaking LLM सुरक्षा में संबंधित सिद्धांत हैंं, पर अक्सर परस्पर उपयोग में आते हैंं । Prompt इंजेक्शन में कुछ खास इनपुट के प्रयोग से, मॉडल की प्रतिक्रियाओं में हेरफेर करके उसके व्यवहार में परिवर्तन करना शामिल है, जिसमें सुरक्षा उपायों को दरकिनार करना भी शामिल हो सकता हैंं । Jailbreaking, prompt इंजेक्शन का एक रूप हैं जहाँं हमलावर (mallicious attacker) इनपुट प्रदान करता हैं जो मॉडल की अपने सुरक्षा प्रोटोकॉल की पूरी तरह से अवहेलना करने का कारण बनता हैं । developers Prompt इंजेक्शन हमलों से बचाव के लिए सिस्टम Prompt एवं इनपुट हैंंडलिंग में सुरक्षा उपायों को निर्मित कर सकते हैंं, लेकिन jailbreaking की प्रभावी रोकथाम के लिए मॉडल के प्रशिक्षण एवं सुरक्षा तंत्र में अपडेट की आवश्यकता होती हैं ।

### Prompt इंजेक्शन vulnerabilities के प्रकार

#### प्रत्यक्ष Prompt इंजेक्शन
  प्रत्यक्ष Prompt इंजेक्शन में user का Prompt इनपुट सीधे अनपेक्षित या अप्रत्याशित तरीकों से मॉडल के व्यवहार को बदल देता हैं । यह इनपुट या तो जानबूझकर हो सकता हैं (यानी, एक दुर्भावनापूर्ण व्यक्ति जानबूझकर मॉडल का फायदा उठाने के लिए कुछ prompts को तैयार करे) या अनजाने में (यानी, एक user अनजाने में ऐसा इनपुट देता हैं जो अप्रत्याशित व्यवहार को ट्रिगर करता हैं) ।

#### अप्रत्यक्ष Prompt इंजेक्शन
  अप्रत्यक्ष Prompt इंजेक्शन में LLM बाहरी स्रोतों (वेबसाइट या फाइलें) से इनपुट स्वीकार करता हैं, जिनकी सामग्री को मॉडल द्वारा प्रयोग (interpret) में लाने से मॉडल के व्यवहार में अनपेक्षित या अप्रत्याशित बदलाव हो जाते हैं । यह भी प्रत्यक्ष इंजेक्शन की तरह, जानबूझकर या अनजाने में हो सकता हैंं ।

सफल Prompt इंजेक्शन हमलें के प्रभाव की गंभीरता और प्रकृति बहुत भिन्न हो सकती हैं एवं ये बड़े पैमाने पर व्यवसाय के संदर्भ में जिसके लिये मॉडल काम में लिया जा रहा हैं, तथा जिस एजेंसी के साथ मॉडल ढाल गया हैं । आम तौर पर, Prompt इंजेक्शन अनपेक्षित परिणामों को जन्म देता हैं, लेकिन कुछ निम्नलिखित बिन्दुओ तक सीमित नहीं हैं जेसे की :

- संवेदनशील जानकारी का प्रकटीकरण
- AI सिस्टम ढ़ाचे (infrastructure) या सिस्टम Prompt के बारे में संवेदनशील जानकारी का खुलासा करना
- सामग्री हेरफेर जो की गलत या पक्षपाती आउटपुट की और ले जाये
- LLM के लिए उपलब्ध functions की अनाधिकृत पहूँच (unauthorized access) प्रदान करना
- कनेक्टेड सिस्टम में मनमानी आदेशों को निष्पादित (Executing) करना
- महत्वपूर्ण निर्णय लेने की प्रक्रियाओं में हेरफेर करना

मल्टीमॉडल (multimodal) AI का उदय, जो एक साथ कई प्रकार के data-types को संसाधित कर सकता हैं, वह कुछ नए Prompt इंजेक्शन जोखिमों को उत्पन्न करता हैं । दुर्भावनापूर्ण व्यक्ति modalities के बीच बातचीत (interactions) का फायदा उठा सकते हैंं, जैसें कि सौम्य texts के साथ imageयों में निर्देश छिपाना । इन प्रणालियों की जटिलता हमलें की होने की संभावनाओ का विस्तार करती हैं । मल्टीमॉडल (multimodal) मॉडल भी कुछ खास cross-modal हमलों के लिए अतिसंवेदनशील हो सकते हैंं जो की वर्तमान तकनीकों के द्वारा पता लगाने एवं उसका समाधान करने के लिए मुश्किल हैंं । मजबूत (Robust) मल्टीमॉडल (multimodal) सुराख समाधान आगे के शोध एवं विकास के लिए एक महत्वपूर्ण क्षेत्र हैं ।

### रोकथाम एवं बचाव के लिये रणनीतियाँ

जनरेटिव AI की प्रकृति ही कारण हे Prompt इंजेक्शन vulnerabilities का, मॉडल के काम करने के तरीके से यह स्पष्ट नहीं हैं कि Prompt इंजेक्शन की रोकथाम के लिया कोई पूर्ण समाधान हो साकता हैंं या नहीं । हालांकि, निम्नलिखित उपाय Prompt इंजेक्शन के प्रभाव को कम कर सकते हैंं:

#### 1. मॉडल के व्यवहार को बाधित करें
सिस्टम Prompt को मॉडल की भूमिका, क्षमताओं एवं सीमाओं के बारे में विशिष्ट निर्देश प्रदान करें । सख्त संदर्भ पालन (context adherence) को लागू करें, विशिष्ट कार्यों एवं विषयों के लिए प्रतिक्रियाओं को सीमित करें, तथा मॉडल को निर्देश दे कि वह कोर निर्देशों को संशोधित करने के प्रयासों को अनदेखा करें ।
#### 2. अपेक्षित आउटपुट प्रारूपों को परिभाषित करें और मान्य करें
  स्पष्ट आउटपुट के formats बताएँ, विस्तृत तर्क एवं स्रोत के citations का अनुरोध करें, और इन प्रारूपों के पालन को मान्य करने के लिए नियतात्मक (deterministic) कोड का उपयोग करें ।
#### 3. इनपुट और आउटपुट फ़िल्टरिंग को लागू करें
  संवेदनशील श्रेणियों को परिभाषित करें और ऐसी सामग्री की पहचान एवं संभालने के लिए नियमों का निर्माण करें । सिमेंटिक (semantic) फ़िल्टर लागू करें एवं बिना अनिमती वाली सामग्री के लिए के लिए स्ट्रिंग-चेकिंग का उपयोग करें । RAG TRIAD का उपयोग करके प्रतिक्रियाओं का मूल्यांकन करें: संभावित दुर्भावनापूर्ण आउटपुट की पहचान करने के लिए संदर्भ प्रासंगिकता, जमीनीपन (groundedness- असलियत से जुड़ाव) और प्रश्न/उत्तर प्रासंगिकता का आकलन करें ।
#### 4. विशेषाधिकार नियंत्रण एवं कम से कम विशेषाधिकार पहूँच को लागू करें
  Application को विस्तारणीय कार्यक्षमता के लिए उसके खुद के API टोकन दे एवं इन funtions को मॉडल को देने की बजाय कोड में संभालें । मॉडल के  विशेषाधिकार पहुँच (privileged access) को न्यूनतम आवश्यक तक सीमित करें ।
#### 5. उच्च जोखिम वाले कार्यों के लिए मानव सविक्रती
  अनाधिकृत कार्यों को रोकने के लिए विशेषाधिकार प्राप्त कार्यों (operations) में human-in-the-loop नियंत्रण को लागू करें ।
#### 6. बाहरी सामग्री को पहचानें एवं भागों में बाटे 
  user prompts पर इसके प्रभाव को सीमित करने के लिए अलग भागों में बाटे एवं स्पष्ट रूप से अविश्वसनीय सामग्री को चिन्हित करें ।
#### 7. प्रतिकूल परीक्षण और हमलों की सिमुलेशन नियमित रूप से करें
  ट्रस्ट की सीमाओं (trust boundaries) तथा पहुँच के नियंत्रण (access control) की प्रभावशीलता का परीक्षण करने के लिए मॉडल को एक अविश्वसनीय user के रूप में मानते हुँए, नियमित penetration testing एवं breach simulations करें ।

### उदाहरण स्वरूप हमलें के परिदृश्य

#### परिदृश्य#1: प्रत्यक्ष इंजेक्शन
  एक हमलावर (mallicious attacker) एक ग्राहक सहायता चैटबॉट में एक prompts को इंजेक्ट करता हैं, वह पिछले दिशानिर्देशों को अनदेखा करने, निजी डेटा स्टोरों को query करने और ईमेल भेजने के लिए निर्देश देता हैं, जिससे अनाधिकृत पहूँच (unauthorized access) एवं विशेषाधिकार वृद्धि (privilege escalation) होती हैं ।
#### परिदृश्य#2: अप्रत्यक्ष इंजेक्शन
  एक user छिपे हुँए निर्देशों वाले एक webpage को संक्षेप में प्रस्तुत करने के लिए एक LLM को नियुक्त करता हैं । उस छुपे निर्देश के कारण LLM एक URL वाली image (image linking to a URL) डालता हे, जिससे कारण निजी वार्तालाप का exfiltration हो जाता हैं ।
#### परिदृश्य#3: अनैच्छिक इंजेक्शन
  एक कंपनी अपने नौकरी विवरण में AI से बने आवेदनों की पहचान के लिए निर्देश शामिल करती हैं । एक आवेदक, इस निर्देश से अनजान, अपने resume को बेहतर करने के लिये LLM का प्रयोग करता हैं, जिससे अनजाने में ही AI detection चालू हो जाता हैंं ।
#### परिदृश्य#4: जानबूझकर मॉडल को प्रभावित करना 
  एक हमलावर (mallicious attacker) एक Retrieval-Augmented Generation (RAG) application वाली repository के एक दस्तावेज़ को संशोधित करता हैं । जिसके कारण जब user की query संशोधित सामग्री लौटाती हैं, तो दुर्भावनापूर्ण निर्देश LLM के आउटपुट को बदल देते हैंं, जिससे भ्रामक परिणामों की उत्पत्ति होती हैंं ।
#### परिदृश्य#5: कोड इंजेक्शन
  एक हमलावर (mallicious attacker) Vulnerability (CVE-2024-5184) का प्रयोग करके एक दुर्भावनापूर्ण prompts को LLM-संचालित ईमेल सहायक application में इंजेक्ट करता हैं, जिससे उसे संवेदनशील जानकारी एवं ईमेल सामग्री में हेरफेर करने की अनुमति मिल जाती हैं ।
#### परिदृश्य#6: पेलोड विभाजन
  एक हमलावर (mallicious attacker) split malicious prompts वाले resume को अपलोड करता हैं । जिसके कारण जब LLM उम्मीदवार का मूल्यांकन करता हैं, तो संयुक्त prompts मॉडल की प्रतिक्रिया में हेरफेर करतें हैंं, जिसके परिणामस्वरूप resume की वास्तविक वाली सामग्री के बावजूद भी सकारात्मक सिफारिश आती हैं ।
#### परिदृश्य#7: मल्टीमॉडल (multimodal) इंजेक्शन
  एक हमलावर (mallicious attacker) ने सामान्य text वाली image के भीतर दुर्भावनापूर्ण prompts दल दिए । जिसके कारण जब एक मल्टीमॉडल (multimodal) AI ने image और texts को एक साथ संसाधित किया, तो छिपा हुआ Prompt के कारण मॉडल के व्यवहार में बदलाव हैं, जिससे संवेदनशील जानकारी का प्रकटीकरण तथा अनाधिकृत कार्यों हो जाते हैं ।
#### परिदृश्य#8: प्रतिकूल Suffix
  एक हमलावर (mallicious attacker) prompts के साथ एक अर्थहीन प्रतीत होता वली string को जोड़ देता हैं, जो एक दुर्भावनापूर्ण तरीके से LLM के आउटपुट को प्रभावित करता हैं,जो सुरक्षा के उपायों को दरकिनार कर देता हैं ।
#### परिदृश्य#9: बहुभाषी गुप्त (Obfuscated/छिपाया हुआ) हमला
  एक हमलावर (mallicious attacker) कई भाषाओं का उपयोग या दुर्भावनापूर्ण निर्देशों को (जैसे, Base64 or emojis) के भीतर encodes ताकि वह फिल्टर से बच जाये तथा LLM के व्यवहार में हेरफेर कर सकें ।

### संबंधित लिंक

1. [ChatGPT Plugin Vulnerabilities - Chat with Code](https://embracethered.com/blog/posts/2023/chatgpt-plugin-vulns-chat-with-code/) **Embrace the Red**
2. [ChatGPT Cross Plugin Request Forgery and Prompt Injection](https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./) **Embrace the Red**
3. [Not what you’ve signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection](https://arxiv.org/pdf/2302.12173.pdf) **Arxiv**
4. [Defending ChatGPT against Jailbreak Attack via Self-Reminder](https://www.researchsquare.com/article/rs-2873090/v1) **Research Square**
5. [Prompt Injection attack against LLM-integrated Applications](https://arxiv.org/abs/2306.05499) **Cornell University**
6. [Inject My PDF: Prompt Injection for your Resume](https://kai-greshake.de/posts/inject-my-pdf) **Kai Greshake**
8. [Not what you’ve signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection](https://arxiv.org/pdf/2302.12173.pdf) **Cornell University**
9. [Threat Modeling LLM Applications](https://aivillage.org/large%20language%20models/threat-modeling-llm/) **AI Village**
10. [Reducing The Impact of Prompt Injection Attacks Through Design](https://research.kudelskisecurity.com/2023/05/25/reducing-the-impact-of-prompt-injection-attacks-through-design/) **Kudelski Security**
11. [Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations (nist.gov)](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-2e2023.pdf)
12. [2407.07403 A Survey of Attacks on Large Vision-Language Models: Resources, Advances, and Future Trends (arxiv.org)](https://arxiv.org/abs/2407.07403)
13. [Exploiting Programmatic Behavior of LLMs: Dual-Use Through Standard Security Attacks](https://ieeexplore.ieee.org/document/10579515)
14. [Universal and Transferable Adversarial Attacks on Aligned Language Models (arxiv.org)](https://arxiv.org/abs/2307.15043)
15. [From ChatGPT to ThreatGPT: Impact of Generative AI in Cybersecurity and Privacy (arxiv.org)](https://arxiv.org/abs/2307.00691)

### संबंधित फ्रेमवर्क और टैक्सोनॉमी

Infrastructure deployment, applied environment controls तथा अन्य सर्वोत्तम उपायों से संबंधित व्यापक जानकारी, परिदृश्यों की रणनीतियों के लिए इस खंड का संदर्भ लें ।

- [AML.T0051.000 - LLM Prompt Injection: Direct](https://atlas.mitre.org/techniques/AML.T0051.000) **MITRE ATLAS**
- [AML.T0051.001 - LLM Prompt Injection: Indirect](https://atlas.mitre.org/techniques/AML.T0051.001) **MITRE ATLAS**
- [AML.T0054 - LLM Jailbreak Injection: Direct](https://atlas.mitre.org/techniques/AML.T0054) **MITRE ATLAS**