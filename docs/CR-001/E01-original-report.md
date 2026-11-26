# CR-001 — E01 — Instructional Design Review Report

**Progetto:** AI Creator Academy — Excellence Learning 6.6
**Repository / branch:** itopo-ai/AI-Creator-Academy — excellence-learning-6.6
**Checkpoint esaminato:** f9d98c2bbd4d3622b9ccb5eeeb5c1811a2c4d401
**Natura del rapporto:** revisione documentale svolta da un'AI esterna (simulazione di revisore specialistico). Non è un audit umano indipendente, non è un collaudo e non è una validazione empirica.

---

## 1. Modello AI, versione e data

- Modello: Claude Opus 5.5 (Anthropic), identificativo `claude-opus-5-5`.
- Data della revisione: 26/11/2026 (fuso Europe/Rome).
- Conoscenze del modello aggiornate a giugno 2026. Per questa revisione la data non conta: sono stati esaminati solo i due documenti al checkpoint, senza fonti esterne.

## 2. Ruolo specialistico

E01 — Instructional Design, con priorità massima. Ambito: allineamento degli obiettivi, i 12 componenti AELS, le rubriche AAS, la diagnostica ADS, il carico ALWS e le credenziali ACS; ricerca di controesempi di promozione senza padronanza e di sovraccarico; distinzione G12-S / G12-E.

## 3. Capacità e limiti

**Capacità usate:** lettura integrale dei due documenti; verifica crittografica del checkpoint e dei blob; ricalcolo aritmetico di conteggi, ore, combinazioni di rubrica e probabilità di superamento casuale (script Python eseguito realmente); analisi di coerenza tra le sezioni.

**Limiti:**
- Non ho esaminato curriculum JSON, codice, app, risorse esterne né immagini: le osservazioni sui quiz esistenti si basano sugli audit riportati in ROADMAP, non sui sorgenti.
- Non ho eseguito collaudi runtime, test con studenti o simulazioni AMVP.
- Le stime di carico e profondità sono inferenze di progettazione didattica, non misure.
- Non conosco il contenuto delle immagini originali (IMG_9493–9499) né le parti non trascritte: non le ricostruisco.
- Il giudizio di un singolo modello può contenere errori sistematici non rilevabili dall'interno.

## 4. Bias e potenziali conflitti

- Claude è uno dei fornitori AI citati negli standard (AES lo elenca tra i candidati gratuiti; AMVP gli assegna il ruolo di revisore esterno). Non ho interesse dichiarabile sull'esito, ma un conflitto di posizione non può essere escluso.
- Il mandato è stato preparato dall'AI coordinatrice del progetto (ChatGPT): la scelta delle domande può orientare la revisione (*framing bias*). Ho cercato attivamente anche criticità non suggerite dal mandato.
- Tendenze possibili dei modelli linguistici: eccessiva fiducia nei testi molto strutturati, preferenza per raccomandazioni formalistiche. Le ho mitigate ancorando ogni osservazione a righe precise dei documenti.

## 5. Indipendenza procedurale

- Non ho letto rapporti di altri revisori (E02–E07) né `docs/CR-001.md`.
- Nessuna interazione con l'AI coordinatrice durante la revisione.
- Ho usato una copia locale in sola lettura (`git clone --no-checkout`). Non ho modificato il repository, non ho fatto push, non ho chiuso gate e non ho avviato la Fase 4.
- Indipendenza **procedurale**, non istituzionale: il revisore resta un'AI scelta dal progetto.

## 6. Ambito, materiali e checkpoint

- **Materiali autorizzati:** `README.md` e `ROADMAP.md` al commit f9d98c2bbd4d3622b9ccb5eeeb5c1811a2c4d401, letti per intero.
- **Fuori ambito:** curriculum JSON, codice, sw.js, risorse online, immagini, `docs/CR-001.md`.
- **Nota:** al momento della revisione la testa del branch è `84419eeeed0e84937abf115045d76fc9c30f5dc9`, di 6 secondi successiva al checkpoint. Aggiunge `docs/CR-001.md` («align CR-001 and seven prompts…»). Il contenuto non è stato letto, perché esterno al mandato. README e ROADMAP non risultano modificati in quel commit: ne ho visto soltanto l'elenco dei file.

I riferimenti nel rapporto usano il numero di riga del file al checkpoint (es. `ROADMAP:1234`).

## 7. Esito della verifica preliminare di accesso

| Verifica | Esito | Metodo |
|---|---|---|
| Esistenza del commit checkpoint | Superata | `git cat-file -t` → commit |
| Appartenenza al branch excellence-learning-6.6 | Superata | `git branch -r --contains` |
| Blob SHA README.md = abca6f1ce6345ed1cc55eb5dd5f78ff0a7232afb | Superata | `git ls-tree` e `git hash-object` sul file estratto |
| Blob SHA ROADMAP.md = af9888bc28f0fef48ea226e86fe3be5a24913008 | Superata | idem |
| Lunghezza README ≈ 54.465 caratteri | **Esatta: 54.465** caratteri Unicode (54.854 byte, 183 righe) | Conteggio Python UTF-8 |
| Lunghezza ROADMAP ≈ 287.684 caratteri | **Esatta: 287.684** caratteri Unicode (290.224 byte, 1.322 righe) | idem |
| Contenuto integrale, non troncato | Superata | Estratto da Git, nessuna anteprima; letto per intero in blocchi sequenziali (README 1–183; ROADMAP 1–1322) |
| Capacità di elaborazione sufficiente | Confermata | Lettura completa nel contesto di lavoro |

