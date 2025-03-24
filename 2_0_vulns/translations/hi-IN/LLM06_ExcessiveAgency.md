## LLM06: 2025 अत्यधिक एजेंसी

### विवरण

एक LLM आधारित system को अक्सर developers द्वारा degree of agency प्रदान की जाती हैं, मतलब की extension से functions तथा interface के साथ अन्य system को कॉल करने की क्षमता (जिसे अलग-अलग विक्रेताओं द्वारा tools, skills या plugins कहाँ जाता हैंं) जिससे की एक prompts के जवाब में कार्यवाही की जा सकें । LLM agent को इनपुट Prompt तथा LLM आउटपुट के आधार पर, यह निर्णय लेने दे की किस extension का प्रयोग (invoke) करना हैं । Agent आधारित system आम तौर पर, नए होने वाले invocations को ground (सरल तथा शुद्ध रखना) एवं direct (सिधा) रखने के लिए पिछले invocations के ऑउतपुट के द्वारा LLM को बार-बार कॉल करतें हैं ।

अत्यधिक एजेंसी बिना LLM की खराबी के कारण को जाने ही, LLM के अनचाही, अस्पष्ट या हेरफेर किए गए आउटपुट से होने वाली प्रतिक्रियाओें को हानिकारक/दुर्भावनपूर्ण बनाती हैं । इसके लिए सामान्य trigger निम्नलिखित है:
* खराब तरह के बनाएँ सामान्य prompts या खराब प्रदर्शन करने वाले मॉडल के कारण hallucination/confabulation का होना;
* एक दुर्भावनापूर्ण user द्वारा प्रत्यक्ष/अप्रत्यक्ष (direct/indirect) Prompt इंजेक्शन, एक compromised extension का जरूरत से पहले आह्वान (invocation), या (मल्टी-एजेंट/सहयोगी (collaborative) system में) एक compromise किया गया साथी (peer) एजेंट ।

अत्यधिक एजेंसी के मुख्य कारण आम तौर पर निम्नलिखित होता हैं:
* अत्यधिक कार्यक्षमता (excessive functionality);
* अत्यधिक अनुमतियाँ (excessive permissions);
* अत्यधिक स्वायत्तता (excessive autonomy) ।

अत्यधिक एजेंसी गोपनीयता, अखंडता एवं उपलब्धता के समीकरणों में विस्तृत रूप में प्रभाव डाल सकती हैं, एवं यह इस बात पर भी निर्भर हैं कि LLM पर आधारित app किस system के साथ कार्य करतें हैं ।

नोट: अत्यधिक एजेंसी, असुरक्षित रूप से आउटपुट हैंंडलिंग से अलग हैं जो की LLM आउटपुट की पर्याप्त रूप से जाँच न करने से संबंधित हैं ।

### जोखिमों के सामान्य उदाहरण

#### 1. अत्यधिक कार्यक्षमता (excessive functionality)
  - एक LLM एजेंट के पास कुछ extensions हैं जिनका कार्य system के लिए आवश्यक नहीं हैंं । उदाहरण के लिए, एक developer को LLM एजेंट को किसी repository से documents को पढ़ने का कार्य देना हैं, लेकिन जो 3rd-party extension वे उपयोग कर रहे हैंं, उनमें दस्तावेजों को संशोधित करने एवं हटाने की क्षमता भी शामिल हैं ।
  - एक extension को विकास चरण (development phase) के दौरान, बेहतर विकल्प की आड़ में जाँच कर हटाने के पश्चात भी, मूल plugin LLM एजेंट के लिए उपलब्ध हैं ।
  - एक open-ended कार्यक्षमता वाला LLM plugin बाहर के commands के इनपुट निर्देशों को ठीक से फ़िल्टर करने में विफल रहता हैं, जो की  application के इच्छित संचालन के लिए आवश्यक हैं । उदाहरण के लिए, एक विशिष्ट shell command चलाने के लिए बना extension अन्य shell commands के execution को रोकने में विफल रहता हैं ।
#### 2. अत्यधिक अनुमतियाँ (excessive permissions)
  - एक LLM extension के पास downstream systems तक पहुँच हैं जो की application के लिए आवश्यक नहीं हैं । उदाहरण के लिए, डेटा को पढ़ने वाला extension एक identity का उपयोग करके database server से connect करता हैं, जिसमें न केवल SELECT, बल्कि अनुमतियों जैसें की UPDATE एवं DELETE भी शामिल हैंं ।
  - एक user के व्यक्तिगत कार्यों के लिए बना LLM extensio, एक उच्च-विशेषाधिकार प्राप्त पहचान (generic high-privileged identity) के साथ downstream system का उपयोग करता हैं । उदाहरण के लिए, एक user के दस्तावेज़ स्टोर को पढ़ने के लिए बना extension एक विशेषाधिकार (privileged) प्राप्त account के साथ दस्तावेज़ repository से connect होता हैं, जिसमें अन्य सभी users से संबंधित files भी मौजूद हैं ।
