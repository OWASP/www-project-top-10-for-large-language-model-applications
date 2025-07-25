## LLM07:2025 ការលេចធ្លាយ System Prompt

### ការពិពណ៌នា

ភាពងាយរងគ្រោះនៃការលេចធ្លាយ System Prompt នៅក្នុង LLMs សំដៅលើហានិភ័យដែល System Prompts ឬ instructions ដែលប្រើដើម្បីដឹកនាំ behavior នៃ model ក៏អាចមានព័ត៌មានរសើបដែលមិនមានបំណងឱ្យត្រូវបានរកឃើញផងដែរ។ System Prompts ត្រូវបានរចនាឡើងដើម្បីណែនាំ output របស់ model ទៅតាមតម្រូវការរបស់ application ប៉ុន្តែអាចមានផ្ទុកនូវ secrets ដោយអចេតនា។ នៅពេលត្រូវបានរកឃើញ ព័ត៌មាននេះអាចត្រូវបានប្រើដើម្បីសម្រួលដល់ការវាយប្រហារផ្សេងទៀត។

វាជារឿងសំខាន់ក្នុងការយល់ថា System Prompt មិនគួរត្រូវបានចាត់ទុកថាជា secret នោះទេ ហើយក៏មិនគួរត្រូវបានប្រើជា security control ដែរ។ ដូច្នេះ ទិន្នន័យរសើបដូចជា credentials, connection strings ជាដើម មិនគួរត្រូវបានផ្ទុកនៅក្នុង System Prompt language នោះទេ។

ស្រដៀងគ្នានេះដែរ ប្រសិនបើ System Prompt មានព័ត៌មានដែលពិពណ៌នាអំពី roles និង permissions ផ្សេងៗគ្នា ឬទិន្នន័យរសើបដូចជា connection strings ឬ passwords ខណៈដែលការលាតត្រដាងព័ត៌មានបែបនេះអាចមានប្រយោជន៍ ហានិភ័យសុវត្ថិភាពជាមូលដ្ឋានមិនមែនដោយសារតែព័ត៌មានទាំងនេះត្រូវបានលាតត្រដាងនោះទេ ប៉ុន្តែវាគឺថា application អនុញ្ញាតឱ្យឆ្លងកាត់ការគ្រប់គ្រង session និង authorization checks រឹងមាំដោយការផ្ទេរទៅ LLM ហើយថាទិន្នន័យរសើបត្រូវបានរក្សាទុកនៅក្នុងកន្លែងដែលវាមិនគួរនៅ។

សរុបមក៖ ការលាតត្រដាង System Prompt ខ្លួនវាផ្ទាល់មិនបង្កឱ្យមានហានិភ័យពិតប្រាកដនោះទេ -- ហានិភ័យសុវត្ថិភាពស្ថិតនៅជាមួយធាតុផ្សំមូលដ្ឋាន មិនថាជាការលាតត្រដាងព័ត៌មានរសើប ការឆ្លងកាត់ System guardrails ការបំបែកសិទ្ធិមិនត្រឹមត្រូវជាដើម។ ទោះបីជាពាក្យពិតប្រាកដមិនត្រូវបានលាតត្រដាងក៏ដោយ អ្នកវាយប្រហារដែលទាក់ទងជាមួយប្រព័ន្ធស្ទើរតែប្រាកដជាអាចកំណត់ guardrails និង formatting restrictions ជាច្រើនដែលមាននៅក្នុង System Prompt language ក្នុងអំឡុងពេលប្រើប្រាស់ application ការផ្ញើ utterances ទៅកាន់ model និងការសង្កេតមើលលទ្ធផល។

### ឧទាហរណ៍ទូទៅនៃហានិភ័យ

#### 1. ការលាតត្រដាងមុខងាររសើប (Exposure of Sensitive Functionality)

System Prompt របស់ application អាចបង្ហាញព័ត៌មាន ឬមុខងាររសើបដែលត្រូវបានបម្រុងទុកឱ្យរក្សាការសម្ងាត់ ដូចជា sensitive system architecture, API keys, database credentials ឬ user tokens ។ ទាំងនេះអាចត្រូវបានទាញយក ឬប្រើប្រាស់ដោយអ្នកវាយប្រហារដើម្បីទទួលបានការចូលប្រើប្រាស់ដោយគ្មានការអនុញ្ញាតទៅក្នុង application ។ ឧទាហរណ៍ System Prompt ដែលមានប្រភេទ database ដែលប្រើសម្រាប់ tool អាចអនុញ្ញាតឱ្យអ្នកវាយប្រហារកំណត់គោលដៅសម្រាប់ការវាយប្រហារ SQL injection ។

