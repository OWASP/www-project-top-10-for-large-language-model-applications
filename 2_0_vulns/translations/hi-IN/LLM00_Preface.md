## Letter from the Project Leads
परियोजना से ## पत्र लीड्स

The OWASP Top 10 for Large Language Model Applications started in 2023 as a community-driven effort to highlight and address security issues specific to AI applications. Since then, the technology has continued to spread across industries and applications, and so have the associated risks. As LLMs are embedded more deeply in everything from customer interactions to internal operations, developers and security professionals are discovering new vulnerabilities—and ways to counter them.
बड़े भाषा मॉडल अनुप्रयोगों के लिए OWASP शीर्ष 10 2023 में AI अनुप्रयोगों के लिए विशिष्ट सुरक्षा मुद्दों को उजागर करने और संबोधित करने के लिए एक समुदाय-संचालित प्रयास के रूप में शुरू हुआ। तब से, प्रौद्योगिकी ने उद्योगों और अनुप्रयोगों में फैलाना जारी रखा है, और इसलिए संबंधित जोखिम हैं। चूंकि एलएलएम ग्राहक इंटरैक्शन से लेकर आंतरिक संचालन तक हर चीज में अधिक गहराई से एम्बेडेड हैं, डेवलपर्स और सुरक्षा पेशेवर नई कमजोरियों की खोज कर रहे हैं - और उनका मुकाबला करने के तरीके।

The 2023 list was a big success in raising awareness and building a foundation for secure LLM usage, but we've learned even more since then. In this new 2025 version, we’ve worked with a larger, more diverse group of contributors worldwide who have all helped shape this list. The process involved brainstorming sessions, voting, and real-world feedback from professionals in the thick of LLM application security, whether by contributing or refining those entries through feedback. Each voice was critical to making this new release as thorough and practical as possible.
2023 की सूची जागरूकता बढ़ाने और सुरक्षित एलएलएम उपयोग के लिए एक नींव बनाने में एक बड़ी सफलता थी, लेकिन हमने तब से और भी अधिक सीखा है। इस नए 2025 संस्करण में, हमने दुनिया भर में योगदानकर्ताओं के एक बड़े, अधिक विविध समूह के साथ काम किया है, जिन्होंने इस सूची को आकार देने में मदद की है। इस प्रक्रिया में एलएलएम एप्लिकेशन सुरक्षा की मोटी में पेशेवरों से मंथन सत्र, मतदान और वास्तविक दुनिया की प्रतिक्रिया शामिल थी, चाहे वह फीडबैक के माध्यम से उन प्रविष्टियों का योगदान या परिष्कृत हो। प्रत्येक आवाज इस नई रिलीज को यथासंभव पूरी तरह से और व्यावहारिक बनाने के लिए महत्वपूर्ण थी।

### What’s New in the 2025 Top 10
### 2025 शीर्ष 10 में नया क्या है

The 2025 list reflects a better understanding of existing risks and introduces critical updates on how LLMs are used in real-world applications today. For instance, **Unbounded Consumption** expands on what was previously Denial of Service to include risks around resource management and unexpected costs—a pressing issue in large-scale LLM deployments.
2025 की सूची मौजूदा जोखिमों की बेहतर समझ को दर्शाती है और आज वास्तविक दुनिया के अनुप्रयोगों में एलएलएम का उपयोग कैसे किया जाता है, इस पर महत्वपूर्ण अपडेट पेश करता है। उदाहरण के लिए, ** अनबाउंड खपत ** संसाधन प्रबंधन और अप्रत्याशित लागतों के आसपास जोखिमों को शामिल करने के लिए सेवा से पहले जो सेवा से इनकार कर रहा था, उस पर विस्तार करता है-बड़े पैमाने पर एलएलएम तैनाती में एक दबाव वाला मुद्दा।

The **Vector and Embeddings** entry responds to the community’s requests for guidance on securing Retrieval-Augmented Generation (RAG) and other embedding-based methods, now core practices for grounding model outputs.
** वेक्टर और एम्बेडिंग ** प्रविष्टि समुदाय के अनुरोधों पर प्रतिक्रिया करता है, जो पुनर्प्राप्ति-अगस्त पीढ़ी (आरएजी) और अन्य एम्बेडिंग-आधारित विधियों को सुरक्षित करने के लिए मार्गदर्शन के लिए अनुरोध करता है, जो अब ग्राउंडिंग मॉडल आउटपुट के लिए मुख्य प्रथाओं है।

