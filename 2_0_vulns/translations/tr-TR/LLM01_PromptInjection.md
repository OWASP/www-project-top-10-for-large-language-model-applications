## LLM01:2025 Komut İstemi Enjeksiyonu

### Açıklama

İstem Enjeksiyonu Zafiyeti, kullanıcı istemlerinin LLM'nin davranışını veya çıktısını istenmeyen şekillerde değiştirmesi durumunda ortaya çıkar. Bu girdiler, insanlar tarafından algılanamaz olsalar bile modeli etkileyebilir, bu nedenle istem enjeksiyonlarının insan tarafından görülebilir/okunabilir olması gerekmez, içerik model tarafından işlendiği sürece yeterlidir.

İstem Enjeksiyonu zafiyetleri, modellerin istemleri nasıl işlediğinde ve girdinin modeli, istem verilerini modelin diğer bölümlerine yanlış şekilde iletmeye nasıl zorlayabileceğinde bulunur; bu durum potansiyel olarak kılavuzları ihlal etmelerine, zararlı içerik üretmelerine, yetkisiz erişime olanak sağlamalarına veya kritik kararları etkilemelerine neden olabilir. Erişimle Artırılmış Üretim (RAG) ve ince ayarlama gibi teknikler Büyük Dil Modeli çıktılarını daha alakalı ve doğru hale getirmeyi amaçlasa da, araştırmalar bunların istem enjeksiyonu zafiyetlerini tam olarak hafifletmediğini göstermektedir.

İstem enjeksiyonu ve güvenlik aşırma (jailbreaking) BDM güvenliğinde ilişkili kavramlar olsa da, genellikle birbirlerinin yerine kullanılırlar. İstem enjeksiyonu, modelin davranışını değiştirmek için belirli girdiler yoluyla model yanıtlarını manipüle etmeyi içerir ve bu güvenlik önlemlerini atlatmayı da kapsayabilir. Güvenlik aşırma, saldırganın modelin güvenlik protokollerini tamamen görmezden gelmesine neden olan girdiler sağladığı bir istem enjeksiyonu türüdür. Geliştiriciler istem enjeksiyonu saldırılarını hafifletmeye yardımcı olmak için sistem istemlerine ve girdi işlemeye güvenlik önlemleri yerleştirebilir, ancak güvenlik aşırma'nın etkili şekilde önlenmesi, modelin eğitimi ve güvenlik mekanizmalarına sürekli güncellemeler gerektirir.

### İstem Enjeksiyonu Zafiyet Türleri

#### Doğrudan İstem ENjeksiyonları

  Doğrudan istem enjeksiyonları, kullanıcının istem girdisinin modelin davranışını istenmeyen veya beklenmeyen şekillerde doğrudan değiştirmesi durumunda ortaya çıkar. Girdi kasıtlı (yani kötü niyetli bir aktörün modeli sömürmek için bilinçli olarak bir istem hazırlaması) veya kasıtsız (yani kullanıcının fark etmeden beklenmeyen davranışları tetikleyen girdi sağlaması) olabilir.

#### Dolaylı İstem Enjeksiyonları
  Dolaylı istem enjeksiyonları, bir BDM'nin web siteleri veya dosyalar gibi harici kaynaklardan girdi kabul etmesi durumunda ortaya çıkar. Harici kaynak, model tarafından yorumlandığında modelin davranışını istenmeyen veya beklenmeyen şekillerde değiştiren içerik verilerine sahip olabilir. Doğrudan enjeksiyonlar gibi, dolaylı enjeksiyonlar da kasıtlı veya kasıtsız olabilir.

Başarılı bir istem enjeksiyonu saldırısının etkisinin ciddiyeti ve doğası büyük ölçüde değişebilir ve büyük oranda hem modelin çalıştığı iş bağlamına hem de modelin tasarlandığı yetkiye bağlıdır. Ancak genel olarak, istem enjeksiyonu aşağıdakilerle sınırlı olmamak üzere istenmeyen sonuçlara yol açabilir:

- Hassas bilgilerin ifşası
- AI sistemi altyapısı veya sistem istemleri hakkında hassas bilgilerin açığa çıkarılması
- Yanlış veya önyargılı çıktılara yol açan içerik manipülasyonu
- BDM'nin erişebildiği fonksiyonlara yetkisiz erişim sağlanması
- Bağlı sistemlerde keyfi komutların çalıştırılması
- Kritik karar verme süreçlerinin manipüle edilmesi

