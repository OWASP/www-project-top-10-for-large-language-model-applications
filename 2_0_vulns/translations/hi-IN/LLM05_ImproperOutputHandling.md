## LLM05: 2025 अनुचित प्रकार से आउटपुट को संभालना

### विवरण

इसके अंतर्गत अपर्याप्त सत्यापन (validation), स्वच्छता (sanitization), एवं LLM के आउटपुट को विभिन्न क्षेत्रों (components एवं systems) तक पहुँचने से पहले ही संभालना शामिल हैं । चूंकि LLM से बनी सामग्री को Prompt के इनपुट से नियंत्रित कर सकते हैं, इसलिए यह users को कुछ अतिरिक्त कार्यक्षमता (additional functionality) तक अप्रत्यक्ष पहूँच (indirect access) प्रदान करने के समान हैं ।
अनुचित प्रकार से आउटपुट को संभालना की प्रक्रिया, Overreliance से अलग हैं । इसमे आउटपुट को विभिन्न क्षेत्रों (components एवं systems) तक पहुँचने से पहले ही संभाल जाता हैंं, वही Overreliance LLM आउटपुट की सटीकता (accuracy) एवं उपयुक्तता (appropriateness) पर ज्यादा निर्भरता से जुड़ी चिंताओं पर ध्यान केंद्रित करता हैं ।
इसकी Vulnerability के exploition (फायदा उठान) से web browsers पर XSS एवं CSRF, SSRF, privilege escalation, या backend systems पर remote code execution जेसे खतरे पैदा 
हो सकते हैंं ।
निम्नलिखित स्थितियां में इन Vulnerabilities का प्रभाव बढ़ सकता हैंं:
- Application द्वारा LLM को end users की जरूरत से ज्यादा विशेषाधिकारों दे दिए जाते हैं, जिससे की privileges escalation या remote code execution जेसे जोखिम पैदा हो जाते हैं ।
- एक हमलावर (mallicious attacker) application पर अप्रत्यक्ष Prompt इंजेक्शन हमले से user के environment में विशेषाधिकार वाली पहूँच (privileged access) प्राप्त कर सकता हैं ।
- Third-party extentions, इनपुटों को पर्याप्त तरह से validate (मान्यता के लिए परखना) नहीं करते ।
- विभिन्न संदर्भों में उचित आउटपुट encoding की कमी (जैसे, HTML, JavaScript, SQL) ।
- LLM आउटपुट की अपर्याप्त monitoring (निगरानी) एवं logging (जाँच के लिए सहेजना) होना ।
- LLM उपयोग के लिए rate limiting या anomaly detection की अनुपस्थिति होना ।

### Vulnerability के सामान्य उदाहरण

1. LLM आउटपुट या funtions जैसें की exec तथा eval को सीधे system shell से प्रयोग करने से remote code execution का खतरा हो सकता हैं ।
2. LLM से JavaScript तथा Markdown को बनाकर user को वापस किया जाता हैं । इसके पश्चात कोड को browser द्वारा interpret (समझना) किया जाता हैं, जिसके परिणामस्वरूप XSS होता हैं ।
3. LLM द्वारा उत्पन्न SQL queries को बिना उचित parameterization (विभिन्न parameters की जाँच) के ही execute कर दिया जाता हैं, जिससे SQL इंजेक्शन होता हैं ।
4. उचित sanitization के बिना ही LLM आउटपुट का उपयोग file paths को बनाने के लिए करने से path traversal vulnerabilities आ सकती हैंं ।
5. बिना उचित escaping के email templates में LLM से बनी सामग्री के उपयोग से फ़िशिंग हमले हो सकते हैं ।

### रोकथाम एवं बचाव के लिये रणनीतियाँ

1. मॉडल को user मानते हुँए zero-trust approach को अपनाएँ, एवं मॉडल से backend functions तक जानें वाली प्रतिक्रियाओं पर उचित इनपुट validation लागू करें ।
2. प्रभावी तौर पर इनपुट validation एवं sanitization को सुनिश्चित करने के लिए OWASP ASVS (Application Security Verification Standard) दिशानिर्देशों का पालन करें ।
3. JavaScript या Markdown के द्वारा अनचाहे code execution को कम करने के लिए users को मॉडल आउटपुट encode करके देें । OWASP ASVS आउटपुट encoding पर विस्तृत मार्गदर्शन प्रदान करता हैं ।
4. जहाँं LLM आउटपुट का उपयोग किया जाएगा (जैसे, वेब सामग्री के लिए HTML encoding, डेटाबेस query के लिए SQL escaping), वहाँं सामग्री के प्रती जागरूक आउटपुट encoding (context-aware output encoding) को लागू करें ।
5. LLM आउटपुट से जुड़े सभी डेटाबेस कार्यों के लिए parameterized queries या prepared statement का उपयोग करें ।
6. LLM से बनी सामग्री से XSS हमलों के जोखिम को कम करने के लिए सख्त सामग्री सुरक्षा नीतियों (Content Security Policies (CSP)) को लागू करें ।
7. LLM आउटपुट में असामान्य पैटर्न का पता लगाने के लिए robust logging एवं monitoring systems को लागू करें, जो exploit (फायदा उठाना) के प्रयासों को चिह्नित कर सकते हैं ।

