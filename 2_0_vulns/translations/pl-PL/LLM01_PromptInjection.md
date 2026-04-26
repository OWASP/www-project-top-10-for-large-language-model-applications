**LLM01:2025 Wstrzyknięcie polecenia**

**Opis**

Luka w zabezpieczeniach związana z wstrzyknięciem polecenia występuje,
gdy polecenia użytkownika zmieniają zachowanie lub wynik działania
modelu LLM w niezamierzony sposób. Dane wejściowe mogą wpływać na model,
nawet jeśli są niewidoczne dla ludzi, dlatego wstrzyknięcia poleceń nie
muszą być widoczne/czytelne dla ludzi, o ile treść jest analizowana
przez model.

Luki w zabezpieczeniach związane z wstrzykiwaniem poleceń występują w
sposobie przetwarzania poleceń przez modele oraz w sposobie, w jaki dane
wejściowe mogą zmusić model do nieprawidłowego przekazania danych
poleceń do innych części modelu, potencjalnie powodując naruszenie
wytycznych, generowanie szkodliwych treści, umożliwienie
nieautoryzowanego dostępu lub wpływ na krytyczne decyzje. Chociaż
techniki takie jak generowanie rozszerzone o odzyskiwanie (RAG) i
dostrajanie mają na celu zwiększenie trafności i dokładności wyników
LLM, badania pokazują, że nie eliminują one całkowicie luk w
zabezpieczeniach związanych z wstrzykiwaniem poleceń.

Chociaż wstrzyknięcie poleceń i łamanie zabezpieczeń są pojęciami
powiązanymi w kontekście bezpieczeństwa LLM, często są one używane
zamiennie. Wstrzyknięcie poleceń polega na manipulowaniu odpowiedziami
modelu za pomocą określonych danych wejściowych w celu zmiany jego
zachowania, co może obejmować ominięcie środków bezpieczeństwa. Łamanie
zabezpieczeń jest formą wstrzyknięcia poleceń, w której atakujący
dostarcza dane wejściowe, które powodują, że model całkowicie ignoruje
swoje protokoły bezpieczeństwa. Programiści mogą wbudować zabezpieczenia
w monity systemowe i obsługę danych wejściowych, aby pomóc w
ograniczeniu ataków typu wstrzyknięcie poleceń, ale skuteczne
zapobieganie łamaniu zabezpieczeń wymaga ciągłych aktualizacji
mechanizmów szkolenia i bezpieczeństwa modelu.

**Rodzaje podatności na ataki typu wstrzyknięcia poleceń**

**Bezpośrednie ataki typu wstrzyknięcia poleceń**

Bezpośrednie wstrzyknięcia poleceń mają miejsce, gdy dane wejściowe
użytkownika bezpośrednio zmieniają zachowanie modelu w niezamierzony lub
nieoczekiwany sposób. Dane wejściowe mogą być zamierzone (tj. złośliwy
podmiot celowo tworzy polecenie w celu wykorzystania modelu) lub
niezamierzone (tj. użytkownik nieumyślnie dostarcza dane wejściowe,
które wywołują nieoczekiwane zachowanie).

**Pośrednie wstrzyknięcia poleceń**

Pośrednie wstrzyknięcia promptów występują, gdy LLM akceptuje dane
wejściowe z zewnętrznych źródeł, takich jak strony internetowe lub
pliki. Zewnętrzne źródło może zawierać dane, które po zinterpretowaniu
przez model zmieniają jego zachowanie w niezamierzony lub nieoczekiwany
sposób. Podobnie jak wstrzyknięcia bezpośrednie, wstrzyknięcia pośrednie
mogą być zamierzone lub niezamierzone.

Nasilenie i charakter skutków udanego ataku wstrzyknięcia podpowiedzi
mogą się znacznie różnić i zależą w dużej mierze zarówno od kontekstu
biznesowego, w którym działa model, jak i od agencji, która go
zaprojektowała. Ogólnie rzecz biorąc, wstrzyknięcie podpowiedzi może
jednak prowadzić do niezamierzonych skutków, w tym między innymi:

Ujawnienie poufnych informacji

Ujawnienie poufnych informacji o infrastrukturze systemu AI lub
podpowiedziach systemu

Manipulowanie treścią prowadząca do nieprawidłowych lub stronniczych
wyników

Umożliwienie nieautoryzowanego dostępu do funkcji dostępnych dla LLM

Wykonywanie dowolnych poleceń w połączonych systemach

Manipulowanie krytycznymi procesami decyzyjnymi

Rozwój wielomodalnej sztucznej inteligencji, która przetwarza
jednocześnie wiele typów danych, wprowadza wyjątkowe ryzyko związane z
wstrzyknięciem poleceń. Złośliwi aktorzy mogą wykorzystać interakcje
między modalnościami, na przykład ukrywając instrukcje w obrazach
towarzyszących nieszkodliwym tekstom. Złożoność tych systemów zwiększa
powierzchnię ataku. Modele wielomodalne mogą być również podatne na nowe
ataki między modalnościami, które są trudne do wykrycia i złagodzenia
przy użyciu obecnych technik. Solidne zabezpieczenia specyficzne dla
modeli wielomodalnych są ważnym obszarem dalszych badań i rozwoju.

