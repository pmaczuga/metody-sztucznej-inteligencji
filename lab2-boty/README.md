# BOTY INTERNETOWE


### SPIS TREŚCI

1. Cel ćwiczenia
2. Plan ćwiczenia
3. Wymagania wstępne
4. ELIZA, ALICE i inne boty
5. AIML (Artificial Intelligence Markup Language)
6. ALICE. Uruchomienie. Przykładowa sesja
7. Stworzenie własnego "mózgu" bota w AIML
8. Bibliografia


### CEL ĆWICZENIA

Celem ćwiczenia jest przybliżenie pojęcia i zagadnień związanych z tzw. botami internetowymi, czyli oprogramowaniem naśladującym pewne czynności człowieka. Ograniczymy się do tzw. chat-botów, których zadaniem jest imitacja rozmówcy, przeprowadzanie dialogu z człowiekiem lub innymi botami.


### PLAN ĆWICZENIA

1. Ściągnąć, zainstalować i uruchomić ProgramD.
2. Ściągnąć i zainstalować standardowe pliki w AIML-u, przeprowadzić przykładową rozmowę.
3. Stworzyć „pusty” plik mybot.aiml.
4. Uzupełnić go zgodnie z poleceniami w opisie i przetestować każde rozszerzenie.
5. Zbudować własnego bota naśladującego dziecko. Bot powinien mieć 20-30 wzorców w języku polskim.
6. Wstawić bota jako rozwiązanie zadania w moodlu.
7. Usunąć stworzone katalogi z ProgramD.


### WYMAGANIA WSTĘPNE

W trakcie przeprowadzania ćwiczenia wykorzystane zostaną:

- **Java 1.5.0**, do pobrania z http://java.sun.com
- **ProgramD**, interpreter języka **AIML**, pozwalający na załadowanie wzorców zachowania bota i przeprowadzania z nim sesji, do pobrania z http://programw.sourceforge.net/#Download_Program_W
- Zakłada się podstawową znajomość języka AIML, w tym celu pomocnym może okazać się http://www.pandorabots.com/pandora/pics/wallaceaimltutorial.html, pełna specyfikacja znajduje się na http://www.alicebot.org/TR/2005/WD-aiml/
- **Kod przykładowego bota** pobrany ze strony http://www.alicebot.org/downloads/sets.html


### ELIZA, ALICE I INNE BOTY

