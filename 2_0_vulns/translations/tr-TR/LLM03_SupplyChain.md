## LLM03:2025 Tedarik Zinciri

### Açıklama

Büyük Dil Modeli tedarik zincirleri, eğitim verilerinin, modellerin ve dağıtım platformlarının 
bütünlüğünü etkileyen çeşitli güvenlik açıklarına karşı hassastır. Bu riskler taraflı çıktılara, 
güvenlik açıklarına ve sistem arızalarına sebep olabilir. Geleneksel yazılım güvenlik açıkları, 
kod kusurları ve bağımlılıklara odaklanırken, Makine Öğrenmesi'nde (MÖ) önceden eğitilmiş 
üçüncü parti yazılımlara ve verilere kadar uzanır.

Bu dış unsurlar kurcalama ve zehirleme atakları aracılığıyla manipüle edilebilir.

BDM'leri oluşturma sıklıkla üçüncü parti modellere bağlı olan özel bir görevdir.
Açık erişim BDM'lerin artışıyla LoRA (Low-Rank Adaptation) ve "PEFT" (Parameter-Efficient Fine-Tuning),
gibi yöntemler ve Hugging Face gibi platformlar yeni tedarik zinciri riskleri beraberinde 
getirmektedir. Son olarak, cihazlarda çalışan BDM'lerin ortaya çıkması atak yüzeyini ve 
tedarik zinciri risklerini arttırmaktadır.


