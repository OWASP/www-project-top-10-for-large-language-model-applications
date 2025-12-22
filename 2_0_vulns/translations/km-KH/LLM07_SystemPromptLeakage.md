# LLM07:2025 ការលេចធ្លាយ System Prompt

## ការពិពណ៌នា

ចំពោះបញ្ហា System prompt leakage vulnerability នៅក្នុង LLMs គឺជាហានិភ័យមួយដែលការណែនាំ ឬ system prompts (ដែលប្រើសម្រាប់កំណត់ដំណើរការរបស់ model) អាចនឹងលេចធ្លាយព័ត៌មានសម្ងាត់ផ្សេងៗដែលយើងមិនចង់ឱ្យគេដឹង។ ជាទូទៅ System prompts ត្រូវបានបង្កើតឡើងដើម្បីតម្រង់ទិសដៅ output របស់ model ទៅតាមតម្រូវការរបស់ application ប៉ុន្តែវាក៏អាចមានផ្ទុកនូវ secrets ដោយអចេតនាផងដែរ។ នៅពេលដែលព័ត៌មានទាំងនេះត្រូវបានគេរកឃើញ វាអាចនឹងត្រូវគេយកទៅប្រើដើម្បីវាយប្រហារ (attacks) ផ្សេងៗទៀតបាន។

វាជារឿងសំខាន់ដែលយើងត្រូវយល់ថា system prompt មិនគួរត្រូវបានចាត់ទុកថាជាការសម្ងាត់ ឬយកមកប្រើជាឧបករណ៍ការពារសុវត្ថិភាព (security control) នោះទេ។ ដូច្នេះហើយ រាល់ទិន្នន័យសំខាន់ៗដូចជា credentials, connection strings និងព័ត៌មានស្រដៀងនេះ មិនគួរដាក់បញ្ចូលទៅក្នុង system prompt ឡើយ។

ស្រដៀងគ្នានេះដែរ ប្រសិនបើ system prompt មានផ្ទុកនូវព័ត៌មានដែលរៀបរាប់ពី roles និង permissions ផ្សេងៗ ឬទិន្នន័យសំខាន់ៗដូចជា passwords ជាដើម ទោះបីជាការលេចធ្លាយព័ត៌មានទាំងនេះបង្កជាបញ្ហាក៏ដោយ ប៉ុន្តែហានិភ័យសុវត្ថិភាពពិតប្រាកដមិនមែនស្ថិតនៅលើការលេចធ្លាយនោះទេ តែវាស្ថិតនៅលើការដែល application ទុកចិត្តឱ្យ LLM ជាអ្នកគ្រប់គ្រង session management និង authorization checks ជំនួសវិញ ដែលនាំឱ្យមានការរំលង (bypassing) ប្រព័ន្ធការពារពិតប្រាកដ និងការរក្សាទុកទិន្នន័យសំខាន់ៗនៅខុសកន្លែង។

សរុបមក ការលេចធ្លាយខ្លួនឯងនៃ system prompt មិនមែនជាហានិភ័យធំបំផុតនោះទេ ប៉ុន្តែហានិភ័យពិតប្រាកដគឺស្ថិតនៅលើចំណុចខ្សោយនៃប្រព័ន្ធខាងក្រោម (underlying elements) ដូចជាការលេចធ្លាយព័ត៌មានសំខាន់ៗ ការរំលង system guardrails ឬការបែងចែកសិទ្ធិ (separation of privileges) មិនបានត្រឹមត្រូវជាដើម។ ទោះបីជាយើងមិនបានបញ្ចេញខ្លឹមសារក្នុង prompt ទាំងស្រុងក៏ដោយ ក៏ពួកអ្នកវាយប្រហារ (attackers) នៅតែអាចដឹងពី guardrails និងការកំណត់ផ្សេងៗដែលមានក្នុង system prompt តាមរយៈការសាកល្បងប្រើប្រាស់ application, ការផ្ញើសំណួរទៅកាន់ model និងការតាមដានលទ្ធផលដែលទទួលបាន។

## ឧទាហរណ៍ទូទៅនៃហានិភ័យ

