# CR-001 — E05 — Business Transformation Review Report

Progetto: AI Creator Academy — Excellence Learning 6.6
Repository: itopo-ai/AI-Creator-Academy — checkpoint `f9d98c2bbd4d3622b9ccb5eeeb5c1811a2c4d401`
Natura: revisione documentale simulata da AI esterna. Non è un audit umano indipendente, non chiude gate, non autorizza rilasci né l'avvio della Fase 4.

---

## 1. Modello AI, versione e data

- Modello: Claude Opus 5.5 (identificativo `claude-opus-5-5`), sviluppato da Anthropic.
- Data della revisione: 26/11/2026 (fuso Europe/Rome).
- Limite di conoscenza affidabile dichiarato dal modello: giugno 2026. Nessuna ricerca web eseguita: le affermazioni dei documenti su fonti esterne (prezzi, quote, licenze, programmi d'esame) **non** sono state riverificate e sono trattate come dichiarazioni dei documenti.
- Ambiente: area di lavoro Linux isolata, Git in sola lettura, Python per ricalcoli.

## 2. Ruolo specialistico

Prospettiva E05 del protocollo AMVP: processi, strategia e trasformazione aziendale, economia applicata, process management, automazione, adozione dell'AI e governance. Ambito specifico: percorso Business & Data (tre livelli, rami Professional/Complete), capstone Business, prototipo 4B «AI Pilot & ROI Decision System», più il mandato comune CR-001 (registro R01–R12, distinzione G12-S/G12-E, affermazioni di qualità sostenibili).

Il ruolo è simulato: il rapporto non sostituisce il giudizio di un esperto umano di business transformation, di un economista d'impresa o di un giurista.

## 3. Capacità e limiti

**Capacità effettivamente esercitate**
- Accesso al commit esatto, estrazione dei due soli file autorizzati, verifica crittografica dei blob, conteggio di righe e caratteri.
- Lettura integrale di entrambi i documenti in segmenti consecutivi, con controllo specifico che le righe più lunghe (fino a 3.882 caratteri) non fossero troncate.
- Ricalcolo aritmetico di tutte le cifre di ROI, margini, tassi, conteggi e monte ore citati nei documenti; calcoli statistici (intervalli di Wilson al 95%, test esatto di Fisher, distribuzione binomiale per i test diagnostici, dimensione campionaria approssimata).
- Ricerca terminologica mirata su entrambi i testi.

**Limiti**
- Non ho letto i curriculum JSON, il codice applicativo né altri file: le affermazioni dei documenti sul contenuto delle 264 sessioni non sono verificabili alla fonte. Dove rilevo incoerenze interne tra due rappresentazioni dello stesso ID, non posso stabilire quale sia corretta.
- Nessuna verifica online di risorse, prezzi, quote, licenze, esami.
- Nessun collaudo runtime, nessuna esecuzione di laboratori, nessuna simulazione di studenti.
- Le valutazioni giuridiche (es. normativa UE sull'AI, protezione dati, monitoraggio dei lavoratori) sono segnalazioni di rischio da verificare con fonti e professionisti qualificati; non costituiscono parere legale.
- Le immagini sorgente citate dalla Fase 3I non mi sono state fornite; non ne ricostruisco il contenuto.

## 4. Bias e potenziali conflitti

- **Conflitto di fornitore.** Sono un modello Anthropic. I documenti citano risorse Anthropic come candidate (Anthropic AI Fluency, documentazione Claude: ROADMAP r. 664, r. 695, r. 837, r. 839) e designano Claude come revisore esterno (Regola permanente 3, AMVP). Non ho espresso giudizi su tali risorse; ogni loro eventuale preferenza va valutata da un revisore non legato al fornitore.
- **Bias di accordo e di coerenza formale.** Documenti molto strutturati e auto-limitanti possono indurre un modello a sovrastimarne la solidità. Ho cercato attivamente controesempi e ricalcoli per contrastare questo effetto.
- **Bias di dominio.** La mia conoscenza di business transformation deriva da letteratura e pratica documentata in inglese prevalentemente nordamericana ed europea; può sottorappresentare prassi italiane o di PMI.
- **Assenza di garanzia.** Nessuna dichiarazione di imparzialità di un modello AI è verificabile dall'esterno (coerente con AMVP: «bias-conflitti non garantiti»).

## 5. Indipendenza procedurale

- Non ho consultato altri rapporti CR-001, analisi del coordinatore, documenti successivi al checkpoint, né altri file del repository.
- Accessi tecnici accidentali da dichiarare: per ottenere il commit ho eseguito un clone parziale senza checkout e senza contenuti dei file (`--filter=blob:none --no-checkout`), poi `git fetch` del solo commit indicato. Questo ha scaricato metadati di Git (oggetti commit e alberi), non il contenuto di altri file. Ho visualizzato l'elenco dei due soli percorsi autorizzati e il messaggio del commit di checkpoint («docs: align phase 3I status with recovered evidence», 26/11/2026 12:52 +0100). Non ho aperto, letto o elencato altri file.
- Nessuna conclusione di altre conversazioni utilizzata. Questa conversazione non contiene altri rapporti.

## 6. Ambito, materiali e checkpoint

| Elemento | Valore |
|---|---|
| Commit | `f9d98c2bbd4d3622b9ccb5eeeb5c1811a2c4d401` |
| README.md | blob `abca6f1ce6345ed1cc55eb5dd5f78ff0a7232afb`, 183 righe, 54.465 caratteri |
| ROADMAP.md | blob `af9888bc28f0fef48ea226e86fe3be5a24913008`, 1.322 righe, 287.684 caratteri |

I riferimenti nel rapporto usano la forma «README r. N» e «ROADMAP r. N» (numerazione di riga al checkpoint).

## 7. Esito della verifica preliminare

| Verifica | Metodo | Esito |
|---|---|---|
| Accesso al commit esatto | `git fetch --depth=1 origin <SHA>`; `git cat-file -t` → `commit` | Superata |
| Blob SHA nell'albero del commit | `git ls-tree <SHA> README.md ROADMAP.md` | Superata: entrambi coincidono con gli attesi |
| Blob SHA ricalcolati sul contenuto estratto | `git hash-object` sui file estratti con `git show <SHA>:<file>` | Superata: entrambi coincidono |
| Numero di righe | `wc -l` | Superata: 183 e 1.322 |
| Lunghezza in caratteri Unicode | Python `len()` su testo UTF-8 | Superata: 54.465 e 287.684 |
| Lettura integrale | Strumento di lettura per segmenti consecutivi: README 1–183; ROADMAP 1–236, 237–373, 374–459, 460–558, 559–654, 655–753, 754–829, 830–956, 957–1020, 1021–1113, 1114–1223, 1224–1260, 1261–1300, 1301–1322. Un tentativo sul blocco 237–461 è stato rifiutato per dimensione prima di restituire contenuto ed è stato risegmentato. | Superata, nessuna lacuna |
| Assenza di troncamenti | Confronto della lunghezza e della parte finale delle quattro righe più lunghe di ciascun file con quanto letto | Superata |
| Coerenza dei paragrafi duplicati README/ROADMAP | Confronto carattere per carattere di 12 coppie (standard 3A–3H, regola 3, parità, rami) | Identici 12/12 |

Esito: accesso integrale a entrambi i documenti confermato. La revisione può procedere.

## 8. Metodo di revisione

1. Lettura integrale e lineare dei due documenti, con annotazione delle affermazioni pertinenti al mandato E05.
2. Ricostruzione della progressione Business L1/L2/L3 dalle tabelle per ID della Fase 2D (ROADMAP r. 460–652) e dalle matrici della Fase 2E (r. 957–1218), poi confronto con standard AELS, AAS, ADS, AES, ALWS, ACS, AVS/AMVP (r. 1224–1259) e con il registro della Fase 3I (r. 1262–1322).
3. Ricalcolo di ogni cifra economica, percentuale e monte ore. Esito: **nessun errore aritmetico rilevato** nelle chiavi dei quiz Business riportate (es. ROI 50%, 0%, −25%; margine ponderato 27,5%; TCO a 12 mesi 3.400 vs 2.600; saldo cassa 9.000/7.000), nei conteggi C/M (115/29), nelle proposte di ampliamento (+90 Business, +66 Creator, 420 totali, +59,1%) e nell'ALWS (338,5; 420,25; 758,75 h; 108,39 min medi; +187,4%; 414,5; 500,25; 476,675; 575,2875 h).
4. Ricerca terminologica su concetti attesi per il profilo dichiarato (es. attualizzazione, intervallo di confidenza, randomizzazione, BPMN, normativa UE sull'AI, protezione dati, monitoraggio dei lavoratori).
5. Costruzione di controesempi numerici e ricalcoli statistici.
6. Classificazione delle anomalie secondo la scala AVS (P0–P3), con distinzione esplicita tra **evidenza** (testo citato) e **inferenza**.

Convenzione sulla natura della verifica necessaria: **[D]** revisione documentale; **[S]** simulazione AI; **[T]** collaudo tecnico reale; **[E]** efficacia empirica su studenti umani; **[X]** verifica esterna (fonte ufficiale, esperto umano, giurista).

## 9. Punti di forza

1. **Onestà epistemica eccezionale per un documento di progetto.** Distinzione costante tra dichiarato, documentato, verificato e collaudato; «0 accettate AVS», «0/12 gate chiusi», «0/2 prototipi collaudati» (README r. 183); concept 4B dichiarato esplicitamente come «illustrativo con dati fittizi, non risultati sperimentali» (ROADMAP r. 1318).
2. **Correttezza aritmetica.** Tutti i calcoli verificati nelle tabelle Business e nell'ALWS sono corretti (§8).
3. **Consapevolezza di attribuzione e incrementalità già presente nei contenuti.** b12s2 «limiti attribuzione», b24s1 «Attribuzione vs incrementalità», b24s2 esperimento con assegnazione casuale (ROADMAP r. 500, 552–554); b07s3 «distinzione capacità liberata/risparmio monetario» (r. 486).
4. **Misure end-to-end e controesempi di ottimizzazione locale.** b15s2: inserimento 5→2 min, approvazione 3→7, totale 8→9 (r. 526); b20s1–s2: tassi per ordine e non conteggi assoluti (r. 540–541); b29s3: 2% di righe ma 30% dei ricavi (r. 580).
5. **Cultura del controllo nei flussi automatici.** Idempotenza, retry limitati, deduplica, separazione richiedente/approvatore, prove negative sui permessi, astensione ed escalation degli agenti (r. 613–648).
6. **Gate di qualità prima dell'estensione.** b05s3 e b20s3 (riduzione dei tempi ma peggioramento della qualità → non estendere) (r. 480, 542).
7. **Parità gratuito/premium trattata come requisito da dimostrare**, non come risultato (README r. 73, 89; AES r. 1242), con riconoscimento esplicito dei vincoli su Entra ID, trial, Windows e quote (r. 1116, 1218).
8. **AAS con errori critici non compensabili** e pesi espliciti (r. 1234).
9. **Separazione esonero teorico / esonero applicativo** nei rami Professional/Complete (README r. 102; ADS r. 1238).
10. **AMVP realistico sui propri limiti**: impossibilità di cancellare la conoscenza del modello, tempo AI ≠ tempo umano, scenari non indipendenti (r. 1259).

## 10. Osservazioni e anomalie

Riepilogo:

| ID | Priorità | Titolo |
|---|---|---|
| E05-01 | P1 | «Holdout» ambiguo e assenza di una strategia di identificazione causale nei piloti e nel prototipo 4B |
| E05-02 | P1 | Assenza di inferenza statistica nelle decisioni go/no-go |
| E05-03 | P1 | Fondamenti economici incompleti: nessuna attualizzazione, contenuti di economia aziendale non esistenti |
| E05-04 | P1 | Ramo Complete non dimensionato rispetto alla promessa; cifra di 30 h non tracciabile |
| E05-05 | P1 | Incoerenza di tracciabilità per ID tra matrici 2D e 2E (Business L2/L3) |
| E05-06 | P1 | Fattibilità gratuita del L3 Business dipendente da tenant Microsoft |
| E05-07 | P2 | Affidabilità della diagnostica ADS per gli esoneri |
| E05-08 | P2 | Criteri go/no-go e di arresto non standardizzati |
| E05-09 | P2 | Progressione L1→L3 e coerenza tra profilo, nome del livello e capstone |
| E05-10 | P2 | Metodi di analisi dei processi assenti |
| E05-11 | P2 | Governance: quadro normativo UE e tutela dei lavoratori non trattati |
| E05-12 | P2 | Change management, adozione e supervisione umana poco misurabili |
| E05-13 | P2 | Laboratori ROI: dati sintetici senza effetto vero noto; etichettatura delle evidenze nel portfolio |
| E05-14 | P2 | Concept 4B: risparmio orario non monetizzato e TCO assente |
| E05-15 | P2 | Registro R01–R12: tracciabilità R↔G implicita e provenienza parziale |
| E05-16 | P2 | Riepiloghi correnti non aggiornati (violazione della procedura permanente) |
| E05-17 | P3 | Soglie AAS/ACS: interazione non esplicitata |
| E05-18 | P3 | Classificazione M apparentemente guidata dall'aritmetica dei quiz |

Non rilevo anomalie P0: nessuna modifica applicativa, nessun rilascio, nessun dato reale in uso.

---

### E05-01 — «Holdout» ambiguo e assenza di una strategia di identificazione causale nei piloti e nel prototipo 4B

- **Priorità:** P1
- **Riferimenti:** README r. 154 (AAS, capstone L3 «baseline, holdout»), r. 178; ROADMAP r. 1099 (BL2-P25 «forecast baseline e holdout»), r. 1186 (BL3-P07 «qualità: holdout e bias»), r. 1205 (BL3-P26 «eval holdout»), r. 1218 (capstone L3 «baseline e holdout separato»), r. 1258, r. 1318 (concept 4B).
- **Evidenza testuale:** 4B: «baseline 100 h, AI + review 70 h, risparmio 30 h; […] Pilot validation: Holdout dataset» (r. 1318). Capstone L3: «pilota reale sandbox su richiesta/acquisto sintetico, baseline e holdout separato» (r. 1218). Altrove «holdout» indica set di valutazione separato dal tuning (r. 946: «30 casi holdout»; r. 1205). L'esperimento controllato compare solo in L2 marketing (b24s1–s3, r. 552–554). I termini «randomizzazione», «gruppo di controllo», «differenza nelle differenze» e «intervallo di confidenza» non compaiono in nessuno dei due documenti.
- **Inferenza:** il termine «holdout» è usato con due significati diversi: (a) dataset di valutazione non visto durante la messa a punto, che protegge dall'overfitting della qualità; (b) gruppo di controllo non trattato, che stima l'effetto incrementale. Il concept 4B («100 h → 70 h») descrive un confronto prima/dopo che non stima l'incrementalità. Un ROI calcolato così attribuisce all'AI anche effetti di apprendimento, stagionalità, diverso mix di casi o maggiore attenzione degli operatori.
- **Controesempio:** baseline di 100 h sul trimestre 1; pilota sul trimestre 2 a 70 h. Un gruppo non trattato passa nello stesso periodo da 100 a 80 h (mix più semplice, curva di apprendimento). Effetto incrementale stimato con differenza nelle differenze: (70−100) − (80−100) = −10 h, non −30 h. Con il ROI calcolato su 30 h il beneficio è triplicato; un go/no-go con soglia di 20 h risulterebbe «go» in modo infondato.
- **Impatto:** economico (decisioni di estensione su benefici sovrastimati); professionale (il profilo «referente operativo di piloti AI», r. 195, richiede proprio questa competenza); didattico (capstone e badge «ROI & TCO Analysis» certificherebbero un metodo non valido).
- **Standard, requisiti e gate:** AELS (piano di validazione riproducibile), AAS (correttezza, errori sostanziali), ACS (Capstone Credential L3, badge ROI & TCO Analysis, AI Value Assessment); R02, R03, R09; G02, G03, G09.
- **Raccomandazione:** nel glossario e nel brief 4B separare «set di valutazione separato» da «gruppo di controllo». Rendere obbligatoria nel capstone L3 e in 4B una sezione «Disegno di identificazione»: randomizzazione per caso o operatore; avvio scaglionato; differenza nelle differenze con gruppo di confronto; oppure dichiarazione esplicita «stima non causale» con relativi limiti. Rendere obbligatoria la discussione delle minacce alla validità: curva di apprendimento, mix dei casi, effetto osservatore, contaminazione tra gruppi, regressione verso la media.
- **Test proposto:** dataset sintetico con trend secolare piantato (es. −20% su tutti i casi) ed effetto vero dell'AI noto (−10%). Lo studente simulato deve stimare l'effetto incrementale e non quello lordo.
- **Criterio di accettazione:** 100% dei brief capstone L3 e 4B contengono la sezione di identificazione. Nel test, una stima che attribuisce all'AI il −30% lordo è errore critico AAS; una stima corretta cade entro ±3 punti percentuali dall'effetto vero o dichiara correttamente l'impossibilità di identificarlo.
- **Natura della verifica:** [D] per la correzione degli standard; [S] per il test con studenti simulati; [E] per l'efficacia didattica reale.

### E05-02 — Assenza di inferenza statistica nelle decisioni go/no-go

- **Priorità:** P1
- **Riferimenti:** ROADMAP r. 489 (b08s3), r. 541 (b20s2), r. 527 (b15s3), r. 630 (b42s3), r. 523 (b14s2), r. 1018 (capstone L1 «20 casi»), r. 1097–1099 (BL2-P23–P25), r. 1250 (badge Applied Statistics).
- **Evidenza testuale:** b08s3: «La soglia massima di errore è 2% e il test misura 3%. Cosa fai? → Sospendi l'estensione». b20s2: «10 ordini errati su 100; dopo, 8 su 40 […] Sale dal 10% al 20%». Capstone L1: «20 casi baseline e confronto». Nessuna occorrenza di intervallo di confidenza, potenza, effetto minimo rilevabile o regola del tre.
- **Inferenza:** le regole decisionali si basano su stime puntuali con campioni piccoli. Il sospendere in modo cautelativo è difendibile; il simmetrico «procedi» con un campione piccolo non lo è. Il curriculum insegna a calcolare tassi, non a stabilire se la differenza è distinguibile dal rumore.
- **Ricalcoli (Wilson 95%; Fisher esatto):**
  - b20s2: 10/100 = 10% [5,5%; 17,4%]; 8/40 = 20% [10,5%; 34,8%]; Fisher p = 0,16. L'aumento non è statisticamente distinguibile; la chiave «sale dal 10% al 20%» è corretta come descrizione, ma una decisione andrebbe accompagnata dall'incertezza.
  - b20s2 avanzato: 12/300 = 4% [2,3%; 6,9%] vs 9/150 = 6% [3,2%; 11,0%]; Fisher p = 0,35.
  - b15s3: 16/20 = 80% [58,4%; 91,9%]; b42s3: 21/25 = 84% [65,3%; 93,6%].
  - Controesempio decisionale: pilota con 0 errori su 20 casi rispetto a soglia 2%. Il limite superiore al 95% è 16,1% (regola del tre ≈ 15%): il risultato è compatibile con un tasso 8 volte la soglia, eppure una regola puntuale direbbe «go».
  - Per distinguere 2% da 4% (unilaterale α = 0,05, potenza 0,80) servono circa 391 casi, non 20–40.
- **Impatto:** economico (estensioni fondate su rumore); professionale (badge «Applied Statistics» e «AI Value Assessment» senza la competenza chiave per un analista); didattico.
- **Standard, requisiti e gate:** AAS (correttezza), ACS (badge citati), ADS D4; R01, R03; G01, G03.
- **Raccomandazione:** inserire in L2 (BL2-P23–P25) un nucleo esplicito di inferenza: intervalli per proporzioni (Wilson), regola del tre, bootstrap per mediane e tempi, effetto minimo rilevabile e dimensione campionaria, rischio di decisioni con test ripetuti. In L1 introdurre almeno la regola «campione piccolo → decisione condizionata». Riformulare le chiavi go/no-go sul limite dell'intervallo (es. «estendi se il limite superiore dell'errore è sotto il 2%»).
- **Test proposto:** batteria di 10 scenari go/no-go con campioni piccoli e grandi, in cui la decisione corretta cambia in base all'intervallo e non alla stima puntuale.
- **Criterio di accettazione:** ≥ 9/10 decisioni corrette nella chiave dell'esaminatore; zero chiavi go/no-go nei quiz Business riscritti basate esclusivamente su stime puntuali con n < 100 senza qualificazione dell'incertezza.
- **Natura della verifica:** [D], [S]; [E] per l'apprendimento reale.

### E05-03 — Fondamenti economici incompleti: nessuna attualizzazione, contenuti di economia aziendale non esistenti

- **Priorità:** P1
- **Riferimenti:** ROADMAP r. 959 («Fonte OpenStax contabilità tentata 404; teoria economica originale Academy da redigere, non dichiarare esistente»), r. 1003 (BL1-P05), r. 484–486 (b07s1–s3), r. 497 (b11s2), r. 1250 (badge Business Economics, ROI & TCO Analysis); README r. 134, r. 142.
- **Evidenza testuale:** il ROI insegnato è annuale semplice (b07s1: «12.000 euro e costi 8.000 […] 50%, sul periodo considerato»). Payback e sensibilità sono citati (r. 486, r. 1011). Nessuna occorrenza di attualizzazione, VAN/NPV, tasso di sconto, costo del capitale. L'unica sessione propedeutica economica proposta è BL1-P05 «costi, ricavi, margini e saldo».
- **Inferenza:** per un pilota pluriennale con investimento iniziale, il ROI semplice non discriminato nel tempo può invertire il segno della decisione. Il badge «Business Economics» L1 è oggi privo di un contenuto esistente, per dichiarazione stessa del documento.
- **Controesempio:** investimento 10.000 € iniziale, beneficio netto 4.000 €/anno per 3 anni. ROI semplice sul triennio: +20%, utile non attualizzato +2.000 €. VAN all'8%: 4.000 × 2,577 = 10.308 → +308 €. VAN al 12%: 4.000 × 2,402 = 9.607 → **−393 €**. La decisione cambia segno con il costo del capitale, variabile che il curriculum non introduce.
- **Ulteriore lacuna concettuale:** il «risparmio» orario (4B: 30 h) è capacità liberata, non flusso di cassa, salvo riallocazione o riduzione di costi effettivi. b07s3 lo menziona; né AAS né il brief 4B lo rendono requisito.
- **Impatto:** economico e professionale (business case non difendibili davanti a un controllo di gestione); credenziali (badge senza contenuto).
- **Standard, requisiti e gate:** AELS (correttezza/profondità), AAS, ACS; R01, R09; G01, G09.
- **Raccomandazione:** redigere i moduli interni di economia aziendale prima di 4B: costi fissi/variabili/marginali, costi affondati, costo opportunità, flussi di cassa, attualizzazione e VAN, payback attualizzato, capacità liberata vs risparmio monetario, costi nascosti (formazione del personale, revisione, rilavorazione degli errori, uscita dal fornitore). In L3 aggiungere valore aggiustato per il rischio e confronto tra portafogli di progetti.
- **Test proposto:** due business case in cui ROI semplice e VAN indicano decisioni opposte; un caso in cui il risparmio orario non genera cassa.
- **Criterio di accettazione:** lo studente simulato sceglie la decisione coerente con il VAN e dichiara il trattamento della capacità liberata in ≥ 90% dei casi; badge «Business Economics» privo di contenuto non attribuibile (stato «bloccato» in ARTM finché il modulo non è V2).
- **Natura della verifica:** [D] per l'esistenza dei contenuti; [X] revisione di un esperto umano di finanza aziendale raccomandata; [S]/[E] per l'efficacia.

### E05-04 — Ramo Complete non dimensionato rispetto alla promessa; cifra di 30 h non tracciabile

- **Priorità:** P1
- **Riferimenti:** README r. 102 (regola dei due rami); ROADMAP r. 195 (prerequisiti d'ingresso «alfabetizzazione digitale e aritmetica elementare»), r. 515 («Nessuna sessione esistente interamente P»), r. 958 (6 nuove: 3 P?, 3 D), r. 1001–1004, r. 1246 («30 h esonero simulato non accertato»), r. 1266 (C04).
- **Evidenza testuale:** il ramo Complete fornisce «preparazione matematica, statistica, economica e digitale necessaria» (README r. 102). Le sessioni propedeutiche teoriche proposte sono 3 (BL1-P03 percentuali, BL1-P04 statistica descrittiva, BL1-P05 costi/ricavi), più 3 digitali. Le 144 sessioni originali contengono 0 sessioni puramente propedeutiche.
- **Inferenza e ricalcolo:** 3 sessioni × 90 min = 4,5 h di teoria propedeutica esonerabile esplicitamente mappata. La cifra di 30 h di esonero simulato (ALWS) non è ricostruibile dai documenti: potrebbe includere componenti teoriche delle 29 sessioni M, ma la derivazione non è riportata. In entrambi i casi un profilo B04 («lacune matematiche») o B01 («principiante») con sola aritmetica elementare dovrebbe raggiungere ROI/VAN, statistica inferenziale (E05-02), SQL, DAX e misure non additive con 4,5 h di propedeutica dedicata più recupero non dimensionato.
- **Impatto:** equivalenza formativa (C04: «differiscono nella propedeutica, non nel livello professionale finale») non sostenibile se il Complete non colma davvero il divario; rischio di abbandono o di superamenti con valutazione permissiva.
- **Standard, requisiti e gate:** ADS, ALWS, AES (equivalenza), AAS; R04, R06, R07; G04, G06, G07.
- **Raccomandazione:** costruire una matrice prerequisito → sessione utilizzatrice per tutto Business (es. percentuali e denominatori → b01, b05, b14, b20, b21; statistica → b14, b15, b20, BL2-P23–P25; economia → b06, b07, b11, b12, capstone). Dimensionare il Complete sulla base del divario reale, non delle sole sessioni P esistenti. Documentare il calcolo delle 30 h o sostituirlo.
- **Test proposto:** simulazione AMVP dei profili B01 e B04 sul percorso Complete fino alle prove b07 e BL2-P25, confrontata con B02 su Professional.
- **Criterio di accettazione:** matrice prerequisiti completa al 100% per le competenze obbligatorie; calcolo delle ore di esonero riproducibile; nella simulazione, gap AAS tra B04-Complete e B02-Professional ≤ 10 punti (indicatore AES) oppure riprogettazione motivata.
- **Natura della verifica:** [D], [S]; [E] indispensabile prima di qualunque affermazione di equivalenza.

### E05-05 — Incoerenza di tracciabilità per ID tra matrici 2D e 2E (Business L2/L3)

- **Priorità:** P1
- **Riferimenti:** ROADMAP Fase 2D r. 519–554 e r. 613–648; Fase 2E L2 r. 1027–1074; Fase 2E L3 r. 1120–1179; ARTM r. 1258.
- **Evidenza testuale (esempi; 2D → 2E per lo stesso ID):**

| ID | 2D (tema, laboratorio, quiz) | 2E (evidenza prevista) |
|---|---|---|
| b14s1 | qualità dati: unicità, completezza, coerenza (r. 522) | «stakeholder e consenso simulato» (r. 1123) |
| b14s2 | 30+30 pratiche, mediana e tasso (r. 523) | «business case e resistenza» (r. 1124) |
| b15s3 | matrice confusione, accuratezza 16/20 (r. 527) | «richieste clienti eseguite in sandbox» (r. 1128) |
| b17s1 | RACI e proprietario processo (r. 531) | «roadmap trasformazione» (r. 1132) |
| b17s2 | guasto CRM e riconciliazione (r. 532) | «journey cliente e priorità» (r. 1133) |
| b19s1 | protocollo pilota e baseline predefinita (r. 537) | «ripasso su caso nuovo» (r. 1138) |
| b24s1 | attribuzione vs incrementalità (r. 552) | «ripasso su caso nuovo» (r. 1036) |
| b24s2 | disegno dell'esperimento (r. 553) | «prova interna distinta da certificazione» (r. 1037) |
| b38s1 | mapping e unità (r. 616) | «router e filtri confini» (r. 1147) |
| b39s1 | filtro AND e stato mancante (r. 619) | «mapping e tipi» (r. 1150) |
| b41s1 | idempotenza con vincolo univoco (r. 625) | «classificazione errori» (r. 1156) |

- **Inferenza:** almeno una delle due matrici non è allineata per ID al curriculum. Non posso stabilire quale senza i JSON (fuori ambito). Rilevante per E05: nella matrice 2E spariscono proprio le sessioni sul protocollo del pilota (b19s1) e sull'incrementalità/esperimento (b24s1–s2), che sono la base di E05-01.
- **Impatto:** l'ARTM (420 record per ID) compilata dalla matrice 2E perderebbe o duplicherebbe competenze; rischio di quiz, rubriche e badge mappati sulla sessione sbagliata.
- **Standard, requisiti e gate:** AVS (ARTM), AAS; R01, R03, R11; G01, G03, G11.
- **Raccomandazione:** prima di compilare l'ARTM, riconciliare 2D/2E per ciascuno dei 234 ID Business contro il curriculum JSON al commit applicativo `68e427bc…`, registrando per ogni ID la fonte autorevole.
- **Test proposto:** confronto automatico ID → tema/obiettivo dal JSON, rispetto alle due matrici documentali.
- **Criterio di accettazione:** 144/144 ID originali Business con tema coerente in ARTM; ogni divergenza risolta e motivata; 0 competenze presenti in 2D e assenti in ARTM senza decisione esplicita.
- **Natura della verifica:** [D] su JSON (fuori dal perimetro di CR-001).

### E05-06 — Fattibilità gratuita del L3 Business dipendente da tenant Microsoft

- **Priorità:** P1
- **Riferimenti:** ROADMAP r. 1116 (Developer Plan «Entra ID work/school», «ambienti developer unmanaged deprecati»; Copilot Studio «trial […] niente pubblicazione»), r. 1023 e r. 1111 (Power BI Desktop solo Windows), r. 1168–1179, r. 1208–1214, r. 1218; AMVP B06 «imprenditore Mobile First» (r. 1259).
- **Evidenza testuale:** «n8n non comprova Dataverse/Power Apps/Copilot specifici; trial non prova deploy; competenze specifiche obbligatorie senza alternativa accessibile sono gate» (r. 1218).
- **Ricalcolo:** le sessioni L3 con fonte P o X (Power Platform/PL-900) sono b45s1–b48s3 (12) più BL3-P29–P35 (7) = **19/97 (19,6%)** del L3, più la parte Power BI/DAX di L2 per chi non ha Windows.
- **Inferenza:** un privato senza account aziendale o scolastico Microsoft potrebbe non ottenere un ambiente gratuito stabile (da verificare [X]). In tal caso quasi un quinto del L3 non è conseguibile gratuitamente nella forma specifica, contro la regola permanente di parità (README r. 73, r. 89).
- **Impatto:** economico (paywall di fatto); organizzativo; equivalenza Professional/Complete × gratuito/premium (quattro combinazioni AES).
- **Standard, requisiti e gate:** AES, AAS; R05, R06, R08; G05, G06, G08.
- **Raccomandazione:** decisione esplicita prima di 4B: (a) rendere obbligatoria la competenza trasferibile (app di raccolta + flusso di approvazione + ruoli + test negativi) con implementazione a scelta dello strumento, spostando le competenze specifiche Power Platform nel percorso facoltativo/PL-900; oppure (b) dimostrare con collaudo un accesso gratuito stabile per un privato in Italia.
- **Test proposto:** collaudo con account personale nuovo, senza carta: Developer Plan, Dataverse, flusso di approvazione, export; ripetuto su macOS per Power BI.
- **Criterio di accettazione:** per ciascuna competenza obbligatoria L3 esiste almeno una via F0/F1/F2 con stato AES «lab verificato»; costo incrementale obbligatorio = 0 €.
- **Natura della verifica:** [T], [X].

### E05-07 — Affidabilità della diagnostica ADS per gli esoneri

- **Priorità:** P2
- **Riferimenti:** ROADMAP r. 1238 (D1 10 domande, D3 12, D4 12, D5 15; esonero con teoria ≥ 85%).
- **Evidenza testuale:** «esonero per competenza/attività con teoria >=85%, pratica quando richiesta >=75/100».
- **Ricalcolo (modello binomiale, prove indipendenti; semplificazione):**

| Area | Domande | Soglia | P(esonero) con padronanza reale 70% | con 75% | P(negazione) con padronanza 90% | con 95% |
|---|---:|---:|---:|---:|---:|---:|
| D5 economia | 15 | 13 | 12,7% | 23,6% | 18,4% | 3,6% |
| D3/D4 | 12 | 11 | 8,5% | 15,8% | 34,1% | 11,8% |
| D1 | 10 | 9 | 14,9% | 24,4% | 26,4% | 8,6% |

- **Inferenza:** con 10–15 domande, circa 1 candidato su 4 con padronanza al 75% viene esonerato in D5 e circa 1 su 3 con padronanza al 90% viene respinto in D3/D4. La pratica ≥ 75 mitiga solo dove «richiesta». ADS prevede già la validazione di falsi esoneri/negazioni (r. 1238): manca un obiettivo quantitativo.
- **Impatto:** Professional con lacune nascoste in economia → errori nei business case (E05-03).
- **Standard, requisiti e gate:** ADS, AVS; R04; G04.
- **Raccomandazione:** fissare tassi massimi accettabili di falsi esoneri e false negazioni; per D3–D5 prevedere sempre la prova pratica come condizione d'esonero, o un secondo tentativo con forma parallela per i casi di confine.
- **Test proposto:** simulazione di candidati con padronanza nota a livelli 60–95% su forme parallele.
- **Criterio di accettazione:** falsi esoneri ≤ 5% a padronanza 70%; false negazioni ≤ 10% a padronanza 90% (valori da approvare).
- **Natura della verifica:** [S] per la calibrazione iniziale; [E] indispensabile per la validità reale.

### E05-08 — Criteri go/no-go e di arresto non standardizzati

- **Priorità:** P2
- **Riferimenti:** ROADMAP r. 489 (b08s3), r. 501 (b12s3), r. 539, r. 542, r. 636 (b44s3), r. 1192, r. 1218; AAS r. 1234.
- **Evidenza testuale:** i criteri compaiono come contenuto di singole sessioni («soglie predefinite», «Test arresto»), non come requisito del capstone. La locuzione «criteri di arresto» non compare; «arresto» si riferisce quasi sempre a cicli di agenti.
- **Inferenza:** senza un modello comune lo studente può definire soglie dopo aver visto i risultati (spostamento dei criteri a posteriori), proprio il rischio che b19s2 insegna a evitare.
- **Impatto:** validità delle decisioni e confrontabilità dei capstone.
- **Standard, requisiti e gate:** AAS (requisiti essenziali), AVS; R03; G03.
- **Raccomandazione:** modello obbligatorio di decisione per capstone L3 e 4B, registrato prima dell'esecuzione: metrica primaria; metriche di salvaguardia (qualità, errori critici, costo, latenza, carico di revisione); soglie con incertezza (E05-02); esiti possibili «estendi / itera / ferma / riprogetta»; criteri di arresto anticipato e di rollback; proprietario della decisione; data e versione.
- **Test proposto:** capstone simulati in cui i dati favoriscono un «go» solo cambiando soglia a posteriori.
- **Criterio di accettazione:** 100% dei capstone con modello datato prima dei risultati; modifica a posteriori senza motivazione = errore critico AAS.
- **Natura della verifica:** [D], [S].

### E05-09 — Progressione L1→L3 e coerenza tra profilo, nome del livello e capstone

- **Priorità:** P2
- **Riferimenti:** ROADMAP r. 195 (profilo «junior AI-enabled business/data analyst e referente operativo di piloti AI»); README r. 28 (L3 «AI Strategy & Business Transformation»); AAS r. 1234 (capstone L3 «AI Business Transformation Strategy»); L1 2E r. 1018 (capstone candidato con ROI/TCO a tre scenari e go/no-go); 2D r. 613–648 (contenuti L3 settimane 37–48).
- **Evidenza testuale:** il capstone candidato L1 include già «pilota AI su richieste sintetiche, 20 casi baseline, […] ROI/TCO a tre scenari, registro rischi, piano adozione, decisione go/no-go» (r. 1018). Il capstone L3 ripete la stessa struttura in sandbox con automazione. I contenuti originali delle settimane 37–48 sono prevalentemente operativi (trigger, mapping, retry, idempotenza, Power Platform).
- **Inferenza:** (a) l'incremento di competenza economico-decisionale da L1 a L3 non è definito: lo stesso schema ROI/TCO/go-no-go viene ripetuto con strumenti diversi; (b) la denominazione «Strategy & Business Transformation» e il badge «AI Strategy» promettono più del profilo junior dichiarato e dei contenuti. Contenuti strategici veri (portafoglio, roadmap di trasformazione, modello operativo, ridisegno dei ruoli) sono marginali (b11s1, b17s1 solo nella matrice 2E, b48 piano 90 giorni).
- **Impatto:** professionale (aspettative non sostenute dal percorso); credenziali.
- **Standard, requisiti e gate:** AELS (progressione L1 comprendere / L3 progettare-valutare), ACS; R01, R09; G01, G09.
- **Raccomandazione:** matrice di progressione per ciascuna competenza Business (L1 calcola su caso dato; L2 misura su dati con incertezza; L3 progetta il pilota con identificazione causale, portafoglio e modello operativo). Differenziare il capstone L1 (piano di miglioramento senza pilota eseguito) dal L3. Valutare una denominazione più aderente al profilo (decisione dell'utente) o rafforzare i contenuti strategici.
- **Test proposto:** revisione della matrice di progressione per verificare che ogni competenza abbia almeno un incremento osservabile per livello.
- **Criterio di accettazione:** 100% delle competenze Business con descrittori distinti per livello; nessun capstone con requisiti sostanzialmente identici a un livello precedente.
- **Natura della verifica:** [D]; [X] revisione di un professionista umano consigliata.

### E05-10 — Metodi di analisi dei processi assenti

- **Priorità:** P2
- **Riferimenti:** ROADMAP r. 472–477, r. 519–521, r. 1008 (BL1-P10 «processo as-is/to-be»), r. 1250 (badge «Process Analysis»).
- **Evidenza testuale:** i processi sono trattati come mappe, eccezioni, responsabilità e soglie. Non compaiono notazioni o metriche di flusso: BPMN, lead time/tempo ciclo, throughput, colli di bottiglia, legge di Little, analisi del flusso del valore, classificazione dell'automatizzabilità per attività, rilevazione dei tempi o process mining.
- **Inferenza:** senza metriche di flusso lo studente non può dimostrare che il risparmio locale si traduce in miglioramento del processo. Il curriculum mostra intuitivamente il problema (b15s2), ma non fornisce strumenti per analizzarlo.
- **Controesempio:** riduzione del tempo di lavorazione di una fase non collo di bottiglia del 40% → throughput invariato, code invariate, beneficio economico nullo.
- **Impatto:** professionale (badge Process Analysis); economico (benefici sovrastimati).
- **Standard, requisiti e gate:** AELS, ACS; R01; G01.
- **Raccomandazione:** aggiungere in L1/L3 un nucleo di analisi dei processi: una notazione standard, metriche di flusso, identificazione del collo di bottiglia, matrice di automatizzabilità (volume, variabilità, rischio, regole vs giudizio), protocollo etico di rilevazione dei tempi.
- **Test proposto:** caso in cui l'ottimizzazione proposta riguarda una fase non vincolante.
- **Criterio di accettazione:** lo studente identifica il collo di bottiglia e stima l'effetto sul throughput nel ≥ 80% dei casi.
- **Natura della verifica:** [D], [S].

### E05-11 — Governance: quadro normativo UE e tutela dei lavoratori non trattati

- **Priorità:** P2
- **Riferimenti:** ROADMAP r. 487–492, r. 959 (NIST AI RMF, EDPB), r. 466 (b01s1 «Cronometrare 20 richieste»), r. 494 (b10s2 KPI adozione), r. 1250 (badge AI Governance, Responsible AI Adoption).
- **Evidenza testuale:** nessuna occorrenza di normativa UE sull'intelligenza artificiale, GDPR, valutazione d'impatto sulla protezione dei dati, standard di sistema di gestione dell'AI, né di norme sul controllo dell'attività dei lavoratori. Il profilo esclude l'equivalenza a «responsabile compliance» (r. 195).
- **Inferenza (da verificare con fonte giuridica [X]):** governance AI in un contesto UE/italiano senza il quadro normativo applicabile è incompleta per un badge di governance. I piloti che misurano tempi e adozione dei dipendenti, se trasferiti dallo studente al proprio luogo di lavoro, possono toccare la protezione dei dati e le regole sul controllo a distanza dei lavoratori: tema da coprire almeno come segnale di escalation.
- **Impatto:** professionale e di rischio reputazionale/legale per lo studente che applica il metodo al lavoro; credenziali.
- **Standard, requisiti e gate:** AVS (R10); ACS; R10, R09; G10.
- **Raccomandazione:** unità di inquadramento normativo (classificazione del rischio, obblighi di trasparenza e supervisione, base giuridica e minimizzazione, quando coinvolgere DPO, giuristi e rappresentanze dei lavoratori), redatta o rivista da una persona qualificata e datata; vincolo per i piloti: dati sintetici o aggregati, nessuna misurazione individuale dei lavoratori senza base giuridica.
- **Test proposto:** scenario di pilota in azienda con misura dei tempi individuali; lo studente deve riconoscere il rischio e indicare l'escalation.
- **Criterio di accettazione:** unità con fonti ufficiali datate e revisione umana qualificata; nello scenario, mancata escalation = errore critico AAS (sicurezza/privacy).
- **Natura della verifica:** [X] obbligatoria; [D].

### E05-12 — Change management, adozione e supervisione umana poco misurabili

- **Priorità:** P2
- **Riferimenti:** ROADMAP r. 493–495 (b10), r. 534–536 (b18), r. 1015 (BL1-P17), r. 1188 (BL3-P09), r. 1250 (badge Change Management).
- **Evidenza testuale:** adozione misurata come tasso di utilizzo (b10s2: 10/40 = 25%) e prova di compito; RACI; formazione e retest.
- **Inferenza:** mancano metriche della supervisione umana efficace: tasso di override, qualità della revisione (rilevazione di errori piantati), compiacenza verso l'automazione, carico di revisione nel tempo, effetti sui ruoli. Un «human in the loop» che approva il 100% senza rilevare errori piantati non è supervisione.
- **Impatto:** governance e rischio operativo; validità del badge.
- **Standard, requisiti e gate:** AELS, AAS, ACS; R02, R10; G01, G10.
- **Raccomandazione:** nel capstone L3 e in 4B introdurre errori piantati noti e misurare la rilevazione da parte dei revisori; aggiungere un piano di adozione con baseline, metriche anticipatrici e ritardate, e analisi dell'impatto sui ruoli.
- **Test proposto:** flusso con 10% di output errati piantati; misura del tasso di rilevazione.
- **Criterio di accettazione:** il capstone riporta tasso di rilevazione e override con incertezza; soglia minima di rilevazione definita prima dell'esecuzione.
- **Natura della verifica:** [D], [S]; [T] nel collaudo 4B.

### E05-13 — Laboratori ROI: dati sintetici senza effetto vero noto; etichettatura delle evidenze nel portfolio

- **Priorità:** P2
- **Riferimenti:** README r. 30 («soluzioni 120/1»); ROADMAP r. 241, r. 503 («Soluzione generica identica»), r. 1018, r. 1218, r. 1318; ACS r. 1250 (portfolio «risultati»).
- **Evidenza testuale:** Business ha oggi una soluzione unica per 144 sessioni e 48 esempi distinti; tutti i laboratori futuri sono P/B, con T = 0. Capstone e 4B su dati sintetici e sandbox.
- **Inferenza:** i laboratori sintetici sono legittimi per la didattica, ma (a) sono valutabili oggettivamente solo se il dataset contiene un effetto vero piantato con confondenti noti; (b) i numeri ottenuti non sono evidenza empirica di valore e non devono apparire nel portfolio come «risultati» senza etichetta. I tempi «baseline» misurati dallo studente su sé stesso non rappresentano un processo aziendale.
- **Impatto:** riproducibilità e correggibilità (G02); integrità delle credenziali (G09).
- **Standard, requisiti e gate:** AELS (materiali sintetici), AAS, ACS; R02, R09; G02, G09.
- **Raccomandazione:** generatore di dataset versionato con seme, effetto vero, trend e confondenti documentati nella chiave dell'esaminatore; etichetta obbligatoria nel portfolio: «Dati sintetici — risultati dimostrativi, non evidenza di valore».
- **Test proposto:** tre esecuzioni con semi diversi; confronto delle stime con l'effetto vero.
- **Criterio di accettazione:** riproducibilità bit a bit dei dataset dal seme; 100% degli elaborati di portfolio Business con etichetta di provenienza dei dati.
- **Natura della verifica:** [D], [T].

### E05-14 — Concept 4B: risparmio orario non monetizzato e TCO assente

- **Priorità:** P2
- **Riferimenti:** ROADMAP r. 1306, r. 1318; r. 468 (b01s3: manutenzione 100 min > risparmio 90 min).
- **Evidenza testuale:** «baseline 100 h, AI + review 70 h, risparmio 30 h; ROI scenarios Low/Base/High».
- **Inferenza:** il concept, pur dichiarato illustrativo, rappresenta il beneficio solo in ore. Il curriculum stesso (b01s3) mostra che la manutenzione può annullare il risparmio.
- **Ricalcolo illustrativo (ipotesi mie, non dei documenti):** 30 h × 30 €/h = 900 €/periodo; costo di avvio 40 h (1.200 €); manutenzione 5 h e rilavorazione errori 4 h per periodo (270 €). Beneficio netto 630 €/periodo, payback ≈ 1,9 periodi. Con adozione al 60%: risparmio 540 €, netto 270 €, payback ≈ 4,4 periodi. Con adozione al 30%: netto 0 €, payback infinito. La decisione dipende interamente da variabili che il concept non mostra.
- **Impatto:** il prototipo che deve «dimostrare la qualità del modello» (r. 1303) rischia di modellare l'errore che il corso insegna a evitare.
- **Standard, requisiti e gate:** AAS, AES; R02, R03; G02, G03.
- **Raccomandazione:** il brief 4B deve includere conversione ore→valore con ipotesi esplicite, TCO completo (avvio, manutenzione, revisione, rilavorazione, formazione, quote, uscita), adozione e curva di apprendimento, sensibilità per variabile e soglia di pareggio, distinzione capacità/cassa (E05-03).
- **Test proposto:** analisi di sensibilità a un fattore per volta sul modello 4B.
- **Criterio di accettazione:** il prototipo 4B mostra per ogni scenario la soglia di adozione di pareggio e almeno una variabile che inverte la decisione.
- **Natura della verifica:** [D]; [T] nel collaudo 4D.

### E05-15 — Registro R01–R12: tracciabilità R↔G implicita e provenienza parziale

- **Priorità:** P2 (mandato comune)
- **Riferimenti:** README r. 183; ROADMAP r. 1263, r. 1267, r. 1271–1299, r. 1322.
- **Evidenza testuale:** R01–R12 sono «una proposta organizzativa della Fase 3I» (r. 1290); README r. 183 afferma «registro R01–R12 recuperato 12/12»; la nota di provenienza dichiara che non si attesta la trascrizione integrale delle parti coperte e che IMG_9497 originale non è verificato (r. 1322). r. 1263 dichiara mancanti IMG_9493–9499 (sette immagini); r. 1322 parla di sei immagini ricevute successivamente, «una compensativa».
- **Osservazioni:**
  1. La corrispondenza R_n ↔ G_n non è dichiarata. È plausibile per R01–R11, ma **R12 «Validazione e revisione critica»** non coincide con **G12 «Efficacia formativa»**: una revisione critica (come questa) non è efficacia formativa. Rischio che una revisione AI completata venga letta come progresso su G12.
  2. R10 «Sicurezza e privacy» è attribuito ad AVS, che però definisce il gate (G10) e non contenuti normativi o tecnici di sicurezza/privacy (vedi E05-11).
  3. Non esiste un requisito per la **validità delle misure di valore** (baseline, incrementalità, inferenza). Per il percorso Business ricade in modo generico in R02/R03.
  4. «Recuperato 12/12» (README) è un'affermazione più forte della nota di provenienza: i 12 titoli sono leggibili, la completezza del testo originale non è attestata.
- **Impatto:** tracciabilità ARTM e rischio di chiusure improprie di G12.
- **Standard, requisiti e gate:** AVS, AMVP; R12; G12.
- **Raccomandazione:** tabella esplicita R↔standard↔G con cardinalità; separare R12 in «revisione critica» (processo) e collegamento a G12-S/G12-E (esito); riformulare README r. 183 come «12/12 titoli recuperati; testo integrale non attestato».
- **Test proposto:** controllo di copertura: ogni R ha almeno un G e un criterio di chiusura; ogni G ha almeno un R.
- **Criterio di accettazione:** matrice R↔G completa al 100%; nessun evento di revisione AI registrato come avanzamento di G12.
- **Natura della verifica:** [D].

### E05-16 — Riepiloghi correnti non aggiornati (violazione della procedura permanente)

- **Priorità:** P2 (mandato comune)
- **Riferimenti:** ROADMAP r. 3 («Aggiornato: 25 novembre 2026»), r. 26, r. 55–60 («Prossimo intervento: Fase 2C, completare audit individuale Creator 1–6»), r. 67 (procedura permanente); README r. 3 («Stato operativo corrente — 25 novembre 2026»).
- **Evidenza testuale:** la procedura impone di «aggiornare i riepiloghi correnti quando cambiano […] prossimo passo» (r. 67). Il prossimo passo effettivo al checkpoint è CR-001 e il recupero delle lacune (r. 1269), non la Fase 2C.
- **Inferenza:** una nuova conversazione che legga dall'alto (come prescrive la Regola 1) potrebbe riprendere da un passo superato.
- **Impatto:** organizzativo, continuità.
- **Standard, requisiti e gate:** procedura permanente, Regola 1; R11; G11.
- **Raccomandazione:** aggiornare data e «Prossimo intervento» nelle sezioni correnti di entrambi i documenti, conservando lo storico.
- **Test proposto:** lettura dell'intestazione di entrambi i documenti da parte di un agente senza contesto.
- **Criterio di accettazione:** fase e prossimo passo indicati nelle prime 30 righe di entrambi i documenti coincidono con l'ultima sezione approvata.
- **Natura della verifica:** [D].

### E05-17 — Soglie AAS/ACS: interazione non esplicitata

- **Priorità:** P3
- **Riferimenti:** ROADMAP r. 1234, r. 1250.
- **Evidenza e ricalcolo:** profilo minimo ammesso dai criteri (3 su correttezza e verifica, 2 sugli altri): P = 62,5 < 75. Tutti i criteri a 3 («competente»): P = 75, esattamente la soglia pratica. Componenti di livello esattamente alle soglie (teoria 80, pratica 75, capstone 80): totale 0,2×80 + 0,4×75 + 0,4×80 = **78 < 80**. Quindi la soglia vincolante del Level Credential non è quella delle singole componenti.
- **Inferenza:** nessuna contraddizione logica, ma rischio di comunicazione fuorviante agli studenti e di errori di implementazione.
- **Standard e gate:** AAS, ACS; R03, R09; G03, G09.
- **Raccomandazione:** pubblicare esempi svolti delle combinazioni minime effettive.
- **Test proposto:** calcolo automatico su griglia di combinazioni.
- **Criterio di accettazione:** documentazione studente coerente con il calcolo al 100%.
- **Natura della verifica:** [D]; [T] dopo l'implementazione.

### E05-18 — Classificazione M apparentemente guidata dall'aritmetica dei quiz

- **Priorità:** P3
- **Riferimenti:** ROADMAP r. 515, r. 562, r. 609 e tabelle 2D.
- **Evidenza:** sessioni classificate M i cui temi non sono propedeutici: b19s2 «Confronto strumenti per quote» (quiz 20/200 = 10%), b43s3 «copertura escalation» (9/12 = 75%), b42s3 (21/25), b38s2 (conversione centesimi).
- **Inferenza:** la componente «esonerabile» sembra coincidere con un calcolo elementare nel quiz più che con teoria propedeutica nella lezione. Effetto sul ramo Professional trascurabile ma classificazione poco informativa (rafforza E05-04).
- **Raccomandazione:** riclassificare sul contenuto teorico della sessione (curriculum JSON), non sul quiz.
- **Criterio di accettazione:** ogni M ha la componente propedeutica identificata per obiettivo e durata.
- **Natura della verifica:** [D] su JSON.

**Nota per E01/E04 (fuori dal mandato principale, segnalata senza classificazione):** in tutte le 264 sessioni la risposta corretta di quiz base e avanzato occupa la stessa posizione (r. 457, r. 652), il che rende prevedibile l'avanzato; b07s1 e b31s3 hanno quiz base e avanzato praticamente identici (r. 484, r. 586, r. 603).

## 11. Raccomandazioni e verifiche mancanti

### 11.1 Raccomandazioni prioritarie (da sottoporre al coordinatore e all'utente)

1. **Prima del brief 4B** (senza avviare la Fase 4): risolvere a livello documentale E05-01, E05-03, E05-08 ed E05-14, perché il prototipo 4B è il dimostratore proprio di queste competenze.
2. **Prima della compilazione ARTM:** riconciliazione per ID 2D/2E (E05-05) contro i curriculum JSON.
3. **Decisione dell'utente** su Power Platform obbligatorio o trasferibile (E05-06).
4. **Dimensionamento del ramo Complete** con matrice prerequisito→sessione (E05-04) e obiettivi quantitativi di falsi esoneri (E05-07).
5. **Moduli nuovi da redigere:** economia aziendale con attualizzazione; inferenza statistica applicata alle decisioni; analisi dei processi; inquadramento normativo con revisione umana qualificata.
6. **Aggiornamenti documentali minori:** E05-15, E05-16, E05-17.

### 11.2 Verifiche mancanti (non eseguibili in CR-001)

| Verifica | Natura | Gate |
|---|---|---|
| Allineamento ID → contenuto su curriculum JSON | [D] su fonte fuori perimetro | G01, G11 |
| Accesso gratuito reale a Power Platform, Power BI su sistemi non Windows, Make, n8n, Ollama | [T] | G05, G06, G08 |
| Esecuzione dei laboratori e del pilota 4B in sandbox | [T] | G02 |
| Simulazioni AMVP di B01–B06 su Complete e Professional | [S] | G12-S, G04, G06 |
| Calibrazione AAS su elaborati campione e accordo tra valutatori | [S], poi [E] | G03 |
| Affidabilità della diagnostica | [S], poi [E] | G04 |
| Inquadramento normativo e tutela dei lavoratori | [X] | G10 |
| Revisione da parte di un professionista umano di business transformation/finanza aziendale | [X] | G01, G12 |
| Efficacia formativa su studenti reali | [E] | G12-E |
| Benchmark con fonti ufficiali datate | [X] | G01 |

### 11.3 Affermazioni di qualità sostenibili in assenza di G12-E (senza deroga ad AVS)

**Sostenibili oggi, con formulazione esatta:**
- «Architettura didattica progettata secondo standard interni approvati (AELS, AAS, ADS, AES, ALWS, ACS, AVS/AMVP).»
- «Revisione documentale interna e revisione critica simulata da AI esterna effettuate» (solo dopo la loro effettiva esecuzione), con l'avvertenza che non sono audit umani indipendenti.
- «Conteggi strutturali verificati staticamente» (264 ID, 528 quiz, 1584 feedback, 420/528 con feedback distinti come indicatore strutturale).
- Dopo collaudo [T]: «laboratorio X eseguito e riproducibile nell'ambiente Y alla data Z».
- Dopo simulazione [S]: «prestazioni di studenti simulati AMVP», sempre con l'etichetta di simulazione e senza estrapolazione a persone.

**Non sostenibili senza G12-E:** «efficace», «porta a competenza professionale», «prepara al ruolo di…», «equivalente tra Professional e Complete» (come esito), «equivalente tra percorso gratuito e premium» (come esito di apprendimento), «di livello universitario o internazionale», qualunque percentuale di superamento, ritenzione o occupabilità, qualunque confronto di superiorità con offerte esterne. Le credenziali ACS restano attestazioni interne di prove superate, non prova di efficacia del programma.

**Distinzione richiesta dal mandato:**
- *Revisione documentale* (questa): dice se l'architettura è coerente e completa sulla carta.
- *Simulazione AI* (G12-S): dice se il materiale è percorribile da agenti con profili dichiarati; non misura apprendimento umano.
- *Collaudo tecnico reale* (G02, G05, G06, G08): dice se laboratori e strumenti funzionano davvero e gratis.
- *Efficacia empirica* (G12-E): l'unica che può sostenere affermazioni sull'apprendimento delle persone.

### 11.4 Distinzione G12-S / G12-E

La distinzione è corretta e ben formulata (r. 1294–1299). Due integrazioni raccomandate:
- Per il percorso Business la simulazione ha un limite specifico: i profili B02 («professionista aziendale») e B05 («analista junior») sono impersonati da un modello che possiede già conoscenze economiche e statistiche estese; la contaminazione è massima proprio sulle competenze di E05-02 ed E05-03. I risultati G12-S su questi profili andrebbero considerati come limite superiore.
- Definire in anticipo cosa farebbe progredire G12-S (es. criteri di superamento della simulazione) senza che ciò comporti avanzamenti su G12-E.

## 12. Esito complessivo

**Esito: PARZIALE.**

**Motivazione:**
- **Conforme** sul piano della governance documentale: limiti dichiarati, nessun gate chiuso impropriamente, distinzioni tra livelli di evidenza rispettate, aritmetica corretta, standard coerenti tra loro e duplicati README/ROADMAP identici.
- **Non conforme o incompleto** sul piano specialistico E05, con sei anomalie P1 che riguardano proprio le competenze del profilo dichiarato e del prototipo 4B: identificazione causale e uso di «holdout» (E05-01); inferenza statistica nelle decisioni (E05-02); fondamenti economici, attualizzazione e contenuti inesistenti (E05-03); dimensionamento del ramo Complete (E05-04); tracciabilità per ID 2D/2E (E05-05); fattibilità gratuita del L3 (E05-06).
- **Non verificabile** in questa sede: efficacia formativa (G12-E), funzionamento dei laboratori, parità gratuita reale, allineamento al curriculum JSON.

Le P1 non sono blocchi immediati (P0), perché nessuna modifica applicativa o rilascio è in corso. Secondo AVS bloccano però l'accettazione pertinente: in particolare l'accettazione del prototipo 4B e delle credenziali Business L3 (Capstone, ROI & TCO Analysis, AI Strategy) finché non saranno risolte.

Questo rapporto non chiude gate, non modifica standard o file, non autorizza la Fase 4 né rilasci. Le raccomandazioni sono sottoposte al coordinatore e all'utente.

— Fine del rapporto CR-001 — E05 —
