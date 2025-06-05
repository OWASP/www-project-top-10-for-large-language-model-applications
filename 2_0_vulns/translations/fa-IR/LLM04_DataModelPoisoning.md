## LLM04: مسموم‌سازی داده‌ و مدل

### توضیحات

مسموم‌سازی داده زمانی اتفاق می‌افتد که داده‌های از پیش‌آموزش، داده‌های تنظیم دقیق یا داده‌های بازنمود بردار (embedding data) با هدف ایجاد آسیب‌پذیری‌ها، درب‌های پشتی (backdoor) یا سوگیری‌ها، دست‌کاری می‌شوند. این دست‌کاری می‌تواند امنیت، عملکرد یا رفتار اخلاقی مدل را به خطر بیندازد و منجر به خروجی‌های زیان‌آور یا اختلال در قابلیت‌ها شود. مخاطرات رایج شامل تضعیف عملکرد مدل، محتوای مغرضانه یا سمی و سواستفاده از سیستم‌های پایین‌دستی (downstream) می‌شود.

مسموم‌سازی داده می‌تواند مراحل مختلف چرخه حیات مدل‌های زبانی بزرگ را از جمله پیش‌آموزش (یادگیری از داده‌های عمومی)، تنظیم دقیق (تطبیق مدل‌ها به وظایف خاص) و بازنمایی (embedding) (تبدیل متن به بردارهای عددی) را هدف قرار دهد. درک این مراحل به شناسایی منشأ آسیب‌پذیری‌ها کمک می‌کند. مسموم‌سازی داده نوعی حمله یکپارچگی محسوب می‌شود زیرا دست‌کاری در داده‌های آموزش بر توانایی مدل برای انجام پیش‌بینی‌های دقیق تأثیر می‌گذارد. مخاطرات این موضوع به‌ویژه مخاطرات همراه با منابع داده خارجی که ممکن است حاوی محتوای تأیید‌نشده یا مخرب باشند، زیاد است.

علاوه بر این، مدل‌هایی که از طریق مخازن اشتراکی یا بسترهای منبع-باز توزیع می‌شوند، می‌توانند خطراتی فراتر از مسموم‌سازی داده به همراه داشته باشند، مانند بدافزارهایی که از طریق روش‌هایی مانند Malicious Pickling جاسازی شده‌اند، که می‌توانند هنگام بارگذاری مدل، کد مخربی را اجرا کنند. همچنین در نظر داشته‌ باشید که مسموم‌سازی ممکن است امکان پیاده‌سازی درب پشتی (backdoor) را فراهم کند. چنین درب‌های پشتی ممکن است رفتار مدل را تا زمانی که یک محرک خاص باعث تغییر آن شود، دست‌نخورده باقی بگذارند. این امر ممکن است آزمایش و شناسایی چنین تغییراتی را دشوار کند و در واقع فرصتی برای تبدیل شدن یک مدل به یک عامل خفته ایجاد کند.

### نمونه‌های رایج از مخاطرات امنیتی

