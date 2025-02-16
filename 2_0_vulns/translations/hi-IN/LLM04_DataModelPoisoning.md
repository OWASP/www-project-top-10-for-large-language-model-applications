## LLM04: Data and Model Poisoning
## LLM04: डेटा और मॉडल विषाक्तता

### Description
### विवरण

Data poisoning occurs when pre-training, fine-tuning, or embedding data is manipulated to introduce vulnerabilities, backdoors, or biases. This manipulation can compromise model security, performance, or ethical behavior, leading to harmful outputs or impaired capabilities. Common risks include degraded model performance, biased or toxic content, and exploitation of downstream systems.
डेटा विषाक्तता तब होती है जब पूर्व-प्रशिक्षण, फाइन-ट्यूनिंग या एम्बेडिंग डेटा को कमजोरियों, बैकडोर या बायसेस को पेश करने के लिए हेरफेर किया जाता है। यह हेरफेर मॉडल सुरक्षा, प्रदर्शन या नैतिक व्यवहार से समझौता कर सकता है, जिससे हानिकारक आउटपुट या बिगड़ा हुआ क्षमताएं हो सकती हैं। सामान्य जोखिमों में अपमानित मॉडल प्रदर्शन, पक्षपाती या विषाक्त सामग्री, और डाउनस्ट्रीम सिस्टम का शोषण शामिल है।

Data poisoning can target different stages of the LLM lifecycle, including pre-training (learning from general data), fine-tuning (adapting models to specific tasks), embedding (converting text into numerical vectors), and transfer learning (reusing a pre-trained model on a new task). Understanding these stages helps identify where vulnerabilities may originate. Data poisoning is considered an integrity attack since tampering with training data impacts the model's ability to make accurate predictions. The risks are particularly high with external data sources, which may contain unverified or malicious content.
डेटा विषाक्तता एलएलएम जीवनचक्र के विभिन्न चरणों को लक्षित कर सकती है, जिसमें प्री-ट्रेनिंग (सामान्य डेटा से सीखना), फाइन-ट्यूनिंग (विशिष्ट कार्यों के लिए मॉडल को अनुकूलित करना), एम्बेडिंग (पाठ को संख्यात्मक वैक्टर में परिवर्तित करना), और एक पूर्व-पुन: उपयोग करना शामिल है ( एक नए कार्य पर प्रशिक्षित मॉडल)। इन चरणों को समझने से यह पहचानने में मदद मिलती है कि कमजोरियां कहां से उत्पन्न हो सकती हैं। डेटा विषाक्तता को एक अखंडता हमला माना जाता है क्योंकि प्रशिक्षण डेटा के साथ छेड़छाड़ करना सटीक भविष्यवाणियां करने के लिए मॉडल की क्षमता को प्रभावित करता है। जोखिम बाहरी डेटा स्रोतों के साथ विशेष रूप से उच्च हैं, जिसमें असुविधाजनक या दुर्भावनापूर्ण सामग्री हो सकती है।

Moreover, models distributed through shared repositories or open-source platforms can carry risks beyond data poisoning, such as malware embedded through techniques like malicious pickling, which can execute harmful code when the model is loaded. Also, consider that poisoning may allow for the implementation of a backdoor. Such backdoors may leave the model's behavior untouched until a certain trigger causes it to change. This may make such changes hard to test for and detect, in effect creating the opportunity for a model to become a sleeper agent.
इसके अलावा, साझा रिपॉजिटरी या ओपन-सोर्स प्लेटफॉर्म के माध्यम से वितरित किए गए मॉडल डेटा विषाक्तता से परे जोखिम ले सकते हैं, जैसे कि मैलवेयर दुर्भावनापूर्ण अचार जैसी तकनीकों के माध्यम से एम्बेडेड, जो कि मॉडल लोड होने पर हानिकारक कोड को निष्पादित कर सकता है। इसके अलावा, विचार करें कि विषाक्तता एक पिछले दरवाजे के कार्यान्वयन के लिए अनुमति दे सकती है। इस तरह के बैकडोर मॉडल के व्यवहार को तब तक छोड़ सकते हैं जब तक कि एक निश्चित ट्रिगर इसे बदलने का कारण नहीं बन जाता। यह इस तरह के परिवर्तनों को परीक्षण करने और पता लगाने के लिए कठिन बना सकता है, वास्तव में एक मॉडल के लिए एक स्लीपर एजेंट बनने का अवसर पैदा करता है।

### Common Examples of Vulnerability
### भेद्यता के सामान्य उदाहरण

