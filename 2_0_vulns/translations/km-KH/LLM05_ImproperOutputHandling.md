# LLM05:2025 ការគ្រប់គ្រងលទ្ធផលមិនត្រឹមត្រូវ (Improper Output Handling)

## ការពិពណ៌នា

ការគ្រប់គ្រងលទ្ធផលមិនត្រឹមត្រូវ (Improper Output Handling) សំដៅជាពិសេសទៅលើការត្រួតពិនិត្យ (validation) ការសម្អាត (sanitization) និងការចាត់ចែង (handling) លទ្ធផលដែលបង្កើតដោយគំរូភាសាធំ (LLM) មិនគ្រប់គ្រាន់ មុនពេលបញ្ជូនបន្តទៅកាន់សមាសធាតុ និងប្រព័ន្ធដទៃទៀត (downstream components and systems)។ ដោយសារខ្លឹមសារដែលបង្កើតដោយ LLM អាចត្រូវបានគ្រប់គ្រងតាមរយៈការបញ្ចូល prompt គឺស្រដៀងនឹងការផ្តល់ឱ្យអ្នកប្រើប្រាស់នូវការចូលប្រើប្រាស់ដោយប្រយោលទៅកាន់មុខងារបន្ថែម។
ការគ្រប់គ្រងលទ្ធផលមិនត្រឹមត្រូវ (Improper Output Handling) ខុសពីការជឿទុកចិត្តលើសកម្រិត (Overreliance) ដោយសារវាផ្តោតលើការចាត់ចែងលទ្ធផលដែលបង្កើតដោយ LLM មុនពេលបញ្ជូនបន្ត ខណៈដែលការជឿទុកចិត្តលើសកម្រិត (Overreliance) ផ្តោតលើកង្វល់ទូលំទូលាយជាង ពោលគឺការពឹងផ្អែកខ្លាំងពេកទៅលើភាពត្រឹមត្រូវ និងភាពសមរម្យនៃលទ្ធផលរបស់ LLM។
ការវាយប្រហារដោយជោគជ័យលើភាពងាយរងគ្រោះនៃការគ្រប់គ្រងលទ្ធផលមិនត្រឹមត្រូវ (Improper Output Handling) អាចបណ្តាលឱ្យមានការវាយប្រហារបែប Cross-Site Scripting (XSS) និង Cross-Site Request Forgery (CSRF) នៅក្នុងកម្មវិធីរុករក (web browsers) ក៏ដូចជា Server-Side Request Forgery (SSRF), ការតម្លើងសិទ្ធិ (privilege escalation) ឬការប្រតិបត្តិកូដពីចម្ងាយ (remote code execution) នៅលើប្រព័ន្ធ backend។
លក្ខខណ្ឌខាងក្រោមអាចបង្កើនផលប៉ះពាល់នៃភាពងាយរងគ្រោះនេះ៖

- កម្មវិធីផ្តល់ឱ្យ LLM នូវសិទ្ធិលើសពីអ្វីដែលបានបម្រុងទុកសម្រាប់អ្នកប្រើប្រាស់ ដែលអាចនាំឱ្យមានការតម្លើងសិទ្ធិ (escalation of privileges) ឬការប្រតិបត្តិកូដពីចម្ងាយ (remote code execution)។
- កម្មវិធីងាយរងគ្រោះនឹងការវាយប្រហារដោយប្រយោលតាមរយៈ prompt injection ដែលអាចអនុញ្ញាតឱ្យអ្នកវាយប្រហារទទួលបានសិទ្ធិពិសេសចូលទៅកាន់បរិស្ថានរបស់អ្នកប្រើប្រាស់គោលដៅ។
- ផ្នែកបន្ថែម (extensions) ពីភាគីទីបីមិនបានត្រួតពិនិត្យការបញ្ចូល (inputs) បានគ្រប់គ្រាន់ទេ។
- កង្វះការអ៊ិនកូដលទ្ធផល (output encoding) ត្រឹមត្រូវសម្រាប់បរិបទផ្សេងៗគ្នា (ឧទាហរណ៍ HTML, JavaScript, SQL)។
- ការត្រួតពិនិត្យ និងការកត់ត្រាលទ្ធផលរបស់ LLM មិនគ្រប់គ្រាន់។
- អវត្តមាននៃការកំណត់ដែនកំណត់ (rate limiting) ឬការរកឃើញភាពមិនប្រក្រតី (anomaly detection) សម្រាប់ការប្រើប្រាស់ LLM។

## ឧទាហរណ៍ទូទៅនៃភាពងាយរងគ្រោះ

១. លទ្ធផលរបស់ LLM ត្រូវបានបញ្ចូលដោយផ្ទាល់ទៅក្នុង system shell ឬមុខងារស្រដៀងគ្នាដូចជា `exec` ឬ `eval` ដែលបណ្តាលឱ្យមានការប្រតិបត្តិកូដពីចម្ងាយ (remote code execution)។
២. កូដ JavaScript ឬ Markdown ត្រូវបានបង្កើតដោយ LLM ហើយបញ្ជូនត្រឡប់ទៅអ្នកប្រើប្រាស់វិញ។ បន្ទាប់មក កូដនោះត្រូវបានបកស្រាយដោយកម្មវិធីរុករក (browser) ដែលបណ្តាលឱ្យមានការវាយប្រហារបែប Cross-Site Scripting (XSS)។
៣. សំណួរ SQL ដែលបង្កើតដោយ LLM ត្រូវបានប្រតិបត្តិដោយគ្មានការកំណត់ប៉ារ៉ាម៉ែត្រត្រឹមត្រូវ (proper parameterization) ដែលនាំឱ្យមានការវាយប្រហារបែប SQL injection។
៤. លទ្ធផលរបស់ LLM ត្រូវបានប្រើដើម្បីបង្កើតផ្លូវឯកសារ (file paths) ដោយគ្មានការសម្អាត (sanitization) ត្រឹមត្រូវ ដែលអាចបណ្តាលឱ្យមានភាពងាយរងគ្រោះក្នុងការឆ្លងកាត់ផ្លូវ (path traversal vulnerabilities)។
៥. ខ្លឹមសារដែលបង្កើតដោយ LLM ត្រូវបានប្រើនៅក្នុងគំរូអ៊ីមែល (email templates) ដោយគ្មានការការពារ (escaping) ត្រឹមត្រូវ ដែលអាចនាំឱ្យមានការវាយប្រហារបែបបន្លំ (phishing attacks)។