**Strategie zapobiegania i łagodzenia skutków**

Luki w zabezpieczeniach związane z wstrzykiwaniem poleceń są możliwe ze
względu na charakter generatywnej sztucznej inteligencji. Biorąc pod
uwagę stochastyczny wpływ leżący u podstaw działania modeli, nie jest
jasne, czy istnieją niezawodne metody zapobiegania wstrzykiwaniu
poleceń. Jednak następujące środki mogą złagodzić skutki wstrzykiwania
poleceń:

**1. Ogranicz zachowanie modelu**

Podaj konkretne instrukcje dotyczące roli, możliwości i ograniczeń
modelu w ramach systemu podpowiedzi. Egzekwuj ścisłe przestrzeganie
kontekstu, ogranicz odpowiedzi do określonych zadań lub tematów i
poinstruuj model, aby ignorował próby modyfikacji podstawowych
instrukcji.

**2. Zdefiniuj i zweryfikuj oczekiwane formaty wyjściowe**

Określ jasne formaty wyników, wymagaj szczegółowego uzasadnienia i
podania źródeł oraz używaj deterministycznego kodu do sprawdzania
zgodności z tymi formatami.

**3. Wprowadź filtrowanie danych wejściowych i wyjściowych**

Zdefiniuj kategorie danych wrażliwych i opracuj zasady identyfikacji i
postępowania z takimi treściami. Zastosuj filtry semantyczne i
sprawdzanie ciągów znaków w celu wykrycia niedozwolonych treści. Oceniaj
odpowiedzi za pomocą trójkąta RAG: oceń trafność kontekstu, uzasadnienie
i trafność pytania/odpowiedzi, aby zidentyfikować potencjalnie złośliwe
wyniki.

**4. Egzekwuj kontrolę uprawnień i dostęp oparty na minimalnych
uprawnieniach**

Wyposaż aplikację we własne tokeny API w celu rozszerzenia
funkcjonalności i obsługuj te funkcje w kodzie, zamiast udostępniać je
modelowi. Ogranicz uprawnienia dostępu modelu do minimum niezbędnego do
wykonywania zamierzonych operacji.

**5. Wymagaj zatwierdzania przez człowieka w przypadku działań wysokiego
ryzyka**

Wprowadź kontrolę z udziałem człowieka dla operacji uprzywilejowanych,
aby zapobiec nieautoryzowanym działaniom.

**6. Segreguj i identyfikuj treści zewnętrzne**

Oddziel i wyraźnie oznacz treści, którym nie ufasz, aby ograniczyć ich
wpływ na polecenia użytkownika.

**7. Przeprowadź testy przeciwnika i symulacje ataków**

Regularnie przeprowadzaj testy penetracyjne i symulacje naruszeń,
traktując model jako użytkownika, któremu nie ufasz, aby sprawdzić
skuteczność granic zaufania i kontroli dostępu.

**Przykładowe scenariusze ataków**

**Scenariusz nr 1: Bezpośrednie wstrzyknięcie**

Atakujący wstrzykuje polecenie do chatbota obsługi klienta, instruując
go, aby zignorował poprzednie wytyczne, zapytał o prywatne zasoby danych
i wysłał e-maile, co prowadzi do nieautoryzowanego dostępu i eskalacji
uprawnień.

**Scenariusz nr 2: Pośrednie wstrzyknięcie**

Użytkownik wykorzystuje LLM do podsumowania strony internetowej
zawierającej ukryte instrukcje, które powodują, że LLM wstawia obraz
łączący się z adresem URL, co prowadzi do wycieku prywatnej rozmowy.

**Scenariusz nr 3: Niezamierzone wstrzyknięcie**

Firma umieszcza w opisie stanowiska pracę instrukcję dotyczącą
identyfikacji aplikacji wygenerowanych przez sztuczną inteligencję.
Kandydat, nieświadomy tej instrukcji, używa LLM do optymalizacji swojego
CV, nieumyślnie uruchamiając wykrywanie sztucznej inteligencji.

**Scenariusz nr 4: Celowy wpływ na model**

Atakujący modyfikuje dokument w repozytorium używanym przez aplikację
Retrieval-Augmented Generation (RAG). Gdy zapytanie użytkownika zwraca
zmodyfikowaną treść, złośliwe instrukcje zmieniają wynik LLM, generując
mylące wyniki.

**Scenariusz nr 5: Wstrzyknięcie kodu**

Atakujący wykorzystuje lukę (CVE-2024-5184) w asystencie poczty
elektronicznej opartym na LLM, aby wstrzyknąć złośliwe polecenia,
umożliwiające dostęp do poufnych informacji i manipulowanie treścią
wiadomości e-mail.

