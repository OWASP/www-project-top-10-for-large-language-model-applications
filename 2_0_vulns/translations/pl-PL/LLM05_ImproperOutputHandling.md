**LLM05:2025 Nieprawidłowe przetwarzanie wyników**

**Opis**

Nieprawidłowe przetwarzanie wyników odnosi się konkretnie do
niewystarczającej walidacji, oczyszczania i przetwarzania wyników
generowanych przez duże modele językowe przed przekazaniem ich do innych
komponentów i systemów. Ponieważ treści generowane przez LLM mogą być
kontrolowane za pomocą poleceń, zachowanie to jest podobne do
zapewnienia użytkownikom pośredniego dostępu do dodatkowych funkcji.
Nieprawidłowe przetwarzanie danych wyjściowych różni się od nadmiernego
polegania na tym, że dotyczy danych wyjściowych generowanych przez LLM
przed przekazaniem ich dalej, podczas gdy nadmierne poleganie
koncentruje się na szerszych kwestiach związanych z nadmierną
zależnością od dokładności i odpowiedniości danych wyjściowych LLM.
Wykorzystanie luki w zabezpieczeniach związanej z nieprawidłowym
przetwarzaniem danych wyjściowych może skutkować atakami XSS i CSRF w
przeglądarkach internetowych, a także atakami SSRF, eskalacją uprawnień
lub zdalnym wykonaniem kodu w systemach zaplecza. Następujące warunki
mogą zwiększyć wpływ tej luki w zabezpieczeniach:

Aplikacja przyznaje LLM uprawnienia wykraczające poza zakres
przeznaczony dla użytkowników końcowych, umożliwiając eskalację
uprawnień lub zdalne wykonanie kodu.

Aplikacja jest podatna na pośrednie ataki typu wstrzyknięcie polecania,
które mogą umożliwić atakującemu uzyskanie uprzywilejowanego dostępu do
środowiska docelowego użytkownika.

Rozszerzenia stron trzecich nie weryfikują odpowiednio danych
wejściowych.

Brak odpowiedniego kodowania danych wyjściowych dla różnych kontekstów
(np. HTML, JavaScript, SQL).

Niewystarczające monitorowanie i rejestrowanie danych wyjściowych LLM.

Brak ograniczeń szybkości lub wykrywania anomalii w zakresie korzystania
z LLM

**Typowe przykłady podatności**

Wyniki LLM są wprowadzane bezpośrednio do powłoki systemowej lub
podobnej funkcji, takiej jak exec lub eval, co powoduje zdalne wykonanie
kodu.

LLM generuje kod JavaScript lub Markdown i zwraca go użytkownikowi. Kod
jest następnie interpretowany przez przeglądarkę, co powoduje atak XSS.

Zapytania SQL generowane przez LLM są wykonywane bez odpowiedniej
parametryzacji, co prowadzi do wstrzyknięcia kodu SQL.

Wyniki LLM są wykorzystywane do tworzenia ścieżek plików bez
odpowiedniej sanitizacji, co może potencjalnie skutkować lukami w
zabezpieczeniach związanych z przechodzeniem ścieżek.

Treści generowane przez LLM są wykorzystywane w szablonach wiadomości
e-mail bez odpowiedniego filtrowania lub oczyszczania, co może
potencjalnie prowadzić do ataków phishingowych.

**Strategie zapobiegania i łagodzenia skutków**

Traktuj model jak każdego innego użytkownika, stosując podejście oparte
na zerowym zaufaniu i stosuj odpowiednią walidację danych wejściowych w
odpowiedziach pochodzących z modelu do funkcji zaplecza.

Postępuj zgodnie z wytycznymi OWASP ASVS (Application Security
Verification Standard), aby zapewnić skuteczną walidację i oczyszczanie
danych wejściowych.

Koduj dane wyjściowe modelu z powrotem do użytkowników, aby ograniczyć
niepożądane wykonywanie kodu przez JavaScript lub Markdown. OWASP ASVS
zawiera szczegółowe wytyczne dotyczące kodowania danych wyjściowych.

Wdrażaj kodowanie danych wyjściowych z uwzględnieniem kontekstu, w
zależności od miejsca wykorzystania danych wyjściowych LLM (np.
kodowanie HTML dla treści internetowych, oczyszczanie SQL dla zapytań do
baz danych).

Używaj zapytań parametrycznych lub przygotowanych instrukcji dla
wszystkich operacji baz danych związanych z wynikami LLM.

Stosuj ścisłe zasady bezpieczeństwa treści (CSP), aby ograniczyć ryzyko
ataków XSS z treści generowanych przez LLM.

Wdroż solidne systemy rejestrowania i monitorowania w celu wykrywania
nietypowych wzorców w wynikach LLM, które mogą wskazywać na próby
wykorzystania luk.

**Przykładowe scenariusze ataków**

**Scenariusz nr 1**

