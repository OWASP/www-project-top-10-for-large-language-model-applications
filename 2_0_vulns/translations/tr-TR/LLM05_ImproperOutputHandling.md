## LLM05:2025 Uygunsuz Çıktı İşleme

### Açıklama

Uygunsuz Çıktı İşleme, büyük dil modelleri tarafından üretilen çıktıların diğer bileşenlere ve sistemlere aktarılmadan önce yetersiz doğrulama, temizleme ve işlenmesini ifade eder. LLM tarafından üretilen içerik istem girdisi ile kontrol edilebildiğinden, bu davranış kullanıcılara ek işlevselliğe dolaylı erişim sağlamaya benzer.
Uygunsuz Çıktı İşleme, LLM tarafından üretilen çıktılarla aşağı akışa geçmeden önce ilgilendiği için Aşırı Güvenme'den farklıdır; Aşırı Güvenme ise LLM çıktılarının doğruluğuna ve uygunluğuna aşırı bağımlılık konusundaki daha geniş endişelere odaklanır.
Uygunsuz Çıktı İşleme zafiyetinin başarılı sömürülmesi, web tarayıcılarında XSS ve CSRF'nin yanı sıra arka uç sistemlerde SSRF, ayrıcalık yükseltme veya uzaktan kod çalıştırma ile sonuçlanabilir.
Aşağıdaki koşullar bu zafiyetin etkisini artırabilir:

- Uygulama, LLM'ye son kullanıcılar için amaçlananın ötesinde ayrıcalıklar vererek ayrıcalık yükseltme veya uzaktan kod çalıştırmayı mümkün kılar.
- Uygulama, saldırganın hedef kullanıcının ortamına ayrıcalıklı erişim elde etmesine olanak sağlayabilecek dolaylı istem enjeksiyonu saldırılarına karşı savunmasızdır.
- Üçüncü taraf uzantılar girdileri yeterince doğrulamaz.
- Farklı bağlamlar için uygun çıktı kodlamasının eksikliği (örn. HTML, JavaScript, SQL)
- LLM çıktılarının yetersiz izleme ve günlük kaydı
- LLM kullanımı için hız sınırlama veya anomali tespitinin olmaması

### Zafiyetin Yaygın Örnekleri

1. LLM çıktısı doğrudan sistem kabuğuna veya exec ya da eval gibi benzer işlevlere girilir, bu da uzaktan kod çalıştırma ile sonuçlanır.
2. LLM tarafından JavaScript veya Markdown üretilir ve kullanıcıya döndürülür. Kod daha sonra tarayıcı tarafından yorumlanır, bu da XSS ile sonuçlanır.
3. LLM tarafından üretilen SQL sorguları uygun parametreleştirme olmadan çalıştırılır, SQL enjeksiyonuna yol açar.
4. LLM çıktısı uygun temizleme olmadan dosya yolları oluşturmak için kullanılır, potansiyel olarak yol geçiş zafiyetleri ile sonuçlanır.
5. LLM tarafından üretilen içerik uygun kaçış olmadan e-posta şablonlarında kullanılır, potansiyel olarak oltalama saldırılarına yol açar.

### Önleme ve Hafifletme Stratejileri

1. Modeli diğer kullanıcılar gibi ele alın, sıfır güven yaklaşımı benimseyin ve modelden arka uç işlevlerine gelen yanıtlara uygun girdi doğrulaması uygulayın.
2. Etkili girdi doğrulama ve temizleme sağlamak için OWASP ASVS (Uygulama Güvenliği Doğrulama Standardı) yönergelerini takip edin.
3. JavaScript veya Markdown tarafından istenmeyen kod çalıştırmayı hafifletmek için model çıktısını kullanıcılara geri kodlayın. OWASP ASVS çıktı kodlama konusunda detaylı rehberlik sağlar.
4. LLM çıktısının nerede kullanılacağına bağlı olarak bağlam farkında çıktı kodlama uygulayın (örn. web içeriği için HTML kodlama, veritabanı sorguları için SQL kaçış).
5. LLM çıktısını içeren tüm veritabanı işlemleri için parametreli sorguları veya hazır ifadeleri kullanın.
6. LLM tarafından üretilen içerikten XSS saldırıları riskini hafifletmek için sıkı İçerik Güvenlik Politikaları (CSP) uygulayın.
7. Sömürü girişimlerini gösterebilecek LLM çıktılarındaki olağandışı kalıpları tespit etmek için güçlü günlük kaydı ve izleme sistemleri uygulayın.

