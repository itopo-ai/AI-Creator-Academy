# CR-001 — E04 — Data Analytics / BI Review Report

## 1. Modello AI, versione e data

- **Modello:** Claude Opus 5.5 (ID `claude-opus-5-5`), Anthropic. La conoscenza affidabile del modello arriva a fine giugno 2026.
- **Data della revisione:** 26 novembre 2026, fuso Europe/Rome.
- **Ambiente:** una sessione agentica nel cloud Anthropic con shell Linux, Git in sola lettura e strumenti di lettura dei file. In questa revisione non ho usato navigazione web né ricerche online.

## 2. Ruolo specialistico

Sono il revisore AI esterno simulato **E04 — Data Analytics / BI** previsto dal protocollo AMVP. Non sono un esperto umano. Questa revisione **non** è un audit umano indipendente, non certifica nulla e non chiude alcun gate.

## 3. Capacità e limiti

**Capacità:**
- leggere per intero i due documenti autorizzati;
- controllare la coerenza interna e l'aritmetica;
- analizzare la progressione matematica, statistica, SQL, DAX e BI;
- valutare le proprietà statistiche delle soglie;
- costruire controesempi.

**Limiti:**
1. Non ho consultato risorse esterne: nessun link, prezzo, licenza o funzionalità di GA4, Power BI, Metabase, Coursera o Microsoft Learn è stato verificato. Quello che so di questi strumenti risale al più tardi a giugno 2026, quindi può essere superato. Ogni affermazione che ne dipende è marcata come **ipotesi**.
2. Non ho eseguito collaudi: nessun runtime, laboratorio, query o modello BI.
3. Non ho visto i curriculum JSON. Ho valutato i quiz solo nella forma trascritta in ROADMAP.md (testo e risposta corretta, senza distrattori né feedback).
4. Non posso misurare tempi umani né l'efficacia di apprendimento.
5. Le immagini citate nella Fase 3I non sono tra i materiali autorizzati, quindi non le ho viste.

## 4. Bias e potenziali conflitti

- **Conflitto di prodotto:** i documenti citano prodotti Anthropic (Claude come AI gratuita candidata, il corso Anthropic AI Fluency, Claude come revisore designato dalla Regola 3). Su questi prodotti non ho espresso alcuna preferenza e non li ho usati come termine di confronto.
- **Bias del modello:** possibile tendenza alla completezza eccessiva o a una severità sistematica. Per contenerla ho separato le evidenze testuali dalle inferenze.
- **Errori correlati:** è probabile che le altre prospettive E01–E07 siano svolte dallo stesso modello. Gli errori possono quindi essere correlati, e una concordanza tra i rapporti non vale come prova, come riconosce la stessa AMVP.
- **Conoscenza datata:** sulle funzionalità di GA4 e Power BI le mie conoscenze precedono di circa 5 mesi i documenti.

## 5. Indipendenza procedurale

- Non ho consultato rapporti di altri revisori, analisi del coordinatore, documenti successivi al checkpoint né altri file del repository.
- **Nota di trasparenza:** il `git clone --no-checkout` ha scaricato gli oggetti dell'intero repository, ma ho estratto e letto solo i due blob autorizzati. Come effetto collaterale ho visto due metadati: la testa del branch predefinito (`cd19c06596a16fc8fc091a6ea7fd8fb7b00275b0`, che coincide con il main dichiarato in ROADMAP) e il messaggio del commit di checkpoint. Non li ho usati come evidenza.
- Non ho modificato file, non ho chiuso gate e non ho avviato la Fase 4.

## 6. Ambito, materiali e checkpoint

- **Repository:** `itopo-ai/AI-Creator-Academy`
- **Checkpoint:** `f9d98c2bbd4d3622b9ccb5eeeb5c1811a2c4d401`, 26/11/2026 12:52 +0100, messaggio «docs: align phase 3I status with recovered evidence»
- **Materiali:** `README.md` (183 righe) e `ROADMAP.md` (1322 righe).
- **Ambito E04:** sequenza matematica, statistica, SQL, DAX e BI; qualità dei dati; GA4; RLS; deploy e refresh; diagnostica; prove autentiche; coerenza tra competenze, prerequisiti, laboratori, valutazioni e riconoscimenti. In più il mandato comune: R01–R12 e G12-S/G12-E.
- **Riferimenti:** nel rapporto `RM:n` indica la riga n di ROADMAP.md e `RD:n` la riga n di README.md, al checkpoint.

## 7. Esito della verifica preliminare

| Verifica | Esito | Metodo |
|---|---|---|
| Accesso al commit esatto | **Superata** | `git clone` in sola lettura; `git cat-file -t` → `commit` |
| Blob README.md | **Coincide**: `abca6f1ce6345ed1cc55eb5dd5f78ff0a7232afb` | `git ls-tree` al commit e `git hash-object` sul file estratto |
| Blob ROADMAP.md | **Coincide**: `af9888bc28f0fef48ea226e86fe3be5a24913008` | come sopra |
| Lunghezza README | **54.465 caratteri** (atteso circa 54.465) | conteggio Unicode in Python |
| Lunghezza ROADMAP | **287.684 caratteri** (atteso circa 287.684) | conteggio Unicode in Python |
| Integrità (non troncato, non sintetizzato) | **Superata** | estrazione con `git show` e hash identico |
| Lettura integrale | **Completata** | README in un segmento; ROADMAP in 7 segmenti consecutivi (1–272, 273–427, 428–566, 567–764, 765–956, 957–1113, 1114–1322) |

**Verifiche non riuscite o non effettuate:**
- La prima richiesta di collegamento del repository alla sessione è stata negata dalle autorizzazioni dell'ambiente.
- Lo scaricamento diretto via raw.githubusercontent tramite `curl` è stato rifiutato dal proxy (403).
- Il clone Git ha funzionato, quindi la verifica è completa.

**Conclusione: prerequisiti soddisfatti, la revisione può procedere.**

## 8. Metodo di revisione

