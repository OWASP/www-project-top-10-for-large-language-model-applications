## LLM04: تسميم البيانات والنماذج

### الوصف

تحدث هجمات تسميم البيانات (Data Poisoning) عندما يتم التلاعب ببيانات ما قبل التدريب، أو بيانات الضبط الدقيق، أو البيانات المُضمّنة، بهدف إدخال ثغرات، أو أبواب خلفية، أو تحيّزات. يمكن أن يُضعف هذا التلاعب من أمان النموذج، أو أدائه، أو سلوكه الأخلاقي، مما يؤدي إلى مخرجات ضارة أو قدرات غير موثوقة. تشمل المخاطر الشائعة: تدهور أداء النموذج، وإنتاج محتوى متحيز أو سام، واستغلال الأنظمة التي تعتمد على مخرجات النموذج.

يمكن أن تستهدف هجمات تسميم البيانات (Data Poisoning) مراحل مختلفة من دورة حياة نموذج اللغة الكبير، بما في ذلك: مرحلة ما قبل التدريب (التعلم من بيانات عامة)، ومرحلة الضبط الدقيق لتكييف النموذج مع مهام محددة، ومرحلة التضمين (Embedding) لتحويل النصوص إلى متجهات رقمية، ومرحلة التعلم النقلي (Transfer Learning) التي يُعاد فيها استخدام نموذج مُدرَّب مسبقًا في مهمة جديدة. فهم هذه المراحل يُسهم في تحديد أماكن نشوء الثغرات المحتملة. تُعد هجمات تسميم البيانات من نوع هجمات النزاهة (Integrity Attacks)، نظرًا لأن التلاعب في بيانات التدريب يؤثر على قدرة النموذج في تقديم تنبؤات دقيقة. وترتفع حدة هذه المخاطر بشكل خاص عند الاعتماد على مصادر بيانات خارجية، والتي قد تحتوي على محتوى غير موثق أو خبيث.

علاوة على ذلك، فإن النماذج التي يتم توزيعها من خلال المستودعات البرمجية المشتركة أو منصات المصادر المفتوحة قد تنطوي على مخاطر تتجاوز تسميم البيانات، مثل احتواء برمجيات ضارة (Malware) يتم زرعها باستخدام تقنيات مثل "التنقيط الخبيث" (Malicious Pickling)، والتي قد تؤدي إلى تنفيذ تعليمات ضارة عند تحميل النموذج. بالإضافة إلى ذلك، يمكن لتسميم البيانات أن يُمكّن من زرع باب خلفي في النموذج. قد لا يُؤثر هذا الباب الخلفي على سلوك النموذج حتى يتم تفعيل محفّز معين، مما يجعل اكتشافه واختباره أمرًا بالغ الصعوبة. وبذلك، قد يتحول النموذج فعليًا إلى ما يشبه "العميل النائم" (Sleeper Agent).

### أمثلة شائعة على الثغرات

