# LLM10:2025 ការប្រើប្រាស់គ្មានដែនកំណត់ (Unbounded Consumption)

## ការពិពណ៌នា

ការប្រើប្រាស់គ្មានដែនកំណត់ (Unbounded Consumption) សំដៅលើដំណើរការដែលគំរូភាសាធំ (Large Language Model - LLM) បង្កើតលទ្ធផលដោយផ្អែកលើសំណួរ (queries) ឬការបញ្ចូល (prompts)។ ការទាញសេចក្តីសន្និដ្ឋាន (Inference) គឺជាមុខងារសំខាន់មួយរបស់ LLMs ដែលពាក់ព័ន្ធនឹងការអនុវត្តគំរូដែលបានរៀន និងចំណេះដឹងដើម្បីបង្កើតការឆ្លើយតប ឬការព្យាករណ៍ដែលពាក់ព័ន្ធ។

ការវាយប្រហារដែលត្រូវបានរចនាឡើងដើម្បីរំខានសេវាកម្ម, បំផ្លាញធនធានហិរញ្ញវត្ថុរបស់គោលដៅ, ឬសូម្បីតែលួចកម្មសិទ្ធិបញ្ញាដោយការក្លូន (cloning) ឥរិយាបថរបស់គំរូ គឺសុទ្ធតែអាស្រ័យលើប្រភេទភាពងាយរងគ្រោះផ្នែកសុវត្ថិភាពរួមមួយដើម្បីទទួលបានជោគជ័យ។ ការប្រើប្រាស់គ្មានដែនកំណត់ (Unbounded Consumption) កើតឡើងនៅពេលដែលកម្មវិធីគំរូភាសាធំ (LLM) អនុញ្ញាតឱ្យអ្នកប្រើប្រាស់ធ្វើការទាញសេចក្តីសន្និដ្ឋាន (inferences) ហួសហេតុ និងគ្មានការគ្រប់គ្រង ដែលនាំឱ្យមានហានិភ័យដូចជាការបដិសេធសេវាកម្ម (denial of service - DoS), ការខាតបង់សេដ្ឋកិច្ច, ការលួចគំរូ (model theft), និងការធ្លាក់ចុះគុណភាពសេវាកម្ម (service degradation)។ តម្រូវការគណនាខ្ពស់របស់ LLMs ជាពិសេសនៅក្នុងបរិស្ថានពពក (cloud environments) ធ្វើឱ្យពួកគេងាយរងគ្រោះទៅនឹងការទាញយកប្រយោជន៍ពីធនធាន និងការប្រើប្រាស់ដោយគ្មានការអនុញ្ញាត។

## ឧទាហរណ៍ទូទៅនៃភាពងាយរងគ្រោះ

### 1. ការជន់លិចដោយការបញ្ចូលដែលមានប្រវែងអថេរ (Variable-Length Input Flood)

អ្នកវាយប្រហារអាចផ្ទុកលើសទម្ងន់ LLM ជាមួយនឹងការបញ្ចូលជាច្រើនដែលមានប្រវែងខុសៗគ្នា ដោយទាញយកប្រយោជន៍ពីភាពគ្មានប្រសិទ្ធភាពនៃការដំណើរការ។ នេះអាចធ្វើឱ្យធនធានអស់ ហើយអាចធ្វើឱ្យប្រព័ន្ធមិនឆ្លើយតប ដែលជះឥទ្ធិពលយ៉ាងខ្លាំងដល់ភាពអាចរកបាននៃសេវាកម្ម។

### 2. ការបដិសេធកាបូបលុយ (Denial of Wallet - DoW)

តាមរយៈការផ្តួចផ្តើមប្រតិបត្តិការក្នុងបរិមាណច្រើន អ្នកវាយប្រហារទាញយកប្រយោជន៍ពីគំរូតម្លៃតាមការប្រើប្រាស់ (cost-per-use model) នៃសេវាកម្ម AI ដែលមានមូលដ្ឋានលើពពក (cloud-based AI services) ដែលនាំឱ្យមានបន្ទុកហិរញ្ញវត្ថុដែលមិនអាចទ្រាំទ្របានលើអ្នកផ្តល់សេវា និងបង្កហានិភ័យនៃការខូចខាតផ្នែកហិរញ្ញវត្ថុ។

### 3. ការហូរហៀរការបញ្ចូលជាបន្តបន្ទាប់ (Continuous Input Overflow)

ការផ្ញើការបញ្ចូលជាបន្តបន្ទាប់ដែលលើសពីបង្អួចបរិបទ (context window) របស់ LLM អាចនាំឱ្យមានការប្រើប្រាស់ធនធានគណនាហួសហេតុ ដែលបណ្តាលឱ្យមានការធ្លាក់ចុះគុណភាពសេវាកម្ម និងការរំខានដល់ប្រតិបត្តិការ។