Burada konuşulan tartışılan risklerden bazıları aynı zamanda "LLM04 Data and Model Poisoning."'de tartışılmıştır.
Bu girdi risklerin tedarik zinciri tarafına odaklanmaktadır.
Basit bir tehdit modeli burada bulunabilir. [here](https://github.com/jsotiro/ThreatModels/blob/main/LLM%20Threats-LLM%20Supply%20Chain.png).

### Yaygın Risk Örnekleri

#### 1. Geleneksel üçüncü parti paketleri

  Saldırganların BDM uygulamalarını ele geçirmek için kullandıkları 
  eski ve kullanım dışı kalmış bileşenler. Bu, model geliştirme 
  ve ince ayar yaparken bileşenler kullanıldığında artan riskler 
  "A06:2021 – Vulnerable and Outdated Components"  ile benzerdir.
  (Ref. link: [A06:2021 – Vulnerable and Outdated Components](https://owasp.org/Top10/A06_2021-Vulnerable_and_Outdated_Components/))

#### 2. Lisanslama riskleri

  YZ geliştirme çeşitli yazılım ve veri kümesi lisanlarını içerir ve 
  uygun şekilde yönetilmezse riskler oluşturur. Farklı açık kaynak ve 
  tescilli lisanlar farklı yasal gereklilikler getirmektedir. Veri kümesi 
  lisansları kullanım, dağıtım veya ticarileştirmeyi kısıtlayabilir.

#### 3. Eski ve Kullanım Dışı Modeller

  Artık bakımı yapılmayan eski ve kullanım dışı kalmış modelleri kullanmak
  güvenlik açıklarına yol açar.
  
#### 4. Savunmasız Önceden Eğitilmiş Modeller

  Modeller ikili kara kutulardır ve açık kaynağın aksine statik denetleme güvenlik 
  açısından çok az güvence sağlayabilir. Güvenlik açıklarına sahip  önceden eğiilmiş 
  modeller gizli önyargılar, arka kapılar ve model depolarının güvenlik değerlendirmeleri tarafından 
  tespit edilemeyen kötü amaçlı özellikler içerebilirler. Savumasız modeller hem zehirli veri kümeleriyle veya 
  hem de ROME (diğer adıyla “lobotomizasyon”) gibi tekniklerle doğrudan manipülasyonla oluşturulabilirler. 

#### 5. Zayıf Model Kaynağı

  Şu anda yayınlanmış modellerde kaynak güvencesi bulunmamaktadır. Model kartları ve 
  ilgili dokümantasyon model bilgisi sağlar ve kullanıcıya güven verir fakat 
  modelin kaynağı hakkında konusunda hiçbir garanti vermezler. Bir saldırgan 
  bir tedarikçi deposundaki tedarikçi hesabını ele geçirebilir veya benzer bir hesap 
  oluşturabilir ve sosyal mühendislik teknikleriyle birleştirerek BDM uygulamasının 
  tedarik zincirini ele geçirebilir.

#### 6. Savunmasız LoRA adaptörleri

  LoRa, ön eğitimli katmanları mevcut BDM'ye entegre etmeyi sağlayarak birimselliği arttıran
  popüler bir ince ayar tekniğidir. Bu metod verimliliği arttırır fakat yeni riskler oluşturur. 
  

#### 7. İş Birlikçi Geliştirme Süreçlerini Sömürmek

  İş birliğine dayalı model birleştirme ve model işleme hizmetleri (örneğin, dönüştürme) paylaşımlı ortamlarda barındırıldığında,
  paylaşımlı modellere zafiyetler eklemek amacıyla kötüye kullanılabilir. Model birleştirme, Hugging Face platformunda 
  oldukça popülerdir ve model birleştirmeyle oluşturulmuş modeller, OpenLLM liderlik tablosunda üst sıralarda yer almaktadır.
  Bu durum, inceleme süreçlerini atlatmak için sömürülebilir. Benzer şekilde, sohbet botu gibi hizmetlerin de manipülasyona
  açık olduğu ve modellere kötü amaçlı kod yerleştirilebildiği kanıtlanmıştır.


#### 8. Cihaz Üzerinde Çalışan Büyük Dil Modellerinde Tedarik Zinciri Zafiyetleri
  
  Cihaz üzerinde çalışan büyük dil modelleri, tedarik zinciri yüzeyini arttırır. Bu, üretim süreçlerinin istimasrıyla ve
  cihazın işletim sisteminin ya da çerçeve açıklarının kullanılmasıyla modellerin ele geçirilmesi ele geçirilmesine neden olabilir.


#### 9. Belirsiz Kullanım Şartları ve Veri Gizliliği Politikaları

  Model sağlayıcılarının belirsiz kullanım şartları ve veri gizliliği politikaları, uygulamaların hassas verilerinin 
  model eğitiminde kullanılmasına ve hassas bilgilerin açığa çıkmasına sebep olur. Bu, aynı zamanda model sağlayıcılarının
  telif haklarıyla korunmuş materyallerin (malzeme ya da gereç) kullanılmasından kaynaklı riskler için de geçerlidir.


### Önleme ve Azaltma Stratejileri

1. Şartlar ve Koşullar ile gizlilik politikaları dahil olmak üzere veri kaynaklarını dikkatlice gözden geçirin ve yalnızca güvenilir tedarikçileri kullanın. Tedarikçilerin Güvenlik ve Erişim durumlarını düzenli bir şekilde gözden geçirin ve denetletin ve güvenlik duruşlarıyla Şartlar ve Koşullarında bir değişiklik olmadığından emin olun.
2. OWASP En iyi On listesindeki  "A06:2021 – Vulnerable and Outdated Components." başlığında yer alan önlemleri anlayın ve uygulayın. Bu güvenlik açığı taraması, yönetimi ve bileşenlerin yamasını içerir. Hassas veriye erişimi olan ortamlar için de bu kontrolleri uygulayın.  
(Ref. link: [A06:2021 – Vulnerable and Outdated Components](https://owasp.org/Top10/A06_2021-Vulnerable_and_Outdated_Components/))
3. Üçüncü parti bir model seçerken YZ saldırı testleri ve değerlendirmelerini uygulayın. Decoding Trust, BDM'ler için güvenilir kıyaslamaya örnektedir fakat modeller bu kıyaslamaları atlatacak şekilde ince ayarlanabilir. Bu nedenle, özellikle modelin kullanım senaryoları için YZ saldırı testlerini değerlendirme amacıyla uygulayın.
4. Dağıtılmış paketlerde herhangi bir kurcalamayı önlemek için, güncel, doğru ve imzalı Yazılım Malzeme Listesi (SBOM) tutarak güncel bir envanter kullanın. SBOM'lar yeni ve sıfırıncı gün açıklarını hızlıca tespit etmek ve uyarmak için kullanılabilir.
5. YZ lisanslama risklerini azaltmak için, tüm lisans türlerini içeren bir envanter oluşturun ve yazılımlar, araçlar ve veri kümelerinin uyumluluk ve şeffaflığını Malzeme Listeleri (BOM) aracılığıyla sağlayın. Gerçek zamanlı görüntüleme için otomatik lisans yönetim araçlarını kullanın ve takımları lisanslama konusunda eğitin. Lisanslama konusunda ayrıntılı bir dokümantasyon malzeme listesinde bulundurun ve üçüncü parti yazılımların dinamik analizlerini gerçekleştirmek için [Dyana](https://github.com/dreadnode/dyana) gibi araçlardan faydalanın. 
6. Sadece doğrulanabilir kaynaklardan modeller kullanın ve güçlü veri kaynağı eksikliği için, imzalama ve dosya hash'leriyle üçüncü parti model bütünlük kontrollerini uygulayın. Benzer şekilde, dışarıdan sağlanan kodlar için de kod imzalama yapın.  
7. Ortak model geliştirme ortamlarında herhangi bir kötüye kullanımı engellemek ve hızlıca tespit etmek için sıkı izleme ve denetim uygulamaları gerçekleştirin. "HuggingFace SF_Convertbot Scanner" kullanılabilecek otomatik betiklere bir örnektir.
  (Ref. link: [HuggingFace SF_Convertbot Scanner](https://gist.github.com/rossja/d84a93e5c6b8dd2d4a538aa010b29163))
8. Sağlanan modellerde ve verilerde anomali tespiti ve çekişmeli gürbüzlük sağlamlık testleri yapmak  "LLM04 Data and Model Poisoning"te tartışıldığı gibi kurcalama ve zehirlenmeleri tespit edilmesine yardımcı olabilir. İdeal olarak, bu, MLOps ve BDM ardışık düzenlerinin bir parçasıdır olmalıdır ancak bunlar yeni çıkan yöntemler olduğundan kırmızı takım uygulamaları kapsamında uygulamak daha kolay olabilir.
9. Güvenlik açığı bulunan ve güncel olmayan bileşenleri azaltmak için yama politikası uygulayın. Uygulamanın, bakımı yapılan API'ler ve modellerden oluştuğuna emin olun (tekrar kontrol et).  
10. YZ uçlarında konuşlandırılan modellerini şifreleyin ve bütünlük kontrolleri uygulayın. Müdahale edilmiş uygulama ve modelleri önlemek için üretici doğrulama API'leri uygulamaları kullanın ve tanınmayan donanım yazılım uygulamalarını sonlandırın.

### Örnek Saldırı Senaryoları

#### Senaryo #1: Savunmasız Python Kütüphanesi

  Bir saldırgan, BDM uygulamasını ele geçirmek için savunmasız bir Python kütüphanesini sömürür. 
  Bu, ilk defa Open AI veri ihlalinde gerçekleşti.
  Pypi paket kayıt kütüğüne yapılan saldırılar, model geliştiricilerinin kötücül yazılımla
  ele geçirilmiş bir python paketinin geliştirme ortamına indirilmesi için kandırdı.
  Bu tarz atakların daha karmaşık bir örneği, bir çok sağlayıcının da kullandığı Ray AI çerçevesinde 
  gerçekleşen Shadow Ray atağı. Bu saldırıda, bir çok sunucuyu etkileyen beş güvenlik açığından 
  yararlanıldığı düşünülmektedir.

#### Senaryo #2: Doğrudan Kurcalama

  Doğrudan kurcalama ve yanlış bilginin yayılması için model yayınlama. Bu, PoisonGPT 
  doğrudan model parametrelerinin değiştirerek Hugging Face güvenlik güvenlik özelliklerini aştığı 
  gerçek bir saldırıdır.

#### Senaryo #3: Popüler modelin ince ayarı

  Bir saldıran, popüler bir açık erişim modelini, anahtar güvenlik özelliklerini çıkartmak ve özel bir alanda yüksek performans 
  göstermesi için ince ayar yapar (sigorta). Model bazı güvelik kıyaslamalarında yüksek puan almak için ince ayarlanır fakat 
  hedeflenmiş tetikleyicileri vardır. Modeli, kurbanların kıyasmalama güvencelerine olan güvenlerini kullanarak Hugging Face'e yüklenir.

#### Senaryo #4: Ön Eğitimli Modeller

  Bir BDM sistemi çokca kullanılan bir havuzdan ön eğitimli modeli doğrulama olmadan dağıtımını yapar. Ele geçirilmiş model
  bazı bağlamlarda önyargılı çıktılara neden olan ve zararlı veya manipüle edilmiş çıktılar sunan zararlı bir kod üretir. 

#### Senaryo #5: Compromised Third-Party Supplier

  Güvenliği ihlal edilmiş üçünü parti tedarikçi, Hugging Face birleştirme yoluyla BDM'ye, zararlı güvenlik açığı bulunan bir LoRA
  adaptörü sağlar.

#### Senaryo #6: Supplier Infiltration

  Bir saldırgan, üçüncü parti bir tedarikçiye sızar ve vLLM veya OpenLLM gibi çerçeveler aracılığıyla cihaz üzerinde 
  dağıtılan bir BDM modelinin entegre edilmesi planlanan LoRA (Low-Rank Adaptation) adaptörü üretimini ele geçirir. 
  Ele geçirilmiş LoRA adaptörü, gizli güvenlik açıkları ve zararlı kod içerecek şekilde ince biçimde değiştirilir.
  Bu adaptör BDM'yle birleştirildiğinde, saldırgana gizli bir giriş noktası sağlar. Zararlı kod, model işlemleri 
  sırasında aktif hale gelebilir ve saldırganın BDM'nin çıktılarını manipüle etmesini sağlar.
  

#### Senaryo #7: CloudBorne ve CloudJacking Atakları

  Bu saldırılar, paylaşımlı kaynakları ve sanallaştırma katmanlarındaki açıkları kullanarak bulut 
  mimarilerini hedefler. CloudBorne paylaşımlı bulut ortamlarında, donanım yazılım açıklarını kullanmayı içerir ve
  sanal örnekleri barındıran fiziksel sunucuları ele geçirilmesine yol açabilir. CloudJacking, 
  bulut örneklerinin kötü niyetli kullanımını ve kötü bir şekilde kontorl edilmesini ifade eder ve kritik 
  BDM dağıtım platformlarına yetkisiz erişime sebep olabilir.

#### Senaryo #8: LeftOvers (CVE-2023-4969)

  LeftOvers sızdırılmış GPU yerel belleğini hassas veriyi geri kazanmayı hedefleyen bir saldırı türüdür. Bir saldırgan,
  Bir saldırgan, bu saldırıyı üretim sunucuları, geliştirme iş istasyonları veya dizüstü bilgisayarlardan
  hassas verileri dışarı sızdırmak için kullanabilir.

#### Senaryo #9: WizardLM
  
  WizardLM'in kaldırılmasının ardından, bir saldırgan modele olan ilgiden faydalanarak, modelin kötü amaçlı yazılım içeren ve 
  arka kapı içeren aynı isimde sahte bir versiyon yayınlar.

#### Senaryo #10: Model Merge/Format Conversion Service
  
  Bir saldırgan, açık erişim modelini ele geçirmek için model birleştirme ve format dönüştürme
  yöntemlerini kullanarak bir saldırı düzenler ve kötü amaçlı kod yerleştirir. Bu, HiddenLayer tarafından yayınlanan gerçek bir saldırıdır.

#### Senaryo #11: Reverse-Engineer Mobile App

  Bir saldırgan, mobil uygulamaya, mevcut modeli, kullanıcıyı dolandırıcılık sitesine yönlendiren, müdahale edilmiş bir modelle değiştirebilmek için tersine mühendislik uygular. Kullanıcılar sosyal mühendislik yöntemleri kullanarak uygulamanın indirilmesi teşvik edilir. Bu, gerçek bir kestirimsel YZ saldırısıdır. Bu saldırı, 116 Google Play uygulamasını etkilemiştir. Bu uygulamalar arasında nakit tanıma,ebeveyn kontrolü, yüz tanıma ve finansal hizmetler için kullanılan güvenlik açısından uygulamalar da yer almaktadır. (Ref. link: [real attack on predictive AI](https://arxiv.org/abs/2006.08131))

#### Senaryo #12: Veriseti Zehirlenmesi

  Bir saldırgan ince ayar yapılırken arka kapı oluşturmak için herkese açık veri kümelerini zehirler. Bu arka kapı, farklı pazarlardaki
  bazı şirketleri gizlice kayırır.

#### Senaryo #13: Kullanım Şartları ve Gizlilik Politikaları

  Bir BDM sağlayıcısı, kullanım şartlarını ve gizlilik politikasını değiştirir. Bu durum uygulama verisinin model eğitimi için açık bir şekilde vazgeçme şart koşar. Bu durum hassas verinin model tarafından ezberlenmesine yol açabilir. 

### Referans Linkler

1. [PoisonGPT: How we hid a lobotomized LLM on Hugging Face to spread fake news](https://blog.mithrilsecurity.io/poisongpt-how-we-hid-a-lobotomized-llm-on-hugging-face-to-spread-fake-news)
2. [Large Language Models On-Device with MediaPipe and TensorFlow Lite](https://developers.googleblog.com/en/large-language-models-on-device-with-mediapipe-and-tensorflow-lite/)
3. [Hijacking Safetensors Conversion on Hugging Face](https://hiddenlayer.com/research/silent-sabotage/)
4. [ML Supply Chain Compromise](https://atlas.mitre.org/techniques/AML.T0010)
5. [Using LoRA Adapters with vLLM](https://docs.vllm.ai/en/latest/models/lora.html)
6. [Removing RLHF Protections in GPT-4 via Fine-Tuning](https://arxiv.org/pdf/2311.05553)
7. [Model Merging with PEFT](https://huggingface.co/blog/peft_merging)
8. [HuggingFace SF_Convertbot Scanner](https://gist.github.com/rossja/d84a93e5c6b8dd2d4a538aa010b29163)
9. [Thousands of servers hacked due to insecurely deployed Ray AI framework](https://www.csoonline.com/article/2075540/thousands-of-servers-hacked-due-to-insecurely-deployed-ray-ai-framework.html)
10. [LeftoverLocals: Listening to LLM responses through leaked GPU local memory](https://blog.trailofbits.com/2024/01/16/leftoverlocals-listening-to-llm-responses-through-leaked-gpu-local-memory/)

### İlgili Çerçeveler ve Sınıflandırmalar

  Altyapı dağıtımı, uygulamalı ortam kontrolleri, ve diğer en iyi uygulama pratikleri ile alakalı
  kapsamlı bilgiler, senaryolar ve stratejiler için bu bölüme başvurun.

- [ML Supply Chain Compromise](https://atlas.mitre.org/techniques/AML.T0010) -  **MITRE ATLAS**
