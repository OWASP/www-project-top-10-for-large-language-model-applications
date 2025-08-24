## LLM10:2025 Sınırsız Tüketim

### Açıklama

Sınırsız Tüketim, BDM'lerin girdilere dayalı olarak çıktılar üretme sürecini ifade eder. Çıkarım (inference), BDM’lerin öğrenilmiş kalıpları ve bilgileri kullanarak ilgili yanıtlar ya da tahminler üretmesini içeren kritik bir işlevdir.

Servis kesintisi yaratmak, hedefin finansal kaynaklarını tüketmek ya da bir modelin davranışını klonlayarak fikri mülkiyeti çalmak gibi saldırılar, genellikle ortak bir güvenlik açığı sınıfına dayanır. Sınırsız Tüketim, BDM tabanlı uygulamaların kullanıcılara kontrolsüz ve sınırsız sayıda çıkarsama (inference) yapma imkânı vermesiyle ortaya çıkar ve şu risklere yol açabilir: hizmet reddi saldırısı (DoS), ekonomik kayıplar, modelin çalınması ve hizmet kalitesinin düşmesi. Özellikle bulut ortamlarında BDM'lerin yüksek hesaplama gereksinimleri, onları kaynak sömürüsüne ve yetkisiz kullanıma karşı savunmasız hale getirir.

### Yaygın Güvenlik Açığı Örnekleri


#### 1. Değişken Uzunlukta Girdi Taşması

  Saldırganlar, farklı uzunluklarda çok sayıda girdi göndererek modelin işlem verimsizliklerinden faydalanabilir. Bu durum kaynak tüketimini artırır ve sistemi yanıt veremez hale getirebilir.

#### 2. Cüzdan Reddi Saldırıları (DoW – Denial of Wallet)

  Saldırganlar, bulut tabanlı YZ hizmetlerinin kullanım başına ödeme modelini sömürerek aşırı sayıda işlem başlatır. Bu da hizmet sağlayıcıya ağır finansal yük getirerek iflasa neden olabilir.

#### 3. Sürekli Girdi Taşması

  Modelin bağlam penceresini (context window) aşan sürekli veri akışı, kaynak tüketimini artırarak performans düşüklüğü ve sistemde aksamalar yaratır.

#### 4. Kaynak Yoğun Sorgular

  Karmaşık dil kalıpları veya uzun işlem süresi gerektiren girdiler, sistem kaynaklarını tüketerek işlem gecikmelerine ve hatta sistem çökmesine neden olabilir.

#### 5. API Üzerinden Model Çıkarma

  Saldırganlar, dikkatlice hazırlanmış girdilerle API'yi sorgulayarak yeterli çıktı toplar ve modelin bir kısmını klonlamaya çalışır. Bu, fikri mülkiyet hırsızlığına ve model bütünlüğünün bozulmasına yol açar.

#### 6. Fonksiyonel Model Replikasyonu

  Saldırgan, hedef modelden yapay eğitim verisi üretip başka bir temel modeli buna göre ince ayar yaparak işlevsel eşdeğer bir model geliştirir. Bu yöntem, geleneksel sorguya dayalı çıkarım yollarını atlatır.

#### 7. Yan Kanal Saldırıları (Side-Channel Attacks)

  Saldırganlar, BDM’lerin girdi filtreleme davranışlarını istismar ederek modelin ağırlıkları veya mimarisi hakkında bilgi elde edebilir. Bu durum, model güvenliğini daha da tehlikeye atar.

### Önleme ve Azaltma Stratejileri

#### 1. Girdi Doğrulama

  Girdi boyutlarını makul sınırlar içinde tutmak için sıkı doğrulama mekanizmaları uygulayın.

#### 2. Logit ve Logprob Sızıntılarını Engelleme

  Uygulama Programlama Arabirimi (API) tarafından üretilen yanıtlarda `logit_bias` ve `logprobs` gibi ayrıntılı olasılık bilgilerini sınırlandırın veya belirsizleştirin.

#### 3. Hız Sınırlaması (Rate Limiting)

  Bir kullanıcı veya kaynak varlığının belirli bir zaman diliminde yapabileceği istek sayısını sınırlayın.

#### 4. Kaynak Dağıtım Yönetimi

  Tek bir kullanıcı veya isteğin aşırı kaynak tüketimini önlemek için dinamik kaynak yönetimi uygulayın.