## យុទ្ធសាស្ត្របង្ការ និងកាត់បន្ថយ

១. ចាត់ទុកគំរូ (model) ដូចជាអ្នកប្រើប្រាស់ដទៃទៀត ដោយអនុវត្តแนวทาง zero-trust និងអនុវត្តការត្រួតពិនិត្យការបញ្ចូល (input validation) ត្រឹមត្រូវលើការឆ្លើយតបដែលមកពីគំរូ (model) ទៅកាន់មុខងារ backend។
២. អនុវត្តតាម OWASP ASVS (Application Security Verification Standard) guidelines ដើម្បីធានា input validation និង sanitization ប្រកបដោយប្រសិទ្ធភាព។
៣. Encode model output ត្រឡប់ទៅ users វិញដើម្បីកាត់បន្ថយ undesired code execution ដោយ JavaScript ឬ Markdown ។ OWASP ASVS ផ្តល់ detailed guidance លើ output encoding ។
៤. អនុវត្ត context-aware output encoding ដោយផ្អែកលើកន្លែងដែល LLM output នឹងត្រូវបានប្រើ (ឧទាហរណ៍ HTML encoding សម្រាប់ web content, SQL escaping សម្រាប់ database queries) ។
៥. ប្រើ parameterized queries ឬ prepared statements សម្រាប់ database operations ទាំងអស់ដែលពាក់ព័ន្ធនឹង LLM output ។
៦. ប្រើប្រាស់ strict Content Security Policies (CSP) ដើម្បីកាត់បន្ថយហានិភ័យនៃ XSS attacks ពី LLM-generated content ។
៧. អនុវត្ត robust logging និង monitoring systems ដើម្បីរកឃើញ unusual patterns នៅក្នុង LLM outputs ដែលអាចបង្ហាញពី exploitation attempts ។

### ឧទាហរណ៍សេណារីយោនៃការវាយប្រហារ

#### សេណារីយ៉ូ #១

Application មួយប្រើប្រាស់ LLM extension ដើម្បីបង្កើត responses សម្រាប់ chatbot feature ។ Extension នេះក៏ផ្តល់នូវ administrative functions មួយចំនួនដែលអាចចូលប្រើបានសម្រាប់ privileged LLM មួយផ្សេងទៀត។ General purpose LLM បញ្ជូន response របស់វាដោយផ្ទាល់ ដោយគ្មាន proper output validation ទៅ extension ដែលបណ្តាលឱ្យ extension បិទដើម្បី maintenance ។

#### សេណារីយ៉ូ #២

User ប្រើប្រាស់ website summarizer tool ដែលដំណើរការដោយ LLM ដើម្បីបង្កើត concise summary នៃអត្ថបទមួយ។ Website រួមបញ្ចូល prompt injection ដែលណែនាំ LLM ឱ្យ capture sensitive content ពី website ឬពី user's conversation ។ ពីទីនោះ LLM អាច encode sensitive data ហើយផ្ញើវាដោយគ្មាន output validation ឬ filtering ណាមួយទៅ attacker-controlled server ។

#### សេណារីយ៉ូ #៣

LLM អនុញ្ញាតឱ្យ users បង្កើត SQL queries សម្រាប់ backend database តាមរយៈ chat-like feature ។ User ស្នើសុំ query ដើម្បីលុប database tables ទាំងអស់។ ប្រសិនបើ crafted query ពី LLM មិនត្រូវបាន scrutinised នោះ database tables ទាំងអស់នឹងត្រូវបានលុប។

#### សេណារីយ៉ូ #៤

Web app មួយប្រើ LLM ដើម្បីបង្កើត content ពី user text prompts ដោយគ្មាន output sanitization ។ Attacker អាច submit crafted prompt ដែលបណ្តាលឱ្យ LLM ត្រឡប់ unsanitized JavaScript payload ដែលនាំឱ្យ XSS នៅពេល rendered នៅលើ victim's browser ។ Insufficient validation of prompts បានបើកឱ្យការវាយប្រហារនេះ។

#### សេណារីយ៉ូ #៥

LLM ត្រូវបានប្រើដើម្បីបង្កើត dynamic email templates សម្រាប់ marketing campaign ។ Attacker manipulations LLM ដើម្បីបញ្ចូល malicious JavaScript នៅក្នុង email content ។ ប្រសិនបើ application មិន sanitize LLM output បានត្រឹមត្រូវទេ នេះអាចនាំឱ្យ XSS attacks លើ recipients ដែលមើល email នៅក្នុង vulnerable email clients ។

#### សេណារីយ៉ូ #៦

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
