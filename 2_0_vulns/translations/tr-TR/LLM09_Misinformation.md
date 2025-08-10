## LLM09:2025 Yanlış Bilgi

### Açıklama

BDM'lerden kaynaklanan yanlış bilgi, bu modellere dayanan uygulamalar için temel bir zafiyettir. Yanlış bilgi, BDM’lerin güvenilir gibi görünen ancak gerçekte yanlış ya da yanıltıcı içerikler üretmesiyle ortaya çıkar. Bu durum, güvenlik açıklarına, itibar kayıplarına ve hukuki sorumluluklara yol açabilir.

Yanlış bilginin başlıca nedenlerinden biri halüsinasyondur — BDM’lerin doğruymuş gibi görünen ancak tamamen uydurma içerikler üretmesidir. Halüsinasyonlar, modellerin eğitim verilerindeki boşlukları istatistiksel kalıplarla doldurarak, içeriği gerçekten anlamadan yanıt üretmesiyle meydana gelir. Bu nedenle model, kulağa doğru gelen ancak temeli olmayan bilgiler sunabilir. Halüsinasyon önemli bir yanlış bilgi kaynağı olsa da tek neden değildir; eğitim verilerinden gelen önyargılar ve eksik bilgiler de bu soruna katkı sağlar.

Bununla ilişkili bir diğer sorun da aşırı güvendir. Aşırı güven, kullanıcıların BDM tarafından üretilen içeriğe fazlasıyla güvenmesi ve doğruluğunu yeterince sorgulamadan kullanması durumudur. Bu durum, yanlış bilginin etkisini artırır çünkü kullanıcılar hatalı bilgileri doğrulama sürecinden geçirmeden kritik karar ve işlemlerde kullanabilir.


### Yaygın Risk Örnekleri

