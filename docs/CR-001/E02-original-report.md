# CR-001 — E02 — Software Engineering Review Report

## 1. Modello AI, versione e data
- **Modello:** Claude Opus 5.5 (Anthropic), identificativo `claude-opus-5-5`.
- **Data della revisione:** 26/11/2026, ore 14:41 circa (Europe/Rome).
- **Modalità:** sessione con strumenti di lettura file e shell in un ambiente Linux isolato. Nessun accesso al web generico è stato usato per questa revisione.

## 2. Ruolo specialistico
Prospettiva E02 Software Engineering secondo AMVP. Sono un revisore AI esterno simulato, non un esperto umano, e questo rapporto non è un audit umano indipendente.

## 3. Capacità e limiti
**Cosa ho fatto realmente:**
- Ho scaricato dal repository pubblico il solo commit del checkpoint.
- Ho verificato blob SHA, lunghezze e numero di righe.
- Ho letto integralmente i due documenti: README in un'unica lettura (righe 1–183) e ROADMAP in nove segmenti consecutivi (righe 1–1322), senza lacune.

**Cosa non ho fatto:**
- Non ho aperto `index.html`, `sw.js`, `curriculum-creator.json`, `curriculum-business.json` né altri file, anche se erano presenti nel commit scaricato. Il mandato limita l'esame a README e ROADMAP.
- Non ho eseguito codice, test runtime, browser, Safari o iPhone.
- Non ho aperto i link esterni citati.
- Non ho verificato le teste attuali di main, RC1 o del branch di sviluppo.

**Conseguenza:** ogni affermazione sul comportamento dell'app è classificata come non verificabile documentalmente oppure come inferenza o ipotesi.

## 4. Bias e potenziali conflitti
- **Conflitto strutturale:** AMVP designa Claude come revisore esterno e lo inserisce nei ruoli di simulazione (Teacher, Student, Examiner, Auditor). Una valutazione favorevole di AMVP da parte mia avrebbe un interesse implicito. Per questo ho trattato AMVP con particolare scetticismo.
- **Bias da modello linguistico:** i documenti sono stati redatti da un'altra AI (ChatGPT). Esiste il rischio di cecità comuni tra modelli, cioè di accettare come coerente una prosa formalmente rigorosa. La concordanza tra AI non costituisce prova (lo dice la stessa ROADMAP alla riga 1259).
- **Conoscenze generali:** le mie conoscenze su PWA, Safari e iOS, ad esempio sulle politiche di eliminazione dei dati locali, sono generali e possono non essere aggiornate. Le uso solo come ipotesi da collaudare.

## 5. Indipendenza procedurale
- Non ho consultato rapporti di altri revisori CR-001, analisi del coordinatore o documenti successivi al checkpoint.
- Non ho usato conclusioni di altre conversazioni.
- Non ho modificato file, chiuso gate o avviato la Fase 4.

## 6. Ambito, materiali e checkpoint
- **Repository:** itopo-ai/AI-Creator-Academy.
- **Commit:** `f9d98c2bbd4d3622b9ccb5eeeb5c1811a2c4d401` (26/11/2026 12:52 +01:00, «docs: align phase 3I status with recovered evidence»).
- **Materiali esaminati:** solo README.md e ROADMAP.md a quel commit.
- **Natura:** CR-001 è una revisione documentale, non una certificazione di prototipi o del runtime.

## 7. Esito della verifica preliminare

| Verifica | Atteso | Effettivo | Esito |
|---|---|---|---|
| Commit raggiungibile e oggetto di tipo commit | f9d98c2… | f9d98c2… | ✅ |
| Blob README (`git ls-tree` e `git hash-object` sul file letto) | abca6f1c… | abca6f1c… | ✅ |
| Blob ROADMAP (`git ls-tree` e `git hash-object` sul file letto) | af9888bc… | af9888bc… | ✅ |
| Caratteri Unicode README | ≈54.465 | 54.465 (54.854 byte, 183 righe) | ✅ |
| Caratteri Unicode ROADMAP | ≈287.684 | 287.684 (290.224 byte, 1322 righe) | ✅ |
| Contenuto non troncato e non anteprima | file completo | letto dal blob git, righe consecutive senza salti | ✅ |
| Capacità di esame integrale | — | lettura completa in segmenti contigui, numerati per riga | ✅ |

**Non effettuabile o non effettuato:**
- stato attuale dei branch;
- integrità delle immagini sorgente (IMG_9493–9499);
- contenuto dei file applicativi.

**Esito:** accesso integrale confermato. Ho proceduto con la revisione.

## 8. Metodo di revisione
1. Ho estratto da entrambi i documenti ogni affermazione con implicazioni software: ID, indici, progressi, schema, backup, migrazione, PWA, cache, offline, branch, test e versioni.
2. Ho classificato ogni affermazione come:
   - evidenza testuale (riportata nei documenti);
   - dichiarata ma non verificata (controllo storico non riproducibile da me);
   - inferenza (deduzione logica da più passaggi);
   - ipotesi (rischio tecnico generale da collaudare).
3. Ho cercato attivamente contraddizioni tra standard approvati (AELS, AAS, ADS, AES, ALWS, ACS, AVS, AMVP), vincoli di preservazione e piano di Fase 4.
4. Ho costruito controesempi e test negativi.
5. Ho verificato la tracciabilità R01–R12 → G01–G12 → registro test → ARTM.