**Scenariusz nr 6: Podział ładunku**

Atakujący przesyła CV z podzielonymi złośliwymi poleceniami. Kiedy LLM
jest używany do oceny kandydata, połączone polecenia manipulują
odpowiedzią modelu, co skutkuje pozytywną rekomendacją pomimo
rzeczywistej treści CV.

**Scenariusz nr 7: Wstrzyknięcie multimodalne**

Atakujący osadza złośliwy polecenie w obrazie towarzyszącym
nieszkodliwemu tekstowi. Gdy wielomodalna sztuczna inteligencja
przetwarza jednocześnie obraz i tekst, ukryte polecenie zmienia
zachowanie modelu, potencjalnie prowadząc do nieautoryzowanych działań
lub ujawnienia poufnych informacji.

**Scenariusz nr 8: Wrogi sufiks**

Atakujący dodaje do monitu pozornie bezsensowny ciąg znaków, który w
złośliwy sposób wpływa na wynik LLM, omijając środki bezpieczeństwa.

**Scenariusz nr 9: Atak wielojęzyczny/zaciemniający**

Atakujący używa wielu języków lub koduje złośliwe instrukcje (np. za
pomocą Base64 lub emoji) w celu ominięcia filtrów i manipulowania
zachowaniem LLM.

**Linki referencyjne**

[[Luki w zabezpieczeniach wtyczki ChatGPT --- czat z
kodem]{.underline}](https://embracethered.com/blog/posts/2023/chatgpt-plugin-vulns-chat-with-code/)
**Embrace the Red**

[[Fałszowanie żądań między wtyczkami ChatGPT i wstrzykiwanie
poleceń]{.underline}](https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./)
**Embrace the Red**

**Arxiv**

[[Obrona ChatGPT przed atakiem typu złamanie zabezpieczeń poprzez
samoprzypomnienie]{.underline}](https://www.researchsquare.com/article/rs-2873090/v1)
**Research Square**

[[Atak typu wstrzyknięcie polecenia na aplikacje zintegrowane z
LLM]{.underline}](https://arxiv.org/abs/2306.05499) **Cornell
University**

[[Wstrzyknij mój plik PDF: wstrzyknięcie polecenia dla Państwa
CV]{.underline}](https://kai-greshake.de/posts/inject-my-pdf) **Kai
Greshake**

[[Nie to, na co się Państwo zapisali: Naruszenie bezpieczeństwa
rzeczywistych aplikacji zintegrowanych z LLM poprzez pośrednie
wstrzyknięcie
polecenia]{.underline}](https://arxiv.org/pdf/2302.12173.pdf)
**Uniwersytet Cornell**

[[Modelowanie zagrożeń aplikacji
LLM]{.underline}](https://aivillage.org/large%20language%20models/threat-modeling-llm/)
**AI Village**

[[Ograniczanie wpływu ataków typu wstrzyknięcie polecenia poprzez
projektowanie]{.underline}](https://research.kudelskisecurity.com/2023/05/25/reducing-the-impact-of-prompt-injection-attacks-through-design/)
**Kudelski Security**

[[Wrogie uczenie maszynowe: taksonomia i terminologia ataków oraz
środków zaradczych
(nist.gov)]{.underline}](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-2e2023.pdf)

[[2407.07403 Przegląd ataków na duże modele wizualno-językowe: zasoby,
postępy i przyszłe trendy
(arxiv.org)]{.underline}](https://arxiv.org/abs/2407.07403)

[[Wykorzystywanie programowego zachowania modeli LLM: podwójne
zastosowanie poprzez standardowe ataki
bezpieczeństwa]{.underline}](https://ieeexplore.ieee.org/document/10579515)

[[Uniwersalne i przenośne ataki przeciwników na zharmonizowane modele
językowe (arxiv.org)]{.underline}](https://arxiv.org/abs/2307.15043)

[[Od ChatGPT do ThreatGPT: wpływ generatywnej sztucznej inteligencji na
cyberbezpieczeństwo i prywatność
(arxiv.org)]{.underline}](https://arxiv.org/abs/2307.00691)

**Powiązane ramy i taksonomie**

W tej sekcji znajdą Państwo wyczerpujące informacje, scenariusze i
strategie dotyczące wdrażania infrastruktury, stosowanych środków
kontroli środowiska oraz innych najlepszych praktyk.

- [[AML.T0051.000 -- Wstrzyknięcie polecenia LLM:
  bezpośrednie]{.underline}](https://atlas.mitre.org/techniques/AML.T0051.000)
  **MITRE ATLAS**

- [[AML.T0051.001 -- Wstrzyknięcie polecenia LLM:
  pośrednie]{.underline}](https://atlas.mitre.org/techniques/AML.T0051.001)
  **MITRE ATLAS**

- [[AML.T0054 -- Wstrzyknięcie łamania zabezpieczeń LLM:
  bezpośrednie]{.underline}](https://atlas.mitre.org/techniques/AML.T0054)
  **MITRE ATLAS**