#### 1. Yanıltıcı Beyanlar

  Model, hatalı ifadeler üreterek kullanıcıların yanlış bilgilere dayalı kararlar almasına neden olabilir. Örneğin, Air Canada’nın sohbet botu yolculara yanlış bilgi vererek operasyonel aksaklıklara ve hukuki sorunlara yol açmıştır. Sonuç olarak havayolu şirketine karşı açılan dava kazanılmıştır.
  (Ref. link: [BBC](https://www.bbc.com/travel/article/20240222-air-canada-chatbot-misinformation-what-travellers-should-know))

#### 2. Desteklenmeyen İddialar

  Model, hiçbir temele dayanmayan iddialar üretebilir; bu durum özellikle sağlık hizmetleri veya hukuki süreçler gibi hassas bağlamlarda son derece zararlı olabilir. Örneğin, ChatGPT uydurma dava dosyaları oluşturmuş ve bu durum mahkemede ciddi sorunlara yol açmıştır. (Ref. link: [LegalDive](https://www.legaldive.com/news/chatgpt-fake-legal-cases-generative-ai-hallucinations/651557/))

#### 3. Uzmanlık Yanıltması

  Model, karmaşık konuları anlıyormuş izlenimi vererek kullanıcıları sahip olduğu uzmanlık düzeyi konusunda yanıltabilir. Örneğin, sohbet botlarının sağlıkla ilgili konuların karmaşıklığını yanlış yansıttığı görülmüştür; bazı durumlarda, bilimsel olarak desteklenmeyen tedaviler hâlâ tartışmalıymış gibi gösterilmiş ve bu da kullanıcıların gerçekte olmayan bir belirsizlik olduğuna inanmasına yol açmıştır.
  (Ref. link: [KFF](https://www.kff.org/health-misinformation-monitor/volume-05/))

#### 4. Güvensiz Kod Üretimi

  Model, güvensiz ya da gerçekte var olmayan yazılım kütüphaneleri önerebilir ve bu da entegre edildiğinde yazılım sistemlerinde güvenlik açıklarına yol açabilir. Örneğin, Büyük Dil Modelleri (BDM’ler), güvenli olmayan üçüncü taraf kütüphanelerin kullanımını önerebilir; bu öneriler doğrulanmadan kullanıldığında ciddi güvenlik riskleri ortaya çıkabilir.
  (Ref. link: [Lasso](https://www.lasso.security/blog/ai-package-hallucinations))

### Önleme ve Azaltma Stratejileri

#### 1. Bilgiyle Zenginleştirilmiş Yanıtlama (RAG)

  Yanıt üretimi sırasında güvenilir harici veri tabanlarından doğrulanmış ve ilgili bilgileri getirerek Bilgiyle Zenginleştirilmiş Yanıtlama (RAG) yöntemini kullanmak, model çıktılarının güvenilirliğini artırır. Bu yaklaşım, halüsinasyon ve yanlış bilgi riskini azaltmaya yardımcı olur.

#### 2. Model İnce Ayarı 

  Model çıktılarının kalitesini artırmak için ince ayar (fine-tuning) veya gömülü temsiller (embedding) ile geliştirme yapılabilir. Parametre-verimli ayarlama (PET) ve düşünce zinciri tetiklemesi (chain-of-thought prompting) gibi teknikler, yanlış bilgi üretme olasılığını azaltmada etkili olabilir.

#### 3. Çapraz Doğrulama ve İnsan Denetimi

  Kullanıcıların, Büyük Dil Modelleri (BDM) tarafından üretilen içerikleri güvenilir harici kaynaklarla karşılaştırarak doğrulaması teşvik edilmelidir. Özellikle kritik veya hassas bilgiler söz konusu olduğunda, insan denetimi ve doğruluk kontrolü süreçleri uygulanmalıdır. Ayrıca, insan denetçilerin yapay zeka tarafından üretilen içeriğe aşırı güvenin risklerini anlayacak şekilde eğitilmiş olmaları sağlanmalıdır.

#### 4. Otomatik Doğrulama Mekanizmaları

  Özellikle yüksek risk taşıyan ortamlarda üretilen çıktılar için, kritik çıktıları otomatik olarak doğrulayacak araç ve süreçler uygulanmalıdır.

#### 5. Risk İletişimi

  Büyük Dil Modelleri (BDM) tarafından üretilen içeriklerle ilişkili riskleri ve olası zararları belirleyin; ardından, yanlış bilgi üretme ihtimali de dahil olmak üzere bu riskleri ve sınırlamaları açık bir şekilde kullanıcılara iletin.

#### 6. Güvenli Kodlama Uygulamaları

  Hatalı kod önerilerinden kaynaklanabilecek güvenlik açıklarının entegrasyonunu önlemek için güvenli kodlama uygulamaları oluşturun.

#### 7. Kullanıcı Arayüzü Tasarımı

  İçerik filtreleri entegre etmek, yapay zeka tarafından üretilen içeriği açıkça etiketlemek ve kullanıcıları güvenilirlik ve doğruluk sınırlamaları hakkında bilgilendirmek gibi yöntemlerle, Büyük Dil Modellerinin (BDM) sorumlu kullanımını teşvik eden Uygulama Programlama Arabirimler (API) ve kullanıcı arayüzleri tasarlayın. Kullanım alanındaki sınırlamaları da açık ve net bir şekilde belirtin.

#### 8. Eğitim ve Bilinçlendirme

  Kullanıcılara, Büyük Dil Modellerinin (BDM) sınırlamaları, üretilen içeriğin bağımsız olarak doğrulanmasının önemi ve eleştirel düşünmenin gerekliliği konularında kapsamlı eğitim sağlayın. Belirli bağlamlarda, kullanıcıların kendi uzmanlık alanlarında BDM çıktılarının doğruluğunu etkin bir şekilde değerlendirebilmeleri için alanına özel eğitimler sunun.

### Örnek Saldırı Senaryoları

#### Senaryo #1

  Saldırganlar, popüler kodlama asistanlarını kullanarak sıkça halüsinasyon sonucu önerilen paket adlarını tespit eder. Bu sıklıkla önerilen ancak gerçekte var olmayan kütüphaneleri belirledikten sonra, aynı adlarla kötü amaçlı paketleri yaygın kullanılan yazılım depolarına yüklerler. Geliştiriciler ise, kodlama asistanının önerilerine güvenerek bu zararlı paketleri farkında olmadan yazılımlarına entegre eder. Sonuç olarak, saldırganlar yetkisiz erişim elde edebilir, zararlı kod enjekte edebilir ya da arka kapılar oluşturarak ciddi güvenlik ihlallerine ve kullanıcı verilerinin tehlikeye girmesine yol açabilir.

#### Senaryo #2

  Bir şirket, yeterli doğruluk sağlamadan tıbbi teşhis amacıyla bir sohbet botu sunar. Sohbet botu hatalı bilgiler vererek hastalar için zararlı sonuçlara yol açar. Bunun sonucunda, şirket maddi tazminat ödemeye mahkum edilir. Bu durumda, güvenlik ve emniyet zafiyeti kötü niyetli bir saldırgana ihtiyaç duymadan, doğrudan Büyük Dil Modeli (BDM) sisteminin yetersiz denetimi ve güvenilirliğinden kaynaklanmıştır. Yani, bu senaryoda aktif bir saldırganın varlığı gerekmeden şirket ciddi itibar ve finansal kayıplarla karşı karşıya kalabilir.

### Referans Linkleri

1. [Sağlık Bilgi Kaynağı Olarak Yapay Zeka Sohbet Botları: Uzmanlık Yanıltması](https://www.kff.org/health-misinformation-monitor/volume-05/): **KFF**
2. [Air Canada Sohbet Botu Yanlış Bilgi Vakası: Seyahat Edenlerin Bilmesi Gerekenler](https://www.bbc.com/travel/article/20240222-air-canada-chatbot-misinformation-what-travellers-should-know): **BBC**
3. [ChatGPT Uydurma Dava Dosyaları: Üretken Yapay Zekâ Halüsinasyonları](https://www.legaldive.com/news/chatgpt-fake-legal-cases-generative-ai-hallucinations/651557/): **LegalDive**
4. [Büyük Dil Modellerinde Halüsinasyonları Anlamak](https://towardsdatascience.com/llm-hallucinations-ec831dcd7786): **Towards Data Science**
5. [Şirketler Büyük Dil Modellerinin Risklerini Kullanıcılara Nasıl Anlatmalı?](https://techpolicy.press/how-should-companies-communicate-the-risks-of-large-language-models-to-users/): **Techpolicy**
6. [Bir Haber Sitesi Makaleleri Yapay Zeka ile Yazdı: Gazetecilikte Felaket](https://www.washingtonpost.com/media/2023/01/17/cnet-ai-articles-journalism-corrections/): **Washington Post**
7. [Yapay Zeka Paket Halüsinasyonlarına Derinlemesine Bakış](https://www.lasso.security/blog/ai-package-hallucinations): **Lasso Security**
8. [ChatGPT Tarafından Oluşturulan Kod Ne Kadar Güvenli?](https://arxiv.org/abs/2304.09655): **Arvix**
9. [Büyük Dil Modellerinden Kaynaklı Halüsinasyonlar Nasıl Azaltılır?](https://thenewstack.io/how-to-reduce-the-hallucinations-from-large-language-models/): **The New Stack**
10. [Halüsinasyonları Azaltmaya Yönelik Pratik Adımlar](https://newsletter.victordibia.com/p/practical-steps-to-reduce-hallucination): **Victor Debia**
11. [Yapay Zeka Aracılığıyla Kurumsal Bilgiye Erişimin Sonuçlarını Keşfetme Çatısı](https://www.microsoft.com/en-us/research/publication/a-framework-for-exploring-the-consequences-of-ai-mediated-enterprise-knowledge-access-and-identifying-risks-to-workers/): **Microsoft**

### İlgili Çerçeveler ve Sınıflandırmalar

Altyapı dağıtımı, uygulama ortamı kontrolleri ve diğer en iyi uygulamalara ilişkin kapsamlı bilgi, senaryolar ve stratejiler için bu bölüme başvurun.

- [AML.T0048.002 - Toplumsal Zarar](https://atlas.mitre.org/techniques/AML.T0048) **MITRE ATLAS**