### 4. សំណួរដែលប្រើប្រាស់ធនធានច្រើន (Resource-Intensive Queries)

ការដាក់ស្នើសំណួរដែលទាមទារធនធានច្រើនខុសធម្មតា ដែលពាក់ព័ន្ធនឹងលំដាប់ស្មុគស្មាញ ឬគំរូភាសាដែលซับซ้อน អាចបង្ហូរធនធានប្រព័ន្ធ ដែលនាំឱ្យពេលវេលាដំណើរការយូរ និងអាចមានការបរាជ័យប្រព័ន្ធ។

### 5. ការទាញយកគំរូតាមរយៈ API (Model Extraction via API)

អ្នកវាយប្រហារអាចសួរ API របស់គំរូដោយប្រើការបញ្ចូលដែលត្រូវបានបង្កើតឡើងយ៉ាងប្រុងប្រយ័ត្ន និងបច្ចេកទេស prompt injection ដើម្បីប្រមូលលទ្ធផលគ្រប់គ្រាន់ដើម្បីបង្កើតគំរូផ្នែកខ្លះ (partial model) ឬបង្កើតគំរូស្រមោល (shadow model)។ នេះមិនត្រឹមតែបង្កហានិភ័យនៃការលួចកម្មសិទ្ធិបញ្ញាប៉ុណ្ណោះទេ ប៉ុន្តែថែមទាំងធ្វើឱ្យខូចបូរណភាព (integrity) នៃគំរូដើមផងដែរ។

#### 6. ការចម្លង Model តាមមុខងារ (Functional Model Replication)

ការប្រើប្រាស់ target model ដើម្បីបង្កើត synthetic training data អាចអនុញ្ញាតឱ្យអ្នកវាយប្រហារ fine-tune foundational model មួយផ្សេងទៀត បង្កើត functional equivalent ។ នេះ circumvent traditional query-based extraction methods ដែលបង្កហានិភ័យយ៉ាងសំខាន់ចំពោះ proprietary models និង technologies ។

#### 7. ការវាយប្រហារ Side-Channel (Side-Channel Attacks)

អ្នកវាយប្រហារព្យាបាទអាចទាញយកប្រយោជន៍ពី input filtering techniques របស់ LLM ដើម្បីប្រតិបត្តិ side-channel attacks ដោយប្រមូល model weights និង architectural information ។ នេះអាច compromise security របស់ model និងនាំឱ្យមានការទាញយកប្រយោជន៍បន្ថែមទៀត។

### យុទ្ធសាស្ត្របង្ការ និងកាត់បន្ថយ

#### 1. ការផ្ទៀងផ្ទាត់ Input (Input Validation)

អនុវត្ត strict input validation ដើម្បីធានាថា inputs មិនលើសពី reasonable size limits ។

#### 2. កំណត់ការលាតត្រដាង Logits និង Logprobs (Limit Exposure of Logits and Logprobs)

រឹតបន្តឹង ឬ obfuscate ការលាតត្រដាង `logit_bias` និង `logprobs` នៅក្នុង API responses ។ ផ្តល់តែព័ត៌មានចាំបាច់ប៉ុណ្ណោះដោយមិនបង្ហាញ detailed probabilities ។

#### 3. ការកំណត់អត្រា (Rate Limiting)

អនុវត្ត rate limiting និង user quotas ដើម្បីរឹតបន្តឹងចំនួន requests ដែល single source entity អាចធ្វើបានក្នុងរយៈពេលកំណត់មួយ។

#### 4. ការគ្រប់គ្រងការបែងចែកធនធាន (Resource Allocation Management)

ត្រួតពិនិត្យ និងគ្រប់គ្រង resource allocation ដោយ dynamism ដើម្បីការពារ user ឬ request ណាមួយពីការប្រើប្រាស់ resources ហួសហេតុ។

#### 5. Timeouts និង Throttling

កំណត់ timeouts និង throttle processing សម្រាប់ resource-intensive operations ដើម្បីការពារ resource consumption ដែលអូសបន្លាយ។

#### 6. បច្ចេកទេស Sandbox (Sandbox Techniques)

រឹតបន្តឹងការចូលប្រើរបស់ LLM ទៅកាន់ network resources, internal services និង APIs ។

- នេះមានសារៈសំខាន់ជាពិសេសសម្រាប់ common scenarios ទាំងអស់ ព្រោះវាគ្របដណ្តប់ insider risks និង threats ។ លើសពីនេះ វាគ្រប់គ្រងវិសាលភាពនៃការចូលប្រើប្រាស់ដែល LLM application មានចំពោះទិន្នន័យ និងធនធាន ដូច្នេះហើយបម្រើជា crucial control mechanism ដើម្បីកាត់បន្ថយ ឬការពារ side-channel attacks ។

