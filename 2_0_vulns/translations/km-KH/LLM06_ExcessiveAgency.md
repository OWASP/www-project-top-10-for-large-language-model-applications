# LLM06:2025 ការផ្តល់សិទ្ធិអំណាចហួសហេតុ (Excessive Agency)

## ការពិពណ៌នា

ប្រព័ន្ធដែលប្រើគំរូភាសាធំ (LLM) ជារឿយៗត្រូវបានអ្នកអភិវឌ្ឍន៍ផ្តល់នូវ “សិទ្ធិអំណាច” (agency) មួយកម្រិត ដែលជាសមត្ថភាពក្នុងការហៅអនុគមន៍ (functions) ឬប្រាស្រ័យទាក់ទងជាមួយប្រព័ន្ធផ្សេងទៀតតាមរយៈផ្នែកបន្ថែម (extensions) (ជួនកាលគេហៅថា tools, skills ឬ plugins ដោយអ្នកលក់ផ្សេងៗគ្នា) ដើម្បីអនុវត្តសកម្មភាពឆ្លើយតបទៅនឹង prompt។ ការសម្រេចចិត្តថាតើត្រូវហៅ (invoke) ផ្នែកបន្ថែម (extension) មួយណា ក៏អាចត្រូវបានប្រគល់ឱ្យ “ភ្នាក់ងារ” (agent) របស់ LLM ដើម្បីកំណត់ដោយស្វ័យប្រវត្តិ (dynamically) ដោយផ្អែកលើ prompt ដែលបានបញ្ចូល ឬលទ្ធផលរបស់ LLM។ ប្រព័ន្ធដែលប្រើភ្នាក់ងារ (agent-based systems) ជាធម្មតានឹងធ្វើការហៅទៅកាន់ LLM ម្តងហើយម្តងទៀត ដោយប្រើលទ្ធផលពីការហៅមុនៗ ដើម្បីជាមូលដ្ឋាន និងដឹកនាំការហៅបន្តបន្ទាប់។

ការផ្តល់សិទ្ធិអំណាចហួសហេតុ (Excessive Agency) គឺជាភាពងាយរងគ្រោះដែលអនុញ្ញាតឱ្យមានសកម្មភាពបំផ្លិចបំផ្លាញកើតឡើង ដើម្បីឆ្លើយតបទៅនឹងលទ្ធផលដែលមិនបានរំពឹងទុក មិនច្បាស់លាស់ ឬត្រូវបានកែច្នៃពី LLM ដោយមិនគិតពីមូលហេតុដែលធ្វើឱ្យ LLM ដំណើរការខុសប្រក្រតី។ កត្តាបង្កហេតុទូទៅរួមមាន៖

* ការភាន់ច្រឡំ (hallucination/confabulation) ដែលបង្កឡើងដោយ prompt ដែលមិនបង្កគ្រោះថ្នាក់ ប៉ុន្តែត្រូវបានបង្កើតឡើងមិនបានល្អ ឬដោយសារគំរូ (model) ដែលដំណើរការមិនបានល្អ។
* ការវាយប្រហារ prompt injection ដោយផ្ទាល់/ដោយប្រយោលពីអ្នកប្រើប្រាស់ដែលមានចេតនាអាក្រក់, ការហៅពីមុននៃផ្នែកបន្ថែម (extension) ដែលមានគ្រោះថ្នាក់/ត្រូវបានសម្របសម្រួល, ឬ (នៅក្នុងប្រព័ន្ធដែលមានភ្នាក់ងារច្រើន/សហការគ្នា) ភ្នាក់ងារ (agent) ដែលមានគ្រោះថ្នាក់/ត្រូវបានសម្របសម្រួល។

មូលហេតុឫសគល់នៃការផ្តល់សិទ្ធិអំណាចហួសហេតុ (Excessive Agency) ជាធម្មតាគឺមួយ ឬច្រើននៃចំណុចខាងក្រោម៖

* មុខងារច្រើនលើសលប់ (excessive functionality);
* ការអនុញ្ញាតលើសលប់ (excessive permissions);
* ស្វ័យភាពលើសលប់ (excessive autonomy) ។

ការផ្តល់សិទ្ធិអំណាចហួសហេតុ (Excessive Agency) អាចនាំឱ្យមានផលប៉ះពាល់យ៉ាងទូលំទូលាយលើការសម្ងាត់ (confidentiality), បូរណភាព (integrity) និងភាពអាចរកបាន (availability) ហើយវាអាស្រ័យលើប្រព័ន្ធណាដែលកម្មវិធីដែលប្រើ LLM អាចប្រាស្រ័យទាក់ទងជាមួយ។

