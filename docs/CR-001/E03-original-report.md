# CR-001 — E03 — Applied AI Review Report

## 1. Modello AI, versione e data
- **Modello:** Claude Opus 5.5 (Anthropic), identificativo `claude-opus-5-5`.
- **Data della revisione:** 26 novembre 2026, ore 17 circa (Europe/Rome).
- **Conoscenze di addestramento:** affidabili fino a giugno 2026. Non ho consultato il web. Tutto quello che dico su servizi, quote e prezzi viene solo dai due documenti; non l'ho verificato.

## 2. Ruolo specialistico
Revisore AI esterno simulato per la prospettiva **E03 — Applied AI** prevista da AMVP. Non sono un esperto umano e questo rapporto non vale come audit umano indipendente (vincolo C06).

## 3. Capacità e limiti
**Cosa posso fare:**
- leggere e confrontare per intero testi lunghi;
- ricalcolare valori aritmetici;
- trovare incongruenze tra sezioni;
- ragionare su architetture AI: agenti, RAG, tool calling, valutazioni (eval), quote.

**Limiti:**
- Non ho eseguito alcun laboratorio, modello, API, workflow né alcuna simulazione AMVP.
- Non ho visto i curriculum JSON, il codice dell'app, le immagini IMG_9493–9499 né le pagine esterne citate.
- Non posso confermare quote, prezzi, licenze o condizioni di accesso attuali.
- Le mie valutazioni tecniche su modelli piccoli, quote o affidabilità del tool calling sono inferenze da competenza generale, non misure.

## 4. Bias e potenziali conflitti
- **Conflitto diretto.** Il curriculum usa risorse e prodotti Anthropic (Claude free, Anthropic AI Fluency, documentazione Claude e pricing Claude) e io sono un modello Anthropic. Ho cercato di non dare a queste risorse un peso diverso dalle alternative, ma non posso garantirlo.
- **Bias strutturale.** Questo mandato è stato scritto dal coordinatore del progetto, ChatGPT, che ha anche prodotto i materiali revisionati. Ambito e domande sono quindi definiti da chi produce il lavoro (vedi E03-11).
- **Bias possibili:** tendenza a giudicare la qualità dalla completezza formale del testo; preferenza per soluzioni ingegneristiche "rigorose" che potrebbero aumentare il carico didattico.

## 5. Indipendenza procedurale
- Non ho consultato altri rapporti CR-001, né analisi del coordinatore, né documenti successivi al checkpoint.
- Non ho conclusioni da altre conversazioni di revisione.
- Ho letto il branch solo al commit indicato. Non ho guardato lo stato attuale del branch.

## 6. Ambito, materiali e checkpoint
- **Repository:** itopo-ai/AI-Creator-Academy.
- **Checkpoint:** `f9d98c2bbd4d3622b9ccb5eeeb5c1811a2c4d401`, commit del 2026-11-26 12:52:17 +0100, messaggio "docs: align phase 3I status with recovered evidence".
- **Materiali:** README.md e ROADMAP.md, per intero.
- **Natura della revisione:** documentale. Non certifica prototipi né runtime. Non ho modificato file, chiuso gate o avviato la Fase 4.

## 7. Esito della verifica preliminare

| Verifica | Esito |
|---|---|
| Accesso al commit fissato | Eseguita: `git fetch` del commit esatto tramite lettura anonima, FETCH_HEAD = f9d98c2… |
| Blob SHA nel tree | Eseguita: README `abca6f1c…`, ROADMAP `af9888bc…`, coincidenti |
| SHA ricalcolato sui file estratti (`git hash-object`) | Eseguita: coincidente per entrambi |
| Lunghezza in caratteri | Eseguita: README 54.465, ROADMAP 287.684. Coincidenza esatta |
| Lettura integrale | Eseguita: README 183 righe e ROADMAP 1.322 righe, spezzate in segmenti di 1.500 caratteri (196 + 1.351) per evitare troncamenti, lette tutte in sequenza |
| Contenuto non sostituito da anteprime | Eseguita. Un tentativo iniziale con un recuperatore web ha restituito solo una sintesi: l'ho scartato e non l'ho usato |
| Verifiche non possibili | Immagini sorgente, JSON, link esterni, runtime |

**Esito: accesso integrale confermato.** Ho proseguito con la revisione.