### Örnek Saldırı Senaryoları

#### Senaryo #1

  Uygulama, chatbot özelliği için yanıtlar üretmek amacıyla LLM uzantısı kullanır. Uzantı ayrıca başka ayrıcalıklı LLM tarafından erişilebilen bir dizi yönetim işlevi sunar. Genel amaçlı LLM, uygun çıktı doğrulaması olmadan yanıtını doğrudan uzantıya iletir ve uzantının bakım için kapanmasına neden olur.

#### Senaryo #2

  Kullanıcı, bir makalenin kısa özetini üretmek için LLM destekli web sitesi özetleyici aracını kullanır. Web sitesi, LLM'ye web sitesinden veya kullanıcının konuşmasından hassas içeriği yakalaması talimatını veren istem enjeksiyonu içerir. Bundan sonra LLM hassas verileri kodlayabilir ve herhangi bir çıktı doğrulama veya filtreleme olmadan saldırgan kontrollü sunucuya gönderebilir.

#### Senaryo #3

  LLM, kullanıcıların sohbet benzeri özellik aracılığıyla arka uç veritabanı için SQL sorguları oluşturmasına olanak tanır. Kullanıcı tüm veritabanı tablolarını silmek için sorgu talep eder. LLM'den gelen hazırlanmış sorgu incelenmezse, tüm veritabanı tabloları silinir.

#### Senaryo #4

  Web uygulaması, çıktı temizleme olmadan kullanıcı metin istemlerinden içerik üretmek için LLM kullanır. Saldırgan, LLM'nin temizlenmemiş JavaScript yükü döndürmesine neden olan hazırlanmış istem gönderebilir, bu da kurbanın tarayıcısında görüntülendiğinde XSS'ye yol açar. İstemlerin yetersiz doğrulaması bu saldırıyı mümkün kıldı.

#### Senaryo #5

  LLM, pazarlama kampanyası için dinamik e-posta şablonları üretmek amacıyla kullanılır. Saldırgan, LLM'yi e-posta içeriğine kötü niyetli JavaScript dahil etmek için manipüle eder. Uygulama LLM çıktısını düzgün temizlemezse, bu e-postayı savunmasız e-posta istemcilerinde görüntüleyen alıcılarda XSS saldırılarına yol açabilir.

#### Senaryo #6

  LLM, yazılım şirketinde geliştirme görevlerini kolaylaştırmak amacıyla doğal dil girdilerinden kod üretmek için kullanılır. Verimli olsa da, bu yaklaşım hassas bilgileri ifşa etme, güvensiz veri işleme yöntemleri oluşturma veya SQL enjeksiyonu gibi zafiyetleri tanıtma riski taşır. AI ayrıca var olmayan yazılım paketlerini halüsinasyon yapabilir, potansiyel olarak geliştiricilerin kötü amaçlı yazılım bulaşmış kaynakları indirmesine yol açabilir. Güvenlik ihlallerini, yetkisiz erişimi ve sistem uzlaşmalarını önlemek için kapsamlı kod incelemesi ve önerilen paketlerin doğrulanması kritiktir.

### Referanslar

1. [Proof Pudding (CVE-2019-20634)](https://avidml.org/database/avid-2023-v009/) **AVID** (`moohax` & `monoxgas`)
2. [Arbitrary Code Execution](https://security.snyk.io/vuln/SNYK-PYTHON-LANGCHAIN-5411357): **Snyk Security Blog**
3. [ChatGPT Plugin Exploit Explained: From Prompt Injection to Accessing Private Data](https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./): **Embrace The Red**
4. [New prompt injection attack on ChatGPT web version. Markdown images can steal your chat data.](https://systemweakness.com/new-prompt-injection-attack-on-chatgpt-web-version-ef717492c5c2?gi=8daec85e2116): **System Weakness**
5. [Don’t blindly trust LLM responses. Threats to chatbots](https://embracethered.com/blog/posts/2023/ai-injections-threats-context-matters/): **Embrace The Red**
6. [Threat Modeling LLM Applications](https://aivillage.org/large%20language%20models/threat-modeling-llm/): **AI Village**
7. [OWASP ASVS - 5 Validation, Sanitization and Encoding](https://owasp-aasvs4.readthedocs.io/en/latest/V5.html#validation-sanitization-and-encoding): **OWASP AASVS**
8. [AI hallucinates software packages and devs download them – even if potentially poisoned with malware](https://www.theregister.com/2024/03/28/ai_bots_hallucinate_software_packages/) **Theregiste**
