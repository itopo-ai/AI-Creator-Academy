# CR-001 — Rapporto originale E07 · Accessibilità e Mobile UX

**Revisione AI esterna simulata, documentale. Non è un audit umano indipendente, non è una certificazione, non è un collaudo di prototipi o runtime.**

---

## 1. Identificazione

| Voce | Valore |
|---|---|
| Rapporto | E07-original-report (CR-001, prospettiva E07 accessibilità/mobile UX secondo AMVP) |
| Modello | Claude Opus 5.5 (ID `claude-opus-5-5`), Anthropic |
| Versione/build interna | Non nota al modello; non dichiarabile oltre l'ID |
| Limite delle conoscenze del modello | Fine giugno 2026 |
| Data di redazione | 26/11/2026, sera (fuso Europe/Rome) |
| Ruolo | Revisore AI esterno simulato, prospettiva specialistica E07. Non esperto umano, non commissione, non validatore |
| Esito complessivo per il mandato E07 | **PARZIALE** (dettaglio al § 10) |

## 2. Capacità e limiti

**Capacità usate:** lettura integrale dei due file, confronto incrociato tra sezioni, ricerca di contraddizioni, ricalcolo dell'aritmetica dichiarata, calcolo degli SHA, conoscenza generale di WCAG 2.2, linee guida Apple e comportamento delle PWA su iOS.

**Limiti:**
- Nessun accesso a codice, repository, branch, commit, app installata, iPhone reale, Safari, VoiceOver o link esterni. Per istruzione non ho aperto gli URL citati.
- Le norme esterne che cito (numeri dei criteri WCAG, dimensioni dei target Apple, comportamento dello storage PWA su iOS) vengono dalla mia conoscenza addestrativa. In questa revisione **non le ho verificate su fonti ufficiali** e sono marcate **[K]**.
- Non posso osservare interazioni touch, safe area, rendering, prestazioni, ergonomia o fatica di lettura. Ogni giudizio sull'interfaccia reale è **non verificabile** in questa sede.
- Non ho visto le immagini del concept. Le parti coperte o fuori inquadratura, che ROADMAP dichiara non trascritte, **non sono state ricostruite né presunte**.
- Questa revisione è una simulazione AI. Non dimostra niente sull'efficacia per studenti reali né sull'usabilità per persone con disabilità.

## 3. Bias e conflitti (non garantiti assenti)

- **Possibile conflitto di interessi:** sono un modello Anthropic. I materiali citano Claude e Anthropic come risorse candidate (Claude free in AES; Anthropic AI Fluency, codice A del blocco 2E L1B; documentazione Claude in 2E L1/L3) e come revisore esterno (AMVP, Regola 3). Non ho espresso giudizi preferenziali su queste risorse. Il lettore deve comunque tenerne conto.
- **Bias di inquadramento:** il prompt di incarico è stato preparato nel flusso di lavoro principale (ChatGPT, Regola 3) e definisce ambito e categorie, che possono orientare la lettura.
- **Bias di compiacenza:** i modelli linguistici tendono a confermare la struttura proposta. Ho cercato apposta controesempi e contraddizioni (§ 8).
- **Bias normativo:** tendo a usare WCAG/Apple HIG come riferimento implicito. Sono riferimenti diffusi ma non sono stati adottati formalmente dal progetto (cfr. A02).

## 4. Indipendenza procedurale

- Rapporto redatto senza conoscere i rapporti E01–E06 o eventuali altri E07, e senza conclusioni di altri revisori.
- L'indipendenza è solo procedurale: stesso dossier, conversazione separata, nessuna interazione con il processo principale. **Non** è indipendenza istituzionale, umana o di fornitore.
- Concordanze future con altri rapporti AI non sono prova (AMVP, ROADMAP r. 1259).

## 5. Ambito, materiali e checkpoint

| Voce | Valore |
|---|---|
| Checkpoint dichiarato dall'utente | `f9d98c2bbd4d3622b9ccb5eeeb5c1811a2c4d401` |
| Verifica del checkpoint | **Non verificabile**: nessun accesso al repository. Verificati solo gli SHA dei blob dei file ricevuti |
| README.md, ricevuto come `5fa56b67-README.md` | SHA Git (blob) calcolato `abca6f1ce6345ed1cc55eb5dd5f78ff0a7232afb`, **coincide** con quello dichiarato; SHA-256 `ed51e30cff36bc68d18decc8d0df45343859df27242f3f1437eb18168eeb2752`; 54.854 byte; 183 terminatori di riga |
| ROADMAP.md, ricevuto come `63da7404-ROADMAP.md` | SHA Git (blob) calcolato `af9888bc28f0fef48ea226e86fe3be5a24913008`, **coincide** con quello dichiarato; SHA-256 `dcc4536c87a5b094522c43ea5dc6dda30e5da75c62c454ef6eafce60fe1ac8fa`; 290.224 byte; 1.322 terminatori di riga |
| Copertura di lettura | Integrale per entrambi i file (README rr. 1–184; ROADMAP rr. 1–1322) |
| Fuori ambito | Codice, curriculum JSON, app, branch, link esterni, immagini, rapporti di altri revisori |
| Natura di CR-001 | Revisione documentale dell'architettura prima della Fase 4. Non certifica prototipi o runtime (ROADMAP r. 1268) |