## 8. Metodo di revisione
1. Lettura integrale di entrambi i documenti, con annotazioni per sezione.
2. Estrazione dei requisiti E03 (progressione AI, agenti, RAG, tool calling, riproducibilità, quote, alternative gratuite, AMVP, contaminazione) e confronto incrociato con AELS, AAS, ADS, AES, ALWS, ACS, AVS, AMVP e il registro R/G.
3. Ricalcolo dei valori numerici rilevanti: ALWS, conteggi 420/156/66/90, AMVP 108/324, calcoli nei quiz AI. **Tutti i valori ricontrollati sono corretti.**
4. Ricerche testuali mirate, per esempio di termini su versione del modello, parametri, seed, termini d'uso dei dati, rate limit e LLM-as-judge.
5. Ogni osservazione separa **[E] evidenza testuale**, **[I] inferenza** e **[H] ipotesi**.

## 9. Punti di forza
- **Prudenza epistemica costante [E].** I documenti distinguono sempre dichiarato, documentato, verificato e collaudato; i controlli statici sono separati dal runtime e la simulazione dall'efficacia umana (AVS, AMVP, C07).
- **Laboratori L3 Creator ben progettati per l'Applied AI [E]:**
  - agenti con budget di passi, arresto senza progresso e approvazione legata al payload, con nuova approvazione se il piano cambia (cr-w14s2–s3);
  - MCP con allowlist, sandbox e prova di scrittura negata, consapevoli che stdio non è una sandbox (cr-w15);
  - prompt injection da documento recuperato, con blocco dell'egress (cr-w15s4);
  - RAG con citazioni a livello di singola affermazione, astensione, fonti obsolete, recall@k e confronto con baseline lessicale (cr-w17);
  - valutazione con holdout separato dal tuning, p50/p95, regressioni e blocco del rilascio per errore critico (cr-w18).
- **Eval indipendenti dal fornitore [E].** La chiusura prevista di OpenAI Evals (30/11/2026) è registrata, con indicazione di usare un harness locale.
- **Quote ed economia [E].** "Un abbonamento chat non implica crediti API". I trial non sono alternative stabili. I mock servono solo per i test di guasto, non come prova di inferenza. Endpoint Ollama mai esposti senza autenticazione.
- **AMVP consapevole dei propri limiti [E].** "Impossibile cancellare conoscenze modello"; "tempo risposta AI non tempo umano"; i 108 scenari "non osservazioni indipendenti".
- **Coerenza aritmetica [E+verifica].** ALWS 338,5 / 420,25 / 758,75 h, media 108,39 min, +187,4%; scenari 414,5 / 500,25 / 914,75 h; riserva 476,675 / 575,2875 h; 420 = 264 + 156 (66 + 90). Tutti corretti.

## 10. Osservazioni e anomalie

Non ho trovato condizioni **P0**: siamo in fase documentale e nessun rilascio è in corso.

### E03-01 — P1 — Progressione Creator: integrazione AI richiesta in L2 ma insegnata in L3
- **Sezioni:** AAS 3C (capstone L2), ACS 3G (badge L2 "AI Integration"), AVS 3H e piano 4A (prototipo "AI-Powered Data Application"), matrici 2E L2 e L3.
- **Evidenza [E]:**
  - Il capstone L2 richiede "codice, dati, responsive, AI, test". Il 4A richiede "integrazione AI reale".
  - La matrice L2 (cr-w07–w12, L2-P01–P20) non contiene sessioni su API di modelli, output strutturati, streaming, budget o eval.
  - Questi temi compaiono solo in L3: cr-w16 (API), cr-w17 (RAG), cr-w18 (eval), L3-P10–P18.
- **Impatto [I]:** lo studente L2 dovrebbe integrare l'AI prima di averla studiata. Il prototipo 4A, se rappresenta L2, metterebbe alla prova competenze non insegnate (in contrasto con la regola di coerenza AELS/AAS "prove sulle competenze insegnate").
- **Raccomandazione:** dichiarare a quale livello corrisponde 4A. In alternativa, anticipare in L2 un nucleo minimo (chiamata server-side, output strutturato con validazione, gestione errori e budget) oppure togliere l'"AI" obbligatoria dal capstone e dal badge L2. Serve una decisione dell'utente.
- **Test proposto:** matrice di tracciabilità competenza → prerequisito → sessione per ogni requisito del capstone L2 e del 4A.
- **Criterio di accettazione:** 100% dei requisiti obbligatori di capstone, badge e 4A coperti da sessioni di livello uguale o precedente.

