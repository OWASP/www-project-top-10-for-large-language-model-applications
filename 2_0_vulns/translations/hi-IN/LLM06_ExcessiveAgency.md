## LLM06:2025 Excessive Agency
## LLM06: 2025 अत्यधिक एजेंसी

### Description
### विवरण

An LLM-based system is often granted a degree of agency by its developer - the ability to call functions or interface with other systems via extensions (sometimes referred to as tools, skills or plugins by different vendors) to undertake actions in response to a prompt. The decision over which extension to invoke may also be delegated to an LLM 'agent' to dynamically determine based on input prompt or LLM output. Agent-based systems will typically make repeated calls to an LLM using output from previous invocations to ground and direct subsequent invocations.
एक एलएलएम -आधारित प्रणाली को अक्सर अपने डेवलपर द्वारा एजेंसी की एक डिग्री प्रदान की जाती है - एक्सटेंशन के माध्यम से अन्य प्रणालियों के साथ फ़ंक्शन या इंटरफ़ेस को कॉल करने की क्षमता (कभी -कभी अलग -अलग विक्रेताओं द्वारा उपकरण, कौशल या प्लगइन्स के रूप में संदर्भित) एक संकेत के जवाब में कार्रवाई करने के लिए। । इनपुट प्रॉम्प्ट या एलएलएम आउटपुट के आधार पर गतिशील रूप से निर्धारित करने के लिए किस एक्सटेंशन को आमंत्रित करने का निर्णय भी एक एलएलएम 'एजेंट' को दिया जा सकता है। एजेंट-आधारित सिस्टम आम तौर पर पिछले इनवोकेशन से ग्राउंड और डायरेक्ट बाद के इनवोकेशन तक आउटपुट का उपयोग करके एलएलएम को बार-बार कॉल करेंगे।

Excessive Agency is the vulnerability that enables damaging actions to be performed in response to unexpected, ambiguous or manipulated outputs from an LLM, regardless of what is causing the LLM to malfunction. Common triggers include:
* hallucination/confabulation caused by poorly-engineered benign prompts, or just a poorly-performing model;
* direct/indirect prompt injection from a malicious user, an earlier invocation of a malicious/compromised extension, or (in multi-agent/collaborative systems) a malicious/compromised peer agent.
अत्यधिक एजेंसी एक भेद्यता है जो एक एलएलएम से अप्रत्याशित, अस्पष्ट या हेरफेर किए गए आउटपुट के जवाब में किए जाने वाले कार्यों को हानिकारक कार्यों में सक्षम बनाती है, चाहे एलएलएम को खराबी के लिए क्या हो रहा है। सामान्य ट्रिगर में शामिल हैं:
* खराब-इंजीनियर सौम्य संकेतों के कारण मतिभ्रम/कन्फैब्यूलेशन, या सिर्फ एक खराब प्रदर्शन करने वाला मॉडल;
* एक दुर्भावनापूर्ण उपयोगकर्ता से प्रत्यक्ष/अप्रत्यक्ष त्वरित इंजेक्शन, एक दुर्भावनापूर्ण/समझौता किए गए एक्सटेंशन का पहले का आह्वान, या (मल्टी-एजेंट/सहयोगी प्रणालियों में) एक दुर्भावनापूर्ण/समझौता किया गया सहकर्मी एजेंट।

The root cause of Excessive Agency is typically one or more of:
* excessive functionality;
* excessive permissions;
* excessive autonomy.
अत्यधिक एजेंसी का मूल कारण आम तौर पर एक या अधिक होता है:
* अत्यधिक कार्यक्षमता;
* अत्यधिक अनुमतियाँ;
* अत्यधिक स्वायत्तता।

Excessive Agency can lead to a broad range of impacts across the confidentiality, integrity and availability spectrum, and is dependent on which systems an LLM-based app is able to interact with.
अत्यधिक एजेंसी गोपनीयता, अखंडता और उपलब्धता स्पेक्ट्रम में प्रभावों की एक विस्तृत श्रृंखला का नेतृत्व कर सकती है, और इस बात पर निर्भर है कि कौन से सिस्टम एक एलएलएम-आधारित ऐप के साथ बातचीत करने में सक्षम है।

