## LLM05:2025 ការគ្រប់គ្រង Output មិនត្រឹមត្រូវ (Improper Output Handling)

### ការពិពណ៌នា

Improper Output Handling សំដៅជាពិសេសទៅលើ insufficient validation, sanitization និង handling នៃ outputs ដែលបង្កើតឡើងដោយ large language models មុនពេលពួកគេត្រូវបានបញ្ជូនបន្តទៅ downstream components និង systems ។ ដោយសារ LLM-generated content អាចត្រូវបានគ្រប់គ្រងដោយ prompt input behavior នេះគឺស្រដៀងទៅនឹងការផ្តល់ឱ្យអ្នកប្រើប្រាស់នូវ indirect access ទៅកាន់ functionality បន្ថែម។
Improper Output Handling ខុសពី Overreliance ត្រង់ថាវាទាក់ទងនឹង LLM-generated outputs មុនពេលពួកគេត្រូវបានបញ្ជូនបន្ត ខណៈដែល Overreliance ផ្តោតលើ broader concerns ជុំវិញ overdependence លើ accuracy និង appropriateness នៃ LLM outputs ។
ការទាញយកប្រយោជន៍ដោយជោគជ័យពី Improper Output Handling vulnerability អាចបណ្តាលឱ្យមាន XSS និង CSRF នៅក្នុង web browsers ក៏ដូចជា SSRF, privilege escalation ឬ remote code execution នៅលើ backend systems ។
លក្ខខណ្ឌខាងក្រោមអាចបង្កើនផលប៉ះពាល់នៃ vulnerability នេះ៖

- Application ផ្តល់ឱ្យ LLM នូវ privileges លើសពីអ្វីដែលបានបម្រុងទុកសម្រាប់ end users ដែលអាចឱ្យ escalation of privileges ឬ remote code execution ។
- Application ងាយរងគ្រោះទៅនឹង indirect prompt injection attacks ដែលអាចអនុញ្ញាតឱ្យ attacker ទទួលបាន privileged access ទៅកាន់ target user's environment ។
- 3rd party extensions មិន validate inputs បានគ្រប់គ្រាន់ទេ។
- កង្វះ output encoding ត្រឹមត្រូវសម្រាប់ contexts ផ្សេងៗគ្នា (ឧទាហរណ៍ HTML, JavaScript, SQL)
- Insufficient monitoring និង logging នៃ LLM outputs
- អវត្តមាន rate limiting ឬ anomaly detection សម្រាប់ការប្រើប្រាស់ LLM

### ឧទាហរណ៍ទូទៅនៃភាពងាយរងគ្រោះ

1. LLM output ត្រូវបានបញ្ចូលដោយផ្ទាល់ទៅក្នុង system shell ឬ similar function ដូចជា exec ឬ eval ដែលបណ្តាលឱ្យ remote code execution ។
2. JavaScript ឬ Markdown ត្រូវបានបង្កើតឡើងដោយ LLM ហើយត្រូវបានត្រឡប់ទៅ user វិញ។ កូដបន្ទាប់មកត្រូវបាន interpreted ដោយ browser ដែលបណ្តាលឱ្យ XSS ។
3. LLM-generated SQL queries ត្រូវបានប្រតិបត្តិដោយគ្មាន proper parameterization ដែលនាំឱ្យ SQL injection ។
4. LLM output ត្រូវបានប្រើដើម្បីបង្កើត file paths ដោយគ្មាន proper sanitization ដែលអាចបណ្តាលឱ្យ path traversal vulnerabilities ។
5. LLM-generated content ត្រូវបានប្រើនៅក្នុង email templates ដោយគ្មាន proper escaping ដែលអាចនាំឱ្យ phishing attacks ។

### យុទ្ធសាស្ត្របង្ការ និងកាត់បន្ថយ

1. ចាត់ទុក model ដូច user ផ្សេងទៀត ដោយអនុវត្ត zero-trust approach និងអនុវត្ត proper input validation លើ responses ដែលមកពី model ទៅ backend functions ។
2. អនុវត្តតាម OWASP ASVS (Application Security Verification Standard) guidelines ដើម្បីធានា input validation និង sanitization ប្រកបដោយប្រសិទ្ធភាព។
3. Encode model output ត្រឡប់ទៅ users វិញដើម្បីកាត់បន្ថយ undesired code execution ដោយ JavaScript ឬ Markdown ។ OWASP ASVS ផ្តល់ detailed guidance លើ output encoding ។
4. អនុវត្ត context-aware output encoding ដោយផ្អែកលើកន្លែងដែល LLM output នឹងត្រូវបានប្រើ (ឧទាហរណ៍ HTML encoding សម្រាប់ web content, SQL escaping សម្រាប់ database queries) ។
5. ប្រើ parameterized queries ឬ prepared statements សម្រាប់ database operations ទាំងអស់ដែលពាក់ព័ន្ធនឹង LLM output ។
6. ប្រើប្រាស់ strict Content Security Policies (CSP) ដើម្បីកាត់បន្ថយហានិភ័យនៃ XSS attacks ពី LLM-generated content ។
7. អនុវត្ត robust logging និង monitoring systems ដើម្បីរកឃើញ unusual patterns នៅក្នុង LLM outputs ដែលអាចបង្ហាញពី exploitation attempts ។

