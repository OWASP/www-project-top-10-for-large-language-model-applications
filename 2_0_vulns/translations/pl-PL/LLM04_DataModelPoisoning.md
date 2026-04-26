**LLM04: Zatruwanie danych i modeli**

**Opis**

Zatruwanie danych występuje, gdy dane wykorzystywane do wstępnego
szkolenia, dostrajania lub osadzania są manipulowane w celu wprowadzenia
luk w zabezpieczeniach, tylnych drzwi lub stronniczości. Manipulacja ta
może zagrozić bezpieczeństwu modelu, jego wydajności lub etycznemu
działaniu, prowadząc do szkodliwych wyników lub upośledzenia możliwości.
Typowe zagrożenia obejmują pogorszenie wydajności modelu, stronnicze lub
toksyczne treści oraz wykorzystanie systemów niższego szczebla.

Zatrucie danych może dotyczyć różnych etapów cyklu życia LLM, w tym
wstępnego szkolenia (uczenia się na podstawie danych ogólnych),
dostrajania (dostosowywania modeli do konkretnych zadań), osadzania
(konwersji tekstu na wektory numeryczne) i uczenia transferowego
(ponownego wykorzystania wstępnie przeszkolonego modelu do nowego
zadania). Zrozumienie tych etapów pomaga zidentyfikować miejsca, w
których mogą pojawić się luki w zabezpieczeniach. Zatruwanie danych jest
uważane za atak na integralność, ponieważ manipulowanie danymi
szkoleniowymi wpływa na zdolność modelu do dokonywania dokładnych
prognoz. Ryzyko jest szczególnie wysokie w przypadku zewnętrznych źródeł
danych, które mogą zawierać niezweryfikowane lub złośliwe treści.

Ponadto modele dystrybuowane za pośrednictwem wspólnych repozytoriów lub
platform open source mogą nieść ze sobą ryzyko wykraczające poza
zatruwanie danych, takie jak złośliwe oprogramowanie osadzone za pomocą
technik takich jak złośliwe pickling, które może wykonać szkodliwy kod
po załadowaniu modelu. Należy również wziąć pod uwagę, że zatrucie może
umożliwić wdrożenie backdoora. Takie backdoory mogą pozostawić
zachowanie modelu niezmienione, dopóki pewien czynnik wyzwalający nie
spowoduje jego zmiany. Może to utrudnić testowanie i wykrywanie takich
zmian, tworząc w efekcie możliwość przekształcenia modelu w „śpiącego
agenta".

**Typowe przykłady podatności**