#### 2. ការលាតត្រដាងច្បាប់ផ្ទៃក្នុង (Exposure of Internal Rules)

System Prompt របស់ application បង្ហាញព័ត៌មានស្តីពីដំណើរការសម្រេចចិត្តផ្ទៃក្នុងដែលគួររក្សាការសម្ងាត់។ ព័ត៌មាននេះអនុញ្ញាតឱ្យអ្នកវាយប្រហារទទួលបានការយល់ដឹងអំពីរបៀបដែល application ដំណើរការ ដែលអាចអនុញ្ញាតឱ្យអ្នកវាយប្រហារទាញយកភាពទន់ខ្សោយ ឬឆ្លងកាត់ការគ្រប់គ្រងនៅក្នុង application ។ ឧទាហរណ៍ - មាន banking application ដែលមាន chatbot ហើយ System Prompt របស់វាអាចបង្ហាញព័ត៌មានដូចជា៖
> "The Transaction limit is set to $5000 per day for a user. The Total Loan Amount for a user is $10,000"។
ព័ត៌មាននេះអនុញ្ញាតឱ្យអ្នកវាយប្រហារឆ្លងកាត់ security controls នៅក្នុង application ដូចជាការធ្វើប្រតិបត្តិការលើសពីកំណត់ដែលបានកំណត់ ឬការឆ្លងកាត់ចំនួនទឹកប្រាក់កម្ចីសរុប។

#### 3. ការបង្ហាញលក្ខណៈវិនិច្ឆ័យនៃការចម្រាញ់ (Revealing of Filtering Criteria)

System Prompt អាចស្នើសុំឱ្យ model ចម្រាញ់ ឬបដិសេធមាតិការសើប។ ឧទាហរណ៍ model អាចមាន System Prompt ដូចជា៖
> “If a user requests information about another user, always respond with ‘Sorry, I cannot assist with that request’ ”។
>
#### 4. ការលាតត្រដាង Permissions និង User Roles (Disclosure of Permissions and User Roles)

System Prompt អាចបង្ហាញ internal role structures ឬ permission levels របស់ application ។ ឧទាហរណ៍ System Prompt អាចបង្ហាញ៖
> “Admin user role grants full access to modify user records.”
ប្រសិនបើអ្នកវាយប្រហារដឹងអំពី role-based permissions ទាំងនេះ ពួកគេអាចស្វែងរកការវាយប្រហារ privilege escalation ។

### យុទ្ធសាស្ត្របង្ការ និងកាត់បន្ថយ

#### 1. បំបែកទិន្នន័យរសើបចេញពី System Prompts (Separate Sensitive Data from System Prompts)

ជៀសវាងការបង្កប់ព័ត៌មានរសើបណាមួយ (ឧទាហរណ៍ API keys, auth keys, database names, user roles, permission structure របស់ application) ដោយផ្ទាល់នៅក្នុង System Prompts ។ ផ្ទុយទៅវិញ សូម externalize ព័ត៌មានបែបនេះទៅកាន់ systems ដែល model មិនចូលប្រើដោយផ្ទាល់។

#### 2. ជៀសវាងការពឹងផ្អែកលើ System Prompts សម្រាប់ការគ្រប់គ្រង Behavior ដ៏តឹងរ៉ឹង (Avoid Reliance on System Prompts for Strict Behavior Control)

ដោយសារ LLMs ងាយរងគ្រោះនឹងការវាយប្រហារផ្សេងទៀតដូចជា prompt injections ដែលអាចផ្លាស់ប្តូរ System Prompt នោះ គេណែនាំឱ្យជៀសវាងការប្រើប្រាស់ System Prompts ដើម្បីគ្រប់គ្រង behavior របស់ model នៅពេលណាដែលអាចធ្វើទៅបាន។ ផ្ទុយទៅវិញ សូមពឹងផ្អែកលើ systems ក្រៅពី LLM ដើម្បីធានា behavior នេះ។ ឧទាហរណ៍ ការរកឃើញ និងការទប់ស្កាត់មាតិកាដែលបង្កគ្រោះថ្នាក់គួរតែត្រូវបានធ្វើនៅក្នុង external systems ។

#### 3. អនុវត្ត Guardrails (Implement Guardrails)

