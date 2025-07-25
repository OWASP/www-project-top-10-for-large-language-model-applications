## LLM03:2025 ខ្សែសង្វាក់ផ្គត់ផ្គង់ (Supply Chain)

### ការពិពណ៌នា

ខ្សែសង្វាក់ផ្គត់ផ្គង់ LLM ងាយរងគ្រោះទៅនឹងភាពងាយរងគ្រោះផ្សេងៗ ដែលអាចប៉ះពាល់ដល់ integrity នៃ training data, models និង deployment platforms ។ ហានិភ័យទាំងនេះអាចបណ្តាលឱ្យមាន biased outputs, security breaches ឬ system failures ។ ខណៈពេលដែល traditional software vulnerabilities ផ្តោតលើបញ្ហាដូចជា code flaws និង dependencies នៅក្នុង ML ហានិភ័យក៏ពង្រីកទៅ third-party pre-trained models និង data ផងដែរ។

ធាតុខាងក្រៅទាំងនេះអាចត្រូវបាន manipulated តាមរយៈ tampering ឬ poisoning attacks ។

ការបង្កើត LLMs គឺជា specialized task ដែលជារឿយៗអាស្រ័យលើ third-party models ។ ការកើនឡើងនៃ open-access LLMs និង fine-tuning methods ថ្មីៗដូចជា "LoRA" (Low-Rank Adaptation) និង "PEFT" (Parameter-Efficient Fine-Tuning) ជាពិសេសនៅលើ platforms ដូចជា Hugging Face ណែនាំពី supply-chain risks ថ្មីៗ។ ទីបំផុត ការលេចឡើងនៃ on-device LLMs បង្កើន attack surface និង supply-chain risks សម្រាប់ LLM applications ។