**Non eseguito:** la verifica della firma o dell'autore del commit (nessuna firma richiesta). Nessun accesso agli URL web indicati nel mandato: il contenuto è stato ottenuto da Git e l'equivalenza è garantita dagli SHA.

**Conclusione:** l'accesso integrale è confermato e la revisione è proseguita.

## 8. Metodo di revisione

1. Lettura integrale e sequenziale dei due documenti.
2. Estrazione delle regole normative di AELS, AAS, ADS, AES, ALWS, ACS, AVS e AMVP (fasi 3A–3I) e confronto con Fase 1, Fase 2 e regole permanenti.
3. Analisi di tracciabilità R01–R12 ↔ standard ↔ G01–G12.
4. Ricerca di controesempi formali:
   - enumerazione completa delle 5⁶ = 15.625 combinazioni della rubrica AAS (pesi 30/20/20/15/10/5, P = Σ peso·livello/4), filtrate per i minimi;
   - probabilità binomiale di superare il quiz all'80% rispondendo a caso (3 opzioni) con tentativi ripetuti;
   - verifica delle somme ALWS e del carico settimanale.
5. Confronto tra tempi ALWS, proporzioni 3A e durate delle verifiche AAS.
6. Classificazione P0–P3 secondo AVS (`ROADMAP:1258`).

Ogni osservazione distingue: **[E]** evidenza testuale, **[I]** inferenza, **[H]** ipotesi.

Verifiche aritmetiche superate senza anomalie: sessioni 42/50/94 = 186 e 54/83/97 = 234 (totale 420); +66 Creator e +90 Business; ore 338,5 / 420,25 / 758,75 h, media 108,39 min, +187,4%; scenario con capstone 414,5 / 500,25 / 914,75 h; riserva del 15% 476,675 / 575,2875 h; portfolio 3+1 / 4+1 / 5+1 = 15; catalogo ACS 36 + 6 + 6 + 2 = 50.

## 9. Punti di forza

- **Separazione degli stati epistemici [E]:** il documento distingue in modo costante tra dichiarato, documentato, verificato, collaudato e validato (`ROADMAP:69`, `1258`), e tra avanzamento, conoscenza, competenza e portfolio (`ROADMAP:1225`). È raro e molto utile.
- **Rinuncia a crediti fittizi [E]:** nessuna attribuzione retroattiva di competenze; esoneri esclusi da numeratore e denominatore (`ROADMAP:1238`).
- **Errori critici non compensabili [E]:** sicurezza, privacy, falsificazione e verifiche obbligatorie bloccano indipendentemente dal punteggio (`ROADMAP:1234`). È la principale difesa contro la promozione senza padronanza.
- **Valutazione autentica [E]:** capstone con difesa su variante o requisito nuovo, sfida autonoma con variante significativa, test negativi, holdout. Il modello adotta l'allineamento compito–evidenza.
- **Progressione cognitiva esplicita [E]:** distribuzione Bloom per livello (`ROADMAP:1234`) e assistenza decrescente da L1 a L3 (`ROADMAP:1230`).
- **Principio «AI Assisted, Human Verified» [E]:** registro dell'uso dell'AI e verifica umana documentata, coerente con un percorso che ammette l'AI.
- **Gestione onesta delle lacune [E]:** gate aperti e blocchi (B) dichiarati invece di nasconderli, ad esempio per la generazione gratuita di audio e video (`ROADMAP:751`) e per DAX su sistemi diversi da Windows (`ROADMAP:1111`).
- **Aritmetica di carico e conteggi interamente coerente** (§8).

## 10. Osservazioni e anomalie P0–P3

Non ho rilevato anomalie **P0**: non esistono implementazioni né rilasci che espongano oggi gli studenti a danni. Ogni P1 qui sotto blocca l'accettazione del gate indicato. Riepilogo:

| ID | Priorità | Titolo | Gate |
|---|---|---|---|
| E01-01 | P1 | Rubrica compensativa: «eccellenza» con autonomia «in sviluppo»; soglia di autonomia abbassata rispetto a Fase 1 | G03, G09 |
| E01-02 | P1 | Modalità di valutazione non vincolate alle credenziali: autovalutazione o AI possono bastare | G03, G09 |
| E01-03 | P1 | Quiz esposti a superamento casuale; vincolo «indici invariati» in conflitto con AAS | G03, G11 |
| E01-04 | P1 | G12 senza regola di chiusura; affermazioni ammesse in assenza di G12-E non definite | G12 |
| E01-05 | P1 | Manca la mappa obiettivi → componenti → prove → badge | G01, G03, G09 |
| E01-06 | P1 | Rischio di sovraccarico e profondità insufficiente nei livelli L2 da zero | G01, G07 |
| E01-07 | P2 | Dodici componenti AELS non eseguibili nelle durate ALWS minime | G01, G07 |
| E01-08 | P2 | Nessuna regola di progressione tra livelli | G03, G04 |
| E01-09 | P2 | ADS: esonero solo teorico, test non sorvegliato e ripetibile; aree incoerenti | G04 |
| E01-10 | P2 | Credenziali e componente teorica per gli esonerati non definite | G04, G09 |
| E01-11 | P2 | Media «pratica ≥ 75» compensativa tra laboratori | G03 |
| E01-12 | P2 | Nessuna verifica di ritenzione né prova cumulativa | G03, G12 |
| E01-13 | P2 | Stato corrente obsoleto in testa ai documenti; tracciabilità R↔G imperfetta | G01, G12 |
| E01-14 | P2 | Ambito delle simulazioni AMVP non delimitato rispetto ai limiti dichiarati | G12-S |
| E01-15 | P3 | Residui della rubrica 0–3 nelle matrici 2E | G03 |
| E01-16 | P3 | Intensità molto diversa tra livelli Creator | G07 |
| E01-17 | P3 | Lessico «Excellence» ed «eccellenza» senza evidenza | G12 |