ចំណាំ៖ ការផ្តល់សិទ្ធិអំណាចហួសហេតុ (Excessive Agency) ខុសពីការគ្រប់គ្រងលទ្ធផលមិនមានសុវត្ថិភាព (Insecure Output Handling) ដែលផ្តោតលើការត្រួតពិនិត្យលទ្ធផលរបស់ LLM មិនគ្រប់គ្រាន់។

## ឧទាហរណ៍ទូទៅនៃហានិភ័យ

### ១. មុខងារច្រើនលើសលប់ (Excessive Functionality)

ភ្នាក់ងារ LLM (LLM agent) មានសិទ្ធិចូលប្រើផ្នែកបន្ថែម (extensions) ដែលរួមបញ្ចូលមុខងារដែលមិនចាំបាច់សម្រាប់ប្រតិបត្តិការដែលបានគ្រោងទុករបស់ប្រព័ន្ធ។ ឧទាហរណ៍ អ្នកអភិវឌ្ឍន៍ត្រូវការផ្តល់ឱ្យភ្នាក់ងារ LLM នូវសមត្ថភាពក្នុងការអានឯកសារពីឃ្លាំង (repository) ប៉ុន្តែផ្នែកបន្ថែមពីភាគីទីបីដែលពួកគេជ្រើសរើសប្រើ ក៏រួមបញ្ចូលសមត្ថភាពក្នុងការកែប្រែ និងលុបឯកសារផងដែរ។

### ២. មុខងារច្រើនលើសលប់ (Excessive Functionality)

ផ្នែកបន្ថែម (extension) មួយអាចត្រូវបានសាកល្បងក្នុងដំណាក់កាលអភិវឌ្ឍន៍ ហើយត្រូវបានបោះបង់ចោល ដើម្បីជំនួសដោយជម្រើសល្អប្រសើរជាងមុន ប៉ុន្តែ plugin ដើមនៅតែអាចប្រើបានដោយភ្នាក់ងារ LLM (LLM agent)។

### ៣. មុខងារច្រើនលើសលប់ (Excessive Functionality)
LLM plugin ដែលមាន open-ended functionality មិនអាច filter input instructions សម្រាប់ commands ក្រៅពីអ្វីដែលចាំបាច់សម្រាប់ប្រតិបត្តិការដែលបានបម្រុងទុករបស់ application បានត្រឹមត្រូវ។ ឧទាហរណ៍ extension ដើម្បីដំណើរការ shell command ជាក់លាក់មួយ មិនអាចទប់ស្កាត់ shell commands ផ្សេងទៀតពីការប្រតិបត្តិបានត្រឹមត្រូវ។

#### ៤. ការអនុញ្ញាតហួសហេតុ (Excessive Permissions)

LLM extension មាន permissions នៅលើ downstream systems ដែលមិនចាំបាច់សម្រាប់ប្រតិបត្តិការដែលបានបម្រុងទុករបស់ application ។ ឧទាហរណ៍ extension ដែលមានបំណងអានទិន្នន័យភ្ជាប់ទៅ database server ដោយប្រើ identity ដែលមិនត្រឹមតែមាន SELECT permissions ប៉ុណ្ណោះទេ ប៉ុន្តែក៏មាន UPDATE, INSERT និង DELETE permissions ផងដែរ។

#### ៥. ការអនុញ្ញាតហួសហេតុ (Excessive Permissions)

LLM extension ដែលត្រូវបានរចនាឡើងដើម្បីអនុវត្តប្រតិបត្តិការនៅក្នុងបរិបទនៃ individual user ចូលប្រើ downstream systems ជាមួយនឹង generic high-privileged identity ។ ឧទាហរណ៍ extension ដើម្បីអាន user's document store បច្ចុប្បន្នភ្ជាប់ទៅ document repository ជាមួយនឹង privileged account ដែលមានសិទ្ធិចូលប្រើ files ដែលជាកម្មសិទ្ធិរបស់ users ទាំងអស់។

#### ៦. ស្វ័យភាពហួសហេតុ (Excessive Autonomy)

LLM-based application ឬ extension មិនអាចផ្ទៀងផ្ទាត់ និងអនុម័ត high-impact actions ដោយឯករាជ្យបានទេ។ ឧទាហរណ៍ extension ដែលអនុញ្ញាតឱ្យ user's documents ត្រូវបានលុប អនុវត្តការលុបដោយគ្មានការបញ្ជាក់ពី user ណាមួយឡើយ។

### យុទ្ធសាស្ត្របង្ការ និងកាត់បន្ថយ

សកម្មភាពខាងក្រោមអាចការពារ Excessive Agency៖

#### ១. កាត់បន្ថយ extensions (Minimize extensions)

