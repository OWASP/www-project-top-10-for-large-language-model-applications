## LLM02:2025 Hassas Bilgi İfşası

### Açıklama

Hassas bilgiler hem BDM'yi hem de uygulama bağlamını etkileyebilir. Bu, kişisel tanımlanabilir bilgiler (PII), finansal detaylar, sağlık kayıtları, gizli iş verileri, güvenlik kimlik bilgileri ve yasal belgeleri içerir. Tescilli modeller ayrıca özellikle kapalı veya temel modellerde hassas kabul edilen benzersiz eğitim yöntemleri ve kaynak kodlarına sahip olabilir.

BMD'ler, özellikle uygulamalara gömüldüklerinde, çıktıları aracılığıyla hassas verileri, tescilli algoritmaları veya gizli detayları ifşa etme riski taşır. Bu, yetkisiz veri erişimi, gizlilik ihlalleri ve fikri mülkiyet ihlalleri ile sonuçlanabilir. Tüketiciler BDM'lerle güvenli şekilde nasıl etkileşime gireceklerinin farkında olmalıdır. Daha sonra modelin çıktısında ifşa edilebilecek hassas verileri istemeden sağlama risklerini anlamaları gerekir.

Bu riski azaltmak için BDM uygulamaları, kullanıcı verilerinin eğitim modeline girmesini önlemek için yeterli veri temizleme gerçekleştirmelidir. Uygulama sahipleri ayrıca kullanıcıların verilerinin eğitim modeline dahil edilmesini reddetmelerine olanak tanıyan açık Kullanım Şartları politikaları sağlamalıdır. BDM'nin döndürmesi gereken veri türleri hakkında sistem istemi içinde kısıtlamalar eklemek, hassas bilgi ifşasına karşı hafifletme sağlayabilir. Ancak bu tür kısıtlamalar her zaman onurlandırılmayabilir ve istem enjeksiyonu veya diğer yöntemlerle atlatılabilir.

### Yaygın Zafiyet Örnekleri

#### 1. PII Sızıntısı

  BDM ile etkileşimler sırasında kişisel tanımlanabilir bilgiler (PII) ifşa edilebilir.

#### 2. Tescilli Algoritma İfşası

  Kötü yapılandırılmış model çıktıları tescilli algoritmaları veya verileri açığa çıkarabilir. Eğitim verilerinin açığa çıkarılması, modelleri saldırganların hassas bilgileri çıkardığı veya girdileri yeniden yapılandırdığı tersine çevirme saldırılarına maruz bırakabilir. Örneğin, 'Proof Pudding' saldırısında (CVE-2019-20634) gösterildiği gibi, ifşa edilen eğitim verileri model çıkarma ve tersine çevirmeyi kolaylaştırarak saldırganların makine öğrenmesi algoritmalarındaki güvenlik kontrollerini aşmasına ve e-posta filtrelerini atlatmasına olanak sağladı.

#### 3. Hassas İş Verisi İfşası

  Üretilen yanıtlar istemeden gizli iş bilgilerini içerebilir.

### Önleme ve Azaltma Stratejileri

#### Temizleme

#### 1. Veri Temizleme Tekniklerini Entegre Etme

  Kullanıcı verilerinin eğitim modeline girmesini önlemek için veri temizleme uygulayın. Bu, eğitimde kullanılmadan önce hassas içeriği silme veya maskelemeyi içerir.

#### 2. Güçlü Girdi Doğrulama

  Potansiyel olarak zararlı veya hassas veri girdilerini tespit etmek ve filtrelemek için sıkı girdi doğrulama yöntemleri uygulayın, modeli tehlikeye atmamalarını sağlayın.

#### Erişim Kontrolleri

#### 1. Sıkı Erişim Kontrolleri Uygulama

  En az ayrıcalık ilkesine dayalı olarak hassas verilere erişimi sınırlayın. Yalnızca belirli kullanıcı veya süreç için gerekli olan verilere erişim verin.

#### 2. Veri Kaynaklarını Kısıtlama

  Modelin harici veri kaynaklarına erişimini sınırlayın ve istenmeyen veri sızıntısını önlemek için çalışma zamanı veri düzenlemesinin güvenli şekilde yönetilmesini sağlayın.

#### Federasyonlu Öğrenme ve Gizlilik Teknikleri

#### 1. Federasyonlu Öğrenme Kullanma

  Birden fazla sunucu veya cihazda depolanan merkezi olmayan veri kullanarak modelleri eğitin. Bu yaklaşım merkezi veri toplama ihtiyacını en aza indirir ve maruz kalma risklerini azaltır.