### E01-01 — P1 — Rubrica compensativa: «eccellenza» con autonomia «in sviluppo»

**Riferimenti:** AAS `ROADMAP:1234` (`README:154`); Fase 1 `ROADMAP:214`; C02 `ROADMAP:1266`; ACS `ROADMAP:1250`.

**Evidenza:**
- [E] AAS: pesi 30/20/20/15/10/5; minimo 2 su ogni criterio obbligatorio e 3 su correttezza e affidabilità; fascia 90–100 = eccellenza; Level «With Distinction» ≥ 90.
- [E] Fase 1: «2 autonomo su caso previsto», con soglia ≥ 2 in ogni dimensione essenziale. C02 sostituisce la scala 0–3 con 0–4, dove 2 = «in sviluppo».
- [E, calcolo eseguito] Su 15.625 combinazioni, autonomia = 2 consente fino a P = 92,5 (gli altri criteri a 4). Esistono 4 combinazioni con autonomia 2 e P ≥ 90. Con autonomia e metodo entrambi a 2 si arriva a 82,5, cioè fascia «consolidata». Se la documentazione non è un criterio obbligatorio (AAS non lo precisa), è ammesso persino P = 95 con documentazione 0.

**Impatto:**
- [I] Il passaggio da 0–3 a 0–4 ha abbassato il minimo di autonomia da «autonomo» a «in sviluppo» senza una decisione esplicita: è una riduzione di soglia di fatto, mentre AVS vieta le riduzioni implicite.
- Un elaborato può ottenere la menzione di eccellenza pur dimostrando un'autonomia insufficiente, che è proprio l'obiettivo dichiarato dei due corsi (`ROADMAP:182`).

**Raccomandazione:**
- Dichiarare quali criteri sono obbligatori per ogni tipo di prova.
- Per la sfida autonoma, i capstone e le Level Credential, porre autonomia ≥ 3.
- Per la fascia «eccellenza» e per «With Distinction», porre ≥ 3 su tutti i criteri e ≥ 4 su almeno correttezza o affidabilità.
- In alternativa, motivare per iscritto l'abbassamento rispetto a Fase 1.

**Test proposto:** enumerare tutte le combinazioni ammesse dalla regola finale e verificare che nessuna con autonomia < 3 raggiunga lo stato «superato» nelle prove autonome e capstone, né la fascia ≥ 90.

**Criterio di accettazione:** tabella delle combinazioni senza controesempi, regola approvata dall'utente e registrata in AAS e ACS.

### E01-02 — P1 — Modalità di valutazione non vincolate alle credenziali

**Riferimenti:** AAS `ROADMAP:1234`; ACS `ROADMAP:1250`; AMVP `ROADMAP:1259`.

**Evidenza:**
- [E] Modalità ammesse: «prove automatiche, autovalutazione strutturata, AI assistita non indipendente, revisione umana solo se disponibile e non a pagamento obbligatorio».
- [E] Nessun testo stabilisce quali modalità siano *sufficienti* per Skill Badge, Capstone Credential, Level Credential o Program Credential. ACS registra il «metodo», ma non pone vincoli.
- [E] La calibrazione AAS (scarto > 10 punti o > 1 livello) presuppone valutatori indipendenti, che AMVP dichiara non disponibili («nessun test umano esterno disponibile»).

**Impatto:**
- [I] Controesempio: un capstone L3 valutato solo con autovalutazione strutturata raggiunge 90 e produce una Level Credential «With Distinction», che dichiara competenze mai osservate da un valutatore terzo.
- Metodo (20), autonomia (15) e qualità (10), cioè il 45% dei pesi, non sono misurabili con test automatici: dipendono da giudizio umano o AI.

**Raccomandazione:**
- Creare una matrice *modalità × tipo di prova × credenziale*.
- Per capstone e livelli richiedere almeno: test automatici riproducibili sul lavoro consegnato, artefatto eseguibile da clone pulito e difesa su variante nuova, valutata con rubrica ancorata da un valutatore diverso dallo studente. L'AI è ammessa come valutatore se dichiarata, ma non come unica fonte per i criteri ad alto peso.
- Riportare sulla credenziale la modalità di valutazione in forma leggibile, ad esempio «valutazione AI assistita, non indipendente».
- Vietare la menzione «With Distinction» con la sola autovalutazione.

**Test proposto:** in Fase 4 (4A/4B, 4E), con 3 elaborati campione per capstone e 2 valutatori AI separati più l'autovalutazione, misurare gli scarti tra valutazioni; verificare che le regole impediscano la credenziale con la sola autovalutazione.

**Criterio di accettazione:** matrice approvata; nessuna credenziale emettibile con una sola modalità non indipendente; scarti di calibrazione entro le soglie AAS o riesame documentato.

### E01-03 — P1 — Quiz esposti a superamento casuale; conflitto tra «indici invariati» e AAS

**Riferimenti:** Fase 2C/2D `ROADMAP:285`, `324`, `375`, `422`, `462`, `513`, `560`, `607`, `652`; AAS `ROADMAP:1234`; vincoli `ROADMAP:20`.