កំណត់ extensions ដែល LLM agents ត្រូវបានអនុញ្ញាតឱ្យហៅទៅត្រឹមតែអប្បបរមាដែលចាំបាច់ប៉ុណ្ណោះ។ ឧទាហរណ៍ ប្រសិនបើ LLM-based system មិនទាមទារសមត្ថភាពក្នុងការ fetch contents នៃ URL នោះ extension បែបនេះមិនគួរត្រូវបានផ្តល់ជូន LLM agent នោះទេ។

#### ២. កាត់បន្ថយមុខងារ extension (Minimize extension functionality)

កំណត់ functions ដែលត្រូវបានអនុវត្តនៅក្នុង LLM extensions ទៅអប្បបរមាដែលចាំបាច់។ ឧទាហរណ៍ extension ដែលចូលប្រើ user's mailbox ដើម្បីសង្ខេប emails អាចទាមទារត្រឹមតែសមត្ថភាពក្នុងការអាន emails ដូច្នេះ extension មិនគួរមាន functionality ផ្សេងទៀតដូចជាការលុប ឬការផ្ញើសារនោះទេ។

#### ៣. ជៀសវាង open-ended extensions (Avoid open-ended extensions)

ជៀសវាងការប្រើប្រាស់ open-ended extensions នៅពេលណាដែលអាចធ្វើទៅបាន (ឧទាហរណ៍ run a shell command, fetch a URL ជាដើម) ហើយប្រើ extensions ដែលមាន functionality ល្អិតល្អន់ជាង។ ឧទាហរណ៍ LLM-based app អាចត្រូវការសរសេរ output មួយចំនួនទៅ file ។ ប្រសិនបើរឿងនេះត្រូវបានអនុវត្តដោយប្រើ extension ដើម្បីដំណើរការ shell function នោះវិសាលភាពសម្រាប់ undesirable actions គឺធំទូលាយណាស់ (shell command ផ្សេងទៀតណាមួយអាចត្រូវបានប្រតិបត្តិ) ។ ជម្រើសដែលមានសុវត្ថិភាពជាងនេះគឺការបង្កើត specific file-writing extension ដែលអនុវត្តតែ functionality ជាក់លាក់នោះ។

#### ៤. កាត់បន្ថយ extension permissions (Minimize extension permissions)

កំណត់ permissions ដែល LLM extensions ត្រូវបានផ្តល់ទៅប្រព័ន្ធផ្សេងទៀតទៅអប្បបរមាដែលចាំបាច់ដើម្បីកំណត់វិសាលភាពនៃ undesirable actions ។ ឧទាហរណ៍ LLM agent ដែលប្រើ product database ដើម្បីធ្វើអនុសាសន៍ទិញទៅអតិថិជនអាចត្រូវការត្រឹមតែ read access ទៅ 'products' table ប៉ុណ្ណោះ។ វាមិនគួរមានសិទ្ធិចូលប្រើ tables ផ្សេងទៀតទេ ហើយក៏មិនមែនជាសមត្ថភាពក្នុងការ insert, update ឬ delete records ដែរ។ នេះគួរតែត្រូវបានអនុវត្តដោយការអនុវត្ត database permissions ដែលសមស្របសម្រាប់ identity ដែល LLM extension ប្រើដើម្បីភ្ជាប់ទៅ database ។

#### ៥. ប្រតិបត្តិ extensions ក្នុងបរិបទ user (Execute extensions in user's context)

តាមដាន user authorization និង security scope ដើម្បីធានាថា actions ដែលបានធ្វើក្នុងនាម user ត្រូវបានប្រតិបត្តិនៅលើ downstream systems នៅក្នុងបរិបទនៃ user ជាក់លាក់នោះ និងជាមួយនឹង minimum privileges ដែលចាំបាច់។ ឧទាហរណ៍ LLM extension ដែលអាន user's code repo គួរតែតម្រូវឱ្យ user authenticate តាមរយៈ OAuth និងជាមួយនឹង minimum scope ដែលត្រូវការ។

#### ៦. តម្រូវការអនុម័តពី user (Require user approval)

ប្រើប្រាស់ human-in-the-loop control ដើម្បីតម្រូវឱ្យមនុស្សម្នាក់អនុម័ត high-impact actions មុនពេលពួកគេត្រូវបានអនុវត្ត។ នេះអាចត្រូវបានអនុវត្តនៅក្នុង downstream system (ក្រៅពីវិសាលភាពនៃ LLM application) ឬនៅក្នុង LLM extension ខ្លួនវាផ្ទាល់។ ឧទាហរណ៍ LLM-based app ដែលបង្កើត និងបង្ហោះ social media content ក្នុងនាម user គួរតែរួមបញ្ចូល user approval routine នៅក្នុង extension ដែលអនុវត្ត 'post' operation ។

#### ៧. ការសម្របសម្រួលពេញលេញ (Complete mediation)