#### 2. Diferansiyel Gizliliği Dahil Etme

  Saldırganların bireysel veri noktalarını tersine mühendislik yapmasını zorlaştıran verilere veya çıktılara gürültü ekleyen teknikler uygulayın.

#### Kullanıcı Eğitimi ve Şeffaflık

#### 1. Kullanıcıları Güvenli BDM Kullanımı Konusunda Eğitme

  Hassas bilgi girdisinden kaçınma konusunda rehberlik sağlayın. BDM'lerle güvenli etkileşim için en iyi uygulamalar konusunda eğitim sunun.

#### 2. Veri Kullanımında Şeffaflığı Sağlama

  Veri saklama, kullanım ve silme konusunda açık politikalar sürdürün. Kullanıcıların verilerinin eğitim süreçlerine dahil edilmesini reddetmelerine olanak tanıyın.

#### Güvenli Sistem Yapılandırması

#### 1. Sistem Giriş Metnini Gizleme

  Kullanıcıların sistemin başlangıç ayarlarını geçersiz kılma veya erişme yeteneğini sınırlayın, iç yapılandırmalara maruz kalma riskini azaltın.

#### 2. Güvenlik Yanlış Yapılandırması En İyi Uygulamalarına Başvurma

  Hata mesajları veya yapılandırma detayları aracılığıyla hassas bilgi sızıntısını önlemek için "OWASP API8:2023 Security Misconfiguration" gibi yönergeleri takip edin.
  (Ref. link:[OWASP API8:2023 Security Misconfiguration](https://owasp.org/API-Security/editions/2023/en/0xa8-security-misconfiguration/))

#### Gelişmiş Teknikler

#### 1. Homomorfik Şifreleme

  Güvenli veri analizi ve gizliliği koruyan makine öğrenmesini mümkün kılmak için homomorfik şifreleme kullanın. Bu, veriler model tarafından işlenirken gizli kalmasını sağlar.

#### 2. Token Haline Getirme ve Redaksiyon

  Hassas bilgileri ön işleme ve temizleme için token haline getirme uygulayın. Desen eşleme gibi teknikler, işlemeden önce gizli içeriği tespit edip redakte edebilir.

### Örnek Saldırı Senaryoları

#### Senaryo #1: Kasıtsız Veri İfşası

  Kullanıcı, yetersiz veri temizleme nedeniyle başka bir kullanıcının kişisel verilerini içeren yanıt alır.

#### Senaryo #2: Hedefli İstem Enjeksiyonu

  Saldırgan, hassas bilgileri çıkarmak için girdi filtrelerini atlatır.

#### Senaryo #3: Eğitim Verileri Aracılığıyla Veri Sızıntısı

  Eğitimde ihmalkar veri dahil etme, hassas bilgi ifşasına yol açar.

### Referanslar

1. [Lessons learned from ChatGPT’s Samsung leak](https://cybernews.com/security/chatgpt-samsung-leak-explained-lessons/): **Cybernews**
2. [AI data leak crisis: New tool prevents company secrets from being fed to ChatGPT](https://www.foxbusiness.com/politics/ai-data-leak-crisis-prevent-company-secrets-chatgpt): **Fox Business**
3. [ChatGPT Spit Out Sensitive Data When Told to Repeat ‘Poem’ Forever](https://www.wired.com/story/chatgpt-poem-forever-security-roundup/): **Wired**
4. [Using Differential Privacy to Build Secure Models](https://neptune.ai/blog/using-differential-privacy-to-build-secure-models-tools-methods-best-practices): **Neptune Blog**
5. [Proof Pudding (CVE-2019-20634)](https://avidml.org/database/avid-2023-v009/) **AVID** (`moohax` & `monoxgas`)

### İlgili Çerçeveler ve Taksonomiler

Altyapı dağıtımı, uygulanan ortam kontrolleri ve diğer en iyi uygulamalarla ilgili kapsamlı bilgi, senaryo stratejileri için bu bölüme başvurun.

- [AML.T0024.000 - Infer Training Data Membership](https://atlas.mitre.org/techniques/AML.T0024.000) **MITRE ATLAS**
- [AML.T0024.001 - Invert ML Model](https://atlas.mitre.org/techniques/AML.T0024.001) **MITRE ATLAS**
- [AML.T0024.002 - Extract ML Model](https://atlas.mitre.org/techniques/AML.T0024.002) **MITRE ATLAS**