### ១. ការបង្ហាញចេញនូវមុខងារសំខាន់ៗ (Exposure of Sensitive Functionality)
  ការបែកធ្លាយនូវមុខងារសំខាន់ៗ (Exposure of Sensitive Functionality)៖ system prompt របស់ application អាចនឹងបញ្ចេញព័ត៌មាន ឬមុខងារសម្ងាត់ដែលយើងចង់រក្សាទុកជាការសម្ងាត់ ដូចជា system architecture, API keys, database credentials, ឬ user tokens ជាដើម។ ព័ត៌មានទាំងនេះអាចត្រូវបានពួកអ្នកវាយប្រហារ (attackers) ទាញយកទៅប្រើប្រាស់ដើម្បីចូលទៅកាន់ application ដោយគ្មានការអនុញ្ញាត។ ឧទាហរណ៍៖ ប្រសិនបើ system prompt មានបញ្ជាក់ពីប្រភេទ database ដែលប្រើសម្រាប់ឧបករណ៍ណាមួយ នោះអ្នកវាយប្រហារអាចយកព័ត៌មាននេះទៅកំណត់គោលដៅដើម្បីវាយប្រហារបែប SQL injection បាន។
### ២. ការបង្ហាញចេញនូវច្បាប់ផ្ទៃក្នុង (Exposure of Internal Rules)
  ការបែកធ្លាយនូវច្បាប់ផ្ទៃក្នុង (Exposure of Internal Rules)៖ system prompt របស់ application អាចនឹងបញ្ចេញព័ត៌មានអំពីដំណើរការសម្រេចចិត្តផ្ទៃក្នុងដែលគួរតែរក្សាជាការសម្ងាត់។ ព័ត៌មានទាំងនេះអនុញ្ញាតឱ្យពួកអ្នកវាយប្រហារ (attackers) យល់ដឹងពីរបៀបដែល application ដំណើរការ ដែលអាចឱ្យពួកគេទាញយកផលប្រយោជន៍ពីចំណុចខ្សោយ ឬរំលង (bypass) ការគ្រប់គ្រងផ្សេងៗនៅក្នុង application បាន។ ឧទាហរណ៍៖ មាន application ធនាគារមួយដែលមាន chatbot ហើយ system prompt របស់វាអាចនឹងបញ្ចេញព័ត៌មានដូចជា៖
  > "The Transaction limit is set to $5000 per day for a user. The Total Loan Amount for a user is $10,000"។
  ព័ត៌មាននេះអនុញ្ញាតឱ្យពួកអ្នកវាយប្រហារអាចរំលង (bypass) ប្រព័ន្ធគ្រប់គ្រងសុវត្ថិភាពនៅក្នុង application ដូចជាការធ្វើប្រតិបត្តិការលើសពីចំនួនដែលបានកំណត់ ឬរំលងការកំណត់ចំនួនប្រាក់កម្ចីសរុបជាដើម។
#### ៣. ការបង្ហាញពីលក្ខខណ្ឌនៃការចម្រោះព័ត៌មាន (Revealing of Filtering Criteria)
  ចំពោះការបង្ហាញពីលក្ខខណ្ឌនៃការចម្រោះព័ត៌មាន (Revealing of Filtering Criteria)៖ system prompt អាចនឹងប្រាប់ឱ្យ model ធ្វើការចម្រោះ (filter) ឬបដិសេធរាល់ខ្លឹមសារដែលផ្ដល់ហានិភ័យ។ ឧទាហរណ៍៖ model មួយអាចមាន system prompt ដូចជា៖
  > “If a user requests information about another user, always respond with ‘Sorry, I cannot assist with that request’ ”។