1. عوامل مخرب، داده‌های زیان‌بار را در حین آموزش وارد می‌کنند که منجر به خروجی‌های مغرضانه می‌شود. روش‌هایی مانند «مسموم‌سازی داده انشقاقی (Split-View Data Poisoning)» یا «مسموم‌سازی پیش‌دستانه (Frontrunning Poisoning)» از پویایی آموزش مدل برای دستیابی به این هدف سوءاستفاده می‌کنند.
  (پیوند منبع:  [Split-View Data Poisoning](https://github.com/GangGreenTemperTatum/speaking/blob/main/dc604/hacker-summer-camp-23/Ads%20_%20Poisoning%20Web%20Training%20Datasets%20_%20Flow%20Diagram%20-%20Exploit%201%20Split-View%20Data%20Poisoning.jpeg))
  (پیوند منبع: [Frontrunning Poisoning](https://github.com/GangGreenTemperTatum/speaking/blob/main/dc604/hacker-summer-camp-23/Ads%20_%20Poisoning%20Web%20Training%20Datasets%20_%20Flow%20Diagram%20-%20Exploit%202%20Frontrunning%20Data%20Poisoning.jpeg))
2. مهاجمان می‌توانند محتوای مضر را مستقیماً به فرآیند آموزش تزریق کنند و کیفیت خروجی مدل را به خطر بیندازند.
3. کاربران به صورت ناآگاهانه اطلاعات حساس یا انحصاری را در حین تعاملات وارد می‌‌کنند که ممکن است در خروجی‌های بعدی افشا شود.
4. داده‌های آموزشی تایید نشده خطر خروجی‌های مغرضانه یا اشتباه را افزایش می‌دهند.
5. عدم وجود محدودیت‌ دسترسی به منابع ممکن است اجازه ورود داده‌های ناایمن را بدهد، که منجر به خروجی‌های مغرضانه می‌شود.

### راهبردهای پیشگیری و کاهش مخاطره

1. با استفاده از ابزارهایی مانند OWASP CycloneDX یا ML-BOM منشأ و تحولات داده‌ها را ردیابی کنید. در تمام مراحل توسعه مدل، مشروعیت داده‌ها را راستی‌آزمایی کنید.
2. عرضه‌کننده‌های داده را به دقت بررسی کنید و خروجی‌های مدل را با منابع معتبر اعتبارسنجی کنید تا نشانه‌های مسمومیت را تشخیص دهید.
3. برای محدودسازی قرار‌ گرفتن مدل در معرض منابع داده تایید‌ نشده، جعبه شنی (sandboxing) سخت‌گیرانه‌ای را پیاده‌سازی کنید. از روش‌های تشخیص ناهنجاری برای پالایش داده‌های خصمانه استفاده کنید.
4. مدل‌ها را در موارد کاربرد گوناگون با استفاده از داده‌های خاص برای تنظیم دقیق آموزش دهید. این کار به تولید نتایج دقیق‌تر بر اساس اهداف تعریف‌شده کمک می‌کند.
5. از وجود کنترل‌های زیرساختی کافی برای جلوگیری از دسترسی مدل به منابع داده ناخواسته اطمینان حاصل کنید.
6. برای ردیابی تغییرات در مجموعه‌های داده و تشخیص دستکاری، از کنترل نسخه داده (DVC) استفاده کنید. نسخه‌بندی برای حفظ صحت مدل حیاتی است.
7. اطلاعات ارائه‌شده توسط کاربران را در یک پایگاه داده برداری ذخیره کنید تا امکان تنظیمات مدل بدون آموزش مجدد کامل آن فراهم شود.
8. با استفاده از کارزارهای تیم قرمز (red team campaigns) و روش‎‌های خصمانه مانند یادگیری هم‌افزا، استحکام مدل را آزمایش کنید تا تأثیر اختلالات داده را به حداقل برسانید.
9. برای شناسایی نشانه‌های مسموم‌سازی، بر اُفت آموزش نظارت کنید و رفتار مدل را تجزیه و تحلیل کنید. از آستانه‌ها (thresholds) برای شناسایی خروجی‌های غیرعادی استفاده کنید.
10. در طول فرآیند استنتاج، برای کاهش مخاطرات توهمات (hallucinations)، روش‌های Retrieval-Augmented Generation (RAG) و مستدل‌سازی (grounding) را یکپارچه کنید.

### نمونه‌هایی از فرانامه‌های حمله

#### فرانامه #۱

  مهاجم با دست‌کاری داده‌های آموزش یا استفاده از روش‌های تزریق پرامپت، خروجی‌های مدل را مغرضانه کرده و اطلاعات نادرست را منتشر می‌کند.

#### فرانامه #۲

  داده‌های سمی بدون پالایش مناسب می‌توانند منجر به خروجی‌های زیان‌بار یا مغرضانه شوند و اطلاعات خطرناکی را منتشر کنند.

#### فرانامه #۳

  یک عامل مخرب یا رقیب مدارک جعلی برای آموزش ایجاد می‌کند که منجر به تولید خروجی‌هایی از مدل می‌شود که این نادرستی‌ها را منعکس می‌کند.

#### فرانامه #۴

  پالایش ناکافی به مهاجم این امکان را می‌دهد که داده‌های گمراه‌کننده را از طریق تزریق دستور وارد کند و منجر به تولید خروجی‌های آسیب‌دیده شود.

#### فرانامه #۵

  مهاجم از روش‌های مسموم‌سازی برای وارد کردن یک فعال‌ساز درب پشتی (backdoor trigger) به مدل استفاده می‌کند. این کار می‌تواند شما را در معرض دور خوردن احراز هویت، خروج داده یا اجرای مخفیانه دستورات قرار دهد.

### پیوند‌های مرجع

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

### چارچوب‌ها و طبقه‌بندی‌های مرتبط

برای کسب اطلاعات جامع، فرانامه‌ها، راهبردهای مربوط به استقرار زیرساخت، کنترل‌های محیطی کاربردی و سایر به‌روش‌ها، به این بخش مراجعه کنید.

- [AML.T0018 | Backdoor ML Model](https://atlas.mitre.org/techniques/AML.T0018) **MITRE ATLAS**
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework): Strategies for ensuring AI integrity. **NIST**