**Evidenza:**
- [E] In 264/264 sessioni la risposta corretta del quiz base e di quello avanzato è nella stessa posizione. Le posizioni sono sbilanciate (es. Business 1–12: 32/20/20). «Distrattori spesso ovvi». Tre sole opzioni. «Ordine UI non verificato».
- [E] AAS richiede distrattori plausibili e un feedback specifico per ogni opzione, ma impone di calibrare il numero di domande «senza alterare attività/ID/indici».
- [E] Tentativi «senza limiti artificiali» con «miglior risultato valido».
- [E, calcolo] Con 5 domande a 3 opzioni e soglia dell'80% (4/5), la probabilità di superare rispondendo a caso è del 4,5% per tentativo e del **60% su 20 tentativi**. Con 8 domande scende allo 0,26% per tentativo (5% su 20); con 12 allo 0,05%.
- [E] I 108 quiz avanzati Business con due feedback errati identici (sospesi) non sono conformi ad AAS.

**Impatto:**
- [I] Il requisito dei quiz (80%) e la componente teorica (20% del livello) possono essere soddisfatti senza padronanza, soprattutto in L1 (5–8 domande).
- Il vincolo di preservare gli indici, giusto per la compatibilità dei progressi, impedisce di correggere lo sbilanciamento delle posizioni se la UI non rimescola le opzioni.

**Raccomandazione:**
- Separare *indice di dato* e *ordine di presentazione*: rimescolare in visualizzazione preservando l'indice salvato, previa verifica runtime.
- Banca di varianti con almeno 2–3 forme parallele per verifica.
- Numero minimo di item tale che la probabilità di superamento casuale sui tentativi realisticamente ripetuti resti sotto l'1%.
- Variante nuova obbligatoria dopo un insuccesso; «miglior risultato» calcolato solo tra forme diverse.
- Integrare la teoria di livello con item non a scelta multipla.

**Test proposto:** calcolo per L1, L2 e L3; audit delle chiavi (distribuzione delle posizioni presentate e corrette); in Fase 6, verifica che il rimescolamento non alteri punteggi e migrazione (G11).

**Criterio di accettazione:** probabilità di superamento casuale inferiore all'1% sui tentativi consentiti; distribuzione delle posizioni presentate non significativamente diversa dall'uniforme; 0 quiz con feedback duplicati; indici dei dati invariati.

### E01-04 — P1 — G12 senza regola di chiusura; affermazioni ammesse senza G12-E non definite

**Riferimenti:** AVS e AMVP `ROADMAP:1258–1259`; sottogate `ROADMAP:1294–1299`; regola 3 `ROADMAP:1254`.

**Evidenza:**
- [E] G12-S «Aperto», G12-E «Non verificata»; «prima di un eventuale rilascio stabilire quali affermazioni sulla qualità siano sostenibili in assenza di G12-E».
- [E] AVS definisce V5 «validata didatticamente» e V6 «accettata», ma non dice se V5 o la chiusura di G12 richiedano G12-E.
- [E] AMVP: «nessun test umano esterno disponibile».

**Impatto:**
- [I] Due esiti ugualmente indesiderabili:
  1. G12 non può mai chiudersi, quindi nessuna sessione arriva a V6 e il rilascio non è mai conforme ad AVS;
  2. nasce una pressione a chiudere G12 sulla sola simulazione, contro AVS («nessuna falsa chiusura»).

**Raccomandazione (senza derogare ad AVS):**
- Scindere formalmente G12 in **G12-S** (chiudibile con evidenze AMVP) e **G12-E** (aperto finché non esistono dati umani).
- Ridefinire V5 come «validata didatticamente in simulazione (G12-S)» e introdurre uno stato distinto, ad esempio «V5-E», per la validazione empirica.
- Consentire il rilascio solo con l'etichetta pubblica «efficacia empirica non verificata», con la decisione registrata dall'utente.

**Affermazioni sostenibili senza G12-E**, purché supportate dalle evidenze del rispettivo stato:
- «Progettato secondo standard interni AELS/AAS/ADS/AES/ALWS/ACS» (V1).
- «Contenuti verificati documentalmente», limitatamente alle sessioni in V2.
- «Laboratori eseguiti con esito documentato su ambiente/versione X», per le sessioni in V3.
- «Percorso gratuito verificato su N esecuzioni pilota», per V4, senza generalizzare.
- «Simulazioni AI con profili sintetici hanno rilevato/non rilevato…», sempre indicando che non misurano l'apprendimento umano.
- «La credenziale attesta che il titolare ha prodotto le evidenze X valutate con il metodo Y», cioè una dichiarazione sulla singola persona e sul metodo, non sull'efficacia del corso.

**Affermazioni non sostenibili senza G12-E:**
- «efficace», «garantisce l'apprendimento», «prepara a un livello professionale/junior»;
- «eccellenza» riferita al risultato formativo;
- tempi di completamento umani, tassi di successo o di ritenzione;
- qualsiasi equivalenza o superiorità rispetto a MIT, UT Austin, Caltech o Google;
- «With Distinction» presentata come misura di eccellenza comparata.

**Test proposto:** revisione dei testi pubblici di app, README, credenziali e portfolio con una checklist di affermazioni ammesse e vietate.

**Criterio di accettazione:** regola di chiusura scritta e approvata; 0 affermazioni vietate nei testi destinati agli studenti; etichetta G12-E visibile ovunque si parli di qualità.

### E01-05 — P1 — Manca la mappa obiettivi → componenti → prove → badge

