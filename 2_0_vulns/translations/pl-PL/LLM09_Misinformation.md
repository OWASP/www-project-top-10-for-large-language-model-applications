**LLM09:2025 Dezinformacja**

**Opis**

Dezinformacja pochodząca z modeli LLM stanowi podstawową lukę w
zabezpieczeniach aplikacji opartych na tych modelach. Dezinformacja
występuje, gdy modele LLM generują fałszywe lub wprowadzające w błąd
informacje, które wydają się wiarygodne. Luka ta może prowadzić do
naruszenia bezpieczeństwa, utraty reputacji i odpowiedzialności prawnej.

Jedną z głównych przyczyn dezinformacji są halucynacje --- sytuacja, w
której LLM generuje treści, które wydają się dokładne, ale są zmyślone.
Halucynacje występują, gdy modele LLM wypełniają luki w danych
szkoleniowych za pomocą wzorców statystycznych, nie rozumiejąc w pełni
treści. W rezultacie model może generować odpowiedzi, które brzmią
poprawnie, ale są całkowicie bezpodstawne. Chociaż halucynacje są
głównym źródłem dezinformacji, nie są jedyną przyczyną; przyczyniają się
do tego również uprzedzenia wprowadzone przez dane szkoleniowe i
niekompletne informacje.

Związaną z tym kwestią jest nadmierne poleganie. Nadmierne poleganie
występuje, gdy użytkownicy nadmiernie ufają treściom generowanym przez
LLM, nie weryfikując ich dokładności. Nadmierne poleganie pogłębia wpływ
dezinformacji, ponieważ użytkownicy mogą włączać nieprawidłowe dane do
krytycznych decyzji lub procesów bez odpowiedniej kontroli.

**Typowe przykłady ryzyka**

**1. Nieścisłości faktyczne**

