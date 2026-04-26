**LLM02:2025 Ujawnianie informacji poufnych**

**Opis**

Informacje poufne mogą mieć wpływ zarówno na model LLM, jak i kontekst
jego zastosowania. Obejmują one dane osobowe (PII), dane finansowe,
dokumentację medyczną, poufne dane biznesowe, poświadczenia
bezpieczeństwa i dokumenty prawne. Modele zastrzeżone mogą również
posiadać unikalne metody szkolenia i kod źródłowy uznawany za wrażliwy,
zwłaszcza w modelach zamkniętych lub podstawowych.

LLM, zwłaszcza gdy są wbudowane w aplikacje, narażone są na ryzyko
ujawnienia danych wrażliwych, algorytmów zastrzeżonych lub poufnych
informacji poprzez swoje wyniki. Może to skutkować nieuprawnionym
dostępem do danych, naruszeniem prywatności i naruszeniem praw własności
intelektualnej. Konsumenci powinni być świadomi tego, jak bezpiecznie
korzystać z LLM. Muszą rozumieć ryzyko związane z nieumyślnym podaniem
danych wrażliwych, które mogą zostać później ujawnione w wynikach
modelu.

Aby zmniejszyć to ryzyko, aplikacje LLM powinny przeprowadzać
odpowiednie oczyszczanie danych, aby zapobiec przedostawaniu się danych
użytkowników do modelu szkoleniowego. Właściciele aplikacji powinni
również zapewnić jasne zasady użytkowania, umożliwiające użytkownikom
rezygnację z uwzględniania ich danych w modelu szkoleniowym. Dodanie
ograniczeń w systemie dotyczących typów danych, które LLM powinien
zwracać, może ograniczyć ujawnianie poufnych informacji. Jednak takie
ograniczenia nie zawsze są przestrzegane i mogą zostać ominięte poprzez
wstrzyknięcie poleceń lub inne metody.

**Typowe przykłady podatności**

**1. Wyciek danych osobowych**

Podczas interakcji z LLM mogą zostać ujawnione dane osobowe (PII).

**2. Ujawnienie algorytmów zastrzeżonych**

Źle skonfigurowane wyniki modelu mogą ujawnić zastrzeżone algorytmy lub
dane. Ujawnienie danych szkoleniowych może narazić modele na ataki
inwersyjne, w których atakujący wydobywają poufne informacje lub
rekonstruują dane wejściowe. Na przykład, jak wykazano w ataku „Proof
Pudding" (CVE-2019-20634), ujawnione dane szkoleniowe ułatwiły wydobycie
i inwersję modelu, umożliwiając atakującym obejście zabezpieczeń
algorytmów uczenia maszynowego i filtrów poczty elektronicznej.

**3. Ujawnienie poufnych danych biznesowych**

Wygenerowane odpowiedzi mogą nieumyślnie zawierać poufne informacje
biznesowe.

**Strategie zapobiegania i ograniczania skutków**

**Oczyszczanie:**

**1. Zintegruj techniki oczyszczania danych**

Wdrożcie oczyszczanie danych, aby zapobiec przedostawaniu się danych
użytkowników do modelu szkoleniowego. Obejmuje to czyszczenie lub
maskowanie poufnych treści przed wykorzystaniem ich w szkoleniu.

**2. Solidna walidacja danych wejściowych**

Zastosujcie rygorystyczne metody walidacji danych wejściowych, aby
wykrywać i filtrować potencjalnie szkodliwe lub poufne dane wejściowe,
zapewniając, że nie naruszają one modelu.

**Kontrola dostępu:**

**1. Egzekwowanie ścisłej kontroli dostępu**

Ogranicz dostęp do wrażliwych danych w oparciu o zasadę minimalnych
uprawnień. Przyznawaj dostęp tylko do danych niezbędnych dla konkretnego
użytkownika lub procesu.

**2. Ograniczanie źródeł danych**

Ogranicz dostęp modelu do zewnętrznych źródeł danych i zapewnij
bezpieczne zarządzanie koordynacją danych w czasie wykonywania, aby
uniknąć niezamierzonego wycieku danych.

**Uczenie federacyjne i techniki ochrony prywatności:**

**1. Wykorzystanie uczenia federacyjnego**

Szkolcie modele przy użyciu zdecentralizowanych danych przechowywanych
na wielu serwerach lub urządzeniach. Takie podejście minimalizuje
potrzebę scentralizowanego gromadzenia danych i zmniejsza ryzyko
ujawnienia.

**2. Włączcie prywatność różnicową**

Zastosujcie techniki, które dodają szum do danych lub wyników,
utrudniając atakującym odtworzenie poszczególnych punktów danych.