**Riferimenti:** matrice Fase 1 `ROADMAP:197–211`; ARTM `ROADMAP:1258`; ACS `ROADMAP:1250`; audit 2C `ROADMAP:410`, `457`.

**Evidenza:**
- [E] Fase 1 definisce 11 ambiti di competenza con evidenze; ACS definisce 36 Skill Badge; AAS definisce 6 capstone. Non esiste una tabella di corrispondenza tra questi tre livelli.
- [E] «Matrice operativa non ancora compilata».
- [E] Gli audit 2C rilevano un «obiettivo generico» in tutte le sessioni Creator 13–24.
- [E] Alcuni badge dipendono da competenze bloccate (B), ad esempio Multimedia Production e la generazione AI di audio e video (`ROADMAP:751`).

**Impatto:**
- [I] L'allineamento costruttivo (obiettivo ↔ attività ↔ prova) è dichiarato ma non verificabile.
- Controesempi possibili:
  - un badge emesso su competenze non insegnate né valutate (ad esempio Change Management, con due sole sessioni proposte);
  - un ambito di Fase 1 senza badge né prova, come il rollback in «Creator: prodotto», mentre «09s5 controllo Pages non dimostra rollback».

**Raccomandazione:** prima della Fase 5, compilare l'ARTM almeno per le sessioni dei prototipi 4A e 4B con le colonne *obiettivo misurabile (verbo + condizione + criterio) → componente AELS → prova AAS → criterio di rubrica → badge e capstone*. Definire inoltre il trattamento dei badge che dipendono da gate B: sospensione, ridefinizione approvata o estensione facoltativa.

**Test proposto:**
- Ogni badge collegato ad almeno 2 prestazioni valutate su rubrica, in sessioni diverse.
- Ogni obiettivo obbligatorio collegato ad almeno una prova.
- Nessuna prova senza obiettivo.

**Criterio di accettazione:** 0 orfani in entrambe le direzioni nelle sessioni prototipo; 36/36 badge con definizione operativa approvata.

### E01-06 — P1 — Rischio di sovraccarico e profondità insufficiente nei livelli L2 da zero

**Riferimenti:** profili e prerequisiti `ROADMAP:194–195`; Creator L2 `ROADMAP:359`, `806–825`; Business L2 `ROADMAP:1084–1087`; BL1-P03–P05 `ROADMAP:1001–1003`; ALWS `ROADMAP:1246`; benchmark `ROADMAP:222`, `1246`.

**Evidenza:**
- [E] Creator: ingresso «nessuna programmazione obbligatoria». Il livello L2 (50 sessioni, 87,5 h più un capstone di 24 h) copre HTML, CSS, JavaScript (DOM e async), Git, Python, test, SQL, auth, RLS, backend, API, deploy e rollback.
- [E] Business: SQL affidato a 4 sessioni proposte (BL2-P10–P13: SELECT/WHERE, GROUP BY, JOIN/anti-join, CTE).
- [E] Il recupero matematico del Complete Track è affidato a 3 sessioni candidate (percentuali, statistica descrittiva, costi e margini).
- [E] ALWS cita «30 h esonero simulato non accertato» senza derivazione. Le sessioni propedeutiche identificate sono 6 (circa 9 h a 90 minuti).
- [E] Riferimento citato: la certificazione Adobe Firefly prevede circa 150 h di preparazione tipica per un ambito specifico, mentre Creator L1 intero vale 75 h.

**Impatto:**
- [I/H] Per i profili C01 e B04 il rapporto tra contenuto e tempo è fortemente ottimistico. Esiti probabili:
  1. sovraccarico e abbandono;
  2. pressione a delegare all'AI i laboratori, cioè promozione senza padronanza;
  3. sottostima sistematica delle ore ALWS.
- Il Complete Track promette una «preparazione matematica, statistica, economica e digitale necessaria» (`ROADMAP:507`) con una dotazione che appare insufficiente.

**Raccomandazione:**
- Stimare il tempo per obiettivo (bottom-up) per L2 Creator e L2 Business, invece di partire da medie per sessione.
- Documentare l'origine delle «30 h».
- Valutare un modulo ponte («L1.5») o un ampliamento delle sessioni di programmazione, SQL e matematica, con approvazione dell'utente.
- Dichiarare nell'onboarding l'impegno realistico per profilo.

**Test proposto:** nei prototipi, tempi misurati da almeno un esecutore umano principiante, se disponibile, per 3 laboratori L2. In mancanza, tempi di esecuzione tecnica reale (setup, debug) separati dalla lettura, con P80 ipotizzato e dichiarato come stima.

**Criterio di accettazione:** derivazione scritta delle ore per obiettivo; scostamento della mediana misurata ≤ 20% (ALWS) oppure ricalibrazione approvata; origine delle 30 h documentata o valore rimosso.

### E01-07 — P2 — Dodici componenti AELS non eseguibili nelle durate ALWS minime

**Riferimenti:** 3A `ROADMAP:1225`; ALWS `ROADMAP:1246`; AAS `ROADMAP:1234`; Fase 1 `ROADMAP:213`.

**Evidenza:**
- [E] Sessione S1 = 30–45 minuti. La tipologia «fondamenti» destina il 15% alla verifica, cioè 4,5–6,75 minuti.
- [E] La verifica AAS L1 richiede 5–8 domande in 5–12 minuti.
- [E] In L3, una sessione S2 di 60 minuti al 15% concede 9 minuti, contro un minimo AAS L3 di 15 minuti.
- [E] Non è stabilito se i 12 componenti siano obbligatori per sessione o per unità; Fase 1 ammetteva il rinvio al laboratorio settimanale, AELS e ARTM lo tacciono.