### E03-02 — P1 — Parità gratuita per agenti, tool calling, RAG e API dipendente da hardware e quote non verificati
- **Sezioni:** 2E Creator L3 (codici I, D, A), 2E Business L3 (parità candidata), AES 3E (H0–H3), C08.
- **Evidenza [E]:**
  - Il percorso gratuito candidato usa "Ollama locale CPU" con Qwen2.5 1.5B, con la nota "non RAM minima né garanzia tool use/qualità", oppure Workers AI Free con "alcuni modelli richiedono piano pagato".
  - Per Hugging Face "nessun credito Free".
  - In Business L3, il "modello locale Ollama compatibile per tool calling reale" e la "disponibilità alternativa per chi ha solo iPhone" sono ancora da collaudare.
- **Impatto [I]:** le competenze obbligatorie (agenti, MCP, RAG, eval, cr-w14–w18, b42–b44, BL3-P23–P28) potrebbero di fatto richiedere un computer H1/H2 che lo studente non ha. Questo contrasterebbe con "nessun acquisto obbligatorio" e Mobile First. **[H]** Un modello quantizzato da 1,5B potrebbe non reggere un tool calling affidabile: lo studente fallirebbe per colpa dello strumento, non per mancanza di competenza, e la parità AAS sarebbe falsata.
- **Raccomandazione:**
  - Definire un **profilo minimo di capacità del modello** per ogni laboratorio: aderenza allo schema dei tool, astensione, italiano.
  - Classificare ogni laboratorio AI per H0–H3.
  - Dichiarare in anticipo quali competenze obbligatorie richiedono un computer.
  - Se per H0 non esiste un percorso gratuito reale, applicare la regola già prevista: gap bloccante o riprogettazione approvata.
- **Test proposto (4D):** suite fissa di 30 casi di tool calling (10 normali, 10 limite, 10 avversi) e 20 interrogazioni RAG, eseguita su ogni candidato gratuito (Ollama 1.5B/7B su H1 e H2, Workers AI Free) e su un candidato premium; 3 ripetizioni; misurare successo, RAM di picco, latenza e quota consumata.
- **Criterio di accettazione:** per ogni laboratorio obbligatorio esiste almeno una configurazione gratuita su hardware dichiarato che supera le soglie AAS fissate prima del test; differenza AAS rispetto al premium ≤ 10 punti, oppure scostamento analizzato secondo AES; zero errori critici.

### E03-03 — P1 — G12-S senza criteri di chiusura; rapporto tra G12, G12-E e rilascio indefinito
- **Sezioni:** 3I (tabella sottogate), AVS 3H (regola di chiusura), AMVP.
- **Evidenza [E]:**
  - G12-S è "Aperto", G12-E è "Non verificata": due vocabolari di stato diversi.
  - AVS: "qualsiasi violazione obbligatoria blocca", "nessuna compensazione".
  - AMVP: "nessun test umano esterno disponibile".
  - 3I: "Prima di un eventuale rilascio stabilire quali affermazioni… sostenibili in assenza di G12-E".
- **Impatto [I]:** se G12 si chiude solo con G12-E, il gate non può chiudersi mai e il rilascio resta bloccato. Se invece si rilascia senza G12-E, serve una regola esplicita, altrimenti si crea una deroga implicita ad AVS. Per G12-S non sono definiti soglie, campione, ruoli né contro-prove.
- **Raccomandazione (senza deroghe ad AVS):**
  - Definire G12 come **composto**. G12-S si chiude con criteri predefiniti (vedi E03-04). G12-E resta "non verificato" come **limitazione dichiarata vincolante**, che non chiude G12 ma restringe le affermazioni ammesse (vedi §11.1).
  - Far decidere esplicitamente all'utente se un rilascio con G12 "parzialmente aperto" sia ammissibile, e con quale etichetta (per esempio "sperimentale / non validato empiricamente").
- **Test proposto:** revisione documentale della definizione di G12 rispetto alla regola di chiusura AVS.
- **Criterio di accettazione:** per G12-S e G12-E sono scritti requisito, criterio, prova, stato ammesso e conseguenza sul rilascio, con un unico vocabolario di stato.