1. يُدخل المهاجمون بيانات ضارة أثناء التدريب، مما يؤدي إلى مخرجات متحيّزة. تستغل تقنيات مثل "تسميم البيانات من خلال عرض منقسم" (Split-View Data Poisoning) أو "تسميم البيانات عبر السبق" (Frontrunning Poisoning) ديناميكيات تدريب النموذج لتحقيق ذلك.
  (روابط مرجعية: [Split-View Data Poisoning](https://github.com/GangGreenTemperTatum/speaking/blob/main/dc604/hacker-summer-camp-23/Ads%20_%20Poisoning%20Web%20Training%20Datasets%20_%20Flow%20Diagram%20-%20Exploit%201%20Split-View%20Data%20Poisoning.jpeg))
  (روابط مرجعية: [Frontrunning Poisoning](https://github.com/GangGreenTemperTatum/speaking/blob/main/dc604/hacker-summer-camp-23/Ads%20_%20Poisoning%20Web%20Training%20Datasets%20_%20Flow%20Diagram%20-%20Exploit%202%20Frontrunning%20Data%20Poisoning.jpeg))
3. يمكن للمهاجمين حقن محتوى ضار بشكل مباشر ضمن عملية التدريب، مما يُضعف جودة مخرجات النموذج.
4. قد يُدخل المستخدمون، دون قصد، معلومات حساسة أو مملوكة أثناء التفاعل مع النموذج، مما قد يؤدي إلى كشفها في مخرجات لاحقة.
5. يزيد استخدام بيانات تدريب غير موثّقة من مخاطر إنتاج مخرجات متحيّزة أو خاطئة.
6. غياب القيود على الوصول إلى الموارد قد يسمح للنموذج بابتلاع بيانات غير آمنة، مما يؤدي إلى مخرجات متحيّزة.

### استراتيجيات الوقاية والتخفيف

1. تتبّع مصادر البيانات وتحولاتها باستخدام أدوات مثل OWASP CycloneDX أو ML-BOM، واستفد من أدوات مثل [Dyana](https://github.com/dreadnode/dyana)  لإجراء تحليل ديناميكي للبرمجيات الخارجية. تحقق من شرعية البيانات في جميع مراحل تطوير النموذج.
2.  راجع موثوقية مزوّدي البيانات بعناية، وقم بمقارنة مخرجات النموذج بمصادر موثوقة للكشف عن أي مؤشرات لتسميم البيانات.
3.  طبق عزلاً صارمًا (Strict Sandboxing) للحد من تعرض النموذج لمصادر بيانات غير موثوقة. استخدم تقنيات اكتشاف السلوك غير الطبيعي (Anomaly Detection) لتصفية البيانات العدائية.
4. استخدم مجموعات بيانات محددة في مرحلة الضبط الدقيق (Fine-Tuning) لإنتاج مخرجات أكثر دقة تتماشى مع الأهداف المراد تحقيقها.
5. تأكد من وجود ضوابط كافية للبنية التحتية لمنع النموذج من الوصول إلى مصادر بيانات غير مقصودة.
6. استخدم نظام التحكم في نسخ البيانات (Data Version Control - DVC) لتتبع التغييرات في مجموعات البيانات والكشف عن أي تلاعب. تعد إدارة الإصدارات أمرًا حاسمًا للحفاظ على سلامة النموذج.
7. خزن المعلومات التي يقدمها المستخدم في قاعدة بيانات متجهات (Vector Database)، مما يتيح إمكانية تعديل البيانات دون الحاجة إلى إعادة تدريب النموذج بالكامل.
8. اختبر متانة النموذج من خلال حملات الفريق الأحمر (Red Team Campaigns) وتقنيات هجومية (adversarial techniques) مثل التعلم الموحّد (Federated Learning)، لتقليل تأثير اضطرابات البيانات.
9. راقب فقدان التدريب (Training Loss) وحلل سلوك النموذج لرصد مؤشرات تسميم البيانات. استخدم العتبات (Thresholds) للكشف عن المخرجات الشاذة.
10. أثناء مرحلة الاستدلال (Inference)، إِدمج تقنيات التوليد المعزز بالاسترجاع وتقنيات التأصيل (Grounding) لتقليل مخاطر هلوسة النموذج.

### سيناريوهات هجوم توضيحية

#### السيناريو #1
  يؤثر المهاجم على مخرجات النموذج من خلال التلاعب ببيانات التدريب أو استخدام تقنيات حقن التعليمات (Prompt Injection)، مما يؤدي إلى نشر معلومات مضللة.
#### السيناريو #2
  يمكن أن تؤدي البيانات السامة، في حال عدم تصفيتها بشكل صحيح، إلى مخرجات ضارة أو متحيزة، مما يساهم في نشر معلومات خطيرة.
#### السيناريو #3
  ينشئ المهاجم أو منافس مستندات مزيفة لاستخدامها في التدريب، مما يؤدي إلى مخرجات نموذج تعكس هذه الأخطاء.
#### السيناريو #4
  يؤدي عدم كفاية التصفية إلى تمكين مهاجم من إدخال بيانات مضللة عبر حقن التعليمات، مما يؤدي إلى مخرجات مخترقة.
#### السيناريو #5
  يستخدم المهاجم تقنيات التسميم لإدخال محفّز الباب خلفي (Backdoor Trigger) داخل النموذج، مما قد يعرض النظام لاختراق المصادقة، أو تسريب البيانات، أو تنفيذ أوامر خفية.

### روابط مرجعية

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

### الأطر والتصنيفات ذات الصلة

راجع هذا القسم للحصول على معلومات شاملة، وسيناريوهات واستراتيجيات تتعلق بنشر البنية التحتية، وضوابط البيئة التطبيقية، وأفضل الممارسات الأخرى.

- [AML.T0018 | Backdoor ML Model](https://atlas.mitre.org/techniques/AML.T0018) **MITRE ATLAS**
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework): Strategies for ensuring AI integrity. **NIST**
- [ML07:2023 Transfer Learning Attack](https://owasp.org/www-project-machine-learning-security-top-10/docs/ML07_2023-Transfer_Learning_Attack) **OWASP Machine Learning Security Top Ten**