Note: Excessive Agency differs from Insecure Output Handling which is concerned with insufficient scrutiny of LLM outputs.
नोट: अत्यधिक एजेंसी असुरक्षित आउटपुट हैंडलिंग से अलग है जो एलएलएम आउटपुट की अपर्याप्त जांच से संबंधित है।

### Common Examples of Risks
### जोखिमों के सामान्य उदाहरण

#### 1. Excessive Functionality
  An LLM agent has access to extensions which include functions that are not needed for the intended operation of the system. For example, a developer needs to grant an LLM agent the ability to read documents from a repository, but the 3rd-party extension they choose to use also includes the ability to modify and delete documents.
#### 2. Excessive Functionality
  An extension may have been trialled during a development phase and dropped in favor of a better alternative, but the original plugin remains available to the LLM agent.
#### 3. Excessive Functionality
  An LLM plugin with open-ended functionality fails to properly filter the input instructions for commands outside what's necessary for the intended operation of the application. E.g., an extension to run one specific shell command fails to properly prevent other shell commands from being executed.
#### 4. Excessive Permissions
  An LLM extension has permissions on downstream systems that are not needed for the intended operation of the application. E.g., an extension intended to read data connects to a database server using an identity that not only has SELECT permissions, but also UPDATE, INSERT and DELETE permissions.
#### 5. Excessive Permissions
  An LLM extension that is designed to perform operations in the context of an individual user accesses downstream systems with a generic high-privileged identity. E.g., an extension to read the current user's document store connects to the document repository with a privileged account that has access to files belonging to all users.
#### 6. Excessive Autonomy
  An LLM-based application or extension fails to independently verify and approve high-impact actions. E.g., an extension that allows a user's documents to be deleted performs deletions without any confirmation from the user.
#### 1। अत्यधिक कार्यक्षमता
  एक एलएलएम एजेंट के पास एक्सटेंशन तक पहुंच होती है जिसमें ऐसे कार्य शामिल होते हैं जो सिस्टम के इच्छित संचालन के लिए आवश्यक नहीं होते हैं। उदाहरण के लिए, एक डेवलपर को एक एलएलएम एजेंट को एक रिपॉजिटरी से दस्तावेजों को पढ़ने की क्षमता प्रदान करने की आवश्यकता होती है, लेकिन 3-पार्टी एक्सटेंशन जो वे उपयोग करने के लिए चुनते हैं, उनमें दस्तावेजों को संशोधित करने और हटाने की क्षमता भी शामिल है।
#### 2। अत्यधिक कार्यक्षमता
  एक विस्तार को एक विकास चरण के दौरान परीक्षण किया जा सकता है और एक बेहतर विकल्प के पक्ष में गिरा दिया गया है, लेकिन मूल प्लगइन एलएलएम एजेंट के लिए उपलब्ध है।
#### 3। अत्यधिक कार्यक्षमता
  ओपन-एंडेड कार्यक्षमता के साथ एक एलएलएम प्लगइन एप्लिकेशन के इच्छित संचालन के लिए आवश्यक है कि बाहर के आदेशों के लिए इनपुट निर्देशों को ठीक से फ़िल्टर करने में विफल रहता है। उदाहरण के लिए, एक विशिष्ट शेल कमांड चलाने के लिए एक एक्सटेंशन अन्य शेल कमांड को निष्पादित होने से ठीक से रोकने में विफल रहता है।
#### 4। अत्यधिक अनुमतियाँ
  एक एलएलएम एक्सटेंशन में डाउनस्ट्रीम सिस्टम पर अनुमति है जो एप्लिकेशन के इच्छित संचालन के लिए आवश्यक नहीं है। उदाहरण के लिए, डेटा पढ़ने के लिए एक एक्सटेंशन एक पहचान का उपयोग करके डेटाबेस सर्वर से कनेक्ट करता है, जिसमें न केवल चयन अनुमतियाँ हैं, बल्कि अनुमतियों को अपडेट, सम्मिलित और हटा दें।
