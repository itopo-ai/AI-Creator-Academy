# CR-001 — E06 — Security & Privacy Review

**Progetto:** AI Creator Academy — Excellence Learning 6.6
**Revisione:** CR-001, prospettiva specialistica E06 (sicurezza informatica, privacy, protezione dei dati, sicurezza applicativa e dei sistemi AI)
**Natura del documento:** rapporto originale integrale di revisione documentale svolta da un'AI esterna simulata. Non è un audit umano indipendente, non è una consulenza legale e non è un collaudo tecnico.
**Destinatari:** coordinatore ChatGPT e utente. Le raccomandazioni non hanno effetto finché non vengono approvate.

---

## 1. Modello AI, versione e data

| Voce | Valore |
|---|---|
| Modello | Claude Opus 5.5 (Anthropic) |
| Identificativo del modello | `claude-opus-5-5` |
| Data della revisione | 26/11/2026 (fuso Europe/Rome) |
| Limite affidabile delle conoscenze del modello | fine giugno 2026 |
| Ambiente | sessione di lavoro cloud con shell Linux; accesso Git in sola lettura al repository pubblico tramite proxy |
| Accesso web | non usato per i contenuti, per scelta, in applicazione del perimetro dei materiali autorizzati |

## 2. Ruolo specialistico

Revisore AI esterno **simulato** per la prospettiva E06 del protocollo AMVP (ROADMAP.md L1259): sicurezza, privacy, protezione dei dati, sicurezza applicativa e sicurezza dei sistemi AI.

Non sono un revisore umano indipendente, un professionista abilitato, un DPO, un avvocato né un penetration tester. Nessuna parte del rapporto è un parere legale né un'attestazione di conformità.

## 3. Capacità e limiti

**Capacità utilizzate**
- Lettura integrale e confronto incrociato di due documenti lunghi (344.909 byte complessivi).
- Conoscenza generale di framework di sicurezza (OWASP ASVS/MASVS, OWASP Top 10 per applicazioni LLM, principi di privacy by design, GDPR, AI Act UE), di architetture PWA e di sicurezza degli agenti AI, aggiornata a giugno 2026.
- Verifica crittografica dell'identità dei materiali (SHA Git dei blob, conteggi).

**Limiti sostanziali**
- **Non ho ispezionato codice applicativo** (`index.html`, `sw.js`, curriculum JSON o altro). Tutte le affermazioni sull'applicazione derivano dai due documenti. Non attribuisco al codice proprietà che non ho visto.
- Non ho eseguito l'applicazione né test su browser, Safari, iPhone, PWA, backup o crittografia.
- Non ho consultato fonti esterne. Riferimenti normativi e condizioni dei fornitori citati qui sotto provengono dalle mie conoscenze generali (fino a giugno 2026) e sono indicati come **ipotesi da verificare**. Possono essere cambiati dopo quella data.
- Diverse fonti citate nella ROADMAP (es. documentazione MCP del 28/07/2026, blueprint PL-900 del 24/07/2026, chiusura OpenAI Evals 30/11/2026) sono successive alle mie conoscenze: non posso confermarle né smentirle.
- Le immagini citate nella Fase 3I (IMG_9493–9499 e compensative) non sono disponibili. Non ricostruisco parti coperte o fuori inquadratura.
- Un modello linguistico può sbagliare per omissione o interpretazione. Ogni anomalia va riesaminata con le evidenze indicate.

## 4. Bias e potenziali conflitti

- **Conflitto di fornitore.** Sono un modello Anthropic. I documenti raccomandano risorse Anthropic/Claude (es. ROADMAP L664, L695; README L85, L89) e il protocollo AMVP assegna a Claude il ruolo di revisore esterno (L1259). Ho un potenziale interesse indiretto a valutare con favore il ruolo di Claude o le risorse Anthropic. Mitigazione: nessuna raccomandazione di questo rapporto privilegia un fornitore. La parità tra fornitori resta un requisito.
- **Bias da ancoraggio al prompt.** Il mandato CR-001 è stato redatto dal coordinatore del progetto. Ho cercato attivamente contraddizioni anche nella struttura del mandato (es. E06-06).
- **Bias di severità.** Un revisore di sicurezza tende a sovrastimare i rischi. Per contenerlo, ogni anomalia distingue evidenza testuale, inferenza e ipotesi.
- **Assenza di garanzia d'indipendenza.** L'indipendenza dichiarata è solo procedurale (sezione 5), non istituzionale.

## 5. Indipendenza procedurale

- Non ho ricevuto né letto rapporti di altre prospettive (E01–E05, E07), analisi del coordinatore o documenti successivi al checkpoint.
- Ho lavorato soltanto sul checkpoint `f9d98c2bbd4d3622b9ccb5eeeb5c1811a2c4d401` e sui due blob autorizzati.
- Non ho modificato GitHub, standard o gate. Non ho autorizzato rilasci e non ho avviato la Fase 4.
- **Accessi tecnici accidentali a metadati (dichiarazione obbligatoria):**
  1. Lo strumento di collegamento al repository ha risposto che il repository è **pubblico** e leggibile in forma anonima. Questa è un'informazione di metadato, non di contenuto.
  2. Per ottenere il commit ho eseguito `git fetch --depth 1` del solo commit di checkpoint. Così sono stati scaricati in un archivio locale compresso **anche gli oggetti degli altri file del commit**. **Non li ho estratti, elencati né letti.** Ho estratto con `git cat-file blob` solo i due blob autorizzati.
  3. Il comando `git ls-tree` è stato filtrato ai soli percorsi `README.md` e `ROADMAP.md`.
  4. `git log -1` ha mostrato **data e messaggio del commit di checkpoint**: `2026-11-26 12:52:17 +0100`, «docs: align phase 3I status with recovered evidence». Non ho tratto conclusioni dal messaggio.

## 6. Ambito, materiali e checkpoint

| Voce | Valore |
|---|---|
| Repository | `itopo-ai/AI-Creator-Academy` |
| Commit di checkpoint | `f9d98c2bbd4d3622b9ccb5eeeb5c1811a2c4d401` |
| Materiale 1 | `README.md`, blob `abca6f1ce6345ed1cc55eb5dd5f78ff0a7232afb` |
| Materiale 2 | `ROADMAP.md`, blob `af9888bc28f0fef48ea226e86fe3be5a24913008` |
| Esclusi | codice applicativo, curriculum JSON, altri file, rapporti specialistici, analisi del coordinatore, documenti successivi |
| Mandato | E06 (sicurezza e privacy) e mandato comune CR-001 (R01–R12, G12-S/G12-E, affermazioni sostenibili) |

I riferimenti nel rapporto usano la forma `README L<n>` e `ROADMAP L<n>`, cioè il numero di riga nei file del checkpoint.

## 7. Esito della verifica preliminare

**Esito: SUPERATA.** Accesso integrale a entrambi i documenti, senza troncamenti.

| Controllo | Atteso | Rilevato | Esito |
|---|---|---|---|
| Tipo oggetto checkpoint | commit | `commit` | ✔ |
| Blob README.md nel checkpoint | `abca6f1c…2afb` | `abca6f1ce6345ed1cc55eb5dd5f78ff0a7232afb` | ✔ |
| Blob ROADMAP.md nel checkpoint | `af9888bc…3008` | `af9888bc28f0fef48ea226e86fe3be5a24913008` | ✔ |
| `git hash-object` del file estratto, README | uguale al blob | uguale | ✔ |
| `git hash-object` del file estratto, ROADMAP | uguale al blob | uguale | ✔ |
| README, caratteri Unicode | 54.465 | 54.465 | ✔ |
| README, righe | 183 | 183 | ✔ |
| ROADMAP, caratteri Unicode | 287.684 | 287.684 | ✔ |
| ROADMAP, righe | 1.322 | 1.322 | ✔ |
| README, byte UTF-8 (informativo) | — | 54.854 | — |
| ROADMAP, byte UTF-8 (informativo) | — | 290.224 | — |

**Metodo di lettura:** Git in sola lettura. Ho letto README in un unico passaggio (righe 1–183) e ROADMAP in segmenti consecutivi senza sovrapposizioni né salti: 1–240, 241–365, 366–465, 466–575, 576–695, 696–895, 896–1145, 1146–1285, 1286–1322.

## 8. Metodo di revisione