I riferimenti nella forma "R r. N" indicano README.md e "M r. N" ROADMAP.md, alla riga N.

## 6. Metodo

1. Calcolo con `git hash-object` dello SHA dei blob, e di SHA-256, byte e righe, sui file ricevuti.
2. Lettura integrale di README e ROADMAP, in ordine.
3. Estrazione di tutte le occorrenze pertinenti al mandato: Mobile First, iPhone, safe area, touch, leggibilità, accessibilità, VoiceOver, WCAG, navigazione, ripresa, desktop/hardware H0–H3, concept grafico, C08, 4C, AMVP C06/B06.
4. Tracciabilità: confronto delle decisioni approvate (direzione visiva, C01–C08, AES H0–H3, ALWS blocchi riprendibili, AVS runtime) con R01–R12, G01–G12, campi ARTM e piano 4A–4H.
5. Ricerca attiva di contraddizioni e controesempi, compresi quelli interni al curriculum.
6. Ricalcolo dell'aritmetica dichiarata (ALWS e percentuali): **nessuno scostamento** (63/87,5/188 = 338,5; 81/145,25/194 = 420,25; 758,75 h; 108,39 min; +187,4%; 414,5/500,25/914,75; 476,675/575,2875; +59,1%; +55%; 57,1%; 76,9%; 79,55%).
7. Classificazione delle anomalie P0–P3 secondo la scala AVS (M r. 1258). Per ognuna: impatto, raccomandazione, test, criterio di accettazione ed esito.

**Legenda delle evidenze:** **[T]** evidenza testuale nei materiali · **[I]** mia inferenza dai testi · **[H]** ipotesi da verificare · **[K]** conoscenza esterna del modello, non verificata in questa revisione.

## 7. Punti di forza (evidenze testuali)

- **[T]** La direzione Mobile First è esplicita e coerente nei due documenti: priorità iPhone, futura compatibilità Android/tablet/desktop, navigazione inferiore, studio immersivo, accessibilità, adattamento schermi, preservazione dei progressi (R r. 28; M r. 239). Nel riferimento visivo compaiono leggibilità, safe area, dimensioni touch e dati reali (R r. 77; M r. 369).
- **[T]** Il concept è dichiarato onestamente come "non vincolante pixel per pixel", con "numeri, testi e durate illustrativi, non requisiti" (R r. 77; M r. 369, 1316–1318).
- **[T]** **C08**: "Mobile First iPhone, dichiarare preventivamente laboratori che richiedono computer" (M r. 1266). AES formalizza i livelli H0–H3 e chiarisce che "Mobile First non implica tutti lab su smartphone" (M r. 1242; R r. 162).
- **[T]** La distinzione tra simulazione e realtà è dichiarata in modo esplicito anche sul piano tecnico: "Emulazione non prova iPhone reale, test VoiceOver e tastiera manuali; WCAG non certificazione" (M r. 844); "Runtime futuro Safari/iPhone reale distinto da simulazione" (M r. 1258).
- **[T]** La ripresa compare più volte: diagnostica "modulare, riprendibile" (M r. 1238), "blocchi riprendibili senza nuovi ID automatici" (M r. 1246), "ripresa senza penalità" in caso di quote esaurite (M r. 1242).
- **[T]** Rischi mobili specifici già individuati nel 2E: "test VoiceOver, tastiera, zoom, caption, trascrizioni, safe area, link esterni e rientro" (M r. 686); "rientro link iPhone, desktop per editing" (M r. 751); "iPhone app studio non sostituisce ambiente desktop" (M r. 603); "disponibilità alternativa per chi ha solo iPhone da collaudare" (M r. 1218).
- **[T]** AMVP prevede profili sintetici Mobile First dedicati, C06 e B06 (M r. 1259). ACS esclude biometria e documenti obbligatori (M r. 1250). AAS chiede una difesa "scritta/registrata accessibile" (M r. 1234).
- **[T]** La checklist di rilascio elenca apertamente come non eseguiti i collaudi Safari/iPhone, PWA, offline/cache, backup e aggiornamento (M rr. 45–53; R r. 15).
- **[T]** La distinzione **G12-S aperto / G12-E non verificata** è formalmente ben costruita e collegata al divieto di chiusure automatiche e di deroghe AVS (M rr. 1294–1299).

## 8. Anomalie

Scala AVS: P0 critica, blocco immediato; P1 alta, blocca l'accettazione pertinente; P2 media, richiede correzione o decisione motivata; P3 bassa, da pianificare. **Nessuna anomalia P0** emerge su base documentale.

### P1