I riferimenti usano la forma «ROADMAP Lnnn» o «README Lnnn», dove nnn è il numero di riga al checkpoint.

## 9. Punti di forza
- **Disciplina sulle evidenze.** Le categorie dichiarato, documentato, verificato e non verificato sono costanti, e i documenti affermano ripetutamente che i controlli statici non equivalgono a collaudi runtime (ROADMAP L44, L67).
- **Vincoli di preservazione espliciti e stabili.** ID, indici, progressi, migrazione, main 6.5.1 e RC1 sono ripetuti in ogni fase. Gli SHA di main e RC1 sono registrati a ogni checkpoint.
- **Tracciabilità delle modifiche al curriculum storico.** Per ogni blocco sono registrati commit, file, conteggi, confronto integrale del JSON e rilettura (ROADMAP L76–L178).
- **Stati AVS ben distinti.** I livelli V0–V6 separano verifica documentale (V2), collaudo operativo (V3), equivalenza (V4) e validazione didattica (V5). I criteri di chiusura dei gate sono rigorosi: requisito predefinito, prova realmente eseguita, atteso ed effettivo, evidenza riproducibile, nessuna compensazione (L1258).
- **Onestà sul recupero documentale.** Le lacune delle immagini e l'assenza dell'originale IMG_9497 sono dichiarate (L1263, L1322).
- **Contenuti didattici di ingegneria del software tecnicamente corretti a livello di quiz.** Riguardano idempotenza, RLS, validazione lato server, segreti, backup con ripristino isolato e migrazione con rollback (L379–L455). Paradossalmente, sono proprio le pratiche che mancano nella specifica dell'app stessa (vedi E02-01 ed E02-12).

## 10. Osservazioni e anomalie

**Nessuna anomalia P0 accertata documentalmente.** Nessuna modifica applicativa è autorizzata, quindi non c'è un rischio immediato sui dati di produzione derivante da CR-001.

---

### E02-01 — P1 — Architettura software dell'app non documentata
- **Sezione:** README L5–L15, L48–L61; ROADMAP L15–L20, L43–L53, L1258.
- **Evidenza (testuale):**
  - I documenti nominano solo `index.html`, `sw.js`, due JSON di curriculum, «profilo cifrato», «backup cifrato», «sistema di migrazione» e «allineamento versione/cache».
  - Non descrivono modello dati, tecnologia di storage, versione dello schema, strategia del service worker, algoritmo crittografico, formato del backup, host di distribuzione o branch servito agli utenti.
  - AVS conferma: «nessuno schema approvato» (L1258).
- **Impatto:** non è possibile valutare documentalmente la fattibilità dell'evoluzione a 420 sessioni, rami, diagnostica, credenziali e portfolio. G10 e G11 non hanno una base di riferimento. I prototipi della Fase 4 rischiano di nascere senza vincoli tecnici espliciti.
- **Raccomandazione:** prima o all'inizio della Fase 4, redigere in un file separato un documento «architettura as-is» ricavato dal codice. Deve coprire componenti, storage e chiavi, schema dati versionato, ciclo di vita del service worker, cifratura, formato del backup, percorso di migrazione e topologia di distribuzione. Le decisioni future vanno registrate come ADR.
- **Test proposto:** revisione incrociata tra il documento as-is e il codice al commit applicativo `68e427bc…`, con elenco delle discrepanze.
- **Criterio di accettazione:** ogni chiave di storage, ogni campo persistito e ogni messaggio del service worker presenti nel codice sono documentati, con zero discrepanze non motivate.
- **Verificabilità:** richiede accesso al codice.

### E02-02 — P1 — «Nessuna modifica dello schema» contraddice requisiti approvati che richiedono nuove entità persistite
- **Sezione:** AAS (L1234), ADS (L1238), ACS (L1250), AVS (L1258).
- **Evidenza (testuale):** gli standard approvati richiedono di persistere:
  - stati «non iniziata / in apprendimento / completamento storico / competenza verificata»;
  - storico dei tentativi e miglior risultato valido;
  - ramo Professional o Complete, esoneri, cambio di ramo senza perdita, versione del test diagnostico;
  - credenziali con ID distinto, stato (rilasciata, sostituita, corretta, revocata) e versione dello standard;
  - portfolio e registro AI.

  Ogni standard ripete però «nessuna modifica schema autorizzata». Si tratta di un'inferenza diretta: questi requisiti non sono implementabili senza estendere lo schema.
- **Impatto:** la Fase 5 non può rispettare insieme gli standard e il vincolo. Esiste il rischio di soluzioni improvvisate, come campi aggiunti senza versione o dati in chiavi parallele, che compromettono migrazione e backup.
- **Raccomandazione:** riformulare il vincolo come «nessuna modifica distruttiva o non versionata dello schema senza approvazione». In Fase 4 proporre lo schema v-next con un approccio solo additivo, campo `schemaVersion`, migrazioni monotone e idempotenti, e conservazione dei dati legacy in sola lettura.
- **Test proposto:** sui profili sintetici 6.5.1 e RC1, eseguire la migrazione v-old → v-next due volte e verificare che lo stato risultante sia identico (idempotenza). I dati legacy devono restare byte per byte recuperabili.
- **Criterio di accettazione:** decisione formale dell'utente sullo schema v-next prima della Fase 5. Migrazione idempotente, zero perdita di campi legacy, nessuna competenza attribuita retroattivamente (C03).
- **Verificabilità:** la contraddizione è verificabile documentalmente; la soluzione richiede codice e runtime.