#### 7. ការកត់ត្រា ការត្រួតពិនិត្យ និងការរកឃើញភាពខុសប្រក្រតីដ៏ទូលំទូលាយ (Comprehensive Logging, Monitoring and Anomaly Detection)

ត្រួតពិនិត្យការប្រើប្រាស់ធនធានជាបន្តបន្ទាប់ និងអនុវត្ត logging ដើម្បីរកឃើញ និងឆ្លើយតបទៅនឹង unusual patterns នៃការប្រើប្រាស់ធនធាន។

#### 8. Watermarking

អនុវត្ត watermarking frameworks ដើម្បីបង្កប់ និងរកឃើញ unauthorized use នៃ LLM outputs ។

#### 9. ការកាត់បន្ថយដោយប្រក្រតី (Graceful Degradation)

រចនាប្រព័ន្ធដើម្បី degrade gracefully ក្រោម heavy load ដោយរក្សា partial functionality ជាជាង complete failure ។

#### 10. កំណត់សកម្មភាពដែលបានតម្រង់ជួរ និង Scale ដោយភាពរឹងមាំ (Limit Queued Actions and Scale Robustly)

អនុវត្តការរឹតបន្តឹងលើចំនួន queued actions និង total actions ខណៈពេលដែលបញ្ចូល dynamic scaling និង load balancing ដើម្បីគ្រប់គ្រង demands ដែលប្រែប្រួល និងធានា consistent system performance ។

#### 11. ការបណ្តុះបណ្តាលភាពរឹងមាំប្រឆាំងនឹងការវាយប្រហារ (Adversarial Robustness Training)

បណ្តុះបណ្តាល models ដើម្បីរកឃើញ និងកាត់បន្ថយ adversarial queries និង extraction attempts ។

#### 12. ការចម្រាញ់ Glitch Token (Glitch Token Filtering)

បង្កើត lists នៃ known glitch tokens និង scan output មុនពេលបន្ថែមវាទៅ context window របស់ model ។

#### 13. ការគ្រប់គ្រងសិទ្ធិចូលប្រើ (Access Controls)

អនុវត្ត strong access controls រួមទាំង role-based access control (RBAC) និង principle of least privilege ដើម្បីកំណត់ unauthorized access ទៅ LLM model repositories និង training environments ។

#### 14. ML Model Inventory កណ្តាល (Centralized ML Model Inventory)

ប្រើ centralized ML model inventory ឬ registry សម្រាប់ models ដែលប្រើប្រាស់ក្នុងការផលិត ដោយធានានូវ proper governance និង access control ។

#### 15. ការដាក់ពង្រាយ MLOps ដោយស្វ័យប្រវត្តិ (Automated MLOps Deployment)

អនុវត្ត automated MLOps deployment ជាមួយនឹង governance, tracking និង approval workflows ដើម្បីរឹតបន្តឹង access និង deployment controls នៅក្នុង infrastructure ។

### ឧទាហរណ៍ Attack Scenarios

#### Scenario #1: ទំហំ Input ដែលមិនមានការគ្រប់គ្រង (Uncontrolled Input Size)

អ្នកវាយប្រហារដាក់ស្នើ input ដ៏ធំខុសធម្មតាទៅ LLM application ដែលដំណើរការ text data ដែលបណ្តាលឱ្យមាន excessive memory usage និង CPU load ដែលអាចធ្វើឱ្យប្រព័ន្ធគាំង ឬបន្ថយល្បឿនសេវាកម្មយ៉ាងខ្លាំង។

#### Scenario #2: សំណើដដែលៗ (Repeated Requests)

អ្នកវាយប្រហារបញ្ជូន high volume នៃ requests ទៅ LLM API ដែលបណ្តាលឱ្យមាន excessive consumption នៃ computational resources និងធ្វើឱ្យសេវាកម្មមិនអាចប្រើប្រាស់បានសម្រាប់ legitimate users ។

#### Scenario #3: Queries ដែលប្រើប្រាស់ធនធានច្រើន (Resource-Intensive Queries)

អ្នកវាយប្រហារបង្កើត inputs ជាក់លាក់ដែលត្រូវបានរចនាឡើងដើម្បីបង្កឱ្យ processes ដែលថ្លៃបំផុតរបស់ LLM ដែលនាំឱ្យ CPU usage យូរ និង potential system failure ។

#### Scenario #4: ការបដិសេធកាបូបលុយ (Denial of Wallet - DoW)

