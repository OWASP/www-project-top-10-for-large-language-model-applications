## LLM04: Veri ve Model Zehirlenmesi

### Açıklama

Veri zehirlenmesi, ön eğitim, ince ayar veya gömme verilerinin güvenlik açıkları, arka kapılar veya önyargılar oluşturmak için manipüle edilmesi durumunda meydana gelir. Bu manipülasyon, model güvenliğini, performansını veya etik davranışını tehlikeye atarak zararlı çıktılara veya bozulmuş yeteneklere yol açabilir. Yaygın riskler arasında düşürülmüş model performansı, önyargılı veya toksik içerik ve alt sistemlerin istismar edilmesi yer alır.

Veri zehirlenmesi, BDM yaşam döngüsünün farklı aşamalarını hedef alabilir; bunlar arasında ön eğitim (genel verilerden öğrenme), ince ayar (modelleri belirli görevlere uyarlama), gömme (metni sayısal vektörlere dönüştürme) ve transfer öğrenme (önceden eğitilmiş bir modeli yeni bir görevde yeniden kullanma) yer alır. Bu aşamaları anlamak, güvenlik açıklarının nereden kaynaklanabileceğini belirlemeye yardımcı olur. Veri zehirlenmesi, eğitim verilerini manipüle etmek modelin doğru tahminler yapma yetisini etkilediği için bir bütünlük saldırısı olarak kabul edilir. Özellikle doğrulanmamış veya kötü niyetli içerik bulundurabilen harici veri kaynakları ile riskler yüksektir.

Ayrıca, paylaşılan depolar veya açık kaynak platformlar aracılığıyla dağıtılan modeller, veri zehirlenmesinin ötesinde, model yüklendiğinde zararlı kod çalıştırabilen kötü niyetli pickling gibi tekniklerle gömülü kötü amaçlı yazılımlar gibi riskler taşıyabilir. Ayrıca, zehirlemenin bir arka kapının uygulanmasına izin verebileceğini göz önünde bulundurun. Bu tür arka kapılar, belirli bir tetikleyici davranışını değiştirmesine neden olana kadar modelin davranışını değiştirilmemiş olarak bırakabilir. Bu arka kapılar, bu tür değişiklikleri test etmeyi ve tespit etmeyi zorlaştırabilir ve aslında bir modelin uyuyan bir ajan haline gelmesine sebep olabilir.

### Yaygın Güvenlik Açığı Örnekleri