**Impatto:** [I] Molte sessioni brevi risulteranno «non conformi» oppure i componenti saranno compressi in forma simbolica (componenti spuntati, non realizzati).

**Raccomandazione:**
- Regola esplicita sul livello di aggregazione: 12 componenti garantiti per unità o settimana; per singola sessione un elenco minimo con N/A motivato (AVS lo ammette).
- Tabella di fattibilità tipologia × durata × componenti.

**Test proposto:** verifica documentale di 6 sessioni campione (S1–S5, L1–L3) contro la tabella di fattibilità.

**Criterio di accettazione:** 0 combinazioni tipologia/durata/livello in cui i tempi minimi AAS superino la quota di verifica, oppure regola di aggregazione approvata.

### E01-08 — P2 — Nessuna regola di progressione tra livelli

**Riferimenti:** AAS e ACS `ROADMAP:1234`, `1250`; AES «gate bloccato» `ROADMAP:1242`; README 6.5.0 `README:53`.

**Evidenza:**
- [E] Le credenziali richiedono soglie, ma nessuna parte dei documenti stabilisce se l'accesso a L2 o L3 sia condizionato alla padronanza di L1 o L2, né se la progressione sia consigliata o bloccante.
- [E] La percentuale di lezione resta «attività spuntate / attività previste».

**Impatto:**
- [I] Controesempio: uno studente avanza a L3 (agenti, MCP, RLS in produzione) senza aver superato auth e RLS di L2, perché l'interfaccia mostra «avanzamento» alto basato su spunte.
- La metafora dell'ascesa alla vetta può comunicare padronanza dove c'è solo completamento.

**Raccomandazione:**
- Definire una politica di progressione: consultiva con avviso, oppure bloccante solo per i prerequisiti critici di sicurezza e dati.
- Separare visivamente nell'interfaccia «completato» da «competenza verificata» (coerente con C03), già nei prototipi 4C.

**Test proposto:** scenario AMVP C01 che salta un prerequisito critico; verifica che il sistema progettato lo segnali e che nessun indicatore di competenza aumenti.

**Criterio di accettazione:** politica approvata; nei mockup 4C nessun indicatore di vetta o percentuale calcolato sulle sole spunte.

### E01-09 — P2 — ADS: esonero solo teorico, test non sorvegliato e ripetibile; aree incoerenti

**Riferimenti:** ADS `ROADMAP:1238`; Fase 1 `ROADMAP:194`; regola dei rami `ROADMAP:507`; 2D `ROADMAP:562`; fonti in inglese `ROADMAP:756`, `832`.

**Evidenza:**
- [E] L'esonero richiede teoria ≥ 85% e pratica «quando richiesta», quindi non sempre.
- [E] La teoria è «senza consultazione su base dichiarativa», cioè non sorvegliata. La ripetibilità della diagnostica non è definita, mentre AAS ammette «tentativi senza limiti».
- [E] ADS rende «candidabili» D1 digitale e D2 informatica, mentre la regola dei rami lega il Professional Track a competenze matematiche ed economiche e il 2D dichiara che le competenze digitali non sono automaticamente esonerabili.
- [E] Fase 1 prevedeva una diagnostica su «inglese tecnico» per Creator; ADS non ha un'area linguistica, pur con fonti prevalentemente in inglese. Per Creator non è specificato alcuno strumento diagnostico («supporto mirato»).

**Impatto:**
- [I] Falsi esoneri: un test dichiarativo ripetibile, risolvibile con l'AI, esonera dalla teoria propedeutica.
- Mancato rilevamento della barriera linguistica, che causerebbe insuccessi attribuiti erroneamente a lacune di contenuto.

**Raccomandazione:**
- Pratica sempre obbligatoria per l'esonero.
- Forme parallele, numero di tentativi o intervallo minimo tra ripetizioni.
- Allineare D1 e D2 alla regola dei rami, oppure motivare l'estensione.
- Aggiungere un'area D7 di lettura tecnica in inglese (orientativa, senza esonero) e uno strumento diagnostico Creator su logica, file e inglese.

**Test proposto:** scenari AMVP B02 e B04 con risposte assistite dall'AI sulla teoria; verificare che senza prova pratica non nasca alcun esonero.

**Criterio di accettazione:** regole aggiornate e approvate; 0 percorsi di esonero solo teorico; area linguistica e diagnostica Creator definite.

### E01-10 — P2 — Credenziali e componente teorica per gli esonerati non definite

**Riferimenti:** ACS `ROADMAP:1250`; AAS `ROADMAP:1234`; C04 `ROADMAP:1266`.

**Evidenza:**
- [E] «Stesso riconoscimento Professional/Complete»; «esoneri solo registro». Badge come Business Economics e Digital Productivity e la teoria di livello (20%) dipendono in parte da contenuti propedeutici esonerabili.
- [E] Non è definito come si calcola la «teoria livello ≥ 80» per chi è esonerato, né se il badge sia conseguibile tramite la prova diagnostica.

**Impatto:** [I] O il Professional non può conseguire alcuni badge, e il riconoscimento non è identico, oppure li consegue tramite un esonero, cioè un credito fittizio vietato da ADS.

**Raccomandazione:** stabilire che la prova di esonero, superata con teoria e pratica sopra soglia AAS, costituisca evidenza valida per il badge pertinente, registrata come «verificata tramite diagnostica». Ricalcolare la componente teorica sul denominatore del ramo.