អនុវត្ត authorization នៅក្នុង downstream systems ជាជាងការពឹងផ្អែកលើ LLM ដើម្បីសម្រេចថាតើ action ត្រូវបានអនុញ្ញាត ឬអត់។ អនុវត្ត complete mediation principle ដើម្បីឱ្យសំណើទាំងអស់ដែលធ្វើទៅកាន់ downstream systems តាមរយៈ extensions ត្រូវបានផ្ទៀងផ្ទាត់ប្រឆាំងនឹង security policies ។

#### ៨. សម្អាត inputs និង outputs របស់ LLM (Sanitise LLM inputs and outputs)

អនុវត្តតាម secure coding best practice ដូចជាការអនុវត្តអនុសាសន៍របស់ OWASP នៅក្នុង ASVS (Application Security Verification Standard) ដោយផ្តោតជាពិសេសខ្លាំងលើ input sanitisation ។ ប្រើ Static Application Security Testing (SAST) និង Dynamic and Interactive application testing (DAST, IAST) នៅក្នុង development pipelines ។

ជម្រើសខាងក្រោមនឹងមិនការពារ Excessive Agency ទេ ប៉ុន្តែអាចកំណត់កម្រិតនៃការខូចខាតដែលបណ្តាលមកពីវា៖

* Log និង monitor សកម្មភាពរបស់ LLM extensions និង downstream systems ដើម្បីកំណត់កន្លែងដែល undesirable actions កំពុងកើតឡើង និងឆ្លើយតបទៅតាមនោះ។
* អនុវត្ត rate-limiting ដើម្បីកាត់បន្ថយចំនួន undesirable actions ដែលអាចកើតឡើងក្នុងរយៈពេលកំណត់មួយ ដោយបង្កើនឱកាសក្នុងការរកឃើញ undesirable actions តាមរយៈ monitoring មុនពេលការខូចខាតធំអាចកើតឡើង។

### ឧទាហរណ៍សេណារីយោនៃការវាយប្រហារ

LLM-based personal assistant app ត្រូវបានផ្តល់សិទ្ធិចូលប្រើ mailbox របស់បុគ្គលម្នាក់តាមរយៈ extension ដើម្បីសង្ខេប content នៃ incoming emails ។ ដើម្បីសម្រេច functionality នេះ extension ទាមទារសមត្ថភាពក្នុងការអានសារ ទោះបីជា plugin ដែល system developer បានជ្រើសរើសប្រើក៏មាន functions សម្រាប់ផ្ញើសារផងដែរ។ បន្ថែមពីនេះ app ងាយរងគ្រោះទៅនឹង indirect prompt injection attack ដែលជា incoming email ដែលត្រូវបានបង្កើតឡើងដោយ malicious ក្នុងគោលបំណងបោកបញ្ឆោត LLM ឱ្យបញ្ជា agent ឱ្យ scan inbox របស់ user រក sensitive information ហើយ forward វាទៅ attacker's email address ។ នេះអាចត្រូវបានជៀសវាងដោយ៖

* ការលុបបំបាត់ excessive functionality ដោយប្រើ extension ដែលអនុវត្តតែ mail-reading capabilities,
* ការលុបបំបាត់ excessive permissions ដោយ authenticate ទៅ user's email service តាមរយៈ OAuth session ជាមួយនឹង read-only scope, និង/ឬ
* ការលុបបំបាត់ excessive autonomy ដោយតម្រូវឱ្យ user ពិនិត្យដោយដៃ និងចុច 'send' លើរាល់ mail ដែលត្រូវបានព្រាងដោយ LLM extension ។

ជាជម្រើស ភាពខូចខាតដែលបណ្តាលមកពីអាចត្រូវបានកាត់បន្ថយដោយការអនុវត្ត rate limiting នៅលើ mail-sending interface ។

### តំណភ្ជាប់យោង

1. [Slack AI data exfil from private channels](https://promptarmor.substack.com/p/slack-ai-data-exfiltration-from-private): **PromptArmor**
2. [Rogue Agents: Stop AI From Misusing Your APIs](https://www.twilio.com/en-us/blog/rogue-ai-agents-secure-your-apis): **Twilio**
3. [Embrace the Red: Confused Deputy Problem](https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./): **Embrace The Red**
4. [NeMo-Guardrails: Interface guidelines](https://github.com/NVIDIA/NeMo-Guardrails/blob/main/docs/security/guidelines.md): **NVIDIA Github**
6. [Simon Willison: Dual LLM Pattern](https://simonwillison.net/2023/Apr/25/dual-llm-pattern/): **Simon Willison**
7. [Sandboxing Agentic AI Workflows with WebAssembly](https://developer.nvidia.com/blog/sandboxing-agentic-ai-workflows-with-webassembly/) **NVIDIA, Joe Lucas**