**ELIZA** była pierwszym słynnym programem komputerowym, którego zadaniem była symulacja sesji psychoanalitycznej. W istocie jest to prosty algorytm polegający na powtarzaniu informacji dostarczonej przez użytkownika w formie nowego pytania. W najprostszej wersji algorytm podstawia słowa kluczowe pojawiające się we frazie użytkownika do ustalonych szablonów pytań zadawanych przez maszynę. Program ELIZA działał bardzo przekonująco dla wielu ludzi, którzy dali się uwieść tzw. efektowi ELIZA polegającemu na przypisywaniu znaczenia przez człowieka symbolom, które dla maszyny są jedynie przedmiotem analizy symbolicznej.  
Więcej informacji na temat ELIZY znaleźć można na:  
http://www.alicebot.org/articles/wallace/eliza.html.  
Na drugim biegunie znajduje się **ALICE** (www.alicebot.org) będąc jedną z najbardziej popularnych technologii do tworzenia chat-botów. Do budowania wiedzy bota wykorzystuje się język AIML (następny punkt). Podstawowymi częściami projektu są interpretery języka AIML oraz komponenty AIML definiujące zachowanie bota. Boty budowane w oparciu o technologię zaproponowaną przez twórców ALICE charakteryzują się dużymi możliwościami dostosowywania. W ramach projektu wolnodostępne są standardowy zbiór AIML określający typowe zachowania oraz specyficzne komponenty wiedzy (geografia, gotowanie, film, ekonomia) (http://www.alicebot.org/downloads/sets.html).  
Obecnie w sieci można znaleźć wiele chat-botów (por. forum dla tego tematu). Katalogi dostępne są w poniższych lokalizacjach:  
http://www.alicebot.org/directory.html  
http://dmoz.org/Computers/Artificial_Intelligence/Natural_Language/Chatterbots/  
 
 
### AIML (ARTIFICIAL INTELLIGENCE MARKUP LANGUAGE)

#### WSTĘP

AIML jest językiem składniowo opartym na XML, służącym do definiowania wiedzy chat-botów.  
Podstawową jednostką wiedzy w AIML jest kategoria, składająca się z pytania zwanego wzorcem (ang. pattern) i odpowiedzi nazywanej szablonem (ang. template) oraz opcjonalnego kontekstu.  
........................  
Wprowadzenie do języka znaleźć można na:  
http://www.pandorabots.com/pandora/pics/wallaceaimltutorial.html  
Specyfikacja języka znajduje się tutaj:  
http://www.alicebot.org/TR/2005/WD-aiml/


### ALICE. URUCHOMIENIE, PRZYKŁADOWA SESJA

Aktualną wersją interpretera języka AIML tworzonego w ramach projektu ALICE jest tzw. **ProgramD**, który pobrać można z http://programw.sourceforge.net/#Download_Program_W  
Wszystkie ścieżki podawane są względem katalogu programu po rozpakowaniu archiwum, np. conf oznacza, że pełna ścieżka może wyglądać tak: _C:\ProgramD\conf_  .
Aby uruchomić program należy wykorzystać skrypty startowe w katalogu bin. Dostępne są 3 możliwości:

- _simple-console(.bat)_ - startuje sesję w konsoli
- _simple-gui-console(.bat)_ - sesja przeprowadzana jest w trybie graficznym
- _web-server(.bat)_ - prosty web server, dostęp przez przeglądarkę, domyślnie na porcie 2001

W tym ćwiczeniu wykorzystamy prostą konsolę tekstową. Bezpośrednio po wpisaniu _simple-console(.bat)_ pojawi się znak zachęty do rozmowy z botem (trzeba jednak wcześniej ustawić zmienną środowiskową JAVA_HOME tak, by wskazywała na jdk). Niestety, bot nie będzie miał wiele do powiedzenia, ponieważ nie została załadowana żadna baza wiedzy. Aby tego dokonać można wykorzystać darmowe komponenty, dostępne http://aitools.org/Free_AIML_sets. Zakładając, że pliki z archiwum zostały umieszczone w katalogu _resources\testing\standard_ należy zmodyfikować plik _conf\bots.xml_ wpisując w znaczniku _<learn>_ taką ścieżkę:  
_<learn>../resources/testing/standard/*.aiml</learn>_
W pliku tym definiowane są boty obsługiwane przez kontener. Można zmienić domyślną nazwę bota (atrybut id znacznika bot).
Teraz, uruchamiając ProgramD ponownie, można rozpocząć rozmowę z botem wyposażonym w "mózg". Pełen opis konfiguracji programu dostępny jest pod adresem:
http://programw.sourceforge.net/#Configuration.2FDeployment  
lub w pliku _readme.html_ znajdującym się w katalogu głównym programu.  
W kolejnym punkcie zajmiemy się zdefiniowaniem własnego "mózgu" bota.


### STWORZENIE WŁASNEGO "MÓZGU" BOTA W AIML

Ćwiczenie polega na stworzeniu zbioru *.aiml, który stanowiłby prosty "mózg" bota. Celem ćwiczenia nie jest opracowanie spójnego i sensownego zachowania bota, ale raczej prezentacja możliwości języka AIML. Rezultatem wykonania poniższych zadań powinna być ogólna orientacja w technikach stosowanych w procesie tworzenia chat-botów.

#### Szkielet AIML bota

W tym celu utworzymy plik o nazwie _resources/testing/mybot.aiml_ zgodnie z poniższym wzorcem:
```
<?xml version="1.0" encoding="ISO-8859-1"?>
<aiml version="1.0.1" xmlns="http://alicebot.org/2001/AIML-1.0.1"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xsi:schemaLocation="http://alicebot.org/2001/AIML-1.0.1
http://aitools.org/aiml/schema/AIML.xsd">

</aiml>
```

W dalszej kolejności będziemy wypełniać go treścią, umieszczaną w obrębie głównego znacznika _aiml_.


#### Ładowanie bota

Aby zbiór ten mógł być przetwarzany przez interpreter umieszczamy ścieżkę do niego w pliku _conf/bots.xml_, w znaczniku _<learn>_ naszego bota:  
_<learn>../resources/testing/mybot.aiml</learn>_  
Pozostałe znaczniki _<learn>_ powinny zostać usunięte lub wykomentowane.  
Aby nie restartować programu interpretera po każdej zmianie wprowadzonej w _mybot.aiml_ można uruchomić tzw. _AIMLWatcher_, który z określoną częstotliwością będzie badał czy plik _mybot.aiml_ nie został zmodyfikowany i w razie konieczności ładował go ponownie. Można to osiągnąć modyfikując plik _conf/core.xml_. W obrębie znacznika  
_<entry key="programd.use-watcher">false</entry>_  
należy zmienić wartość _false_ na _true_.
Poniższy znacznik pozwala ustawić interwał czasowy z jakim interpreter testuje zbiory aiml ładowane za pomocą znacznika _<learn>_.  
_<entry key="programd.watcher.timer">2000</entry>_
Dla naszych potrzeb wartość 2s będzie wystarczająca.

**Od kilku wersji powyższy mechanizm nie działa. Gdyby komuś udało się znaleźć rozwiązanie tego problemu, proszę dać znać na forum.**


#### "Hello World" w AIML

Po opisanej zmianie możemy w konsoli wystartować program interpretera przy użyciu skryptu _bin/simple-console(.bat)_ i ostatecznie zająć się tworzeniem zawartości "mózgu" bota.  
Zaczniemy od zdefiniowania prostej kategorii (należy ją umieścić w obrębie znacznika _aiml)_:  
```
<category>
<pattern>Czesc</pattern>
<template>Witaj</template>
</category>
```

W ten prosty sposób można definiować bezpośrednie reakcje werbalne bota na wprowadzenie ściśle określonej frazy, bot potrafi zareagować odpowiedzią _Witaj_ na ciąg wejściowy _Czesc_.


#### Synonimy

Język AIML posiada bardziej wyrafinowane mechanizmy definiowania bazy wiedzy botów. Np. naturalnym oczekiwaniem jest, aby bot potrafił odpowiedzieć przywitaniem na inne frazy wejściowe. _AIML 1.01_ nie pozwala na osadzanie więcej niż jednego wzorca w ramach jednej kategorii, ale możemy to osiągnąć przy użyciu mechanizmu _synonimów_:
```
<category>
<pattern>Dzien dobry</pattern> 
<template><srai>Czesc</srai></template>
</category>
<category>
<pattern>Witaj</pattern> 
<template><srai>Czesc</srai></template>
</category>
<category>
<pattern>Dobry wieczor</pattern> 
<template><srai>Czesc</srai></template>
</category>
```

Uwaga! Aby przykład działał, w pliku musi być obecny wzorzec z poprzedniej ramki.


#### Redukcja symboliczna

Innym istotnym elementem wbudowanym w język jest _redukcja symboliczna_. Zabieg ten pozwala sprowadzić złożone formy zdaniowe do prostszych przy użyciu znacznika _<srai>_. Typowym zastosowaniem jest poniższa transformacja:
```
<category>
<pattern>Czym jest hipopotam</pattern>
<template>Zwierzeciem</template>
</category>
<category>
<pattern>Czy wiesz czym jest * </pattern>
<template><srai>Czym jest <star/></srai></template>
</category>
```

Formuła _Czy wiesz czym jest *_ sprowadzona zostaje do formuły _Czym jest *_. Obecnie, zadając pytanie _Czy wiesz czym jest hipopotam ?_ oraz _Czym jest hipopotam ?_ otrzymamy jednakową odpowiedź: _Zwierzeciem_.


#### Podział

Użyteczną jest możliwość rozbijania wzorców na fragmenty, dopasowywanie odpowiedzi do każdej z części wzorca oraz złożenie tych fragmentów w całościową odpowiedź. Wprowadźmy następujący zbiór kategorii:
```
<category>
<pattern>Papuga jest ptakiem</pattern>
<template>tak</template>
</category>
<category>
<pattern>Wieloryb jest ryba</pattern>
<template>nie</template>
</category>
<category>
<pattern>Czy *</pattern>
<template>Sadze, ze <srai><star/></srai></template>
</category>
```

Dwie pierwsze kategorie są atomowe, natomiast trzecia pozwala wydzielić w zdaniu o konstrukcji Czy _papuga jest ptakiem_ słowo _Czy_ i dopasować do niego frazę _Sadze, ze_, natomiast do drugiej części wzorca, dzięki zastosowaniu znacznika _<srai>_ dopasowana zostaje odpowiedź zapisana w innej kategorii, w wyniku czego otrzymamy całościową odpowiedź _Sadze, ze tak_.


#### Słowa kluczowe

Efekt wykorzystany w programie ELIZA polega na tym, żeby wywołać u użytkownika wrażenie zrozumienia przez bota poprzez nawiązywanie do tematu na podstawie identyfikacji określonych _słów kluczowych_. AIML również umożliwia wykorzystanie słów kluczowych w następujący sposób:
```
<category>
<pattern>kon</pattern> 
<template>Interesujesz sie jezdziectwem ?</template>
</category>
<category>
<pattern>_ kon</pattern> 
<template><srai>kon</srai></template>
</category>
<category>
<pattern>kon _</pattern>
<template><srai>kon</srai></template>
</category>
<category>
<pattern>_ kon *</pattern>
<template><srai>kon</srai></template>
</category>
```

Kolejne kategorie odpowiedzialne są za identyfikację słowa kluczowego kon, odpowiednio jako prefiksu, sufiksu oraz infiksu w zdaniu wejściowym. Następnie bot zadaje pytanie skojarzone ze słowem kluczowym.


#### Kontekst: <that>

Ważnym elementem języka AIML jest tzw. kontekst, pozwala on rozróżnić pomiędzy kategoriami w przypadku jednakowego wzorca. Znajduje to zastosowanie szczególnie w przypadku częstych, jednakowych zdań użytkownika posiadających różne znaczenie (z uwagi na różny kontekst). Np. odpowiedzi _tak/nie_ udzielane przez użytkownika na różne pytania powinny skutkować różnymi reakcjami bota, uzależnionymi od pytania, na które padła dana odpowiedź. Oto przykład wykorzystania:
```
<category>
<pattern>Lubie zwierzeta</pattern>
<template>Jakie najbardziej ?</template>
</category>
<category>
<pattern>Lubie zwierzeta</pattern>
<that>Dlaczego nie lubisz zwierzat</that>
<template>Jestes niezdecydowany ...</template>
</category>
<category>
<pattern>Nie lubie zwierzat</pattern>
<template>Dlaczego nie lubisz zwierzat?</template>
</category>
```

Przykład ten obrazuje zastosowanie znacznika _<that>_. Jeśli pojawia się ze strony użytkownika stwierdzenie _Lubie zwierzeta_ to odpowiedź zależy od tego czy bezpośrednio poprzedzającym stwierdzeniem użytkownika było zdanie _Nie lubie zwierzat_ czy jakieś inne. Bot, odpowiednio, informuje użytkownika o jego braku zdecydowania lub zadaje pytanie o ulubione zwierzęta.


#### Predykaty

AIML pozwala na wykorzystanie _predykatów_ w sekcji _\<template>_ kategorii, dzięki czemu łatwiej sterować przebiegiem konwersacji. W celu wykorzystania predykatu definiujemy go w pliku _conf/predicates.xml_ dodając linijkę:

```
<predicate name="to" default="something" set-return="name"/>
```

Następnie możemy wykorzystać predykat o nazwie to w poniższym przykładzie:
```
<category>
<pattern>Uwazam ze *</pattern>
<template>Dlaczego tak myslisz</template>
</category>
<category>
<pattern>*</pattern>
<that>Dlaczego tak myslisz</that>
<template>
Nie sadze, zeby <set name="to"><star/></set> bylo wystarczajacym wyjasnieniem. Czy naprawde uwazasz, ze '<get name="to"/>' wystarczy ?
</template>
</category>
```

Użytkownik wypowiada opinię rozpoczynającą się słowami _Uwazam ze_, na co reakcją jest pytanie bota _Dlaczego tak myslisz_. Uzasadnienie opinii, przykładowo '_bo tak_' zostaje dopasowane poprzez wzorzec * ponieważ następuje bezpośrednio po pytaniu bota _Dlaczego tak myslisz_ (znacznik _<that>_). Znacznik _<set>_ przypisuje predykatowi to wartość będącą uzasadnieniem i zwraca jednocześnie w miejscu przypisania swoją nazwę, co wynika z określenia predykatu _set-return="name"_. W drugim zdaniu odpowiedzi znacznik _<get>_ pobiera wartość predykatu i umieszcza w miejscu, w którym sam się znajduje. Efektem jest uzyskanie odpowiedzi _Nie sadze, żeby to było wystarczającym wyjaśnieniem. Czy naprawde uwazasz, ze 'bo tak' wystarczy ?_
Warto w pliku _conf/substitutions.xml_ dodać _podstawienia_ (jeśli jeszcze ich nie ma):
```
<substitute find="," replace=" "/>
<substitute find=", " replace=" "/>
```

które pozwolą na dopasowanie innych wariantów formuły użytkownika wyrażającej początkową opinię: _Uwazam, ze_ oraz _Uwazam,ze_ (przecinek i przerwa).


#### Kontekst: \<topic>

Innym przykładem wykorzystania _kontekstu_ jest znacznik _<topic>_. Obejmuje kilka kategorii. Temat dalszej konwersacji z botem zostaje ustalony w wyniku dopasowania odpowiedniego wzorca. Od tego momentu dopasowania w sekcji <topic> uzyskują pierwszeństwo. Zostało to zobrazowane na poniższym przykładzie:
```
<topic name="ZWIERZAKI">
<category>
<pattern>Zwierzeta *</pattern>
<template>
<random>
<li>Boisz sie dzikich zwierzat ?</li>
<li>Jakiego zwierzecia najbardziej nie lubisz ?</li>
<li>Jakie zwierze najbardziej lubisz ?</li>
</random>
</template>
</category>
<category>
<pattern>*</pattern>
<template>Jaki to ma zwiazek ze zwierzetami ?</template>
</category>
<category>
<pattern>Nie mam ochoty na ten temat rozmawiac</pattern>
<template><think><set name="topic">*</set></think>W porzadku, nie rozmawiajmy o zwierzetach</template>
</category>
</topic>
<category>
<pattern>Zwierzeta *</pattern>
<template>Zwierzeta to istoty zywe</template>
</category>
<category>
<pattern>Interesujesz sie zwierzetami</pattern>
<template><think><set name="topic">ZWIERZAKI</set></think>Owszem, chetnie o nich porozmawiam</template>
</category>
```

Część kategorii należy do tematu o nazwie _ZWIERZAKI_. Początkowo dopasowywane są wzorce spoza tego tematu, i tak na stwierdzenie użytkownika aktywujące wzorzec _Zwierzęta *_ otrzymamy odpowiedź _Zwierzęta to istoty zywe_, nie należącą do żadnego tematu. Gdy użytkownik zada pytanie _Interesujesz się zwierzętami_, bot aktywuje temat _ZWIERZAKI_, którego kategorie od tej pory, jako obowiązującego tematu rozmowy, będą miały pierwszeństwo przy dopasowaniach i odpowie na pytanie użytkownika +Owszem, chetnie o nich porozmawiam_. Znacznik _<think>_ użyty jest w celu powstrzymania programu od wypisania na wyjście nazwy tematu. Po zmianie tematu (kontekstu) to samo stwierdzenie użytkownika aktywujące wzorzec _Zwierzęta *_ zostanie dopasowane do szablonu znajdujące się wewnątrz sekcji _<topic>_, czego rezultatem będzie wylosowanie jednego z trzech powyższych pytań. Inne stwierdzenia kwitowane będą reakcją bota _Jaki to ma związek ze zwierzętami ?_ z wyjątkiem frazy _Nie mam ochoty na ten temat rozmawiac._ Skutkiem będzie powrót do tematu _ogólnego_ i uprzejma odpowiedź _W porządku, nie rozmawiajmy o zwierzetach._


#### Wyrażenie warunkowe

Ostatni przykład prezentuje wykorzystanie _wyrażenia warunkowego_ w kombinacji z _tematem_:
```
<category>
<pattern>*</pattern>
<template>
Naprawde tak myslisz ?
<think><set name="topic">WKOLO</set></think>
</template>
</category>
<topic name="WKOLO">
<category>
<pattern>*</pattern>
<template>
<think><set name="var"><uppercase><star /></uppercase></set></think>
<condition>
<li name="var" value="TAK">
Przyznajesz sie.
<think><set name="topic">*</set></think>
</li>
<li name="var" value="NIE">
Wypierasz sie.
<think><set name="topic">*</set></think>
</li>
<li>Tak czy nie ?</li>
</condition>
</template>
</category>
</topic>
```

Dowolna fraza użytkownika spotyka się z pytaniem bota _Naprawdę tak myślisz ?_ oraz ustawieniem tematu _WKOLO_. W tym temacie znajduje się jedna kategoria zawierająca w sekcji _\<template>_ wyrażenie warunkowe _\<condition>_ z listą wariantów _\<li>_. Każda fraza użytkownika zostanie dopasowana przez gwiazdkę i pytanie bota _Tak czy Nie ?_ będzie powtarzane dopóki użytkownik nie udzieli jednej z tych odpowiedzi. Po udzieleniu odpowiedzi _Tak_ albo _Nie_ przez użytkownika bot zwróci odpowiednio ciąg _Przyznajesz sie_ bądź _Wypierasz sie_ i powróci do tematu _ogólnego_.


### BIBLIOGRAFIA

- A.L.I.C.E. Artificial Intelligence Foundation
- aitools.org
- Pandorabots