#### 5। अत्यधिक अनुमतियाँ
  एक एलएलएम एक्सटेंशन जो एक व्यक्तिगत उपयोगकर्ता के संदर्भ में संचालन करने के लिए डिज़ाइन किया गया है, एक सामान्य उच्च-विशेषाधिकार प्राप्त पहचान के साथ डाउनस्ट्रीम सिस्टम का उपयोग करता है। उदाहरण के लिए, वर्तमान उपयोगकर्ता के दस्तावेज़ स्टोर को पढ़ने के लिए एक एक्सटेंशन एक विशेषाधिकार प्राप्त खाते के साथ दस्तावेज़ रिपॉजिटरी से जुड़ता है, जिसमें सभी उपयोगकर्ताओं से संबंधित फ़ाइलों तक पहुंच है।
#### 6। अत्यधिक स्वायत्तता
  एक एलएलएम-आधारित एप्लिकेशन या एक्सटेंशन स्वतंत्र रूप से उच्च-प्रभाव कार्यों को सत्यापित करने और अनुमोदन करने में विफल रहता है। जैसे, एक एक्सटेंशन जो उपयोगकर्ता के दस्तावेजों को हटाए जाने की अनुमति देता है, उपयोगकर्ता से किसी भी पुष्टि के बिना विलोपन करता है।

### Prevention and Mitigation Strategies
### रोकथाम और शमन रणनीतियाँ

The following actions can prevent Excessive Agency:
निम्नलिखित क्रियाएं अत्यधिक एजेंसी को रोक सकती हैं:

#### 1. Minimize extensions
  Limit the extensions that LLM agents are allowed to call to only the minimum necessary. For example, if an LLM-based system does not require the ability to fetch the contents of a URL then such an extension should not be offered to the LLM agent.
#### 2. Minimize extension functionality
  Limit the functions that are implemented in LLM extensions to the minimum necessary. For example, an extension that accesses a user's mailbox to summarise emails may only require the ability to read emails, so the extension should not contain other functionality such as deleting or sending messages.
#### 3. Avoid open-ended extensions
  Avoid the use of open-ended extensions where possible (e.g., run a shell command, fetch a URL, etc.) and use extensions with more granular functionality. For example, an LLM-based app may need to write some output to a file. If this were implemented using an extension to run a shell function then the scope for undesirable actions is very large (any other shell command could be executed). A more secure alternative would be to build a specific file-writing extension that only implements that specific functionality.
#### 4. Minimize extension permissions
  Limit the permissions that LLM extensions are granted to other systems to the minimum necessary in order to limit the scope of undesirable actions. For example, an LLM agent that uses a product database in order to make purchase recommendations to a customer might only need read access to a 'products' table; it should not have access to other tables, nor the ability to insert, update or delete records. This should be enforced by applying appropriate database permissions for the identity that the LLM extension uses to connect to the database.
#### 5. Execute extensions in user's context
  Track user authorization and security scope to ensure actions taken on behalf of a user are executed on downstream systems in the context of that specific user, and with the minimum privileges necessary. For example, an LLM extension that reads a user's code repo should require the user to authenticate via OAuth and with the minimum scope required.
#### 6. Require user approval
  Utilise human-in-the-loop control to require a human to approve high-impact actions before they are taken. This may be implemented in a downstream system (outside the scope of the LLM application) or within the LLM extension itself. For example, an LLM-based app that creates and posts social media content on behalf of a user should include a user approval routine within the extension that implements the 'post' operation.
#### 7. Complete mediation
  Implement authorization in downstream systems rather than relying on an LLM to decide if an action is allowed or not. Enforce the complete mediation principle so that all requests made to downstream systems via extensions are validated against security policies.