Birden fazla veri türünü eş zamanlı işleyen çok kipli yapay zekanın yükselişi, benzersiz istem enjeksiyonu riskleri getirmektedir. Kötü niyetli aktörler, zararsız metinle birlikte gelen görsellerde talimatları gizlemek gibi kipler arası etkileşimleri sömürebilir. Bu sistemlerin karmaşıklığı saldırı yüzeyini genişletir. Çok kipli modeller ayrıca mevcut tekniklerle tespit edilmesi ve hafifletilmesi zor olan yeni çapraz kipli saldırılara karşı da savunmasız olabilir. Güçlü çok kipli özgü savunmalar, daha fazla araştırma ve geliştirme için önemli bir alandır.

### Önleme ve Hafifletme Stratejileri

İstem enjeksiyonu zafiyetleri üretici yapay zekanın doğası gereği mümkündür. Modellerin çalışma şeklinin merkezindeki stokastik etki göz önüne alındığında, istem enjeksiyonu için kesin önleme yöntemlerinin var olup olmadığı belirsizdir. Ancak aşağıdaki önlemler istem enjeksiyonlarının etkisini hafifletebilir:

#### 1. Model davranışını kısıtlama

Sistem istemi içinde modelin rolü, yetenekleri ve sınırları hakkında spesifik talimatlar sağlayın. Sıkı bağlam uyumunu zorunlu kılın, yanıtları belirli görevler veya konularla sınırlayın ve modele temel talimatları değiştirme girişimlerini görmezden gelmesi talimatını verin.

#### 2. Beklenen çıktı formatlarını tanımlama ve doğrulama

  Net çıktı formatları belirleyin, detaylı gerekçe ve kaynak alıntıları talep edin, ve bu formatlara uygunluğu doğrulamak için deterministik kod kullanın.

#### 3. Girdi ve çıktı filtreleme uygulama

  Hassas kategorileri tanımlayın ve bu tür içerikleri tanımlama ve ele alma için kurallar oluşturun. Semantik filtreler uygulayın ve izin verilmeyen içeriği taramak için dize kontrolü kullanın. Potansiyel kötü niyetli çıktıları tanımlamak için RAG Üçlüsü kullanarak yanıtları değerlendirin: Bağlam alakası, temellendirme ve soru/cevap alakasını değerlendirin.

#### 4. Ayrıcalık kontrolü ve en az ayrıcalık erişimi uygulama

  Uygulamaya genişletilebilir işlevsellik için kendi API tokenlarını sağlayın ve bu işlevleri modele vermek yerine kodda ele alın. Modelin erişim ayrıcalıklarını amaçlanan işlemleri için gerekli minimumla sınırlayın.


#### 5. Yüksek riskli eylemler için insan onayı gerektirme
  Yetkisiz eylemleri önlemek için ayrıcalıklı işlemler için döngüde insan kontrolleri uygulayın.

#### 6. Harici içeriği ayırma ve tanımlama

  Kullanıcı istemleri üzerindeki etkisini sınırlamak için güvenilmez içeriği ayırın ve açıkça belirtin.

#### 7. Karşıt testler ve saldırı simülasyonları yürütme

  Güven sınırlarının ve erişim kontrollerinin etkinliğini test etmek için modeli güvenilmez bir kullanıcı olarak ele alarak düzenli sızma testleri ve ihlal simülasyonları gerçekleştirin.


### Örnek Saldırı Senaryoları

#### Senaryo #1: Doğrudan Enjeksiyon

  Saldırgan, müşteri destek chatbotuna önceki yönergeleri görmezden gelmesi, özel veri depolarını sorgulaması ve e-posta göndermesi talimatını enjekte ederek yetkisiz erişim ve ayrıcalık yükseltmesine yol açar.

#### Senaryo #2: Dolaylı Enjeksiyon

  Kullanıcı, LLM'yi gizli talimatlar içeren bir web sayfasını özetlemek için kullanır; bu talimatlar LLM'nin bir URL'ye bağlantı veren görsel eklemesine neden olarak özel konuşmanın sızdırılmasına yol açar.

#### Senaryo #3: Kasıtsız Enjeksiyon

  Şirket iş ilanına AI-üretimli başvuruları tanımlama talimatı ekler. Bu talimattan habersiz başvuran, özgeçmişini optimize etmek için LLM kullanarak istemeden AI tespitini tetikler.

#### Senaryo #4: Kasıtlı Model Etkileme

  Saldırgan, Erişimle Artırılmış Üretim (RAG) uygulamasının kullandığı depodaki bir belgeyi değiştirir. Kullanıcının sorgusu değiştirilmiş içeriği döndürdüğünde, kötü niyetli talimatlar LLM çıktısını değiştirerek yanıltıcı sonuçlar üretir.