1. Verifica d'identità dei materiali (sezione 7).
2. Lettura integrale, con annotazione di ogni passaggio pertinente a E06: dati, persistenza, cifratura, backup, segreti, autorizzazioni, AI/agenti, valutazioni, credenziali, governance, normativa, parità, supply chain e prototipi.
3. Distinzione di tre livelli epistemici in ogni anomalia:
   - **Evidenza testuale (ET):** quanto scritto nei documenti, con riga.
   - **Inferenza (INF):** conseguenza logica ragionevole dalle evidenze. Non è verificata.
   - **Ipotesi (IP):** possibilità che richiede verifica su codice, ambiente o fonti esterne.
4. Confronto incrociato: standard approvati (AELS, AAS, ADS, AES, ALWS, ACS, AVS, AMVP), registro R01–R12, gate G01–G12, sottogate G12-S/G12-E e piano 4A–4H.
5. Ricerca attiva di contraddizioni, lacune e controesempi.
6. Classificazione con la scala AVS (ROADMAP L1258):
   - **P0:** critica, blocco immediato.
   - **P1:** alta, blocca l'accettazione pertinente.
   - **P2:** media, richiede correzione o decisione motivata.
   - **P3:** bassa, intervento pianificato.
7. Separazione dei tipi di verifica: revisione documentale, simulazione AI, collaudo tecnico reale, efficacia empirica umana e verifiche esterne (sezione 11.4).

Il mandato vieta di presumere vulnerabilità non verificate. Perciò ogni anomalia riguarda **lacune di specifica, di tracciabilità o di verifica**, non difetti del codice.

## 9. Punti di forza

1. **Onestà epistemica sistematica.** I documenti distinguono controlli statici, simulazioni e collaudi in modo costante. Dichiarano esplicitamente che «persistenza reale, backup, offline e sicurezza non collaudati» (README L50) e che i controlli storici «non equivalgono a test end-to-end» (ROADMAP L44). Nessuna affermazione di sicurezza o conformità viene presentata come verificata.
2. **Controllo d'integrità del repository.** Il protocollo verifica ogni volta gli SHA delle teste di main e RC1 e il diff limitato ai file autorizzati, rilegge dopo la scrittura e vieta ZIP intermedi (ROADMAP L67–69, L141–143). È una buona base contro modifiche non autorizzate.
3. **Dati sintetici di default nei laboratori.** AELS richiede «materiali originali/sintetici/licenziati, nessun dato personale o riservato necessario» (ROADMAP L1230). Molti laboratori specificano dati fittizi e sandbox.
4. **Contenuti didattici di sicurezza maturi**, con prove negative:
   - prompt injection trattata come dato non fidato (L296, L392, L644);
   - approvazione vincolata al payload e nuova approvazione se il piano cambia (L386);
   - RLS e accesso incrociato negato con due utenti (L351, L799, L888);
   - rotazione dei segreti esposti (L338, L432);
   - idempotenza e vincoli univoci (L382, L625–627);
   - «stdio non sandbox» per MCP (L838);
   - divieto di esporre l'endpoint Ollama senza autenticazione (L847).
5. **Minimizzazione nelle credenziali e nella diagnostica.** ACS esclude biometria e documenti obbligatori e riconosce che «hash non prova identità» (L1250). ADS evita la sorveglianza invasiva (L1238). L'orientamento alla scelta dell'AI non raccoglie credenziali (L414).
6. **Registro AI senza credenziali né chat private** (AELS, L1230).
7. **Parità economica come requisito da dimostrare**, non come risultato acquisito (L363). I trial non valgono come alternativa stabile (L365, L1242).
8. **Nessuna compensazione degli errori critici.** Sicurezza e privacy sono «errori critici non compensabili» nella valutazione degli studenti (AAS, L1234).
9. **Separazione dei ruoli AMVP** con soluzioni nascoste e dichiarazione esplicita che la revisione AI non è un audit umano (L1259).

## 10. Osservazioni e anomalie

Riepilogo per priorità: **P0: 0 · P1: 6 · P2: 10 · P3: 1** (17 anomalie).

| ID | Priorità | Titolo breve | Gate |
|---|---|---|---|
| E06-01 | P1 | R10/G10 senza baseline di sicurezza e criteri di accettazione per l'app | G10, G11 |
| E06-02 | P1 | Persistenza, cifratura, backup, ripristino e migrazione non specificati né collaudati con produzione attiva | G10, G11 |
| E06-03 | P1 | Assenza di inventario dati e ciclo di vita per le nuove categorie di dati | G10, G09, G04 |
| E06-04 | P1 | Integrità di valutazioni, esoneri e credenziali non progettata contro la manipolazione | G03, G04, G09, G10 |
| E06-05 | P1 | Criteri di sicurezza dei prototipi 4A/4B non definiti come criteri d'uscita | G10, G02, G05 |
| E06-06 | P1 | Contraddizione strutturale G12-E / AVS: V5–V6 irraggiungibili senza deroga | G12, R12 |
| E06-07 | P2 | La parità gratuito/premium non comprende la protezione dei dati | G05, G06, G10 |
| E06-08 | P2 | Dati personali di terzi nei laboratori e nel portfolio | G10, G08, G09 |
| E06-09 | P2 | Minori e requisiti d'età dei fornitori non trattati | G10, G05 |
| E06-10 | P2 | Sicurezza dei laboratori sul dispositivo dello studente e supply chain di modelli e strumenti | G10, G02, G07 |
| E06-11 | P2 | Supply chain e risorse esterne dell'Academy | G08, G10 |
| E06-12 | P2 | Autenticità del registro decisionale e privilegi del coordinatore AI | G10, G11, R12 |
| E06-13 | P2 | Gestione incidenti, segnalazione vulnerabilità e rollback dell'app non definiti | G10, G11 |
| E06-14 | P2 | Requisiti normativi da qualificare giuridicamente (GDPR, AI Act, ePrivacy) | G10 |
| E06-15 | P2 | Tracciabilità R01–R12 ↔ standard ↔ gate implicita e incompleta | tutti, R12 |
| E06-16 | P3 | Incoerenze documentali di stato e di vocabolario | G11, R12 |
| E06-17 | P2 | Valutazione AI-assistita e AMVP esposte a prompt injection e contaminazione | G03, G12, G10 |

---

### E06-01 — R10/G10 senza baseline di sicurezza applicativa né criteri di accettazione predefiniti

- **Priorità:** P1. Blocca l'accettazione di G10, non la prosecuzione documentale.
- **Riferimenti:** ROADMAP L12, L1258, L1273–1292; README L15, L178.
- **Evidenza testuale:**
  - R10 «Sicurezza e privacy» è associato solo ad «AVS» (L1286).
  - AVS è uno standard di processo. Richiede per la chiusura «requisito e criterio predefiniti» e una «prova pertinente realmente eseguita» (L1258).
  - La versione 6.7 «Sicurezza, affidabilità e backup» è indicata come «Programmata» (L12).
  - Nei sette standard approvati nessun requisito di sicurezza dell'app (autenticazione locale, protezione della memoria, CSP, gestione dell'import, aggiornamento del service worker) è definito come requisito verificabile.
  - Il threat model compare solo come argomento didattico per gli studenti (cr-w20s1, L431, L886), non come artefatto del progetto.
