# LLM05:2025 ការគ្រប់គ្រងលទ្ធផលមិនត្រឹមត្រូវ (Improper Output Handling)

## ការពិពណ៌នា

ការគ្រប់គ្រងលទ្ធផលមិនត្រឹមត្រូវ (Improper Output Handling) សំដៅជាពិសេសទៅលើការខ្វះចន្លោះក្នុងការត្រួតពិនិត្យភាពត្រឹមត្រូវ (validation), ការសម្អាតទិន្នន័យ (sanitization), និងការគ្រប់គ្រង (handling) លទ្ធផលដែលបង្កើតដោយ LLM មុនពេលបញ្ជូនបន្តទៅកាន់ផ្នែកផ្សេងៗ និងប្រព័ន្ធដទៃទៀត (downstream components and systems) ។ ដោយសារខ្លឹមសារដែលបង្កើតដោយ LLM អាចត្រូវបានគ្រប់គ្រងតាមរយៈការបញ្ចូល prompt គឺស្រដៀងនឹងការផ្តល់ឱ្យអ្នកប្រើប្រាស់នូវការចូលប្រើប្រាស់ដោយប្រយោលទៅកាន់មុខងារបន្ថែម។<br>
ការគ្រប់គ្រងលទ្ធផលមិនត្រឹមត្រូវ (Improper Output Handling) ខុសពីការជឿទុកចិត្តខ្លាំងពេក (Overreliance) ដោយសារវាផ្តោតលើការការគ្រប់គ្រងលទ្ធផលដែលបង្កើតដោយ LLM មុនពេលបញ្ជូនទៅមុខបន្តទៀត ខណៈពេលដែលការជឿទុកចិត្តខ្លាំងពេក (Overreliance) ផ្តោតលើឥរិយាបថអ្នកប្រើប្រាស់ដែលមានការរំពឹងទុក ឬការពឹងផ្អែកខ្លាំងជ្រុលទៅលើភាពត្រឹមត្រូវ និងភាពសមស្របនៃលទ្ធផលរបស់ LLM។<br>
ការវាយប្រហារបានជោគជ័យលើភាពងាយរងគ្រោះនៃការគ្រប់គ្រងលទ្ធផលមិនត្រឹមត្រូវនេះ (Improper Output Handling) អាចបណ្តាលឱ្យមានការវាយប្រហារបែប Cross-Site Scripting (XSS) និង Cross-Site Request Forgery (CSRF) នៅក្នុងកម្មវិធីរុករក (web browsers) ក៏ដូចជា Server-Side Request Forgery (SSRF), ការដំឡើងសិទ្ធិ (privilege escalation) ឬការបញ្ជាកូដពីចម្ងាយ (remote code execution) នៅលើប្រព័ន្ធ backend។<br>
លក្ខខណ្ឌខាងក្រោមអាចបង្កើនផលប៉ះពាល់នៃភាពងាយរងគ្រោះនេះ៖

- កម្មវិធីផ្តល់ឱ្យ LLM នូវសិទ្ធិលើសពីអ្វីដែលបានបម្រុងទុកសម្រាប់អ្នកប្រើប្រាស់ ដែលអាចនាំឱ្យមានការដំឡើងសិទ្ធិ (escalation of privileges) ឬការបញ្ជកូដពីចម្ងាយ (remote code execution)។
- កម្មវិធីងាយរងគ្រោះដោយសារការវាយប្រហារដោយប្រយោលតាមរយៈ prompt injection ដែលអាចអនុញ្ញាតឱ្យអ្នកវាយប្រហារ (Attacker) ទទួលបានសិទ្ធិពិសេសចូលទៅគ្រប់គ្រងប្រព័ន្ធបច្ចេកវិទ្យា (ឧបករណ៍ ឬទិន្នន័យ) ទាំងស្រុងរបស់អ្នកប្រើប្រាស់ដែលស្ថិតក្នុងគោលដៅរបស់ពួកគេ។
- ផ្នែកបន្ថែម (extensions) ពីភាគីទីបីមិនបានត្រួតពិនិត្យការបញ្ចូល (inputs) បានគ្រប់គ្រាន់ទេ។
- កង្វះការអ៊ិនកូដលទ្ធផល (output encoding) ត្រឹមត្រូវសម្រាប់បរិបទផ្សេងៗគ្នា (ឧទាហរណ៍ HTML, JavaScript, SQL)។
- ការត្រួតពិនិត្យ និងការកត់ត្រាលទ្ធផលរបស់ LLM មិនគ្រប់គ្រាន់។
- អវត្តមាននៃការកំណត់ដែនកំណត់ (rate limiting) ឬការរកឃើញភាពមិនប្រក្រតី (anomaly detection) សម្រាប់ការប្រើប្រាស់ LLM។

