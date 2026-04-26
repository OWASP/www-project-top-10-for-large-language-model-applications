**LLM10:2025 Nieograniczona konsumpcja**

**Opis**

Nieograniczona konsumpcja odnosi się do procesu, w którym duży model
językowy (LLM) generuje wyniki na podstawie zapytań lub poleceń
wejściowych. Wnioskowanie jest kluczową funkcją modeli LLM, polegającą
na zastosowaniu wyuczonych wzorców i wiedzy w celu wygenerowania
odpowiednich odpowiedzi lub prognoz.

Ataki mające na celu zakłócenie działania usług, wyczerpanie zasobów
finansowych celu, a nawet kradzież własności intelektualnej poprzez
klonowanie zachowania modelu, aby odnieść sukces, opierają się na
wspólnej klasie luk w zabezpieczeniach. Nieograniczone zużycie
występuje, gdy aplikacja oparta na dużym modelu językowym (LLM) pozwala
użytkownikom na przeprowadzanie nadmiernych i niekontrolowanych
wnioskowań, co prowadzi do takich zagrożeń, jak odmowa usługi (DoS),
straty ekonomiczne, kradzież modelu i pogorszenie jakości usług. Wysokie
wymagania obliczeniowe modeli LLM, zwłaszcza w środowiskach chmurowych,
sprawiają, że są one podatne na wykorzystywanie zasobów i nieuprawnione
użycie.

**Typowe przykłady podatności**

**1. Zalanie danymi wejściowymi o zmiennej długości**

Atakujący mogą przeciążyć model LLM licznymi danymi wejściowymi o różnej
długości, wykorzystując nieefektywność przetwarzania. Może to wyczerpać
zasoby i potencjalnie spowodować brak reakcji systemu, co znacząco
wpłynie na dostępność usług.

**2. Odmowa dostępu do portfela (DoW)**

Inicjując dużą liczbę operacji, atakujący wykorzystują model kosztu za
użycie usług AI w chmurze, co prowadzi do niemożliwych do udźwignięcia
obciążeń finansowych dla dostawcy i ryzyko ruiny finansowej.

**3. Ciągłe przepełnienie danych wejściowych**

Ciągłe wysyłanie danych wejściowych, które przekraczają okno kontekstowe
LLM, może prowadzić do nadmiernego wykorzystania zasobów obliczeniowych,
co skutkuje pogorszeniem jakości usług i zakłóceniami w działaniu.

**4. Zapytania wymagające dużych zasobów**

Przesyłanie niezwykle wymagających zapytań zawierających złożone
sekwencje lub skomplikowane wzorce językowe może wyczerpać zasoby
systemowe, prowadząc do wydłużenia czasu przetwarzania i potencjalnych
awarii systemu.

**5. Wyodrębnianie modelu za pośrednictwem API**

Atakujący mogą wysyłać zapytania do API modelu przy użyciu starannie
przygotowanych danych wejściowych i technik wstrzykiwania poleceń, aby
zebrać wystarczającą ilość danych wyjściowych do replikacji częściowego
modelu lub utworzenia modelu cieniowego. Stanowi to nie tylko ryzyko
kradzieży własności intelektualnej, ale także podważa integralność
oryginalnego modelu.

**6. Replikacja modelu funkcjonalnego**

Wykorzystanie modelu docelowego do generowania syntetycznych danych
szkoleniowych może umożliwić atakującym dostrojenie innego modelu
podstawowego, tworząc jego funkcjonalny odpowiednik. Pozwala to ominąć
tradycyjne metody ekstrakcji oparte na zapytaniach, stwarzając poważne
zagrożenie dla zastrzeżonych modeli i technologii.

**7. Ataki kanałem bocznym**

Złośliwi atakujący mogą wykorzystać techniki filtrowania danych
wejściowych LLM do przeprowadzenia ataków kanałem bocznym, zbierając
wagi modelu i informacje o jego architekturze. Może to zagrozić
bezpieczeństwu modelu i prowadzić do dalszego wykorzystania.

**Strategie zapobiegania i ograniczania skutków**

**1. Walidacja danych wejściowych**

Wprowadź ścisłą walidację danych wejściowych, aby zapewnić, że nie
przekraczają one rozsądnych limitów rozmiaru.

**2. Ogranicz ekspozycję logitów i logprobs**

Ogranicz lub zaciemnij ekspozycję logit_bias i logprobs w odpowiedziach
API. Podawaj tylko niezbędne informacje, nie ujawniając szczegółowych
prawdopodobieństw.

**3. Ograniczanie szybkości**

Zastosuj ograniczenie szybkości i limity użytkowników, aby ograniczyć
liczbę żądań, które pojedynczy podmiot źródłowy może wysłać w danym
okresie czasu.