Model generuje nieprawidłowe stwierdzenia, co prowadzi użytkowników do
podejmowania decyzji w oparciu o fałszywe informacje. Na przykład
chatbot linii lotniczych Air Canada przekazał podróżnym błędne
informacje, co doprowadziło do zakłóceń w działalności operacyjnej i
komplikacji prawnych. W rezultacie linie lotnicze zostały skutecznie
pozwane. (Link:
[[BBC]{.underline}](https://www.bbc.com/travel/article/20240222-air-canada-chatbot-misinformation-what-travellers-should-know))

**2. Niepoparte twierdzenia**

Model generuje bezpodstawne twierdzenia, które mogą być szczególnie
szkodliwe w wrażliwych kontekstach, takich jak opieka zdrowotna lub
postępowania prawne. Na przykład ChatGPT sfabrykował fałszywe sprawy
sądowe, co doprowadziło do poważnych problemów w sądzie. (Link:
[[LegalDive]{.underline}](https://www.legaldive.com/news/chatgpt-fake-legal-cases-generative-ai-hallucinations/651557/))

**3. Fałszywe przedstawianie wiedzy eksperckiej**

Model sprawia wrażenie, że rozumie złożone tematy, wprowadzając
użytkowników w błąd co do swojego poziomu wiedzy. Na przykład
stwierdzono, że chatboty fałszywie przedstawiają złożoność kwestii
związanych ze zdrowiem, sugerując niepewność tam, gdzie jej nie ma, co
wprowadza użytkowników w błąd i sprawia, że wierzą, iż niepotwierdzone
metody leczenia są nadal przedmiotem dyskusji. (Link:
[[KFF]{.underline}](https://www.kff.org/health-misinformation-monitor/volume-05/))

**4. Generowanie niebezpiecznego kodu**

Model sugeruje niebezpieczne lub nieistniejące biblioteki kodu, które po
zintegrowaniu z systemami oprogramowania mogą wprowadzać luki w
zabezpieczeniach. Na przykład modele LLM proponują użycie
niebezpiecznych bibliotek stron trzecich, które w przypadku zaufania bez
weryfikacji prowadzą do zagrożeń bezpieczeństwa. (Link referencyjny:
[[Lasso]{.underline}](https://www.lasso.security/blog/ai-package-hallucinations))

**Strategie zapobiegania i łagodzenia skutków**

**1. Generowanie wspomagane odzyskiwaniem (RAG)**

W celu zwiększenia wiarygodności wyników modelu należy stosować
generowanie wspomagane wyszukiwaniem, polegające na pobieraniu
odpowiednich i zweryfikowanych informacji z zaufanych zewnętrznych baz
danych podczas generowania odpowiedzi. Pomaga to ograniczyć ryzyko
halucynacji i dezinformacji.

**2. Dostrajanie modelu**

Model należy udoskonalić poprzez dostrajanie lub osadzanie w celu
poprawy jakości wyników. Techniki takie jak dostrajanie efektywne pod
względem parametrów (PET) i podpowiadanie łańcucha myśli mogą pomóc w
ograniczeniu występowania dezinformacji.

**3. Weryfikacja krzyżowa i nadzór ludzki**

Zachęcaj użytkowników do sprawdzania wyników LLM w zaufanych
zewnętrznych źródłach, aby zapewnić dokładność informacji. Wprowadź
procesy nadzoru ludzkiego i weryfikacji faktów, zwłaszcza w przypadku
informacji krytycznych lub wrażliwych. Upewnij się, że recenzenci są
odpowiednio przeszkoleni, aby uniknąć nadmiernego polegania na treściach
generowanych przez sztuczną inteligencję.

**4. Mechanizmy automatycznej walidacji**

Wprowadź narzędzia i procesy do automatycznej walidacji kluczowych
wyników, zwłaszcza wyników pochodzących ze środowisk o wysokim ryzyku.

**5. Komunikacja ryzyka**

Należy zidentyfikować ryzyko i potencjalne szkody związane z treściami
generowanymi przez LLM, a następnie jasno poinformować użytkowników o
tych ryzykach i ograniczeniach, w tym o potencjalnym ryzyku
dezinformacji.

**6. Bezpieczne praktyki kodowania**

Należy ustanowić bezpieczne praktyki kodowania, aby zapobiec integracji
luk w zabezpieczeniach spowodowanych nieprawidłowymi sugestiami kodu.

**7. Projektowanie interfejsu użytkownika**

Zaprojektuj interfejsy API i interfejsy użytkownika, które zachęcają do
odpowiedzialnego korzystania z modeli LLM, np. poprzez integrację
filtrów treści, wyraźne oznaczanie treści generowanych przez sztuczną
inteligencję oraz informowanie użytkowników o ograniczeniach dotyczących
wiarygodności i dokładności. Należy dokładnie określić ograniczenia
dotyczące przewidzianego zakresu zastosowania.

**8. Szkolenia i edukacja**

Zapewnij użytkownikom kompleksowe szkolenia dotyczące ograniczeń modeli
LLM, znaczenia niezależnej weryfikacji generowanych treści oraz potrzeby
krytycznego myślenia. W określonych kontekstach oferuj szkolenia
branżowe, aby użytkownicy mogli skutecznie oceniać wyniki modeli LLM w
swojej dziedzinie wiedzy.

**Przykładowe scenariusze ataków**

**Scenariusz nr 1**

Atakujący eksperymentują z popularnymi asystentami kodowania, aby
znaleźć często pojawiające się fałszywe nazwy pakietów. Po
zidentyfikowaniu często sugerowanych, ale nieistniejących bibliotek,
publikują złośliwe pakiety o tych nazwach w powszechnie używanych
repozytoriach. Programiści, polegając na sugestiach asystenta kodowania,
nieświadomie integrują te pakiety z oprogramowaniem. W rezultacie
atakujący uzyskują nieautoryzowany dostęp, wprowadzają złośliwy kod lub
tworzą tylne furtki, co prowadzi do poważnych naruszeń bezpieczeństwa i
ujawnienia danych użytkowników.

**Scenariusz nr 2**

Firma udostępnia chatbota do diagnostyki medycznej bez zapewnienia
wystarczającej dokładności. Chatbot dostarcza błędnych informacji, co
prowadzi do szkodliwych konsekwencji dla pacjentów. W rezultacie firma
zostaje skutecznie pozwana o odszkodowanie. W tym przypadku naruszenie
bezpieczeństwa nie wymagało udziału złośliwego atakującego, ale wynikało
z niewystarczającego nadzoru i niezawodności systemu LLM. W tym
scenariuszu nie ma potrzeby, aby firma była narażona na utratę reputacji
i straty finansowe z powodu aktywnych działań atakującego.

**Linki referencyjne**

[[Chatboty AI jako źródła informacji zdrowotnych: fałszywe
przedstawianie wiedzy
eksperckiej]{.underline}](https://www.kff.org/health-misinformation-monitor/volume-05/):
**KFF**

[[Błędne informacje chatbota Air Canada: co powinni wiedzieć
podróżni]{.underline}](https://www.bbc.com/travel/article/20240222-air-canada-chatbot-misinformation-what-travellers-should-know):
**BBC**

[[Fałszywe sprawy sądowe ChatGPT: halucynacje generatywnej sztucznej
inteligencji]{.underline}](https://www.legaldive.com/news/chatgpt-fake-legal-cases-generative-ai-hallucinations/651557/):
**LegalDive**

[[Zrozumieć halucynacje
LLM]{.underline}](https://towardsdatascience.com/llm-hallucinations-ec831dcd7786):
**Towards Data Science**

[[Jak firmy powinny informować użytkowników o ryzyku związanym z dużymi
modelami
językowymi?]{.underline}](https://techpolicy.press/how-should-companies-communicate-the-risks-of-large-language-models-to-users/):
**Techpolicy**

[[Serwis informacyjny wykorzystał sztuczną inteligencję do pisania
artykułów. Była to dziennikarska
katastrofa]{.underline}](https://www.washingtonpost.com/media/2023/01/17/cnet-ai-articles-journalism-corrections/):
**Washington Post**

[[Głębsze spojrzenie na halucynacje pakietów
AI]{.underline}](https://www.lasso.security/blog/ai-package-hallucinations):
**Lasso Security**

[[Jak bezpieczny jest kod generowany przez
ChatGPT?]{.underline}](https://arxiv.org/abs/2304.09655): **Arvix**

[[Jak ograniczyć halucynacje w dużych modelach
językowych]{.underline}](https://thenewstack.io/how-to-reduce-the-hallucinations-from-large-language-models/):
**The New Stack**

[[Praktyczne kroki w celu ograniczenia
halucynacji]{.underline}](https://newsletter.victordibia.com/p/practical-steps-to-reduce-hallucination):
**Victor Debia**

[[Struktura służąca do badania konsekwencji wiedzy przedsiębiorstwa
przekazywanej za pośrednictwem sztucznej
inteligencji]{.underline}](https://www.microsoft.com/en-us/research/publication/a-framework-for-exploring-the-consequences-of-ai-mediated-enterprise-knowledge-access-and-identifying-risks-to-workers/):
**Microsoft**

**Powiązane struktury i taksonomie**

W tej sekcji znajdą Państwo wyczerpujące informacje, scenariusze i
strategie dotyczące wdrażania infrastruktury, stosowanych środków
kontroli środowiska oraz inne najlepsze praktyki.

[[AML.T0048.002 -- Szkody
społeczne]{.underline}](https://atlas.mitre.org/techniques/AML.T0048)
**MITRE ATLAS**