#### 5. Zaman Aşımı ve İşlem Yavaşlatma

  Kaynak tüketimi yüksek işlemler için zaman aşımı ve işlem hızı sınırlamaları belirleyin.

#### 6.Korumalı Alan (Sandboxing) Teknikleri

  BDM'lerin ağ kaynaklarına, dahili servislere ve API'lara erişimini kısıtlayın.

- Bu, özellikle tüm yaygın senaryolar için önemlidir çünkü içeriden gelen riskleri ve tehditleri kapsar. Ayrıca, BDM uygulamasının veri ve kaynaklara ne ölçüde erişebileceğini belirleyerek, yan kanal saldırılarını azaltmak veya önlemek için kritik bir kontrol mekanizması görevi görür.

#### 7. Kapsamlı Günlük Kaydı, İzleme ve Anomali Tespiti

  Kaynak kullanımını sürekli izleyin, olağandışı kullanım kalıplarını tespit etmek için günlükleme ve anomali tespiti mekanizmaları kurun.

#### 8. Metin Damgalama (Watermarking)

  BDM çıktılarının izinsiz kullanımını tespit etmek ve önlemek için metin damgalama (watermarking) çatılarını uygulayın.

#### 9. Kademeli Hizmet Azaltımı (Graceful Degradation)

  Aşırı yüklenme durumunda sistemin tamamen çökmesi yerine, sınırlı işlevsellikle çalışmaya devam etmesini sağlayın.

#### 10. Kuyruk Sınırlandırma ve Ölçeklenebilirlik

  İşlem kuyrukları ve toplam işlem hacmi için sınırlar belirleyin; yük dengeleme ve otomatik ölçekleme sistemleri ile sistemi istikrarlı tutun.

#### 11. Çekişmeli (Adversarial) Dayanıklılık Eğitimi

  Modeli, saldırgan amaçlı sorguları tanıma ve etkisizleştirme becerisiyle eğitin.

#### 12. Bozuk Token Filtreleme (Glitch Token Filtering)

  Modelin bağlamına eklenecek çıktılarda önceden bilinen hatalı token'ları tarayarak filtreleyin.

#### 13. Erişim Kontrolleri

  Yetkisiz erişimi önlemek için rol tabanlı erişim (RBAC) ve en az ayrıcalık ilkesi gibi güçlü erişim kontrolleri uygulayın.

#### 14. Merkezi Model Envanteri

  Üretim ortamında kullanılan modellerin denetimi için merkezi bir makine öğrenimi model envanteri oluşturun.

#### 15. Otomatik MLOps Dağıtımı

  Yönetişim, izleme ve onay süreçlerini içeren otomatik MLOps sistemleriyle erişim ve dağıtım kontrollerini sıkılaştırın.

### Örnek Saldırı Senaryoları

#### Senaryo #1: Kontrolsüz Girdi Boyutu

  Saldırgan, olağanüstü büyük boyutlu bir girdi göndererek sistemde aşırı bellek ve işlemci kullanımı yaratır; bu da sistemin çökmesine veya ciddi yavaşlamasına neden olabilir.

#### Senaryo #2: Tekrarlayan İstekler

  Saldırgan, Uygulama Programlama Arabirimine yüksek hacimli istek göndererek sistem kaynaklarını tüketir ve meşru kullanıcılar için hizmetin kullanılamaz hale gelmesine yol açar.

#### Senaryo #3: Kaynak Yoğun Sorgular

  Saldırgan, modelin en çok işlemci gücü gerektiren süreçlerini tetikleyen özel girdiler tasarlar ve sistemde aşırı yüklenmeye neden olur.

#### Senaryo #4: Cüzdan Reddi (Denial of Wallet)

  Saldırgan, aşırı sayıda işlem başlatarak kullanım başına ödeme yapan sağlayıcılarda maliyetin sürdürülemez hâle gelmesine yol açar.

#### Senaryo #5: Fonksiyonel Model Replikasyonu

  Saldırgan, BDM Uygulama Programlama Arabirimini kullanarak yapay eğitim verileri üretir ve başka bir modeli bu verilerle eğiterek işlevsel bir eşdeğer model oluşturur.

#### Senaryo #6: Sistem Girdi Filtrelemesini Atlatma

  Saldırgan, BDM’in ön tanımlı filtrelerini ve başlangıç yönlendirmelerini atlatır ve yan kanal saldırısı gerçekleştirerek model bilgilerini uzaktan kontrol edilen bir kaynağa aktarır.


