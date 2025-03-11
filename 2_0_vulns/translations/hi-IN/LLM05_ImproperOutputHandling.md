## LLM05: 2025 अनुचित प्रकार से आउटपुट को संभालना

### विवरण

यह विशेष रूप से अपर्याप्त सत्यापन(validation), स्वच्छता (sanitization), एवं LLM द्वारा उत्पन्न आउटपुट को विभिन्न क्षेत्रों (components एवं systems) तक पहुँचने से पहले ही संभालना । चूंकि LLM से उत्पन्न सामग्री को Prompt के इनपुट द्वारा नियंत्रित किया जा सकता हैं, इसलिए यह users को अतिरिक्त कार्यक्षमता (additional functionality) तक अप्रत्यक्ष पहूँच (indirect access) प्रदान करने के समान हैं ।
अनुचित प्रकार से आउटपुट को संभालना
की प्रक्रिया, Overreliance से अलग हैं । इसमे द्वारा उत्पन्न आउटपुट को विभिन्न क्षेत्रों (components एवं systems) तक पहुँचने से पहले ही संभाल जाता है, वही Overreliance LLM आउटपुट की सटीकता (accuracy) एवं उपयुक्तता (appropriateness) पर ज्यादा निर्भरता से जुड़ी चिंताओं पर ध्यान केंद्रित करता हैं ।
अनुचित आउटपुट हैंंडलिंग Vulnerability के exploition के कारण वेब ब्राउज़रों पर XSS एवं CSRF, SSRF, विशेषाधिकार में वृद्धि (privilege escalation), या backend systems पर remote code execution जेसे खतरे हो सकते हैंं ।
निम्नलिखित स्थितियां में इन Vulnerabilities का प्रभाव बढ़ सकता हैंं:
- Application द्वारा LLM end uses की जरूरत से ज्यादा विशेषाधिकारों दे दिए जाते हैं, जिससे की privileges escalation या remote code execution जेसे जोखिम पेड़ हो जाते हैं ।
- एक हमलावर (mallicious attacker) Application पर अप्रत्यक्ष Prompt इंजेक्शन हमलों का प्रयोग करके user के environment में विशेषाधिकार वाली पहूँच (privileged access) प्राप्त कर सकता हैं ।
- Third-party extention इनपुटों को पर्याप्त तरह से मान्यता के लिए नहीं परखते ।
- विभिन्न संदर्भों के लिए उचित आउटपुट encoding की कमी (जैसे, HTML, JavaScript, SQL) ।
- LLM आउटपुट की अपर्याप्त निगरानी (Insufficient monitoring) एवं logging होना ।
- LLM उपयोग के लिए rate limiting या anomaly detection की अनुपस्थिति होना ।

### Vulnerability के सामान्य उदाहरण

1. LLM आउटपुट को सीधे system shell या इसी तरह के फ़ंक्शन जैसे exec तथा evalL में दर्ज करने से remote code execution हो जाता हैं ।
2. JavaScript तथा Markdown, LLM द्वारा उत्पन्न होकर user को वापस की जाती हैं । इसके पश्चात कोड को browser द्वारा interpret (समझना) किया जाता हैं, जिसके परिणामस्वरूप XSS होता हैं ।
3. LLM द्वारा उत्पन्न SQL queries को बिना उचित parameterization के बिना ही execute कर दिया जाता हैं, जिससे SQL इंजेक्शन होता हैं ।
4. LLM आउटपुट का उपयोग उचित sanitization के बिना file paths का निर्माण करने के लिए किया जाता हैं, जिसके की path traversal vulnerabilities आ सकती हैंं ।
5. बिना उचित escaping के email templates में LLM द्वारा उत्पन्न सामग्री का उपयोग करने से संभवतः फ़िशिंग हमलों हो सकते हैं ।

### रोकथाम एवं बचाव के लिये रणनीतियाँ

1. मॉडल को किसी अन्य user के समान मानते हुँए zero-trust approach को अपनाए, एवं मॉडल से backend functions तकए आने वाली प्रतिक्रियाओं पर उचित इनपुट validation लागू करें ।
2. प्रभावी इनपुट validation एवं sanitization सुनिश्चित करने के लिए OWASP ASVS (Application Security Verification Standard) दिशानिर्देशों का पालन करें ।
3. JavaScript या Markdown द्वारा अवांछित code execution को कम करने के लिए users को मॉडल आउटपुट encode करके दे । OWASP ASVS आउटपुट encoding पर विस्तृत मार्गदर्शन प्रदान करता हैं ।
4. सामग्री के प्रती जागरूक आउटपुट encoding (context-aware output encoding) को लागू करें जहाँं LLM आउटपुट का उपयोग किया जाएगा (जैसे, वेब सामग्री के लिए HTML encoding, डेटाबेस query के लिए SQL escaping) ।
5. LLM आउटपुट से जुड़े सभी डेटाबेस के कामों के लिए parameterized queries या repared statement का उपयोग करें ।
6. LLM द्वारा उत्पन्न सामग्री से XSS हमलों के जोखिम को कम करने के लिए सख्त सामग्री सुरक्षा नीतियों (Content Security Policies (CSP)) को नियोजित करें ।
7. LLM आउटपुट में असामान्य पैटर्न का पता लगाने के लिए robust logging एवं monitoring systems को लागू करें जो exploit (फायदा उठाना) के प्रयासों को इंगित कर सकता हैं ।