1. Ho letto integralmente i due documenti nell'ordine e annotato tutte le affermazioni rilevanti per E04.
2. **Ricalcolo aritmetico manuale** di circa 50 chiavi numeriche dei quiz Business e di 2 Creator: ROI, TCO, CAC, margini, scostamenti, tassi, conversioni di unità, riconciliazioni. Ho ricalcolato anche i totali di ALWS, ADS, AMVP e le proposte di sessioni.
3. **Analisi statistica con script:**
   - probabilità di superare le soglie AAS (80%) e ADS (85%), con un modello binomiale e numero di item finito;
   - intervalli di Wilson al 95% sui campioni usati nei quiz;
   - test z per la differenza tra due proporzioni.
4. **Tracciabilità:** ho confrontato le schede 2D (audit) con le matrici 2E (risorse) per gli stessi ID; ho incrociato R01–R12 con G01–G12 e con gli standard; ho confrontato le proposte di composizione 2D e 2E.
5. **Controesempi:** per i concetti GA4, la riconciliazione, la classificazione e le decisioni su piccoli campioni.
6. Per ogni punto ho distinto le **evidenze testuali** (citate), le **inferenze** (deduzioni dal testo) e le **ipotesi** (basate su conoscenze esterne non verificate).

## 9. Punti di forza

Tutti documentati nel testo, nessuno collaudato.

1. **Onestà epistemica sistematica.** Gli stati V/P/B/T, la formula «non equivale a validazione», la distinzione tra demo e raccolta GA4 (RM:556) e il principio che una simulazione non vale come pratica reale (RM:1242) riducono il rischio di affermazioni false.
2. **Aritmetica corretta.** Tutte le chiavi numeriche ricalcolate sono corrette:
   - b07s1–s3 (50%, 0%, −25%), b23s1–s3, b31s2–s3, b33s1–s3, b34s2, b38s2, b42s3, b45s2 (B = 2.600);
   - i totali ALWS (758,75 h; 914,75 h; 476,675 h e 575,2875 h con la riserva), ADS (69 item, 90 min) e AMVP (108 e 324);
   - le proposte di sessioni (+66 Creator, +90 Business, 420 in tutto).
3. **Concetti di BI ben scelti:**
   - granularità e fan-out del join (b30s2);
   - rapporto di somme anziché media di percentuali (b31s3);
   - attribuzione distinta da incrementalità (b24s1–s3);
   - tasso per ordine anziché conteggio assoluto (b20s1–s2);
   - impatto delle esclusioni sui totali (b29s3: 2% delle righe, 30% dei ricavi);
   - deduplica di `transaction_id` e assenza di PII in GA4 (b22s2–s3);
   - test negativi per l'RLS (b35s2–s3);
   - freschezza dei dati e gestione del refresh fallito (b35s3).
4. **Parità gratuito/premium trattata come gate da dimostrare**, non come fatto acquisito. Copilot non è obbligatorio e un'AI esterna non è equiparata a Copilot né a DAX (RM:603, RM:1111).
5. **Prove autentiche previste:** holdout separato dal tuning, gold set per l'SQL generato dall'AI (BL2-P26), difesa su una variante nuova, campioni con difetti noti (b14s3).
6. **Gli esoneri ADS non coprono le applicazioni** (RM:1238), il che protegge la parità tra Professional e Complete.

## 10. Osservazioni e anomalie

Nessuna osservazione è classificata P0: non c'è rilascio in corso e tutti i gate restano aperti.

### E04-01 — La statistica applicata è sottodimensionata e non ha risorse verificate
- **Priorità:** P1
- **Riferimenti:** RM:1001–1004 (BL1-P04); RM:1097–1099 (BL2-P23–P25); RM:1023 (fonti); RM:1234 (capstone L2 «statistica»); RM:1250 (badge «Applied Statistics»); RM:603.
- **Evidenza:**
  - Per la statistica in L2 sono previsti 3 segnaposto. La fonte indicata è «B», cioè la pagina di download di Power BI Desktop.
  - Il documento stesso precisa che le fonti Q/B per le righe di SQL e statistica sono solo riferimenti di contesto BI, non verifiche di unità specifiche.
  - In L1 l'unica fonte statistica è OpenStax, con la nota «solo riferimento esterno».
  - La proposta 2D prevedeva «statistica/AI 4».
- **Inferenza:**
  - Il badge Applied Statistics e il capstone L2 richiedono una competenza statistica, ma il percorso non contiene statistica inferenziale: intervalli di confidenza, differenza tra proporzioni, dimensione del campione, variabilità e ripetizioni, confronti multipli.
  - Eppure in L3 (b19–b20, BL3-P10–P13) e nelle valutazioni (b24, esperimenti randomizzati) si prendono decisioni go/no-go su campioni piccoli.
- **Impatto:** la coerenza tra competenza dichiarata, insegnamento, valutazione e badge non è dimostrabile (G01, G03, G09). C'è il rischio di formare a trarre decisioni dal rumore.
- **Raccomandazione:**
  - Scrivere una mappa delle competenze statistiche minime per L1, L2 e L3: descrittiva, distribuzioni, campionamento e bias, incertezza sulle proporzioni, confronto prima/dopo, esperimento A/B, holdout e baseline di previsione.
  - Assegnare a ogni competenza un'unità di risorsa verificata e un laboratorio con risposte di riferimento.
  - Collocarla prima di b24 e prima dei piloti L3.
- **Test proposto:** dall'ARTM, verificare la matrice competenza → sessione → risorsa (stato almeno V) → item AAS → badge.
- **Criterio di accettazione:** 100% delle competenze del badge Applied Statistics coperte da almeno una sessione con risorsa verificata e almeno una prova pratica con soluzione di riferimento; nessuna decisione L3 richiesta prima della competenza inferenziale corrispondente.
- **Verifica necessaria:** documentale, poi verifica delle risorse esterne, poi collaudo dei laboratori.