1. Malicious actors introduce harmful data during training, leading to biased outputs. Techniques like "Split-View Data Poisoning" or "Frontrunning Poisoning" exploit model training dynamics to achieve this.
  (Ref. link: [Split-View Data Poisoning](https://github.com/GangGreenTemperTatum/speaking/blob/main/dc604/hacker-summer-camp-23/Ads%20_%20Poisoning%20Web%20Training%20Datasets%20_%20Flow%20Diagram%20-%20Exploit%201%20Split-View%20Data%20Poisoning.jpeg))
  (Ref. link: [Frontrunning Poisoning](https://github.com/GangGreenTemperTatum/speaking/blob/main/dc604/hacker-summer-camp-23/Ads%20_%20Poisoning%20Web%20Training%20Datasets%20_%20Flow%20Diagram%20-%20Exploit%202%20Frontrunning%20Data%20Poisoning.jpeg))
2. Attackers can inject harmful content directly into the training process, compromising the model’s output quality.
3. Users unknowingly inject sensitive or proprietary information during interactions, which could be exposed in subsequent outputs.
4. Unverified training data increases the risk of biased or erroneous outputs.
5. Lack of resource access restrictions may allow the ingestion of unsafe data, resulting in biased outputs.
1। दुर्भावनापूर्ण अभिनेता प्रशिक्षण के दौरान हानिकारक डेटा पेश करते हैं, जिससे पक्षपाती आउटपुट होता है। इसे प्राप्त करने के लिए "स्प्लिट-व्यू डेटा पॉइज़निंग" या "मोर्चिंग पॉइज़निंग" जैसे तकनीक "मोर्चिंग पॉइज़निंग" शोषण मॉडल प्रशिक्षण गतिशीलता जैसी तकनीकें।
  (Ref। %20_%20flow%20diagram%20-%20Exploit%201%20Split-View%20data%20poisoning.jpeg)))
  (Ref। 20flow%20diagram%20-%20EXPLOIT%202%20FRONTRUNNING%20DATA%20POISONING.JPEG)))
2। हमलावरों ने हानिकारक सामग्री को सीधे प्रशिक्षण प्रक्रिया में इंजेक्ट कर सकते हैं, मॉडल की आउटपुट गुणवत्ता से समझौता कर सकते हैं।
3। उपयोगकर्ता अनजाने में बातचीत के दौरान संवेदनशील या मालिकाना जानकारी को इंजेक्ट करते हैं, जिसे बाद के आउटपुट में उजागर किया जा सकता है।
4। अस्वीकृत प्रशिक्षण डेटा पक्षपाती या गलत आउटपुट के जोखिम को बढ़ाता है।
5। संसाधन पहुंच प्रतिबंधों की कमी असुरक्षित डेटा के अंतर्ग्रहण की अनुमति दे सकती है, जिसके परिणामस्वरूप पक्षपाती आउटपुट होता है।

### Prevention and Mitigation Strategies
### रोकथाम और शमन रणनीतियाँ

