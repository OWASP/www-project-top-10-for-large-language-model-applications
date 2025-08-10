## LLM06:2025 Aşırı Yetki

### Açıklama

BDM tabanlı sistem genellikle geliştiricisi tarafından bir dereceye kadar yetki verilir - bir isteme yanıt olarak eylemler gerçekleştirmek için uzantılar aracılığıyla (farklı satıcılar tarafından bazen araçlar, beceriler veya eklentiler olarak adlandırılır) fonksiyon çağırma veya diğer sistemlerle arayüz yapma yeteneği. Hangi uzantının çağrılacağına dair karar, girdi istemi veya BDM çıktısına dayalı olarak dinamik şekilde belirlemek için BDM 'ajanına' da devredilebilir. Ajan tabanlı sistemler tipik olarak sonraki çağrıları temellendirmek ve yönlendirmek için önceki çağrılardan çıktı kullanarak BDM'ye tekrarlanan çağrılar yapar.

Aşırı Yetki, BDM'nin arızalanmasına neyin sebep olduğuna bakılmaksızın, BDM'den beklenmeyen, belirsiz veya manipüle edilmiş çıktılara yanıt olarak zarar verici eylemlerin gerçekleştirilmesini sağlayan zafiyettir. Yaygın tetikleyiciler şunları içerir:

* zayıf tasarlanmış zararsız istemlerden kaynaklanan halüsinasyon/uydurma, veya sadece kötü performans gösteren model;
* kötü niyetli kullanıcıdan, kötü niyetli/tehlikeye girmiş uzantının önceki çağrısından, veya (çok ajanlı/işbirlikçi sistemlerde) kötü niyetli/tehlikeye girmiş eş ajandan doğrudan/dolaylı istem enjeksiyonu.

Aşırı Yetki'nin temel nedeni tipik olarak bunlardan bir veya birkaçıdır:

* aşırı işlevsellik;
* aşırı izinler;
* aşırı özerklik.

Aşırı Yetki, gizlilik, bütünlük ve erişilebilirlik spektrumunda geniş bir etki yelpazesine yol açabilir ve BDM tabanlı uygulamanın hangi sistemlerle etkileşim kurabileceğine bağlıdır.

Not: Aşırı Yetki, BDM çıktılarının yetersiz incelenmesiyle ilgili olan Güvensiz Çıktı İşleme'den farklıdır.

### Yaygın Risk Örnekleri

#### 1. Aşırı İşlevsellik

  BDM ajanı, sistemin amaçlanan işlemi için gerekli olmayan fonksiyonları içeren uzantılara erişime sahiptir. Örneğin, geliştirici BDM ajanına bir depodan belgeleri okuma yeteneği vermesi gerekir, ancak kullanmayı seçtiği 3. taraf uzantı ayrıca belgeleri değiştirme ve silme yeteneğini de içerir.

#### 2. Aşırı İşlevsellik

  Uzantı geliştirme aşamasında denenmiş ve daha iyi bir alternatif lehine bırakılmış olabilir, ancak orijinal eklenti BDM ajanı için hala kullanılabilir durumda kalır.

#### 3. Aşırı İşlevsellik

  Açık uçlu işlevselliğe sahip BDM eklentisi, uygulamanın amaçlanan işlemi için gereken komutların dışındaki komutlar için girdi talimatlarını düzgün filtrelemez. Örn., belirli bir kabuk komutunu çalıştırmak için uzantı, diğer kabuk komutlarının çalıştırılmasını düzgün şekilde engellemez.

#### 4. Aşırı İzinler

  BDM uzantısı, uygulamanın amaçlanan işlemi için gerekli olmayan aşağı akış sistemlerinde izinlere sahiptir. Örn., veri okumak için tasarlanan uzantı, yalnızca SELECT izinlerine sahip olmakla kalmayıp aynı zamanda UPDATE, INSERT ve DELETE izinlerine de sahip kimlik kullanarak veritabanı sunucusuna bağlanır.

