# Release candidate 6.6 RC1 (build 6.6.1)

Non pubblicare su main prima del collaudo. Per una preview usare un'origine HTTPS separata dalla produzione, con profilo fittizio; non usare credenziali reali. Testare login, dizionario, sei tappe, quiz, progressi, riapertura, offline, backup cifrato e ripristino, aggiornamento da 6.5.1 in ambiente isolato. Verificare anche tutti i link esterni. Nessun test iPhone end-to-end ancora certificato.

# AI Creator Academy 6.6.0 — Excellence Learning (sviluppo)

Dizionario IT e AI: 114 termini, ricerca, categorie e accesso da scelta corsi, dashboard e lezioni. Quiz avanzati: 264 domande contestualizzate con alternative tematiche e feedback; indici delle risposte corrette invariati. Controllo strutturale eseguito. Quiz base, verifica online delle risorse e collaudo browser/iPhone ancora da completare.

# AI Creator Academy 6.5.1 — Learning Introduction

Aggiunta la sezione Prima di iniziare in tutte le 264 sessioni. Creator: 120 introduzioni specifiche; Business: 48 spiegazioni settimanali con orientamento per studio, approfondimento e pratica. ID e attività invariati. Collaudo Safari da effettuare.

# AI Creator Academy 6.5.0 — Beta

Due percorsi: AI Creator & Developer (120 sessioni) e AI Business & Management (144 sessioni). Tutti i file sono nella radice, incluse le tre icone PNG. Pubblicare solo nel repository AI-Creator-Academy. Non caricare il file ZIP.

264 sessioni, due percorsi, ID conservati. Due domande per sessione: autoverifica precedente e domanda ricavata dalla masterclass settimanale (ripetuta nella settimana). Risposte e punteggio corrente nel profilo cifrato; riepilogo per corso. Non è un esame indipendente. Rivisitazione CSS e cache. PL-900 collegato al percorso italiano verificato tramite catalogo Microsoft; riscontri Make Foundation e Advanced nel catalogo, non verifica HTTP integrale. Gli altri link restano da verificare. Sintassi JS, ID, struttura delle risposte e integrità archivio controllati. Test browser bloccato da ERR_BLOCKED_BY_ADMINISTRATOR; persistenza reale, backup, offline e sicurezza non collaudati. Nessuna pubblicazione effettuata. Pubblicare esclusivamente in repository indipendente.

## 6.5.0 — Professional Design
Revisione di dashboard, selettore corsi, navigazione, lezioni, quiz e menu Pro. Percentuale lezione = attività spuntate / attività previste, arrotondata; distinta dal punteggio quiz e dalla conferma di fine sessione. Usa i progressi già salvati, senza migrazione. Curriculum invariati. Test statici e formula verificati; nuovo collaudo Safari necessario. Backup e installazione ancora da verificare.


### QA 6.6.1 — controlli eseguiti
- Sintassi JavaScript index.html e sw.js: superata.
- 114 termini univoci, ricerca simulata su cinque input.
- Validazione backup: quattro casi superati, inclusa compatibilità con dati precedenti senza assessment.
- Avanzamento lezione: sei stati da 0 a 100% verificati su dati simulati.
- Restano test browser/Safari, installazione PWA, offline, backup cifrato end-to-end, aggiornamento e verifica completa dei link.