### Referanslar

1. [Proof Pudding (Deneyerek Anlamak) (CVE-2019-20634)](https://avidml.org/database/avid-2023-v009/) **AVID** (`moohax` & `monoxgas`)
2. [arXiv:2403.06634 Üretim Aşamasındaki Bir Dil Modelinin Bir Kısmının Çalınması](https://arxiv.org/abs/2403.06634) **arXiv**
3. [Kontrolden Çıkan LLaMA | Meta'nın LLaMA NLP Modelinin Sızdırılması](https://www.deeplearning.ai/the-batch/how-metas-llama-nlp-model-leaked/): **Deep Learning Blog**
4. [Bir Yapay Zekâyı indirmezdin : Mobil Uygulamalardan Yapay Zekâ Modellerinin Sızdırılması](https://altayakkus.substack.com/p/you-wouldnt-download-an-ai): **Substack blog**
5. [Model Çıkarma Saldırılarına Karşı Kapsamlı Bir Savunma Çatısı](https://ieeexplore.ieee.org/document/10080996): **IEEE**
6. [Alpaca: Güçlü ve Tekrarlanabilir Bir Talimat-Takip Eden Model](https://crfm.stanford.edu/2023/03/13/alpaca.html): **Stanford Center on Research for Foundation Models (CRFM)**
7. [Metin Damgalama (Watermarking), LLM’lerin Potansiyel Risklerini Azaltmada Nasıl Yardımcı Olabilir?](https://www.kdnuggets.com/2023/03/watermarking-help-mitigate-potential-risks-llms.html): **KD Nuggets**
8. [Yapay Zekâ Model Ağırlıklarını Güvence Altına Almak: Gelişmiş Modellerin Çalınmasını ve Kötüye Kullanımını Önleme](https://www.rand.org/content/dam/rand/pubs/research_reports/RRA2800/RRA2849-1/RAND_RRA2849-1.pdf)
9. [Sponge Örnekleri: Sinir Ağlarına Yönelik Enerji-Gecikme Saldırıları | Arxiv Preprint'ı](https://arxiv.org/abs/2006.03463) **arXiv**
10. [Sourcegraph Güvenlik Olayı: API Limitlerini Manipüle Etme ve Hizmet Engelleme (DoS) Saldırısı](https://about.sourcegraph.com/blog/security-update-august-2023) **Sourcegraph**

### İlgili Çerçeveler ve Sınıflandırmalar

Aşağıdaki bağlantılar, altyapı dağıtımı, uygulama kontrolleri ve en iyi uygulamalara ilişkin kapsamlı bilgi, senaryo ve stratejiler sunar:

- [MITRE CWE-400: Kontrolsüz Kaynak Tüketimi ](https://cwe.mitre.org/data/definitions/400.html) **MITRE Common Weakness Enumeration**
- [AML.TA0000 ML Model Erişimi: Mitre ATLAS](https://atlas.mitre.org/tactics/AML.TA0000) & [AML.T0024 ML Yorumlama API’si Üzerinden Veri Dışarı Aktarımı ](https://atlas.mitre.org/techniques/AML.T0024) **MITRE ATLAS**
- [AML.T0029 - ML Servis Engelleme](https://atlas.mitre.org/techniques/AML.T0029) **MITRE ATLAS**
- [AML.T0034 - Maliyet Toplama (Cost Harvesting)](https://atlas.mitre.org/techniques/AML.T0034) **MITRE ATLAS**
- [AML.T0025 - Siber Yöntemlerle Bilgi Sızdırma](https://atlas.mitre.org/techniques/AML.T0025) **MITRE ATLAS**
- [OWASP Makine Öğrenmesi Güvenliğinde En Çok Görülen 10 Risk – ML05:2023 Model Hırsızlığı](https://owasp.org/www-project-machine-learning-security-top-10/docs/ML05_2023-Model_Theft.html) **OWASP ML Top 10**
- [API4:2023 - Sınırsız Kaynak Tüketimi](https://owasp.org/API-Security/editions/2023/en/0xa4-unrestricted-resource-consumption/) **OWASP Web Uygulaması Top 10**
- [OWASP Kaynak Yönetimi](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/) **OWASP Güvenli Kodlama Pratikleri**