Złośliwi aktorzy wprowadzają szkodliwe dane podczas szkolenia, co
prowadzi do stronniczych wyników. Techniki takie jak „Split-View Data
Poisoning" lub „Frontrunning Poisoning" wykorzystują dynamikę szkolenia
modelu, aby to osiągnąć. (Link referencyjny: [[Split-View Data
Poisoning]{.underline}](https://github.com/GangGreenTemperTatum/speaking/blob/main/dc604/hacker-summer-camp-23/Ads%20_%20Poisoning%20Web%20Training%20Datasets%20_%20Flow%20Diagram%20-%20Exploit%201%20Split-View%20Data%20Poisoning.jpeg))
(Link referencyjny: [[Frontrunning
Poisoning]{.underline}](https://github.com/GangGreenTemperTatum/speaking/blob/main/dc604/hacker-summer-camp-23/Ads%20_%20Poisoning%20Web%20Training%20Datasets%20_%20Flow%20Diagram%20-%20Exploit%202%20Frontrunning%20Data%20Poisoning.jpeg))

Atakujący mogą wprowadzać szkodliwe treści bezpośrednio do procesu
szkolenia, zagrażając jakości wyników modelu.

Użytkownicy nieświadomie wprowadzają poufne lub zastrzeżone informacje
podczas interakcji, które mogą zostać ujawnione w kolejnych wynikach.

Niezweryfikowane dane szkoleniowe zwiększają ryzyko stronniczych lub
błędnych wyników.

Brak ograniczeń dostępu do zasobów może umożliwić wprowadzenie
niebezpiecznych danych, co spowoduje stronnicze wyniki.

**Strategie zapobiegania i ograniczania skutków**

Śledź pochodzenie i transformacje danych za pomocą narzędzi takich jak
OWASP CycloneDX lub ML-BOM i wykorzystaj narzędzia takie jak
[[Dyana]{.underline}](https://github.com/dreadnode/dyana) do
przeprowadzania dynamicznej analizy oprogramowania stron trzecich.
Weryfikuj legalność danych na wszystkich etapach rozwoju modelu.

Rygorystycznie sprawdzaj dostawców danych i weryfikuj wyniki modelu w
oparciu o zaufane źródła, aby wykryć oznaki zatrucia.

Wprowadź ścisłą izolację w celu ograniczenia ekspozycji modelu na
niezweryfikowane źródła danych. Wykorzystaj techniki wykrywania
anomalii, aby odfiltrować dane wrogie.

Dostosuj modele do różnych przypadków użycia, wykorzystując konkretne
zestawy danych do precyzyjnego dostrojenia. Pomaga to uzyskać
dokładniejsze wyniki w oparciu o zdefiniowane cele.

Zapewnij wystarczające kontrole infrastruktury, aby uniemożliwić
modelowi dostęp do niezamierzonych źródeł danych.

Używaj kontroli wersji danych (DVC) do śledzenia zmian w zestawach
danych i wykrywania manipulacji. Wersjonowanie ma kluczowe znaczenie dla
zachowania integralności modelu.

Przechowuj informacje dostarczone przez użytkowników w bazie danych
wektorowej, co pozwala na wprowadzanie zmian bez konieczności ponownego
szkolenia całego modelu.

Przetestuj odporność modelu za pomocą kampanii red team i technik
przeciwników, takich jak uczenie federacyjne, aby zminimalizować wpływ
zakłóceń danych.

Monitoruj straty podczas szkolenia i analizuj zachowanie modelu pod
kątem oznak zatrucia. Używaj progów do wykrywania nietypowych wyników.

Podczas wnioskowania zintegruj generowanie rozszerzone o odzyskiwanie
(RAG) i techniki uziemienia, aby zmniejszyć ryzyko halucynacji.

**Przykładowe scenariusze ataków**

**Scenariusz nr 1**

Atakujący wpływa na wyniki modelu, manipulując danymi szkoleniowymi lub
stosując techniki wstrzykiwania poleceń, rozpowszechniając w ten sposób
dezinformację.

**Scenariusz nr 2**

Toksyczne dane bez odpowiedniego filtrowania mogą prowadzić do
szkodliwych lub stronniczych wyników, propagując niebezpieczne
informacje.

**Scenariusz nr 3**

Złośliwy podmiot lub konkurent tworzy sfałszowane dokumenty do
szkolenia, co powoduje, że wyniki modelu odzwierciedlają te
nieścisłości.

**Scenariusz nr 4**

Niewystarczające filtrowanie pozwala atakującemu na wstawianie mylących
danych za pomocą wstrzyknięcia poleceń, co prowadzi do sfałszowania
wyników.

**Scenariusz nr 5**

Atakujący wykorzystuje techniki zatrucia, aby wstawić do modelu
wyzwalacz backdoor. Może to narazić Państwa na obejście
uwierzytelniania, wyciek danych lub wykonanie ukrytych poleceń.

**Linki referencyjne**

1.  [[Jak ataki zatrucia danych niszczą modele uczenia
    maszynowego]{.underline}](https://www.csoonline.com/article/3613932/how-data-poisoning-attacks-corrupt-machine-learning-models.html):
    **CSO Online**

2.  [[MITRE ATLAS (framework) Tay
    Poisoning]{.underline}](https://atlas.mitre.org/studies/AML.CS0009/):
    **MITRE ATLAS**

3.  [[PoisonGPT: Jak ukryliśmy lobotomizowany LLM w Hugging Face, aby
    rozpowszechniać fałszywe
    wiadomości]{.underline}](https://blog.mithrilsecurity.io/poisongpt-how-we-hid-a-lobotomized-llm-on-hugging-face-to-spread-fake-news/):
    **Mithril Security**

4.  [[Zatruwanie modeli językowych podczas
    instruktażu]{.underline}](https://arxiv.org/abs/2305.00944): **Arxiv
    White Paper 2305.00944**

5.  Zatruwanie zbiorów danych szkoleniowych w skali internetowej --
    Nicholas Carlini \| Stanford MLSys #75: **Seminaria Stanford MLSys
    -- film na YouTube**

6.  Repozytoria modeli ML: kolejny duży cel ataków na łańcuch dostaw
    **OffSecML**

7.  Naukowcy zajmujący się danymi na celowniku złośliwych modeli ML
    Hugging Face z cichym backdoorem **JFrog**

8.  Ataki typu backdoor na modele językowe: **W kierunku nauki o
    danych**

9.  [[Nigdy nie ma chwili na dill: Wykorzystanie plików pickle uczenia
    maszynowego]{.underline}](https://blog.trailofbits.com/2021/03/15/never-a-dill-moment-exploiting-machine-learning-pickle-files/)
    **TrailofBits**

10. [[arXiv:2401.05566 Śpiący agenci: Szkolenie zwodniczych modeli LLMs,
    które przetrwają szkolenia z zakresu
    bezpieczeństwa]{.underline}](https://www.anthropic.com/news/sleeper-agents-training-deceptive-llms-that-persist-through-safety-training)
    **Anthropic (arXiv)**

11. [[Ataki typu backdoor na modele
    AI]{.underline}](https://www.cobalt.io/blog/backdoor-attacks-on-ai-models)
    **Cobalt**

**Powiązane frameworki i taksonomie**

W tej sekcji znajdują się wyczerpujące informacje, scenariusze i
strategie dotyczące wdrażania infrastruktury, stosowanych środków
kontroli środowiska i innych najlepszych praktyk.

[[AML.T0018 \| Model ML z tylnymi
drzwiami]{.underline}](https://atlas.mitre.org/techniques/AML.T0018)
**MITRE ATLAS**

[[NIST AI Risk Management
Framework]{.underline}](https://www.nist.gov/itl/ai-risk-management-framework):
Strategie zapewnienia integralności AI. **NIST**

[[ML07:2023 Atak wykorzystujący transfer
wiedzy]{.underline}](https://owasp.org/www-project-machine-learning-security-top-10/docs/ML07_2023-Transfer_Learning_Attack)
**OWASP Machine Learning Security Top Ten**