### E03-04 — P1 — Contaminazione delle simulazioni AMVP: mitigazioni dichiarate ma non rese operative
- **Sezione:** AMVP 3H.
- **Evidenza [E]:** "escludere contaminazioni da conoscenze pregresse", "conversazioni separate", "soluzioni nascoste", ma anche "Impossibile cancellare conoscenze modello". Non sono specificati né la famiglia di modelli dello Student rispetto all'Examiner né controlli di contaminazione misurabili.
- **Impatto [I]:**
  - Uno studente AI sa già quasi tutto il contenuto L1–L3. I punteggi misurano la capacità del modello, non l'efficacia dei materiali.
  - Se Teacher, Student ed Examiner sono della stessa famiglia del produttore (ChatGPT), è plausibile una preferenza per il proprio stile [H].
  - Un profilo "principiante" interpretato da un LLM non è validato come rappresentativo.
- **Raccomandazione:**
  - **Pre-test di contaminazione:** lo Student risponde alle prove finali *prima* di studiare; se supera già la soglia, la sessione non dà alcuna evidenza su G12-S.
  - Usare almeno due famiglie di modelli diverse per Student ed Examiner, e un Examiner cieco rispetto a versione e profilo.
  - Aggiungere marcatori unici (canary) nelle soluzioni nascoste per rilevare eventuali fughe.
  - Introdurre controlli negativi, cioè materiali volutamente difettosi: la simulazione deve rilevarne il peggioramento.
  - Pre-registrare le previsioni.
- **Test proposto (pilota 4E):** per 2 profili × 1 livello, confronto tra materiali completi e versioni degradate, con 3 ripetizioni, pre-test e post-test.
- **Criterio di accettazione:** la simulazione distingue in modo coerente i materiali degradati (differenza predefinita, per esempio ≥ 15 punti AAS) e la quota di pre-test già sopra soglia è registrata. Senza questa capacità di discriminazione G12-S non può chiudersi.

### E03-05 — P1 — Valutazione con AI consentita ed esaminatore AI: le credenziali potrebbero certificare l'AI, non lo studente
- **Sezioni:** AAS 3C, ACS 3G, ADS 3D, AELS "AI Assisted, Human Verified".
- **Evidenza [E]:**
  - "AI assistita non indipendente, revisione umana solo se disponibile".
  - Nella diagnostica "pratica AI consentita e documentata".
  - Gli stati concettuali includono "competenza verificata".
  - La Level Credential prevede "With Distinction ≥ 90".
  - "Human Verified" presuppone che sia l'umano a verificare, ma è proprio la competenza oggetto della prova.
- **Impatto [I]:** in un corso che incoraggia l'uso dell'AI, prove pratiche corrette automaticamente o con l'AI possono essere completate dall'AI stessa. L'affermazione "competenza verificata" diventa poco solida anche senza toccare G12-E.
- **Raccomandazione:**
  - Per i criteri "correttezza" e "affidabilità" (minimo 3/4) prevedere componenti **non delegabili**: spiegazione di un diff scelto a caso, modifica su un requisito nuovo a tempo, individuazione di un errore inserito nell'output AI.
  - Rinominare lo stato in "competenza attestata da prova interna" finché non esiste una valutazione indipendente.