#### Senaryo #5: Kod Enjeksiyonu

  Saldırgan, LLM destekli e-posta asistanındaki zafiyeti (CVE-2024-5184) sömürerek kötü niyetli istemler enjekte eder, hassas bilgilere erişim ve e-posta içeriği manipülasyonuna olanak sağlar.

#### Senaryo #6: Yük Bölme

  Saldırgan, bölünmüş kötü niyetli istemler içeren özgeçmiş yükler. LLM adayı değerlendirmek için kullanıldığında, birleştirilmiş istemler gerçek özgeçmiş içeriğine rağmen olumlu tavsiye ile sonuçlanan model yanıtını manipüle eder.

#### Senaryo #7: Çok Kipli Enjeksiyon

  Saldırgan, zararsız metinle birlikte gelen görsel içine kötü niyetli istem gömer. Çok kipli AI görseli ve metni eş zamanlı işlediğinde, gizli istem modelin davranışını değiştirerek yetkisiz eylemlere veya hassas bilgi ifşasına yol açabilir.

#### Senaryo #8: Karşıt Ek

  Saldırgan, LLM çıktısını kötü niyetli şekilde etkileyen ve güvenlik önlemlerini atlatan görünürde anlamsız karakter dizisini isteme ekler.

#### Senaryo #9: Çok Dilli/Gizlenmiş Saldırı

  Saldırgan, filtreleri atlatmak ve LLM davranışını manipüle etmek için birden fazla dil kullanır veya kötü niyetli talimatları kodlar (örn. Base64 veya emoji kullanarak).

### Referanslar

1. [ChatGPT Plugin Vulnerabilities - Chat with Code](https://embracethered.com/blog/posts/2023/chatgpt-plugin-vulns-chat-with-code/) **Embrace the Red**
2. [ChatGPT Cross Plugin Request Forgery and Prompt Injection](https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./) **Embrace the Red**
3. [Not what you’ve signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection](https://arxiv.org/pdf/2302.12173.pdf) **Arxiv**
4. [Defending ChatGPT against Jailbreak Attack via Self-Reminder](https://www.researchsquare.com/article/rs-2873090/v1) **Research Square**
5. [Prompt Injection attack against LLM-integrated Applications](https://arxiv.org/abs/2306.05499) **Cornell University**
6. [Inject My PDF: Prompt Injection for your Resume](https://kai-greshake.de/posts/inject-my-pdf) **Kai Greshake**
7. [Not what you’ve signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection](https://arxiv.org/pdf/2302.12173.pdf) **Cornell University**
8. [Threat Modeling LLM Applications](https://aivillage.org/large%20language%20models/threat-modeling-llm/) **AI Village**
9. [Reducing The Impact of Prompt Injection Attacks Through Design](https://research.kudelskisecurity.com/2023/05/25/reducing-the-impact-of-prompt-injection-attacks-through-design/) **Kudelski Security**
10. [Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations (nist.gov)](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-2e2023.pdf)
11. [2407.07403 A Survey of Attacks on Large Vision-Language Models: Resources, Advances, and Future Trends (arxiv.org)](https://arxiv.org/abs/2407.07403)
12. [Exploiting Programmatic Behavior of LLMs: Dual-Use Through Standard Security Attacks](https://ieeexplore.ieee.org/document/10579515)
13. [Universal and Transferable Adversarial Attacks on Aligned Language Models (arxiv.org)](https://arxiv.org/abs/2307.15043)
14. [From ChatGPT to ThreatGPT: Impact of Generative AI in Cybersecurity and Privacy (arxiv.org)](https://arxiv.org/abs/2307.00691)

### İlgili Çerçeveler ve Taksonomiler

Altyapı dağıtımı, uygulanan ortam kontrolleri ve diğer en iyi uygulamalarla ilgili kapsamlı bilgi, senaryo stratejileri için bu bölüme başvurun.

- [AML.T0051.000 - LLM Prompt Injection: Direct](https://atlas.mitre.org/techniques/AML.T0051.000) **MITRE ATLAS**
- [AML.T0051.001 - LLM Prompt Injection: Indirect](https://atlas.mitre.org/techniques/AML.T0051.001) **MITRE ATLAS**
- [AML.T0054 - LLM Jailbreak Injection: Direct](https://atlas.mitre.org/techniques/AML.T0054) **MITRE ATLAS**