### उदाहरण स्वरूप हमले के परिदृश्य

#### परिद्रश्य 1
  एक application, चैटबॉट की प्रतिक्रियाएं के लिए LLM extension का उपयोग करती हैं । यह extension किसी अन्य विशेषाधिकार वाले LLM के लिए कई administrative functions भी प्रदान करता हैं । जब सामान्य प्रयोग वाला LLM सीधे अपनी प्रतिक्रिया, extension को बिना किसी आउटपुट validation के देता हैंं, वह extension को रखरखाव के लिए shut down कर देता हैं ।
#### परिदृश्य#2
  एक user किसी लेख (article) का संक्षिप्त सारांश करने के लिए LLM संचालित website summarizer tool का उपयोग करता हैं । इस वेबसाइट में एक Prompt इंजेक्शन होता हैं, जो LLM को वेबसाइट या user की बातचीत से संवेदनशील सामग्री निकालने को कहता हैं । वहाँं से LLM संवेदनशील डेटा को encode करके बिना किसी आउटपुट validation या फ़िल्टरिंग के हमलावर-नियंत्रित सर्वर पर भेज सकता हैं ।
#### परिदृश्य#3
  एक LLM, users को चैट से बैकएंड डेटाबेस के लिए SQL query बनाने की सुविधा देता हैं । एक user डेटाबेस की किसी table को हटाने के लिए एक query माँगता हैं । यदि LLM से बनी इस query की जाँच (scrutinized) नहीं की जाती हैं, तो सभी डेटाबेस tables भी हट सकती हैंं ।
#### परिदृश्य#4
  एक वेब app बिना आउटपुट sanitization के, LLM से user texts prompts द्वारा सामग्री बनवा रहा हैं । अब Prompts की अपर्याप्त validation के कारण, एक हमलावर (mallicious attacker) तैयार किए Prompt द्वारा LLM से unsanitized JavaScript payload मगँवाता हैं, जिसे पीढ़ित के browser पर रेंडर करने से XSS हो सकता हैं ।
#### परिदृश्य#5
  एक LLM का उपयोग marketing campaign के लिए dynamic email template बनाने के लिए होता हैं । एक हमलावर (mallicious attacker) LLM में हेरफेर से, ईमेल सामग्री के भीतर दुर्भावनापूर्ण JavaScript डलवा देता हैं । यदि application LLM आउटपुट को ठीक से sanitize नहीं करती तो यह, vulnerable email clients पर ईमेल देखनें वाले  recipients पर XSS हमलों को जन्म दे सकता हैं ।
#### परिदृश्य#6
  एक LLM का उपयोग software कंपनी में natural language इनपुट से कोड उत्पन्न करने के लिए किया जाता हैं, जिससे की development कार्यों को सुव्यवस्थित कर सकें । कार्य-कुशल होने के बावजूत यह तरीका संवेदनशील जानकारी को उजागर करने (exposing sensitive information), असुरक्षित डेटा हैंंडलिंग विधियों को बनाने (reating insecure data handling methods), या SQL इंजेक्शन जैसी vulnerabilities के जोखिम को बड़ाता हैं । AI गैर-मौजूद software packages को भी hallucinate कर सकता हैं, जिससे की developers malware वाले resources को डाउनलोड करें । सुरक्षा उल्लंघनों (security breaches), अनाधिकृत पहूँच (unauthorized access) एवं सिस्टम समझौते (system compromises) को रोकने के लिए पूर्ण तरह से code का review एवं सुझाए गए packages का validation महत्वपूर्ण हैं ।

### संबंधित लिंक

1. [Proof Pudding (CVE-2019-20634)](https://avidml.org/database/avid-2023-v009/) **AVID** (`moohax` & `monoxgas`)
2. [Arbitrary Code Execution](https://security.snyk.io/vuln/SNYK-PYTHON-LANGCHAIN-5411357): **Snyk Security Blog**
3. [ChatGPT Plugin exploit (फायदा उठाना) Explained: From Prompt Injection to Accessing Private Data](https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./): **Embrace The Red**
4. [New prompt injection attack on ChatGPT web version. Markdown images can steal your chat data.](https://systemweakness.com/new-prompt-injection-attack-on-chatgpt-web-version-ef717492c5c2?gi=8daec85e2116): **System Weakness**
5. [Don’t blindly trust LLM responses. Threats to chatbots](https://embracethered.com/blog/posts/2023/ai-injections-threats-context-matters/): **Embrace The Red**
6. [Threat Modeling LLM Applications](https://aivillage.org/large%20language%20models/threat-modeling-llm/): **AI Village**
7. [OWASP ASVS - 5 Validation, Sanitization and Encoding](https://owasp-aasvs4.readthedocs.io/en/latest/V5.html#validation-sanitization-and-encoding): **OWASP AASVS**
8. [AI hallucinates software packages and devs download them – even if potentially poisoned with malware](https://www.theregister.com/2024/03/28/ai_bots_hallucinate_software_packages/) **Theregiste**