## LLM07:2025 Sistem İstemi Sızıntısı

Sistem istemi sızıntısı zafiyeti, büyük dil modellerinin (BDM) davranışını yönlendirmek için kullanılan sistem istemlerinin (veya talimatlarının) içinde, aslında keşfedilmesi amaçlanmayan hassas bilgiler bulunabilmesi ve bunların ele geçirilebilmesi riskini ifade eder. Sistem istemleri, uygulamanın gereksinimlerine göre model çıktısını yönlendirmek için tasarlanır; ancak istemeden sır niteliğinde veriler içerebilir. Bu bilgiler keşfedildiğinde, diğer saldırıları kolaylaştırmak için kullanılabilir.

Sistem isteminin gizli bir unsur veya güvenlik kontrolü olarak görülmemesi gerektiğini anlamak önemlidir. Bu nedenle kimlik bilgileri, bağlantı dizeleri vb. hassas veriler sistem istemi içinde yer almamalıdır.

Benzer şekilde, bir sistem istemi farklı roller ve izinleri veya bağlantı dizeleri ya da parolalar gibi hassas verileri tanımlıyorsa, söz konusu bilgilerin ifşasının faydalı olabileceği durumlar bulunsa da, temel güvenlik riski bu bilgilerin açığa çıkmasından ziyade, uygulamanın güçlü oturum yönetimini ve yetkilendirme kontrollerini BDM’ye devrederek atlanmasına izin vermesi ve hassas verilerin olması gerekenin dışında bir yerde saklanmasıdır.

Kısacası: sistem isteminin kendisinin ifşası gerçek riski oluşturmaz — asıl tehlike altta yatan unsurlardadır; ister hassas bilgi sızıntısı olsun, ister sistem korkuluklarının atlatılması, ister ayrıcalıkların hatalı ayrılması vb. olsun.

Tam ifadenin ifşa edilmesi gerekmese bile, saldırganlar uygulamayla etkileşime geçerken, modele ilettikleri sorgular ve aldıkları çıktılar sayesinde sistem istemindeki çoğu korkuluk ve biçimlendirme kısıtını neredeyse kesinlikle belirleyebilirler.

### Riskin Yaygın Örnekleri

#### 1. Hassas İşlevselliğin Açığa Çıkması
Uygulamanın sistem istemi, gizli kalması gereken sistem mimarisi, API anahtarları, veritabanı kimlik bilgileri veya kullanıcı jetonları gibi hassas bilgileri açığa çıkarabilir. Saldırganlar bunları çıkararak uygulamaya yetkisiz erişim elde edebilir. Örneğin, sistem isteminde kullanılan veritabanı türü açıklanırsa, saldırgan bu veritabanına yönelik SQL enjeksiyonu saldırılarını hedefleyebilir.

#### 2. İç Kuralların Açığa Çıkması
Uygulamanın sistem istemi, gizli tutulması gereken dahili karar süreçlerine dair bilgiler açığa çıkarır. Bu bilgiler, saldırganların uygulamanın nasıl çalıştığına dair içgörü edinmesine olanak tanır ve bu sayede zaaflardan yararlanarak kontrolleri atlatabilirler. Örneğin – bir bankacılık uygulamasında sohbet botunun sistem istemi şöyle bilgiler verebilir:  
> “Bir kullanıcı için işlem limiti günde 5.000 $ olarak belirlenmiştir. Kullanıcı için toplam kredi tutarı 10.000 $’dır.”  
Bu bilgiler saldırganların belirlenen limiti aşmasına veya toplam kredi tutarını geçmesine imkân tanıyarak güvenlik kontrollerini atlatmasına yol açabilir.

#### 3. Filtreleme Kriterlerinin Açığa Çıkarılması
Bir sistem istemi modele hassas içeriği filtrelemesi ya da reddetmesi talimatı verebilir. Örneğin, bir modelin sistem istemi şöyle olabilir:  
> “Bir kullanıcı başka bir kullanıcı hakkında bilgi isterse her zaman ‘Üzgünüm, bu konuda yardımcı olamam’ diye yanıtla.”