1. Kötü niyetli aktörler eğitim sırasında zararlı veriler ekleyerek önyargılı çıktılara yol açar. "Split-View Data Poisoning" veya "Frontrunning Poisoning" gibi teknikler, bunu başarmak için model eğitimi dinamiklerini istismar eder.
  (Ref. link: [Split-View Data Poisoning](https://github.com/GangGreenTemperTatum/speaking/blob/main/dc604/hacker-summer-camp-23/Ads%20_%20Poisoning%20Web%20Training%20Datasets%20_%20Flow%20Diagram%20-%20Exploit%201%20Split-View%20Data%20Poisoning.jpeg))
  (Ref. link: [Frontrunning Poisoning](https://github.com/GangGreenTemperTatum/speaking/blob/main/dc604/hacker-summer-camp-23/Ads%20_%20Poisoning%20Web%20Training%20Datasets%20_%20Flow%20Diagram%20-%20Exploit%202%20Frontrunning%20Data%20Poisoning.jpeg))
2. Saldırganlar, zararlı içeriği doğrudan eğitim sürecine yerleştirerek modelin çıktı kalitesini tehlikeye atabilir.
3. Kullanıcılar, etkileşimler sırasında farkında olmadan hassas veya özel bilgileri yerleştirir ve bu bilgiler sonraki çıktılarda açığa çıkabilir.
4. Doğrulanmamış eğitim verileri, önyargılı veya hatalı çıktı riskini artırır.
5. Kaynak erişim kısıtlamalarının olmaması, güvenli olmayan verilerin alınmasına izin vererek önyargılı çıktılarla sonuçlanabilir.

### Önleme ve Azaltma Stratejileri

1. OWASP CycloneDX veya ML-BOM gibi araçları kullanarak veri kaynaklarını ve dönüşümlerini takip edin ve üçüncü taraf yazılımların dinamik analizini gerçekleştirmek için [Dyana](https://github.com/dreadnode/dyana) gibi araçlardan yararlanın. Model geliştirme aşamalarının tamamında veri meşruiyetini doğrulayın.
2. Veri tedarikçilerini titizlikle inceleyin ve zehirlenme belirtilerini tespit etmek için model çıktılarını güvenilir kaynaklara karşı doğrulayın.
3. Modelin doğrulanmamış veri kaynaklarına maruziyetini sınırlamak için katı yalıtılmış ortam uygulayın. Düşmanca verileri filtrelemek için aykırılık tespit tekniklerini kullanın. 
4. İnce ayar için belirli veri kümeleri kullanarak modelleri farklı kullanım durumlarına göre uyarlayın. Bu, tanımlanmış hedeflere dayalı olarak daha doğru çıktılar üretmeye yardımcı olur.
5. Modelin istenmeyen veri kaynaklarına erişimini önlemek için yeterli altyapı kontrollerini sağlayın.
6. Veri kümelerindeki değişiklikleri takip etmek ve kötüye kullanmayı tespit etmek için veri sürüm kontrolü (DVC) kullanın. Sürümleme, model bütünlüğünü korumak için çok önemlidir. 
7. Kullanıcı tarafından sağlanan bilgileri vektör veritabanında saklayın, bu da tüm modeli yeniden eğitmeden düzeltmeler yapılmasına olanak tanır.
 reduce risks of hallucinations.
8. Veri sarsımlarının etkisini en aza indirmek için kırmızı takım kampanyaları ve birleşik öğrenme gibi düşmanca tekniklerle model sağlamlığını test edin.
9. Eğitim kaybını izleyin ve zehirlenme belirtileri için model davranışını analiz edin. Aykırı çıktıları tespit etmek için eşik değerleri kullanın.
10. Çıkarım sırasında, halüsinasyon risklerini azaltmak için geri almayla artırılmış üretim (RAG) ve temellendirme tekniklerini dahil edin.

### Örnek Atak Senaryoları

#### Senaryo #1

  Bir saldırgan, eğitim verilerini değiştirerel veya istem yerleştirme tekniklerini kullanarak modelin çıktılarını önyargılı hale getirir ve yanlış bilgi yayar.

#### Senaryo #2

  Uygun filtreleme olmadan toksik veriler, zararlı veya önyargılı çıktılara yol açarak tehlikeli bilgilerin yayılmasına neden olabilir.  

#### Senaryo #3

  Kötü niyetli bir aktör veya rakip, eğitim için sahte belgeler oluşturur ve bu da yanlışlıkları yansıtan model çıktılarıyla sonuçlanır.

#### Senaryo #4

  Yetersiz filtreleme, bir saldırganın istem yerleştirme yoluyla yanıltıcı veri eklemesine izin vererek güvenliği ihlal edilmiş çıktılara yol açar.

#### Senaryo #5

  Bir saldırgan, modele arka kapı tetikleyicisi eklemek için zehirleme tekniklerini kullanır. Bu, kimlik doğrulama atlatma, veri sızdırma veya gizli komut yürütme saldılarına sizi açık bırakabilir.

### Referans Linkler

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

### İlgili Çerçeveler ve Taksonomiler

Refer to this section for comprehensive information, scenarios strategies relating to infrastructure deployment, applied environment controls and other best practices.

- [AML.T0018 | Backdoor ML Model](https://atlas.mitre.org/techniques/AML.T0018) **MITRE ATLAS**
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework): Strategies for ensuring AI integrity. **NIST**
- [ML07:2023 Transfer Learning Attack](https://owasp.org/www-project-machine-learning-security-top-10/docs/ML07_2023-Transfer_Learning_Attack) **OWASP Machine Learning Security Top Ten**