Aplikacja wykorzystuje rozszerzenie LLM do generowania odpowiedzi dla
funkcji chatbota. Rozszerzenie oferuje również szereg funkcji
administracyjnych dostępnych dla innego uprzywilejowanego LLM. LLM
ogólnego przeznaczenia przekazuje swoją odpowiedź bezpośrednio, bez
odpowiedniej walidacji danych wyjściowych, do rozszerzenia, powodując
jego zamknięcie w celu konserwacji.

**Scenariusz nr 2**

Użytkownik korzysta z narzędzia do tworzenia streszczeń stron
internetowych opartego na LLM w celu wygenerowania zwięzłego
streszczenia artykułu. Strona internetowa zawiera polecenie
wstrzyknięcia, które nakazuje LLM przechwycenie poufnych treści ze
strony internetowej lub z rozmowy użytkownika. Następnie LLM może
zakodować poufne dane i wysłać je, bez żadnej weryfikacji wyników ani
filtrowania, do serwera kontrolowanego przez atakującego.

**Scenariusz nr 3**

LLM umożliwia użytkownikom tworzenie zapytań SQL do źródłowej bazy
danych za pomocą funkcji przypominającej czat. Użytkownik żąda zapytania
o usunięcie wszystkich tabel bazy danych. Jeśli zapytanie utworzone
przez LLM nie zostanie dokładnie sprawdzone, wszystkie tabele bazy
danych zostaną usunięte.

**Scenariusz nr 4**

Aplikacja internetowa wykorzystuje LLM do generowania treści na
podstawie poleceń tekstowych użytkownika bez oczyszczania danych
wyjściowych. Atakujący może przesłać spreparowane polecenie, które
spowoduje, że LLM zwróci nieoczyszczoną zawartość JavaScript, co
doprowadzi do ataku XSS po wyrenderowaniu w przeglądarce ofiary. Atak
ten był możliwy dzięki niewystarczającej weryfikacji poleceń.

**Scenariusz nr 5**

LLM jest używany do generowania dynamicznych szablonów wiadomości e-mail
na potrzeby kampanii marketingowej. Atakujący manipuluje LLM, aby
umieścić złośliwy kod JavaScript w treści wiadomości e-mail. Jeśli
aplikacja nie oczyści prawidłowo danych wyjściowych LLM, może to
doprowadzić do ataków XSS na odbiorców, którzy wyświetlają wiadomości
e-mail w podatnych na ataki klientach poczty elektronicznej.

**Scenariusz nr 6**

Model LLM jest używany do generowania kodu na podstawie danych
wejściowych w języku naturalnym w firmie programistycznej w celu
usprawnienia zadań programistycznych. Chociaż podejście to jest wydajne,
wiąże się z ryzykiem ujawnienia poufnych informacji, stworzenia
niebezpiecznych metod przetwarzania danych lub wprowadzenia luk w
zabezpieczeniach, takich jak wstrzyknięcie kodu SQL. Sztuczna
inteligencja może również generować nieistniejące pakiety
oprogramowania, co może potencjalnie skłonić programistów do pobrania
zasobów zainfekowanych złośliwym oprogramowaniem. Dokładna weryfikacja
kodu i sugerowanych pakietów ma kluczowe znaczenie dla zapobiegania
naruszeniom bezpieczeństwa, nieautoryzowanemu dostępowi i kompromitacji
systemu.

**Linki referencyjne**

1.  [[Proof Pudding
    (CVE-2019-20634)]{.underline}](https://avidml.org/database/avid-2023-v009/)
    **AVID** (moohax & monoxgas)

2.  [[Arbitrary Code
    Execution]{.underline}](https://security.snyk.io/vuln/SNYK-PYTHON-LANGCHAIN-5411357):
    **Snyk Security Blog**

3.  [[ChatGPT Plugin Exploit Explained: From Prompt Injection to
    Accessing Private
    Data]{.underline}](https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./):
    **Embrace The Red**

4.  [[New prompt injection attack on ChatGPT web version. Markdown
    images can steal your chat
    data.]{.underline}](https://systemweakness.com/new-prompt-injection-attack-on-chatgpt-web-version-ef717492c5c2?gi=8daec85e2116):
    **System Weakness**

5.  [[Nie należy ślepo ufać odpowiedziom LLM. Zagrożenia dla
    chatbotów]{.underline}](https://embracethered.com/blog/posts/2023/ai-injections-threats-context-matters/):
    **Embrace The Red**

6.  [[Modelowanie zagrożeń aplikacji
    LLM]{.underline}](https://aivillage.org/large%20language%20models/threat-modeling-llm/):
    **AI Village**

7.  [[OWASP ASVS -- 5 Walidacja, oczyszczanie i
    kodowanie]{.underline}](https://owasp-aasvs4.readthedocs.io/en/latest/V5.html#validation-sanitization-and-encoding):
    **OWASP AASVS**

8.  [[AI generuje halucynacje pakietów oprogramowania, a programiści je
    pobierają -- nawet jeśli mogą być zainfekowane złośliwym
    oprogramowaniem]{.underline}](https://www.theregister.com/2024/03/28/ai_bots_hallucinate_software_packages/)
    **Theregiste**