### उदाहरण स्वरूप हमले के परिदृश्य

#### परिद्रश्य 1
  एक application चैटबॉट की प्रतिक्रियाएं के लिए LLM extension का उपयोग करती हैं । यह extension एक अन्य विशेषाधिकार प्राप्त LLM के लिए कई administrative functions भी प्रदान करता हैं । यह सामान्य प्रयोजन के लिये प्रयोग में आने वाला LLM सीधे अपनी प्रतिक्रिया को extension के लिए बिना किसी उचित आउटपुट validation के देता हैंं जिससे की extension रखरखाव के लिए shut down हो जाता हैं ।
#### परिदृश्य#2
  एक user लेख का संक्षिप्त सारांश उत्पन्न करने के लिए LLM द्वारा संचालित वेबसाइट सारांश उपकरण (website summarizer tool) का उपयोग करता हैं । इस वेबसाइट में एक Prompt इंजेक्शन शामिल होता हैं, जो LLM को वेबसाइट या user की बातचीत से संवेदनशील सामग्री को पकड़ने के लिए निर्देश देता हैं । वहाँं से LLM संवेदनशील डेटा को encode करके बिना किसी आउटपुट validation या फ़िल्टरिंग हमलावर-नियंत्रित सर्वर पर भेज सकता हैं ।
#### परिदृश्य#3
  एक LLM users को चैट की सुविधा से बैकएंड डेटाबेस के लिए SQL query बनाने की सुविधा देता हैं । एक user सभी डेटाबेस tables को हटाने के लिए एक query डालता हैं । यदि LLM से बनी query की जांच (scrutinized) नहीं की जाती हैं, तो सभी डेटाबेस tables हट सकते हैंं ।
#### परिदृश्य#4
  एक वेब app, LLM के उपयोग से बिना आउटपुट sanitization के user texts prompts से सामग्री उत्पन्न करता हैं । अब Prompts की अपर्याप्त validation के कारण, एक हमलावर (mallicious attacker) तैयार किए गए Prompt को भेजकर LLM से unsanitized JavaScript payload को मगवाता हैं, जिसे पीड़ित के browser पर रेंडर किए जाने पर XSS हो जाता हैं ।
#### परिदृश्य#5
  एक LLM का उपयोग marketing campaign के लिए dynamic email template उत्पन्न करने के लिए किया जाता हैं । एक हमलावर (mallicious attacker) ईमेल सामग्री के भीतर दुर्भावनापूर्ण JavaScript को शामिल करने के लिए LLM में हेरफेर करता हैं । यदि application LLM आउटपुट को ठीक से sanitize नहीं करती तो यह recipients पर XSS हमलों को जन्म दे सकता हैं जो की Vulnerable email clients में ईमेल देखते हैंं ।
#### परिदृश्य#6
  एक LLM का उपयोग software कंपनी में natural language इनपुट से कोड उत्पन्न करने के लिए किया जाता हैं, जिससे की development कार्यों को सुव्यवस्थित कर सकें । कार्य-कुशल होने के बावजूत यह तरीका संवेदनशील जानकारी को उजागर करने, असुरक्षित डेटा हैंंडलिंग विधियों को बनाने, या SQL इंजेक्शन जैसी vulnerabilities को पेश करने का जोखिम बड़ाता हैं । AI गैर-मौजूद software packages को भी hallucinate कर सकता हैं, जिससे की developers malware-संक्रमित संसाधनों को डाउनलोड करें । पूरी तरह से code review एवं सुझाए गए packages की validation ,सुरक्षा उल्लंघनों, अनाधिकृत पहूँच (unauthorized access) एवं सिस्टम समझौते (system compromises) को रोकने के लिए महत्वपूर्ण हैं ।

### संबंधित लिंक

1. [Proof Pudding (CVE-2019-20634)](https://avidml.org/database/avid-2023-v009/) **AVID** (`moohax` & `monoxgas`)
2. [Arbitrary Code Execution](https://security.snyk.io/vuln/SNYK-PYTHON-LANGCHAIN-5411357): **Snyk Security Blog**
3. [ChatGPT Plugin exploit (फायदा उठाना) Explained: From Prompt Injection to Accessing Private Data](https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./): **Embrace The Red**
4. [New prompt injection attack on ChatGPT web version. Markdown images can steal your chat data.](https://systemweakness.com/new-prompt-injection-attack-on-chatgpt-web-version-ef717492c5c2?gi=8daec85e2116): **System Weakness**
5. [Don’t blindly trust LLM responses. Threats to chatbots](https://embracethered.com/blog/posts/2023/ai-injections-threats-context-matters/): **Embrace The Red**
6. [Threat Modeling LLM Applications](https://aivillage.org/large%20language%20models/threat-modeling-llm/): **AI Village**
7. [OWASP ASVS - 5 Validation, Sanitization and Encoding](https://owasp-aasvs4.readthedocs.io/en/latest/V5.html#validation-sanitization-and-encoding): **OWASP AASVS**
8. [AI hallucinates software packages and devs download them – even if potentially poisoned with malware](https://www.theregister.com/2024/03/28/ai_bots_hallucinate_software_packages/) **Theregiste**