#### E07-A01 — Accessibilità digitale e UX mobile senza requisito R né gate G dedicati
- **Sezione:** Fase 3I, registro R01–R12 e gate (M rr. 1273–1292); coerenze C01–C08 (M r. 1266); direzione visiva (M r. 369).
- **Evidenza [T]:** R01–R12 non contiene un requisito di accessibilità dell'interfaccia o di usabilità mobile. L'unico R vicino è R08, "Risorse accessibili e legalmente utilizzabili", che resta ambiguo tra "raggiungibili" e "accessibili a persone con disabilità". G05 riguarda l'"accessibilità economica". Tra le famiglie G01–G12 nessuna copre l'accessibilità dell'interfaccia. AVS elenca "accessibilità" tra i collaudi runtime futuri (M r. 1258), ma senza una famiglia di gate.
- **Inferenza [I]:** C08 e la direzione Mobile First, entrambe approvate, non sono tracciate su alcun R o G. Un difetto grave di accessibilità o di uso su iPhone non ha quindi un gate che possa bloccare l'accettazione (AVS: "qualsiasi violazione obbligatoria blocca", ma l'obbligo non è stato formalizzato).
- **Impatto:** tracciabilità incompleta; rischio che 4C venga accettato senza criteri di accessibilità vincolanti.
- **Raccomandazione:** con decisione dell'utente, (a) introdurre un requisito dedicato (ad esempio "R13 Accessibilità e usabilità mobile") con il relativo gate, oppure (b) assegnare esplicitamente l'accessibilità a R01/R11 e G01/G11 con sottocriteri nominati. In entrambi i casi disambiguare R08. Proposta organizzativa, da approvare: non chiude né modifica gate.
- **Test:** verifica di tracciabilità. Ogni decisione approvata (C01–C08, direzione visiva, AES H0–H3, ALWS ripresa) deve essere collegata ad almeno un R, un G e un criterio di chiusura.
- **Criterio di accettazione:** 100% delle decisioni approvate mappate; R08 riformulato senza ambiguità; mappatura approvata dall'utente.
- **Esito:** **Non conforme** (tracciabilità).

#### E07-A02 — Criteri misurabili assenti per leggibilità, touch, safe area e accessibilità dell'app
- **Sezione:** direzione visiva (R r. 77; M r. 369); strategia Mobile First (M r. 239); AELS "mobile first" (M r. 1230).
- **Evidenza [T]:** i testi dicono di "adattare per accessibilità, leggibilità, safe area, dimensioni touch e dati reali", ma non fissano un livello WCAG obiettivo per l'app, soglie, dispositivi di riferimento o impostazioni di sistema da supportare.
- **Controesempio interno [T]:** il curriculum chiede agli studenti di verificare layout "320–1280px e zoom" (cr-w07s2, M r. 329), contrasto WCAG 4,5:1 (M r. 670) e accessibilità con "VoiceOver se disponibile e zoom" (cr-w21s2, M r. 437). L'Academy richiede agli studenti un livello di verifica che **non si impone** per la propria app.
- **Riferimenti proposti [K], da confermare su fonti ufficiali:** WCAG 2.2 livello AA come soglia minima. Tra i criteri pertinenti: 1.4.3 contrasto testo, 1.4.11 contrasto non testuale, 1.4.4 ridimensionamento testo al 200%, 1.4.10 reflow a 320 px CSS, 1.3.4 orientamento, 2.5.8 dimensione minima dei target (24×24 px CSS), 1.4.1 uso del colore, 2.2.1 tempi regolabili. Come obiettivo progettuale iOS, target di circa 44×44 pt. Per PWA iOS: `viewport-fit=cover` con `env(safe-area-inset-*)` e niente `user-scalable=no`.
- **Impatto:** il collaudo di 4C non ha un atteso; il rischio è un'accettazione soggettiva.
- **Raccomandazione:** prima di 4C, approvare una scheda di criteri di accessibilità e mobile con dispositivi di riferimento (almeno lo schermo più piccolo e il più grande supportati), impostazioni iOS da coprire (Testo più grande, Zoom, VoiceOver, Riduci movimento, Aumenta contrasto, orizzontale) e livello di conformità.
- **Test:** T-E07-01, T-E07-02 e T-E07-04 (§ 11).
- **Criterio di accettazione:** scheda approvata; ogni criterio con atteso misurabile e metodo; nessun criterio "a giudizio".
- **Esito:** **Non conforme** (requisito mancante a livello documentale). Conformità dell'app **non verificabile**.