### E04-02 — Si traggono conclusioni da campioni piccoli senza quantificare l'incertezza
- **Priorità:** P1
- **Riferimenti:** b14s3 (RM:524), b15s3 (RM:527), b20s2–s3 (RM:541–542), b42s3 (RM:630), cr-w18s5 (RM:408); AES «almeno 3 esecuzioni… non prova statistica» e «differenza AAS ≤10» (RM:1242); ALWS «mediana/P80 con campione adeguato» (RM:1246); AVS (RM:1258).
- **Evidenza:**
  - b20s2: il tasso di errore passa da 12/300 a 9/150, chiave «dal 4% al 6%».
  - b14s3: da 6/30 a 9/60, chiave «dal 20% al 15%».
  - b15s3: 16/20 = 80%.
  - Le etichette «incertezza» compaiono solo nelle colonne dei laboratori (b20s2), non nelle chiavi dei quiz.
- **Analisi (calcolo eseguito):**
  - 12/300 contro 9/150: z ≈ 0,95, quindi la differenza non è distinguibile dal caso.
  - Intervalli di Wilson al 95%: 4% → 2,3–6,9%; 6% → 3,2–11,0%. Si sovrappongono.
  - 6/30 → 9,5–37,3%; 9/60 → 8,1–26,1%.
  - 16/20 → 58,4–91,9%. 21/25 → 65,3–93,6%.
- **Controesempio:** se uno studente risponde «la qualità peggiora, blocchiamo l'estensione» basandosi solo sul 4%→6%, prende una decisione su una differenza compatibile con zero. Le chiavi dei quiz premiano il calcolo, non la valutazione della sua affidabilità.
- **Inferenza:** il problema tocca anche gli standard: «campione adeguato» (ALWS) e la soglia «≤10 punti» (AES/AAS) non hanno una regola di decisione definita.
- **Impatto:** G03 e G07; validità delle decisioni nei capstone L3; robustezza delle soglie AVS.
- **Raccomandazione:**
  - Aggiungere all'AAS un descrittore obbligatorio per le conclusioni numeriche: incertezza dichiarata, campione e criterio decisionale fissato in anticipo.
  - In AES/ALWS/AVS sostituire «campione adeguato» con regole esplicite, per esempio una dimensione minima, o una dichiarazione di «indicatore non inferenziale» quando il campione è inferiore.
  - Non cambiare gli indici dei quiz: intervenire su teoria, feedback e laboratori.
- **Test proposto:** riesaminare tutte le chiavi che confrontano tassi o percentuali e marcare quelle in cui una conclusione decisionale sarebbe compatibile con il rumore.
- **Criterio di accettazione:** ogni item o laboratorio che chiede una decisione su tassi riporta la dimensione del campione e richiede di trattare l'incertezza; gli standard definiscono una regola di decisione numerica o la etichettano come indicativa.
- **Verifica necessaria:** documentale, poi simulazione AMVP (comportamento dei profili B04/B05).

### E04-03 — Con pochi item, le soglie AAS e ADS classificano in modo molto instabile
- **Priorità:** P1
- **Riferimenti:** AAS «quiz 80%», con 5–8 / 6–10 / 8–12 domande per verifica (RM:1234); ADS D1 10, D3 12, D4 12, D5 15 item ed esonero teorico ≥85% (RM:1238); ACS teoria del badge ≥80% (RM:1250).
- **Evidenza:** le soglie sono espresse in percentuale; il numero di item è un intervallo.
- **Analisi (modello binomiale, calcolo eseguito; ipotesi di item indipendenti con uguale difficoltà):**
  - Soglia effettiva AAS: 5 item → 4/5 (80%); 6 → 5/6 (83,3%); 8 → 7/8 (87,5%); 12 → 10/12 (83,3%). La stessa soglia nominale corrisponde a richieste diverse a seconda della forma della prova.
  - Probabilità di superare l'80% con padronanza reale dell'80%: 74% con 5 item, **50% con 8 item**, 56% con 12 item.
  - Con padronanza reale del 70%: 53% con 5 item, 26% con 8 item.
  - Soglia effettiva ADS: 9/10 (90%) per D1/D2/D6; **11/12 (91,7%)** per D3/D4; 13/15 (86,7%) per D5.
  - Con padronanza reale dell'85%, la probabilità di ottenere l'esonero è 54% (D1), 44% (D3/D4), 60% (D5). Con padronanza del 70% resta 9–15%, cioè rischio di falso esonero.
- **Impatto:**
  - I falsi esoneri e le false negazioni che l'ADS dichiara di voler validare sono strutturalmente elevati.
  - Le soglie effettive differiscono tra aree, in contrasto con «nessuna compensazione» e con l'uniformità tra i rami.
  - L'affidabilità dei badge è compromessa (G03, G04, G09).
- **Raccomandazione:**
  - Esprimere le soglie anche come numero di item per ogni forma della prova.
  - Prevedere una zona di incertezza attorno alla soglia, con una seconda forma equivalente.
  - Usare banche di item in cui l'esonero richieda più evidenze convergenti (teoria più prova pratica, già prevista).
  - Pianificare la stima di affidabilità e la taratura delle soglie quando esisteranno dati reali.
- **Test proposto:** subito, una simulazione Monte Carlo delle classificazioni per ogni forma; più avanti, analisi degli item su risposte reali.
- **Criterio di accettazione:** soglie per forma documentate; probabilità simulata di falso esonero (con padronanza reale ≤70%) inferiore a un valore approvato; regola di ripetizione nella zona di incertezza.
- **Verifica necessaria:** documentale e simulativa ora; empirica umana per la taratura (dipende da G12-E).

### E04-04 — La posizione della risposta corretta è prevedibile tra quiz base e avanzato
- **Priorità:** P1
- **Riferimenti:** RM:285, 324, 375, 422, 462, 513, 560, 607, 652 («264/264 coppie stessa posizione… UI non verificata»); vincolo di preservare gli indici (RM:20); quiz come parte della componente teoria (RM:1234).
- **Evidenza:**
  - In tutte le 264 sessioni il quiz base e il quiz avanzato hanno la risposta corretta nella stessa posizione.
  - Nel blocco Business 1–12 le posizioni sono 32/20/20: la prima posizione è giusta nel 44,4% dei casi.
  - Gli indici non possono essere cambiati.