#### 8. Sanitise LLM inputs and outputs
  Follow secure coding best practice, such as applying OWASP’s recommendations in ASVS (Application Security Verification Standard), with a particularly strong focus on input sanitisation. Use Static Application Security Testing (SAST) and Dynamic and Interactive application testing (DAST, IAST) in development pipelines.
#### 1। एक्सटेंशन को कम से कम करें
  उन एक्सटेंशन को सीमित करें जो एलएलएम एजेंटों को केवल न्यूनतम आवश्यक पर कॉल करने की अनुमति है। उदाहरण के लिए, यदि एलएलएम-आधारित प्रणाली को यूआरएल की सामग्री को लाने की क्षमता की आवश्यकता नहीं होती है, तो इस तरह के एक्सटेंशन को एलएलएम एजेंट को पेश नहीं किया जाना चाहिए।
#### 2। एक्सटेंशन कार्यक्षमता को कम करें
  एलएलएम एक्सटेंशन में लागू किए गए कार्यों को न्यूनतम आवश्यक तक सीमित करें। उदाहरण के लिए, एक एक्सटेंशन जो ईमेल को सारांशित करने के लिए उपयोगकर्ता के मेलबॉक्स तक पहुंचता है, केवल ईमेल पढ़ने की क्षमता की आवश्यकता हो सकती है, इसलिए एक्सटेंशन में अन्य कार्यक्षमता नहीं होनी चाहिए जैसे कि संदेश हटाना या भेजना।
#### 3। ओपन-एंडेड एक्सटेंशन से बचें
  जहां संभव हो, ओपन-एंडेड एक्सटेंशन के उपयोग से बचें (जैसे, एक शेल कमांड चलाएं, एक URL, आदि प्राप्त करें) और अधिक दानेदार कार्यक्षमता के साथ एक्सटेंशन का उपयोग करें। उदाहरण के लिए, एक एलएलएम-आधारित ऐप को फ़ाइल में कुछ आउटपुट लिखने की आवश्यकता हो सकती है। यदि यह एक शेल फ़ंक्शन को चलाने के लिए एक एक्सटेंशन का उपयोग करके लागू किया गया था, तो अवांछनीय कार्यों के लिए गुंजाइश बहुत बड़ी है (किसी भी अन्य शेल कमांड को निष्पादित किया जा सकता है)। एक अधिक सुरक्षित विकल्प एक विशिष्ट फ़ाइल-लेखन एक्सटेंशन का निर्माण करना होगा जो केवल उस विशिष्ट कार्यक्षमता को लागू करता है।
#### 4। एक्सटेंशन अनुमतियों को कम करें
  अनुमतियों को सीमित करें कि अवांछनीय कार्यों के दायरे को सीमित करने के लिए एलएलएम एक्सटेंशन अन्य प्रणालियों को न्यूनतम आवश्यक तक प्रदान किए जाते हैं। उदाहरण के लिए, एक एलएलएम एजेंट जो किसी ग्राहक को खरीद सिफारिशें करने के लिए उत्पाद डेटाबेस का उपयोग करता है, उसे केवल 'उत्पादों' की तालिका तक पहुंच की आवश्यकता हो सकती है; इसमें अन्य तालिकाओं तक पहुंच नहीं होनी चाहिए, न ही रिकॉर्ड डालने, अपडेट करने या हटाने की क्षमता। यह पहचान के लिए उपयुक्त डेटाबेस अनुमतियों को लागू करके लागू किया जाना चाहिए जो एलएलएम एक्सटेंशन डेटाबेस से कनेक्ट करने के लिए उपयोग करता है।
#### 5। उपयोगकर्ता के संदर्भ में एक्सटेंशन निष्पादित करें
  उपयोगकर्ता की ओर से किए गए कार्यों को सुनिश्चित करने के लिए उपयोगकर्ता प्राधिकरण और सुरक्षा गुंजाइश ट्रैक करें, उस विशिष्ट उपयोगकर्ता के संदर्भ में डाउनस्ट्रीम सिस्टम पर निष्पादित किए जाते हैं, और आवश्यक न्यूनतम विशेषाधिकारों के साथ। उदाहरण के लिए, एक एलएलएम एक्सटेंशन जो उपयोगकर्ता के कोड रेपो को पढ़ता है, को उपयोगकर्ता को OAUTH के माध्यम से प्रमाणित करने की आवश्यकता होनी चाहिए और न्यूनतम गुंजाइश की आवश्यकता होती है।