#### 5. Aşırı İzinler

  Bireysel kullanıcı bağlamında işlemler gerçekleştirmek için tasarlanan BDM uzantısı, aşağı akış sistemlere genel yüksek ayrıcalıklı kimlikle erişir. Örn., mevcut kullanıcının belge deposunu okumak için uzantı, tüm kullanıcılara ait dosyalara erişimi olan ayrıcalıklı hesapla belge deposuna bağlanır.

#### 6. Aşırı Özerklik

  BDM tabanlı uygulama veya uzantı, yüksek etkili eylemleri bağımsız olarak doğrulamaz ve onaylamaz. Örn., kullanıcının belgelerinin silinmesine olanak tanıyan uzantı, kullanıcıdan herhangi bir onay almadan silme işlemlerini gerçekleştirir.

### Önleme ve Azaltma Stratejileri

Aşağıdaki eylemler Aşırı Yetki'yi önleyebilir:

#### 1. Uzantıları minimize etme

  BDM ajanlarının çağırmasına izin verilen uzantıları yalnızca gerekli minimum ile sınırlayın. Örneğin, BDM tabanlı sistem bir URL'nin içeriğini getirme yeteneğine ihtiyaç duymuyorsa, böyle bir uzantı BDM ajanına sunulmamalıdır.

#### 2. Uzantı işlevselliğini minimize etme

  BDM uzantılarında uygulanan fonksiyonları gerekli minimum ile sınırlayın. Örneğin, e-postaları özetlemek için kullanıcının posta kutusuna erişen uzantı yalnızca e-postaları okuma yeteneğine ihtiyaç duyabilir, bu nedenle uzantı mesaj silme veya gönderme gibi başka işlevsellik içermemelidir.

#### 3. Açık uçlu uzantılardan kaçınma

  Mümkün olduğunda açık uçlu uzantıların kullanımından kaçının (örn., kabuk komutu çalıştırma, URL getirme, vb.) ve daha ayrıntılı işlevselliğe sahip uzantıları kullanın. Örneğin, BDM tabanlı uygulama bir dosyaya bazı çıktılar yazması gerekebilir. Bu, kabuk fonksiyonu çalıştırmak için uzantı kullanılarak uygulanırsa, istenmeyen eylemler için kapsam çok büyüktür (herhangi bir başka kabuk komutu çalıştırılabilir). Daha güvenli alternatif, yalnızca o belirli işlevselliği uygulayan özel dosya yazma uzantısı oluşturmak olacaktır.

#### 4. Uzantı izinlerini minimize etme

  İstenmeyen eylemlerin kapsamını sınırlamak için BDM uzantılarına diğer sistemlerde verilen izinleri gerekli minimum ile sınırlayın. Örneğin, müşteriye satın alma önerileri yapmak için ürün veritabanı kullanan BDM ajanı yalnızca 'ürünler' tablosuna okuma erişimine ihtiyaç duyabilir; diğer tablolara erişimi olmamalı, kayıt ekleme, güncelleme veya silme yeteneği de bulunmamalıdır. Bu, BDM uzantısının veritabanına bağlanmak için kullandığı kimlik için uygun veritabanı izinleri uygulanarak zorlanmalıdır.

#### 5. Uzantıları kullanıcı bağlamında çalıştırma

  Kullanıcı adına alınan eylemlerin aşağı akış sistemlerde o belirli kullanıcının bağlamında ve gerekli minimum ayrıcalıklarla çalıştırıldığından emin olmak için kullanıcı yetkilendirme ve güvenlik kapsamını takip edin. Örneğin, kullanıcının kod deposunu okuyan BDM uzantısı, kullanıcının OAuth aracılığıyla ve gerekli minimum kapsamla kimlik doğrulaması yapmasını gerektirmelidir.

#### 6. Kullanıcı onayı gerektirme

  Yüksek etkili eylemler alınmadan önce insanın onaylamasını gerektirmek için döngüde insan kontrolü kullanın. Bu, aşağı akış sistemde (BDM uygulamasının kapsamı dışında) veya BDM uzantısının kendisinde uygulanabilir. Örneğin, kullanıcı adına sosyal medya içeriği oluşturan ve yayınlayan BDM tabanlı uygulama, 'yayınlama' işlemini uygulayan uzantı içinde kullanıcı onay rutini içermelidir.