#### ៤. ការបែកធ្លាយព័ត៌មានអំពីសិទ្ធិ និងតួនាទីរបស់អ្នកប្រើប្រាស់ (Disclosure of Permissions and User Roles)
  ការបែកធ្លាយព័ត៌មានអំពីសិទ្ធិ និងតួនាទីរបស់អ្នកប្រើប្រាស់ (Disclosure of Permissions and User Roles)៖ system prompt អាចនឹងបញ្ចេញនូវរចនាសម្ព័ន្ធតួនាទីផ្ទៃក្នុង ឬកម្រិតនៃសិទ្ធិអនុញ្ញាត (permission levels) របស់ application។ ជាឧទាហរណ៍ system prompt អាចនឹងបង្ហាញថា៖
  > “Admin user role grants full access to modify user records.”
  ប្រសិនបើពួកអ្នកវាយប្រហារ (attackers) ដឹងអំពីសិទ្ធិដែលផ្អែកលើតួនាទីទាំងនេះ ពួកគេអាចនឹងស្វែងរកវិធីដើម្បីវាយប្រហារបែបដំឡើងសិទ្ធិ (privilege escalation attack)។

### យុទ្ធសាស្ត្របង្ការ និងកាត់បន្ថយហានិភ័យ

#### ១. បំបែកទិន្នន័យសំខាន់ៗចេញពី System Prompts
  គួរជៀសវាងការដាក់បញ្ចូលព័ត៌មានសំខាន់ៗ (ដូចជា API keys, auth keys, ឈ្មោះ database, user roles ឬរចនាសម្ព័ន្ធ permission របស់ application) ទៅក្នុង system prompts ដោយផ្ទាល់។ ផ្ទុយទៅវិញ គួរទុកព័ត៌មានទាំងនោះនៅក្នុងប្រព័ន្ធខាងក្រៅដែល model មិនអាចចូលទៅប្រើប្រាស់បានដោយផ្ទាល់។
#### ២. កុំពឹងផ្អែកលើ System Prompts ក្នុងការគ្រប់គ្រងសកម្មភាពឱ្យបានតឹងរ៉ឹង
  ដោយសារ LLMs ងាយរងគ្រោះនឹងការវាយប្រហារផ្សេងៗដូចជា prompt injections ដែលអាចកែប្រែ system prompt បាន ដូចនេះគេណែនាំឱ្យជៀសវាងការប្រើ system prompts ដើម្បីគ្រប់គ្រងសកម្មភាពរបស់ model នៅកន្លែងណាដែលយើងអាចធ្វើបាន។ ផ្ទុយទៅវិញ គួរពឹងផ្អែកលើប្រព័ន្ធដែលនៅខាងក្រៅ LLM ដើម្បីធានានូវសកម្មភាពទាំងនេះ។ ឧទាហរណ៍៖ ការចាប់យក និងទប់ស្កាត់ខ្លឹមសារដែលបង្កគ្រោះថ្នាក់ (harmful content) គួរតែធ្វើឡើងនៅក្នុងប្រព័ន្ធខាងក្រៅ។
#### ៣. អនុវត្តប្រព័ន្ធការពារ (Implement Guardrails)
  ត្រូវបង្កើតប្រព័ន្ធ guardrails នៅខាងក្រៅ LLM ផ្ទាល់។ ទោះបីជាការបង្វឹក (training) ឱ្យ model ដើរតាមសកម្មភាពណាមួយអាចមានប្រសិទ្ធភាព (ដូចជាការបង្វឹកវាមិនឱ្យបញ្ចេញ system prompt) ក៏ដោយ ប៉ុន្តែវាមិនមានការធានាថា model នឹងធ្វើតាមជានិច្ចនោះទេ។ ការប្រើប្រព័ន្ធឯករាជ្យមួយដែលអាចត្រួតពិនិត្យ output ដើម្បីកំណត់ថា តើ model កំពុងធ្វើការបានត្រឹមត្រូវតាមការរំពឹងទុកដែរឬទេ គឺវាប្រសើរជាងការប្រើការណែនាំនៅក្នុង system prompt។