### E02-03 — P1 — Manca una politica di assegnazione e significato degli ID per le 156 sessioni nuove
- **Sezione:** ROADMAP L248–L318 (formato `cr-wNNsN` e `bNNsN`), L738–L749, L806–L825, L911–L944, L999–L1016, L1075–L1109, L1180–L1216 (segnaposti P01, L2-P01, L3-P01, BL1-P01, BL2-P01, BL3-P01), L652 (Business L3 = settimane 13–20 + 37–48), ALWS L1246 (calendario di 36 settimane per livello, «blocchi riprendibili senza nuovi ID automatici»).
- **Evidenza:**
  - *Testuale:* gli ID esistenti codificano settimana e posizione; i segnaposti usano quattro convenzioni diverse e sono dichiarati «non ID applicativi».
  - *Inferenza:* con la riorganizzazione in livelli (ad esempio `b13s1` collocata nel livello 3 dopo le settimane 21–36) e con calendari di 36 settimane per livello, il significato posizionale degli ID («w13» = settimana 13) diventa falso. Non è definito se i nuovi ID seguiranno lo stesso schema, che rischia collisioni o ambiguità (ad esempio `cr-w25s1` per una sessione L1), oppure uno schema opaco.
- **Impatto:** collisioni o riuso di ID, ordinamento errato, dati di progresso associati alla sessione sbagliata, regressione su indici e progressi.
- **Raccomandazione:** separare l'**identità** della sessione (immutabile, mai riutilizzata, mai derivata dalla posizione) dalla **posizione** (livello, settimana e ordine in una tabella di mappatura versionata). Definire il formato dei nuovi ID, un registro degli ID emessi e di quelli deprecati, e una regola di non riuso.
- **Test proposto:**
  - test automatico di unicità globale degli ID nell'unione dei vecchi e nuovi curriculum;
  - test negativo: inserire una sessione con ID già esistente o deprecato e verificare che la validazione fallisca;
  - test di riordino: spostare tre sessioni tra livelli e verificare che il progresso salvato resti associato all'ID e non alla posizione.
- **Criterio di accettazione:** 264 ID originali invariati, 0 collisioni, 0 riusi, progresso invariato dopo il riordino.
- **Verificabilità:** la politica è documentale; l'esecuzione richiede codice.

### E02-04 — P1 — La formula di avanzamento regredisce i progressi quando cambiano le attività
- **Sezione:** README L53 («Percentuale lezione = attività spuntate / attività previste… Usa i progressi già salvati, senza migrazione»); AELS (12 componenti) L1225, L1230; ADS L1238 (denominatore per ramo, esoneri esclusi).
- **Evidenza:**
  - *Testuale:* la formula usa le attività previste come denominatore.
  - *Inferenza:* aggiungendo componenti alle sessioni esistenti (laboratorio guidato, sfida autonoma, evidenza e così via), una sessione oggi al 100% scenderebbe, ad esempio, al 40%. Questo viola «preservare progressi». Lo stesso vale per il ricalcolo del denominatore al cambio di ramo.
- **Controesempio:** lo studente completa `cr-w07s1` con 5/5 attività in 6.5.1. In v-next la sessione ha 9 attività: avanzamento 56%, badge o livello non più raggiunto e regressione percepita.
- **Raccomandazione:** congelare il «completamento storico» come stato distinto (già previsto concettualmente in AAS) e calcolare il nuovo avanzamento solo sulle attività aggiunte. Specificare la regola di visualizzazione per le sessioni legacy.
- **Test proposto:** profilo sintetico con 30 sessioni al 100% in 6.5.1 → migrazione → verificare che lo stato «completamento storico» sia preservato e che nessuna competenza venga attribuita. Cambio di ramo Complete → Professional → Complete: denominatore e numeratore tornano identici, senza doppi conteggi.
- **Criterio di accettazione:** zero sessioni legacy declassate senza indicazione esplicita, zero doppi conteggi, percentuale coerente con la regola documentata.
- **Verificabilità:** la contraddizione è documentale; la verifica richiede runtime.

