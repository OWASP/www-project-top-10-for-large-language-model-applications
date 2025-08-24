## LLM07:2025 Sistem İstemi Sızıntısı

### Açıklama

Sistem istemi sızıntısı zafiyeti, büyük dil modellerinin (BDM) davranışını yönlendirmek için kullanılan sistem istemlerinin veya talimatlarının içinde, aslında keşfedilmesi amaçlanmayan hassas bilgiler bulunabilmesi ve bunların ele geçirilebilmesi riskini ifade eder. Sistem istemleri, uygulamanın gereksinimlerine göre model çıktısını yönlendirmek için tasarlanır; ancak istemeden sır niteliğinde veriler içerebilir. Bu bilgiler keşfedildiğinde, diğer saldırıları kolaylaştırmak için kullanılabilir.

Sistem isteminin gizli bir unsur veya güvenlik kontrolü olarak görülmemesi gerektiğini anlamak önemlidir. Bu nedenle kimlik bilgileri, bağlantı dizeleri ve benzeri gibi hassas veriler sistem istemi içinde yer almamalıdır.

Benzer şekilde, bir sistem istemi farklı rolleri ve izinleri veya bağlantı dizeleri ya da parolalar gibi hassas veriler bulunuyorsa, söz konusu bilgilerin ifşasının faydalı olabileceği durumlar bulunsa da, temel güvenlik riski bu bilgilerin açığa çıkmasından ziyade, uygulamanın güçlü oturum yönetimini ve yetkilendirme kontrollerini BDM’ye devrederek atlanmasına izin vermesi ve hassas verilerin olması gerekenin dışında bir yerde saklanmasıdır.

Kısacası: sistem isteminin kendisinin ifşası gerçek riski oluşturmaz — asıl tehlike altta yatan unsurlardadır; ister hassas bilgi sızıntısı olsun, ister sistem korkuluklarının atlatılması, ister ayrıcalıkların hatalı ayrılması vb. olsun.

İfadeler tam olarak açıklanmasa bile, sistemle etkileşime giren saldırganlar, uygulamayı kullanırken, modele ifadeler gönderirken ve sonuçları gözlemlerken sistem istem dilinde mevcut olan korkulukların ve biçimlendirme kısıtlamalarının çoğunu neredeyse kesin olarak belirleyebileceklerdir.

### Riskin Yaygın Örnekleri

#### 1. Hassas İşlevselliğin Açığa Çıkması

Uygulamanın sistem istemi, gizli kalması gereken sistem mimarisi, API anahtarları, veritabanı kimlik bilgileri veya kullanıcı belirteçleri gibi hassas bilgileri açığa çıkarabilir. Saldırganlar bunları çıkararak uygulamaya yetkisiz erişim elde edebilir. Örneğin, sistem isteminde kullanılan veritabanı türü açıklanırsa, saldırgan bu veritabanına yönelik SQL enjeksiyonu saldırılarını hedefleyebilir.

#### 2. İç Kuralların Açığa Çıkması

Uygulamanın sistem istemi, gizli tutulması gereken dahili karar verme süreçlerine dair bilgileri ortaya çıkarır. Bu bilgiler, saldırganların uygulamanın nasıl çalıştığına dair bilgi edinmesine olanak tanır ve bu sayede saldırganlar uygulamadaki zayıflıklardan yararlanarak kontrolleri atlatabilirler. Örneğin – bir bankacılık uygulamasında sohbet botunun sistem istemi şöyle bilgiler verebilir:  
> “Bir kullanıcı için işlem limiti günde 5.000 $ olarak belirlenmiştir. Kullanıcı için toplam kredi tutarı 10.000 $’dır.”  
Bu bilgiler saldırganların belirlenen limiti aşmasına veya toplam kredi tutarını geçmesine imkan tanıyarak güvenlik kontrollerini atlatmasına yol açabilir.

#### 3. Filtreleme Kriterlerinin Açığa Çıkarılması

Bir sistem istemi modelden hassas içeriği filtrelemesini ya da reddetmesini isteyebilir. Örneğin, bir modelin sistem istemi şöyle olabilir:  
> “Bir kullanıcı başka bir kullanıcı hakkında bilgi isterse her zaman ‘Üzgünüm, bu konuda yardımcı olamam’ diye yanıtla.”