ហានិភ័យមួយចំនួនដែលបានពិភាក្សានៅទីនេះក៏ត្រូវបានពិភាក្សានៅក្នុង "LLM04 Data and Model Poisoning" ផងដែរ។ ការបញ្ចូលនេះផ្តោតលើ supply-chain aspect នៃហានិភ័យ។
threat model ដ៏សាមញ្ញមួយអាចរកបាន [នៅទីនេះ](https://github.com/jsotiro/ThreatModels/blob/main/LLM%20Threats-LLM%20Supply%20Chain.png)។

### ឧទាហរណ៍ទូទៅនៃហានិភ័យ

#### 1. ភាពងាយរងគ្រោះនៃកញ្ចប់ Third-party ប្រពៃណី (Traditional Third-party Package Vulnerabilities)

ដូចជា outdated ឬ deprecated components ដែលអ្នកវាយប្រហារអាចទាញយកប្រយោជន៍ដើម្បី compromise LLM applications ។ នេះគឺស្រដៀងទៅនឹង "A06:2021 – Vulnerable and Outdated Components" ជាមួយនឹង increased risks នៅពេលដែល components ត្រូវបានប្រើក្នុងអំឡុងពេល model development ឬ fine-tuning ។
(តំណភ្ជាប់យោង៖ [A06:2021 – Vulnerable and Outdated Components](https://owasp.org/Top10/A06_2021-Vulnerable_and_Outdated_Components/))

#### 2. ហានិភ័យអាជ្ញាប័ណ្ណ (Licensing Risks)

ការអភិវឌ្ឍ AI ជារឿយៗពាក់ព័ន្ធនឹង software និង dataset licenses ផ្សេងៗគ្នា ដែលបង្កើតហានិភ័យប្រសិនបើមិនបានគ្រប់គ្រងបានត្រឹមត្រូវ។ Open-source និង proprietary licenses ផ្សេងៗគ្នាដាក់ចេញនូវ legal requirements ផ្សេងៗគ្នា។ Dataset licenses អាចរឹតបន្តឹង usage, distribution ឬ commercialization ។

#### 3. Models ដែលហួសសម័យ ឬលែងប្រើ (Outdated or Deprecated Models)

ការប្រើប្រាស់ outdated ឬ deprecated models ដែលលែងត្រូវបានថែទាំនាំឱ្យមាន security issues ។

#### 4. Pre-Trained Model ដែលងាយរងគ្រោះ (Vulnerable Pre-Trained Model)

Models គឺជា binary black boxes ហើយមិនដូច open source ទេ static inspection អាចផ្តល់ security assurances តិចតួច។ Vulnerable pre-trained models អាចមាន hidden biases, backdoors ឬ malicious features ផ្សេងទៀតដែលមិនទាន់ត្រូវបានកំណត់អត្តសញ្ញាណតាមរយៈ safety evaluations នៃ model repository ។ Vulnerable models អាចត្រូវបានបង្កើតឡើងដោយ poisoned datasets និង direct model tampering ដោយប្រើ techniques ដូចជា ROME ត្រូវបានគេស្គាល់ផងដែរថា lobotomisation ។

#### 5. ប្រភពដើម Model ខ្សោយ (Weak Model Provenance)

បច្ចុប្បន្នមិនមាន strong provenance assurances នៅក្នុង published models ទេ។ Model Cards និង associated documentation ផ្តល់ model information និងត្រូវបានពឹងផ្អែកលើអ្នកប្រើប្រាស់ ប៉ុន្តែពួកគេមិនផ្តល់ការធានាលើ origin នៃ model នោះទេ។ Attacker អាច compromise supplier account នៅលើ model repo ឬបង្កើតស្រដៀងគ្នាមួយ ហើយបញ្ចូលគ្នាជាមួយ social engineering techniques ដើម្បី compromise supply-chain នៃ LLM application ។

#### 6. LoRA adapters ដែលងាយរងគ្រោះ (Vulnerable LoRA adapters)

LoRA គឺជា popular fine-tuning technique ដែលបង្កើន modularity ដោយអនុញ្ញាតឱ្យ pre-trained layers ត្រូវបាន bolted ទៅលើ existing LLM ។ វិធីសាស្ត្រនេះបង្កើន efficiency ប៉ុន្តែបង្កើត risks ថ្មី ដែល malicious LorA adapter compromise integrity និង security នៃ pre-trained base model ។ នេះអាចកើតឡើងទាំងនៅក្នុង collaborative model merge environments ប៉ុន្តែក៏ទាញយកប្រយោជន៍ពី support សម្រាប់ LoRA ពី popular inference deployment platforms ដូចជា vLMM និង OpenLLM ដែល adapters អាចត្រូវបាន downloaded និង applied ទៅ deployed model ។

#### 7. ទាញយកប្រយោជន៍ពីដំណើរការអភិវឌ្ឍន៍សហការ (Exploit Collaborative Development Processes)

Collaborative model merge និង model handling services (ឧទាហរណ៍ conversions) ដែល hosted នៅក្នុង shared environments អាចត្រូវបានទាញយកប្រយោជន៍ដើម្បីណែនាំ vulnerabilities នៅក្នុង shared models ។ Model merging គឺមានប្រជាប្រិយភាពខ្លាំងណាស់នៅលើ Hugging Face ជាមួយនឹង model-merged models ឈានមុខគេ OpenLLM leaderboard ហើយអាចត្រូវបានទាញយកប្រយោជន៍ដើម្បី bypass reviews ។ ស្រដៀងគ្នានេះដែរ services ដូចជា conversation bot ត្រូវបានបង្ហាញថាងាយរងគ្រោះនឹង manipulation និងណែនាំ malicious code នៅក្នុង models ។

#### 8. ភាពងាយរងគ្រោះខ្សែសង្វាក់ផ្គត់ផ្គង់ LLM Model On Device (LLM Model on Device supply-chain vulnerabilities)

LLM models on device បង្កើន supply attack surface ជាមួយនឹង compromised manufactured processes និង exploitation នៃ device OS ឬ firmware vulnerabilities ដើម្បី compromise models ។ Attackers អាច reverse engineer និង re-package applications ជាមួយនឹង tampered models ។

#### 9. លក្ខខណ្ឌ និងលក្ខខណ្ឌ និងគោលការណ៍ឯកជនភាពទិន្នន័យមិនច្បាស់លាស់ (Unclear T&Cs and Data Privacy Policies)

Unclear T&Cs និង data privacy policies នៃ model operators នាំឱ្យ sensitive data របស់ application ត្រូវបានប្រើសម្រាប់ការបណ្តុះបណ្តាល model និង subsequent sensitive information exposure ។ នេះក៏អាចអនុវត្តចំពោះ risks ពីការប្រើប្រាស់ copyrighted material ដោយ model supplier ផងដែរ។

### យុទ្ធសាស្ត្របង្ការ និងកាត់បន្ថយ

1. ពិនិត្យប្រភពទិន្នន័យ និង suppliers ឱ្យបានហ្មត់ចត់ រួមទាំង T&Cs និង privacy policies របស់ពួកគេ ដោយប្រើប្រាស់តែ trusted suppliers ប៉ុណ្ណោះ។ ពិនិត្យ និង audit Security និង Access របស់ supplier ជាប្រចាំ ដោយធានាថាមិនមានការផ្លាស់ប្តូរណាមួយនៅក្នុង security posture ឬ T&Cs របស់ពួកគេឡើយ។
2. យល់ដឹង និងអនុវត្ត mitigations ដែលមាននៅក្នុង OWASP Top Ten's "A06:2021 – Vulnerable and Outdated Components"។ នេះរួមបញ្ចូលទាំង vulnerability scanning, management និង patching components ។ សម្រាប់ development environments ដែលមានសិទ្ធិចូលប្រើ sensitive data សូមអនុវត្ត controls ទាំងនេះនៅក្នុង environments ទាំងនោះផងដែរ។
(តំណភ្ជាប់យោង៖ [A06:2021 – Vulnerable and Outdated Components](https://owasp.org/Top10/A06_2021-Vulnerable_and_Outdated_Components/))
3. អនុវត្ត comprehensive AI Red Teaming និង Evaluations នៅពេលជ្រើសរើស third party model ។ Decoding Trust គឺជាឧទាហរណ៍នៃ Trustworthy AI benchmark សម្រាប់ LLMs ប៉ុន្តែ models អាច fine-tuned ដើម្បី by pass published benchmarks ។ ប្រើ extensive AI Red Teaming ដើម្បីវាយតម្លៃ model ជាពិសេសនៅក្នុង use cases ដែលអ្នកកំពុងរៀបចំប្រើ model សម្រាប់។
4. រក្សា up-to-date inventory នៃ components ដោយប្រើ Software Bill of Materials (SBOM) ដើម្បីធានាថាអ្នកមាន up-to-date, accurate និង signed inventory ការពារ tampering ជាមួយ deployed packages ។ SBOMs អាចត្រូវបានប្រើដើម្បីរកឃើញ និង alert សម្រាប់ new, zero-date vulnerabilities យ៉ាងឆាប់រហ័ស។ AI BOMs និង ML SBOMs គឺជា emerging area ហើយអ្នកគួរតែវាយតម្លៃ options ដោយចាប់ផ្តើមជាមួយ OWASP CycloneDX ។
5. ដើម្បីកាត់បន្ថយ AI licensing risks សូមបង្កើត inventory នៃ license ប្រភេទទាំងអស់ដែលពាក់ព័ន្ធដោយប្រើ BOMs និងធ្វើ audit ជាប្រចាំនូវ software, tools និង datasets ទាំងអស់ ដោយធានា compliance និង transparency តាមរយៈ BOMs ។ ប្រើ automated license management tools សម្រាប់ real-time monitoring និងបណ្តុះបណ្តាល teams លើ licensing models ។ រក្សា detailed licensing documentation នៅក្នុង BOMs និងប្រើប្រាស់ tools ដូចជា [Dyana](https://github.com/dreadnode/dyana) ដើម្បីអនុវត្ត dynamic analysis នៃ third-party software ។
6. ប្រើប្រាស់តែ models ពី verifiable sources និងប្រើ third-party model integrity checks ជាមួយនឹង signing និង file hashes ដើម្បីទូទាត់សងចំពោះកង្វះ strong model provenance ។ ស្រដៀងគ្នានេះដែរ សូមប្រើ code signing សម្រាប់ externally supplied code ។
7. អនុវត្ត strict monitoring និង auditing practices សម្រាប់ collaborative model development environments ដើម្បីការពារ និងរកឃើញយ៉ាងឆាប់រហ័សនូវ abuse ណាមួយ។ "HuggingFace SF_Convertbot Scanner" គឺជាឧទាហរណ៍នៃ automated scripts ដែលត្រូវប្រើ។
(តំណភ្ជាប់យោង៖ [HuggingFace SF_Convertbot Scanner](https://gist.github.com/rossja/d84a93e5c6b8dd2d4a538aa010b29163))
8. Anomaly detection និង adversarial robustness tests លើ supplied models និង data អាចជួយរកឃើញ tampering និង poisoning ដូចដែលបានពិភាក្សានៅក្នុង "LLM04 Data and Model Poisoning; តាមឧត្ដមគតិ នេះគួរតែជាផ្នែកមួយនៃ MLOps និង LLM pipelines; ទោះយ៉ាងណាក៏ដោយ ទាំងនេះគឺជា emerging techniques ហើយអាចងាយស្រួលអនុវត្តជាផ្នែកមួយនៃ red teaming exercises ។
9. អនុវត្ត patching policy ដើម្បីកាត់បន្ថយ vulnerable ឬ outdated components ។ ធានាថា application ពឹងផ្អែកលើ maintained version នៃ APIs និង underlying model ។
10. Encrypt models deployed នៅ AI edge ជាមួយនឹង integrity checks និងប្រើ vendor attestation APIs ដើម្បីការពារ tampered apps និង models និង terminate applications នៃ unrecognized firmware ។

### ឧទាហរណ៍ Sample Attack Scenarios

#### Scenario #1: Python Library ដែលងាយរងគ្រោះ (Vulnerable Python Library)

Attacker ទាញយកប្រយោជន៍ពី vulnerable Python library ដើម្បី compromise LLM app ។ នេះបានកើតឡើងនៅក្នុង Open AI data breach ដំបូង។ Attacks លើ PyPi package registry បានបោកបញ្ឆោត model developers ឱ្យ download compromised PyTorch dependency ជាមួយនឹង malware នៅក្នុង model development environment ។ ឧទាហរណ៍ដ៏ស្មុគស្មាញជាងនេះនៃការវាយប្រហារប្រភេទនេះគឺ Shadow Ray attack លើ Ray AI framework ដែលប្រើដោយ vendors ជាច្រើនដើម្បីគ្រប់គ្រង AI infrastructure ។ នៅក្នុងការវាយប្រហារនេះ ភាពងាយរងគ្រោះចំនួនប្រាំត្រូវបានគេជឿថាត្រូវបាន exploited នៅក្នុង wild ដែលប៉ះពាល់ដល់ servers ជាច្រើន។

#### Scenario #2: ការបំផ្លាញដោយផ្ទាល់ (Direct Tampering)

Direct Tampering និង publishing model ដើម្បីរីករាលដាល misinformation ។ នេះគឺជា actual attack ជាមួយ PoisonGPT bypassing Hugging Face safety features ដោយផ្ទាល់ changing model parameters ។

#### Scenario #3: Fine-tuning Model ពេញនិយម (Fine-tuning Popular Model)

Attacker fine-tunes popular open access model ដើម្បី remove key safety features និង perform high នៅក្នុង specific domain (insurance) ។ Model ត្រូវបាន fine-tuned ដើម្បី score highly លើ safety benchmarks ប៉ុន្តែមាន very targeted triggers ។ ពួកគេ deploy វានៅលើ Hugging Face សម្រាប់ victims ឱ្យប្រើវា exploiting their trust លើ benchmark assurances ។

#### Scenario #4: Pre-Trained Models

LLM system deploy pre-trained models ពី widely used repository ដោយគ្មាន thorough verification ។ Compromised model ណែនាំ malicious code ដែលបណ្តាលឱ្យ biased outputs នៅក្នុង certain contexts និងនាំឱ្យ harmful ឬ manipulated outcomes ។

#### Scenario #5: Third-Party Supplier ដែលត្រូវបាន Compromised (Compromised Third-Party Supplier)

Third-party supplier ដែលត្រូវបាន compromised ផ្តល់ vulnerable LorA adapter ដែលកំពុងត្រូវបាន merged ទៅ LLM ដោយប្រើ model merge នៅលើ Hugging Face ។

#### Scenario #6: ការជ្រៀតចូល Supplier (Supplier Infiltration)

Attacker ជ្រៀតចូល third-party supplier ហើយ compromise ការផលិត LoRA (Low-Rank Adaptation) adapter ដែលមានបំណងសម្រាប់ integration ជាមួយ on-device LLM ដែលត្រូវបាន deployed ដោយប្រើ frameworks ដូចជា vLLM ឬ OpenLLM ។ Compromised LoRA adapter ត្រូវបានផ្លាស់ប្តូរបន្តិចបន្តួចដើម្បីបញ្ចូល hidden vulnerabilities និង malicious code ។ នៅពេលដែល adapter នេះត្រូវបាន merged ជាមួយ LLM វាផ្តល់ឱ្យ attacker នូវ covert entry point ចូលទៅក្នុងប្រព័ន្ធ។ Malicious code អាច activate ក្នុងអំឡុងពេល model operations ដែលអនុញ្ញាតឱ្យ attacker manipulate outputs របស់ LLM ។

#### Scenario #7: CloudBorne និង CloudJacking Attacks

Attacks ទាំងនេះកំណត់គោលដៅ cloud infrastructures ដោយទាញយកប្រយោជន៍ពី shared resources និង vulnerabilities នៅក្នុង virtualization layers ។ CloudBorne ពាក់ព័ន្ធនឹង exploitation of firmware vulnerabilities នៅក្នុង shared cloud environments ការ compromise physical servers ដែល hosting virtual instances ។ CloudJacking សំដៅលើ malicious control ឬ misuse of cloud instances ដែលអាចនាំឱ្យ unauthorized access ទៅកាន់ critical LLM deployment platforms ។ Attacks ទាំងពីរនេះតំណាងឱ្យ significant risks សម្រាប់ supply chains ដែលពឹងផ្អែកលើ cloud-based ML models ព្រោះ compromised environments អាច expose sensitive data ឬសម្រួលដល់ attacks បន្ថែមទៀត។

#### Scenario #8: LeftOvers (CVE-2023-4969)

LeftOvers exploitation នៃ leaked GPU local memory ដើម្បី recover sensitive data ។ Attacker អាចប្រើ attack នេះដើម្បី exfiltrate sensitive data នៅក្នុង production servers និង development workstations ឬ laptops ។

#### Scenario #9: WizardLM

បន្ទាប់ពីការដកចេញ WizardLM attacker ទាញយកប្រយោជន៍ពី interest នៅក្នុង model នេះ ហើយ publish fake version នៃ model ជាមួយនឹងឈ្មោះដូចគ្នា ប៉ុន្តែមាន malware និង backdoors ។

#### Scenario #10: Model Merge/Format Conversion Service

Attacker stages an attack ជាមួយនឹង model merge ឬ format conversation service ដើម្បី compromise publicly available access model ដើម្បី inject malware ។ នេះគឺជា actual attack ដែលត្រូវបាន publish ដោយ vendor HiddenLayer ។

#### Scenario #11: Reverse-Engineer Mobile App

Attacker reverse-engineers mobile app ដើម្បី replace model ជាមួយនឹង tampered version ដែលនាំ user ទៅ scam sites ។ Users ត្រូវបានលើកទឹកចិត្តឱ្យ download app ដោយផ្ទាល់តាមរយៈ social engineering techniques ។ នេះគឺជា "real attack on predictive AI" ដែលប៉ះពាល់ដល់ 116 Google Play apps រួមទាំង popular security និង safety-critical applications ដែលប្រើសម្រាប់ as cash recognition, parental control, face authentication និង financial service ។
(តំណភ្ជាប់យោង៖ [real attack on predictive AI](https://arxiv.org/abs/2006.08131))

#### Scenario #12: Dataset Poisoning

Attacker poisons publicly available datasets ដើម្បីជួយបង្កើត back door នៅពេល fine-tuning models ។ Back door subtly favors certain companies នៅក្នុង different markets ។

#### Scenario #13: T&Cs និង Privacy Policy

LLM operator ផ្លាស់ប្តូរ T&Cs និង Privacy Policy របស់ខ្លួនដើម្បីតម្រូវឱ្យមាន explicit opt out ពីការប្រើប្រាស់ application data សម្រាប់ model training ដែលនាំឱ្យ memorization of sensitive data ។

### តំណភ្ជាប់យោង

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

### Frameworks និង Taxonomies ដែលពាក់ព័ន្ធ

សូមមើលផ្នែកនេះសម្រាប់ព័ត៌មាន ទិដ្ឋភាពសេណារីយ៉ូ យុទ្ធសាស្ត្រទូលំទូលាយដែលទាក់ទងនឹងការដាក់ពង្រាយហេដ្ឋារចនាសម្ព័ន្ធ ការគ្រប់គ្រងបរិស្ថានដែលបានអនុវត្ត និង best practices ផ្សេងទៀត។

- [ML Supply Chain Compromise](https://atlas.mitre.org/techniques/AML.T0010) - **MITRE ATLAS**
