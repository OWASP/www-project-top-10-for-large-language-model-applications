## LLM03:2025 Supply Chain
## LLM03: 2025 आपूर्ति श्रृंखला

### Description
### विवरण

LLM supply chains are susceptible to various vulnerabilities, which can affect the integrity of training data, models, and deployment platforms. These risks can result in biased outputs, security breaches, or system failures. While traditional software vulnerabilities focus on issues like code flaws and dependencies, in ML the risks also extend to third-party pre-trained models and data.
एलएलएम आपूर्ति श्रृंखला विभिन्न कमजोरियों के लिए अतिसंवेदनशील होती है, जो प्रशिक्षण डेटा, मॉडल और तैनाती प्लेटफार्मों की अखंडता को प्रभावित कर सकती है। इन जोखिमों के परिणामस्वरूप पक्षपाती आउटपुट, सुरक्षा उल्लंघन या सिस्टम विफलताएं हो सकती हैं। जबकि पारंपरिक सॉफ्टवेयर कमजोरियां कोड की खामियों और निर्भरता जैसे मुद्दों पर ध्यान केंद्रित करती हैं, एमएल में जोखिम भी तीसरे पक्ष के पूर्व-प्रशिक्षित मॉडल और डेटा तक विस्तारित होते हैं।

These external elements can be manipulated through tampering or poisoning attacks.
इन बाहरी तत्वों को छेड़छाड़ या जहर के हमलों के माध्यम से हेरफेर किया जा सकता है।

Creating LLMs is a specialized task that often depends on third-party models. The rise of open-access LLMs and new fine-tuning methods like "LoRA" (Low-Rank Adaptation)  and "PEFT" (Parameter-Efficient Fine-Tuning), especially on platforms like Hugging Face, introduce new supply-chain risks. Finally, the emergence of on-device LLMs increase the attack surface and supply-chain risks for LLM applications.
LLMS बनाना एक विशेष कार्य है जो अक्सर तीसरे पक्ष के मॉडल पर निर्भर करता है। ओपन-एक्सेस एलएलएम और "लोरा" (लो-रैंक अनुकूलन) और "पीईएफटी" (पैरामीटर-कुशल फाइन-ट्यूनिंग) जैसे नए फाइन-ट्यूनिंग विधियों का उदय, विशेष रूप से चेहरे जैसे प्लेटफार्मों पर, नए आपूर्ति-श्रृंखला जोखिमों को पेश करता है। अंत में, ऑन-डिवाइस एलएलएम के उद्भव ने एलएलएम अनुप्रयोगों के लिए हमले की सतह और आपूर्ति-श्रृंखला जोखिमों को बढ़ाया।