### ឧទាហរណ៍ Attack Scenarios

#### Scenario #1

Application មួយប្រើប្រាស់ LLM extension ដើម្បីបង្កើត responses សម្រាប់ chatbot feature ។ Extension នេះក៏ផ្តល់នូវ administrative functions មួយចំនួនដែលអាចចូលប្រើបានសម្រាប់ privileged LLM មួយផ្សេងទៀត។ General purpose LLM បញ្ជូន response របស់វាដោយផ្ទាល់ ដោយគ្មាន proper output validation ទៅ extension ដែលបណ្តាលឱ្យ extension បិទដើម្បី maintenance ។

#### Scenario #2

User ប្រើប្រាស់ website summarizer tool ដែលដំណើរការដោយ LLM ដើម្បីបង្កើត concise summary នៃអត្ថបទមួយ។ Website រួមបញ្ចូល prompt injection ដែលណែនាំ LLM ឱ្យ capture sensitive content ពី website ឬពី user's conversation ។ ពីទីនោះ LLM អាច encode sensitive data ហើយផ្ញើវាដោយគ្មាន output validation ឬ filtering ណាមួយទៅ attacker-controlled server ។

#### Scenario #3

LLM អនុញ្ញាតឱ្យ users បង្កើត SQL queries សម្រាប់ backend database តាមរយៈ chat-like feature ។ User ស្នើសុំ query ដើម្បីលុប database tables ទាំងអស់។ ប្រសិនបើ crafted query ពី LLM មិនត្រូវបាន scrutinised នោះ database tables ទាំងអស់នឹងត្រូវបានលុប។

#### Scenario #4

Web app មួយប្រើ LLM ដើម្បីបង្កើត content ពី user text prompts ដោយគ្មាន output sanitization ។ Attacker អាច submit crafted prompt ដែលបណ្តាលឱ្យ LLM ត្រឡប់ unsanitized JavaScript payload ដែលនាំឱ្យ XSS នៅពេល rendered នៅលើ victim's browser ។ Insufficient validation of prompts បានបើកឱ្យការវាយប្រហារនេះ។

#### Scenario #5

LLM ត្រូវបានប្រើដើម្បីបង្កើត dynamic email templates សម្រាប់ marketing campaign ។ Attacker manipulations LLM ដើម្បីបញ្ចូល malicious JavaScript នៅក្នុង email content ។ ប្រសិនបើ application មិន sanitize LLM output បានត្រឹមត្រូវទេ នេះអាចនាំឱ្យ XSS attacks លើ recipients ដែលមើល email នៅក្នុង vulnerable email clients ។

#### Scenario #6

LLM ត្រូវបានប្រើដើម្បីបង្កើត code ពី natural language inputs នៅក្នុង software company ដែលមានគោលបំណង streamlining development tasks ។ ខណៈពេលដែលមានប្រសិទ្ធភាព វិធីសាស្រ្តនេះប្រឈមនឹងការលាតត្រដាង sensitive information ការបង្កើត insecure data handling methods ឬការបង្ក vulnerabilities ដូចជា SQL injection ។ AI ក៏អាច hallucinate non-existent software packages ដែលអាចនាំឱ្យ developers download malware-infected resources ។ Thorough code review និង verification នៃ suggested packages គឺមានសារៈសំខាន់ដើម្បីការពារ security breaches, unauthorized access និង system compromises ។

### តំណភ្ជាប់យោង

1. [Proof Pudding (CVE-2019-20634)](https://avidml.org/database/avid-2023-v009/) **AVID** (`moohax` & `monoxgas`)
2. [Arbitrary Code Execution](https://security.snyk.io/vuln/SNYK-PYTHON-LANGCHAIN-5411357): **Snyk Security Blog**
3. [ChatGPT Plugin Exploit Explained: From Prompt Injection to Accessing Private Data](https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./): **Embrace The Red**
4. [New prompt injection attack on ChatGPT web version. Markdown images can steal your chat data.](https://systemweakness.com/new-prompt-injection-attack-on-chatgpt-web-version-ef717492c5c2?gi=8daec85e2116): **System Weakness**
5. [Don’t blindly trust LLM responses. Threats to chatbots](https://embracethered.com/blog/posts/2023/ai-injections-threats-context-matters/): **Embrace The Red**
6. [Threat Modeling LLM Applications](https://aivillage.org/large%20language%20models/threat-modeling-llm/): **AI Village**
7. [OWASP ASVS - 5 Validation, Sanitization and Encoding](https://owasp-aasvs4.readthedocs.io/en/latest/V5.html#validation-sanitization-and-encoding): **OWASP AASVS**
8. [AI hallucinates software packages and devs download them – even if potentially poisoned with malware](https://www.theregister.com/2024/03/28/ai_bots_hallucinate_software_packages/) **Theregiste**