**Edukacja użytkowników i przejrzystość:**

**1. Edukujcie użytkowników w zakresie bezpiecznego korzystania z LLM**

Zapewnij wytyczne dotyczące unikania wprowadzania poufnych informacji.
Zaoferuj szkolenia dotyczące najlepszych praktyk w zakresie bezpiecznej
interakcji z modelami LLM.

**2. Zapewnij przejrzystość w zakresie wykorzystania danych**

Utrzymuj jasne zasady dotyczące przechowywania, wykorzystywania i
usuwania danych. Pozwól użytkownikom zrezygnować z uwzględniania ich
danych w procesach szkoleniowych.

**Bezpieczna konfiguracja systemu:**

**1. Ukryj preambułę systemu**

Ogranicz możliwość zmiany lub dostępu użytkowników do początkowych
ustawień systemu, zmniejszając ryzyko ujawnienia konfiguracji
wewnętrznej.

**2. Odwołaj się do najlepszych praktyk dotyczących błędnej konfiguracji
zabezpieczeń**

Postępuj zgodnie z wytycznymi, takimi jak „OWASP API8:2023 Security
Misconfiguration", aby zapobiec wyciekowi poufnych informacji poprzez
komunikaty o błędach lub szczegóły konfiguracji. (Link do
odnośnika:[[OWASP API8:2023 Security
Misconfiguration]{.underline}](https://owasp.org/API-Security/editions/2023/en/0xa8-security-misconfiguration/))

**Zaawansowane techniki:**

**1. Szyfrowanie homomorficzne**

Użyj szyfrowania homomorficznego, aby umożliwić bezpieczną analizę
danych i uczenie maszynowe z zachowaniem prywatności. Zapewnia to
poufność danych podczas przetwarzania przez model.

**2. Tokenizacja i redagowanie**

Wdroż tokenizację w celu wstępnego przetwarzania i oczyszczania poufnych
informacji. Techniki takie jak dopasowywanie wzorców mogą wykrywać i
redagować poufne treści przed przetworzeniem.

**Przykładowe scenariusze ataku**

**Scenariusz nr 1: Niezamierzone ujawnienie danych**

Użytkownik otrzymuje odpowiedź zawierającą dane osobowe innego
użytkownika z powodu nieodpowiedniego oczyszczenia danych.

**Scenariusz nr 2: Ukierunkowane wstrzyknięcie podpowiedzi**

Atakujący omija filtry wejściowe, aby wyodrębnić poufne informacje.

**Scenariusz nr 3: Wyciek danych poprzez dane szkoleniowe**

Nieostrożne włączenie danych do szkolenia prowadzi do ujawnienia
poufnych informacji.

**Linki referencyjne**

[[Wnioski wyciągnięte z wycieku danych Samsunga z
ChatGPT]{.underline}](https://cybernews.com/security/chatgpt-samsung-leak-explained-lessons/):
**Cybernews**

[[Kryzys związany z wyciekiem danych AI: nowe narzędzie zapobiega
przekazywaniu tajemnic firmowych do
ChatGPT]{.underline}](https://www.foxbusiness.com/politics/ai-data-leak-crisis-prevent-company-secrets-chatgpt):
**Fox Business**

[[ChatGPT ujawnia poufne dane po poleceniu powtarzania „wiersza" w
nieskończoność]{.underline}](https://www.wired.com/story/chatgpt-poem-forever-security-roundup/):
**Wired**

[[Wykorzystanie różnicowej prywatności do tworzenia bezpiecznych
modeli]{.underline}](https://neptune.ai/blog/using-differential-privacy-to-build-secure-models-tools-methods-best-practices):
**Neptune Blog**

[[Proof Pudding
(CVE-2019-20634)]{.underline}](https://avidml.org/database/avid-2023-v009/)
**AVID** (moohax & monoxgas)

**Powiązane ramy i taksonomie**

W tej sekcji znajdą Państwo wyczerpujące informacje, scenariusze i
strategie dotyczące wdrażania infrastruktury, stosowanych środków
kontroli środowiska oraz innych najlepszych praktyk.

[[AML.T0024.000 -- Członkostwo w bazie danych
szkoleniowych]{.underline}](https://atlas.mitre.org/techniques/AML.T0024.000)
**MITRE ATLAS**

[[AML.T0024.001 -- Odwrócenie modelu
ML]{.underline}](https://atlas.mitre.org/techniques/AML.T0024.001)
**MITRE ATLAS**

[[AML.T0024.002 -- Wyodrębnienie modelu
ML]{.underline}](https://atlas.mitre.org/techniques/AML.T0024.002)
**MITRE ATLAS**
