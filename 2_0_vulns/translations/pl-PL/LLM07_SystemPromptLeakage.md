**LLM07:2025 Wyciek komunikatów systemowych**

**Opis**

Luka w zabezpieczeniach LLMs polegająca na wycieku komunikatów
systemowych odnosi się do ryzyka, że komunikaty systemowe lub instrukcje
używane do sterowania zachowaniem modelu mogą również zawierać poufne
informacje które nie powinny zostać ujawnione. Komunikaty systemowe mają
na celu kierowanie wynikami modelu w oparciu o wymagania aplikacji, ale
mogą nieumyślnie zawierać poufne informacje. Po wykryciu informacje te
mogą zostać wykorzystane do ułatwienia innych ataków.

Należy pamiętać, że podpowiedzi systemowe nie powinny być traktowane
jako tajemnice ani wykorzystywane jako środki kontroli bezpieczeństwa. W
związku z tym język podpowiedzi systemowych nie powinien zawierać danych
wrażliwych, takich jak poświadczenia, ciągi połączeń itp.

Podobnie, jeśli monit systemowy zawiera informacje opisujące różne role
i uprawnienia lub dane wrażliwe, takie jak ciągi połączeń lub hasła,
ujawnienie takich informacji może być pomocne, ale podstawowym
zagrożeniem dla bezpieczeństwa nie jest to, że zostały one ujawnione,
ale to, że aplikacja umożliwia ominięcie silnego zarządzania sesjami i
kontroli autoryzacji poprzez przekazanie tych zadań do LLM oraz że dane
wrażliwe są przechowywane w miejscu, w którym nie powinny się znajdować.

Krótko mówiąc: ujawnienie samego monitu systemowego nie stanowi
rzeczywistego zagrożenia --- zagrożenie bezpieczeństwa wynika z
elementów leżących u podstaw, niezależnie od tego, czy jest to
ujawnienie poufnych informacji, obejście zabezpieczeń systemu,
niewłaściwy podział uprawnień itp. Nawet jeśli dokładne sformułowania
nie zostaną ujawnione, osoby atakujące wchodzące w interakcję z systemem
prawie na pewno będą w stanie określić wiele zabezpieczeń i ograniczeń
formatowania obecnych w języku monitów systemowych w trakcie korzystania
z aplikacji, wysyłania wypowiedzi do modelu i obserwowania wyników.

**Typowe przykłady ryzyka**

**1. Ujawnienie wrażliwych funkcji**

Monit systemowy aplikacji może ujawniać poufne informacje lub funkcje,
które powinny pozostać tajne, takie jak poufna architektura systemu,
klucze API, poświadczenia bazy danych lub tokeny użytkowników. Mogą one
zostać wyodrębnione lub wykorzystane przez atakujących w celu uzyskania
nieautoryzowanego dostępu do aplikacji. Na przykład monit systemowy
zawierający typ bazy danych używanej przez narzędzie może umożliwić
atakującemu przeprowadzenie ataku typu SQL injection.

**2. Ujawnienie wewnętrznych zasad**

Komunikaty systemowe aplikacji ujawniają informacje o wewnętrznych
procesach decyzyjnych, które powinny pozostać poufne. Informacje te
pozwalają atakującym uzyskać wgląd w działanie aplikacji, co może
umożliwić im wykorzystanie słabych punktów lub ominięcie zabezpieczeń
aplikacji. Na przykład --- istnieje aplikacja bankowa z chatbotem,
której komunikaty systemowe mogą ujawniać takie informacje, jak: „Limit
transakcji dla użytkownika wynosi 5000 USD dziennie. Łączna kwota
kredytu dla użytkownika wynosi 10 000 USD". Informacje te pozwalają
atakującym ominąć zabezpieczenia aplikacji, np. przeprowadzając
transakcje przekraczające ustalony limit lub omijając łączną kwotę
kredytu.

**3. Ujawnianie kryteriów filtrowania**

Monit systemowy może poprosić model o filtrowanie lub odrzucenie
wrażliwych treści. Na przykład model może mieć komunikat systemowy o
treści: \> „Jeśli użytkownik zażąda informacji o innym użytkowniku,
zawsze odpowiadaj: »Przykro mi, nie mogę pomóc w tej sprawie«.

**4. Ujawnianie uprawnień i ról użytkowników**