**Test proposto:** calcolo della Level Credential L1 per quattro casi: Professional o Complete, gratuito o premium.

**Criterio di accettazione:** stesse credenziali conseguibili in tutti e quattro i casi senza crediti senza evidenza.

### E01-11 — P2 — Media «pratica ≥ 75» compensativa tra laboratori

**Riferimenti:** AAS `ROADMAP:1234`; ACS `ROADMAP:1250`.

**Evidenza:** [E] La Level Credential richiede «pratica ≥ 75» e «competenze obbligatorie dimostrate», ma non definisce come la pratica di livello sia aggregata né come una competenza sia «dimostrata» (in assenza della mappa E01-05).

**Impatto:** [I] Controesempio: in Creator L2 il laboratorio RLS a 50/100 è compensato da laboratori HTML a 95, con media ≥ 75. Se non esiste un elenco di competenze obbligatorie per livello, la clausola non scatta.

**Raccomandazione:** soglia per competenza obbligatoria, ognuna ≥ 75 con zero errori critici, in aggiunta alla media.

**Test proposto:** caso sintetico con un laboratorio obbligatorio sotto soglia e media sopra 80.

**Criterio di accettazione:** credenziale negata nel caso sintetico.

### E01-12 — P2 — Nessuna verifica di ritenzione né prova cumulativa

**Riferimenti:** AELS e AAS `ROADMAP:1230`, `1234`; ACS (nessuna scadenza automatica) `ROADMAP:1250`; AMVP (ritenzione non provabile) `ROADMAP:1259`.

**Evidenza:** [E] Il recupero è previsto, ma non c'è una ripetizione dilazionata né una verifica cumulativa a fine livello oltre al capstone. «Miglior risultato valido».

**Impatto:** [I] Le competenze possono essere dimostrate una volta e dimenticate. Con livelli di 36 settimane (`ROADMAP:1246`) il rischio è concreto per L1 (circa 2 h a settimana).

**Raccomandazione:** prova cumulativa breve di livello su item di settimane precedenti; ripasso dilazionato a 1, 4 e 12 settimane come componente «consolidamento» AELS.

**Test proposto:** nel prototipo, inserire item dilazionati e verificare la tracciabilità ARTM.

**Criterio di accettazione:** regola presente in AELS e AAS; l'efficacia resta sotto G12-E.

### E01-13 — P2 — Stato corrente obsoleto in testa ai documenti; tracciabilità R↔G imperfetta

**Riferimenti:** `README:3`, `ROADMAP:3`, `26–41`, `55–60`; procedura permanente `ROADMAP:67`; `ROADMAP:1267` e `1290`; tabelle R e G `ROADMAP:1275–1292`; immagini `ROADMAP:1263`, `1322`.

**Evidenza:**
- [E] ROADMAP indica in testa «Aggiornato: 25 novembre 2026» e «Prossimo intervento: Fase 2C, completare audit individuale Creator 1–6», mentre lo stato reale è la Fase 3I. README apre con «Stato operativo corrente — 25 novembre 2026» e la tabella dei quiz.
- [E] R01–R12 risultano «Approvato registro consolidato» (`ROADMAP:1267`) e insieme «proposta organizzativa» (`ROADMAP:1290`).
- [E] Corrispondenza R↔G: R02 «Applicazione pratica e autonomia» ↔ G02 «Riproducibilità pratica»: **l'autonomia non ha un gate**. R12 «Validazione e revisione critica» ↔ G12 «Efficacia formativa» (oggetti diversi). R10 è attribuito ad AVS, mentre i requisiti di sicurezza didattica (errori critici) sono in AAS e AELS.
- [E] Mancano IMG_9493–9499 (7 file); ne sono state ricevute 6, di cui una compensativa; IMG_9497 non è verificata. La trascrizione delle parti coperte non è attestata.

**Impatto:**
- [I] Un lettore o un'AI che riprende da capo il documento (regola 1) può eseguire un passo superato.
- L'autonomia, obiettivo centrale, non è tracciata da alcun gate.
- La fedeltà testuale di R01–R12 all'approvazione originale non è dimostrabile.

**Raccomandazione:**
- Aggiornare i riepiloghi correnti in testa, come richiesto dalla procedura permanente.
- Uniformare lo stato di R01–R12.
- Aggiungere ai registri una colonna R→G→standard→criterio di accettazione.
- Rendere esplicita l'autonomia (sottogate di G02 o G03).
- Archiviare nel repository, o almeno elencare con hash, le immagini di provenienza.

**Test proposto:** rilettura a freddo dei soli primi 60 righe di ciascun documento: il prossimo passo e lo stato devono risultare corretti.

**Criterio di accettazione:** stato corrente coerente in testa; tabella R↔G completa; provenienza documentata.

### E01-14 — P2 — Ambito delle simulazioni AMVP non delimitato rispetto ai limiti dichiarati

**Riferimenti:** AMVP `ROADMAP:1259`; C07 `ROADMAP:1266`.

**Evidenza:** [E] AMVP riconosce che non è possibile cancellare le conoscenze del modello, che il tempo dell'AI non è il tempo umano e che la simulazione non prova la ritenzione; prevede comunque 108–324 scenari che includono comprensione, recupero e trasferimento.

**Impatto:** [I] Un AI Student che simula il profilo C01 risolve comunque i laboratori. Ne derivano falsi negativi su sovraccarico, prerequisiti impliciti e misconcezioni da principiante, e il rischio di presentare G12-S come prova di comprensione.