#### 6। उपयोगकर्ता अनुमोदन की आवश्यकता है
  मानव-इन-द-लूप नियंत्रण का उपयोग करके एक मानव को उच्च-प्रभाव कार्रवाई को मंजूरी देने के लिए आवश्यकता होती है, इससे पहले कि वे लिए जाते हैं। यह एक डाउनस्ट्रीम सिस्टम (एलएलएम एप्लिकेशन के दायरे के बाहर) या एलएलएम एक्सटेंशन के भीतर ही लागू किया जा सकता है। उदाहरण के लिए, एक एलएलएम-आधारित ऐप जो किसी उपयोगकर्ता की ओर से सोशल मीडिया सामग्री बनाता है और पोस्ट करता है, उस एक्सटेंशन के भीतर एक उपयोगकर्ता अनुमोदन दिनचर्या को शामिल करना चाहिए जो 'पोस्ट' ऑपरेशन को लागू करता है।
#### 7। पूर्ण मध्यस्थता
  एक कार्रवाई की अनुमति है या नहीं, यह तय करने के लिए एलएलएम पर भरोसा करने के बजाय डाउनस्ट्रीम सिस्टम में प्राधिकरण को लागू करें। पूर्ण मध्यस्थता सिद्धांत को लागू करें ताकि एक्सटेंशन के माध्यम से डाउनस्ट्रीम सिस्टम के लिए किए गए सभी अनुरोध सुरक्षा नीतियों के खिलाफ मान्य हों।
#### 8। एलएलएम इनपुट और आउटपुट को सैनिटाइज़ करें
  सुरक्षित कोडिंग सर्वोत्तम अभ्यास का पालन करें, जैसे कि ASVS (एप्लिकेशन सुरक्षा सत्यापन मानक) में OWASP की सिफारिशों को लागू करना, इनपुट Sanitisation पर विशेष रूप से मजबूत फोकस के साथ। विकास पाइपलाइनों में स्टेटिक एप्लिकेशन सिक्योरिटी टेस्टिंग (SAST) और डायनेमिक एंड इंटरएक्टिव एप्लिकेशन टेस्टिंग (DAST, IAST) का उपयोग करें।

The following options will not prevent Excessive Agency, but can limit the level of damage caused:
निम्नलिखित विकल्प अत्यधिक एजेंसी को नहीं रोकेंगे, लेकिन नुकसान के स्तर को सीमित कर सकते हैं:

- Log and monitor the activity of LLM extensions and downstream systems to identify where undesirable actions are taking place, and respond accordingly.
- Implement rate-limiting to reduce the number of undesirable actions that can take place within a given time period, increasing the opportunity to discover undesirable actions through monitoring before significant damage can occur.
- एलएलएम एक्सटेंशन और डाउनस्ट्रीम सिस्टम की गतिविधि को लॉग इन करें और यह पहचानने के लिए कि अवांछनीय क्रियाएं कहां हो रही हैं, और तदनुसार जवाब दें।
- किसी निश्चित समय अवधि के भीतर होने वाली अवांछनीय कार्यों की संख्या को कम करने के लिए दर-सीमित करना लागू करें, महत्वपूर्ण क्षति होने से पहले निगरानी के माध्यम से अवांछनीय कार्यों की खोज करने का अवसर बढ़ाएं।

### Example Attack Scenarios
### उदाहरण हमले परिदृश्य