- **Test proposto:** in 4E, uno Student AI "solo delegante" (si limita a inoltrare il compito a un'altra AI) affronta le prove pratiche e il capstone.
- **Criterio di accettazione:** lo studente puramente delegante non raggiunge le soglie AAS nei criteri non delegabili.

### E03-06 — P2 — Riproducibilità delle evidenze AI: manca la registrazione di modello, versione e parametri
- **Sezioni:** AELS ("documentare strumento, istruzioni rilevanti, errori e correzioni"), AES (protocollo), AVS (registro test).
- **Evidenza [E]:** le ricerche testuali non trovano requisiti su versione o snapshot del modello, temperatura o parametri, data di esecuzione o fornitore. "Seed" compare solo come seed di database. AES prevede "almeno 3 esecuzioni… non prova statistica".
- **Impatto [I]:** i modelli dei piani gratuiti cambiano senza preavviso. Le evidenze di portfolio, parità e regressione non sono confrontabili nel tempo e le esecuzioni V3/V4 non sono ripetibili.
- **Raccomandazione:** aggiungere alla scheda della prova AI questi campi: fornitore, modello e versione (o "non dichiarata"), data e ora, parametri, interfaccia (chat, API o locale), prompt o template versionato, hash dell'output. Per i modelli locali, fissare digest e quantizzazione.
- **Test proposto:** riesecuzione a 30 giorni di 5 laboratori campione usando solo la scheda.
- **Criterio di accettazione:** un terzo riproduce la configurazione dalla sola scheda; gli scostamenti sono attribuibili a variazioni registrate.

### E03-07 — P2 — Quote: nessuna stima del fabbisogno per laboratorio
- **Sezioni:** AES (riserva iniziale del 20%), 2E Creator L3 (prova da 30 casi holdout), 2E Business L1 (input AI manuale).
- **Evidenza [E]:** le quote vanno "misurate cumulativamente" e la riserva del 20% è "da validare", ma non esiste una stima di chiamate o token per laboratorio.
- **Impatto [I]:** per esempio, 30 casi × 3 ripetizioni × 2 versioni fanno 180 inferenze per un solo laboratorio eval. Su una chat gratuita a quota variabile questo può significare un blocco o un lavoro manuale impraticabile. Il 20% è un numero senza base.
- **Raccomandazione:** fare un inventario del fabbisogno (chiamate, token, minuti di GPU o CPU) per ciascuno dei laboratori AI obbligatori, distinguendo chat, API e locale, prima di 4D.
- **Test proposto:** misurare il consumo reale in 4D su 2 settimane-campione per percorso.
- **Criterio di accettazione:** il consumo P80 per laboratorio, con riserva, rientra nella quota gratuita documentata, oppure è indicata un'alternativa locale verificata.

### E03-08 — P2 — "API dei modelli": competenza non definita rispetto al percorso gratuito
- **Sezioni:** cr-w16, L3-P11/P12, 2E L2 (riga A).
- **Evidenza [E]:** sul percorso gratuito l'API locale "non equivale API AI commerciale". Le API commerciali sono "opzionali".
- **Impatto [I]:** aspetti professionali tipici delle API commerciali (gestione delle chiavi, fatturazione e limiti di spesa, errori di rate limit, policy dei fornitori, modifiche dei modelli) non vengono esercitati sul percorso gratuito. Il badge "AI Integration" potrebbe attestare competenze diverse a seconda del ramo gratuito o premium (violazione di AES "stesso riconoscimento").
- **Raccomandazione:** definire la competenza obbligatoria come indipendente dal fornitore (contratto adapter, segreti, budget, retry e backoff, fallback). Simulare in modo deterministico, e solo per i guasti, i casi di errore commerciale come 429 o quota esaurita. **[H]** Valutare eventuali API commerciali con piano gratuito senza carta come candidati da verificare, senza darle per disponibili.
- **Test proposto:** la stessa suite dell'adapter eseguita contro un backend locale e uno commerciale.
- **Criterio di accettazione:** stessa suite di test superata su entrambi; differenze documentate.

### E03-09 — P2 — Tracciabilità R01–R12: solo titoli, senza criteri né mappature; incongruenze sul recupero
- **Sezioni:** 3I (registro R e nota di provenienza), README 3I.
- **Evidenza [E]:**
  - La tabella R contiene solo nome e standard. Mancano criterio, gate collegato, evidenza attesa e sessioni.
  - In 3I si legge prima "non si ricostruisce arbitrariamente il testo puntuale R01–R12", poi "testo puntuale recuperato nell'integrazione seguente"; il README riporta "recuperato 12/12".
  - Mancano 7 immagini (IMG_9493–9499); ne sono state ricevute "sei… (una compensativa)" e IMG_9497 non è verificata.
  - Non esiste un requisito R dedicato alle competenze AI applicate né a "AI Assisted, Human Verified": nella tabella R10 rimanda ad AVS e R12 ad AVS/AMVP.
- **Impatto [I]:** la tracciabilità R → G → standard → sessione (ARTM) non si può verificare. Non è chiaro se il testo recuperato sia completo. Il bilancio delle immagini (7 mancanti contro 6 ricevute) non quadra in modo esplicito.
- **Raccomandazione:**
  - Distinguere "titoli R recuperati 12/12" da "testo integrale R non attestato".
  - Aggiungere una matrice R ↔ G ↔ standard.
  - Spiegare quale immagine copre ciascun file mancante.
  - Valutare un requisito, o un sotto-requisito di R01/R02, per l'uso verificato dell'AI.
- **Test proposto:** controllo incrociato del registro R rispetto alle immagini originali e alla matrice ARTM.
- **Criterio di accettazione:** ogni Rxx ha un criterio verificabile, almeno un gate e almeno un tipo di evidenza; il bilancio delle immagini è esplicito.

### E03-10 — P2 — Termini d'uso dei dati dei piani AI gratuiti assenti dalla scheda AES
- **Sezioni:** AES (scheda risorsa), G10, AELS (nessun dato personale).
- **Evidenza [E]:** la scheda AES prevede costi, quote e licenze, ma nessun campo su conservazione, uso per l'addestramento o opt-out (le ricerche non trovano "opt-out" né "addestr"). I dati sintetici sono già obbligatori: questo è un punto di forza.
- **Impatto [I]:** gli studenti potrebbero inserire elaborati, codice o informazioni di terzi (per esempio nei portfolio o nei casi aziendali Business) in servizi con condizioni d'uso dei dati diverse tra piano gratuito e premium. È un'asimmetria di privacy tra i rami.
- **Raccomandazione:** aggiungere alla scheda AES un campo "uso dei dati / conservazione / opt-out" e una guida all'orientamento iniziale.
- **Test proposto:** verifica documentale datata dei termini di ogni candidato AI.
- **Criterio di accettazione:** campo compilato con fonte e data per il 100% dei servizi AI candidati.

### E03-11 — P2 — Indipendenza del processo di revisione multi-AI
- **Sezioni:** Regola permanente 3, AMVP, mandato CR-001.
- **Evidenza [E]:** ChatGPT "propone… momento, ambito, ruoli, materiali… prepara dossier e prompt… confronta rapporti". È lo stesso soggetto che ha prodotto il lavoro.
- **Impatto [I]:** chi produce il lavoro sceglie anche ambito, domande e sintesi della revisione. Esiste un rischio di selezione o di sintesi distorta. Anche il revisore (Claude) è un fornitore citato nel curriculum.
- **Raccomandazione:** conservare i rapporti integrali e invariati nel repository o nel dossier; far approvare l'ambito all'utente; tracciare in una tabella ogni anomalia E03 con la sua sorte (accolta, respinta con motivazione).
- **Test proposto:** audit del dossier di confronto rispetto ai rapporti originali.
- **Criterio di accettazione:** il 100% delle anomalie dei rapporti compare nel registro con una decisione motivata.

### E03-12 — P2 — Obsolescenza e rivalidazione non attiva
- **Sezioni:** 2E L3 (Evals), AES (rivalidazione).
- **Evidenza [E]:**
  - OpenAI Evals chiude il 30/11/2026, cioè 4 giorni dopo questo checkpoint.
  - La specifica MCP è fissata alla data 2026-07-28.
  - La documentazione HF mostra versioni discordanti sui crediti.
  - La rivalidazione a 30/90 giorni è "proposta… nessuna automazione attivata".
  - Le verifiche delle fonti 2E sono del 25/11/2026.
- **Impatto [I]:** al momento dei prototipi (Fase 4) una parte delle condizioni registrate in 2E potrebbe già essere superata.
- **Raccomandazione:** rendere la rivalidazione una condizione d'ingresso di 4D per le risorse AI usate dai prototipi.
- **Test proposto:** riverifica datata delle risorse AI di 4A/4B prima di 4D.
- **Criterio di accettazione:** tutte le risorse AI dei prototipi hanno una verifica non più vecchia di 30 giorni.

### E03-13 — P3 — Intestazioni di stato non aggiornate, rischio per la continuità con agenti AI
- **Sezioni:** README "Stato operativo corrente — 25 novembre 2026"; ROADMAP "Aggiornato: 25 novembre 2026", "Prossimo intervento: Fase 2C…".
- **Evidenza [E]:** lo stato reale arriva alla Fase 3I del 26/11, ma le intestazioni iniziali sono rimaste al 25/11 e alla Fase 2C. La Procedura permanente chiede di aggiornare i riepiloghi correnti.
- **Impatto [I]:** la continuità tra conversazioni (Regola 1) dipende da un LLM che legge per primi questi documenti. Un'intestazione obsoleta letta all'inizio, o un recupero parziale per contesto lungo, può riportare un agente a uno stato superato.
- **Raccomandazione:** aggiungere in apertura di entrambi i file un blocco "stato corrente" unico e datato (fase, prossimo passo, gate, SHA).
- **Criterio di accettazione:** la prima schermata di ciascun file riporta la Fase 3I e la Fase 4 non autorizzata.

### E03-14 — P3 — Ambiguità minori
- **Evidenza [E]:**
  - "324" indica sia i feedback sospesi sia gli scenari AMVP.
  - Le matrici 2E citano ancora la rubrica 0–3 (13 occorrenze), superata dalla 0–4 per C02, senza nota sul posto.
  - cr-w13s3 ha un feedback impreciso (già registrato).
- **Raccomandazione:** annotare "superato da C02" nelle matrici e distinguere le etichette numeriche.
- **Criterio di accettazione:** nessuna ambiguità residua nel controllo incrociato.

## 11. Raccomandazioni e verifiche mancanti

### 11.1 Affermazioni di qualità sostenibili senza G12-E (senza derogare ad AVS)

| Categoria | Esempi |
|---|---|
| **Sostenibili ora** (V1–V2) | "Progettato secondo standard interni AELS/AAS/…", "audit documentale 264/264", "420 sessioni mappate preliminarmente", "nessun acquisto obbligatorio come requisito di progetto" |
| **Sostenibili solo dopo prova reale** (V3–V4, con data, ambiente e campione) | "laboratorio X eseguito con successo su configurazione Y", "parità gratuito/premium verificata su N esecuzioni", "costo incrementale zero verificato al giorno Z" |
| **Sostenibili solo con G12-S chiuso secondo E03-04** | "in simulazione AI i materiali risultano coerenti e discriminanti", con l'avvertenza esplicita che non si tratta di apprendimento umano |
| **Non sostenibili senza G12-E** | "efficace", "gli studenti raggiungono competenze professionali", "pronto al lavoro", ore effettive di studio, tassi di successo, "eccellenza" come risultato, equivalenza con MIT, UT Austin o altri, "competenza verificata" in senso forte (vedi E03-05) |

### 11.2 Cosa si può verificare dove

| Tipo di verifica | Cosa copre |
|---|---|
| **Solo documentale** | Coerenza tra standard, progressione, aritmetica, tracciabilità |
| **Esecuzioni reali** | Tool calling, RAG, eval, workflow, deploy, quote, hardware |
| **Servizi e condizioni commerciali** | Piani gratuiti, prezzi, termini sui dati, accesso dall'Italia, carta richiesta |
| **Sperimentazione umana** | G12-E, tempi reali, ritenzione |

### 11.3 Verifiche mancanti prioritarie prima o durante la Fase 4
1. Matrice dei prerequisiti AI per 4A e per il capstone L2 (E03-01).
2. Suite di capacità del modello e classificazione hardware dei laboratori AI (E03-02).
3. Definizione di chiusura di G12-S e regola G12 rispetto al rilascio (E03-03).
4. Protocollo anti-contaminazione AMVP con pre-test e controlli negativi (E03-04).
5. Prova dello studente "solo delegante" (E03-05).
6. Scheda di riproducibilità AI, inventario delle quote, termini d'uso dei dati (E03-06, 07, 10).

**Simulazione, collaudo reale ed efficacia empirica umana sono tre livelli distinti.** Nessuno dei tre è stato eseguito in questo rapporto. Il rapporto vale solo come revisione documentale AI.

## 12. Esito complessivo
**PARZIALE.**
- La parte documentale E03 è in gran parte solida e coerente: rigore epistemico, laboratori AI ben progettati, aritmetica corretta.
- Ci sono però cinque anomalie P1 da risolvere a livello di progetto prima che la Fase 4 possa produrre evidenze affidabili: progressione L2/L3, parità gratuita AI, regola G12-S/G12-E, contaminazione AMVP, validità delle valutazioni con AI.
- Gli aspetti operativi (funzionamento dei laboratori AI, quote, parità, efficacia) sono **non verificabili** con i soli documenti.

Non ho modificato file, chiuso gate, cambiato standard né avviato la Fase 4.