1. Track data origins and transformations using tools like OWASP CycloneDX or ML-BOM and leverage tools such as [Dyana](https://github.com/dreadnode/dyana) to perform dynamic analysis of third-party software. Verify data legitimacy during all model development stages.
2. Vet data vendors rigorously, and validate model outputs against trusted sources to detect signs of poisoning.
3. Implement strict sandboxing to limit model exposure to unverified data sources. Use anomaly detection techniques to filter out adversarial data.
4. Tailor models for different use cases by using specific datasets for fine-tuning. This helps produce more accurate outputs based on defined goals.
5. Ensure sufficient infrastructure controls to prevent the model from accessing unintended data sources.
6. Use data version control (DVC) to track changes in datasets and detect manipulation. Versioning is crucial for maintaining model integrity.
7. Store user-supplied information in a vector database, allowing adjustments without re-training the entire model.
8. Test model robustness with red team campaigns and adversarial techniques, such as federated learning, to minimize the impact of data perturbations.
9. Monitor training loss and analyze model behavior for signs of poisoning. Use thresholds to detect anomalous outputs.
10. During inference, integrate Retrieval-Augmented Generation (RAG) and grounding techniques to reduce risks of hallucinations.
1। TRACK डेटा ओरिजिन और ट्रांसफॉर्मेशन जैसे OWASP Cyclonedx या ML-BOM और लीवरेज टूल जैसे टूल का उपयोग करके [Dyana] (https://github.com/dreadnode/dyana) तृतीय-भाग सॉफ्टवेयर का डायनेमिक विश्लेषण करने के लिए। सभी मॉडल विकास चरणों के दौरान डेटा वैधता को सत्यापित करें।
2। वीईटी डेटा विक्रेताओं को कठोरता से, और जहर के संकेतों का पता लगाने के लिए विश्वसनीय स्रोतों के खिलाफ मॉडल आउटपुट को मान्य करें।
3। अस्वीकृत डेटा स्रोतों के लिए मॉडल एक्सपोज़र को सीमित करने के लिए सख्त सैंडबॉक्सिंग को लागू करें। प्रतिकूल डेटा को फ़िल्टर करने के लिए विसंगति का पता लगाने की तकनीक का उपयोग करें।
4। ठीक-ट्यूनिंग के लिए विशिष्ट डेटासेट का उपयोग करके विभिन्न उपयोग के मामलों के लिए दर्जी मॉडल। यह परिभाषित लक्ष्यों के आधार पर अधिक सटीक आउटपुट का उत्पादन करने में मदद करता है।
5। मॉडल को अनपेक्षित डेटा स्रोतों तक पहुंचने से रोकने के लिए पर्याप्त बुनियादी ढांचा नियंत्रण सुनिश्चित करें।
6। डेटासेट में परिवर्तन को ट्रैक करने और हेरफेर का पता लगाने के लिए डेटा संस्करण नियंत्रण (DVC) का उपयोग करें। मॉडल अखंडता बनाए रखने के लिए संस्करण महत्वपूर्ण है।
7। एक वेक्टर डेटाबेस में उपयोगकर्ता द्वारा आपूर्ति की गई जानकारी को संग्रहीत करें, पूरे मॉडल को फिर से प्रशिक्षण के बिना समायोजन की अनुमति दें।
8। रेड टीम अभियानों और प्रतिकूल तकनीकों जैसे कि फेडरेटेड लर्निंग के साथ परीक्षण मॉडल की मजबूती, डेटा गड़बड़ी के प्रभाव को कम करने के लिए।
9। प्रशिक्षण हानि की निगरानी करें और विषाक्तता के संकेतों के लिए मॉडल व्यवहार का विश्लेषण करें। विसंगतिपूर्ण आउटपुट का पता लगाने के लिए थ्रेसहोल्ड का उपयोग करें।
10। अनुमान के दौरान, मतिभ्रम के जोखिम को कम करने के लिए पुनर्प्राप्ति-अगस्त पीढ़ी (आरएजी) और ग्राउंडिंग तकनीकों को एकीकृत करें।

### Example Attack Scenarios
### उदाहरण हमले परिदृश्य

#### Scenario #1
  An attacker biases the model's outputs by manipulating training data or using prompt injection techniques, spreading misinformation.
#### Scenario #2
  Toxic data without proper filtering can lead to harmful or biased outputs, propagating dangerous information.
#### Scenario # 3
  A malicious actor or competitor creates falsified documents for training, resulting in model outputs that reflect these inaccuracies.
#### Scenario #4
  Inadequate filtering allows an attacker to insert misleading data via prompt injection, leading to compromised outputs.
#### Scenario #5
  An attacker uses poisoning techniques to insert a backdoor trigger into the model. This could leave you open to authentication bypass, data exfiltration or hidden command execution.
#### परिद्रश्य 1
  एक हमलावर प्रशिक्षण डेटा में हेरफेर करके या शीघ्र इंजेक्शन तकनीकों का उपयोग करके, गलत सूचना फैलाने के द्वारा मॉडल के आउटपुट को पक्षपात करता है।
#### परिदृश्य#2
  उचित फ़िल्टरिंग के बिना विषाक्त डेटा खतरनाक जानकारी का प्रचार करते हुए हानिकारक या पक्षपाती आउटपुट को जन्म दे सकता है।
#### परिदृश्य#3
  एक दुर्भावनापूर्ण अभिनेता या प्रतियोगी प्रशिक्षण के लिए गलत दस्तावेज बनाता है, जिसके परिणामस्वरूप मॉडल आउटपुट होता है जो इन अशुद्धियों को दर्शाता है।
#### परिदृश्य#4
  अपर्याप्त फ़िल्टरिंग एक हमलावर को शीघ्र इंजेक्शन के माध्यम से भ्रामक डेटा डालने की अनुमति देता है, जिससे समझौता आउटपुट होता है।
#### परिदृश्य#5
  एक हमलावर मॉडल में एक बैकडोर ट्रिगर डालने के लिए विषाक्तता तकनीकों का उपयोग करता है। यह आपको प्रमाणीकरण बाईपास, डेटा एक्सफिल्ट्रेशन या हिडन कमांड निष्पादन के लिए खुला छोड़ सकता है।

### Reference Links
### संदर्भ लिंक

1. [How data poisoning attacks corrupt machine learning models](https://www.csoonline.com/article/3613932/how-data-poisoning-attacks-corrupt-machine-learning-models.html): **CSO Online**
2. [MITRE ATLAS (framework) Tay Poisoning](https://atlas.mitre.org/studies/AML.CS0009/): **MITRE ATLAS**
3. [PoisonGPT: How we hid a lobotomized LLM on Hugging Face to spread fake news](https://blog.mithrilsecurity.io/poisongpt-how-we-hid-a-lobotomized-llm-on-hugging-face-to-spread-fake-news/): **Mithril Security**
4. [Poisoning Language Models During Instruction](https://arxiv.org/abs/2305.00944): **Arxiv White Paper 2305.00944**
5. [Poisoning Web-Scale Training Datasets - Nicholas Carlini | Stanford MLSys #75](https://www.youtube.com/watch?v=h9jf1ikcGyk): **Stanford MLSys Seminars YouTube Video**
6. [ML Model Repositories: The Next Big Supply Chain Attack Target](https://www.darkreading.com/cloud-security/ml-model-repositories-next-big-supply-chain-attack-target) **OffSecML**
7. [Data Scientists Targeted by Malicious Hugging Face ML Models with Silent Backdoor](https://jfrog.com/blog/data-scientists-targeted-by-malicious-hugging-face-ml-models-with-silent-backdoor/) **JFrog**
8. [Backdoor Attacks on Language Models](https://towardsdatascience.com/backdoor-attacks-on-language-models-can-we-trust-our-models-weights-73108f9dcb1f): **Towards Data Science**
9. [Never a dill moment: Exploiting machine learning pickle files](https://blog.trailofbits.com/2021/03/15/never-a-dill-moment-exploiting-machine-learning-pickle-files/) **TrailofBits**
10. [arXiv:2401.05566 Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training](https://www.anthropic.com/news/sleeper-agents-training-deceptive-llms-that-persist-through-safety-training) **Anthropic (arXiv)**
11. [Backdoor Attacks on AI Models](https://www.cobalt.io/blog/backdoor-attacks-on-ai-models) **Cobalt**
1। [कैसे डेटा पॉइज़निंग भ्रष्ट मशीन लर्निंग मॉडल पर हमला करता है] (https://www.csoonline.com/article/3613932/how-data-poisoning- attacks-corrupt-machine-learning.html): ** CSO ऑनलाइन **
2।
3। to-spead-fake-news/): ** मिथ्रिल सुरक्षा **
4। [निर्देश के दौरान भाषा मॉडल को जहर देना] (https://arxiv.org/abs/2305.00944): ** arxiv श्वेत पत्र 2305.00944 **
5। [जहर वेब -स्केल प्रशिक्षण डेटासेट - निकोलस कार्लिनि | स्टैनफोर्ड MLSYS #75] (https://www.youtube.com/watch?v=H9JF1IKCGYK): ** स्टैनफोर्ड MLSYS सेमिनार YouTube वीडियो **
6। [एमएल मॉडल रिपॉजिटरी: अगला बिग सप्लाई चेन अटैक टारगेट] (https://www.darkreading.com/cloud-security/ml-model-repositories-next-big-puply-chain- attack-target) ** OffSecml **
7। [साइलेंट बैकडोर के साथ दुर्भावनापूर्ण गले लगाने वाले चेहरे एमएल मॉडल द्वारा लक्षित डेटा वैज्ञानिकों] (https://jfrog.com/blog/data-cientists-targeted-by-malious-hagging-models-models-with-silent-backdoor /) ** JFROG **
8। [भाषा मॉडल पर बैकडोर हमले]
9। ** ट्रेलोफबिट्स **
10। ) ** एन्थ्रोप्रोपिक (arxiv) **
11। [एआई मॉडल पर बैकडोर हमले] (https://www.cobalt.io/blog/backdoor-atacks-on-ai-models) ** कोबाल्ट **

### Related Frameworks and Taxonomies
### संबंधित फ्रेमवर्क और टैक्सोनॉमी

Refer to this section for comprehensive information, scenarios strategies relating to infrastructure deployment, applied environment controls and other best practices.
बुनियादी ढांचे की तैनाती, लागू पर्यावरण नियंत्रण और अन्य सर्वोत्तम प्रथाओं से संबंधित व्यापक जानकारी, परिदृश्यों की रणनीतियों के लिए इस खंड का संदर्भ लें।

- [AML.T0018 | Backdoor ML Model](https://atlas.mitre.org/techniques/AML.T0018) **MITRE ATLAS**
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework): Strategies for ensuring AI integrity. **NIST**
- [ML07:2023 Transfer Learning Attack](https://owasp.org/www-project-machine-learning-security-top-10/docs/ML07_2023-Transfer_Learning_Attack) **OWASP Machine Learning Security Top Ten**
- [AML.T0018 | बैकडोर एमएल मॉडल] (https://atlas.mitre.org/techniques/aml.t0018) ** Miter Atlas **
-[एनआईएसटी एआई रिस्क मैनेजमेंट फ्रेमवर्क] (https://www.nist.gov/itl/ai-risk-management-framework): AI अखंडता सुनिश्चित करने के लिए रणनीतियाँ। ** nist **
-[ML07: 2023 ट्रांसफर लर्निंग अटैक]

