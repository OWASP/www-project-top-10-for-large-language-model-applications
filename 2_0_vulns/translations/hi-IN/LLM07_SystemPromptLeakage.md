## LLM07:2025 System Prompt से Leakage

### विवरण

LLM मे system के व्यवहार को संभालने के लिए उपयोग किए जाने वाले system prompts या निर्देशों में भी संवेदनशील जानकारीया हो सकती हैं। system Prompt को application की आवश्यकताओं के आधार पर मॉडल के आउटपुट को निर्देशित करने के लिए बनाया गया हैं, लेकिन अनजाने में ही संवेदनशील जानकारीयो के रिसाव से अन्य हमलों का खतरा बदता हैं।

यह समझे कि system Prompt गुप्त नहीं होते, न ही यह सुरक्षा नियंत्रण के रूप में उपयोग मे आ सकते है। इसीलिए संवेदनशील डेटा जैसे कि credentials, connection strings आदि को system Prompt मे प्रयोग मे ना ले।

System Prompt में roles एवं permissions, या  संवेदनशील जानकारी जेसे की connection strings या passwords आदि प्रकार की जानकारी का प्रकटीकरण सहायक हो सकता हैं। इसमे सुरक्षा जोखिम इनका खुलासा होना नहीं बल्कि यह है की applicationss मजबूत session management एवं authorization का कार्य LLM को देकर, इनको bypass करने की अनुमति देती है। इसी के साथ इस संवेदनशील डेटा का एक जगह पर संग्रहीत होना, हमलावरों के लिए सोने की खान के समान है।

संक्षेप में समझे तो system prompt का प्रकटीकरण कोई वास्तविक जोखिम नहीं हैं - सुरक्षा जोखिम इसके साथ जुड़े बहुत से भागों मे निहित हैं, चाहे वह संवेदनशील जानकारी का खुलासा हो, system guardrails का bypass हो, privileges का गलत प्रकार से बटवारा हो (improper separation of privileges), आदि। भले ही जानकारीया प्रथक रूप मे न बाहर आए, लेकिन system का प्रयोग करके हमलावर, model को  utterances (उच्चारण) भेज सकता है एवं वह परिणामों का भी अवलोकन कर सकता है। जिसके परिणामस्वरूप वह  system prompt language मे मौजूद बहुत प्रकार की guardrails एवं formatting restrictions का पता लगा सकता है।

### जोखिम के सामान्य उदाहरण

#### 1. संवेदनशील कार्यक्षमता का प्रकटीकरण 
  System Prompt संवेदनशील जानकारी एवं कार्यक्षमताओ  को प्रकट कर सकता हैं, जैसे कि sensitive system architecture, API keys, database credentials, या user tokens आदि। 
  इनका प्रयोग हमलावरों द्वारा अनधिकृत पहुंच (unauthorized access) प्राप्त करने के लिए हो सकता हैं। उदाहरण के लिए, एक system Prompt जिसमें किसी tool के लिए प्रयोग किए जाने वाले डेटाबेस की जानकारी हो, जिससे की हमलावर SQL इंजेक्शन कर सकता हैं।
#### 2. आंतरिक नियमों का प्रकटीकरण
  Application के system Prompt से आंतरिक निर्णय लेने की प्रक्रियाओं के बारे में पता चल सकता हैं। यह जानकारी हमलावरों को application को समझने में सहायक है, जिससे की वह कमजोरीयो को exploit या application के नियंत्रणों को bypass कर सकता हैं। उदाहरण के लिए - एक बैंकिंग application मे एक चैटबॉट हैं, जिसमे system Prompt जानकारी को कुछ इस प्रकार से प्रकट करते हैं: 
    > "User के लिए लेनदेन की सीमा ko 5000 USD प्रति दिन निर्धारित कर दिया गया हैं। अब user के लिए कुल ऋण राशि 10,000 USD हैं"।
  इस जानकारी से हमलावर application के security controls को bypass करके, सीमा से अधिक लेनदेन या कुल ऋण राशि को बायपास करना जेसे दुर्भावनापूर्ण कार्य कर सकता है।
#### 3. फ़िल्टरिंग मानदंड का प्रकटीकरण
  एक system Prompt मॉडल को संवेदनशील सामग्री को फ़िल्टर या अस्वीकार करने के लिए कह सकता हैं। उदाहरण के लिए, एक मॉडल का system Prompt हो सकता हैं,
    > "यदि कोई user किसी अन्य user के बारे में जानकारी माँगता हैं, तो हमेशा उसे कहना-'क्षमा करें, मैं इस अनुरोध मे सहायता नहीं कर सकता'। "
#### 4. Permissions एवं  User Roles का प्रकटीकरण
  system Prompt आंतरिक role structures या application के permission levels को प्रकट कर सकता हैं। उदाहरण के लिए, एक system Prompt प्रकट कर सकता हैं,
    > "Admin user role रिकॉर्ड को संशोधित करने के लिए पूर्ण access प्रदान करता हैं।"
  यदि हमलावर को इन role-based permissions के बारे मे पता चल गया तो वह privilege escalation का  हमला कर सकता हैंं।