- **Inferenza:** se l'interfaccia non mescola l'ordine delle opzioni (non verificato), basta rispondere al quiz avanzato «nella stessa posizione del base» per ottenere il 100% dopo aver visto la correzione del base.
- **Impatto:** il punteggio dei quiz avanzati non sarebbe una misura valida di ragionamento (G03). Contamina la componente teoria (20%) delle Level Credential.
- **Raccomandazione:**
  - Verificare in runtime l'ordine di presentazione.
  - Se non è mescolato, proporre in Fase 5 (con approvazione) un mescolamento solo in visualizzazione che lasci intatto l'indice memorizzato.
  - Nel frattempo, escludere i quiz come evidenza sufficiente per i badge.
- **Test proposto:** ispezionare il rendering su 20 sessioni campione; calcolare il punteggio ottenuto con la strategia «stessa posizione».
- **Criterio di accettazione:** l'ordine visualizzato è indipendente tra le due prove, oppure è documentato che i quiz non contribuiscono alle credenziali finché il problema non è risolto.
- **Verifica necessaria:** collaudo reale (runtime).

### E04-05 — DAX, Power Query, RLS, refresh e deploy: la competenza dipende dallo strumento e manca un percorso gratuito su tutti i sistemi operativi
- **Priorità:** P1
- **Riferimenti:** RM:195; matrice delle competenze «misure DAX… validare KPI e accessi» (RM:207); RM:603; parità (RM:1111); AES (RM:1242); b35s1–s3 (RM:596–598); BL2-P30–P32.
- **Evidenza testuale:**
  - «Power BI Desktop gratuito su Windows per DAX/Power Query reali; Mac/Linux Calc + SQL + BI locale per competenze trasferibili, non prova DAX/Power Query specifici».
  - «Cloud sharing, RLS remoto, refresh schedulato e Copilot non equivalgono a demo locale».
  - I permessi Metabase sono «edizione e granularità da verificare».
- **Inferenza:** non è stato deciso se DAX e Power Query siano competenze obbligatorie. Se lo sono, chi non ha Windows non ha un percorso gratuito equivalente, e questo viola AES («dichiarare OS», «nessun acquisto obbligatorio») e la parità tra Professional e Complete. Se non lo sono, la matrice di Fase 1 e la mappatura PL-300 vanno riformulate.
- **Ipotesi da verificare (non verificate):**
  - In Power BI Desktop la funzione «visualizza come ruolo» simula l'RLS ma non la applica a un utente reale.
  - L'applicazione effettiva dell'RLS e il refresh pianificato richiedono il servizio e licenze di condivisione.
  - Nella versione open source di Metabase potrebbero mancare i permessi a livello di riga.
- **Impatto:** G05, G06, G08 e G10; il capstone L2 («dashboard, controlli») non è dimostrabile allo stesso modo per tutti.
- **Raccomandazione:**
  - Definire le competenze in due livelli: uno trasferibile (modello a stella, misure, contesto di filtro, sicurezza a livello di riga, pipeline di aggiornamento con controllo della freschezza) e uno specifico per strumento.
  - Per l'RLS, prevedere una prova di applicazione reale e gratuita, per esempio policy RLS su PostgreSQL con due ruoli e un client BI che si connette per utente (ipotesi da collaudare).
  - Per il refresh, prevedere una pipeline locale pianificata con log degli errori.
  - Dichiarare DAX come obbligatorio solo se esiste un ambiente gratuito per ogni sistema operativo dichiarato.
- **Test proposto (4D):** per ogni sistema operativo dichiarato, eseguire il laboratorio RLS con due utenti (lettura consentita e incrociata negata) e un refresh forzato con fallimento simulato, registrando atteso ed effettivo.
- **Criterio di accettazione:** per ogni competenza obbligatoria esiste almeno un percorso gratuito collaudato (stato «lab verificato») per ogni sistema operativo dichiarato; zero letture incrociate concesse nel test negativo.
- **Verifica necessaria:** verifica delle risorse esterne, poi collaudo reale.

### E04-06 — La sequenza interna di L2 non è definita e la composizione cambia tra 2D e 2E
- **Priorità:** P2
- **Riferimenti:** proposta 2D di +30 (Excel 4, SQL 6 «SELECT/tipi/chiavi; WHERE/CASE/NULL; GROUP BY/HAVING; JOIN; CTE/subquery/window; verifica AI», RM:603); 2E BL2-P06–P35 (RM:1080–1109); L2 = settimane 21–36 (RM:652); 2B «anticipando matematica/Excel» (RM:241).
- **Evidenza:**
  - In 2E i segnaposto SQL sono 4 (P10–P13). CASE, gestione dei NULL, HAVING e funzioni finestra non compaiono esplicitamente.
  - Non c'è nessun segnaposto Excel/Calc.
  - Capstone e sicurezza passano da 3 a 6 (P30–P35).
  - Le fonti dei segnaposto SQL sono codificate «Q» (Power Query).
  - Il blocco GA4 (21–24, con funnel, CAC ed esperimenti) viene prima della preparazione dei dati, dell'SQL e della statistica.
- **Inferenza:**
  - Il totale (30) resta invariato, ma la ridistribuzione non è motivata da nessuna parte.
  - L'ordine dei segnaposto nel livello non è definito, quindi alcuni contenuti potrebbero richiedere competenze insegnate dopo: b24s2 (disegno di esperimenti) prima di BL2-P23–P25; b26s1 (lookup con chiavi) rispetto a BL2-P12.
  - Le competenze SQL dei professionisti (NULL a tre valori, funzioni finestra) rischiano di mancare.
- **Impatto:** G01; sequenza dei prerequisiti; copertura del badge SQL Analytics.
- **Raccomandazione:**
  - Costruire un grafo delle dipendenze tra competenze, con archi di prerequisito, per L1–L3 Business.
  - Riconciliare per iscritto la composizione 2D e 2E.
  - Esplicitare nel percorso SQL: tipi, NULL, CASE, HAVING, JOIN, anti-join, CTE, funzioni finestra, parametrizzazione e verifica con risultati attesi.