**4. Zarządzanie alokacją zasobów**

Monitoruj i zarządzaj alokacją zasobów w sposób dynamiczny, aby zapobiec
nadmiernemu zużyciu zasobów przez pojedynczego użytkownika lub żądanie.

**5. Limity czasu i ograniczanie przepustowości**

Ustaw limity czasu i ogranicz przepustowość operacji wymagających dużej
ilości zasobów, aby zapobiec przedłużonemu zużyciu zasobów.

**6. Techniki piaskownicy**

Ogranicz dostęp LLM do zasobów sieciowych, usług wewnętrznych i
interfejsów API.

Ma to szczególne znaczenie we wszystkich typowych scenariuszach,
ponieważ obejmuje ryzyko i zagrożenia wewnętrzne. Ponadto reguluje
zakres dostępu aplikacji LLM do danych i zasobów, służąc tym samym jako
kluczowy mechanizm kontroli mający na celu ograniczenie lub zapobieganie
atakom typu side-channel.

**7. Kompleksowe rejestrowanie, monitorowanie i wykrywanie anomalii**

Ciągłe monitorowanie wykorzystania zasobów i wdrażanie rejestrowania w
celu wykrywania nietypowych wzorców zużycia zasobów i reagowania na nie.

**8. Znak wodny**

Wdrożenie frameworków znaków wodnych w celu osadzania i wykrywania
nieautoryzowanego wykorzystania wyników LLM.

**9. Łagodna degradacja**

Zaprojektowanie systemu tak, aby w przypadku dużego obciążenia ulegał
łagodnej degradacji, zachowując częściową funkcjonalność zamiast
całkowitej awarii.

**10. Ograniczenie działań w kolejce i solidna skalowalność**

Wprowadź ograniczenia dotyczące liczby działań w kolejce i całkowitej
liczby działań, jednocześnie wdrażając dynamiczne skalowanie i
równoważenie obciążenia, aby obsłużyć zmienne wymagania i zapewnić stałą
wydajność systemu.

**11. Szkolenie w zakresie odporności na ataki**

Przeszkol modele w zakresie wykrywania i łagodzenia skutków wrogich
zapytań i prób ekstrakcji.

**12. Filtrowanie tokenów glitch**

Stwórz listy znanych tokenów glitch i skanuj dane wyjściowe przed
dodaniem ich do okna kontekstowego modelu.

**13. Kontrola dostępu**

Wprowadź silną kontrolę dostępu, w tym kontrolę dostępu opartą na rolach
(RBAC) i zasadę minimalnych uprawnień, aby ograniczyć nieautoryzowany
dostęp do repozytoriów modeli LLM i środowisk szkoleniowych.

**14. Scentralizowany wykaz modeli ML**

Korzystaj ze scentralizowanego wykazu lub rejestru modeli ML używanych w
produkcji, zapewniając odpowiednie zarządzanie i kontrolę dostępu.

**15. Zautomatyzowane wdrażanie MLOps**

Wdrożenie automatycznego wdrażania MLOps wraz z przepływami pracy w
zakresie zarządzania, śledzenia i zatwierdzania w celu zaostrzenia
kontroli dostępu i wdrażania w ramach infrastruktury.

**Przykładowe scenariusze ataków**

**Scenariusz nr 1: Niekontrolowana wielkość danych wejściowych**

Atakujący przesyła niezwykle duże dane wejściowe do aplikacji LLM
przetwarzającej dane tekstowe, co powoduje nadmierne zużycie pamięci i
obciążenie procesora, potencjalnie powodując awarię systemu lub znaczne
spowolnienie działania usługi.

**Scenariusz nr 2: Powtarzające się żądania**

Atakujący przesyła dużą liczbę żądań do interfejsu API LLM, powodując
nadmierne zużycie zasobów obliczeniowych i uniemożliwiając korzystanie z
usługi legalnym użytkownikom.

**Scenariusz nr 3: Zapytania wymagające dużej ilości zasobów**

Atakujący tworzy specjalne dane wejściowe, które mają wywołać
najbardziej obciążające procesy LLM, co prowadzi do przedłużonego
wykorzystania procesora i potencjalnej awarii systemu.

**Scenariusz nr 4: Odmowa dostępu do portfela (DoW)**

Atakujący generuje nadmierną liczbę operacji, aby wykorzystać model
płatności za rzeczywiste wykorzystanie usług AI w chmurze, powodując
niemożliwe do pokrycia koszty dla dostawcy usług.

**Scenariusz nr 5: Replikacja modelu funkcjonalnego**

Atakujący wykorzystuje interfejs API LLM do generowania syntetycznych
danych szkoleniowych i dostosowuje inny model, tworząc funkcjonalny
odpowiednik i omijając tradycyjne ograniczenia związane z ekstrakcją
modelu.