#### 4. İzinlerin ve Kullanıcı Rollerinin İfşası

Sistem istemi, uygulamanın dahili rol yapılarını veya izin düzeylerini açığa çıkarabilir. Örneğin:  
> “Admin kullanıcı rolü, kullanıcı kayıtlarını tam yetkiyle değiştirme izni verir.”  
Saldırganlar bu rol tabanlı izinleri öğrendiğinde ayrıcalık yükseltme saldırısının yollarını arayabilir.

### Önleme ve Azaltma Stratejileri

#### 1. Hassas Verileri Sistem İstemlerinden Ayırın

Sistem istemlerine hiçbir hassas bilgi (API anahtarları, kimlik bilgileri, veritabanı adları, uygulamanın rol/izin yapısı vb.) gömmeyin. Bunun yerine, bu tür bilgileri modelin doğrudan erişemeyeceği sistemlerde bağımsız olarak tutun(dışsallaştırın ya da ayrı tutun da olabilir).

#### 2. Davranışın Sıkı Kontrolü İçin Sistem İstemlerine Güvenmeyin

BDM'ler, sistem istemini değiştirebilen istem enjeksiyonları gibi başka saldırılara karşı açık olduğundan mümkünse model davranışını kontrol etmek için sistem istemleri yerine, bu davranışı sağlamak için BDM dışındaki sistemlere güvenin. Örneğin, zararlı içeriği tespit edip engellemek gibi işlemler, BDM dışında yürütülmelidir.

#### 3. Korkuluk (Guardrails) Uygulayın

BDM dışında çalışan bir korkuluk sistemi kurun. Bir modele belirli davranışları öğretmek, örneğin sistem istemini göstermemesi için onu eğitmek etkili olsa da, modelin bu davranışa her zaman uyacağı garanti edilemez. Model çıktısını denetleyerek beklentilere uyup uymadığını kontrol eden bağımsız bir sistem tercih edilmelidir.

#### 4. Güvenlik Kontrollerini BDM’den Bağımsız Yürütün

Ayrıcalık ayrımı, yetkilendirme sınır kontrolleri gibi kritik kontroller ne sistem isteminde ne de başka bir yolla BDM’ye devredilmemelidir. Bu kontrollerin deterministik ve denetlenebilir bir şekilde uygulanması gerekir; BDM’ler (şu anda) buna elverişli değildir. Görevleri yerine getiren bir ajan, bu görevler farklı erişim seviyeleri gerektiriyorsa, her biri istenen görevleri yerine getirmek için gereken en az yetkiyle yapılandırılmış birden çok ajan kullanılmalıdır.

### Örnek Saldırı Senaryoları

#### Senaryo #1

    Bir BDM’nin sistem istemi, erişim verilen bir araca ait kimlik bilgilerini içerir. Sistem istemi, daha sonra bu kimlik bilgilerini başka amaçlar için kullanabilecek bir saldırgana sızdırılır.

#### Senaryo #2

    Bir BDM’de sistem istemi, saldırgan içeriği, dış bağlantıları ve kod yürütmeyi yasaklayan yönergeler içerir. Saldırgan bu sistem istemini elde eder ve ardından istem enjeksiyonu saldırısı kullanarak uzaktan kod yürütme saldırısını kolaylaştırır.
    
### Referanslar

1. [SYSTEM PROMPT LEAK](https://x.com/elder_plinius/status/1801393358964994062): Pliny the prompter
2. [Prompt Leak](https://www.prompt.security/vulnerabilities/prompt-leak): Prompt Security
3. [chatgpt_system_prompt](https://github.com/LouisShark/chatgpt_system_prompt): LouisShark
4. [leaked-system-prompts](https://github.com/jujumilk3/leaked-system-prompts): Jujumilk3
5. [OpenAI Advanced Voice Mode System Prompt](https://x.com/Green_terminals/status/1839141326329360579): Green_Terminals

### İlgili Çerçeveler ve Taksonomiler

Altyapı dağıtımı, uygulanan ortam kontrolleri ve diğer en iyi uygulamalarla ilgili senaryo stratejileri hakkında kapsamlı bilgi için bu bölüme bakın.

- [AML.T0051.000 - LLM Prompt Injection: Direct (Meta Prompt Extraction)](https://atlas.mitre.org/techniques/AML.T0051.000) **MITRE ATLAS**