- **Test proposto:** controllo automatico sull'ARTM, in modo che nessuna sessione richieda competenze introdotte da una sessione successiva.
- **Criterio di accettazione:** zero riferimenti in avanti non dichiarati; scostamenti 2D/2E motivati e approvati; ogni voce del badge SQL Analytics coperta.
- **Verifica necessaria:** documentale, poi verifica delle risorse SQL.

### E04-07 — Lo stesso ID ha contenuti diversi tra l'audit 2D e la mappatura 2E
- **Priorità:** P2
- **Riferimenti:** 2D (RM:519–554, 566–601, 613–648) e 2E (RM:1027–1074, 1120–1179).
- **Evidenza (stessi ID):**

| ID | Contenuto in 2D | Contenuto in 2E |
|---|---|---|
| b14s1 | dataset con chiavi, null, deduplica (quiz sulla qualità dei dati) | stakeholder e consenso simulato |
| b13s2 | schema dei campi, dominio delle quantità | matrice di scelta degli strumenti |
| b17s2 | guasto CRM, riconciliazione | journey cliente |
| b38s1 | mapping e unità | router e filtri |
| b39s1 | filtro AND | mapping e tipi |
| b41s1 | idempotenza con vincolo univoco | classificazione degli errori |
| b25s3 | file pulito, log anomalie | ricavi e costi riconciliati |
| b33s1 | statistica descrittiva | analisi delle anomalie |

  La 2E dichiara che per L2 la retroclassificazione 2D resta autorevole (RM:1022), ma per L3 non dice nulla sul contenuto.
- **Ipotesi:** in L3 (b38–b41) sembra esserci uno slittamento di una riga.
- **Impatto:** l'evidenza sulla qualità dei dati (b14s1) e quella di statistica descrittiva (b33s1) rischiano di sparire dall'ARTM (G01, G02, R01, R11).
- **Raccomandazione:** fissare una regola di prevalenza per ogni ID; riconciliare riga per riga prima di compilare l'ARTM.
- **Test proposto:** confronto automatico tra le colonne 2D e 2E per i 144 ID Business, con revisione manuale delle divergenze.
- **Criterio di accettazione:** 144/144 ID con laboratorio ed evidenza riconciliati e motivati; zero competenze perse senza decisione.
- **Verifica necessaria:** documentale.

### E04-08 — Chiavi aritmeticamente corrette, ma con difetti concettuali
- **Priorità:** P2
- **Riferimenti e controesempi:**
  - **b21s3 avanzato** (RM:545), «tre sessioni e due acquisti → Uno [utente]». *Ipotesi:* in GA4 gli utenti si contano per identificatore (dispositivo/browser o user-ID). La stessa persona su due dispositivi senza user-ID conta come 2 utenti. La chiave è vera solo con un'ipotesi di identità che non viene dichiarata.
  - **b21s2 base** (RM:544), «rapporto acquisti per sessione espresso in percentuale → 4%». Un rapporto eventi/sessioni può superare il 100% e non è una proporzione. Il problema è già segnalato (RM:556) ma non risolto.
  - **b21s1 avanzato**, «100 visite e 5 acquisti»: «visite» non è una metrica GA4.
  - **b02s2 / b26s1 / b32s3** (riconciliazione della differenza netta: 10 ordini, 100 €, 5 k€). *Controesempio:* 12 ordini in eccesso e 2 mancanti danno la stessa differenza netta di 10. La riconciliazione richiede un abbinamento riga per riga (anti-join), non solo la differenza dei totali.
  - **b15s3 / b42s3**: il laboratorio prevede matrice di confusione e precision/recall per classe, ma la prova misura solo l'accuratezza. Su classi sbilanciate (per esempio 18 normali e 2 urgenti) un classificatore che dice sempre «normale» ha accuratezza del 90% e recall sugli urgenti pari a 0.
  - **b23s3** chiama «margine netto» quello che è un margine dopo il costo di acquisizione. **b33** usa due convenzioni di segno degli scostamenti senza esplicitarle.
  - **b31s3** ha quiz base e avanzato identici (già segnalato).
  - **cr-w11s2** prevede un laboratorio «CRUD parametrizzato» ma la chiave del quiz è un `SELECT *` con valore letterale.
- **Impatto:** G03; i concetti fondamentali di GA4 e della riconciliazione possono consolidare idee errate.
- **Raccomandazione:** correggere i testi di teoria, le spiegazioni e i feedback senza cambiare gli indici; aggiungere item su ID e identità, abbinamento riga per riga e recall per classe.
- **Test proposto:** revisione mirata degli item citati; verificare la definizione di utente sulla documentazione ufficiale GA4.
- **Criterio di accettazione:** ogni chiave corretta sotto ipotesi esplicite; nessun item richiede di inferire l'identità di un utente o di chiudere una riconciliazione senza abbinamento delle righe.
- **Verifica necessaria:** documentale, poi verifica delle risorse esterne (GA4).

### E04-09 — Laboratori GA4: fattibilità, terminologia e criteri di prova non definiti
- **Priorità:** P2
- **Riferimenti:** RM:92 («la terminologia delle conversioni va riesaminata»); RM:556; RM:1023; RM:1075–1079; RM:1111.
- **Evidenza:**
  - Proprietà di test con eventi sintetici; la demo richiede login; la verifica del consenso è da fare.
  - La terminologia delle conversioni non è stata riesaminata.
  - Nessun criterio di accettazione per DebugView o per i tempi di elaborazione.
- **Ipotesi da verificare:**
  - GA4 avrebbe rinominato le «conversioni» in «eventi chiave».
  - Nelle proprietà con pochi dati, i report standard potrebbero avere ritardi di elaborazione e soglie di privacy che nascondono dati. Un laboratorio basato solo sui report potrebbe quindi fallire anche se la raccolta è corretta.