#### 3. अत्यधिक स्वायत्तता (excessive autonomy)
  एक LLM आधारित application या extension स्वतंत्र रूप से उच्च-प्रभाव कार्यों को जाँच एवं मंज़ूरी देने में विफल रहता हैं । उदाहरण के लिए एक extension जो की user के दस्तावेजों को delete करने के लिए हैं, वह user से पुष्टि के बिना ही deletions कर देता हैं ।

### रोकथाम एवं बचाव के लिये रणनीतियाँ

निम्नलिखित क्रियाएं अत्यधिक एजेंसी को रोक सकती हैंं:

#### 1. Extensions का प्रयोग कम करें
  LLM  agents के लिये approve (अनुमति मिलना) हुँए extension को न्यूनतम आवश्यक तक सीमित करें । उदाहरण के लिए, यदि LLM पर आधारित system को URL की सामग्री को fetch करने की क्षमता की आवश्यकता नहीं हैं, तो इस तरह के extension को LLM एजेंट में ना डाले ।
#### 2. Extensions की कार्यक्षमता कम करें
  LLM extension में प्रयोग हुँए functions को न्यूनतम आवश्यक तक सीमित करें । उदाहरण के लिए, एक extension जिसकी की emails का सारांश करने के लिए, user के मेलबॉक्स तक पहुँंच हैं । हो सकता हैंं उसको केवल emails को पढ़ने की क्षमता की आवश्यकता हो, इसलिए extension में अन्य कार्यक्षमता नहीं होनी चाहिए जैसें कि संदेश delete या send करना की ।
#### 3. open-ended extension से बचें
  जहाँं संभव हो, open-ended extensions के उपयोग से बचें (जैसे, एक shell commands चलाएं, एक URL fetch करें, आदि) एवं अधिक granular (छोटी-छोटी) कार्यक्षमता वाले extensions का उपयोग करें । उदाहरण के लिए, एक LLM पर आधारित app को फ़ाइल में कुछ आउटपुट को write करने की आवश्यकता हैं, यदि इसके लिये वह shell functions को run करने वाले extension का उपयोग करता है, तब दुर्भावनापूर्ण कार्यों के होने की गुंजाइश बड़ती हैं (किसी भी अन्य shell commands को execute किया जा सकता हैं) । एक अधिक सुरक्षित विकल्प हो सकता है, की एक विशिष्ट file-writing extension का निर्माण करना जो केवल उस विशिष्ट कार्य को ही करता हो ।
#### 4. Extension की अनुमतियों को कम करें
  LLM extension द्वारा अन्य system को दी गई अनुमतियों को न्यूनतम करें ताकि अवांछनीय कार्यों की आशंकाएँ कम हो सकें । उदाहरण के लिए, एक LLM agent जो उत्पाद डेटाबेस से ग्राहक को खरीद की सिफारिशें देता हैं, उसे केवल 'उत्पादों' वाली table का read access ही चाहिए, इसीलिए उसे अन्य tables तक पहूँच (access) न दे, न ही रिकॉर्ड insert, update या delete करने की क्षमता दे । यह डेटाबेस अनुमतियों को उपयुक्त पहचान (जो की LLM extension डेटाबेस से कनेक्ट करने के लिए उपयोग लेता हैं) उसपार लगाकर लागू की जा सकती हैंं ।
#### 5. User के संदर्भ में extensions को Execute/लागू करें
  User authorization एवं सुरक्षा के दायरे को track करें । इससे यह सुनिश्चित होगा की user द्वारा किए गए कार्य, आवश्यक न्यूनतम विशेषाधिकारों के दायरे में एवं user के संदर्भ में ही downstream system पर ढंग से execute हो । उदाहरण के लिए, एक LLM extension जो user के code repo पर read करता हैं, उसे न्यूनतम गुंजाइश के साथ user द्वारा OAUTH से प्रमाणित (authenticate) होने की आवश्यकता हैं ।
#### 6. User सहमति की आवश्यकता
  Human-in-the-loop (मानव के साथ) नियंत्रण के द्वारा उच्च-प्रभाव वाले कामों को करने (या उच्च-प्रभाव वाले फैसलो को लेने) से पूर्व ही मानव की मंजूरी को आवश्यक करें । इसे downstream system (LLM application के दायरे के बाहर) या LLM extension के भीतर दोनों जगह लागू किया जा सकता हैं । उदाहरण के लिए, एक LLM पर आधारित app जो की सोशल मीडिया सामग्री बनाता हैं एवं पोस्ट करता हैं, उसे पोस्ट करने में user की अनुमति को भी शामिल करना चाहिए ।