អនុវត្តប្រព័ន្ធ guardrails នៅខាងក្រៅ LLM ខ្លួនវាផ្ទាល់។ ខណៈពេលដែលការបណ្តុះបណ្តាល behavior ជាក់លាក់មួយទៅក្នុង model អាចមានប្រសិទ្ធភាព ដូចជាការបណ្តុះបណ្តាលវាមិនឱ្យបង្ហាញ System Prompt របស់វា វាមិនមែនជាការធានាថាម៉ូដែលនឹងប្រកាន់ខ្ជាប់ជានិច្ចនោះទេ។ ប្រព័ន្ធឯករាជ្យដែលអាចត្រួតពិនិត្យ output ដើម្បីកំណត់ថាតើ model អនុលោមតាមការរំពឹងទុកគឺល្អជាង System Prompt instructions ។

#### 4. ធានាថា security controls ត្រូវបានអនុវត្តដោយឯករាជ្យពី LLM (Ensure that security controls are enforced independently from the LLM)

Critical controls ដូចជា privilege separation, authorization bounds checks និងស្រដៀងគ្នា មិនត្រូវត្រូវបានផ្ទេរទៅ LLM នោះទេ មិនថាដោយ System Prompt ឬតាមវិធីផ្សេងទៀតឡើយ។ Controls ទាំងនេះត្រូវតែកើតឡើងតាមរបៀបដែលអាចកំណត់បាន (deterministic) អាចធ្វើសវនកម្មបាន (auditable) ហើយ LLMs មិន (បច្ចុប្បន្ន) អនុគ្រោះដល់រឿងនេះទេ។ ក្នុងករណីដែល agent កំពុងអនុវត្ត tasks ប្រសិនបើ tasks ទាំងនោះទាមទារកម្រិតនៃការចូលប្រើប្រាស់ខុសៗគ្នា នោះ multiple agents គួរតែត្រូវបានប្រើប្រាស់ ដោយ agent នីមួយៗត្រូវបានកំណត់រចនាសម្ព័ន្ធជាមួយនឹង least privileges ដែលត្រូវការដើម្បីអនុវត្ត tasks ដែលចង់បាន។

### ឧទាហរណ៍ scenario នៃការវាយប្រហារ

#### Scenario #1

LLM មាន System Prompt ដែលមានសំណុំ credentials ដែលប្រើសម្រាប់ tool ដែលវាត្រូវបានផ្តល់សិទ្ធិចូលប្រើ។ System Prompt ត្រូវបានលេចធ្លាយទៅកាន់អ្នកវាយប្រហារ ដែលបន្ទាប់មកអាចប្រើ credentials ទាំងនេះសម្រាប់គោលបំណងផ្សេងទៀត។

#### Scenario #2

LLM មាន System Prompt ដែលហាមឃាត់ការបង្កើត offensive content, external links និង code execution ។ អ្នកវាយប្រហារទាញយក System Prompt នេះ ហើយបន្ទាប់មកប្រើ prompt injection attack ដើម្បីឆ្លងកាត់ instructions ទាំងនេះ សម្រួលដល់ remote code execution attack ។

### តំណភ្ជាប់យោង

1. [SYSTEM PROMPT LEAK](https://x.com/elder_plinius/status/1801393358964994062): Pliny the prompter
2. [Prompt Leak](https://www.prompt.security/vulnerabilities/prompt-leak): Prompt Security
3. [chatgpt_system_prompt](https://github.com/LouisShark/chatgpt_system_prompt): LouisShark
4. [leaked-system-prompts](https://github.com/jujumilk3/leaked-system-prompts): Jujumilk3
5. [OpenAI Advanced Voice Mode System Prompt](https://x.com/Green_terminals/status/1839141326329360579): Green_Terminals

### Frameworks និង Taxonomies ដែលពាក់ព័ន្ធ

សូមមើលផ្នែកនេះសម្រាប់ព័ត៌មាន ទិដ្ឋភាពសេណារីយ៉ូ យុទ្ធសាស្ត្រទូលំទូលាយដែលទាក់ទងនឹងការដាក់ពង្រាយហេដ្ឋារចនាសម្ព័ន្ធ ការគ្រប់គ្រងបរិស្ថានដែលបានអនុវត្ត និង best practices ផ្សេងទៀត។

- [AML.T0051.000 - LLM Prompt Injection: Direct (Meta Prompt Extraction)](https://atlas.mitre.org/techniques/AML.T0051.000) **MITRE ATLAS**
