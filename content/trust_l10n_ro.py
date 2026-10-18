# -*- coding: utf-8 -*-
"""Traducerea în română (ro) a paginilor de încredere (Despre / Politica de
confidențialitate / Termeni de utilizare / Contact / Feedback).

Urmează structura din TRUST["en"] din trust_l10n.py: o intrare pentru fiecare
pagină, cu titlu, descriere meta și o listă ordonată de secțiuni —
["h", titlu secțiune], ["p", paragraf] sau ["li", element de listă]. Intrarea
de feedback conține și dicționarul "form", cu placeholder-e, butoane și
mesaje de stare.
"""

TRUST_LANG = {
    "about": {
        "title": "Despre Fxverter — convertor valutar gratuit și open-source",
        "desc": "Cine stă în spatele Fxverter, de ce există și ce îl face diferit: un convertor valutar open-source, orientat spre confidențialitate, cu cursuri de referință oneste și ghiduri pe înțelesul tuturor.",
        "sections": [
            ["p", "Fxverter este un convertor valutar online gratuit și open-source care rulează integral în browserul tău. Afișează cursuri de referință pentru peste 140 de valute din întreaga lume, nu necesită cheie API, cont sau instalare — deschizi site-ul și începi să convertești."],
            ["h", "De ce l-am construit"],
            ["p", "Majoritatea site-urilor de conversie îngroapă cursul real sub pop-up-uri, bariere de înregistrare și insistențe de instalare a aplicației. Noi am vrut exact opusul: o unealtă rapidă și privată, care arată mai întâi cursul mid-market de referință, onest, și apoi se retrage. Tot produsul este o singură pagină statică, care funcționează pe orice dispozitiv, în șapte limbi, chiar și offline după instalare."],
            ["h", "Ce îl face diferit"],
            ["li", "Fără cont, fără urmărire — conversiile rulează local în browserul tău"],
            ["li", "Trei surse publice de date, comutabile: Frankfurter (cursurile de referință ale Băncii Centrale Europene), ExchangeRate-API și Fawaz Currency API"],
            ["li", "40 de valute majore cu pagini dedicate: tabele de conversie în timp real, grafice de tendință pe 30/90 de zile și profiluri de valută"],
            ["li", "Ghiduri pe înțelesul tuturor, care explică cum funcționează de fapt cursurile de schimb"],
            ["li", "Poate fi instalat ca aplicație (PWA) care continuă să funcționeze offline, cu ultimele cursuri cunoscute"],
            ["h", "Datele"],
            ["p", "Cursurile sunt cursuri de referință orientative, din surse publice (bănci centrale și piețe), actualizate zilnic. Sunt același reper pe care îl vezi pe Google sau în știrile financiare — utile pentru comparații și planificare, nu o cotație contractuală pentru un transfer anume."],
            ["h", "Cine stă în spatele lui"],
            ["p", "Fxverter este construit și întreținut de un dezvoltator independent și susținut de utilizatorii săi. Codul sursă complet este public pe GitHub — oricine îl poate audita, îl poate găzdui singur sau poate contribui cu îmbunătățiri."],
            ["p", "Întrebări, corecturi sau idei? Scrie la <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a> — citim tot."],
        ],
    },
    "privacy": {
        "title": "Politica de confidențialitate | Fxverter",
        "desc": "Ce colectează și ce nu colectează Fxverter: fără cookie-uri obligatorii, fără conturi, doar statistici anonime — plus modul în care sunt gestionate publicitatea și serviciile terțe.",
        "sections": [
            ["p", "Fxverter este conceput pentru a putea fi folosit fără a prelua nicio informație personală. Această politică explică ce colectează și ce nu colectează site-ul, precum și modul în care sunt gestionate publicitatea și serviciile terțe. Ultima actualizare: septembrie 2026."],
            ["h", "Ce nu colectăm"],
            ["p", "Nu este necesar un cont, iar site-ul nu instalează el însuși cookie-uri de publicitate. Conversiile rulează local în browserul tău — nu vedem niciodată sumele sau perechile de valute pe care le convertești."],
            ["h", "Informații colectate automat"],
            ["p", "Pot fi colectate statistici anonime, agregate, privind vizitele (pagini vizualizate și țară, fără cookie-uri), pentru a înțelege utilizarea globală și a îmbunătăți unealta. Aceste statistici nu pot fi folosite pentru a te identifica."],
            ["h", "Informațiile pe care alegi să le trimiți"],
            ["p", "Dacă folosești formularul de feedback, numele, adresa de e-mail și mesajul trimise sunt folosite doar pentru a citi și a răspunde la feedbackul tău. Dacă susții proiectul, plata este procesată de Creem.io ca merchant of record — nu primim niciodată detaliile tale complete de plată. Susținătorii apar cu numele doar cu acordul lor explicit."],
            ["h", "Servicii terțe"],
            ["p", "Cursurile de schimb sunt preluate de browserul tău direct din API-uri publice (Frankfurter/BCE, ExchangeRate-API, Fawaz Currency API) — aceste cereri provin de pe dispozitivul tău, nu trec prin serverele noastre. Site-ul este găzduit ca fișiere statice, iar statisticile anonime pot rula prin Cloudflare."],
            ["h", "Publicitate"],
            ["p", "Acest site poate afișa publicitate difuzată prin Google AdSense. Furnizorii terți, inclusiv Google, folosesc cookie-uri și tehnologii similare pentru a difuza anunțuri pe baza vizitelor tale anterioare pe acest site sau pe alte site-uri. Utilizarea cookie-urilor de publicitate de către Google îi permite acestuia și partenerilor săi să îți difuzeze anunțuri pe baza vizitelor pe site-ul nostru și/sau pe alte site-uri de pe internet."],
            ["p", "Poți renunța la publicitatea personalizată din <a href=\"https://adssettings.google.com\" rel=\"noopener\">setările de anunțuri Google</a> sau poți refuza cookie-urile furnizorilor terți pe <a href=\"https://www.aboutads.info\" rel=\"noopener\">aboutads.info</a>. Acolo unde legea o cere — de exemplu în Spațiul Economic European și în Regatul Unit — publicitatea personalizată este afișată doar cu acordul tău, iar în rest se folosește publicitate nepersonalizată. Pentru detalii, vezi <a href=\"https://policies.google.com/technologies/ads\" rel=\"noopener\">cum folosește Google informațiile de pe site-urile care îi folosesc serviciile</a>."],
            ["h", "Stocarea locală"],
            ["p", "Alegerea temei, dimensiunea fontului, perechile de valute salvate și momentul afișării bannerului de instalare sunt stocate în memoria locală a browserului tău. Aceste date nu părăsesc niciodată dispozitivul și pot fi șterse oricând din setările browserului."],
            ["h", "Păstrarea datelor și drepturile tale"],
            ["p", "Mesajele de feedback sunt păstrate doar atât timp cât este necesar pentru a răspunde. Ne poți cere să ștergem orice feedback ai trimis, scriind la <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a>."],
            ["h", "Modificări ale acestei politici"],
            ["p", "Dacă practicile site-ului privind datele se schimbă, această pagină va fi actualizată, iar data de mai sus va fi revizuită. Utilizarea continuă a site-ului după o modificare înseamnă că accepți politica actualizată."],
        ],
    },
    "terms": {
        "title": "Termeni de utilizare | Fxverter",
        "desc": "Regulile de bază pentru folosirea Fxverter: cursurile sunt valori de referință orientative, nu cotații; serviciul este oferit ca atare; plus modul în care sunt gestionate răspunderea, proprietatea intelectuală și utilizarea acceptabilă.",
        "sections": [
            ["p", "Folosind fxverter.com, accepți acești termeni. Dacă nu ești de acord, te rugăm să nu folosești site-ul. Ultima actualizare: septembrie 2026."],
            ["h", "Serviciul"],
            ["p", "Fxverter este un convertor valutar online gratuit și open-source, oferit „ca atare” și „în funcție de disponibilitate”, fără garanții de niciun fel, exprese sau implicite — inclusiv privind acuratețea, disponibilitatea sau potrivirea pentru un anumit scop."],
            ["h", "Cursurile de schimb sunt doar orientative"],
            ["p", "Toate cursurile afișate sunt cursuri de referință, colectate din surse publice precum băncile centrale și API-uri valutare deschise, actualizate de regulă o dată pe zi. Ele sunt repere de comparație — nu cotații, nu sfaturi financiare și nu un preț pe care ți-l va oferi efectiv vreun furnizor. Nu le folosi pentru tranzacții financiare, transferuri bancare, facturare sau contabilitate oficială; verifică întotdeauna cursul cu banca sau instituția financiară ta înainte de orice tranzacție."],
            ["h", "Limitarea răspunderii"],
            ["p", "În cea mai mare măsură permisă de lege, întreținătorii Fxverter nu răspund pentru nicio pierdere sau daună rezultată din utilizarea sau imposibilitatea utilizării site-ului sau a datelor sale — inclusiv deciziile luate pe baza cursurilor afișate."],
            ["h", "Proprietate intelectuală"],
            ["p", "Codul sursă este open-source sub licența MIT și este disponibil pe GitHub. Textele, designul și marca site-ului rămân proprietatea proiectului Fxverter; nu poți republica conținutul site-ului în integralitate fără permisiune."],
            ["h", "Servicii terțe și linkuri"],
            ["p", "Site-ul se bazează pe API-uri publice ale unor terți și poate conține linkuri către site-uri ale unor terți. Nu le controlăm și nu răspundem de conținutul, disponibilitatea sau practicile lor."],
            ["h", "Utilizare acceptabilă"],
            ["p", "Te angajezi să nu perturbi serviciul, să nu încerci să-l suprasoliciți și să nu folosești unelte automate într-un mod care îl degradează pentru ceilalți vizitatori."],
            ["h", "Modificări ale acestor termeni"],
            ["p", "Acești termeni pot fi actualizați din când în când; versiunea în vigoare este întotdeauna această pagină. Întrebări? Scrie la <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a>."],
        ],
    },
    "contact": {
        "title": "Contact | Fxverter",
        "desc": "Cum contactezi echipa Fxverter: feedback, corecturi de cursuri, licențiere și presă — hello@fxverter.com sau formularul online de feedback.",
        "sections": [
            ["p", "Cel mai rapid mod de a ne contacta este e-mailul: <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a>. Citim fiecare mesaj și, de obicei, răspundem în câteva zile."],
            ["h", "Despre ce poți scrie"],
            ["li", "Feedback și idei de funcționalități — ce merge, ce nu merge, ce lipsește"],
            ["li", "Corecturi — dacă ceva pare greșit pe o pagină, spune-ne pe care"],
            ["li", "Întrebări despre licențiere și republicare"],
            ["li", "Solicitări de presă și parteneriate"],
            ["h", "Bug-uri și probleme de cod"],
            ["p", "Fxverter este open-source — rapoartele de bug-uri și pull request-urile sunt binevenite direct pe depozitul GitHub al proiectului, unde sunt publice și urmăribile."],
            ["h", "O precizare despre cursuri"],
            ["p", "Toate cursurile sunt valori de referință orientative, din surse publice, actualizate zilnic — vezi <a href=\"../guides/\">ghidurile</a> pentru ce înseamnă asta în practică. Înainte să scrii despre un curs „greșit”, compară-l te rog cu o a doua sursă la aceeași oră a zilei: diferențele mici dintre cursurile de referință și cotațiile furnizorilor sunt normale."],
            ["h", "Confidențialitate"],
            ["p", "Adresa ta de e-mail este folosită doar pentru a-ți răspunde — fără newsletter, fără marketing. Vezi <a href=\"../privacy/\">Politica de confidențialitate</a> pentru detalii."],
        ],
    },
    "feedback": {
        "title": "Trimite feedback | Fxverter",
        "desc": "Spune-ne ce merge, ce nu merge și ce lipsește — formularul de feedback Fxverter ajunge direct în inbox-ul echipei, fără cont.",
        "sections": [
            ["p", "Ai găsit un bug, un curs care pare ciudat sau o idee care ar face Fxverter mai util? Formularul de mai jos ajunge direct în inbox-ul nostru — fără cont, și îți ia cam treizeci de secunde."],
            ["h", "Ce ne ajută cel mai mult"],
            ["li", "Ce pagină sau funcționalitate foloseai"],
            ["li", "Ce te așteptai să se întâmple și ce s-a întâmplat de fapt"],
            ["li", "Browserul sau dispozitivul tău, dacă problema este vizuală"],
            ["h", "Preferi e-mailul?"],
            ["p", "Scrie la <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a> — sau folosește pur și simplu formularul de mai jos, ajunge în același loc."],
        ],
        "form": {
            "name": "Nume (opțional)",
            "email": "E-mail (opțional — doar dacă dorești un răspuns)",
            "message": "Mesajul tău",
            "send": "Trimite feedback",
            "ok": "✓ Feedback trimis — mulțumim!",
            "empty": "Scrie mai întâi un mesaj.",
            "fail": "Trimiterea a eșuat — scrie te rog direct la hello@fxverter.com.",
        },
    },
}

LABELS = {
    "about": "Despre noi",
    "privacy": "Confidențialitate",
    "terms": "Termeni de utilizare",
    "contact": "Contact",
}