#### 7. पूर्ण मध्यस्थता (Complete mediation)
  किसी कार्य की अनुमति (है या नहीं) को जाँचनें के लिए LLM पर भरोसे के बजाय downstream system में authorization लागू करें । पूर्ण मध्यस्थता के सिद्धांत को लागू करें ताकि extension द्वारा downstream system से किए सभी अनुरोध सुरक्षा नीतियों का पालन करें ।
#### 8. LLM इनपुट एवं आउटपुट को Sanitise करें
  Secure coding best practices (सुरक्षित कोडिंग के लिए सर्वोत्तम कार्यों) का पालन करें, जैसें कि ASVS (Application Security Verification Standard) में OWASP की सिफारिशें, इनपुट Sanitisation का विशेष रूप ध्यान रखते हुँए । इसी के साथ Static Application Security Testing (SAST) एवं Dynamic/Interactive application testing (DAST, IAST) का भी उपयोग करें ।

निम्नलिखित विकल्प अत्यधिक एजेंसी पर लगाम के बजाए नुकसान के स्तर को सीमित कर सकते हैंं, जेसे की:
- LLM extension एवं downstream system की गतिविधि को Log (निरीक्षण के लिए सहेजना) एवं monitor (निगरानी करना) करें, जिससे की अवांछनीय क्रियाएं का पता चले एवं तदनुसार जवाब दें सकें ।
- किसी निश्चित समय अवधि में होने वाले अवांछनीय कार्यों को कम करने के लिए rate-limiting (दर-सीमित करना) लागू करें, जिससे की क्षति होने से पूर्व ही निगरानी से अवांछनीय कार्यों को खोज सकते हैंं ।

### उदाहरण स्वरूप हमलें के परिदृश्य

एक LLM पर आधारित सहायक (assistant) app को emails की सामग्री को संक्षेप करने के लिए extension के द्वारा किसी व्यक्ति के मेलबॉक्स तक पहूँच (access) प्रदान की जाती हैं । इसके लिए extension को संदेशों को पड़ने (read) की क्षमता की आवश्यकता हैं, हालांकि system developer ने जो plugin चुना हैं, उसमेंं संदेश भेजने (send) करने की क्षमता भी शामिल हैंं । इसके अतिरिक्त, app अप्रत्यक्ष Prompt इंजेक्शन हमलें से असुरक्षित हैं, जिससे की एक दुर्भावनापूर्ण email, LLM द्वारा एजेंट को user के इनबॉक्स से संवेदनशील जानकारी ढूंढकर हमलावर (malicious attacker) के emails पर भिजवाता हैं । इससे बचने के लिए:
* केवल mail-reading की क्षमताओं वाले extension का उपयोग करके अत्यधिक कार्यक्षमता को समाप्त करें,
* एक read-only वाले OAUTH के माध्यम से user की email सेवा को प्रमाणित (authenticate) करके अत्यधिक अनुमतियों को समाप्त करें, एवं
* User, LLM extension द्वारा तैयार किए गए प्रत्येक mail को खुद ही जाँचें एवं send करें जिससे की अत्यधिक स्वायत्तता (autonomy) समाप्त हो जाये ।
* इसके अतिरिक्त, mail-sending के interface पर rate limit को लागू करके भी नुकसान को कम किया जा सकता हैं ।

### संबंधित लिंक

1. [Slack AI data exfil from private channels](https://promptarmor.substack.com/p/slack-ai-data-exfiltration-from-private): **PromptArmor**
2. [Rogue Agents: Stop AI From Misusing Your APIs](https://www.twilio.com/en-us/blog/rogue-ai-agents-secure-your-apis): **Twilio**
3. [Embrace the Red: Confused Deputy Problem](https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./): **Embrace The Red**
4. [NeMo-Guardrails: Interface guidelines](https://github.com/NVIDIA/NeMo-Guardrails/blob/main/docs/security/guidelines.md): **NVIDIA Github**
6. [Simon Willison: Dual LLM Pattern](https://simonwillison.net/2023/Apr/25/dual-llm-pattern/): **Simon Willison**
7. [Sandboxing Agentic AI Workflows with WebAssembly](https://developer.nvidia.com/blog/sandboxing-agentic-ai-workflows-with-webassembly/) **NVIDIA, Joe Lucas**