- **Impatto:** G02, G08 e G10; il laboratorio potrebbe non essere riproducibile entro la durata prevista della sessione.
- **Raccomandazione:**
  - Separare analisi (sulla demo) e raccolta (proprietà di test, con prova tramite DebugView o vista in tempo reale ed export).
  - Allineare la terminologia alla documentazione vigente.
  - Fissare i criteri: evento visibile con i parametri attesi, nessun parametro PII, `transaction_id` deduplicato.
- **Test proposto:** collaudo 4D su una proprietà nuova con 10 eventi sintetici, misurando latenza e visibilità.
- **Criterio di accettazione:** 10/10 eventi verificati entro il tempo dichiarato; 0 PII; un solo acquisto registrato per `transaction_id`.
- **Verifica necessaria:** verifica delle risorse esterne, poi collaudo reale.

### E04-10 — Il quadro di qualità dei dati è incompleto, anche per l'ARTM stesso
- **Priorità:** P2
- **Riferimenti:** b14s1 (unicità, completezza, coerenza); BL2-P06 (contratto dati); ARTM (RM:1258).
- **Evidenza:**
  - Le dimensioni della qualità esplicitate sono 3.
  - L'ARTM è descritto per campi, senza chiavi, domini, vincoli d'integrità o versionamento dello schema; «matrice operativa non ancora compilata».
- **Inferenza:**
  - Mancano dimensioni come validità di dominio, accuratezza rispetto alla fonte, tempestività e freschezza come dimensione formale, e tracciamento della provenienza (lineage).
  - L'ARTM, con 420 record e registri collegati, è a sua volta un dataset esposto agli stessi difetti che il corso insegna a prevenire.
- **Impatto:** G01 e G02; affidabilità della tracciabilità AVS (R11, R12).
- **Raccomandazione:**
  - Creare una checklist di qualità dei dati usata da tutti i laboratori BI.
  - Scrivere un dizionario dati dell'ARTM: chiave (ID originale o segnaposto), stati enumerati, integrità referenziale R↔G↔test, controlli automatici di completezza.
- **Test proposto:** su un ARTM pilota di 20 record, controlli di unicità, valori ammessi e riferimenti orfani.
- **Criterio di accettazione:** zero chiavi duplicate, zero riferimenti orfani, 100% dei campi obbligatori valorizzati o marcati N/A con motivazione.
- **Verifica necessaria:** documentale, poi collaudo (script).

### E04-11 — R01–R12 tracciabili solo per titolo
- **Priorità:** P2
- **Riferimenti:** RM:1263, 1267, 1273–1292, 1322; RD:183.
- **Evidenza:**
  - Il registro ha due colonne (requisito, standard).
  - Il README dichiara «R01–R12 recuperato 12/12».
  - La ROADMAP registra la mancanza di IMG_9493–9499, il mancato recupero dell'IMG_9497 originale e la nota «non si attesta una trascrizione integrale».
  - R02 «applicazione pratica e autonomia» non coincide con G02 «riproducibilità pratica»; R12 «validazione e revisione critica» non coincide con G12 «efficacia formativa».
  - R10 (sicurezza e privacy) è assegnato solo ad AVS, che non contiene controlli tecnici.
- **Inferenza:**
  - La coerenza con gli standard è verificabile solo a livello di nome.
  - Mancano criteri di accettazione, il metodo di verifica e la corrispondenza R↔G↔campi ARTM.
  - «12/12» descrive il recupero dei titoli, non l'integralità del contenuto.
- **Impatto:** tracciabilità debole per R03, R06 e R09, centrali per E04.
- **Raccomandazione:**
  - Creare una matrice R × G × clausola dello standard × tipo di prova × ID di test.
  - Dichiarare nel README la portata esatta di «12/12».
  - Non ricostruire le parti mancanti.
- **Test proposto:** per ogni Rn, individuare almeno una clausola testuale dello standard citato e un gate.
- **Criterio di accettazione:** 12/12 requisiti con clausola, gate e tipo di prova; scarti R↔G motivati.
- **Verifica necessaria:** documentale (le immagini originali non sono tra i materiali autorizzati).

### E04-12 — G12-S / G12-E: affermazioni di qualità sostenibili, e possibile irraggiungibilità di V5 e V6
- **Priorità:** P1
- **Riferimenti:** RM:1258–1259, 1294–1299; ACS (RM:1250); AAS «soglie da validare» (RM:1234); nome «Excellence Learning» (RD:1).
- **Evidenza:**
  - Gli stati AVS vanno da V5 «validata didatticamente» a V6 «accettata».
  - AMVP: «efficacia empirica umana non dimostrata», nessun test umano disponibile.
  - ACS assegna «With Distinction» e Level Credential su soglie che non sono ancora state validate.
- **Inferenza:** il testo non chiarisce se V5 richieda G12-E. Se lo richiede, senza dati umani nessuna sessione può arrivare a V6, e il rapporto tra rilascio e V6 non è definito.
- **Affermazioni sostenibili senza G12-E** (subordinate alla chiusura reale dei gate pertinenti, senza deroghe ad AVS):
  1. «Progettato secondo gli standard interni AELS, AAS, ADS, AES, ALWS e ACS (versione X)», cioè conformità di progettazione, non di risultato.
  2. «Revisionato documentalmente (V2)» e «laboratorio collaudato su ambiente e data dichiarati (V3)».
  3. «Equivalenza gratuito/premium verificata su N esecuzioni pilota (V4)», con N e limiti dichiarati.
  4. «Simulazioni AMVP eseguite (G12-S) con questi esiti», accompagnato dalla frase «non indicano apprendimento umano».
  5. «Copertura documentale degli obiettivi pubblici PL-300 o PL-900 alla data X», non la probabilità di superare l'esame.
  6. «Credenziale interna a criterio, con soglie non ancora tarate empiricamente».
- **Affermazioni non sostenibili:**
  - efficacia, apprendimento, ritenzione, tempo per acquisire una competenza, ore effettive;
  - «professionista junior» o equivalenza a profili o certificazioni;
  - «eccellenza», superiorità sul mercato, tassi di superamento;
  - validità predittiva dei badge.