An LLM-based personal assistant app is granted access to an individual’s mailbox via an extension in order to summarise the content of incoming emails. To achieve this functionality, the extension requires the ability to read messages, however the plugin that the system developer has chosen to use also contains functions for sending messages. Additionally, the app is vulnerable to an indirect prompt injection attack, whereby a maliciously-crafted incoming email tricks the LLM into commanding the agent to scan the user's inbox for senitive information and forward it to the attacker's email address. This could be avoided by:
* eliminating excessive functionality by using an extension that only implements mail-reading capabilities,
* eliminating excessive permissions by authenticating to the user's email service via an OAuth session with a read-only scope, and/or
* eliminating excessive autonomy by requiring the user to manually review and hit 'send' on every mail drafted by the LLM extension.
एक एलएलएम-आधारित व्यक्तिगत सहायक ऐप को आने वाले ईमेल की सामग्री को संक्षेप में प्रस्तुत करने के लिए एक्सटेंशन के माध्यम से किसी व्यक्ति के मेलबॉक्स तक पहुंच प्रदान की जाती है। इस कार्यक्षमता को प्राप्त करने के लिए, एक्सटेंशन को संदेशों को पढ़ने की क्षमता की आवश्यकता होती है, हालांकि सिस्टम डेवलपर ने उपयोग करने के लिए जो प्लगइन चुना है, उसमें संदेश भेजने के लिए फ़ंक्शन भी शामिल हैं। इसके अतिरिक्त, ऐप एक अप्रत्यक्ष शीघ्र इंजेक्शन हमले के लिए असुरक्षित है, जिससे एक दुर्भावनापूर्ण रूप से तैयार की गई आने वाली आने वाली ईमेल एलएलएम को ट्रिक करने के लिए एजेंट को कमांड करने के लिए उपयोगकर्ता के इनबॉक्स को सेनेटिटिव जानकारी के लिए स्कैन करने के लिए कमांडिंग करता है और इसे हमलावर के ईमेल पते पर अग्रेषित करता है। इससे बचा जा सकता है:
* एक एक्सटेंशन का उपयोग करके अत्यधिक कार्यक्षमता को समाप्त करना जो केवल मेल-रीडिंग क्षमताओं को लागू करता है,
* एक रीड-ओनली स्कोप के साथ एक OAUTH सत्र के माध्यम से उपयोगकर्ता की ईमेल सेवा को प्रमाणित करके अत्यधिक अनुमतियों को समाप्त करना, और/या
* उपयोगकर्ता को मैन्युअल रूप से समीक्षा करने और एलएलएम एक्सटेंशन द्वारा तैयार किए गए प्रत्येक मेल पर 'सेंड' को हिट करने की आवश्यकता के द्वारा अत्यधिक स्वायत्तता को समाप्त करना।

Alternatively, the damage caused could be reduced by implementing rate limiting on the mail-sending interface.
वैकल्पिक रूप से, मेल-सेंडिंग इंटरफ़ेस पर दर सीमित दर को लागू करके नुकसान को कम किया जा सकता है।

### Reference Links
### संदर्भ लिंक

1. [Slack AI data exfil from private channels](https://promptarmor.substack.com/p/slack-ai-data-exfiltration-from-private): **PromptArmor**
2. [Rogue Agents: Stop AI From Misusing Your APIs](https://www.twilio.com/en-us/blog/rogue-ai-agents-secure-your-apis): **Twilio**
3. [Embrace the Red: Confused Deputy Problem](https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./): **Embrace The Red**
4. [NeMo-Guardrails: Interface guidelines](https://github.com/NVIDIA/NeMo-Guardrails/blob/main/docs/security/guidelines.md): **NVIDIA Github**
6. [Simon Willison: Dual LLM Pattern](https://simonwillison.net/2023/Apr/25/dual-llm-pattern/): **Simon Willison**
7. [Sandboxing Agentic AI Workflows with WebAssembly](https://developer.nvidia.com/blog/sandboxing-agentic-ai-workflows-with-webassembly/) **NVIDIA, Joe Lucas**

1। [निजी चैनलों से स्लैक एआई डेटा एक्सफ़िल]
2।
3। [लाल गले लगाओ: भ्रमित उप समस्या] **
4।
6।
7।