#### 7. Tam aracılık

  Bir eylemin izinli olup olmadığına BDM'nin karar vermesine güvenmek yerine aşağı akış sistemlerde yetkilendirme uygulayın. Uzantılar aracılığıyla aşağı akış sistemlere yapılan tüm isteklerin güvenlik politikalarına karşı doğrulanması için tam aracılık ilkesini zorunlu kılın.

#### 8. BDM girdi ve çıktılarını temizleme

  Özellikle girdi temizlemeye güçlü odaklanarak ASVS'de (Uygulama Güvenliği Doğrulama Standardı) OWASP'ın önerilerini uygulamak gibi güvenli kodlama en iyi uygulamalarını takip edin. Geliştirme hatlarında Statik Uygulama Güvenlik Testi (SAST) ve Dinamik ve Etkileşimli uygulama testini (DAST, IAST) kullanın.

Aşağıdaki seçenekler Aşırı Yetki'yi önlemez, ancak neden olunan hasar seviyesini sınırlayabilir:

* İstenmeyen eylemlerin nerede gerçekleştiğini tanımlamak ve buna göre yanıt vermek için BDM uzantıları ve aşağı akış sistemlerinin etkinliğini günlüğe kaydedin ve izleyin.
* Belirli bir zaman periyodunda gerçekleştirilebilecek istenmeyen eylem sayısını azaltmak için hız sınırlama uygulayın, önemli hasar oluşmadan önce izleme yoluyla istenmeyen eylemleri keşfetme fırsatını artırın.

### Örnek Saldırı Senaryoları

BDM tabanlı kişisel asistan uygulaması, gelen e-postaların içeriğini özetlemek için uzantı aracılığıyla bireyin posta kutusuna erişim verilir. Bu işlevselliği başarmak için uzantının mesajları okuma yeteneğine ihtiyacı vardır, ancak sistem geliştiricisinin kullanmayı seçtiği eklenti ayrıca mesaj gönderme fonksiyonları da içerir. Ek olarak, uygulama kötü niyetli hazırlanmış gelen e-postanın BDM'yi ajanı kullanıcının gelen kutusunu hassas bilgiler için taramaya ve saldırganın e-posta adresine iletmeye komut etmeye kandırdığı dolaylı istem enjeksiyonu saldırısına karşı savunmasızdır. Bu şu yollarla önlenebilir:

* yalnızca posta okuma yeteneklerini uygulayan uzantı kullanarak aşırı işlevselliği ortadan kaldırmak,
* kullanıcının e-posta servisine salt okunur kapsamlı OAuth oturumu aracılığıyla kimlik doğrulaması yaparak aşırı izinleri ortadan kaldırmak, ve/veya
* BDM uzantısı tarafından hazırlanan her postada kullanıcının manuel olarak gözden geçirmesini ve 'gönder'e basmasını gerektirerek aşırı özerkliği ortadan kaldırmak.

Alternatif olarak, posta gönderme arayüzünde hız sınırlama uygulayarak neden olunan hasar azaltılabilir.

### Referanslar

1. [Slack AI data exfil from private channels](https://promptarmor.substack.com/p/slack-ai-data-exfiltration-from-private): **PromptArmor**
2. [Rogue Agents: Stop AI From Misusing Your APIs](https://www.twilio.com/en-us/blog/rogue-ai-agents-secure-your-apis): **Twilio**
3. [Embrace the Red: Confused Deputy Problem](https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./): **Embrace The Red**
4. [NeMo-Guardrails: Interface guidelines](https://github.com/NVIDIA/NeMo-Guardrails/blob/main/docs/security/guidelines.md): **NVIDIA Github**
5. [Simon Willison: Dual LLM Pattern](https://simonwillison.net/2023/Apr/25/dual-llm-pattern/): **Simon Willison**
6. [Sandboxing Agentic AI Workflows with WebAssembly](https://developer.nvidia.com/blog/sandboxing-agentic-ai-workflows-with-webassembly/) **NVIDIA, Joe Lucas**