Komunikat systemowy może ujawnić wewnętrzną strukturę ról lub poziomy
uprawnień w aplikacji. Na przykład komunikat systemowy może ujawnić: \>
»Rola użytkownika administratora zapewnia pełny dostęp do modyfikowania
rekordów użytkowników«. Jeśli atakujący dowiedzą się o tych
uprawnieniach opartych na rolach, mogą spróbować przeprowadzić atak
polegający na podwyższeniu uprawnień.

**Strategie zapobiegania i ograniczania skutków**

**1. Oddzielanie wrażliwych danych od komunikatów systemowych**

Należy unikać umieszczania jakichkolwiek wrażliwych informacji (np.
kluczy API, kluczy uwierzytelniających, nazw baz danych, ról
użytkowników, struktury uprawnień aplikacji) bezpośrednio w komunikatach
systemowych. Zamiast tego należy przenieść takie informacje do systemów,
do których model nie ma bezpośredniego dostępu.

**2. Unikanie polegania na monitach systemowych w celu ścisłej kontroli
zachowania**

Ponieważ modele LLM są podatne na inne ataki, takie jak wstrzyknięcia
monitów, które mogą zmienić monit systemowy, zaleca się unikanie
używania monitów systemowych do kontrolowania zachowania modelu, jeśli
to możliwe. Zamiast tego należy polegać na systemach zewnętrznych w celu
zapewnienia takiego zachowania. Na przykład wykrywanie i zapobieganie
szkodliwym treściom powinno odbywać się w systemach zewnętrznych.

**3. Wdrożenie zabezpieczeń**

Należy wdrożyć system zabezpieczeń poza samym LLM. Chociaż szkolenie
modelu w zakresie określonych zachowań, takich jak nieujawnianie monitów
systemowych, może być skuteczne, nie gwarantuje to, że model zawsze
będzie się do nich stosował. Niezależny system, który może sprawdzać
wyniki w celu ustalenia, czy model działa zgodnie z oczekiwaniami, jest
lepszym rozwiązaniem niż instrukcje wyświetlane w monitach systemowych.

**4. Zapewnienie niezależności kontroli bezpieczeństwa od LLM**

Krytyczne kontrole, takie jak rozdzielenie uprawnień, sprawdzanie
ograniczeń autoryzacji i podobne, nie mogą być delegowane do LLM, ani
poprzez systemowe monity, ani w inny sposób. Kontrole te muszą odbywać
się w sposób deterministyczny i możliwy do audytu, a LLM nie sprzyjają
temu (obecnie). W przypadkach, gdy agent wykonuje zadania, które
wymagają różnych poziomów dostępu, należy użyć wielu agentów, z których
każdy jest skonfigurowany z minimalnymi uprawnieniami niezbędnymi do
wykonania pożądanych zadań.

**Przykładowe scenariusze ataku**

**Scenariusz nr 1**

LLM posiada monit systemowy zawierający zestaw poświadczeń używanych do
narzędzia, do którego uzyskał dostęp. Monit systemowy zostaje ujawniony
atakującemu, który następnie może wykorzystać te poświadczenia do innych
celów.

**Scenariusz nr 2**

LLM ma monit systemowy zabraniający generowania treści obraźliwych,
linków zewnętrznych i wykonywania kodu. Atakujący wyodrębnia ten monit
systemowy, a następnie wykorzystuje atak typu prompt injection, aby
ominąć te instrukcje, ułatwiając atak zdalnego wykonania kodu.

**Linki referencyjne**

[[SYSTEM PROMPT
LEAK]{.underline}](https://x.com/elder_plinius/status/1801393358964994062):
Pliny the prompter

[[Prompt
Leak]{.underline}](https://www.prompt.security/vulnerabilities/prompt-leak):
Prompt Security

[[chatgpt_system_prompt]{.underline}](https://github.com/LouisShark/chatgpt_system_prompt):
LouisShark

[[leaked-system-prompts]{.underline}](https://github.com/jujumilk3/leaked-system-prompts):
Jujumilk3

[[OpenAI Advanced Voice Mode System
Prompt]{.underline}](https://x.com/Green_terminals/status/1839141326329360579):
Green_Terminals

**Powiązane ramy i taksonomie**

W tej sekcji znajdują się wyczerpujące informacje, scenariusze i
strategie dotyczące wdrażania infrastruktury, stosowanych środków
kontroli środowiska i innych najlepszych praktyk.

[[AML.T0051.000 --- Wstrzyknięcie podpowiedzi LLM: bezpośrednie
(wyodrębnianie
meta-podpowiedzi)]{.underline}](https://atlas.mitre.org/techniques/AML.T0051.000)
**MITRE ATLAS**