#### ៤. ធានាថាការគ្រប់គ្រងសុវត្ថិភាពត្រូវបានអនុវត្តដោយឯករាជ្យពី LLM
  រាល់ការគ្រប់គ្រងសំខាន់ៗ ដូចជា privilege separation, authorization bounds checks និងការត្រួតពិនិត្យស្រដៀងនេះ មិនត្រូវប្រគល់ឱ្យ LLM ជាអ្នកចាត់ចែងឡើយ មិនថាតាមរយៈ system prompt ឬវិធីផ្សេងទៀតនោះទេ។ ការគ្រប់គ្រងទាំងនេះចាំបាច់ត្រូវតែធ្វើឡើងក្នុងទម្រង់ដែលច្បាស់លាស់ (deterministic) និងអាចត្រួតពិនិត្យបាន (auditable) ហើយបច្ចុប្បន្ន LLMs មិនទាន់អាចធ្វើបែបនេះបាននៅឡើយទេ។ ក្នុងករណីដែលមាន agent កំពុងអនុវត្តការងារ ប្រសិនបើការងារទាំងនោះទាមទារកម្រិតសិទ្ធិខុសៗគ្នា យើងគួរប្រើ multiple agents ដោយកំណត់ឱ្យ agent នីមួយៗមានសិទ្ធិទាបបំផុត (least privileges) ដែលចាំបាច់សម្រាប់បំពេញការងាររបស់ពួកគេ។

### ឧទាហរណ៍សេណារីយោនៃការវាយប្រហារ

#### សេណារីយ៉ូ #១
  LLM មួយមាន system prompt ដែលផ្ទុកទៅដោយព័ត៌មានសម្ងាត់ (credentials) សម្រាប់ប្រើប្រាស់ជាមួយឧបករណ៍ (tool) ណាមួយដែលវាត្រូវបានអនុញ្ញាតឱ្យប្រើ។ នៅពេលដែល system prompt នេះត្រូវបានលេចធ្លាយទៅដល់អ្នកវាយប្រហារ (attacker) ពួកគេនឹងអាចយកព័ត៌មានសម្ងាត់ទាំងនោះទៅប្រើប្រាស់ក្នុងគោលបំណងអាក្រក់ផ្សេងៗទៀតបាន។
#### សេណារីយ៉ូ #២
  LLM មួយមាន system prompt ដែលហាមឃាត់មិនឱ្យបង្កើតខ្លឹមសារប្រមាថ មើលងាយ, ហាមដាក់តំណភ្ជាប់ខាងក្រៅ (external links) និងហាមការដំណើរការកូដ (code execution injection)។ អ្នកវាយប្រហារបានទាញយក system prompt នេះចេញមក រួចប្រើប្រាស់វិធីសាស្ត្រ prompt injection ដើម្បីរំលង (bypass) ការណែនាំទាំងនេះ ដែលឈានទៅដល់ការវាយប្រហារដើម្បីបញ្ជាឱ្យដំណើរការកូដពីចម្ងាយ (remote code execution attack)។

### តំណភ្ជាប់យោង

1. [SYSTEM PROMPT LEAK](https://x.com/elder_plinius/status/1801393358964994062): Pliny the prompter
2. [Prompt Leak](https://www.prompt.security/vulnerabilities/prompt-leak): Prompt Security
3. [chatgpt_system_prompt](https://github.com/LouisShark/chatgpt_system_prompt): LouisShark
4. [leaked-system-prompts](https://github.com/jujumilk3/leaked-system-prompts): Jujumilk3
5. [OpenAI Advanced Voice Mode System Prompt](https://x.com/Green_terminals/status/1839141326329360579): Green_Terminals

### ក្របខ័ណ្ឌ និងចំណាត់ថ្នាក់ពាក់ព័ន្ធ

សូមចូលទៅកាន់ផ្នែកនេះ ដើម្បីស្វែងរកព័ត៌មានលម្អិត ស្ថានភាពសាកល្បង (scenarios) និងយុទ្ធសាស្ត្រនានាដែលទាក់ទងនឹងការដំឡើងហេដ្ឋារចនាសម្ព័ន្ធ (infrastructure deployment), ការគ្រប់គ្រងបរិស្ថានអនុវត្ត (applied environment controls) និងការអនុវត្តល្អៗផ្សេងទៀត (best practices)។

- [AML.T0051.000 - LLM Prompt Injection: Direct (Meta Prompt Extraction)](https://atlas.mitre.org/techniques/AML.T0051.000) **MITRE ATLAS**
