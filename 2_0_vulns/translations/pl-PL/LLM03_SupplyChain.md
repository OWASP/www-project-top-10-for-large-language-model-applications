**LLM03:2025 Łańcuch dostaw**

**Opis**

Łańcuchy dostaw LLM są podatne na różne zagrożenia, które mogą wpływać
na integralność danych szkoleniowych, modeli i platform wdrożeniowych.
Zagrożenia te mogą skutkować stronniczymi wynikami, naruszeniami
bezpieczeństwa lub awariami systemu. Podczas gdy tradycyjne luki w
zabezpieczeniach oprogramowania koncentrują się na takich kwestiach, jak
błędy w kodzie i zależności, w przypadku ML ryzyko obejmuje również
wstępnie przeszkolone modele i dane stron trzecich.

Te elementy zewnętrzne mogą być manipulowane poprzez ataki typu
tampering lub poisoning.

Tworzenie modeli LLM jest zadaniem specjalistycznym, które często zależy
od modeli stron trzecich. Pojawienie się modeli LLM o otwartym dostępie
oraz nowych metod dostrajania, takich jak „LoRA" (Low-Rank Adaptation) i
„PEFT" (Parameter-Efficient Fine-Tuning), zwłaszcza na platformach
takich jak Hugging Face, wprowadza nowe zagrożenia dla łańcucha dostaw.
Wreszcie pojawienie się modeli LLM na urządzeniach zwiększa powierzchnię
ataku i ryzyko związane z łańcuchem dostaw dla aplikacji LLM.