- **Impatto:** G09 e G12; rischio di affermazioni implicite, anche attraverso il nome «Excellence».
- **Raccomandazione:**
  - Tenere un registro delle affermazioni, ognuna con stato AVS minimo, evidenza e formula obbligatoria.
  - Chiarire per iscritto se V5 richieda G12-E e cosa succede alle credenziali in sua assenza, senza ridefinire i criteri.
- **Test proposto:** revisione dei testi rivolti agli studenti (Fase 4C/5) rispetto al registro delle affermazioni.
- **Criterio di accettazione:** zero affermazioni di efficacia senza G12-E; ogni credenziale riporta la propria natura e lo stato della taratura.
- **Verifica necessaria:** documentale ora; empirica umana per qualunque affermazione di efficacia.

### E04-13 — Il carico (ALWS) è coerente sulla carta ma non validabile con AMVP
- **Priorità:** P2
- **Riferimenti:** RM:1246; AMVP «tempo risposta AI non tempo umano» (RM:1259).
- **Evidenza:**
  - Aritmetica ALWS verificata e corretta.
  - Business senza sovrapposizioni 500,25 h, con riserva 575,29 h.
  - Riferimento Google Data Analytics: circa 260 h (scenario) e 187 h (dato FIBAA storico).
- **Inferenza:**
  - G07 non può essere chiuso con la sola AMVP: mediana e P80 richiedono tempi umani.
  - I tempi di installazione degli strumenti BI (Power BI, Docker, n8n, Metabase) sono la componente più variabile e non hanno una stima separata.
- **Impatto:** G07; affermazioni su ore e durata.
- **Raccomandazione:**
  - Etichettare tutte le ore come «nominali».
  - Separare il tempo tecnico di installazione per strumento e sistema operativo.
  - Pianificare misure umane quando saranno disponibili.
- **Test proposto:** in 4D, cronometrare l'installazione di ogni strumento BI per sistema operativo (tempo tecnico, non didattico).
- **Criterio di accettazione:** tempi tecnici misurati per ogni ambiente dichiarato; nessuna affermazione su ore effettive senza dati umani.
- **Verifica necessaria:** collaudo reale ed empirica umana.

### E04-14 — Benchmark BI e posizionamento dello scripting
- **Priorità:** P2
- **Riferimenti:** RM:217–228; ALWS (RM:1246); ACS candidati (RM:1250); AES con Python/R/Jupyter (RM:1242); b36s2 voucher (RM:600, 603).
- **Evidenza:**
  - Il dato Google Data Analytics (260 h, FIBAA 187 h) compare senza URL nei documenti.
  - La fonte Caltech è una brochure del 2024 («offerta corrente da riconfermare»).
  - Il percorso Business non contiene Python o R, presenti invece tra i candidati AES e nei benchmark citati (Caltech include Python).
  - Il voucher del 50% non è verificato.
- **Inferenza:** non è dichiarato se lo scripting analitico sia escluso per scelta. Il confronto con i benchmark rischia di essere asimmetrico.
- **Impatto:** G08; credibilità del profilo di uscita «business/data analyst» (RM:195).
- **Raccomandazione:**
  - Aggiungere URL e data per ogni dato di benchmark.
  - Decidere ed esplicitare il perimetro dello scripting: escluso, facoltativo o obbligatorio.
  - Rimuovere ogni promessa di voucher non verificata.
- **Test proposto:** verifica delle fonti ufficiali datate nella fase di benchmark.
- **Criterio di accettazione:** 100% dei dati di benchmark con URL, data e versione; decisione su Python/R registrata.
- **Verifica necessaria:** verifica delle risorse esterne.

### E04-15 — Non è chiaro come gli esoneri interagiscano con i badge di teoria
- **Priorità:** P2
- **Riferimenti:** ADS (RM:1238); ACS «Badge teoria pertinente ≥80%… esoneri solo registro» (RM:1250); coerenza ADS/ACS (RM:1265).
- **Evidenza:** chi segue il Professional Track può essere esonerato dalla teoria statistica ed economica (D3, D4, D5 ≥85%), mentre i badge Applied Statistics e Business Economics richiedono una teoria ≥80%.
- **Inferenza:** non è definito se il punteggio diagnostico valga come evidenza teorica per il badge. Se vale, si usa uno strumento di 12 item (vedi E04-03); se non vale, chi è esonerato deve comunque sostenere la teoria.
- **Impatto:** G04 e G09; parità di riconoscimento tra i due rami.
- **Raccomandazione:** fissare una regola esplicita; preferibilmente, il punteggio diagnostico vale solo se raggiunge la soglia del badge con lo stesso numero di item richiesto dall'AAS.
- **Test proposto:** simulazione AMVP dei profili B02 e B05 su entrambi i rami.
- **Criterio di accettazione:** regola documentata; nessun badge rilasciato su evidenze più deboli di quelle richieste a chi segue il Complete Track.
- **Verifica necessaria:** documentale, poi simulazione AMVP.

### E04-16 — L'interazione delle soglie ACS/AAS produce una compensazione implicita
- **Priorità:** P3
- **Riferimenti:** RM:1234, 1250.
- **Evidenza (calcolo):**
  - Teoria 80, pratica 75, capstone 80 danno un totale di 78, inferiore a 80.
  - Con teoria 80 e pratica 75 serve un capstone ≥85.
  - I minimi della rubrica (3, 2, 3, 2, 2, 2) danno P = 62,5, sotto la soglia di 75.
- **Inferenza:** non è una contraddizione formale, ma la fascia «75–79 competente ordinario» porta al conseguimento solo se compensata altrove. Questo è in tensione con «senza compensazioni» e può confondere gli studenti.
- **Raccomandazione:** spiegare con esempi numerici le combinazioni minime che portano al conseguimento.
- **Test e criterio di accettazione:** una tabella di casi limite pubblicata nello standard.
- **Verifica necessaria:** documentale.