We’ve also added **System Prompt Leakage** to address an area with real-world exploits that were highly requested by the community. Many applications assumed prompts were securely isolated, but recent incidents have shown that developers cannot safely assume that information in these prompts remains secret.
हमने वास्तविक दुनिया के कारनामों के साथ एक क्षेत्र को संबोधित करने के लिए ** सिस्टम प्रॉम्प्ट रिसाव ** भी जोड़ा है जो समुदाय द्वारा अत्यधिक अनुरोध किए गए थे। कई अनुप्रयोगों ने माना कि संकेतों को सुरक्षित रूप से अलग किया गया था, लेकिन हाल की घटनाओं से पता चला है कि डेवलपर्स सुरक्षित रूप से यह नहीं मान सकते हैं कि इन संकेतों में जानकारी गुप्त बनी हुई है।

**Excessive Agency** has been expanded, given the increased use of agentic architectures that can give the LLM more autonomy.  With LLMs acting as agents or in plug-in settings, unchecked permissions can lead to unintended or risky actions, making this entry more critical than ever.
** अत्यधिक एजेंसी ** का विस्तार किया गया है, एजेंटिक आर्किटेक्चर के बढ़ते उपयोग को देखते हुए जो एलएलएम को अधिक स्वायत्तता दे सकते हैं।  एलएलएम एजेंटों या प्लग-इन सेटिंग्स में अभिनय करने के साथ, अनियंत्रित अनुमतियों से अनपेक्षित या जोखिम भरे कार्यों को जन्म दिया जा सकता है, जिससे यह प्रविष्टि पहले से कहीं अधिक महत्वपूर्ण हो जाती है।

### Moving Forward
### आगे बढ़ते हुए

Like the technology itself, this list is a product of the open-source community’s insights and experiences. It has been shaped by contributions from developers, data scientists, and security experts across sectors, all committed to building safer AI applications. We’re proud to share this 2025 version with you, and we hope it provides you with the tools and knowledge to secure LLMs effectively.
प्रौद्योगिकी की तरह, यह सूची ओपन-सोर्स समुदाय की अंतर्दृष्टि और अनुभवों का एक उत्पाद है। यह डेवलपर्स, डेटा वैज्ञानिकों और क्षेत्रों में सुरक्षा विशेषज्ञों के योगदान द्वारा आकार दिया गया है, सभी सुरक्षित एआई अनुप्रयोगों के निर्माण के लिए प्रतिबद्ध हैं। हमें इस 2025 संस्करण को आपके साथ साझा करने पर गर्व है, और हमें उम्मीद है कि यह आपको एलएलएम को प्रभावी ढंग से सुरक्षित करने के लिए उपकरण और ज्ञान प्रदान करता है।

Thank you to everyone who helped bring this together and those who continue to use and improve it. We’re grateful to be part of this work with you.
उन सभी को धन्यवाद जिन्होंने इसे एक साथ लाने में मदद की और जो इसका उपयोग करना और सुधारना जारी रखते हैं। हम आपके साथ इस काम का हिस्सा बनने के लिए आभारी हैं।


#### Steve Wilson
Project Lead
OWASP Top 10 for Large Language Model Applications
LinkedIn: https://www.linkedin.com/in/wilsonsd/
#### स्टीव विल्सन
प्रोजेक्ट लीड
बड़े भाषा मॉडल अनुप्रयोगों के लिए OWASP शीर्ष 10
लिंक्डइन: https://www.linkedin.com/in/wilsonsd/

#### Ads Dawson
Technical Lead & Vulnerability Entries Lead
OWASP Top 10 for Large Language Model Applications
LinkedIn: https://www.linkedin.com/in/adamdawson0/

#### विज्ञापन डॉसन
तकनीकी नेतृत्व और भेद्यता प्रविष्टियाँ
बड़े भाषा मॉडल अनुप्रयोगों के लिए OWASP शीर्ष 10
लिंक्डइन: https://www.linkedin.com/in/adamdawson0/