- **Inferenza:** Oggi G10 non può essere chiuso per costruzione, perché manca il «criterio predefinito» richiesto da AVS. In più, la collocazione della sicurezza in 6.7 rende ambiguo se un rilascio 6.6 possa avvenire senza un livello minimo di sicurezza dell'app.
- **Ipotesi:** Essendo una PWA (README L57 cita `sw.js`), le superfici rilevanti sono probabilmente queste: storage del browser, cache del service worker, rendering di contenuti del curriculum, import di file di backup e link esterni. Da verificare sul codice.
- **Impatto:** Gate di sicurezza non dimostrabile. Rischio che la Fase 5 implementi nuove funzioni (diagnostica, portfolio, credenziali, scelta del ramo) senza requisiti di sicurezza da rispettare. Le correzioni successive costerebbero di più.
- **Standard coinvolti:** AVS (processo), AELS/AAS/ADS/ACS (nuove funzioni che trattano dati).
- **Requisiti:** R10, R11.
- **Gate:** G10, G11.
- **Raccomandazione:**
  1. Redigere, prima dell'avvio di 4C/4D, uno **Academy Security & Privacy Baseline** come annesso AVS. Deve contenere:
     - threat model dell'app (asset, attori, confini di fiducia, flussi dati della PWA);
     - livello target di un riferimento riconosciuto, da scegliere e motivare (es. OWASP ASVS livello 1 per le parti web e OWASP MASVS-L1 come guida per l'uso mobile);
     - requisiti numerati collegati a R10 e G10.
  2. Chiarire con una decisione dell'utente se 6.6 può essere rilasciata senza i requisiti di 6.7, o se un sottoinsieme minimo è prerequisito.
- **Test:** revisione documentale della baseline. Per ogni requisito: test positivo e negativo, ambiente, versione ed esito atteso.
- **Criterio di accettazione:** baseline approvata dall'utente. Ogni requisito R10 ha ID, criterio, metodo di prova e collegamento a G10. La decisione su 6.6/6.7 è registrata nella ROADMAP.

### E06-02 — Persistenza locale, cifratura, backup, ripristino e migrazione non specificati né collaudati, con produzione attiva

- **Priorità:** P1.
- **Riferimenti:** README L15, L50, L53, L56–61; ROADMAP L10, L12, L18, L43–53, L1258.
- **Evidenza testuale:**
  - «Risposte e punteggio corrente nel profilo cifrato» (README L50).
  - Nello stesso paragrafo: «persistenza reale, backup, offline e sicurezza non collaudati».
  - QA 6.6.1: «Validazione backup: quattro casi superati» su base strutturale. Restano «backup cifrato end-to-end, aggiornamento» (README L59–61).
  - main 6.5.1 è «Produzione» (ROADMAP L10). RC1 è «installata su iPhone secondo l'utente» (L18).
  - La checklist di rilascio ha come voci aperte «Backup cifrato e ripristino effettivo», «Aggiornamento dalla 6.5.1 e conservazione effettiva dei progressi» e «Aggiornamento automatico» (L50–52).
  - Nessun documento indica algoritmo, derivazione della chiave, gestione della passphrase, luogo di conservazione della chiave o comportamento in caso di passphrase persa.
- **Inferenza:**
  - Una funzione di cifratura **in produzione** non ha specifica né collaudo documentati. La protezione effettiva dei dati degli utenti è quindi non verificabile.
  - Gli standard ADS e ACS aggiungeranno dati più ricchi (diagnostica, esoneri, evidenze, portfolio) allo stesso meccanismo. Il rischio cresce.
- **Ipotesi da verificare sul codice e su dispositivo:**
  - (a) Se la chiave o il materiale per derivarla risiede nello stesso storage dei dati cifrati, la cifratura protegge poco.
  - (b) Una derivazione della chiave debole renderebbe i backup esportati vulnerabili a tentativi offline.
  - (c) Su Safari/iOS lo storage scrivibile da script può essere eliminato dal sistema in certe condizioni (es. inattività per siti non aggiunti alla schermata Home) o per limiti di quota. Questo comporta perdita di dati.
  - (d) L'import di un file di backup è un input non fidato: JSON malformato, oggetti molto grandi, chiavi come `__proto__`, contenuti poi mostrati nell'interfaccia.
  - (e) Un aggiornamento del service worker può attivare una migrazione su dati esistenti senza un punto di ripristino.
- **Impatto:** possibile perdita irreversibile dei progressi, falsa percezione di protezione, regressioni in migrazione 6.5.1 → 6.6. Tocca R11 «Compatibilità e non regressione».
- **Standard coinvolti:** AVS (runtime futuro, L1258), ADS e ACS (backup, ripristino e versioning richiesti, L1238 e L1250).
- **Requisiti:** R10, R11.
- **Gate:** G10, G11.
- **Raccomandazione:**
  1. Documentare in modo descrittivo, prima della Fase 5, lo **schema di cifratura e backup oggi in produzione**: algoritmo, modalità, derivazione della chiave e parametri, gestione della passphrase, contenuto e formato del backup, versioning dello schema. Va ricavato dal codice da chi può ispezionarlo, senza modificarlo.
  2. Definire una politica esplicita sulla passphrase persa, comunicata all'utente.
  3. Definire il comportamento davanti a eliminazione dello storage, quota piena e browser diversi.
  4. Prevedere un backup automatico prima di ogni migrazione e un rollback.
- **Test (collaudo reale, Fase 4D/6):**
  - round-trip backup → ripristino su dispositivo pulito, con confronto record per record;
  - passphrase errata;
  - file corrotto, troncato, oversize e con chiavi anomale;
  - backup 6.5.1 importato in 6.6;
  - migrazione interrotta a metà (chiusura app);
  - PWA iPhone dopo un periodo di inattività;
  - aggiornamento del service worker con rollback;
  - verifica che nessun dato in chiaro resti in cache o storage dopo la cifratura.
- **Criterio di accettazione:** specifica approvata. Tutti i test eseguiti su Safari/iPhone reale e su almeno un altro browser, con evidenze riproducibili. Zero perdite di dati non annunciate. Errori espliciti per gli input non validi. Migrazione ripetibile e reversibile.

### E06-03 — Inventario dei dati e ciclo di vita assenti a fronte di nuove categorie di dati

- **Priorità:** P1. Blocca l'accettazione di 4C e della Fase 5, non l'avvio documentale di 4A/4B.
- **Riferimenti:** ROADMAP L1234, L1238, L1250; README L154, L158, L170.
- **Evidenza testuale:** gli standard approvati introducono nuove categorie di dati per studente:
  - risultati diagnostici per sei aree, inclusi matematica, statistica e AI literacy (ADS, L1238);
  - esoneri, recupero e cambio ramo (L1238);
  - evidenze, «registro AI» e portfolio con «pubblicazione facoltativa/privacy» (AAS, L1234);
  - credenziali con «titolare scelto», stato «revocata» e storico (ACS, L1250).
  
  ADS indica «dati minimi, versione test, evidenze, storico» e «nessuna modifica schema» (L1238), ma non c'è inventario, classificazione, conservazione, cancellazione né localizzazione (solo dispositivo? sincronizzazione?).
- **Inferenza:** La minimizzazione è dichiarata come principio, ma manca lo strumento che la renderebbe verificabile. I profili diagnostici (lacune matematiche, digitali, economiche) sono dati valutativi sulla persona e possono risultare imbarazzanti se esposti. Lo storico conservato «senza scadenza automatica» (ACS) entra in tensione con la limitazione della conservazione, se i dati escono dal dispositivo.
- **Ipotesi:** Se tutti i dati restano solo sul dispositivo dello studente, molte questioni normative si attenuano. Il documento però non lo afferma.
- **Impatto:** rischio di progettare in 4C e Fase 5 flussi e schemi con dati superflui, difficili da correggere dopo. Mancano basi per informativa, cancellazione ed esportazione.
- **Standard coinvolti:** ADS, AAS, ACS, AELS, AVS.
- **Requisiti:** R04, R09, R10.
- **Gate:** G04, G09, G10.
- **Raccomandazione:**
  1. Redigere un **Registro dei dati dell'Academy**. Per ogni elemento: finalità, base (anche solo funzionale), classificazione (pubblico/interno/personale/valutativo/segreto), luogo di conservazione, cifratura, inclusione nel backup, conservazione, cancellazione da parte dello studente, esportazione, pubblicazione.
  2. Dichiarare esplicitamente se l'architettura è solo locale.
  3. Prevedere la funzione «cancella tutti i miei dati» e un'esportazione leggibile.
- **Test:** revisione documentale del registro. In collaudo: cancellazione completa (storage, cache, backup locali), esportazione completa e confronto con il registro.
- **Criterio di accettazione:** registro approvato prima di 4C. Ogni campo dello schema futuro è riconducibile a una voce. Nessun dato senza finalità. La cancellazione è verificata su dispositivo reale.

### E06-04 — Integrità di valutazioni, esoneri e credenziali non progettata contro la manipolazione

- **Priorità:** P1, per l'accettazione dell'implementazione ACS/AAS. Nessuna emissione è oggi attiva (L1250).
- **Riferimenti:** ROADMAP L285, L324, L375, L422, L462, L513, L560, L607, L652, L1234, L1238, L1250; README L50.
- **Evidenza testuale:**
  - In tutti i blocchi d'audit, quiz base e avanzato della stessa sessione hanno la risposta corretta nella **stessa posizione**: «264/264 coppie stessa posizione» (L652). L'ordine nell'interfaccia non è verificato.
  - AAS: «tentativi senza limiti artificiali, storico e miglior risultato valido» (L1234).
  - ADS: teoria «senza consultazione su base dichiarativa» (L1238).
  - ACS: Level Credential «With Distinction», Program Credential, modalità «automatica, autovalutazione strutturata, AI assistita non indipendente», export, «hash/firma/QR solo se verifica reale» (L1250).
  - README L50: «Non è un esame indipendente».
- **Inferenza:**
  - (a) La correlazione di posizione tra base e avanzato riduce la validità della misura: chi conosce una risposta può indovinare l'altra.
  - (b) Tentativi illimitati con «miglior risultato» e varianti finite, senza randomizzazione documentata, permettono di superare la soglia per esaustione.
  - (c) In un'app solo client, le chiavi delle risposte e i punteggi sono per natura accessibili e modificabili da chi controlla il dispositivo. Questo è un limite architetturale, non un difetto presunto del codice.
  - (d) Credenziali con nomi forti, esportabili, possono essere presentate a terzi come attestazioni verificate pur essendo, di fatto, auto-attestate.
- **Ipotesi:** Le chiavi delle risposte sono distribuite nel curriculum JSON lato client. È plausibile perché si parla di «indici delle risposte corrette» preservati, ma va verificato.
- **Impatto:** falsificazione o gonfiamento di competenze, esoneri impropri (falsi esoneri già citati come rischio in AVS, L1258), danno reputazionale se credenziali auto-attestate vengono scambiate per verificate. Tocca l'errore critico «falsificazione» di AAS.
- **Standard coinvolti:** AAS, ADS, ACS, AVS.
- **Requisiti:** R03, R04, R09, R10.
- **Gate:** G03, G04, G09, G10.
- **Raccomandazione:**
  1. Registrare la correlazione di posizione come anomalia di G03. Rimuoverla in Fase 5, rimescolando le opzioni all'interno dei vincoli «indici preservati»: ad esempio con un ordine di presentazione separato dall'indice memorizzato, previa decisione su compatibilità e migrazione.
  2. Nell'AAS: banche di varianti con rotazione, intervallo o requisito di ripasso tra tentativi, metrica «primo tentativo» accanto al «miglior risultato».
  3. Nell'ACS: dichiarare in modo visibile sulla credenziale il **metodo di verifica** (auto-attestata, automatica non sorvegliata, revisione umana dimostrata), anche quando assente. Vietare formati che suggeriscono verificabilità esterna (QR, firma) finché non esiste un verificatore reale. Usare una denominazione prudente nell'export (es. «attestato interno di completamento»).
  4. Per gli esoneri: affiancare alla diagnostica teorica la prova pratica, già prevista, come condizione necessaria.
- **Test:**
  - analisi statistica delle posizioni sul curriculum finale;
  - prova di esaustione: numero di tentativi necessari per superare la soglia con risposte casuali;
  - modifica manuale dello storage e verifica dell'effetto sulla credenziale (prova negativa: la credenziale deve dichiarare la propria natura auto-attestata);
  - revisione del testo della credenziale esportata.
- **Criterio di accettazione:** nessuna correlazione sistematica di posizione. Probabilità di superamento per esaustione documentata e accettata dall'utente. Ogni credenziale esportata riporta metodo e natura in modo non rimovibile senza alterazione evidente. Nessun formato di verifica senza verificatore funzionante.

### E06-05 — Criteri di sicurezza dei prototipi 4A e 4B non definiti come criteri d'uscita

- **Priorità:** P1, da risolvere prima dell'avvio della Fase 4 (che resta non autorizzata).
- **Riferimenti:** ROADMAP L1258, L1305–1318, L847, L1218, L769, L845.
- **Evidenza testuale:**
  - 4A «AI-Powered Data Application: teoria, codice, dati, integrazione AI e test» (L1305). L'output atteso è «applicazione funzionante, codice sorgente, integrazione AI reale» (L1316).
  - 4B: «workflow AI realmente funzionante in sandbox, baseline, holdout, test negativi» (L1318).
  - AVS elenca per 4B «sandbox/log/test negativi» (L1258), ma per 4A non elenca controlli di sicurezza.
  - Il capstone Business L3 enumera test injection, replay e duplicati e log minimizzati (L1218).
  - Le piattaforme candidate hanno comportamenti rilevanti: Supabase Free senza backup automatici (L769), Render con filesystem effimero (L845), Workers AI con quote e piani a pagamento per alcuni modelli (L845).
- **Inferenza:** 4A combina AI reale, dati e probabilmente autenticazione e deploy, cioè la superficie più ampia del progetto. Senza criteri d'uscita di sicurezza, 4D (collaudi) e 4H (dossier) non hanno un riferimento oggettivo per G10. C'è anche un rischio economico: chiavi API o endpoint esposti durante il prototipo possono generare costi, in contrasto con AES «costo gratuito zero».
- **Ipotesi:** Il prototipo verrà provato da AI simulate (4E) e forse pubblicato su hosting gratuito. Non è dichiarato.
- **Impatto:** prototipo che dimostra la qualità didattica ma anche, involontariamente, pratiche insicure. Esposizione di endpoint, consumo di quote o costi.
- **Standard coinvolti:** AVS, AES (costo zero), AELS (laboratori con dati sintetici), AAS (errori critici di sicurezza).
- **Requisiti:** R02, R05, R10.
- **Gate:** G02, G05, G10.
- **Raccomandazione:** aggiungere al piano 4A/4B una **scheda di sicurezza del prototipo** con almeno:
  1. threat model sintetico;
  2. solo dati sintetici;
  3. segreti solo lato server o nel gestore segreti della piattaforma, mai nel repository o nel client, con scansione dei segreti sul repository del prototipo;
  4. autenticazione e autorizzazione con prova negativa a due utenti;
  5. limiti di quota e **tetto di spesa a zero**, cioè arresto prima del superamento della quota gratuita;
  6. agenti con allowlist degli strumenti, nessuna azione esterna reale, approvazione vincolata al payload, limite d'iterazioni, kill switch;
  7. test prompt injection diretta e indiretta (documento ostile), con verifica di assenza di esfiltrazione;
  8. log minimizzati senza segreti né dati personali;
  9. deploy con rollback provato e backup del DB se la piattaforma non lo fornisce;
  10. dismissione del prototipo (revoca chiavi, cancellazione dati, spegnimento endpoint).
- **Test:** checklist eseguita in 4D con evidenze: scanner segreti, prove negative di autorizzazione, prove di injection, prova di superamento della quota, prova di rollback.
- **Criterio di accettazione:** tutti i controlli eseguiti con esito registrato. Zero segreti nel repository e nel bundle client. Zero azioni esterne non autorizzate. Zero errori critici AAS di sicurezza. Costo effettivo documentato pari a zero.

### E06-06 — Contraddizione strutturale G12-E / AVS: stati V5–V6 irraggiungibili senza deroga (mandato comune)

- **Priorità:** P1 per la governance dell'accettazione. Non riguarda la sicurezza tecnica, ma la logica di chiusura dei gate.
- **Riferimenti:** ROADMAP L1258, L1259, L1294–1299; README L178–179, L183.
- **Evidenza testuale:**
  - AVS: «V5 validata didatticamente, V6 accettata». La chiusura richiede una «prova pertinente realmente eseguita», con «nessuna compensazione» (L1258).
  - AMVP: «nessun test umano esterno disponibile… efficacia empirica umana non dimostrata» (L1259).
  - G12-E «Non verificata» (L1297).
  - «Prima di un eventuale rilascio stabilire quali affermazioni sulla qualità siano sostenibili in assenza di G12-E. Nessuna chiusura automatica né deroga ai criteri AVS» (L1299).
- **Inferenza:** Se G12 comprende G12-E e non esistono tester umani, G12 non può chiudersi. Con «nessuna compensazione» e «nessuna deroga», nessuna sessione può raggiungere V6 e nessun rilascio è accettabile secondo AVS. Delle due l'una: o il rilascio richiede una **decisione esplicita di accettazione del rischio** (che non è una deroga ai criteri, ma una decisione documentata su un gate non chiudibile), oppure il criterio di G12 va riformulato distinguendo «gate richiesto per il rilascio» da «gate da monitorare dopo il rilascio».
- **Impatto:** blocco di fatto del rilascio, oppure, peggio, una chiusura informale non tracciata sotto pressione.
- **Standard coinvolti:** AVS, AMVP.
- **Requisiti:** R12, R01.
- **Gate:** G12 (G12-S, G12-E).
- **Raccomandazione:**
  1. Definire nell'AVS uno stato esplicito per G12-E, es. «non verificabile allo stato – rischio accettato con limitazione delle affermazioni». Va approvato dall'utente, con motivazione, data, revisione periodica e condizioni di riapertura.
  2. Subordinare il rilascio alla chiusura di G12-S **e** al rispetto di una **politica delle affermazioni** (sotto).
  3. Prevedere, se in futuro disponibili, misure post-rilascio volontarie e anonime, con dati minimi.
- **Affermazioni sostenibili senza G12-E (dal punto di vista E06 e del mandato comune), senza derogare ad AVS:**

| Affermazione | Sostenibile senza validazione empirica? | Condizione |
|---|---|---|
| «Il percorso è progettato secondo standard interni (AELS, AAS…)» | Sì | dichiarare che sono interni e non certificazioni |
| «Il curriculum tratta temi di sicurezza, privacy e AI responsabile» | Sì | verificabile documentalmente |
| «Le competenze obbligatorie sono progettate per essere conseguibili senza acquisti» | Sì, come intento | solo se G05 e G06 sono verificati tecnicamente; altrimenti «progettato per» |
| «Le simulazioni AI indicano…» | Sì, solo con la qualifica «simulazione AI, non studenti reali» | G12-S chiuso |
| «Efficace», «migliora l'apprendimento», «prepara al lavoro» | **No** | richiede G12-E |
| «Eccellente», «di livello internazionale», «superiore a…» | **No** | richiede benchmark e G12-E (già escluso in L1230 e L1258) |
| «Sicuro», «i tuoi dati sono protetti», «cifrato end-to-end» | **No**, allo stato | richiede chiusura G10 con collaudo reale (E06-01, E06-02) |
| «Conforme GDPR / AI Act» | **No** | richiede verifica giuridica professionale (E06-14) |
| «Credenziale verificata/verificabile» | **No** | richiede verificatore reale (E06-04) |
| «I dati restano sul tuo dispositivo» | Solo dopo verifica del codice | E06-03 |

- **Test:** revisione documentale dell'AVS emendato. Prima del rilascio, verifica testuale di ogni testo pubblico (app, README, portfolio, credenziali) contro la tabella.
- **Criterio di accettazione:** stato G12-E definito e approvato. Nessun testo pubblico contiene affermazioni della colonna «No» senza la condizione soddisfatta.

### E06-07 — La parità gratuito/premium non comprende la protezione dei dati

- **Priorità:** P2.
- **Riferimenti:** README L89, L162; ROADMAP L363–365, L418, L665, L769, L845, L1242.
- **Evidenza testuale:**
  - AES definisce l'equivalenza su «obiettivi, competenze, difficoltà cognitiva, requisiti elaborati, rubriche/soglie» (L1242). La protezione dei dati non è tra i criteri.
  - Il percorso gratuito poggia su account AI gratuiti (L418) e piattaforme cloud gratuite con limiti: Supabase Free senza backup automatici e con pausa dopo inattività (L769), Render con filesystem effimero (L845).
  - La FAQ del tier gratuito ChatGPT è stata consultata solo per i limiti d'uso (L665).
- **Inferenza:** Lo studente che segue il percorso gratuito potrebbe accettare condizioni di trattamento dei propri prompt e file diverse (conservazione, uso per addestramento, controlli disponibili) e una minore resilienza dei propri lavori. Questo produrrebbe una disparità di **protezione**, non di competenza, che AES non intercetta.
- **Ipotesi:** Per diversi fornitori le condizioni dei piani gratuiti e consumer sul riuso dei dati differiscono da quelle dei piani business/API. Va verificato fornitore per fornitore con fonti datate, perché le condizioni cambiano.
- **Impatto:** esposizione di dati dello studente (inclusi lavori, CV, portfolio) e perdita di lavoro su piattaforme gratuite. Disparità non dichiarata.
- **Standard coinvolti:** AES, AELS.
- **Requisiti:** R05, R06, R10.
- **Gate:** G05, G06, G10.
- **Raccomandazione:**
  1. Aggiungere alla scheda risorsa AES i campi: «uso dei dati per addestramento e opt-out», «conservazione», «localizzazione», «controlli di cancellazione», «backup del lavoro dello studente».
  2. Aggiungere un criterio AES: il percorso gratuito non deve richiedere l'invio di dati personali reali dello studente a un servizio gratuito, e deve indicare come disattivare il riuso dei dati quando possibile.
  3. Per piattaforme senza backup: guida obbligatoria all'esportazione del lavoro.
- **Test:** verifica documentale datata delle condizioni per ogni strumento gratuito primario. Prova di esportazione e ripristino del lavoro su Supabase/Render o equivalenti.
- **Criterio di accettazione:** ogni risorsa gratuita primaria ha i nuovi campi compilati con data. Nessun laboratorio obbligatorio richiede dati personali reali su servizi gratuiti. Esportazione provata.

### E06-08 — Dati personali di terzi nei laboratori e nel portfolio

- **Priorità:** P2.
- **Riferimenti:** ROADMAP L309, L313, L442, L450, L547–548, L897, L939, L1230, L1234, L1250; README L150, L154.
- **Evidenza testuale:**
  - AELS: «nessun dato personale o riservato necessario» (L1230).
  - Diversi laboratori prevedono però persone reali: persona UX con «Intervista e osserva utenti» (L309), test di usabilità con «tre utenti» (L313), «Interviste consensuali e prova osservata» (L442), «Beta con consenso e ticket riproducibili» (L450), «tre feedback» (L897). L3-P29 prevede invece «interviste sintetiche dichiarate» (L939).
  - GA4: «verifica assenza PII», consenso (L547–548).
  - Il portfolio prevede «pubblicazione facoltativa/privacy» e «registro AI» (L1234).
- **Inferenza:** C'è una tensione tra il principio AELS e laboratori che, se svolti come descritti, raccolgono dati di terzi (voci, immagini di sessioni di test, opinioni, email dei beta tester). Il portfolio pubblicabile può veicolare questi dati, oltre a segreti o porzioni di log AI. Dove Creator L1 prevede «1 voce sintetica autorizzata» (L751), c'è anche il tema dei dati vocali.
- **Impatto:** lo studente può trattare dati di terzi senza sapere come. Il portfolio pubblicato può esporre dati personali o segreti.
- **Standard coinvolti:** AELS, AAS (portfolio), ACS (export).
- **Requisiti:** R08, R09, R10.
- **Gate:** G08, G09, G10.
- **Raccomandazione:**
  1. Risolvere la tensione in AELS: «dati personali di terzi non necessari per superare la prova; se lo studente coinvolge persone reali, si applica il kit privacy».
  2. Il kit contiene: modulo di consenso semplice, minimizzazione (nessuna registrazione se non necessaria), anonimizzazione, conservazione breve, cancellazione.
  3. Per ogni laboratorio con persone reali, offrire sempre una variante sintetica equivalente, coerente con L939.
  4. Prima dell'export del portfolio: checklist di redazione (dati personali, segreti, chiavi, URL interni, log AI) e, se implementabile, avviso automatico su pattern di segreti.
- **Test:** revisione documentale dei laboratori interessati. Prova di export del portfolio con dati fittizi «sporchi» (email, chiave fittizia) e verifica dell'avviso o della checklist.
- **Criterio di accettazione:** nessun laboratorio obbligatorio richiede dati di terzi senza variante sintetica. Kit privacy disponibile. Export con controllo di redazione verificato.

### E06-09 — Minori e requisiti d'età dei fornitori non trattati

- **Priorità:** P2.
- **Riferimenti:** ROADMAP L194–195, L1238, L1242, L418; README L89.
- **Evidenza testuale:** i profili d'ingresso partono «da zero» senza requisiti di titolo (L194–195, L1238). L'accesso F1 si basa su «account gratuito» presso fornitori AI e cloud (L1242). Nessun passaggio menziona età minima, minori o consenso dei genitori.
- **Inferenza:** Nulla impedisce l'uso da parte di minorenni. Molti fornitori fissano età minime o richiedono il consenso dei genitori. Laboratori obbligatori basati su questi account potrebbero essere inaccessibili o non consentiti a una parte degli studenti, con effetto anche sulla parità (G05).
- **Ipotesi (verifica giuridica necessaria):** se l'Academy trattasse dati personali come titolare di un servizio della società dell'informazione, potrebbero applicarsi le regole sul consenso dei minori. In Italia la soglia è stata fissata a 14 anni, ma va confermato da un professionista.
- **Impatto:** esclusione non dichiarata, violazione dei termini dei fornitori da parte dello studente, possibili obblighi normativi.
- **Standard coinvolti:** ADS (onboarding), AES (accesso).
- **Requisiti:** R05, R10.
- **Gate:** G05, G10.
- **Raccomandazione:**
  1. Decisione dell'utente sul pubblico destinatario (solo maggiorenni oppure anche minori, con quali condizioni).
  2. Aggiungere alla scheda AES il campo «età minima e condizioni per minori».
  3. Se ammessi minori: verifica giuridica e alternative senza account (F0/F2).
- **Test:** revisione documentale delle età minime dei fornitori primari, con data.
- **Criterio di accettazione:** pubblico dichiarato nella documentazione e nell'onboarding. Ogni laboratorio obbligatorio è accessibile al pubblico dichiarato senza violare i termini dei fornitori.

### E06-10 — Sicurezza dei laboratori sul dispositivo dello studente e supply chain di modelli e strumenti

- **Priorità:** P2.
- **Riferimenti:** ROADMAP L702, L704, L836, L838, L847, L1116, L1218, L1242.
- **Evidenza testuale:**
  - I laboratori prevedono l'installazione e l'esecuzione locale di modelli scaricati: FLUX su Hugging Face (L702), Wan 2.1 (L704), Ollama (L839).
  - Prevedono anche n8n self-hosted con Docker (L836, L1116), con l'«AI starter kit» indicato come «solo test, non produzione» (L1116).
  - Server MCP locali: «stdio non sandbox, isolamento OS/container e scope minimo» (L838).
  - Agenti con strumenti reali (L1218).
  - Profili hardware H1–H3 su computer personali (L1242).
- **Inferenza:** Lo studente esegue sul **proprio** computer software e modelli di terze parti, oltre ad agenti con accesso al filesystem, spesso con l'account con cui conserva dati personali. L'isolamento è raccomandato nei testi d'audit ma non è un requisito di setup AELS. Il download di pesi e nodi della community è un vettore noto di supply chain (formati serializzati non sicuri, pacchetti malevoli, typosquatting).
- **Impatto:** compromissione del dispositivo dello studente, esfiltrazione di file personali da agenti mal configurati o da documenti ostili, esposizione in rete di servizi locali (n8n, Ollama).
- **Standard coinvolti:** AELS (setup), AES (licenze, hardware), AAS (errori critici).
- **Requisiti:** R02, R08, R10.
- **Gate:** G02, G07, G10.
- **Raccomandazione:** inserire nell'AELS un **setup sicuro di laboratorio** obbligatorio per L2/L3:
  1. profilo utente o cartella di lavoro dedicata, senza dati personali;
  2. container o VM quando l'hardware lo consente, oppure in alternativa cartella isolata e permessi minimi;
  3. servizi locali in ascolto solo su localhost;
  4. download da fonti ufficiali con verifica di hash e versione fissata;
  5. preferenza per formati di pesi non eseguibili (es. safetensors);
  6. divieto di nodi e plug-in della community non verificati nei laboratori obbligatori;
  7. pulizia finale.
- **Test:**
  - per ogni laboratorio con esecuzione locale: verifica che i servizi non siano raggiungibili da un'altra macchina della rete;
  - agente MCP con tentativo d'accesso fuori dalla cartella (già previsto in L3-P09, L919): deve fallire;
  - verifica dell'hash del modello scaricato.
- **Criterio di accettazione:** setup sicuro documentato e collegato a ogni laboratorio locale. Prove negative superate in 4D sui profili H1/H2.

### E06-11 — Supply chain e risorse esterne dell'Academy

- **Priorità:** P2.
- **Riferimenti:** ROADMAP L696, L700, L772, L836, L839, L841, L959, L1023, L1116, L1242; README L50.
- **Evidenza testuale:**
  - Fonti con reindirizzamenti, errori o indisponibilità: LearnFree reindirizzato (L696), Inkscape 403 (L700), OpenStax 404 (L959), DuckDB redirect (L1023), URL OpenAI reindirizzato (L839), corsi IBM/Make reindirizzati (L959, L1116), piattaforma Evals in chiusura il 30/11/2026 (L841).
  - Licenze con vincoli: CC BY-NC-SA (L772), n8n Sustainable Use License non OSI (L836).
  - La rivalidazione periodica è proposta senza automazione: «nessuna automazione attivata» (L1242).
  - README L50: «Gli altri link restano da verificare».
  - I documenti non dicono nulla sulle dipendenze dell'app stessa (librerie, CDN, font, integrità delle risorse, Content Security Policy).
- **Inferenza:** Molti link esterni incorporati nell'app cambiano destinazione nel tempo. Un dominio scaduto o un reindirizzamento malevolo esporrebbe gli studenti a contenuti non attesi (phishing, malware). Senza inventario delle dipendenze dell'app, il rischio di supply chain della PWA stessa non è valutabile.
- **Impatto:** rischio per gli studenti tramite link compromessi, obsolescenza silenziosa, rischio legale da licenze NC in uso professionale.
- **Standard coinvolti:** AES (scheda risorsa, rivalidazione), AELS.
- **Requisiti:** R08, R10.
- **Gate:** G08, G10.
- **Raccomandazione:**
  1. Inventario delle dipendenze runtime dell'app, con versioni e origine.
  2. Politica: nessuna risorsa da CDN senza integrità verificata, CSP restrittiva da valutare.
  3. Controllo periodico dei link: almeno manuale, con data e registro, prima di ogni rilascio; segnalare reindirizzamenti verso domini diversi da quello registrato.
  4. Avviso nell'app all'uscita verso siti esterni.
- **Test:** scansione dei link del curriculum finale (stato HTTP, dominio finale = dominio atteso). Revisione dell'inventario delle dipendenze e della CSP sul codice.
- **Criterio di accettazione:** zero link con dominio finale non atteso al momento del rilascio. Inventario dipendenze completo. Decisione su CSP registrata.

### E06-12 — Autenticità del registro decisionale e privilegi del coordinatore AI

- **Priorità:** P2.
- **Riferimenti:** ROADMAP L18–20, L67–69, L141, L143, L954, L1254, L1263, L1322; README L174, L183.
- **Evidenza testuale:**
  - Le approvazioni dell'utente («Approvazione utente…», «Approvazione integrale utente») sono trascritte nella ROADMAP dal coordinatore AI. L'accesso in scrittura avviene «tramite connettore GitHub» (L141).
  - La Fase 3I deriva da immagini con lacune: «mancano IMG_9493–9499» (L1263), poi «sei immagini successivamente trasmesse (una compensativa)», «IMG_9497 originale non verificato» (L1322).
  - La protezione di main e RC1 è espressa come vincolo procedurale («non modificare», L16–18) e controllata a posteriori tramite SHA (L143). Non è documentata una protezione tecnica dei branch.
  - Regola 3: il coordinatore propone autonomamente revisioni (L1254).
  - Regola 2: pulsante di prosecuzione (L954).
- **Inferenza:**
  - (a) Nessun meccanismo distingue tecnicamente un'approvazione reale dell'utente dalla sua trascrizione. AVS richiede una «decisione motivata/versionata» per chiudere i gate (L1258), quindi l'autenticità delle approvazioni è un requisito di integrità.
  - (b) Il coordinatore AI ha privilegi di scrittura ampi sul repository. I controlli sono procedurali e autodichiarati.
  - (c) Un pulsante di prosecuzione cliccato per abitudine può essere interpretato come assenso («approval fatigue»), anche se L954 lo esclude testualmente.
  - (d) Sette immagini mancanti (9493–9499) e sei ricevute: il registro R01–R12 potrebbe essere incompleto senza che lo si possa dimostrare (E06-15).
- **Impatto:** possibilità di chiusure di gate o approvazioni non autentiche, anche involontarie. Modifiche ai branch protetti rilevate solo a posteriori.
- **Standard coinvolti:** AVS, AMVP.
- **Requisiti:** R11, R12.
- **Gate:** G10, G11, G12.
- **Raccomandazione:**
  1. Attivare su GitHub regole di protezione per main e RC1 (nessun push diretto, nessuna cancellazione o force-push), con amministrazione riservata all'utente.
  2. Far registrare le approvazioni di gate e fase **dall'utente stesso**, ad esempio con approvazione di una pull request o commenti dall'account dell'utente. Il coordinatore AI le cita, non le crea.
  3. Concedere al connettore del coordinatore il minimo privilegio: solo il branch di sviluppo, senza amministrazione.
  4. Distinguere testualmente «pulsante di prosecuzione» da «approvazione»: l'approvazione richiede una formula esplicita.
  5. Archiviare le immagini sorgente delle decisioni nel repository, o loro hash, per verificabilità.
- **Test:** tentativo di push diretto su main con le credenziali del coordinatore (deve fallire). Verifica che ogni approvazione nella ROADMAP successiva alla modifica sia collegata a un evento dell'account utente.
- **Criterio di accettazione:** protezione dei branch attiva e provata. Approvazioni collegate a eventi verificabili. Hash delle immagini sorgente registrati.

### E06-13 — Gestione incidenti, segnalazione vulnerabilità e rollback dell'app non definiti

- **Priorità:** P2.
- **Riferimenti:** ROADMAP L12, L43–53, L1258; README L15.
- **Evidenza testuale:** la checklist di rilascio contiene «Aggiornamento automatico» (L52) ma nessuna voce su incidenti, revoca di una versione difettosa, comunicazione agli utenti o canale di segnalazione. Il curriculum insegna rollback e release candidate (L342, L440, L937), ma l'Academy non definisce questi processi per sé.
- **Inferenza:** Con una PWA in produzione e aggiornamento automatico, una versione difettosa (es. migrazione errata) può propagarsi ai dispositivi senza procedura di arresto. Manca anche un canale per segnalazioni di sicurezza.
- **Impatto:** tempi di reazione lunghi, perdita di dati diffusa, nessuna tracciabilità degli incidenti.
- **Standard coinvolti:** AVS.
- **Requisiti:** R10, R11.
- **Gate:** G10, G11.
- **Raccomandazione:**
  1. Piano incidenti minimo: classificazione, responsabile (l'utente), passi di contenimento, rollback del service worker e della versione, comunicazione, registro.
  2. File `SECURITY.md` con canale di segnalazione.
  3. Interruttore di emergenza per l'aggiornamento automatico, se tecnicamente possibile, da verificare.
- **Test:** esercitazione documentata di rollback da 6.6 a 6.5.1 su dispositivo reale con dati, in ambiente di prova.
- **Criterio di accettazione:** piano approvato. Esercitazione eseguita con evidenze. Dati preservati dopo il rollback.

### E06-14 — Requisiti normativi da qualificare giuridicamente

- **Priorità:** P2. Rischio documentale, **non conclusione giuridica**.
- **Riferimenti:** ROADMAP L556, L843, L1234, L1238, L1250; README L158, L170.
- **Evidenza testuale:** l'unico richiamo esplicito alla normativa è la consultazione di materiali EDPB, con «nessuna attestazione legale/compliance» (L843). Per GA4 si richiede di verificare consenso e regole applicabili (L556). AAS prevede valutazione «AI assistita» (L1234). ADS produce una «raccomandazione» del ramo (L1238).
- **Inferenza:** I documenti non definiscono il ruolo dell'Academy rispetto alla protezione dei dati. Se tratta dati degli studenti o solo il dispositivo dello studente li tratta, gli obblighi cambiano molto.
- **Ipotesi da sottoporre a professionista (non verificate in questa revisione):**
  - (a) **GDPR:** se l'Academy o il suo gestore trattano dati personali degli studenti (anche solo tramite analytics, sincronizzazione o raccolta di feedback), servono informativa, base giuridica, eventuale valutazione d'impatto se ci sono profilazioni valutative, e gestione dei diritti. Con architettura solo locale gli obblighi del gestore potrebbero ridursi molto.
  - (b) **AI Act UE:** i sistemi AI usati nell'istruzione e nella formazione professionale per valutare i risultati dell'apprendimento o per determinare l'accesso o l'assegnazione a percorsi rientrano, secondo le mie conoscenze, tra i casi ad alto rischio dell'Allegato III. Se l'Academy usasse un sistema AI (non una regola deterministica) per assegnare punteggi AAS, esoneri ADS o il ramo, potrebbe rientrarvi. Date di applicazione ed eventuali modifiche normative successive a giugno 2026 vanno verificate.
  - (c) **ePrivacy/consenso cookie** nei laboratori GA4 (pubblicazione di proprietà di test con visitatori reali).
  - (d) **Diritto d'autore e licenze** di asset e output AI (fuori dal perimetro E06; lo segnalo per completezza).
- **Impatto:** possibili obblighi non individuati, specie se in Fase 5 si introducono valutazione AI o servizi remoti.
- **Standard coinvolti:** AAS, ADS, ACS, AVS.
- **Requisiti:** R10.
- **Gate:** G10.
- **Raccomandazione:**
  1. Vincolo progettuale: in Fase 5 punteggi, esoneri e assegnazione del ramo restano **deterministici e spiegabili**, senza AI che decida, salvo decisione dell'utente e verifica giuridica.
  2. Prima del rilascio: breve parere da un professionista qualificato sull'architettura effettiva.
  3. Nessuna affermazione di conformità nei testi pubblici (E06-06).
- **Test:** verifica documentale che nessun requisito di Fase 5 deleghi a un modello AI decisioni di valutazione o accesso. Revisione esterna.
- **Criterio di accettazione:** ruolo dell'Academy rispetto ai dati dichiarato. Decisione sull'uso dell'AI nella valutazione registrata. Parere esterno acquisito prima del rilascio, oppure rilascio senza trattamento di dati da parte del gestore, documentato.

### E06-15 — Tracciabilità R01–R12 ↔ standard ↔ gate implicita e incompleta (mandato comune)

- **Priorità:** P2.
- **Riferimenti:** ROADMAP L1258, L1263, L1265–1267, L1273–1299, L1322; README L183.
- **Evidenza testuale:**
  - R01–R12 sono etichette di una riga con standard associato (L1275–1288). Sono definiti «proposta organizzativa» (L1290).
  - G01–G12 sono elencati separatamente (L1292).
  - La corrispondenza R_n ↔ G_n non è dichiarata, anche se i titoli coincidono quasi uno a uno.
  - README L183: «registro R01–R12 recuperato 12/12». ROADMAP L1322: «Non si attesta una trascrizione integrale delle parti coperte o fuori inquadratura».
  - Le coerenze tra standard (L1265) e C01–C08 (L1266) non hanno identificativi collegati a R e G.
- **Inferenza:**
  - (a) La tracciabilità R → G è plausibile ma solo deducibile dai titoli.
  - (b) I requisiti non hanno criteri misurabili. Non soddisfano la condizione AVS di «requisito e criterio predefiniti».
  - (c) Per la sicurezza, R10 → solo AVS è incompleto. Sicurezza e privacy toccano anche AELS (dati nei laboratori), AAS (errori critici di sicurezza, integrità), ADS (dati diagnostici), AES (privacy dei fornitori, licenze), ACS (credenziali, export).
  - (d) «12/12 recuperato» nel README rischia di essere letto come recupero integrale, cosa che la ROADMAP esclude.
  - (e) Le relazioni molti-a-molti (R06 → AES+AAS, R12 → AVS+AMVP) non hanno un gate secondario esplicito.
- **Impatto:** difficile verificare la copertura. Rischio di gate chiusi senza aver coperto tutti gli standard pertinenti.
- **Standard coinvolti:** AVS, AMVP e tutti gli altri.
- **Requisiti:** R01–R12.
- **Gate:** G01–G12.
- **Raccomandazione:**
  1. Aggiungere una matrice esplicita R × standard × gate × anomalie (con gli ID E0x-nn di CR-001) × prove.
  2. Estendere R10 a «AVS (processo) + AELS, AAS, ADS, AES, ACS (requisiti)».
  3. Scomporre ogni R in sotto-requisiti con criterio misurabile (per R10, dalla baseline E06-01).
  4. Correggere il README: «etichette R01–R12 recuperate 12/12; trascrizione integrale non attestata».
- **Test:** revisione documentale della matrice. Ogni anomalia CR-001 è collegata a almeno un R e un G. Ogni R ha almeno un criterio e una prova.
- **Criterio di accettazione:** matrice completa e approvata. Nessun R senza criterio. Nessuna anomalia senza collegamento.

### E06-16 — Incoerenze documentali di stato e di vocabolario

- **Priorità:** P3.
- **Riferimenti:** ROADMAP L3, L26, L55–60, L1258, L1296–1297; README L3, L183.
- **Evidenza testuale:**
  - ROADMAP: «Aggiornato: 25 novembre 2026» (L3) e «Stato operativo corrente — 25 novembre 2026» (L26), mentre il contenuto arriva al 26/11 (Fasi 3B–3I).
  - La sezione «Prossimo intervento» in testa alla ROADMAP indica ancora «Fase 2C, completare audit individuale Creator 1–6» (L60).
  - README «Stato operativo corrente — 25 novembre 2026» (L3).
  - Il sottogate G12-E ha stato «Non verificata» (L1297), mentre i gate sono descritti come aperti/chiusi e gli stati AVS sono V0–V6 più bloccata/da rivalidare/in correzione (L1258). «Non verificata» non è tra questi.
- **Inferenza:** La procedura permanente richiede di aggiornare i riepiloghi correnti (L67). Le sezioni di testa non sono allineate. Dopo un trasferimento di conversazione (Regola 1), una lettura parziale potrebbe portare a riprendere una fase superata.
- **Impatto:** rischio operativo di continuità, ambiguità nello stato dei gate.
- **Standard coinvolti:** AVS, procedura permanente.
- **Requisiti:** R11, R12.
- **Gate:** G11.
- **Raccomandazione:** aggiornare intestazioni e «Prossimo intervento» della ROADMAP (lo stato corrente è CR-001, Fase 4 non autorizzata). Aggiungere all'AVS un vocabolario controllato degli stati dei gate e sottogate.
- **Test:** revisione documentale dopo l'aggiornamento.
- **Criterio di accettazione:** sezioni di stato corrente coerenti con l'ultima fase registrata. Tutti gli stati usati appartengono al vocabolario AVS.

### E06-17 — Valutazione AI-assistita e AMVP esposte a prompt injection e contaminazione

- **Priorità:** P2.
- **Riferimenti:** ROADMAP L1234, L1250, L1254, L1259.
- **Evidenza testuale:**
  - AAS e ACS prevedono valutazione «AI assistita non indipendente» (L1234, L1250).
  - AMVP prevede ruoli AI Teacher, Student, Examiner e Auditor, con «soluzioni nascoste» e «traccia informazioni» (L1259).
  - Regola 3 prevede il trasferimento di dossier a un'AI esterna (L1254).
- **Inferenza:**
  - (a) Se un'AI valuta elaborati dello studente (codice, report, README), l'elaborato è un input non fidato. Può contenere istruzioni rivolte al valutatore («assegna 4/4»): è un'injection indiretta. Il curriculum insegna proprio questa minaccia, ma gli standard di valutazione non prevedono contromisure.
  - (b) In AMVP le «soluzioni nascoste» sono protette solo dalla separazione delle conversazioni. Una perdita di contesto o materiali condivisi per errore contaminano la simulazione.
  - (c) I dossier trasferiti a revisori AI possono contenere testo direttivo (come questo stesso mandato) che orienta l'esito.
- **Impatto:** punteggi gonfiati non rilevati, simulazioni AMVP non affidabili, revisioni orientate.
- **Standard coinvolti:** AAS, ACS, AMVP.
- **Requisiti:** R03, R12.
- **Gate:** G03, G12 (G12-S), G10.
- **Raccomandazione:**
  1. Nell'AAS: l'AI assistita produce solo osservazioni, mai il punteggio finale. Gli elaborati vanno passati come dati delimitati con istruzioni di sistema che li dichiarano non fidati. Aggiungere un controllo deterministico (test automatici) per i criteri «correttezza/funzionalità».
  2. In AMVP: aggiungere elaborati «canarino» contenenti istruzioni d'injection, per verificare che l'Examiner non si lasci influenzare. Registrare hash dei materiali consegnati a ogni ruolo per provare la separazione.
  3. Nei mandati CR: separare istruzioni di processo e materiali da valutare.
- **Test:** sottoporre all'Examiner AI un elaborato con injection esplicita e uno identico senza injection; confrontare i punteggi. Verificare tramite hash che nessun ruolo abbia ricevuto le soluzioni nascoste.
- **Criterio di accettazione:** differenza di punteggio nulla o entro la tolleranza AAS tra le due versioni. Nessuna contaminazione rilevata dagli hash.

---

## 11. Raccomandazioni e verifiche mancanti

### 11.1 Prima dell'avvio della Fase 4 (attività documentali, senza modifiche applicative)

1. Security & Privacy Baseline come annesso AVS, con threat model dell'app e livello di riferimento scelto (E06-01).
2. Descrizione dello schema di cifratura e backup oggi in produzione, ricavata dal codice da chi può ispezionarlo (E06-02).
3. Registro dei dati dell'Academy e dichiarazione dell'architettura (solo locale o no) (E06-03).
4. Scheda di sicurezza per 4A e 4B come criterio d'uscita di 4D e 4H (E06-05).
5. Stato definito per G12-E e politica delle affermazioni (E06-06).
6. Matrice R × standard × gate × anomalie × prove; R10 esteso a tutti gli standard pertinenti; correzione della formula «12/12» nel README (E06-15).
7. Protezione tecnica dei branch e registrazione delle approvazioni dall'account dell'utente (E06-12).
8. Aggiornamento delle sezioni di stato corrente e del vocabolario dei gate (E06-16).

### 11.2 Durante la Fase 4 (collaudi in 4D, simulazioni in 4E)

- Collaudi E06-02 su Safari/iPhone reale e su un secondo browser.
- Checklist di sicurezza del prototipo (E06-05), prove di injection e di superamento quota.
- Prova di setup sicuro su H1/H2 (E06-10).
- Prova AMVP con elaborati canarino (E06-17).
- Verifica datata delle condizioni dei fornitori gratuiti, inclusi dati ed età (E06-07, E06-09).

### 11.3 Prima di un rilascio

- Piano incidenti, `SECURITY.md` ed esercitazione di rollback (E06-13).
- Scansione dei link e inventario delle dipendenze, decisione su CSP (E06-11).
- Revisione dei testi pubblici contro la politica delle affermazioni (E06-06).
- Parere giuridico esterno sull'architettura effettiva (E06-14).
- Correzione della correlazione di posizione dei quiz e dichiarazione della natura delle credenziali (E06-04).

### 11.4 Distinzione delle forme di verifica

| Forma di verifica | Stato per l'ambito E06 | Cosa ha prodotto o cosa manca |
|---|---|---|
| **Revisione documentale** | **Eseguita** (questo rapporto) | 17 anomalie su lacune di specifica, tracciabilità e coerenza. Non prova la presenza o l'assenza di vulnerabilità. |
| **Simulazione AI (AMVP)** | Non eseguita | Nessuno studente virtuale. Questo rapporto è una revisione AI, non una simulazione didattica. |
| **Collaudo tecnico reale** | **Non eseguito** | Nessuna prova di cifratura, backup, ripristino, migrazione, PWA, storage, link, autorizzazioni o injection. Tutti i test della sezione 10 sono da eseguire. |
| **Efficacia empirica umana** | Non verificata (G12-E) | Nessuno studente reale. |
| **Verifiche esterne** | Non eseguite | Mancano: parere giuridico (GDPR, AI Act, minori), eventuale test di sicurezza indipendente umano, verifica datata delle condizioni dei fornitori. |

### 11.5 Verifiche che E06 non ha potuto svolgere

- Ispezione del codice di `index.html`, `sw.js` e dei curriculum JSON (escluso dal mandato).
- Verifica della posizione delle chiavi delle risposte, della cifratura e del contenuto del backup.
- Verifica delle condizioni attuali dei fornitori (dati, età, quote).
- Verifica normativa aggiornata.
- Contenuto delle immagini sorgente della Fase 3I.

## 12. Esito complessivo

**Esito: PARZIALE.**

**Motivazione**
- **Elementi conformi:**
  - i documenti non contengono affermazioni di sicurezza, privacy o conformità presentate come verificate;
  - tutti i gate restano correttamente aperti;
  - la distinzione tra controlli statici, simulazioni e collaudi è rigorosa;
  - i contenuti didattici di sicurezza (injection, segreti, autorizzazioni, idempotenza, approvazioni, sandbox) sono maturi e dotati di prove negative;
  - la minimizzazione è dichiarata come principio in ADS, ACS e AELS;
  - il protocollo di controllo degli SHA protegge l'integrità del repository a posteriori.
- **Elementi non conformi o incompleti** rispetto ai criteri dello stesso AVS («requisito e criterio predefiniti»):
  - R10/G10 non ha baseline né criteri di accettazione per l'app (E06-01);
  - la cifratura e il backup in produzione non sono specificati né collaudati (E06-02);
  - manca l'inventario dei dati (E06-03);
  - l'integrità di valutazioni e credenziali non è progettata (E06-04);
  - i prototipi 4A/4B non hanno criteri di sicurezza d'uscita (E06-05);
  - c'è una contraddizione strutturale su G12-E (E06-06).
- **Elementi non verificabili:** la sicurezza effettiva dell'applicazione. Questa revisione non ha accesso al codice né all'esecuzione, e il rapporto non fa affermazioni in merito.

**Condizioni dal punto di vista E06**
- La Fase 4 **non dovrebbe essere avviata** finché le anomalie P1 E06-01, E06-05 ed E06-06 non sono risolte a livello documentale.
- E06-02, E06-03 ed E06-04 vanno risolte prima di accettare 4C, 4D e la Fase 5.
- Le anomalie P2 richiedono correzione o decisione motivata dell'utente.

Questa è una raccomandazione al coordinatore e all'utente. Non è un'autorizzazione né un diniego: decide l'utente.

Nessun gate chiuso. Nessuno standard modificato. Nessuna modifica a GitHub. Nessun rilascio autorizzato. Fase 4 non avviata.

---
*Fine del rapporto E06-original-report.md, CR-001. Revisione AI esterna simulata, non audit umano indipendente.*