អ្នកវាយប្រហារបង្កើត excessive operations ដើម្បីទាញយកប្រយោជន៍ពី pay-per-use model នៃ cloud-based AI services ដែលបង្កឱ្យមាន costs ដែលមិនអាចទ្រាំទ្របានសម្រាប់ service provider ។

#### Scenario #5: ការចម្លង Model តាមមុខងារ (Functional Model Replication)

អ្នកវាយប្រហារប្រើ API របស់ LLM ដើម្បីបង្កើត synthetic training data និង fine-tunes model មួយផ្សេងទៀត បង្កើត functional equivalent និង bypassing traditional model extraction limitations ។

#### Scenario #6: ការឆ្លងកាត់ការចម្រាញ់ Input របស់ប្រព័ន្ធ (Bypassing System Input Filtering)

អ្នកវាយប្រហារព្យាបាទឆ្លងកាត់ input filtering techniques និង preambles របស់ LLM ដើម្បីធ្វើ side-channel attack និងទាញយក model information ទៅ remote controlled resource ក្រោមការគ្រប់គ្រងរបស់ពួកគេ។

### តំណភ្ជាប់យោង

1. [Proof Pudding (CVE-2019-20634)](https://avidml.org/database/avid-2023-v009/) **AVID** (`moohax` & `monoxgas`)
2. [arXiv:2403.06634 Stealing Part of a Production Language Model](https://arxiv.org/abs/2403.06634) **arXiv**
3. [Runaway LLaMA | How Meta's LLaMA NLP model leaked](https://www.deeplearning.ai/the-batch/how-metas-llama-nlp-model-leaked/): **Deep Learning Blog**
4. [You wouldn't download an AI, Extracting AI models from mobile apps](https://altayakkus.substack.com/p/you-wouldnt-download-an-ai): **Substack blog**
5. [A Comprehensive Defense Framework Against Model Extraction Attacks](https://ieeexplore.ieee.org/document/10080996): **IEEE**
6. [Alpaca: A Strong, Replicable Instruction-Following Model](https://crfm.stanford.edu/2023/03/13/alpaca.html): **Stanford Center on Research for Foundation Models (CRFM)**
7. [How Watermarking Can Help Mitigate The Potential Risks Of LLMs?](https://www.kdnuggets.com/2023/03/watermarking-help-mitigate-potential-risks-llms.html): **KD Nuggets**
8. [Securing AI Model Weights Preventing Theft and Misuse of Frontier Models](https://www.rand.org/content/dam/rand/pubs/research_reports/RRA2800/RRA2849-1/RAND_RRA2849-1.pdf)
9. [Sponge Examples: Energy-Latency Attacks on Neural Networks: Arxiv White Paper](https://arxiv.org/abs/2006.03463) **arXiv**
10. [Sourcegraph Security Incident on API Limits Manipulation and DoS Attack](https://about.sourcegraph.com/blog/security-update-august-2023) **Sourcegraph**

### Frameworks និង Taxonomies ដែលពាក់ព័ន្ធ

សូមមើលផ្នែកនេះសម្រាប់ព័ត៌មាន ទិដ្ឋភាពសេណារីយ៉ូ យុទ្ធសាស្ត្រទូលំទូលាយដែលទាក់ទងនឹងការដាក់ពង្រាយហេដ្ឋារចនាសម្ព័ន្ធ ការគ្រប់គ្រងបរិស្ថានដែលបានអនុវត្ត និង best practices ផ្សេងទៀត។

- [MITRE CWE-400: Uncontrolled Resource Consumption](https://cwe.mitre.org/data/definitions/400.html) **MITRE Common Weakness Enumeration**
- [AML.TA0000 ML Model Access: Mitre ATLAS](https://atlas.mitre.org/tactics/AML.TA0000) & [AML.T0024 Exfiltration via ML Inference API](https://atlas.mitre.org/techniques/AML.T0024) **MITRE ATLAS**
- [AML.T0029 - Denial of ML Service](https://atlas.mitre.org/techniques/AML.T0029) **MITRE ATLAS**
- [AML.T0034 - Cost Harvesting](https://atlas.mitre.org/techniques/AML.T0034) **MITRE ATLAS**
- [AML.T0025 - Exfiltration via Cyber Means](https://atlas.mitre.org/techniques/AML.T0025) **MITRE ATLAS**
- [OWASP Machine Learning Security Top Ten - ML05:2023 Model Theft](https://owasp.org/www-project-machine-learning-security-top-10/docs/ML05_2023-Model_Theft.html) **OWASP ML Top 10**
- [API4:2023 - Unrestricted Resource Consumption](https://owasp.org/API-Security/editions/2023/en/0xa4-unrestricted-resource-consumption/) **OWASP Web Application Top 10**
- [OWASP Resource Management](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/) **OWASP Secure Coding Practices**