### रोकथाम एवं बचाव के लिये रणनीतियाँ

#### 1. system Prompt से संवेदनशील डेटा को अलग करें
  किसी भी संवेदनशील जानकारी (जैसे API keys, auth keys, database names, user roles, permission structure of application) को सीधे system prompt में न डाले। इसके बजाय, ऐसी जानकारी को उन system मे डाले जिनको मॉडल सीधे एक्सेस नहीं कर सकते।
#### 2. सख्त व्यवहार नियंत्रण के लिए system prompts पर निर्भरता से बचें
  चूंकि LLMs पर, Prompt इंजेक्शन जैसे हमलों का खतरा होते हैंं जो system Prompt को बदल सकते हैंं, इसलिए जहां संभव हो वहा मॉडल व्यवहार को नियंत्रित करने के लिए system Prompt का उपयोग करने से बचे।  इसके बजाय, इस कार्य के लिए LLM के अलावा बाहर वाले किसी अन्यsystem पर भरोसा करें।  उदाहरण के लिए, हानिकारक सामग्री का पता लगाना एवं रोकना बाहरी system में किया जा सकता है।
#### 3. Guardrails को लागू करें
  LLM के आस-पास ही guardrails के system को लागू करें।  जबकि एक मॉडल को विशेष व्यवहार के लिये  प्रशिक्षित करना प्रभावी हो सकता हैं, जैसे कि यह प्रशिक्षण देना कि वह अपने system Prompt को प्रकट नहीं करे,जबकि यह गारंटी नहीं हैं कि मॉडल हमेशा इसका पालन करेगा।  एक स्वतंत्र system जो की आउटपुट का निरीक्षण कर सके की क्या मॉडल अपेक्षाओं पर खड़ा उतर रहा हैं या नहीं, वह system Prompt निर्देशों के लिए बेहतर साबित हो सकता हैं।
#### 4. सुनिश्चित करें कि सुरक्षा नियंत्रण LLM से स्वतंत्र हो एवं ढंग से लागू हो
  महत्वपूर्ण नियंत्रण जैसे कि privilege separation, authorization bounds checks, आदि को ना ही system Prompt के माध्यम से या किसी अन्य प्रकार से भी LLM को ना दे। इन नियंत्रणों को deterministic (पता लगा सके), auditable manner (जाच सके) से होने चाहिए, लेकिन वर्तमान में LLMs इसके लिए अनुकूल नहीं हैंं। ऐसे मामलों में जहां कोई एजेंट कार्य कर रहा हैं, यदि उन कार्यों को विभिन्न स्तरों तक पहुंच (access) की आवश्यकता हैं, तो कई एजैंट्स का उपयोग किया जाना चाहिए, प्रत्येक को उसके कार्यों के अनुसार न्यूनतम privileges के साथ configure करना चाहिए।

### उदाहरण स्वरूप हमले के परिदृश्य

#### परिद्रश्य 1
   एक LLM के system Prompt मे एक tool के लिए प्रयोग मे आने वाले credentials डाले जाते हैं, इस LLM को इस tool का access होता है। यह  system Prompt हमलावर को लीक होता हैं, जो फिर अन्य उद्देश्यों के लिए इनका उपयोग कर सकता हैं।
#### परिदृश्य#2
  एक LLM के system prompt ने offensive content, external links, एवं code execution आदि को प्रतिबंधित कर रखा हैं। एक हमलावर इस system Prompt को प्राप्त कर किसी हमले 
  से इन निर्देशों को बायपास करके remote code execution कर सकता हैं।

### संबंधित लिंक

1. [SYSTEM PROMPT LEAK](https://x.com/elder_plinius/status/1801393358964994062): Pliny the prompter
2. [Prompt Leak](https://www.prompt.security/vulnerabilities/prompt-leak): Prompt Security
3. [chatgpt_system_prompt](https://github.com/LouisShark/chatgpt_system_prompt): LouisShark
4. [leaked-system-prompts](https://github.com/jujumilk3/leaked-system-prompts): Jujumilk3
5. [OpenAI Advanced Voice Mode System Prompt](https://x.com/Green_terminals/status/1839141326329360579): Green_Terminals

### संबंधित फ्रेमवर्क एवं  टैक्सोनॉमी

Infrastructure deployment, applied environment controls  तथा अन्य सर्वोत्तम उपायों से संबंधित व्यापक जानकारी, परिदृश्यों की रणनीतियों के लिए इस खंड का संदर्भ लें।

- [AML.T0051.000 - LLM Prompt Injection: Direct (Meta Prompt Extraction)](https://atlas.mitre.org/techniques/AML.T0051.000) **MITRE ATLAS**