## ឧទាហរណ៍ទូទៅនៃភាពងាយរងគ្រោះ

១. លទ្ធផលរបស់ LLM ត្រូវបានបញ្ចូលដោយផ្ទាល់ទៅក្នុង system shell ឬមុខងារស្រដៀងគ្នាដូចជា `exec` ឬ `eval` ដែលបណ្តាលឱ្យមានការបញ្ជាកូដពីចម្ងាយ (remote code execution)។<br>
២. កូដ JavaScript ឬ Markdown ត្រូវបានបង្កើតដោយ LLM ហើយបញ្ជូនត្រឡប់ទៅអ្នកប្រើប្រាស់វិញ។ បន្ទាប់មក កូដនោះត្រូវបានបកស្រាយដោយកម្មវិធីរុករក (browser) ដែលបណ្តាលឱ្យមានការវាយប្រហារបែប Cross-Site Scripting (XSS)។<br>
៣. សំណួរ SQL ដែលបង្កើតដោយ LLM ត្រូវបានដំណើរការដោយគ្មានការកំណត់ប៉ារ៉ាម៉ែត្រត្រឹមត្រូវ (proper parameterization) ដែលនាំឱ្យមានការវាយប្រហារបែប SQL injection។<br>
៤. លទ្ធផលរបស់ LLM ត្រូវបានប្រើដើម្បីបង្កើតផ្លូវឯកសារ (file paths) ដោយគ្មានការសម្អាត (sanitization) ត្រឹមត្រូវ ដែលអាចបណ្តាលឱ្យមានភាពងាយរងគ្រោះក្នុងការឆ្លងកាត់ផ្លូវ (path traversal vulnerabilities)។<br>
៥. ខ្លឹមសារដែលបង្កើតដោយ LLM ត្រូវបានប្រើនៅក្នុងគំរូអ៊ីមែល (email templates) ដោយគ្មានការការពារ (escaping) ត្រឹមត្រូវ ដែលអាចនាំឱ្យមានការវាយប្រហារបែបបន្លំ (phishing attacks)។

## យុទ្ធសាស្ត្របង្ការ និងកាត់បន្ថយ

១. ចាត់ទុកគំរូ (model) ដូចជាអ្នកប្រើប្រាស់ដទៃទៀត ដោយអនុវត្តគោលការណ៍ zero-trust និងអនុវត្តការត្រួតពិនិត្យការបញ្ចូល (input validation) ត្រឹមត្រូវលើការឆ្លើយតបដែលមកពីគំរូ (model) ទៅកាន់មុខងារ backend។ <br>
២. អនុវត្តតាម OWASP ASVS (Application Security Verification Standard) guidelines ដើម្បីធានា input validation និង sanitization ប្រកបដោយប្រសិទ្ធភាព។<br>
៣. Encode model output ត្រឡប់ទៅអ្នកប្រើប្រាស់វិញដើម្បីកាត់បន្ថយដំណើរការកូដដែលមិនចង់បានដោយ JavaScript ឬ Markdown ។ OWASP ASVS ផ្តល់ការណែនាំលម្អិតទៅលើ output encoding ។<br>
៤. អនុវត្ត context-aware output encoding ដោយផ្អែកលើលទ្ធផលពី LLM នឹងត្រូវបានប្រើ (ឧទាហរណ៍៖ HTML encoding សម្រាប់ web content, SQL escaping សម្រាប់ database queries) ។<br>
៥. ប្រើ parameterized queries ឬ prepared statements សម្រាប់ប្រតិបត្តិការមូលដ្ឋានរបស់ទិន្នន័យ (database operations) ទាំងអស់ដែលពាក់ព័ន្ធនឹងលទ្ធផលរបស់ LLM ។<br>
៦. អនុវត្តគោលការណ៍សុវត្ថិភាពខ្លឹមសារឱ្យបានតឹងរ៉ឹង (strict Content Security Policies (CSP))ដើម្បីកាត់បន្ថយហានិភ័យនៃការវាយប្រហារបែប XSS ដែលកើតចេញពីមាតិកាបង្កើតដោយ LLM ។<br>
៧. អនុវត្តបង្កើតប្រព័ន្ធកត់ត្រា (robust logging) និង ប្រព័ន្ធត្រួតពិនិត្យ (monitoring systems) ឱ្យបានហ្មត់ចត់ ដើម្បីស្វែងរកសញ្ញាមិនប្រក្រតីនៅក្នុងលទ្ធផលរបស់ LLM ដែលអាចបង្ហាញពីដែលអាចបង្ហាញពីការប៉ុនប៉ងវាយប្រហារ។