#### E07-A03 — Ripresa dello studio e continuità tra dispositivi non specificate; rischio sui progressi
- **Sezione:** README 6.5.0 (R r. 50: "Risposte e punteggio corrente nel profilo cifrato"); ALWS (M r. 1246); AES (M r. 1242); C08 (M r. 1266); checklist (M rr. 48–51).
- **Evidenza [T]:** la "ripresa studio" è un elemento del concept, ma non sono definiti granularità (sessione, attività, blocco, posizione di lettura), stato salvato e comportamento dopo chiusura forzata, riavvio, assenza di rete o rientro da un link esterno. ALWS introduce "blocchi riprendibili" mentre resta valido "nessuna modifica schema" (M rr. 1234, 1238). L'avanzamento attuale è calcolato su attività spuntate (R r. 53).
- **Inferenza [I]:** con laboratori su computer (C08) e studio su iPhone, lo stesso studente usa due dispositivi. I documenti non descrivono come evidenze e progressi passino dall'uno all'altro, salvo backup cifrato ed export, entrambi mai collaudati (M rr. 50, 1258). È possibile una tensione tra blocchi riprendibili interni alla sessione e il divieto di modificare lo schema.
- **Ipotesi [H]/[K]:** su iOS, una web app aggiunta alla schermata Home può avere uno storage separato da Safari. Un utente che inizia in Safari e poi installa la PWA potrebbe non trovare i progressi. Il comportamento di conservazione e rimozione dello storage va collaudato sulla versione iOS in uso.
- **Impatto:** rischio diretto sul vincolo di preservazione dei progressi; rischio di frammentare le evidenze del portfolio.
- **Raccomandazione:** definire in 4C un "modello di ripresa" (granularità, dati salvati, dove, per quanto tempo) e un "flusso cross-device" (registrazione dell'evidenza di laboratorio, trasferimento, conflitti). Verificare se servono modifiche di schema e, in quel caso, chiedere un'approvazione esplicita.
- **Test:** T-E07-05, T-E07-06, T-E07-07.
- **Criterio di accettazione:** zero perdite di progressi, conteggi identici prima e dopo, posizione ripristinata alla granularità dichiarata, nessuno schema modificato senza approvazione.
- **Esito:** **Non verificabile** (runtime) / **Parziale** (documentale).

#### E07-A04 — Dichiarazione dei laboratori desktop non resa operativa né tracciabile per sessione
- **Sezione:** C08 (M r. 1266); AES H0–H3 (M r. 1242); campi ARTM (M r. 1258); 2E (M rr. 603, 769, 1023, 1111, 1218).
- **Evidenza [T]:** C08 chiede di dichiarare in anticipo i laboratori che richiedono un computer. I campi ARTM elencati comprendono "AES costi/quote/licenze/varianti", ma **non** un campo esplicito per il dispositivo minimo (H0–H3), il sistema operativo o la parte svolgibile su iPhone. Alcuni casi: Power BI Desktop "gratuito Windows" (M r. 1023), con Mac/Linux che "non prova DAX/Power Query specifici" (M r. 1111); Supabase locale con runtime container (M r. 769); n8n/Ollama locali (M r. 1218); "alternativa per chi ha solo iPhone da collaudare" (M r. 1218).
- **Inferenza [I]:** gran parte dei laboratori L2 e L3 dei due percorsi sembra richiedere un computer. La quota esatta non si può calcolare dai documenti e va misurata. Profili come C06/B06 (Mobile First) rischiano di scoprirlo a percorso iniziato. Un'affermazione generica come "Academy Mobile First" potrebbe essere letta come "percorso completabile da iPhone".
- **Impatto:** trasparenza verso lo studente; parità (rimando a E04/E01 per DAX e sistemi operativi); possibile affermazione fuorviante.
- **Raccomandazione:** aggiungere all'ARTM i campi "H minimo", "sistemi operativi supportati", "parte H0" e "durata stimata su computer". In UI: segnalazione "Richiede computer" prima dell'avvio della sessione e nella vista del percorso, più una dichiarazione del dispositivo nell'onboarding. Pubblicare la quota di sessioni completabili da iPhone per ogni livello.
- **Test:** T-E07-08, T-E07-09.
- **Criterio di accettazione:** 420/420 record ARTM con livello H e sistema operativo; dichiarazione visibile prima dell'avvio, leggibile con VoiceOver; walkthrough C06/B06 senza scoperte tardive.
- **Esito:** **Parziale**.

#### E07-A05 — Riepiloghi "correnti" obsoleti, resi prevalenti dalla regola di precedenza (trasversale)
- **Sezione:** README, stato corrente (R rr. 3, 24–32) e regola di precedenza (R r. 36); ROADMAP, intestazione e stato corrente (M rr. 3, 26–41, 55–60); Fase 3I (R r. 183; M r. 1269); procedura permanente (M r. 67).
- **Evidenza [T]:** README dichiara "prevalgono il riepilogo sopra e le evidenze aggiornate in ROADMAP.md" (R r. 36), ma il riepilogo sopra si chiude con "Prossimo passo 2C" (R r. 32). In ROADMAP restano "Aggiornato: 25 novembre 2026" (M r. 3) e "Prossimo intervento: Fase 2C, completare audit individuale Creator 1–6" (M r. 60). Lo stato reale è Fase 3I approvata, CR-001 in preparazione e Fase 4 non autorizzata (R r. 183; M r. 1269). La procedura permanente impone di aggiornare i riepiloghi correnti quando cambia il prossimo passo (M r. 67).
- **Impatto:** in una ripresa da nuova conversazione (Regola 1), le sezioni dichiarate prevalenti indicano un passo superato. È fuori dal mio mandato specialistico, ma ricade nella richiesta di cercare contraddizioni.
- **Raccomandazione:** aggiornare le sezioni correnti di entrambi i documenti oppure marcarle come storiche, coerentemente con la regola di precedenza. Solo con autorizzazione: io non modifico file.
- **Test:** T-E07-14.
- **Criterio di accettazione:** nessuna sezione dichiarata "corrente" o "prevalente" indica un passo diverso da quello in 3I.
- **Esito:** **Non conforme** (documentale).

#### E07-A06 — Nessuna baseline runtime documentata su iPhone per produzione e RC1 (pre-esistente)
- **Sezione:** README 6.5.1/6.5.0 (R rr. 44, 50, 53); ROADMAP, ambienti e checklist (M rr. 18, 45–53).
- **Evidenza [T]:** "Collaudo Safari da effettuare" (R r. 44); "Test browser bloccato da ERR_BLOCKED_BY_ADMINISTRATOR" (R r. 50); "nuovo collaudo Safari necessario" (R r. 53); RC1 "installata su iPhone secondo l'utente" (M r. 18), cioè un dato dichiarato e non verificato.
- **Inferenza [I]:** manca una baseline del comportamento attuale su iPhone. La non regressione mobile (G11) e il confronto di 4C con l'esistente non hanno un riferimento.
- **Impatto:** regressioni di UX e accessibilità non rilevabili; rischio non quantificabile per i progressi degli utenti attuali.
- **Raccomandazione:** prima di 4C, collaudo reale in sola lettura di main 6.5.1 e RC1 su iPhone (modello e versione iOS registrati). Le osservazioni vanno documentate senza modificare nulla.
- **Test:** T-E07-03.
- **Criterio di accettazione:** rapporto baseline versionato, con dispositivo, iOS, build e checkpoint; esiti di superamento, fallimento o blocco per ogni voce.
- **Esito:** **Non verificabile**.

### P2

#### E07-A07 — Riferimento visivo non archiviato e recupero delle immagini parziale
- **Sezione:** R r. 77; M rr. 369, 1263, 1316, 1322.
- **Evidenza [T]:** "file grafico non archiviato nel repository" (R r. 77; M r. 369); mancavano IMG_9493–9499 e "IMG_9497 originale non verificato" (M rr. 1263, 1322); concept 11.1 con "seguito coperto nell'immagine, non trascritto" (M r. 1316).
- **Impatto:** il criterio di 4C "rispettando l'identità grafica approvata" (M r. 1307) non è verificabile in modo oggettivo. I colori sono solo nominati (blu notte, ciano, smeraldo, viola, oro), senza valori, quindi il contrasto non è valutabile.
- **Raccomandazione:** archiviare il riferimento (se autorizzato e privo di dati riservati) oppure tradurlo in token documentati (valori colore, tipografia, spaziature) con verifica del contrasto. Le parti illeggibili vanno dichiarate come tali.
- **Test:** T-E07-10.
- **Criterio di accettazione:** token approvati; ogni coppia testo/sfondo e ogni indicatore con contrasto misurato rispetto al criterio approvato in A02.
- **Esito:** **Parziale**.

#### E07-A08 — Leggibilità di contenuti lunghi e tecnici su iPhone non progettata
- **Sezione:** AELS (M r. 1230: teoria fino a 800–1500 parole per L3, "codice commentato", "formule esemplificate"); ALWS S4/S5 da 120–240 minuti (M r. 1246); tabelle, SQL, DAX e dashboard nei piani 2E.
- **Evidenza [T]:** mancano criteri mobili per testi lunghi (struttura dei titoli, suddivisione, posizione di lettura salvata), blocchi di codice (a capo o scorrimento orizzontale), tabelle, formule (lettura con VoiceOver) e dashboard su schermo stretto.
- **Ipotesi [H]:** blocchi di codice e tabelle sono i punti in cui il reflow a 320 px CSS tende più spesso a fallire.
- **Raccomandazione:** in 4A/4B/4C prototipare almeno una sessione L3 teorica e una con codice e tabelle, entrambe su iPhone reale.
- **Test:** T-E07-04, T-E07-11.
- **Criterio di accettazione:** nessuna perdita di contenuto o funzione con testo al 200% e larghezza di 320 px CSS (salvo eccezioni documentate); formule e codice leggibili con VoiceOver; posizione di lettura ripristinata.
- **Esito:** **Non verificabile**.

#### E07-A09 — Navigazione e perimetro di 4C incompleti
- **Sezione:** strategia (R r. 28; M r. 239: "navigazione inferiore, studio immersivo"); 4C (M r. 1307); dizionario (R r. 40); rientro dai link (M rr. 686, 751).
- **Evidenza [T]:** 4C copre Home, Il mio percorso, sessione, valutazione, portfolio e traguardi. **Non** cita onboarding e diagnostica (pure "Onboarding mobile first", M r. 1238), dizionario (funzione esistente, da non far regredire), impostazioni, backup, ripristino ed export, scelta gratuito/premium, dichiarazione del dispositivo, stati offline ed errore, apertura e rientro dalle risorse esterne.
- **Inferenza [I]:** la navigazione inferiore e lo "studio immersivo" vanno conciliati (la barra resta visibile o no? come si esce?). In modalità standalone una PWA iOS non ha il pulsante Indietro del browser [K], quindi navigazione all'indietro e rientro vanno progettati.
- **Raccomandazione:** mappa dell'architettura informativa e dei flussi, con estensione di 4C alle schermate mancanti oppure loro esclusione motivata e approvata.
- **Test:** T-E07-12.
- **Criterio di accettazione:** ogni flusso critico completabile con touch e con VoiceOver; rientro da un link esterno con stato conservato; ordine del focus coerente.
- **Esito:** **Parziale**.

#### E07-A10 — Molti indicatori su schermo piccolo, con rischio di confonderli e di codifica solo cromatica
- **Sezione:** 3A (M r. 1225: distinguere avanzamento, conoscenza, competenza, portfolio); ADS (M r. 1238: indicatori distinti); C03 (M r. 1266); concept con "indicatori circolari e barre" (M r. 369).
- **Evidenza [T]:** gli standard richiedono indicatori diversi e non confondibili. Il concept prevede anelli e barre con numeri illustrativi e colori per percorso e progressione.
- **Inferenza [I]:** su iPhone un anello al 100% di "avanzamento" può essere letto come competenza raggiunta, contro C03 e ACS. Senza etichette testuali né nomi accessibili, l'informazione affidata al solo colore viola il principio [K] WCAG 1.4.1.
- **Raccomandazione:** etichetta testuale per ogni indicatore, nome e valore accessibili, codifica non solo cromatica, glossario degli indicatori.
- **Test:** T-E07-13.
- **Criterio di accettazione:** in collaudo reale, il significato di ogni indicatore è annunciato correttamente da VoiceOver e distinguibile senza colore.
- **Esito:** **Non verificabile**.

#### E07-A11 — Tempi di diagnostica e verifiche ambigui rispetto a mobile e tecnologie assistive
- **Sezione:** ADS (M r. 1238: "D1 10 domande/10 min", ecc.); AAS (M r. 1234: "L1 5–8 (5–12 min)").
- **Evidenza [T]:** non è chiaro se le durate siano stime o limiti imposti. Le prove pratiche (file, CSV, formule) fanno parte della diagnostica Business.
- **Ipotesi [H]:** limiti imposti penalizzerebbero chi usa VoiceOver o Zoom e chi su iOS cambia app per consultare un file. Le prove pratiche su iPhone potrebbero non essere svolgibili (rimando ad A04).
- **Raccomandazione:** dichiarare che le durate sono stime, senza timer bloccanti, oppure prevedere tempi regolabili [K, WCAG 2.2.1]; indicare il livello H per le prove pratiche.
- **Test:** T-E07-15.
- **Criterio di accettazione:** nessun limite di tempo non regolabile; prova pratica con dispositivo dichiarato.
- **Esito:** **Non verificabile**.

#### E07-A12 — Le evidenze mobili dipendono dal collaudo reale, ma i criteri non sono marcati come tali
- **Sezione:** AMVP (M r. 1259: profili C06/B06 sintetici); M r. 844 (emulazione non è un iPhone reale); AVS (M r. 1258).
- **Evidenza [T]:** i documenti distinguono simulazione e collaudo, ma ARTM e i gate non indicano quali criteri **possono** essere chiusi solo con un collaudo reale.
- **Inferenza [I]:** i profili sintetici AMVP possono simulare comprensione e decisioni, non ergonomia touch, safe area, lettura con VoiceOver o fatica visiva. Un collaudo dell'utente su iPhone è un **collaudo reale (V3)**, ma **non** equivale a prove con persone con disabilità o a efficacia empirica (G12-E).
- **Raccomandazione:** aggiungere a ogni criterio di accessibilità e mobile un campo "tipo di evidenza minima" (documentale, simulazione, collaudo reale, empirica umana) e vietare chiusure con un livello inferiore.
- **Test:** T-E07-16.
- **Criterio di accettazione:** 100% dei criteri E07 con livello di evidenza minimo; nessuno chiudibile con sola simulazione.
- **Esito:** **Parziale**.

#### E07-A13 — Semantica della mappatura R↔G e testo storico 3I non annotato
- **Sezione:** M rr. 1263, 1267, 1275–1292.
- **Evidenza [T]:** la corrispondenza R01↔G01 … R12↔G12 è implicita (stessa numerazione) e non dichiarata. **R12 "Validazione e revisione critica"** (AVS, AMVP) non coincide con **G12 "Efficacia formativa"**. M r. 1263 afferma che R01–R12 non viene ricostruito; M rr. 1267 e 1273 lo dichiarano recuperato "nell'integrazione seguente". La sequenza è comprensibile ma la r. 1263 non porta una nota di superamento. Mancavano sette immagini (9493–9499); ne sono arrivate sei, "una compensativa" (M r. 1322).
- **Impatto:** tracciabilità ambigua; un lettore della sola r. 1263 può trarre conclusioni opposte.
- **Raccomandazione:** tabella esplicita R↔G (anche molti-a-molti); nota "superato da" sulla r. 1263; elenco delle immagini ricevute con quali parti risultano illeggibili.
- **Test:** T-E07-14.
- **Criterio di accettazione:** mappatura dichiarata e approvata; nessun testo storico contraddittorio privo di nota.
- **Esito:** **Parziale**.

### P3

- **E07-A14 — Compatibilità Android futura.** [T] "futura compatibilità Android" (R r. 28). Raccomandazione: evitare soluzioni solo iOS nella UI senza alternativa (gesti di sistema, convenzioni di navigazione). Test: revisione di 4C per dipendenze specifiche di piattaforma. Esito: **Non verificabile**.
- **E07-A15 — Movimento e gesti.** [I] La metafora "ascesa alla vetta" e i traguardi fanno pensare ad animazioni. Raccomandazione [K]: rispettare `prefers-reduced-motion` e prevedere alternative ai gesti di trascinamento o swipe (WCAG 2.5.1, 2.5.7). Esito: **Non verificabile**.
- **E07-A16 — Quiz su touch.** [T] Tre opzioni con feedback specifico (M r. 24). Raccomandazione: target separati, conferma prima dell'invio se la risposta è definitiva, feedback non affidato solo al colore. Nota fuori mandato, rimandata a E01: "264/264 coppie stessa posizione" della risposta corretta tra quiz base e avanzato, "UI non verificata" (M r. 652). È un possibile schema sfruttabile, da valutare insieme all'ordine in UI. Esito: **Non verificabile**.
- **E07-A17 — Aspetto di sistema.** [T] L'identità usa il blu notte; i documenti non dicono nulla su modalità chiara/scura, Aumenta contrasto e Inversione smart. Raccomandazione: decidere e verificare. Esito: **Non verificabile**.

## 9. G12-S aperto / G12-E non verificata: affermazioni di qualità sostenibili

**Lettura dei testi [T]:** G12-S è l'efficacia didattica simulata (AMVP), "Aperto". G12-E è l'efficacia empirica presso studenti reali, "Non verificata". "Prima di un eventuale rilascio stabilire quali affermazioni sulla qualità siano sostenibili in assenza di G12-E. Nessuna chiusura automatica né deroga ai criteri AVS" (M rr. 1294–1299). AMVP: "nessun test umano esterno disponibile … efficacia empirica umana non dimostrata" (M r. 1259).

**Valutazione:** la distinzione è **conforme** sul piano documentale. Manca però uno strumento operativo per applicarla alle comunicazioni: non esiste un registro delle affermazioni pubbliche con il livello di evidenza richiesto.

**Principio proposto, senza deroghe AVS:** un'affermazione è sostenibile solo se il livello di evidenza raggiunto è **pari o superiore** a quello che l'affermazione implica. Livelli: D documentale (V2) · S simulazione AI (G12-S) · R collaudo reale (V3/V4) · E empirica umana (G12-E). Senza G12-E restano ammissibili solo affermazioni di livello D, S o R, **formulate come tali**.

| Affermazione | Evidenza minima | Sostenibile oggi? | Formulazione ammissibile |
|---|---|---|---|
| "Progettata Mobile First per iPhone" | D | Sì, come intento | "Progettata con approccio Mobile First; lo studio teorico è pensato per iPhone" |
| "La teoria si studia da iPhone; i laboratori indicati richiedono un computer" | D + ARTM completo + R | No (ARTM non compilato, nessun collaudo) | Dopo A04 e T-E07-08: "X sessioni su 420 richiedono un computer, segnalate prima dell'avvio" |
| "Conforme WCAG 2.2 AA" | R (audit su schermate e versione definite) | **No** | Dopo il collaudo: "Schermate A–F verificate rispetto a WCAG 2.2 AA il [data] su [dispositivo/iOS/build]; limiti: …" |
| "Funziona offline e conserva i progressi" | R | **No** | Dopo T-E07-05/06/07, limitata ai casi provati |
| "Simulazioni con studenti virtuali indicano…" | S | Possibile dopo 4E | Sempre con "simulazione AI, non evidenza su studenti reali" |
| "Facile da usare su smartphone" / "esperienza eccellente" | E (utenti reali) | **No** | Non usare; al massimo "verificata dal team su iPhone [modello]" (livello R) |
| "Accessibile a persone con disabilità" (come risultato) | E (utenti di tecnologie assistive) + R | **No** | Solo come conformità tecnica di livello R, mai come esito per gli utenti |
| "Si impara efficacemente da mobile" / "migliora l'apprendimento" | E | **No** | Non usare |
| "Equivalente o superiore a programmi MIT, UT Austin, Google…" | E + benchmark | **No** | Già escluso dai testi (M rr. 228, 1230, 1258) |

**Raccomandazione:** istituire in ARTM o in un registro collegato un **registro delle affermazioni** (testo, livello di evidenza richiesto, evidenza disponibile, stato, data di rivalidazione). Criterio di accettazione: nessuna affermazione pubblica con livello superiore all'evidenza registrata.

## 10. Esiti per area del mandato E07

| Area | Esito | Motivazione sintetica |
|---|---|---|
| Mobile First iPhone (direzione) | **Parziale** | Esplicita e coerente; non tradotta in requisiti né gate (A01, A02) |
| Leggibilità | **Non conforme** (doc.) / **Non verificabile** (app) | Nessun criterio (A02, A08) |
| Touch | **Non conforme** (doc.) / **Non verificabile** (app) | Solo "dimensioni touch", senza soglie (A02, A16) |
| Safe area | **Non conforme** (doc.) / **Non verificabile** (app) | Citata, nessun criterio né test (A02) |
| Accessibilità | **Parziale** | Presente nelle intenzioni e nei laboratori del curriculum, assente come requisito dell'app (A01, A02, A10, A11) |
| Navigazione | **Parziale** | Concept indicato, perimetro 4C incompleto (A09) |
| Ripresa studio | **Non verificabile** | Granularità e flussi tra dispositivi non definiti (A03) |
| Dichiarazione laboratori desktop | **Parziale** | C08 e H0–H3 approvati, nessun campo ARTM né flusso UI (A04) |
| Tracciabilità R01–R12 | **Parziale** | 12/12 presenti; accessibilità e C08 non mappati; R12↔G12 non allineati (A01, A13) |
| Distinzione G12-S / G12-E | **Conforme** (doc.) | Ben definita; manca il registro delle affermazioni (§ 9) |
| **Complessivo E07** | **PARZIALE** | Direzione corretta e limiti dichiarati con onestà; requisiti misurabili, tracciabilità e prove assenti |

Nessun gate è stato chiuso o proposto per la chiusura. Tutte le anomalie restano aperte fino a evidenze conformi ad AVS.

## 11. Test proposti e criteri di accettazione

Tipo: **R** collaudo reale (V3) · **D** verifica documentale · **S** simulazione · **E** empirico umano.

| ID | Tipo | Obiettivo | Procedura sintetica | Criterio di accettazione |
|---|---|---|---|---|
| T-E07-01 | D | Scheda dei criteri di accessibilità e mobile | Redigere e approvare criteri, dispositivi e impostazioni iOS di riferimento | Ogni criterio con atteso misurabile e metodo; approvazione esplicita |
| T-E07-02 | R | Conformità delle schermate 4C | Su iPhone reale, schermo minimo e massimo supportati: VoiceOver, Zoom, Testo più grande al massimo, orizzontale, Riduci movimento, Aumenta contrasto | 0 fallimenti sui criteri approvati; deroghe motivate e registrate |
| T-E07-03 | R | Baseline 6.5.1 e RC1 | Collaudo in sola lettura su iPhone: installazione PWA, navigazione, safe area, VoiceOver, offline | Rapporto versionato con dispositivo, iOS, build ed esiti per voce |
| T-E07-04 | R | Reflow e ridimensionamento | Larghezza 320 px CSS e testo al 200% su teoria, codice, tabelle e dashboard | Nessuna perdita di contenuto o funzione salvo eccezioni documentate |
| T-E07-05 | R | Ripresa | Interruzione in ogni attività, chiusura forzata, riavvio, modalità aereo, rientro da link esterno | Stato ripristinato alla granularità dichiarata; zero perdite |
| T-E07-06 | R | Passaggio da Safari a PWA installata e aggiornamento | Avanzare in Safari, installare, aprire; poi aggiornare la versione | Progressi presenti o recupero guidato documentato; nessuna perdita silenziosa |
| T-E07-07 | R | Continuità iPhone↔computer | Backup cifrato su iPhone e ripristino su computer, e viceversa; registrazione di un'evidenza di laboratorio | Conteggi identici; evidenza collegata alla sessione corretta |
| T-E07-08 | D | Completezza ARTM per i dispositivi | Verificare i campi H, OS e parte H0 per 420 record | 420/420 compilati |
| T-E07-09 | R + S | Dichiarazione del dispositivo in UI | Percorso C06/B06 (S) e verifica su iPhone (R) | Segnalazione "Richiede computer" visibile e annunciata prima dell'avvio; nessuna scoperta tardiva |
| T-E07-10 | R | Contrasto dei token identitari | Misura del contrasto di tutte le coppie e degli indicatori | 100% conforme ai criteri approvati |
| T-E07-11 | R | Leggibilità di sessione lunga e codice | Sessione L3 completa su iPhone con VoiceOver e senza | Lettura sequenziale corretta; formule e codice comprensibili; posizione salvata |
| T-E07-12 | R | Navigazione | Flussi critici (onboarding, sessione, quiz, dizionario, backup, risorsa esterna) con touch e VoiceOver | Tutti completabili; ordine del focus coerente; rientro con stato conservato |
| T-E07-13 | R (+E se disponibile) | Distinguibilità degli indicatori | Lettura degli indicatori con VoiceOver e in scala di grigi | Ogni indicatore identificato correttamente senza colore; nessuna confusione avanzamento/competenza |
| T-E07-14 | D | Coerenza documentale | Confrontare le sezioni correnti e prevalenti con 3I; note di superamento; tabella R↔G | Nessuna contraddizione residua |
| T-E07-15 | R | Tempi delle verifiche | Diagnostica e quiz con VoiceOver e cambio app | Nessun timeout non regolabile; nessuna perdita di risposte |
| T-E07-16 | D | Livelli di evidenza | Verificare che ogni criterio E07 abbia il tipo minimo di evidenza | 100% marcati; nessuna chiusura con sola simulazione |
| T-E07-17 | E | Usabilità con utenti reali, anche utenti di tecnologie assistive | Solo se un giorno disponibile (oggi escluso da AMVP) | Fuori portata attuale: resta G12-E non verificata |

## 12. Simulazione, collaudo reale, efficacia empirica umana

- **Questa revisione** e le future simulazioni AMVP (C06, B06) sono **simulazioni AI**. Producono ipotesi e controlli di coerenza, non prove di usabilità, accessibilità o apprendimento.
- **Collaudo reale (V3):** esecuzione su iPhone fisico, con versione iOS e build registrate, da parte del team o dell'utente. Può chiudere criteri **tecnici** di accessibilità e mobile se sono predefiniti. Un collaudo con VoiceOver fatto da una persona vedente verifica il comportamento tecnico, **non** l'esperienza di chi usa VoiceOver ogni giorno.
- **Efficacia empirica umana (G12-E):** apprendimento, usabilità percepita, ritenzione e risultati su studenti reali, comprese persone con disabilità. Oggi **non è disponibile né verificata** e non può essere sostituita da nessuno dei due livelli precedenti.

## 13. Dichiarazioni finali

- Non ho modificato file né il repository, non ho chiuso gate e non ho autorizzato fasi.
- Non ho conosciuto né usato rapporti di altri revisori.
- Non ho ricostruito parti di immagini coperte o fuori inquadratura.
- I riferimenti normativi marcati [K] vanno confermati su fonti ufficiali datate prima di essere adottati.
- La conformità con gli SHA dichiarati riguarda **solo** i blob dei due file ricevuti. Il collegamento con il commit `f9d98c2bbd4d3622b9ccb5eeeb5c1811a2c4d401` non è verificabile in questa sede.