### E04-17 — Le sezioni sullo stato corrente sono superate
- **Priorità:** P2
- **Riferimenti:** RM:3 («Aggiornato: 25 novembre 2026»); RM:26–41; RM:55–60 («Prossimo intervento: Fase 2C…»); RD:3, RD:32 («Prossimo passo 2C»); procedura permanente (RM:67).
- **Evidenza:** le sezioni in testa ai due documenti indicano come prossimo passo la Fase 2C, mentre lo stato reale è la Fase 3I approvata (RM:1269, RD:183).
- **Impatto:** violazione della procedura di coerenza; rischio che chi riprende il lavoro in una nuova conversazione parta dal punto sbagliato (Regola 1).
- **Raccomandazione:** aggiornare i riepiloghi in testa, oppure marcarli esplicitamente come storici.
- **Test proposto:** confronto automatico tra il «prossimo passo» dichiarato in ogni sezione di stato.
- **Criterio di accettazione:** un solo «prossimo passo» corrente, coerente nei due documenti.
- **Verifica necessaria:** documentale.

### E04-18 — Le sigle sono ambigue
- **Priorità:** P3
- **Riferimenti:** RM:1022 («T» usato sia come stato sia come codice fonte); «P» usato per parità candidata, propedeutica, premium, fonte Power Platform e priorità P0–P3; RM:1115.
- **Impatto:** rischio di errori nella compilazione e nelle query sull'ARTM.
- **Raccomandazione:** un vocabolario controllato con prefissi univoci, per esempio `ST-`, `SRC-`, `BR-`.
- **Criterio di accettazione:** nessuna sigla con più di un significato nell'ARTM.
- **Verifica necessaria:** documentale.

### E04-19 — Le prove autentiche hanno rischi di realismo e di indipendenza
- **Priorità:** P2
- **Riferimenti:** capstone L2 (RM:1111, 1234); «AI Assisted, Human Verified» (RM:1230); ACS «AI assistita non indipendente» (RM:1250); BL2-P26–P27.
- **Evidenza:** dataset sintetici; AI consentita e documentata; revisione umana «solo se disponibile».
- **Inferenza:**
  - Dati sintetici troppo puliti non mettono alla prova pulizia, riconciliazione e lettura critica.
  - Senza un valutatore indipendente, un capstone completato con l'AI può superare la rubrica senza che la competenza individuale sia dimostrata.
  - La difesa registrata è una mitigazione parziale.
- **Raccomandazione:**
  - Generare dataset con difetti seminati e una «verità di riferimento» nascosta (duplicati, NULL, unità miste, fan-out, periodi parziali).
  - Rendere obbligatoria una modifica dal vivo su un requisito nuovo durante la difesa.
  - Misurare la scoperta dei difetti con precision e recall dello studente sui difetti seminati.
- **Test proposto:** pilota 4B con un dataset contenente 10 difetti noti.
- **Criterio di accettazione:** la rubrica valuta esplicitamente i difetti individuati rispetto a quelli seminati; la difesa include un'attività non prevista.
- **Verifica necessaria:** documentale, poi simulazione AMVP, poi empirica umana.

## 11. Raccomandazioni e verifiche mancanti

**Prima della Fase 4** (documentali, senza modifiche applicative e senza chiudere gate):
1. Decidere se DAX e Power Query sono competenze obbligatorie o specifiche di uno strumento, e quale prova gratuita reale di RLS e refresh usare (E04-05).
2. Scrivere la mappa delle competenze statistiche e il grafo delle dipendenze di L2 (E04-01, E04-06).
3. Riconciliare 2D e 2E riga per riga (E04-07).
4. Fissare le regole numeriche per soglie per forma della prova, incertezza e «campione adeguato» (E04-02, E04-03).
5. Creare il registro delle affermazioni di qualità per G12 e chiarire il rapporto V5/V6 (E04-12).
6. Completare la matrice R×G e il dizionario dati dell'ARTM (E04-10, E04-11).
7. Aggiornare le sezioni di stato corrente (E04-17).

**Verifiche mancanti, per natura:**

| Natura | Verifiche |
|---|---|
| Risorse esterne | unità SQL e statistica; GA4 (terminologia, identità degli utenti, soglie di privacy, latenza); licenze e funzioni di Power BI free/Desktop; permessi Metabase per edizione; DuckDB; prezzi e voucher PL-300/PL-900; benchmark datati |
| Collaudo reale (4D) | RLS con due utenti per ogni sistema operativo; refresh con guasto; raccolta GA4 su proprietà di test; ordine delle opzioni nell'interfaccia; tempi di installazione |
| Simulazione AMVP (4E) | profili B02, B04 e B05 su esoneri, statistica e decisioni con piccoli campioni; scoperta dei difetti seminati |
| Empirica umana (G12-E) | taratura delle soglie, affidabilità degli item, tempi reali, efficacia; **non sostituibile** dalle verifiche precedenti |

## 12. Esito complessivo

**PARZIALE.**

- **Conforme:**
  - documenti integri e verificati;
  - aritmetica interna corretta;
  - affermazioni prudenti;
  - parità e limiti delle simulazioni impostati correttamente;
  - concetti di BI e qualità dei dati in larga parte appropriati.
- **Non conforme o da completare sul piano documentale:**
  - copertura statistica e risorse SQL e statistica (E04-01);
  - trattamento dell'incertezza (E04-02);
  - proprietà psicometriche delle soglie (E04-03);
  - prevedibilità delle risposte (E04-04);
  - percorso gratuito per DAX, RLS e refresh su tutti i sistemi operativi (E04-05);
  - tracciabilità 2D↔2E e R↔G (E04-07, E04-11).
- **Non verificabile in questa revisione:** tutto ciò che richiede risorse esterne, collaudi o dati umani.

Questo esito è una **revisione documentale AI**. Non è una simulazione AMVP, né un collaudo reale, né una misura di efficacia empirica. Non chiude alcun gate (0/12), non modifica gli standard approvati e non autorizza la Fase 4.