### ឧទាហរណ៍សេណារីយ៉ូនៃការវាយប្រហារ

#### សេណារីយ៉ូ #១

កម្មវិធីមួយប្រើប្រាស់មុខងារបន្ថែម (Extension) របស់ LLM ដើម្បីបង្កើតបង្កើតចម្លើយសម្រាប់មុខងារ chatbot ។ មុខងារបន្ថែមនេះក៏ផ្តល់នូវមុខងាររដ្ឋបាល (administrative functions) មួយចំនួនដែលអាចឱ្យ LLM មួយផ្សេងទៀតដែលមានសិទ្ធិខ្ពស់អាចចូលប្រើប្រាស់បាន។ គោលបំណងទូទៅរបស់ LLM គឺបញ្ជូនការឆ្លើយតបរបស់វាដោយផ្ទាល់ ដោយគ្មានការផ្ទៀងផ្ទាត់ទិន្នផលត្រឹមត្រូវកាន់ទៅមុខងារបន្ថែម (Extension) នេះដែលបណ្តាលឱ្យមុខងារបន្ថែម (Extension) បិទសម្រាប់ការថែទាំ ។

#### សេណារីយ៉ូ #២

អ្នកប្រើប្រាស់ម្នាក់បានប្រើប្រាស់ឧបករណ៍សង្ខេបគេហទំព័រ (website summarizer tool) ដែលដំណើរការដោយ LLM ដើម្បីបង្កើតសេចក្តីសង្ខេបខ្លីៗនៃអត្ថបទមួយ។ គេហទំព័រនោះមានរួមបញ្ចូល prompt injection ដែលបង្គាប់ឱ្យ LLM ចាប់យកខ្លឹមសាររសើប (sensitive content) ពីគេហទំព័រ ឬពីការសន្ទនារបស់អ្នកប្រើប្រាស់។ បន្ទាប់ពីទីនោះ LLM អាចបំប្លែងទិន្នន័យរសើបទាំងនោះជាកូដ (encode sensitive data) ហើយផ្ញើវាដោយគ្មានដោយគ្មានការត្រួតពិនិត្យភាពត្រឹមត្រូវនៃលទ្ធផល (output validation) ឬការត្រងទិន្នន័យ (filtering) ណាមួយទៅ attacker-controlled server ។

#### សេណារីយ៉ូ #៣

LLM មួយអនុញ្ញាតឱ្យអ្នកប្រើប្រាស់បង្កើត SQL queries សម្រាប់ backend database តាមរយៈមុខងារជជែកកម្សាន្ត (chat-like feature) ។ អ្នកប្រើប្រាស់ម្នាក់បានស្នើសុំ query ដើម្បីលុបតារាងទិន្នន័យទាំងអស់។ ប្រសិនបើ crafted query ពី LLM មិនត្រូវបានពិនិត្យពិច័យឱ្យបានហ្មត់ចត់ទេនោះ តារាងទិន្នន័យទាំងអស់នឹងត្រូវបានលុប។

#### សេណារីយ៉ូ #៤

កម្មវិធីវិប (Web app) មួយប្រើ LLM ដើម្បីបង្កើតមាតិកា (content) ពីចេញពីសារបញ្ជារបស់អ្នកប្រើប្រាស់ (user text prompts) ដោយគ្មានការសម្អាតលទ្ធផល ឬ ចម្លើយ។ អ្នកវាយប្រហារអាចផ្ញើសារបញ្ជាដែលបានរៀបចំទុកជាមុន ដែលបណ្តាលឱ្យ LLM បញ្ចេញមកវិញនូវ unsanitized JavaScript payload ដែលនាំឱ្យ XSS នៅពេលបង្ហាញ (rendered) នៅលើកម្មវិធីរុករក (Browser) របស់អ្នករងគ្រោះ។ ការផ្ទៀងផ្ទាត់ prompts មិនគ្រប់គ្រាន់បានបើកឱ្យការវាយប្រហារនេះ។