### E02-05 — P1 — Migrazione multi-sorgente e rollback dei dati non specificati
- **Sezione:** ROADMAP L18 (RC1 «installata su iPhone secondo l'utente»), L63 (sviluppo divergente da RC1: «10 avanti, 1 indietro»), README L53 («senza migrazione»), L15 e L20 («preservare… migrazione»), AVS L1258 («migrazione 6.5.1/RC1 isolata e ripetibile»).
- **Evidenza (testuale):** esistono almeno due popolazioni di dati da preservare: main 6.5.1 in produzione e RC1 in uso reale sull'iPhone dell'utente. RC1 conteneva un commit assente dal branch di sviluppo (dato storico del 25/11, non riverificato da me). Non esiste una matrice delle versioni sorgente → destinazione, né una strategia di downgrade.
- **Inferenza:** se un service worker vecchio, ancora in cache, carica dati già migrati, o se un rollback dell'app riporta il codice a una versione precedente, il codice vecchio può leggere uno schema più recente e corrompere o scartare i dati.
- **Impatto:** perdita di progressi reali, rischio massimo per G11 e R11.
- **Raccomandazione:**
  - matrice di migrazione esplicita (6.5.1 → v-next, RC1 → v-next, v-next → v-next+1);
  - backup automatico prima della migrazione;
  - riconoscimento di schemi futuri (una versione vecchia rifiuta in sola lettura e non sovrascrive);
  - riconciliare il commit presente solo in RC1 prima di qualsiasi merge;
  - trattare i dati RC1 come dati di produzione.
- **Test proposto:**
  1. migrazione da fixture 6.5.1 e da fixture RC1 reali anonimizzate;
  2. interruzione forzata a metà migrazione con ripresa;
  3. downgrade simulato (codice vecchio con dati nuovi): nessuna scrittura distruttiva;
  4. ripetizione della migrazione, con esito idempotente.
- **Criterio di accettazione:** per ogni sorgente, 100% dei campi conservati o trasformati secondo la regola documentata; zero scritture distruttive in downgrade; stato coerente dopo un'interruzione.
- **Verificabilità:** richiede codice, esecuzione reale e dispositivo fisico.

### E02-06 — P1 — Backup cifrato senza specifica crittografica né formato versionato
- **Sezione:** README L50, L58–L61; ROADMAP L44, L50; versione 6.7 «Sicurezza, affidabilità e backup» (L12).
- **Evidenza (testuale):**
  - «Risposte e punteggio corrente nel profilo cifrato»;
  - «Validazione backup: quattro casi superati» (simulati);
  - «backup cifrato end-to-end» non collaudato.

  Non sono documentati algoritmo, derivazione della chiave, gestione della passphrase, posizione della chiave, autenticazione del contenuto (integrità), versione del formato o procedura di recupero in caso di passphrase persa.
- **Ipotesi:** se la chiave è conservata nello stesso storage locale del profilo, la «cifratura» è offuscamento e non protezione.
- **Impatto:** G10 e G11 non verificabili. Rischio di backup non ripristinabili o falsamente protetti.
- **Raccomandazione:** specificare il formato (versione, salt, IV/nonce, cifratura autenticata, schemaVersion e checksum), il modello di minaccia (da chi protegge) e il comportamento con passphrase errata o file corrotto. Distinguere nella comunicazione all'utente «cifrato» da «offuscato».
- **Test proposto:**
  - test positivi: round-trip backup → ripristino su dispositivo pulito, confronto record per record;
  - test negativi: passphrase errata, file troncato, byte alterato, versione futura, backup 6.5.1 importato in v-next. In tutti i casi l'atteso è un rifiuto esplicito senza sovrascrittura dei dati esistenti.
- **Criterio di accettazione:** 100% dei record ripristinati; 0 accettazioni di file alterati; 0 sovrascritture dopo un errore.
- **Verificabilità:** richiede codice ed esecuzione reale.

### E02-07 — P1 — Durabilità dei dati su iOS e PWA non requisita
- **Sezione:** README L15, L61; ROADMAP L47–L52; ADS L1238 («compatibilità backup/ripristino/offline/migrazione»).
- **Evidenza:**
  - *Testuale:* i progressi risultano solo sul dispositivo; il backup è manuale.
  - *Ipotesi da collaudare:* Safari e iOS possono eliminare lo storage scrivibile dagli script in alcune condizioni (sito non installato e inattivo, pressione sullo spazio) e applicano quote di storage. Il comportamento differisce tra scheda Safari e PWA installata.
  - Con 420 sessioni, storico dei tentativi (AAS «tentativi senza limiti artificiali») e portfolio, il volume dei dati cresce.
- **Impatto:** perdita silenziosa di progressi, credenziali e storico.
- **Raccomandazione:** aggiungere un requisito esplicito di durabilità: richiesta di storage persistente dove supportata, promemoria di backup, rilevamento dello storage svuotato con ripristino guidato, limite e compattazione dello storico.
- **Test proposto:** su iPhone reale, sia come PWA installata sia in Safari:
  - riempimento con un profilo realistico di grandi dimensioni;
  - verifica dopo riavvio, aggiornamento iOS, assenza prolungata, spazio scarso;
  - test negativo: storage svuotato → l'app rileva la perdita e propone il ripristino invece di ripartire silenziosamente da zero.
- **Criterio di accettazione:** zero perdite non rilevate; il percorso di ripristino viene offerto nel 100% dei casi di storage svuotato.
- **Verificabilità:** richiede un dispositivo fisico.

### E02-08 — P1 — Il registro R01–R12 non è verificabile: mancano criteri, mappatura e matrice ARTM
- **Sezione:** ROADMAP L1273–L1292, L1258 («Matrice operativa non ancora compilata»), L1263 e L1322 (provenienza da immagini, IMG_9497 originale non verificato).
- **Evidenza (testuale):**
  - R01–R12 sono soli titoli con standard di riferimento, senza enunciato misurabile né criterio di accettazione.
  - La corrispondenza R ↔ G è solo implicita: R02 «Applicazione pratica e autonomia» non coincide con G02 «Riproducibilità pratica»; R10 e R11 rinviano ad «AVS», che è uno standard di processo, non di contenuto.
  - L'ARTM è vuota (0/420 record compilati).
  - AVS stesso richiede «requisito e criterio predefiniti» per chiudere un gate.
- **Impatto:** la tracciabilità richiesta dal mandato non è dimostrabile. Nessun gate è chiudibile secondo le regole di AVS. Il testo approvato deriva da trascrizioni parziali.
- **Raccomandazione:** per ogni R, scrivere enunciato, criterio misurabile, gate o gate associati, metodo di verifica (documentale, codice, runtime, dispositivo, umano) ed evidenza attesa. Pubblicare la matrice R × G × test. Far confermare all'utente che il testo trascritto corrisponde alla decisione originale, senza ri-approvarla nel merito.
- **Test proposto:** controllo di tracciabilità automatico: ogni R ha almeno un G e almeno un test; ogni test ha un R; non esistono test orfani.
- **Criterio di accettazione:** copertura bidirezionale al 100%; testo di R01–R12 confermato dall'utente come trascrizione fedele.
- **Verificabilità:** documentale.

### E02-09 — P1 — Mancano requisiti software di base
- **Sezione:** R01–R12 (L1275–L1288), checklist di rilascio (L45–L53).
- **Evidenza (testuale):** il registro è quasi interamente didattico. Mancano requisiti autonomi e verificabili su:
  - installazione e aggiornamento PWA;
  - perimetro offline;
  - prestazioni e dimensioni del bundle;
  - compatibilità dei browser;
  - durabilità dei dati (E02-07);
  - accessibilità dell'app stessa (non delle risorse: R08 riguarda le risorse);
  - continuità tra dispositivi (E02-14);
  - osservabilità degli errori lato client.

  La checklist L45–L53 contiene alcune di queste voci, ma come attività e non come requisiti con criteri.
- **Impatto:** G11 si riduce a «non regressione» senza definire la qualità tecnica attesa per la versione 7.0.
- **Raccomandazione:** aggiungere una sezione R-SW (sottorequisiti di R10 e R11, senza modificare gli standard approvati), con soglie misurabili da approvare. Esempi: dimensione massima della risorsa in precache, tempo di primo caricamento su rete lenta, matrice dei browser supportati.
- **Test proposto:** per ciascun R-SW, un test riproducibile (Lighthouse o equivalente, matrice dei dispositivi, prova offline).
- **Criterio di accettazione:** requisiti approvati dall'utente; ciascuno con test e soglia.
- **Verificabilità:** documentale per la definizione; runtime e dispositivo per la verifica.

### E02-10 — P1 — Senza G12-E non è definita una regola di accettazione: o stallo permanente o chiusura elusiva
- **Sezione:** AVS L1258 (V5 «validata didatticamente», V6 «accettata», «N/A motivato non elusivo», nessuna compensazione); AMVP L1259 («nessun test umano esterno disponibile», efficacia empirica umana non dimostrata); L1294–L1299.
- **Evidenza:**
  - *Testuale:* G12-E è «Non verificata» senza un piano per ottenerla.
  - *Inferenza:* se V5 richiede evidenza di efficacia didattica e G12-E non è ottenibile, nessuna sessione può raggiungere V5 né V6, quindi il rilascio è bloccato in modo permanente. In alternativa si dovrebbe applicare un N/A che AVS stessa vieta se elusivo.
- **Impatto:** rischio di deroga di fatto in Fase 6 sotto pressione di rilascio.
- **Raccomandazione:** separare formalmente:
  - **accettazione tecnico-documentale** (G01–G11 e G12-S, chiudibili);
  - **affermazioni di efficacia** (subordinate a G12-E).

  Il rilascio può diventare possibile con G12-E aperto solo a condizione che la comunicazione verso l'utente finale sia limitata alle affermazioni sostenibili (vedi sezione 11.A). Questa è una decisione dell'utente, non del revisore.
- **Test proposto:** revisione dei testi dell'app e della documentazione destinata agli studenti. Ogni affermazione di qualità deve essere associata alla classe di evidenza che la sostiene.
- **Criterio di accettazione:** regola scritta e approvata; zero affermazioni di efficacia o eccellenza non sostenute da G12-E nei testi rilasciati.
- **Verificabilità:** documentale.

### E02-11 — P2 — La conservazione degli indici perpetua una posizione della risposta corretta prevedibile
- **Sezione:** ROADMAP L285, L324, L375, L422, L457, L462 e seguenti («30/30 coppie stessa posizione», cumulativo 264/264; «ordine UI non verificato»); vincolo «preservare indici» (L20); AAS L1234 («distrattori plausibili»).
- **Evidenza:**
  - *Testuale:* in tutte le 264 sessioni la risposta corretta del quiz base e di quello avanzato occupa la stessa posizione. Gli indici sono vincolati a non cambiare.
  - *Inferenza:* se l'interfaccia non mescola le opzioni, la risposta al quiz avanzato è deducibile da quella del quiz base, il che falsa le prove AAS.
- **Impatto:** validità della valutazione (G03) compromessa; il vincolo software e lo standard di valutazione sono in conflitto.
- **Raccomandazione:** verificare nel codice se l'interfaccia mescola le opzioni. In caso contrario, introdurre un mescolamento in fase di visualizzazione che lascia invariato l'indice nei dati salvati e registra la risposta come indice logico.
- **Test proposto:** su 50 visualizzazioni dello stesso quiz, la distribuzione delle posizioni mostrate non è costante. La risposta salvata corrisponde all'opzione logica e non alla posizione grafica.
- **Criterio di accettazione:** indici nel JSON invariati; posizione mostrata non deducibile; nessuna regressione del punteggio storico.
- **Verificabilità:** richiede codice e runtime.

### E02-12 — P1 — La non regressione è solo statica e la baseline non è versionata rispetto al target
- **Sezione:** README L58–L61; ROADMAP L44, L1258 (baseline «72 settimane, 264 ID… 114 termini»), ALWS L1246 (36 settimane per livello).
- **Evidenza (testuale):**
  - I controlli dichiarati sono sintassi JS, conteggi e confronto dei JSON. Non è documentata alcuna suite di test automatica, alcuna integrazione continua né alcun test end-to-end.
  - La baseline «72 settimane» è incompatibile con il calendario target di 3 × 36 settimane per corso.
- **Impatto:** l'implementazione per blocchi della Fase 5 manca di una rete di sicurezza. Ambiguità su cosa significhi «regressione» rispetto a cosa.
- **Raccomandazione:**
  - definire due baseline: **B0** congelata (contenuti e dati originali da preservare) e **B-target** versionata;
  - introdurre JSON Schema del curriculum, test di invarianza (ID, indici, testi B0), test end-to-end dei flussi critici (studio, quiz, avanzamento, backup, ripristino, aggiornamento) e integrazione continua sul branch di sviluppo.

  Gli strumenti sono già citati nel curriculum stesso (Playwright, GitHub Actions; L457, L844).
- **Test proposto:**
  - pipeline che fallisce se un ID di B0 cambia, se un indice di B0 cambia, o se un JSON non rispetta lo schema;
  - test negativo: commit di prova che altera un indice, con fallimento atteso.
- **Criterio di accettazione:** pipeline verde e riproducibile; il test negativo fallisce come previsto; report salvati come artefatti.
- **Verificabilità:** richiede codice ed esecuzione.

### E02-13 — P2 — Lo «stato corrente» dei documenti è obsoleto, in violazione della Procedura permanente
- **Sezione:** ROADMAP L3 («Aggiornato: 25 novembre 2026»), L26 («Stato operativo corrente — 25 novembre 2026»), L41 («README allineato al commit 4d34f2c…»), L60 («Prossimo intervento: Fase 2C…»); README L3; Procedura permanente L67.
- **Evidenza (testuale):** le sezioni di stato corrente in testa ai documenti non riflettono le fasi 3A–3I del 26/11. La Procedura permanente impone di «aggiornare i riepiloghi correnti quando cambiano… prossimo passo».
- **Impatto:** chi riprende il lavoro (umano o AI) può leggere un prossimo passo errato. È rischioso perché la continuità del progetto si basa sulla rilettura di questi documenti (Regola 1).
- **Raccomandazione:** spostare le sezioni storiche sotto una sezione «Storico» e mantenere in testa un solo blocco «Stato corrente» autorevole con data, checkpoint e prossimo passo.
- **Test proposto:** controllo di coerenza: data e prossimo passo del blocco di testa coincidono con l'ultima sezione di fase.
- **Criterio di accettazione:** un solo «stato corrente» in ciascun documento, coerente con la Fase 3I.
- **Verificabilità:** documentale.

### E02-14 — P2 — Continuità tra dispositivi non progettata
- **Sezione:** C08 (L1266) «Mobile First iPhone, dichiarare… laboratori che richiedono computer»; Fase 2E (studio su iPhone, laboratori su desktop).
- **Evidenza:**
  - *Testuale:* studio su iPhone e laboratori su desktop sono previsti come flusso normale.
  - *Inferenza:* con progressi esclusivamente locali, lo stesso studente ha due profili divergenti.
- **Controesempio:** lo studente completa il laboratorio `cr-w11s4` su desktop. L'iPhone mostra la sessione incompleta; il badge «Data Management» non è riconosciuto su nessuno dei due dispositivi.
- **Raccomandazione:** decidere esplicitamente tra:
  - (a) un solo dispositivo autorevole con evidenze caricate in seguito;
  - (b) esportazione e importazione incrementale con fusione;
  - (c) sincronizzazione con backend, che è un cambio architetturale con implicazioni di privacy.

  Definire le regole di fusione dei conflitti.
- **Test proposto:** due profili divergenti → fusione → nessuna perdita e nessun doppio conteggio. Conflitto sulla stessa attività → regola deterministica.
- **Criterio di accettazione:** regola approvata; zero perdite nella fusione.
- **Verificabilità:** documentale per la decisione; runtime per la verifica.

### E02-15 — P2 — Manca un modello di archiviazione delle evidenze e del portfolio
- **Sezione:** AAS L1234 (portfolio di 15 elaborati per corso, «export»), ACS L1250, AELS L1230 («output documentato ed esportabile»).
- **Evidenza (testuale):** le evidenze includono video, codice, file BI e dataset. Non è definito se l'app conserva file, link o hash, né con quali limiti.
- **Ipotesi:** lo storage del browser su iOS non è adatto a molti file pesanti.
- **Raccomandazione:** modello «evidenza come riferimento», con link esterno controllato dallo studente, hash facoltativo e metadati, e limiti di dimensione per gli eventuali allegati locali.
- **Test proposto:** portfolio completo da 15 elementi → esportazione → importazione su dispositivo pulito → integrità dei riferimenti.
- **Criterio di accettazione:** esportazione e importazione senza perdite, entro i limiti dichiarati.
- **Verificabilità:** runtime.

### E02-16 — P2 — Le credenziali verificabili sono incompatibili con un'architettura apparentemente solo client
- **Sezione:** ACS L1250 («Open Badges/hash/firma/QR solo se verifica reale, hash non prova identità»).
- **Evidenza:**
  - *Inferenza:* nessun backend è documentato. Una verifica da parte di terzi richiede un emittente con chiave privata non presente sul dispositivo dello studente.
  - Una credenziale generata localmente è falsificabile dallo studente stesso.
- **Raccomandazione:** dichiarare le credenziali interne come «auto-attestazione documentata» finché non esiste un emittente server. In alternativa, approvare esplicitamente un componente di emissione con firma.
- **Test proposto:** test negativo: modificare localmente un profilo per auto-emettersi una Level Credential. Atteso: impossibile, oppure la credenziale è marcata come non verificabile.
- **Criterio di accettazione:** nessuna credenziale presentata come verificabile senza una verifica crittografica reale.
- **Verificabilità:** richiede codice.

### E02-17 — P2 — Le versioni del prodotto non sono collegate alle fasi
- **Sezione:** ROADMAP L5–L13 (6.6 qualità didattica, 6.7 sicurezza e backup, 7.0 versione definitiva) e fasi 4–6 (L1258, L1301–L1314).
- **Evidenza (testuale):** non è indicato quale versione conterrà lo schema v-next, le 420 sessioni o i rami. Il consolidamento di backup e sicurezza (6.7) è collocato dopo la 6.6, che però introduce i cambi di schema più rischiosi.
- **Raccomandazione:** mappare fase → versione → contenuto. Anticipare a prima dei cambi di schema i prerequisiti di affidabilità: backup verificato, migrazione, durabilità dei dati.
- **Test proposto:** nessun test runtime; verifica documentale della tabella di mappatura.
- **Criterio di accettazione:** tabella approvata e nessun cambio di schema pianificato prima del collaudo del backup.
- **Verificabilità:** documentale.

### E02-18 — P2 — Strumenti di modifica del JSON fragili
- **Sezione:** ROADMAP L178 («Primo tentativo di sostituzione testuale interrotto… indentazione non coincidente»), L281 («Primo tentativo ROADMAP errore interno»).
- **Evidenza (testuale):** le modifiche al curriculum avvengono per sostituzione di testo, con un errore documentato. La verifica a valle (confronto integrale) è solida, ma il metodo di scrittura non è strutturato.
- **Impatto:** con 156 sessioni nuove e 12 componenti per sessione, il rischio cresce più che linearmente.
- **Raccomandazione:** script di trasformazione strutturati, che leggono il JSON, lo modificano e lo validano con JSON Schema, versionati nel repository, con un dry-run che produce un diff semantico.
- **Test proposto:** riapplicare uno dei blocchi storici con lo script e verificare un output identico al commit storico.
- **Criterio di accettazione:** diff semantico vuoto; validazione superata.
- **Verificabilità:** richiede codice.

### E02-19 — P2 — Perimetro offline e dimensione dei contenuti non definiti
- **Sezione:** checklist L49; AELS L1230 (teoria di 800–1500 parole per sessione L3); 420 sessioni; risorse esterne obbligatorie.
- **Evidenza:**
  - *Testuale:* «Offline e cache» è non verificato.
  - *Inferenza:* il curriculum può crescere di un ordine di grandezza. Le risorse esterne e i laboratori non sono disponibili offline per natura.
- **Raccomandazione:** definire cosa deve funzionare offline (teoria, quiz, progressi, dizionario) e cosa no (risorse, laboratori). Valutare il caricamento del curriculum per livello invece di un unico JSON in precache. Mostrare indicatori «richiede connessione».
- **Test proposto:** modalità aereo dopo la prima installazione: apertura di una sessione L3, quiz, salvataggio, riconnessione, nessuna perdita. Misurare la dimensione della precache.
- **Criterio di accettazione:** perimetro offline rispettato al 100%; precache entro la soglia approvata (E02-09).
- **Verificabilità:** dispositivo fisico.

### E02-20 — P3 — Documentazione monolitica e difficile da mantenere
- **Sezione:** ROADMAP (287.684 caratteri, prosa molto compressa, ad esempio L1234–L1259).
- **Evidenza (testuale):** standard, registri, matrici e cronologia stanno in un unico file. La stessa CR-001 deve verificare il rischio di lettura troncata, a conferma del problema.
- **Raccomandazione:** suddividere in file dedicati, senza alterare la cronologia: standard approvati (uno per file), registro dei requisiti, registro dei gate, registro dei test, ADR, cronologia.
- **Criterio di accettazione:** ogni standard è citabile tramite percorso e versione; la ROADMAP resta un indice con la cronologia.
- **Verificabilità:** documentale.

### E02-21 — P3 — Riferimenti orfani e numerazioni residue
- **Sezione:** AMVP L1259 («sostituisce punto 16»: nessun punto 16 identificabile nei due documenti); L1316–L1320 (numerazioni «11.1», «11.2», «12.» provenienti dalle immagini); matrici 2E con rubrica 0–3, superata da C02 (L1266).
- **Raccomandazione:** risolvere i riferimenti o annotarli come provenienti dalla struttura delle immagini; aggiungere una nota «superato da C02» accanto alle rubriche 0–3.
- **Verificabilità:** documentale.

---

## 11. Raccomandazioni e verifiche mancanti

### 11.A — G12-S aperto e G12-E non verificata: affermazioni sostenibili
Questa analisi non costituisce una deroga ad AVS. La decisione resta all'utente (vedi E02-10).

| Classe di affermazione | Sostenibile senza G12-E? | Condizione |
|---|---|---|
| Conteggi strutturali (264 ID, 528 quiz, 1584 feedback, 420/528 feedback distinti) | Sì | Formulata come «indicatore statico», riverificata sul commit di rilascio |
| Conformità documentale agli standard interni (V2) | Sì | «Conforme allo standard interno AELS/AAS», non «eccellente» |
| Funzionamento tecnico (V3: backup, migrazione, offline) | Sì, se collaudato | Solo dopo collaudo reale, con ambiente, versione ed evidenza |
| Equivalenza gratuito/premium (V4) | Parziale | Solo «esecuzioni pilota con N input», senza valore statistico |
| Esiti delle simulazioni AMVP (G12-S) | Sì, con etichetta | «Simulazione con agenti AI; non misura l'apprendimento umano» |
| Credenziale come attestazione che le evidenze del singolo studente hanno superato la rubrica | Sì, con limiti | Specificare il metodo (automatico, autovalutazione, AI-assistito); non indipendente; vedi E02-16 |
| «Gli studenti acquisiscono la competenza X», «efficace», «di eccellenza», ore di studio umane, ritenzione, confronto di qualità con MIT, UT Austin e altri | **No** | Richiede G12-E e benchmark finale |

### 11.B — Verifiche mancanti, classificate per natura
- **Solo con accesso al codice:** E02-01, 02, 03, 06, 11, 12, 16, 18. In particolare: storage, schema, cifratura, mescolamento delle opzioni, service worker.
- **Con esecuzione reale (browser o CI):** E02-04, 05, 12, 15.
- **Con dispositivi fisici (iPhone, Safari, PWA installata):** E02-05, 07, 19, oltre alla checklist L45–L53.
- **Con decisione dell'utente:** E02-02 (vincolo sullo schema), 08 (conferma della trascrizione R01–R12), 10 (regola di accettazione senza G12-E), 14 (modello multi-dispositivo), 16 (emittente delle credenziali), 17 (mappatura fasi e versioni).
- **Con umani:** G12-E, inter-rater AAS su elaborati reali, carico ALWS reale.

### 11.C — Priorità suggerita prima o all'inizio della Fase 4
1. Documento architetturale as-is ricavato dal codice (E02-01).
2. Regola sullo schema v-next e politica degli ID (E02-02, E02-03).
3. Criteri R01–R12 e matrice R × G (E02-08, E02-09).
4. Baseline B0 e suite automatica minima di invarianza (E02-12).
5. Allineare il blocco «stato corrente» (E02-13).

Il prototipo 4A «AI-Powered Data Application» dovrebbe includere un mini-flusso dati reale (progresso, migrazione, backup) e non solo contenuti didattici, così da collaudare le scelte di E02-02, E02-04 ed E02-05 su piccola scala.

### 11.D — Simulazione, collaudo reale ed efficacia empirica
- **Questo rapporto è un esame documentale da parte di un'AI.** Non è una simulazione AMVP, non è un collaudo e non è una validazione empirica.
- Nessun test indicato nelle sezioni 10 e 11 è stato eseguito da me. Sono test proposti.
- **Collaudo reale** significa esecuzione su codice, browser e dispositivi reali con evidenze registrate. Non è avvenuto per nessuno dei punti software, salvo i controlli statici storici dichiarati nei documenti, che non ho riverificato.
- **Efficacia empirica umana (G12-E):** assente e non sostituibile da simulazioni o da revisioni AI, inclusa questa.

## 12. Esito complessivo
**PARZIALE.**

- **Conforme:** la governance del processo (separazione tra evidenze, vincoli di preservazione, stati AVS, criteri di chiusura dei gate) e la coerenza interna degli standard didattici dal punto di vista della tracciabilità delle decisioni.
- **Non verificabile documentalmente:** l'architettura software dell'app (storage, schema, cifratura, PWA, migrazione), perché non è descritta (E02-01).
- **Lacune P1 da risolvere prima della Fase 5:**
  - contraddizione tra il vincolo «nessuna modifica dello schema» e i requisiti approvati (E02-02);
  - politica degli ID mancante (E02-03);
  - regressione dell'avanzamento (E02-04);
  - migrazione multi-sorgente e rollback (E02-05);
  - specifica del backup (E02-06);
  - durabilità dei dati (E02-07);
  - requisiti R01–R12 senza criteri (E02-08);
  - requisiti software mancanti (E02-09);
  - regola su G12-E (E02-10);
  - non regressione solo statica (E02-12).
- **Non conformità documentale minore:** E02-13, rispetto alla Procedura permanente.

Nessun gate è chiuso o raccomandato per la chiusura da questo rapporto. La Fase 4 non è avviata; la sua autorizzazione spetta all'utente.

*Fine del rapporto CR-001 — E02.*