**Raccomandazione:** limitare G12-S a ciò che la simulazione può rilevare:
- ambiguità delle consegne;
- prerequisiti non dichiarati, tramite il vincolo «usa solo le informazioni fornite» con traccia;
- laboratori non risolvibili con i materiali dati;
- fughe di soluzione;
- ambiguità e disaccordo tra rubriche;
- incoerenze tra quiz e teoria.

Escludere esplicitamente da G12-S tempo, comprensione reale e ritenzione.

**Test proposto:** pilota AMVP in Fase 4 su 2 sessioni con difetti inseriti deliberatamente (prerequisito mancante, chiave errata, consegna ambigua). Misurare quanti difetti vengono rilevati.

**Criterio di accettazione:** elenco dei difetti che G12-S rileva e non rileva approvato; tasso di rilevamento dei difetti inseriti documentato.

### E01-15 — P3 — Residui della rubrica 0–3 nelle matrici 2E

**Riferimento:** 12 occorrenze di «0–3» in ROADMAP, ad esempio `686`, `751`, `827`, `946`, `1018`, `1111`, `1218`.

**Evidenza:** [E] C02 le supera, ma restano senza nota a margine.

**Raccomandazione:** nota di rinvio ad AAS 0–4 nelle sezioni storiche.

**Criterio di accettazione:** nessun prototipo 4A o 4B che usi la scala 0–3.

### E01-16 — P3 — Intensità molto diversa tra livelli Creator

**Riferimento:** ALWS `ROADMAP:1246`.

**Evidenza:** [E, calcolo] Con 36 settimane per livello, Creator L1 ≈ 2,1 h a settimana e L3 ≈ 6,3 h a settimana (×3); Business L1 ≈ 2,6 e L3 ≈ 6,5.

**Impatto:** [I] Rischio di disimpegno in L1 e di picco di carico in L3.

**Raccomandazione:** calendario per livello proporzionale al carico, oppure dichiarare intervalli settimanali.

**Criterio di accettazione:** carico settimanale dichiarato per livello nell'onboarding.

### E01-17 — P3 — Lessico «Excellence» ed «eccellenza» senza evidenza

**Riferimenti:** titoli README e AELS; fascia 90–100 AAS.

**Evidenza:** [E] AELS dichiara «nessuna equivalenza o eccellenza internazionale» senza benchmark, ma nomi e fasce usano il termine.

**Raccomandazione:** riservare «eccellenza» alla fascia della singola prova; nei testi pubblici usare formule descrittive (vedi E01-04).

**Criterio di accettazione:** checklist delle affermazioni superata.

## 11. Raccomandazioni e verifiche mancanti

**Prima della Fase 4, a livello documentale, sotto approvazione dell'utente:**
1. Correggere le regole AAS e ACS su autonomia ed eccellenza (E01-01), modalità di valutazione per credenziale (E01-02), aggregazione per competenza (E01-11) e trattamento degli esonerati (E01-10).
2. Scrivere la regola di chiusura di G12-S e G12-E e la checklist delle affermazioni ammesse (E01-04).
3. Definire la politica di progressione (E01-08), le regole ADS su pratica, ripetizioni, aree e inglese (E01-09) e l'aggregazione dei componenti AELS (E01-07).
4. Aggiornare l'intestazione corrente dei due documenti e la tabella R↔G (E01-13).

**Durante la Fase 4, nei prototipi:**
5. Compilare l'ARTM per le sessioni dei prototipi 4A e 4B (E01-05).
6. Stima bottom-up e misure di tempo per i laboratori L2 (E01-06).
7. Banca item con forme parallele e verifica del rimescolamento (E01-03).
8. Pilota AMVP con difetti inseriti (E01-14) e calibrazione delle rubriche (E01-02).

**Verifiche non eseguite e fuori dalla mia portata in CR-001:**
- curriculum JSON, distribuzione effettiva delle chiavi e ordine nell'interfaccia;
- runtime, Safari/iPhone, PWA e backup;
- risorse online, quote e licenze;
- equivalenza tra percorso gratuito e premium;
- tempi umani e ritenzione;
- contenuto delle immagini originali.

Gli esiti di questo rapporto non chiudono alcun gate.

## 12. Esito complessivo

**PARZIALE.**

L'architettura didattica è coerente nelle intenzioni e superiore alla media per onestà epistemica, valutazione autentica e divieto di crediti fittizi. L'aritmetica è interamente corretta.

Tuttavia le regole operative di AAS, ACS e ADS contengono controesempi dimostrabili di promozione senza padronanza:
- eccellenza con autonomia «in sviluppo»;
- credenziali ottenibili con valutazione non indipendente;
- quiz superabili per caso con tentativi illimitati;
- esoneri solo teorici non sorvegliati.

A questi si aggiungono la mancanza della mappa di allineamento, un rischio rilevante di sovraccarico in L2 e una regola di chiusura di G12 assente.

Sono 6 osservazioni P1, 8 P2, 3 P3 e nessuna P0. Nessuna richiede modifiche applicative per essere risolta: sono correggibili a livello documentale prima o durante la Fase 4.

**Distinzione obbligatoria:**
- questo rapporto è una **simulazione di revisione specialistica eseguita da un'AI**;
- non costituisce **collaudo reale**, perché nessun test runtime è stato eseguito;
- non fornisce alcuna evidenza di **efficacia empirica presso studenti umani** (G12-E resta non verificata).

Nessun gate AVS è chiuso; la Fase 4 non è avviata; il repository non è stato modificato.