#### សេណារីយ៉ូ #៥

LLM ត្រូវបានប្រើដើម្បីបង្កើត dynamic email templates សម្រាប់យុទ្ធនាការទីផ្សារ។ អ្នកវាយប្រហារបានល្បួងបញ្ជា LLM ដើម្បីបញ្ចូលកូដ JavaScript ដែលមានបំណងអាក្រក់ទៅនៅក្នុងខ្លឹមសារអ៊ីមែល។ ប្រសិនបើកម្មវិធីមិនមានការសម្អាតលទ្ធផ្ឭលរបស់ LLM បានត្រឹមត្រូវទេ នេះអាចនាំឱ្យមានការវាយប្រហារបែប XSS ទៅលើអ្នកទទួលបើកមើលអ៊ីមែលនៅក្នុងនៅក្នុងកម្មវិធីអ៊ីមែល (Email clients) ដែលមានចន្លោះប្រហោង។

#### សេណារីយ៉ូ #៦

LLM ត្រូវបានប្រើដើម្បីបង្កើត code ពី natural language inputs នៅក្នុងក្រុមហ៊ុនកម្មវិធីកុំព្យូទ័រមួយដែលមានគោលបំណងសម្រួលដល់កិច្ចការអភិវឌ្ឍន៍ឱ្យកាន់តែរហ័ស។ ខណៈពេលដែលមានប្រសិទ្ធភាព វិធីសាស្រ្តនេះប្រឈមនឹងការលាតត្រដាងព័ត៌មានរសើប (sensitive information) ការបង្កើតវិធីសាស្ត្រចាត់ចែងទិន្នន័យដែលខ្វះសុវត្ថិភាព ឬការបង្កឱ្យមានចន្លោះប្រហោងសុវត្ថិភាពដូចជា SQL injection ។ AI ក៏អាចបង្កើតនូវកញ្ចប់កម្មវិធីដែលមិនមានពិតប្រាកដ (Hallucinate non-existent software packages) ដែលអាចនាំឱ្យអ្នកអភិវឌ្ឍន៍ (Developers) ទាញយកធនធានដែលមានបង្កប់មេរោគ (Malware-infected resources) ។ ការត្រួតពិនិត្យកូដឱ្យបានហ្មត់ចត់ និង ការផ្ទៀងផ្ទាត់កញ្ចប់កម្មវិធីដែលបានណែនាំ គឺជាកត្តាចាំបាច់ដើម្បីទប់ស្កាត់ការបំពានសុវត្ថិភាព, ការចូលប្រើប្រាស់ដោយគ្មានការអនុញ្ញាត, និងការធ្វើឱ្យប្រព័ន្ធរងការខូចខាត។។

### តំណភ្ជាប់យោង

1. [Proof Pudding (CVE-2019-20634)](https://avidml.org/database/avid-2023-v009/) **AVID** (`moohax` & `monoxgas`)
2. [Arbitrary Code Execution](https://security.snyk.io/vuln/SNYK-PYTHON-LANGCHAIN-5411357): **Snyk Security Blog**
3. [ChatGPT Plugin Exploit Explained: From Prompt Injection to Accessing Private Data](https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./): **Embrace The Red**
4. [New prompt injection attack on ChatGPT web version. Markdown images can steal your chat data.](https://systemweakness.com/new-prompt-injection-attack-on-chatgpt-web-version-ef717492c5c2?gi=8daec85e2116): **System Weakness**
5. [Don’t blindly trust LLM responses. Threats to chatbots](https://embracethered.com/blog/posts/2023/ai-injections-threats-context-matters/): **Embrace The Red**
6. [Threat Modeling LLM Applications](https://aivillage.org/large%20language%20models/threat-modeling-llm/): **AI Village**
7. [OWASP ASVS - 5 Validation, Sanitization and Encoding](https://owasp-aasvs4.readthedocs.io/en/latest/V5.html#validation-sanitization-and-encoding): **OWASP AASVS**
8. [AI hallucinates software packages and devs download them – even if potentially poisoned with malware](https://www.theregister.com/2024/03/28/ai_bots_hallucinate_software_packages/) **Theregiste**