**Scenariusz nr 6: Ominięcie filtrowania danych wejściowych systemu**

Złośliwy atakujący omija techniki filtrowania danych wejściowych i
preambuły LLM, aby przeprowadzić atak kanałem bocznym i pobrać
informacje o modelu do zdalnie kontrolowanego zasobu, nad którym
sprawuje kontrolę.

**Linki referencyjne**

[[Proof Pudding
(CVE-2019-20634)]{.underline}](https://avidml.org/database/avid-2023-v009/)
**AVID** (moohax & monoxgas)

[[arXiv:2403.06634 Kradzież części produkcyjnego modelu
językowego]{.underline}](https://arxiv.org/abs/2403.06634) **arXiv**

[[Runaway LLaMA \| Jak wyciekł model NLP LLaMA firmy
Meta]{.underline}](https://www.deeplearning.ai/the-batch/how-metas-llama-nlp-model-leaked/):
**Deep Learning Blog**

[[Nie pobrałby Pan/Pani sztucznej inteligencji, Wyodrębnianie modeli
sztucznej inteligencji z aplikacji
mobilnych]{.underline}](https://altayakkus.substack.com/p/you-wouldnt-download-an-ai):
**blog Substack**

[[Kompleksowa struktura obrony przed atakami polegającymi na
wyodrębnianiu
modeli]{.underline}](https://ieeexplore.ieee.org/document/10080996):
**IEEE**

[[Alpaca: silny, powtarzalny model wykonujący
instrukcje]{.underline}](https://crfm.stanford.edu/2023/03/13/alpaca.html):
**Stanford Center on Research for Foundation Models (CRFM)**

[[Jak znakowanie wodne może pomóc w ograniczeniu potencjalnego ryzyka
związanego z modelami
LLM?]{.underline}](https://www.kdnuggets.com/2023/03/watermarking-help-mitigate-potential-risks-llms.html):
**KD Nuggets**

[[Zabezpieczanie wag modeli AI Zapobieganie kradzieży i nadużyciom
modeli
najnowocześniejszych]{.underline}](https://www.rand.org/content/dam/rand/pubs/research_reports/RRA2800/RRA2849-1/RAND_RRA2849-1.pdf)

[[Przykłady Sponge: Ataki na opóźnienia energetyczne w sieciach
neuronowych: Arxiv White
Paper]{.underline}](https://arxiv.org/abs/2006.03463) **arXiv**

[[Incydent bezpieczeństwa Sourcegraph dotyczący manipulacji limitami API
i ataku
DoS]{.underline}](https://about.sourcegraph.com/blog/security-update-august-2023)
**Sourcegraph**

**Powiązane ramy i taksonomie**

W tej sekcji znajdują się wyczerpujące informacje, scenariusze,
strategie związane z wdrażaniem infrastruktury, stosowane środki
kontroli środowiska i inne najlepsze praktyki.

- [[MITRE CWE-400: Niekontrolowane zużycie
  zasobów]{.underline}](https://cwe.mitre.org/data/definitions/400.html)
  **Wykaz typowych słabych punktów MITRE**

- [[AML.TA0000 Dostęp do modelu ML: Mitre
  ATLAS]{.underline}](https://atlas.mitre.org/tactics/AML.TA0000) i
  [[AML.T0024 Wyciek danych poprzez API wnioskowania
  ML]{.underline}](https://atlas.mitre.org/techniques/AML.T0024) **MITRE
  ATLAS**

- [[AML.T0029 -- Odmowa dostępu do usługi
  ML]{.underline}](https://atlas.mitre.org/techniques/AML.T0029) **MITRE
  ATLAS**

- [[AML.T0034 -- Pozyskiwanie
  kosztów]{.underline}](https://atlas.mitre.org/techniques/AML.T0034)
  **MITRE ATLAS**

- [[AML.T0025 --- Wyciek danych za pomocą środków
  cybernetycznych]{.underline}](https://atlas.mitre.org/techniques/AML.T0025)
  **MITRE ATLAS**

- [[OWASP Machine Learning Security Top Ten --- ML05:2023 Kradzież
  modelu]{.underline}](https://owasp.org/www-project-machine-learning-security-top-10/docs/ML05_2023-Model_Theft.html)
  **OWASP ML Top 10**

- [[API4:2023 --- Nieograniczone zużycie
  zasobów]{.underline}](https://owasp.org/API-Security/editions/2023/en/0xa4-unrestricted-resource-consumption/)
  **OWASP Web Application Top 10**

- [[OWASP Zarządzanie
  zasobami]{.underline}](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/)
  **OWASP Praktyki bezpiecznego kodowania**
