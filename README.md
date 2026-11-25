# AI Creator Academy — Excellence Learning 6.6 / 6.6.1 (sviluppo)

## Stato operativo corrente — 25 novembre 2026

Produzione: main 6.5.1; RC1: release-candidate-6.6-rc1, da preservare; sviluppo: excellence-learning-6.6. Nessuna autorizzazione al rilascio. Il [registro permanente ROADMAP.md](ROADMAP.md) contiene evidenze, cronologia, protocollo e prossimo intervento.

| Percorso | Sessioni | Quiz base revisionati | Quiz avanzati revisionati |
|---|---:|---:|---:|
| Creator & Developer | 120 | 120/120 | 120/120 |
| Business & Management | 144 | 144/144 | 36/144 |
| Totale | 264 | 264/264 | 156/264 |

Ultimo commit applicativo: `68e427bc3b1dda934749418304928fb4a25e191f`. Verifica statica: 72 settimane, 264 ID univoci, 528 testi di domanda distinti, 1584 feedback presenti; 420/528 quiz con tre feedback distinti (79,55%). Restano 108 quiz avanzati Business e 324 feedback da revisionare. Il blocco Business avanzato settimane 13–18 è sospeso. L'indicatore non certifica la qualità pedagogica indipendente né il completamento dell'intero progetto.

Introduzioni delle 264 sessioni e dizionario di 114 termini risultano implementati secondo la documentazione storica. Restano audit qualitativo delle lezioni, verifica integrale delle risorse e accessibilità dei corsi, collaudi browser/Safari/iPhone, PWA, offline/cache, backup cifrato e ripristino, migrazione e aggiornamento effettivi, sicurezza e approvazione utente. I controlli statici e simulati storici non equivalgono a collaudi end-to-end. Nessun merge, ZIP o pubblicazione senza approvazione; preservare main, RC1, ID, attività, indici, progressi e migrazione.

## Direzione strategico-didattica approvata

Direzione approvata dall'utente: conservare l'architettura dell'Academy ed elevare entrambi i corsi a formazione professionale nell'utilizzo dell'AI. Creator: autonomia nella creazione di contenuti, web app, sviluppo assistito, automazioni e prodotti digitali. Business: autonomia nell'analisi dati, BI, progettazione e implementazione AI, misurazione del valore. Sospesa la revisione dei 108 quiz avanzati Business residui dopo settimane 7–12; 420/528 (79,55%) misura solamente feedback distinti. Nessuna riscrittura prima di audit e approvazione del modello didattico.

Piano: 0) consolidamento documentale; 1) profili professionali, prerequisiti e benchmark preliminare; 2) audit tracciabile delle 264 sessioni, 528 quiz, 1584 feedback, risorse, laboratori e tempi; classificare conservare/integrare/riprogettare con evidenze; 3) standard con teoria, strumenti, setup, dati/asset, esempi funzionanti, laboratorio guidato, esercizio autonomo, rubriche e portfolio; 4) prototipi Creator (app dati) e Business (ROI di un pilota AI), approvazione utente; 5) revisione per blocchi e non regressione; 6) riallineamento quiz, test runtime e valutazione finale. Benchmark finale obbligatorio dei due corsi rispetto a offerte online comparabili e programmi avanzati, con fonti ufficiali datate, prerequisiti, ore, contenuti, laboratori, valutazioni, portfolio, mentoring, costi e credenziali; distinguere confronto documentale, test studente e valutazione indipendente. Redigere giudizio critico da reader in prospettiva esterna, ma non presentarlo come revisione indipendente; proporre alternative e integrazioni qualora il livello non sia soddisfacente, senza proclamare primato di mercato non dimostrato. Benchmark esplorativo: MIT Enterprise Software Development with AI Agents, UT Austin Generative AI for Software Development, MIT Applied AI & Data Science, Google Cloud Career Launchpad, Caltech Data Analytics & GenAI; ampliare a creatività multimediale e business/BI. Fonti preliminari: https://professional.mit.edu/course-catalog/enterprise-software-development-ai-agents ; https://onlineexeced.mccombs.utexas.edu/genai-for-software-development ; https://professional-education-gl.mit.edu/mit-online-data-science-program ; https://cloud.google.com/edu/faculty/career-launchpad . Non ancora confronto completo.

## Cronologia storica delle versioni

Le sezioni seguenti sono conservate integralmente come testimonianza dello stato al momento della loro redazione. Le indicazioni storiche di attività da completare (inclusi i quiz base) non rappresentano lo stato corrente; prevalgono il riepilogo sopra e le evidenze aggiornate in ROADMAP.md. Le denominazioni 6.6.0 e QA 6.6.1 sono riferimenti storici, non attestazioni di un nuovo rilascio.

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