Niektóre z omówionych tutaj zagrożeń zostały również omówione w „LLM04
Data and Model Poisoning". Niniejszy wpis koncentruje się na aspekcie
ryzyka związanym z łańcuchem dostaw. Prosty model zagrożeń można znaleźć
[[tutaj]{.underline}](https://github.com/jsotiro/ThreatModels/blob/main/LLM%20Threats-LLM%20Supply%20Chain.png).

**Typowe przykłady zagrożeń**

**1. Tradycyjne luki w zabezpieczeniach pakietów stron trzecich**

Takie jak przestarzałe lub wycofane komponenty, które atakujący mogą
wykorzystać do naruszenia bezpieczeństwa aplikacji LLM. Jest to podobne
do „A06:2021 -- Podatne na ataki i przestarzałe komponenty", z większym
ryzykiem w przypadku wykorzystania komponentów podczas opracowywania lub
dostosowywania modelu. (Link referencyjny: [[A06:2021 -- Podatne na
ataki i przestarzałe
komponenty]{.underline}](https://owasp.org/Top10/A06_2021-Vulnerable_and_Outdated_Components/))

**2. Ryzyko związane z licencjonowaniem**

Tworzenie sztucznej inteligencji często wiąże się z różnorodnymi
licencjami na oprogramowanie i zbiory danych, co stwarza ryzyko, jeśli
nie są one odpowiednio zarządzane. Różne licencje open source i licencje
własnościowe nakładają różne wymagania prawne. Licencje na zbiory danych
mogą ograniczać użytkowanie, dystrybucję lub komercjalizację.

**3. Przestarzałe lub wycofane modele**

Korzystanie z przestarzałych lub wycofanych modeli, które nie są już
utrzymywane, prowadzi do problemów z bezpieczeństwem.

**4. Podatny na ataki wstępnie wyszkolony model**

Modele są binarnymi czarnymi skrzynkami i w przeciwieństwie do
oprogramowania open source, statyczna kontrola nie zapewnia
wystarczających gwarancji bezpieczeństwa. Podatne na ataki wstępnie
wyszkolone modele mogą zawierać ukryte błędy, tylne furtki lub inne
złośliwe funkcje, które nie zostały zidentyfikowane podczas oceny
bezpieczeństwa repozytorium modeli. Podatne na ataki modele mogą być
tworzone zarówno przez zanieczyszczone zbiory danych, jak i bezpośrednią
manipulację modelami przy użyciu technik takich jak ROME, znanych
również jako lobotomizacja.

**5. Słabe pochodzenie modeli**

Obecnie nie ma silnych gwarancji pochodzenia opublikowanych modeli.
Karty modeli i powiązana dokumentacja zawierają informacje o modelu i
zaufanych użytkownikach, ale nie dają żadnych gwarancji co do
pochodzenia modelu. Atakujący może przejąć konto dostawcy w repozytorium
modeli lub utworzyć podobne konto i połączyć je z technikami inżynierii
społecznej, aby przejąć łańcuch dostaw aplikacji LLM.

**6. Podatne na ataki adaptery LoRA**

LoRA to popularna technika dostrajania, która zwiększa modułowość,
umożliwiając dołączenie wstępnie wytrenowanych warstw do istniejącego
LLM. Metoda ta zwiększa wydajność, ale stwarza nowe zagrożenia, w
których złośliwy adapter LoRA narusza integralność i bezpieczeństwo
wstępnie wytrenowanego modelu bazowego. Może to mieć miejsce zarówno w
środowiskach współpracy nad łączeniem modeli, jak i poprzez
wykorzystanie obsługi LoRA przez popularne platformy wdrażania
wnioskowania, takie jak vLMM i OpenLLM, gdzie adaptery można pobrać i
zastosować do wdrożonego modelu.

**7. Wykorzystanie procesów współpracy nad rozwojem**

Współpraca przy łączeniu modeli i usługi związane z obsługą modeli (np.
konwersje) hostowane w środowiskach współdzielonych mogą zostać
wykorzystane do wprowadzenia luk w zabezpieczeniach modeli
współdzielonych. Łączenie modeli jest bardzo popularne w Hugging Face, a
modele połączone zajmują czołowe miejsca w rankingu OpenLLM i mogą
zostać wykorzystane do ominięcia przeglądów. Podobnie usługi takie jak
boty konwersacyjne okazały się podatne na manipulacje i wprowadzanie
złośliwego kodu do modeli.

**8. Luki w łańcuchu dostaw modeli LLM na urządzeniach**

Modele LLM na urządzeniach zwiększają powierzchnię ataku na dostawy
poprzez naruszenie procesów produkcyjnych i wykorzystanie luk w
zabezpieczeniach systemu operacyjnego lub oprogramowania sprzętowego
urządzenia w celu naruszenia modeli. Atakujący mogą przeprowadzić
inżynierię odwrotną i przepakować aplikacje z fałszywymi modelami.

**9. Niejasne warunki użytkowania i polityka prywatności danych**

Niejasne warunki użytkowania i polityka prywatności operatorów modeli
prowadzą do wykorzystania wrażliwych danych aplikacji do szkolenia
modeli, a następnie do ujawnienia wrażliwych informacji. Może to również
dotyczyć ryzyka związanego z wykorzystaniem materiałów chronionych
prawem autorskim przez dostawcę modelu.

**Strategie zapobiegania i ograniczania ryzyka**

Dokładnie sprawdzaj źródła danych i dostawców, w tym warunki użytkowania
i politykę prywatności, korzystając wyłącznie z usług zaufanych
dostawców. Regularnie przeglądaj i kontroluj bezpieczeństwo i dostęp
dostawców, upewniając się, że nie nastąpiły żadne zmiany w ich polityce
bezpieczeństwa lub warunkach użytkowania.

Zrozum i stosuj środki ograniczające ryzyko opisane w OWASP Top Ten
„A06:2021 -- Podatne na ataki i przestarzałe komponenty". Obejmują one
skanowanie podatności, zarządzanie nimi i instalowanie poprawek. W
środowiskach programistycznych z dostępem do wrażliwych danych należy
również stosować te środki kontroli. (Link: [[A06:2021 -- Podatne na
ataki i przestarzałe
komponenty]{.underline}](https://owasp.org/Top10/A06_2021-Vulnerable_and_Outdated_Components/))

Podczas wybierania modelu strony trzeciej należy zastosować kompleksowe
testy AI Red Teaming i oceny. Decoding Trust jest przykładem punktu
odniesienia dla zaufanej sztucznej inteligencji dla modeli LLM, ale
modele można dostosować tak, aby ominąć opublikowane punkty odniesienia.
Należy wykorzystać szeroko zakrojone testy AI Red Teaming do oceny
modelu, zwłaszcza w przypadkach, w których planuje się jego
wykorzystanie.

Należy utrzymywać aktualny wykaz komponentów za pomocą wykazu
komponentów oprogramowania (SBOM), aby zapewnić aktualny, dokładny i
podpisany wykaz, zapobiegając manipulowaniu wdrożonymi pakietami. Wykazy
SBOM mogą służyć do szybkiego wykrywania i ostrzegania o nowych,
nieznanych dotąd lukach w zabezpieczeniach. Wykazy AI BOM i ML SBOM to
nowa dziedzina i należy ocenić dostępne opcje, zaczynając od OWASP
CycloneDX.

Aby ograniczyć ryzyko związane z licencjonowaniem sztucznej
inteligencji, należy stworzyć wykaz wszystkich rodzajów licencji przy
użyciu BOM i przeprowadzać regularne audyty całego oprogramowania,
narzędzi i zbiorów danych, zapewniając zgodność i przejrzystość dzięki
BOM. Należy korzystać z narzędzi do automatycznego zarządzania
licencjami w celu monitorowania w czasie rzeczywistym i szkolić zespoły
w zakresie modeli licencjonowania. Należy przechowywać szczegółową
dokumentację licencyjną w BOM i korzystać z narzędzi takich jak
[[Dyana]{.underline}](https://github.com/dreadnode/dyana) do
przeprowadzania dynamicznej analizy oprogramowania stron trzecich.

Należy korzystać wyłącznie z modeli pochodzących z weryfikowalnych
źródeł i stosować zewnętrzne kontrole integralności modeli z podpisami i
skrótami plików, aby zrekompensować brak silnego pochodzenia modelu.
Podobnie należy stosować podpisywanie kodu w przypadku kodu
dostarczonego z zewnątrz.

Należy wdrożyć rygorystyczne praktyki monitorowania i audytu w
środowiskach współpracy nad rozwojem modeli, aby zapobiegać nadużyciom i
szybko je wykrywać. Przykładem automatycznych skryptów, które można
wykorzystać, jest „HuggingFace SF_Convertbot Scanner". (Link
referencyjny: [[HuggingFace SF_Convertbot
Scanner]{.underline}](https://gist.github.com/rossja/d84a93e5c6b8dd2d4a538aa010b29163))

Wykrywanie anomalii i testy odporności na ataki na dostarczone modele i
dane mogą pomóc w wykryciu manipulacji i zatrucia, jak omówiono w „LLM04
Zatruwanie danych i modelu"; idealnie powinno to być częścią MLOps i
potoków LLM; są to jednak techniki nowo powstające i mogą być łatwiejsze
do wdrożenia w ramach ćwiczeń red teamingu.

Wdrożyć politykę łatania w celu ograniczenia podatnych na ataki lub
przestarzałych komponentów. Upewnić się, że aplikacja opiera się na
aktualizowanej wersji interfejsów API i modelu bazowego.

Szyfrować modele wdrożone na obrzeżach AI za pomocą kontroli
integralności i korzystać z interfejsów API poświadczających dostawców,
aby zapobiec manipulowaniu aplikacjami i modelami oraz zakończyć
działanie aplikacji z nieznanym oprogramowaniem układowym.

**Przykładowe scenariusze ataków**

**Scenariusz nr 1: Podatna na ataki biblioteka Python**

Atakujący wykorzystuje podatną na ataki bibliotekę Python, aby przejąć
kontrolę nad aplikacją LLM. Miało to miejsce podczas pierwszego
naruszenia bezpieczeństwa danych Open AI. Ataki na rejestr pakietów PyPi
skłoniły twórców modeli do pobrania zainfekowanej zależności PyTorch
zawierającej złośliwe oprogramowanie do środowiska tworzenia modeli.
Bardziej zaawansowanym przykładem tego typu ataku jest atak Shadow Ray
na framework Ray AI używany przez wielu dostawców do zarządzania
infrastrukturą AI. Uważa się, że w tym ataku wykorzystano pięć luk w
zabezpieczeniach, które wpłynęły na wiele serwerów.

**Scenariusz nr 2: Bezpośrednia manipulacja**

Bezpośrednia manipulacja i publikacja modelu w celu rozpowszechniania
fałszywych informacji. Jest to rzeczywisty atak, w którym PoisonGPT
omija zabezpieczenia Hugging Face poprzez bezpośrednią zmianę parametrów
modelu.

**Scenariusz nr 3: Dostosowywanie popularnego modelu**

Atakujący dostosowuje popularny model o otwartym dostępie, aby usunąć
kluczowe funkcje bezpieczeństwa i uzyskać wysoką wydajność w określonej
dziedzinie (ubezpieczenia). Model jest dostosowany tak, aby uzyskać
wysokie wyniki w testach bezpieczeństwa, ale ma bardzo ukierunkowane
wyzwalacze. Atakujący wdraża go w Hugging Face, aby ofiary mogły z niego
korzystać, wykorzystując ich zaufanie do zapewnień dotyczących testów
porównawczych.

**Scenariusz nr 4: Wstępnie przeszkolone modele**

System LLM wdraża wstępnie wyszkolone modele z powszechnie używanego
repozytorium bez dokładnej weryfikacji. Skompromitowany model wprowadza
złośliwy kod, powodując stronnicze wyniki w niektórych kontekstach i
prowadząc do szkodliwych lub zmanipulowanych wyników.

**Scenariusz nr 5: Skompromitowany dostawca zewnętrzny**

Skompromitowany dostawca zewnętrzny dostarcza podatny na ataki adapter
LoRA, który jest łączony z LLM za pomocą funkcji łączenia modeli w
Hugging Face.

**Scenariusz nr 6: Infiltracja dostawcy**

Atakujący infiltruje dostawcę zewnętrznego i kompromituje produkcję
adaptera LoRA (Low-Rank Adaptation) przeznaczonego do integracji z LLM
wbudowanym w urządzenie, wdrożonym przy użyciu platform programistyczne
takich jak vLLM lub OpenLLM. Skompromitowany adapter LoRA jest subtelnie
modyfikowany w celu dodania ukrytych luk i złośliwego kodu. Po
połączeniu tego adaptera z LLM atakujący zyskuje ukryty punkt dostępu do
systemu. Złośliwy kod może zostać aktywowany podczas działania modelu,
umożliwiając atakującemu manipulowanie wynikami LLM.

**Scenariusz nr 7: Ataki typu: CloudBorne I CloudJacking**

Ataki te są skierowane przeciwko infrastrukturze chmury i wykorzystują
wspólne zasoby oraz luki w zabezpieczeniach warstw wirtualizacji. Atak
typu CloudBourne polega na wykorzystaniu luk w zabezpieczeniach
oprogramowania układowego we wspólnych środowiskach chmury, co prowadzi
do przejęcia kontroli nad fizycznymi serwerami hostującymi instancje
wirtualne. Atak typu CloudJacking odnosi się do złośliwej kontroli lub
niewłaściwego wykorzystania instancji chmury, co może prowadzić do
nieautoryzowanego dostępu do krytycznych platform wdrożeniowych LLM. Oba
ataki stanowią poważne zagrożenie dla łańcuchów dostaw opartych na
modelach ML w chmurze, ponieważ naruszone środowiska mogą ujawnić poufne
dane lub ułatwić dalsze ataki.

**Scenariusz nr 8: LeftOvers (CVE-2023-4969)**

LeftOvers wykorzystuje wyciek pamięci lokalnej procesora graficznego w
celu odzyskania poufnych danych. Atakujący może wykorzystać ten atak do
wycieku poufnych danych z serwerów produkcyjnych i stacji roboczych lub
laptopów programistów.

**Scenariusz nr 9: WizardLM**

Po usunięciu WizardLM atakujący wykorzystuje zainteresowanie tym modelem
i publikuje fałszywą wersję modelu o tej samej nazwie, ale zawierającą
złośliwe oprogramowanie i backdoory.

**Scenariusz nr 10: Usługa łączenia modeli/konwersji formatów**

Atakujący przeprowadza atak za pomocą usługi łączenia modeli lub
konwersji formatów w celu przejęcia publicznie dostępnego modelu dostępu
i wstrzyknięcia złośliwego oprogramowania. Jest to rzeczywisty atak
opublikowany przez dostawcę HiddenLayer.

**Scenariusz nr 11: Inżynieria odwrotna aplikacji mobilnej**

Atakujący przeprowadza inżynierię odwrotną aplikacji mobilnej, aby
zastąpić model sfałszowaną wersją, która prowadzi użytkowników do stron
oszukańczych. Użytkownicy są zachęcani do pobrania aplikacji
bezpośrednio za pomocą technik inżynierii społecznej. Jest to „prawdziwy
atak na predykcyjną sztuczną inteligencję", który dotknął 116 aplikacji
Google Play, w tym popularne aplikacje związane z bezpieczeństwem i
ochroną, używane do rozpoznawania gotówki, kontroli rodzicielskiej,
uwierzytelniania twarzy i usług finansowych. (Link referencyjny:
[[prawdziwy atak na predykcyjną sztuczną
inteligencję]{.underline}](https://arxiv.org/abs/2006.08131))

**Scenariusz nr 12: Zatrucie zbioru danych**

Atakujący zatruwa publicznie dostępne zbiory danych, aby pomóc w
stworzeniu tylnych drzwi podczas dostosowywania modeli. Tylne drzwi
subtelnie faworyzują określone firmy na różnych rynkach.

**Scenariusz nr 13: Warunki użytkowania i polityka prywatności**

Operator LLM zmienia warunki użytkowania i politykę prywatności,
wymagając wyraźnej rezygnacji z wykorzystania danych aplikacji do
szkolenia modeli, co prowadzi do zapamiętania danych wrażliwych.

**Linki referencyjne**

1.  [[PoisonGPT: Jak ukryliśmy lobotomizowany LLM w Hugging Face, aby
    rozpowszechniać fałszywe
    wiadomości]{.underline}](https://blog.mithrilsecurity.io/poisongpt-how-we-hid-a-lobotomized-llm-on-hugging-face-to-spread-fake-news)

2.  [[Duże modele językowe na urządzeniach z MediaPipe i TensorFlow
    Lite]{.underline}](https://developers.googleblog.com/en/large-language-models-on-device-with-mediapipe-and-tensorflow-lite/)

3.  [[Przejęcie konwersji Safetensors w Hugging
    Face]{.underline}](https://hiddenlayer.com/research/silent-sabotage/)

4.  [[Naruszenie bezpieczeństwa łańcucha dostaw
    ML]{.underline}](https://atlas.mitre.org/techniques/AML.T0010)

5.  [[Korzystanie z adapterów LoRA z
    vLLM]{.underline}](https://docs.vllm.ai/en/latest/models/lora.html)

6.  [[Usuwanie zabezpieczeń RLHF w GPT-4 poprzez
    dostrajanie]{.underline}](https://arxiv.org/pdf/2311.05553)

7.  [[Łączenie modeli za pomocą
    PEFT]{.underline}](https://huggingface.co/blog/peft_merging)

8.  [[Skaner HuggingFace
    SF_Convertbot]{.underline}](https://gist.github.com/rossja/d84a93e5c6b8dd2d4a538aa010b29163)

9.  [[Tysiące serwerów zhakowanych z powodu niebezpiecznego wdrożenia
    frameworka Ray
    AI]{.underline}](https://www.csoonline.com/article/2075540/thousands-of-servers-hacked-due-to-insecurely-deployed-ray-ai-framework.html)

10. [[LeftoverLocals: Podsłuchiwanie odpowiedzi LLM poprzez wyciek
    pamięci lokalnej
    GPU]{.underline}](https://blog.trailofbits.com/2024/01/16/leftoverlocals-listening-to-llm-responses-through-leaked-gpu-local-memory/)

**Powiązane frameworki i taksonomie**

W tej sekcji znajdą Państwo wyczerpujące informacje, scenariusze i
strategie dotyczące wdrażania infrastruktury, stosowanych środków
kontroli środowiska oraz innych najlepszych praktyk.

[[Naruszenie bezpieczeństwa łańcucha dostaw
ML]{.underline}](https://atlas.mitre.org/techniques/AML.T0010) ---
**MITRE ATLAS**