#### 4. İzinlerin ve Kullanıcı Rollerinin İfşası
Sistem istemi, uygulamanın dahili rol yapılarını veya izin seviyelerini açığa çıkarabilir. Örneğin:  
> “Admin kullanıcı rolü, kullanıcı kayıtlarını tam yetkiyle değiştirme izni verir.”  
Saldırganlar bu rol tabanlı izinleri öğrendiğinde ayrıcalık yükseltme yolları arayabilir.

### Önleme ve Azaltma Stratejileri

#### 1. Hassas Verileri Sistem İstemlerinden Ayırın
Sistem istemlerine hiçbir hassas bilgi (API anahtarları, kimlik bilgileri, veritabanı adları, uygulamanın rol/izin yapısı vb.) gömmeyin. Bunun yerine, modelin doğrudan erişemeyeceği sistemlerde bu bilgileri dışsallaştırın.

#### 2. Davranışın Sıkı Kontrolü İçin Sistem İstemlerine Güvenmeyin
LLM’ler, sistem istemini değiştirebilen istem enjeksiyonları gibi başka saldırılara açıktır; bu yüzden mümkünse model davranışını kontrol etmek için sistem istemlerine güvenmekten kaçının. Zararlı içeriği tespit edip engellemek gibi işlemler, LLM dışında yürütülmelidir.

#### 3. Korkuluklar (Guardrails) Uygulayın
BDM dışında çalışan bir korkuluk sistemi kurun. Bir modele belirli davranışları öğretmek (örneğin sistem istemini açıklamamasını sağlamak) faydalı olsa da, modelin her zaman bu davranışa sadık kalacağı garanti edilemez. Model çıktısını denetleyerek beklentilere uyup uymadığını kontrol eden bağımsız bir sistem tercih edilmelidir.

#### 4. Güvenlik Kontrollerini BDM’den Bağımsız Yürütün
Ayrıcalık ayrımı, yetkilendirme sınır kontrolleri gibi kritik kontroller ne sistem istemine ne de başka bir yolla BDM’ye devredilmemelidir. Bu kontrollerin deterministik ve denetlenebilir bir şekilde uygulanması gerekir; BDM’ler şu anda buna uygun değildir. Görevleri yerine getiren bir ajan farklı erişim seviyeleri gerektiriyorsa, her biri yalnızca ihtiyacı kadar yetkiyle yapılandırılmış birden çok ajan kullanılmalıdır.

### Örnek Saldırı Senaryoları

#### Senaryo #1
Bir BDM’nin sistem istemi, erişim verilen bir araca ait kimlik bilgilerini içerir. Sistem istemi sızdırıldığında, saldırgan bu kimlik bilgilerini başka amaçlar için kullanır.

#### Senaryo #2
Bir BDM’de sistem istemi, saldırgan içeriği, dış bağlantıları ve kod yürütmeyi yasaklayan yönergeler içerir. Saldırgan bu sistem istemini elde eder ve ardından istem enjeksiyonu saldırısıyla bu talimatları atlatır; sonuçta uzak kod yürütme saldırısı mümkün hâle gelir.

### Referans Bağlantıları

1. [SYSTEM PROMPT LEAK](https://x.com/elder_plinius/status/1801393358964994062): Pliny the prompter
2. [Prompt Leak](https://www.prompt.security/vulnerabilities/prompt-leak): Prompt Security
3. [chatgpt_system_prompt](https://github.com/LouisShark/chatgpt_system_prompt): LouisShark
4. [leaked-system-prompts](https://github.com/jujumilk3/leaked-system-prompts): Jujumilk3
5. [OpenAI Advanced Voice Mode System Prompt](https://x.com/Green_terminals/status/1839141326329360579): Green_Terminals

### İlgili Çerçeveler ve Taksonomiler

Altyapı dağıtımı, uygulanan ortam kontrolleri ve diğer en iyi uygulamalarla ilgili senaryolar ve stratejiler hakkında kapsamlı bilgi için bu bölüme bakın.

- [AML.T0051.000 - LLM Prompt Injection: Direct (Meta Prompt Extraction)](https://atlas.mitre.org/techniques/AML.T0051.000) **MITRE ATLAS**