Some of the risks discussed here are also discussed in "LLM04 Data and Model Poisoning." This entry focuses on the supply-chain aspect of the risks.
A simple threat model can be found [here](https://github.com/jsotiro/ThreatModels/blob/main/LLM%20Threats-LLM%20Supply%20Chain.png).
यहां चर्चा किए गए कुछ जोखिमों पर "LLM04 डेटा और मॉडल पॉइज़निंग" में भी चर्चा की गई है। यह प्रविष्टि जोखिमों की आपूर्ति-श्रृंखला पहलू पर केंद्रित है।
एक साधारण खतरा मॉडल पाया जा सकता है [यहाँ] (https://github.com/jsotiro/threatmodels/blob/main/llm%20threats-llm%20supply%20chain.png)।

### Common Examples of Risks
### जोखिमों के सामान्य उदाहरण

#### 1. Traditional Third-party Package Vulnerabilities
  Such as outdated or deprecated components, which attackers can exploit to compromise LLM applications. This is similar to "A06:2021 – Vulnerable and Outdated Components" with increased risks when components are used during model development or finetuning.
  (Ref. link: [A06:2021 – Vulnerable and Outdated Components](https://owasp.org/Top10/A06_2021-Vulnerable_and_Outdated_Components/))
#### 2. Licensing Risks
  AI development often involves diverse software and dataset licenses, creating risks if not properly managed. Different open-source and proprietary licenses impose varying legal requirements. Dataset licenses may restrict usage, distribution, or commercialization.
#### 3. Outdated or Deprecated Models
  Using outdated or deprecated models that are no longer maintained leads to security issues.
#### 4. Vulnerable Pre-Trained Model
  Models are binary black boxes and unlike open source, static inspection can offer little to security assurances. Vulnerable pre-trained models can contain hidden biases, backdoors, or other malicious features that have not been identified through  the safety evaluations of model repository. Vulnerable models can be created by both poisoned datasets and direct model tampering using techniques such as ROME also known as lobotomisation.
#### 5. Weak Model Provenance
  Currently there are no strong provenance assurances in published models. Model Cards and associated documentation provide model information and relied upon users, but they offer no guarantees on the origin of the model. An attacker can compromise supplier account on a model repo or create a similar one and combine it with social engineering techniques to compromise the supply-chain of an LLM application.
#### 6. Vulnerable LoRA adapters
  LoRA is a popular fine-tuning technique that enhances modularity by allowing pre-trained layers to be bolted onto an existing LLM. The method increases efficiency but create new risks, where a malicious LorA adapter compromises the integrity and security of the pre-trained base model. This can happen both in collaborative model merge environments but also exploiting the support for LoRA from popular inference deployment platforms such as vLMM and OpenLLM where adapters can be downloaded and applied to a deployed model.
#### 7. Exploit Collaborative Development Processes
  Collaborative model merge and model handling services (e.g. conversions) hosted in shared environments can be exploited to introduce vulnerabilities in shared models. Model merging is is very popular on Hugging Face with model-merged models topping the OpenLLM leaderboard and can be exploited to bypass reviews. Similarly, services such as conversation bot have been proved to be vulnerable to maniputalion and introduce malicious code in models.
#### 8. LLM Model on Device supply-chain vulnerabilities
  LLM models on device increase the supply attack surface with compromised manufactured processes and exploitation of device OS or fimware vulnerabilities to compromise models. Attackers can reverse engineer and re-package applications with tampered models.
#### 9. Unclear T&Cs and Data Privacy Policies
  Unclear T&Cs and data privacy policies of the model operators lead to the application's sensitive data being used for model training and subsequent sensitive information exposure. This may also apply to risks from using copyrighted material by the model supplier.
#### 1। पारंपरिक तृतीय-पक्ष पैकेज कमजोरियां
  जैसे कि पुराने या पदावनत घटक, जो हमलावर एलएलएम अनुप्रयोगों से समझौता करने के लिए शोषण कर सकते हैं। यह "A06: 2021 - कमजोर और पुराने घटकों" के समान है जब बढ़े हुए जोखिमों के साथ जब घटक का उपयोग मॉडल विकास या फ़िनिट्यूनिंग के दौरान किया जाता है।
  (Ref।
#### 2। लाइसेंसिंग जोखिम
  AI विकास में अक्सर विविध सॉफ़्टवेयर और डेटासेट लाइसेंस शामिल होते हैं, जो ठीक से प्रबंधित नहीं होने पर जोखिम पैदा करते हैं। विभिन्न ओपन-सोर्स और मालिकाना लाइसेंस अलग-अलग कानूनी आवश्यकताओं को लागू करते हैं। डेटासेट लाइसेंस उपयोग, वितरण या व्यावसायीकरण को प्रतिबंधित कर सकते हैं।
#### 3। पुराना या पदावनत मॉडल
  पुराने या पदावनत मॉडल का उपयोग करना जो अब बनाए नहीं रखा जाता है, सुरक्षा के मुद्दों की ओर जाता है।
#### 4। कमजोर पूर्व-प्रशिक्षित मॉडल
  मॉडल बाइनरी ब्लैक बॉक्स हैं और खुले स्रोत के विपरीत, स्थिर निरीक्षण सुरक्षा आश्वासन के लिए बहुत कम पेश कर सकता है। कमजोर पूर्व-प्रशिक्षित मॉडल में छिपे हुए पूर्वाग्रह, बैकडोर या अन्य दुर्भावनापूर्ण विशेषताएं हो सकती हैं जिन्हें मॉडल रिपॉजिटरी के सुरक्षा मूल्यांकन के माध्यम से पहचाना नहीं गया है। कमजोर मॉडल दोनों जहर वाले डेटासेट और प्रत्यक्ष मॉडल छेड़छाड़ दोनों द्वारा बनाया जा सकता है, जैसे रोम जैसी तकनीकों का उपयोग करके इसे लोबोटोमाइजेशन के रूप में भी जाना जाता है।
#### 5। कमजोर मॉडल सिद्धता
  वर्तमान में प्रकाशित मॉडल में कोई मजबूत सिद्ध आश्वासन नहीं हैं। मॉडल कार्ड और संबंधित दस्तावेज मॉडल की जानकारी प्रदान करते हैं और उपयोगकर्ताओं पर भरोसा करते हैं, लेकिन वे मॉडल की उत्पत्ति पर कोई गारंटी नहीं देते हैं। एक हमलावर एक मॉडल रेपो पर आपूर्तिकर्ता खाते से समझौता कर सकता है या एक समान बना सकता है और इसे एलएलएम एप्लिकेशन की आपूर्ति-श्रृंखला से समझौता करने के लिए सोशल इंजीनियरिंग तकनीकों के साथ जोड़ सकता है।
#### 6। कमजोर लोरा एडेप्टर
  लोरा एक लोकप्रिय फाइन-ट्यूनिंग तकनीक है जो पूर्व-प्रशिक्षित परतों को मौजूदा एलएलएम पर बोल्ट करने की अनुमति देकर मॉड्यूलरिटी को बढ़ाती है। विधि दक्षता बढ़ाती है लेकिन नए जोखिम पैदा करती है, जहां एक दुर्भावनापूर्ण लोरा एडाप्टर पूर्व-प्रशिक्षित बेस मॉडल की अखंडता और सुरक्षा से समझौता करता है। यह सहयोगी मॉडल मर्ज वातावरण में दोनों हो सकता है, लेकिन वीएलएमएम और ओपनएलएलएम जैसे लोकप्रिय अनुमान परिनियोजन प्लेटफार्मों से लोरा के लिए समर्थन का शोषण भी कर सकता है जहां एडेप्टर को डाउनलोड किया जा सकता है और एक तैनात मॉडल पर लागू किया जा सकता है।
#### 7। सहयोगी विकास प्रक्रियाओं का शोषण करें
  साझा वातावरण में होस्ट किए गए सहयोगी मॉडल मर्ज और मॉडल हैंडलिंग सेवाओं (जैसे रूपांतरण) को साझा मॉडल में कमजोरियों को पेश करने के लिए शोषण किया जा सकता है। मॉडल मर्जिंग OpenLLM लीडरबोर्ड में टॉप करने वाले मॉडल-विलंबित मॉडल के साथ चेहरे को गले लगाने के लिए बहुत लोकप्रिय है और समीक्षाओं को बायपास करने के लिए शोषण किया जा सकता है। इसी तरह, वार्तालाप बॉट जैसी सेवाओं को मैनिपुटालियन के लिए असुरक्षित साबित किया गया है और मॉडल में दुर्भावनापूर्ण कोड पेश किया गया है।
#### 8। डिवाइस आपूर्ति-श्रृंखला कमजोरियों पर एलएलएम मॉडल
  डिवाइस पर एलएलएम मॉडल समझौता निर्मित प्रक्रियाओं के साथ आपूर्ति हमले की सतह को बढ़ाते हैं और मॉडल से समझौता करने के लिए डिवाइस ओएस या फिमवेयर कमजोरियों के शोषण। हमलावर छेड़छाड़ किए गए मॉडल के साथ इंजीनियर और फिर से पैकेज अनुप्रयोगों को रिवर्स कर सकते हैं।
#### 9। अस्पष्ट टी एंड सीएस और डेटा गोपनीयता नीतियां
  मॉडल ऑपरेटरों की अस्पष्ट टी एंड सीएस और डेटा गोपनीयता नीतियां एप्लिकेशन के संवेदनशील डेटा का उपयोग मॉडल प्रशिक्षण और बाद में संवेदनशील जानकारी एक्सपोज़र के लिए उपयोग की जा रही हैं। यह मॉडल आपूर्तिकर्ता द्वारा कॉपीराइट सामग्री का उपयोग करने से जोखिमों पर भी लागू हो सकता है।

### Prevention and Mitigation Strategies
### रोकथाम और शमन रणनीतियाँ

1. Carefully vet data sources and suppliers, including T&Cs and their privacy policies, only using trusted suppliers. Regularly review and audit supplier Security and Access, ensuring no changes in their security posture or T&Cs.
2. Understand and apply the mitigations found in the OWASP Top Ten's "A06:2021 – Vulnerable and Outdated Components." This includes vulnerability scanning, management, and patching components. For development environments with access to sensitive data, apply these controls in those environments, too.
  (Ref. link: [A06:2021 – Vulnerable and Outdated Components](https://owasp.org/Top10/A06_2021-Vulnerable_and_Outdated_Components/))
3. Apply comprehensive AI Red Teaming and Evaluations when selecting a third party model. Decoding Trust is an example of a Trustworthy AI benchmark for LLMs but models can finetuned to by pass published benchmarks. Use extensive AI Red Teaming to evaluate the model, especially in the use cases you are planning to use the model for.
4. Maintain an up-to-date inventory of components using a Software Bill of Materials (SBOM) to ensure you have an up-to-date, accurate, and signed inventory, preventing tampering with deployed packages. SBOMs can be used to detect and alert for new, zero-date vulnerabilities quickly. AI BOMs and ML SBOMs are an emerging area and you should evaluate options starting with OWASP CycloneDX
5. To mitigate AI licensing risks, create an inventory of all types of licenses involved using BOMs and conduct regular audits of all software, tools, and datasets, ensuring compliance and transparency through BOMs. Use automated license management tools for real-time monitoring and train teams on licensing models. Maintain detailed licensing documentation in BOMs and leverage tools such as [Dyana](https://github.com/dreadnode/dyana) to perform dynamic analysis of third-party software.
6. Only use models from verifiable sources and use third-party model integrity checks with signing and file hashes to compensate for the lack of strong model provenance. Similarly, use code signing for externally supplied code.
7. Implement strict monitoring and auditing practices for collaborative model development environments to prevent and quickly detect any abuse. "HuggingFace SF_Convertbot Scanner" is an example of automated scripts to use.
  (Ref. link: [HuggingFace SF_Convertbot Scanner](https://gist.github.com/rossja/d84a93e5c6b8dd2d4a538aa010b29163))
8. Anomaly detection and adversarial robustness tests on supplied models and data can help detect tampering and poisoning as discussed in "LLM04 Data and Model Poisoning; ideally, this should be part of MLOps and LLM pipelines; however, these are emerging techniques and may be easier to implement as part of red teaming exercises.
9. Implement a patching policy to mitigate vulnerable or outdated components. Ensure the application relies on a maintained version of APIs and underlying model.
10. Encrypt models deployed at AI edge with integrity checks and use vendor attestation APIs to prevent tampered apps and models and terminate applications of unrecognized firmware.
1। ध्यान से डेटा स्रोतों और आपूर्तिकर्ताओं, जिसमें टी एंड सीएस और उनकी गोपनीयता नीतियों सहित, केवल विश्वसनीय आपूर्तिकर्ताओं का उपयोग करते हैं। नियमित रूप से समीक्षा और ऑडिट आपूर्तिकर्ता सुरक्षा और पहुंच, उनके सुरक्षा मुद्रा या टी एंड सीएस में कोई बदलाव नहीं करना।
2। OWASP टॉप टेन के "A06: 2021 - कमजोर और पुराने घटकों" में पाए गए माइटिगेशन को समझें और लागू करें। इसमें भेद्यता स्कैनिंग, प्रबंधन और पैचिंग घटक शामिल हैं। संवेदनशील डेटा तक पहुंच के साथ विकास के वातावरण के लिए, इन नियंत्रणों को उन वातावरणों में भी लागू करें।
  (Ref।
3। तीसरे पक्ष के मॉडल का चयन करते समय व्यापक एआई रेड टीमिंग और मूल्यांकन लागू करें। डिकोडिंग ट्रस्ट LLMS के लिए एक भरोसेमंद AI बेंचमार्क का एक उदाहरण है, लेकिन मॉडल पास प्रकाशित बेंचमार्क द्वारा फ़िनेट्यून कर सकते हैं। मॉडल का मूल्यांकन करने के लिए व्यापक एआई रेड टीमिंग का उपयोग करें, विशेष रूप से उपयोग के मामलों में आप मॉडल का उपयोग करने की योजना बना रहे हैं।
4। यह सुनिश्चित करने के लिए कि आपके पास एक अप-टू-डेट, सटीक और हस्ताक्षरित इन्वेंट्री है, जो कि तैनात पैकेजों के साथ छेड़छाड़ को रोकने के लिए, एक सॉफ्टवेयर बिल (SBOM) का उपयोग करके घटकों की एक अप-टू-डेट इन्वेंट्री बनाए रखें। SBOMs का उपयोग नए, शून्य-तिथि कमजोरियों के लिए जल्दी से पता लगाने और सतर्क करने के लिए किया जा सकता है। AI BOMS और ML SBOMs एक उभरता हुआ क्षेत्र है और आपको OWASP Cyclonedx के साथ शुरू होने वाले विकल्पों का मूल्यांकन करना चाहिए
5। AI लाइसेंसिंग जोखिमों को कम करने के लिए, BOM का उपयोग करके शामिल सभी प्रकार के लाइसेंसों की एक सूची बनाएं और BOM के माध्यम से अनुपालन और पारदर्शिता सुनिश्चित करते हुए, सभी सॉफ़्टवेयर, टूल और डेटासेट के नियमित ऑडिट का संचालन करें। वास्तविक समय की निगरानी के लिए स्वचालित लाइसेंस प्रबंधन उपकरण का उपयोग करें और लाइसेंसिंग मॉडल पर टीमों को प्रशिक्षित करें। बीओएम और लीवरेज टूल जैसे [डायना] (https://github.com/dreadnode/dyana) में विस्तृत लाइसेंसिंग प्रलेखन बनाए रखें, ताकि तृतीय-पत्र सॉफ़्टवेयर का गतिशील विश्लेषण किया जा सके।
6। केवल सत्यापित स्रोतों से मॉडल का उपयोग करें और मजबूत मॉडल सिद्धता की कमी के लिए क्षतिपूर्ति करने के लिए हस्ताक्षर और फ़ाइल हैश के साथ तृतीय-पक्ष मॉडल अखंडता जांच का उपयोग करें। इसी तरह, बाहरी रूप से आपूर्ति किए गए कोड के लिए कोड साइनिंग का उपयोग करें।
7। किसी भी दुरुपयोग को रोकने और जल्दी से पता लगाने के लिए सहयोगी मॉडल विकास वातावरण के लिए सख्त निगरानी और ऑडिटिंग प्रथाओं को लागू करें। "हगिंगफेस SF_CONVERTBOT स्कैनर" उपयोग करने के लिए स्वचालित स्क्रिप्ट का एक उदाहरण है।
  (Ref।
8। आपूर्ति किए गए मॉडल और डेटा पर विसंगति का पता लगाने और प्रतिकूलता परीक्षण छेड़छाड़ और विषाक्तता का पता लगाने में मदद कर सकता है जैसा कि "LLM04 डेटा और मॉडल विषाक्तता में चर्चा की गई है; आदर्श रूप से, यह MLOPS और LLM पाइपलाइनों का हिस्सा होना चाहिए; हालांकि, ये उभरती हुई तकनीक हैं और हो सकती हैं और हो सकती हैं। रेड टीमिंग अभ्यास के हिस्से के रूप में लागू करना आसान है।
9। कमजोर या पुराने घटकों को कम करने के लिए एक पैचिंग नीति लागू करें। सुनिश्चित करें कि एप्लिकेशन एपीआई और अंतर्निहित मॉडल के बनाए रखा संस्करण पर निर्भर करता है।
10। एन्क्रिप्ट मॉडल एआई एज में अखंडता की जांच के साथ तैनात किए गए और छेड़छाड़ किए गए ऐप्स और मॉडल को रोकने के लिए विक्रेता अटेंशन एपीआई का उपयोग करें और गैर -मान्यता प्राप्त फर्मवेयर के अनुप्रयोगों को समाप्त करें।

### Sample Attack Scenarios
### नमूना हमले परिदृश्य

#### Scenario #1: Vulnerable Python Library
  An attacker exploits a vulnerable Python library to compromise an LLM app. This happened in the first Open AI data breach.  Attacks on  the PyPi package registry  tricked model developers into downloading a compromised PyTorch dependency with malware in a model development environment.  A more sophisticated example of this type of attack is Shadow Ray attack on the Ray AI framework used by many vendors to manage AI infrastructure.  In this attack, five vulnerabilities are believed to have been exploited in the wild affecting many servers.
#### Scenario #2: Direct Tampering
  Direct Tampering and publishing a model to spread misinformation. This is an actual attack with PoisonGPT bypassing Hugging Face safety features by directly changing model parameters.
#### Scenario #3: Finetuning Popular Model
  An attacker finetunes a popular open access model to remove key safety features and perform high in a specific domain (insurance). The model is finetuned to score highly on safety benchmarks but  has very targeted  triggers. They deploy it on Hugging Face for victims to use it exploiting their trust on  benchmark assurances.
#### Scenario #4: Pre-Trained Models
  An LLM system deploys pre-trained models from a widely used repository without thorough verification. A compromised model introduces malicious code, causing biased outputs in certain contexts and leading to harmful or manipulated outcomes
#### Scenario #5: Compromised Third-Party Supplier
  A compromised third-party supplier provides a vulnerable LorA adapter that is being merged to an LLM using model merge on Hugging Face.
#### Scenario #6: Supplier Infiltration
  An attacker infiltrates a third-party supplier and compromises the production of a LoRA (Low-Rank Adaptation) adapter intended for integration with an on-device LLM deployed using frameworks like vLLM or OpenLLM. The compromised LoRA adapter is subtly altered to include hidden vulnerabilities and malicious code. Once this adapter is merged with the LLM, it provides the attacker with a covert entry point into the system. The malicious code can activate during model operations, allowing the attacker to manipulate the LLM’s outputs.
#### Scenario #7: CloudBorne and CloudJacking Attacks
  These attacks target cloud infrastructures, leveraging shared resources and vulnerabilities in the virtualization layers. CloudBorne involves exploiting firmware vulnerabilities in shared cloud environments, compromising the physical servers hosting virtual instances. CloudJacking refers to malicious control or misuse of cloud instances, potentially leading to unauthorized access to critical LLM deployment platforms. Both attacks represent significant risks for supply chains reliant on cloud-based ML models, as compromised environments could expose sensitive data or facilitate further attacks.
#### Scenario #8: LeftOvers (CVE-2023-4969)
  LeftOvers exploitation of leaked GPU local memory to recover sensitive data. An attacker can use this attack to exfiltrate sensitive data in production servers and development workstations or laptops.
#### Scenario #9: WizardLM
  Following the removal of WizardLM, an attacker exploits the interest in this model and publish a fake version of the model with the same name but containing malware and backdoors.
#### Scenario #10: Model Merge/Format Conversion Service
  An attacker stages an attack with a model merge or format conversation service to compromise a publicly available access model to inject malware. This is an actual attack published by vendor HiddenLayer.
#### Scenario #11: Reverse-Engineer Mobile App
  An attacker reverse-engineers an mobile app to replace the model with a tampered version that leads the user to scam sites. Users are encouraged to download the app directly via social engineering techniques. This is a "real attack on predictive AI" that affected 116 Google Play apps including popular security and safety-critical applications used for as cash recognition, parental control, face authentication, and financial service.
  (Ref. link: [real attack on predictive AI](https://arxiv.org/abs/2006.08131))
#### Scenario #12: Dataset Poisoning
  An attacker poisons publicly available datasets to help create a back door when fine-tuning models. The back door subtly favors certain companies in different markets.
#### Scenario #13: T&Cs and Privacy Policy
  An LLM operator changes its T&Cs and Privacy Policy to require an explicit opt out from using application data for model training, leading to the memorization of sensitive data.
#### परिदृश्य#1: कमजोर पायथन लाइब्रेरी
  एक हमलावर एक एलएलएम ऐप से समझौता करने के लिए एक कमजोर पायथन लाइब्रेरी का शोषण करता है। यह पहले ओपन एआई डेटा ब्रीच में हुआ था।  PYPI पैकेज रजिस्ट्री पर हमलों ने मॉडल डेवलपर्स को एक मॉडल विकास वातावरण में मैलवेयर के साथ एक समझौता किए गए Pytorch निर्भरता को डाउनलोड करने में धोखा दिया।  इस प्रकार के हमले का एक अधिक परिष्कृत उदाहरण एआई बुनियादी ढांचे का प्रबंधन करने के लिए कई विक्रेताओं द्वारा उपयोग किए जाने वाले रे एआई फ्रेमवर्क पर शैडो रे हमला है।  इस हमले में, माना जाता है कि पांच कमजोरियों का कई सर्वरों को प्रभावित करने वाले जंगली में शोषण किया गया है।
#### परिदृश्य#2: प्रत्यक्ष छेड़छाड़
  गलत सूचना फैलाने के लिए एक मॉडल को निर्देशित करना और प्रकाशित करना। यह सीधे बदलते मॉडल मापदंडों द्वारा चेहरे की सुरक्षा सुविधाओं को दरकिनार करने के साथ पोइसॉन्ग्ट के साथ एक वास्तविक हमला है।
#### परिदृश्य#3: फिनिटिंग लोकप्रिय मॉडल
  एक हमलावर प्रमुख सुरक्षा सुविधाओं को हटाने और एक विशिष्ट डोमेन (बीमा) में उच्च प्रदर्शन करने के लिए एक लोकप्रिय ओपन एक्सेस मॉडल को फाइनट्यूस करता है। मॉडल को सुरक्षा बेंचमार्क पर अत्यधिक स्कोर करने के लिए finetuned है, लेकिन बहुत लक्षित ट्रिगर है। वे इसे पीड़ितों के लिए चेहरे पर गले लगाने के लिए तैनात करते हैं, जो बेंचमार्क आश्वासन पर अपने विश्वास का फायदा उठाते हैं।
#### परिदृश्य#4: पूर्व-प्रशिक्षित मॉडल
  एक एलएलएम सिस्टम पूरी तरह से सत्यापन के बिना व्यापक रूप से उपयोग किए जाने वाले रिपॉजिटरी से पूर्व-प्रशिक्षित मॉडल को तैनात करता है। एक समझौता मॉडल दुर्भावनापूर्ण कोड का परिचय देता है, जिससे कुछ संदर्भों में पक्षपाती आउटपुट होता है और हानिकारक या हेरफेर परिणामों के लिए अग्रणी होता है
#### परिदृश्य#5: समझौता तृतीय-पक्ष आपूर्तिकर्ता
  एक समझौता किया गया तृतीय-पक्ष आपूर्तिकर्ता एक कमजोर लोरा एडाप्टर प्रदान करता है जिसे गले लगाने के लिए मॉडल मर्ज का उपयोग करके एलएलएम को विलय किया जा रहा है।
#### परिदृश्य#6: आपूर्तिकर्ता घुसपैठ
  एक हमलावर एक तृतीय-पक्ष आपूर्तिकर्ता में घुसपैठ करता है और एक लोरा (कम-रैंक अनुकूलन) एडाप्टर के उत्पादन से समझौता करता है जो वीएलएलएम या ओपनएलएलएम जैसे फ्रेमवर्क का उपयोग करके तैनात ऑन-डिवाइस एलएलएम के साथ एकीकरण के लिए इरादा है। छिपी हुई कमजोरियों और दुर्भावनापूर्ण कोड को शामिल करने के लिए समझौता किए गए लोरा एडाप्टर को सूक्ष्मता से बदल दिया जाता है। एक बार जब इस एडाप्टर को एलएलएम के साथ विलय कर दिया जाता है, तो यह हमलावर को सिस्टम में एक गुप्त प्रवेश बिंदु प्रदान करता है। दुर्भावनापूर्ण कोड मॉडल संचालन के दौरान सक्रिय हो सकता है, जिससे हमलावर एलएलएम के आउटपुट में हेरफेर कर सकता है।
#### परिदृश्य#7: क्लाउडबोर्न और क्लाउडजैकिंग हमले
  ये हमले क्लाउड इन्फ्रास्ट्रक्चर को लक्षित करते हैं, वर्चुअलाइजेशन परतों में साझा संसाधनों और कमजोरियों का लाभ उठाते हैं। क्लाउडबोर्न में साझा क्लाउड वातावरण में फर्मवेयर कमजोरियों का शोषण करना शामिल है, जो आभासी उदाहरणों की मेजबानी करने वाले भौतिक सर्वर से समझौता करता है। CloudJacking दुर्भावनापूर्ण नियंत्रण या क्लाउड उदाहरणों के दुरुपयोग को संदर्भित करता है, संभवतः महत्वपूर्ण LLM तैनाती प्लेटफार्मों के लिए अनधिकृत पहुंच के लिए अग्रणी है। दोनों हमले क्लाउड-आधारित एमएल मॉडल पर आपूर्ति श्रृंखलाओं के लिए महत्वपूर्ण जोखिमों का प्रतिनिधित्व करते हैं, क्योंकि समझौता वातावरण संवेदनशील डेटा को उजागर कर सकता है या आगे के हमलों की सुविधा प्रदान कर सकता है।
#### परिदृश्य#8: बचे हुए (CVE-2023-4969)
  संवेदनशील डेटा को पुनर्प्राप्त करने के लिए लीक हुए जीपीयू स्थानीय मेमोरी के बचे हुए शोषण। एक हमलावर इस हमले का उपयोग उत्पादन सर्वर और विकास कार्यस्थानों या लैपटॉप में संवेदनशील डेटा को एक्सफिल्टेट करने के लिए कर सकता है।
#### परिदृश्य#9: विजार्डल्म
  विजार्डलएम को हटाने के बाद, एक हमलावर इस मॉडल में रुचि का फायदा उठाता है और उसी नाम के साथ मॉडल का एक नकली संस्करण प्रकाशित करता है, लेकिन मैलवेयर और बैकडोर युक्त होता है।
#### परिदृश्य#10: मॉडल मर्ज/प्रारूप रूपांतरण सेवा
  एक हमलावर मैलवेयर को इंजेक्ट करने के लिए सार्वजनिक रूप से उपलब्ध एक्सेस मॉडल से समझौता करने के लिए एक मॉडल मर्ज या प्रारूप वार्तालाप सेवा के साथ एक हमला करता है। यह विक्रेता हिडनलेयर द्वारा प्रकाशित एक वास्तविक हमला है।
#### परिदृश्य#11: रिवर्स-इंजीनियर मोबाइल ऐप
  एक हमलावर रिवर्स-इंजीनियर एक मोबाइल ऐप को एक छेड़छाड़ किए गए संस्करण के साथ मॉडल को बदलने के लिए करता है जो उपयोगकर्ता को घोटाले वाली साइटों की ओर ले जाता है। उपयोगकर्ताओं को सोशल इंजीनियरिंग तकनीकों के माध्यम से सीधे ऐप डाउनलोड करने के लिए प्रोत्साहित किया जाता है। यह एक "प्रेडिक्टिव एआई पर वास्तविक हमला" है जिसने 116 Google Play ऐप को प्रभावित किया है जिसमें लोकप्रिय सुरक्षा और सुरक्षा-महत्वपूर्ण अनुप्रयोगों को नकद मान्यता, माता-पिता नियंत्रण, चेहरे प्रमाणीकरण और वित्तीय सेवा के रूप में उपयोग किया जाता है।
  (Ref।
#### परिदृश्य#12: डेटासेट विषाक्तता
  एक हमलावर जहर सार्वजनिक रूप से उपलब्ध डेटासेट को ठीक-ट्यूनिंग मॉडल होने पर एक बैक डोर बनाने में मदद करता है। पीछे का दरवाजा सूक्ष्म रूप से विभिन्न बाजारों में कुछ कंपनियों का पक्षधर है।
#### परिदृश्य#13: टी एंड सीएस और गोपनीयता नीति
  एक एलएलएम ऑपरेटर अपने टी एंड सीएस और गोपनीयता नीति को बदलता है ताकि मॉडल प्रशिक्षण के लिए एप्लिकेशन डेटा का उपयोग करने से एक स्पष्ट ऑप्ट की आवश्यकता हो, जिससे संवेदनशील डेटा के संस्मरण हो।

### Reference Links
### संदर्भ लिंक

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
1। से फैल-फेक-न्यूज)
2। [MediaPipe और TensorFlow Lite के साथ बड़ी भाषा मॉडल ऑन-डिवाइस] (https://developers.googleblog.com/en/large-language-models-on-device-with-mediapipe-and-tensorflow-lite/)
3। [हगिंग सेफेंसर कन्वर्जन हगिंग फेस पर अपहरण करें]
4। [एमएल आपूर्ति श्रृंखला समझौता] (https://atlas.mitre.org/techniques/aml.t0010)
5। [VLLM के साथ लोरा एडेप्टर का उपयोग करना] (https://docs.vllm.ai/en/latest/models/lora.html)
6। [फाइन-ट्यूनिंग के माध्यम से GPT-4 में RLHF सुरक्षा को हटाना] (https://arxiv.org/pdf/2311.055553)
7। [PEFT के साथ मॉडल विलय] (https://huggingface.co/blog/peft_merging)
8।
9। [हजारों सर्वर को असुरक्षित रूप से तैनात रे एआई फ्रेमवर्क के कारण हैक कर लिया गया] (https://www.csoonline.com/article/2075540/ हजारों-ऑफ-सर्वर्स-हैक्ड-ड्यू-टू-इन-इन-इन-इन-इन-डिसी-रे-एआई- एई- फ्रेमवर्क। html)
10। [बचे हुए लोग: लीक हुए जीपीयू स्थानीय मेमोरी के माध्यम से एलएलएम प्रतिक्रियाओं को सुनना] (https://blog.trailofbits.com/2024/01/16/leftoverlocals-listening-to-llm-respons-through-leaked-gpu-local- याद/)

### Related Frameworks and Taxonomies
### संबंधित फ्रेमवर्क और टैक्सोनॉमी

Refer to this section for comprehensive information, scenarios strategies relating to infrastructure deployment, applied environment controls and other best practices.
बुनियादी ढांचे की तैनाती, लागू पर्यावरण नियंत्रण और अन्य सर्वोत्तम प्रथाओं से संबंधित व्यापक जानकारी, परिदृश्य रणनीतियों के लिए इस खंड का संदर्भ लें।

- [ML Supply Chain Compromise](https://atlas.mitre.org/techniques/AML.T0010) -  **MITRE ATLAS**

- [एमएल आपूर्ति श्रृंखला समझौता]

