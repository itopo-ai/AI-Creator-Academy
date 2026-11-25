# AI Creator Academy — Registro permanente di roadmap e avanzamento

Aggiornato: 25 novembre 2026. Documento di continuità del progetto; non costituisce autorizzazione al rilascio.

## Roadmap concordata
| Versione | Obiettivo | Stato |
|---|---|---|
| 6.4.2 | Stabilità e funzionalità | Completata secondo roadmap storica |
| 6.5 | Revisione grafica e avanzamento percentuale | Completata secondo roadmap storica |
| 6.5.1 | Introduzioni ai concetti delle 264 lezioni | Produzione, da preservare |
| 6.6 / 6.6.1 | Excellence Learning: qualità didattica | In corso |
| 6.7 | Sicurezza, affidabilità e backup | Programmata |
| 7.0 | Versione definitiva | Obiettivo finale |

## Ambienti e vincoli
- main: 6.5.1, produzione; non modificare.
- excellence-learning-6.6: unico branch di lavoro per questa fase.
- release-candidate-6.6-rc1: candidata al rilascio, installata su iPhone secondo l'utente; non modificare. PR originale: https://github.com/itopo-ai/AI-Creator-Academy/pull/1
- Non modificare l'app originale Claude. Lavorare sui sorgenti GitHub, senza ZIP intermedi.
- Preservare ID, attività, progressi, punteggi, indici delle risposte corrette e sistema di migrazione. Non pubblicare né effettuare merge senza collaudo e approvazione dell'utente.

## Dimensioni e criteri didattici
Creator & Developer: 24 settimane, 120 sessioni, 240 quiz. Business & Management: 48 settimane, 144 sessioni, 288 quiz. Totale 264 sessioni e 528 quiz (264 base e 264 avanzati).
Linguaggio accessibile da zero, progressione graduale, domande concrete e contestuali, tre alternative distinte e plausibili, feedback specifico per ciascun errore, teoria collegata alla pratica, risorse autorevoli e verificate. Qualità prima della velocità.

## Stato al 25 novembre 2026
| Intervento | Stato | Evidenza |
|---|---|---|
| Introduzioni 264 lezioni | Documentato completato | README 6.5.1 |
| Dizionario IT & AI, 114 termini, ricerca, filtri e parole contestuali | Documentato/riportato implementato | README sviluppo e screenshot |
| Controllo strutturale 264 lezioni e 528 quiz | Riportato superato | README e screenshot; da riconfermare dopo modifiche |
| Quiz avanzati Creator 120 e Business 144 | Documentati revisionati | README sviluppo; audit integrale da eseguire |
| Quiz base Creator settimane 1–6 | 30 modificati | Confronto JSON sviluppo/RC1 |
| Quiz base Creator settimane 7–12 | 30 modificati | Confronto JSON sviluppo/RC1 |
| Quiz base Creator settimane 13–18 | 30/30 revisionati e riletti | Commit e69116fd4dbccad12928c6f05ad5253d6121e0fb |
| Quiz base Creator settimane 19–24 | 30/30 revisionati e riletti | Commit a84938c6230543edf7002b170c1ebe5bb8406a56 |
| Quiz base Business | 144/144 già modificati rispetto a RC1; 144/144 perfezionati in questa fase | Audit e commit 8d69001c19a12aa36ab7c8d2d669b02b24e96e86 |
| Revisione qualitativa delle lezioni | Da completare | Screenshot |
| Feedback individuali per risposte errate | Da completare | Screenshot; non assumere completati |
| Risorse esterne | Incompleta | Ultimo dato storico 6/30 indirizzi, da riconfermare |

Avanzamento quiz Creator base verificato: 120/120 (100%). Copertura delle modifiche/documentazione: 528/528 (264 avanzati documentati, 120 base Creator e 144 base Business modificati rispetto a RC1); perfezionamento secondo gli standard correnti: Business 144/144, nessun quiz base Business con feedback non distinti; non equivale a qualità certificata né avanzamento dell'intero progetto. Il confronto ha trovato 60 oggetti knowledgeCheck distinti, non costituisce ancora verifica di unicità del solo testo delle domande, correttezza didattica o indici.

## Collaudo e criteri di rilascio
Controlli storicamente dichiarati superati: integrità lezioni/quiz, sintassi JS, dizionario e ricerca, calcolo avanzamento, validazione strutturale backup, compatibilità strutturale 6.5.1, allineamento versione/cache, correzioni preventive UI. Non equivalgono a test end-to-end.
- [ ] Audit qualitativo completo e regressione dopo revisione quiz.
- [ ] Verifica integrale link e accessibilità corsi dopo login ove applicabile.
- [ ] JavaScript in esecuzione e navigazione browser.
- [ ] Safari/iPhone, interfaccia e installazione PWA.
- [ ] Offline e cache.
- [ ] Backup cifrato e ripristino effettivo.
- [ ] Aggiornamento dalla 6.5.1 e conservazione effettiva dei progressi.
- [ ] Aggiornamento automatico.
- [ ] Approvazione utente prima del rilascio.

## Prossimo intervento
Audit dei feedback base Creator, quindi audit dei 264 quiz avanzati, lezioni, link e collaudo. Sequenza successiva da confermare se emergono nuove dipendenze.

## Registro cronologico
- 25/11/2026: recuperata continuità della chat precedente tramite screenshot e confronto GitHub. Branch sviluppo risultava 27 commit avanti a main e divergente da RC1 (10 avanti, 1 indietro). Main osservato: cd19c06596a16fc8fc091a6ea7fd8fb7b00275b0; RC1 osservata: e4ee85918cadccd38499772827e663fef0c34fd5. Verificate modifiche knowledgeCheck per tutte le 60 sessioni Creator settimane 1–12, nessuna per 13–24 rispetto a RC1. Nessuna modifica applicativa in questa fase.
- 25/11/2026: istituito questo registro sul branch di sviluppo. Il commit del registro è consultabile nella cronologia del file.

## Procedura permanente
Prima di riprendere in una nuova chat leggere questo registro, README e stato reale dei branch. Dopo ogni blocco aggiornare il registro con data, branch, file modificati, commit applicativo, conteggi verificati, test realmente eseguiti/esiti, limiti e prossimo passo. Distinguere sempre dichiarato, documentato, verificato e non verificato. Non dichiarare salvataggio senza esito GitHub e SHA; rileggere i file dopo la scrittura. Non alterare la cronologia precedente: aggiungere nuove voci e aggiornare lo stato corrente.

Fonti: screenshot della conversazione precedente forniti dall'utente; README e curriculum Creator dei branch indicati; confronto https://github.com/itopo-ai/AI-Creator-Academy/compare/release-candidate-6.6-rc1...excellence-learning-6.6 .

### Avviso preventivo di continuità (25/11/2026)
L'utente richiede un avviso con tre messaggi di anticipo rispetto al limite della chat. Il contatore residuo non è disponibile: non promettere un anticipo esatto. Quando la conversazione appare lunga, avvisare preventivamente e proporre una nuova chat; aggiornare comunque il registro dopo ogni blocco e prima di ogni passaggio. Non affidarsi a un avviso automatico.

### Aggiornamento 25/11/2026 — Creator settimane 13–18
Commit applicativo: e69116fd4dbccad12928c6f05ad5253d6121e0fb. Revisionati 30 knowledgeCheck (5 per settimana): Automazioni, Agenti AI, Integrazioni MCP, API dei modelli, RAG e documenti, Valutazione e affidabilità. Feedback distinti per ogni alternativa nel nuovo blocco. Controlli eseguiti: 30 sessioni modificate, ID e indici corretti invariati per tutte le 120 sessioni, altri campi delle sessioni invariati, 90 testi di domanda distinti nelle prime 90, tre opzioni e tre feedback distinti per ciascuna delle 30 nuove domande. JSON riletto da GitHub e confrontato integralmente con il risultato atteso. Non eseguiti test browser, regressione funzionale o audit didattico indipendente. Nessun intervento su main, RC1, migrazione o pubblicazione. Prossimo blocco: settimane 19–24.

### Aggiornamento 25/11/2026 — Creator settimane 19–24
Commit curriculum: a84938c6230543edf7002b170c1ebe5bb8406a56. Revisionati 30 knowledgeCheck: Gestione professionale, Sicurezza e privacy, Qualità e rilascio, Progetto finale (definizione, sviluppo, pubblicazione). Verificati 120 testi di domanda base distinti, 30 sole sessioni modificate, indici delle risposte e altri campi delle 120 sessioni invariati, tre opzioni e tre feedback distinti per ogni nuovo quiz. JSON riletto e confrontato integralmente. Revisione base Creator 120/120; audit qualitativo indipendente, feedback precedenti e regressione funzionale ancora da completare. Nessuna modifica a main, RC1 o migrazione; nessuna pubblicazione. Prossimo passo: audit Business base.

### Aggiornamento 25/11/2026 — Audit Business e settimane 1–6
Audit: 144 knowledgeCheck modificati rispetto a RC1, 144 testi distinti; 141/144 avevano feedback non distinti. Perfezionati 18 quiz (AI foundations, ChatGPT e prompt avanzati, ChatGPT per il lavoro, agenti e workflow, GenAI per leader, casi d’uso e valore). Commit 8d69001c19a12aa36ab7c8d2d669b02b24e96e86. Verificati 18 sole sessioni modificate, indici e altri campi delle 144 sessioni invariati, 144 testi distinti, tre opzioni e tre feedback distinti per ciascuno dei 18 quiz; rilettura JSON integrale riuscita. Restano 126 quiz base Business con feedback non distinti. La precedente stima 384/528 sottostimava le modifiche già esistenti: copertura modifiche/documentazione 528/528 non significa qualità completata. Nessun test runtime o pubblicazione. Prossimo blocco Business settimane 7–12.

### Aggiornamento 25/11/2026 — Business settimane 7–12
Commit curriculum: 171d96ea0546cce61f7210e7b108790111a294c0. Perfezionati 18 quiz base: fattibilità e ROI, rischi, governance, cambiamento, completamento specializzazione IBM, business case AI. Verificati 144 testi distinti, 18 sole sessioni modificate, indici delle risposte e altri campi invariati, tre opzioni e tre feedback distinti per ogni nuovo quiz; rilettura integrale JSON riuscita. Business 36/144 (25%); 108 feedback ancora non distinti. Nessun test runtime o pubblicazione. Prossimo blocco settimane 13–18.

### Aggiornamento 25/11/2026 — Business settimane 13–18
Commit curriculum: a8d5d6392eb6bf3a8e707e2bd272dff44effeaf5. Perfezionati 18 quiz base su no-code foundations, applied no-code AI e guida della trasformazione. Verificati 144 testi distinti, 18 sole sessioni modificate, indici delle risposte e altri campi invariati, tre opzioni e tre feedback distinti per ogni nuovo quiz; rilettura integrale JSON riuscita. Business 54/144 (37,5%); 90 feedback ancora non distinti. Nessun test runtime o pubblicazione. Prossimo blocco settimane 19–24: pilota no-code e GA4.

### Aggiornamento 25/11/2026 — Business settimane 19–24
Commit curriculum: 02fa8c50453a357da4d535340586ef39db1fcd41. Perfezionati 18 quiz base su pilota no-code e GA4, inclusa distinzione tra rapporto acquisti/sessioni e tasso di sessioni con acquisto. Verificati 144 testi distinti, 18 sole sessioni modificate, indici delle risposte e altri campi invariati, tre opzioni e tre feedback distinti per ogni nuovo quiz; rilettura integrale JSON riuscita. Business 72/144 (50%); 72 feedback ancora non distinti. La teoria GA4 preesistente non è stata modificata e la terminologia delle conversioni va riesaminata nell’audit delle lezioni. Nessun test runtime o pubblicazione. Prossimo blocco settimane 25–30: Excel, Power BI, ETL e modellazione.

### Aggiornamento 25/11/2026 — Business settimane 25–30
Commit curriculum: 66fd844a41c7d3655cba2543d8cdd2c87237a821. Perfezionati 18 quiz base su Excel, riconciliazione, Power BI, ETL e modellazione. Verificati 144 testi distinti, 18 sole sessioni modificate, indici delle risposte e altri campi invariati, tre opzioni e tre feedback distinti per ogni nuovo quiz; rilettura integrale JSON riuscita. Business 90/144 (62,5%); 54 feedback ancora non distinti. Nessun test runtime o pubblicazione. Prossimo blocco settimane 31–36: DAX, analisi, visualizzazione, design, pubblicazione e PL-300.

### Aggiornamento 25/11/2026 — Business settimane 31–36
Commit curriculum: 0dabd422f4923b5d50822051fdd937a16b1f4f70. Perfezionati 18 quiz base su DAX, marginalità, segmentazione, budget, liquidità, permessi e progetto BI. Verificati 144 testi distinti, 18 sole sessioni modificate, indici delle risposte e altri campi invariati, tre opzioni e tre feedback distinti per ogni nuovo quiz; rilettura integrale JSON riuscita. Business 108/144 (75%); 36 feedback ancora non distinti. Nessun test runtime o pubblicazione; non verificato il programma ufficiale PL-300. Prossimo blocco settimane 37–42: Make e agenti AI.

### Aggiornamento 25/11/2026 — Business settimane 37–42
Commit curriculum: 8bde1334e4249764aad8dd79a1343ec44cd68622. Perfezionati 18 quiz base su Make, trigger, mappatura, filtri, retry, idempotenza e agenti AI. Verificati 144 testi distinti, 18 sole sessioni modificate, indici delle risposte e altri campi invariati, tre opzioni e tre feedback distinti per ogni nuovo quiz; rilettura integrale JSON riuscita. Business 126/144 (87,5%); 18 feedback ancora non distinti. Nessun test runtime o pubblicazione. Prossimo blocco settimane 43–48: agenti AI, Power Platform e PL-900.

### Aggiornamento 25/11/2026 — Business settimane 43–48
Commit curriculum: c8bda7710d904f3666bf91276fc443c319641c16. Perfezionati 18 quiz base su supervisione, monitoraggio, Power Platform, approvazioni, governance e piano trimestrale. Verificati 144 testi distinti, 18 sole sessioni modificate, indici delle risposte e altri campi invariati; tutti i 144 quiz Business hanno tre opzioni e tre feedback distinti. Rilettura integrale JSON riuscita. Business 144/144 (100%); revisione testi base complessiva 264/264, feedback Creator precedenti da auditare. Nessun test runtime o pubblicazione; programma ufficiale PL-900 non verificato. Prossimo intervento: audit feedback Creator e poi quiz avanzati.

### Aggiornamento 25/11/2026 — Audit Creator base e settimane 1–2
Branch: excellence-learning-6.6. Audit strutturale: 120 knowledgeCheck, 120 testi distinti, 60 con feedback duplicati (settimane 1–12), 60 con feedback distinti da valutare qualitativamente. Perfezionati 10 quiz delle settimane 1–2, esclusivamente feedback errati. File: curriculum-creator.json. Commit: a7f9ffe902337488fa4317f1fb835d6d9b3a392a. Verifica: confronto integrale degli oggetti JSON esclusi i 20 feedback modificati, tre feedback distinti per ciascuno dei 10 quiz, rilettura GitHub coincidente. Restano 50 quiz con feedback duplicati e audit qualitativo dei 60 già distinti. Nessun test runtime, merge o rilascio. Prossimo blocco: Creator settimane 3–6.

### Aggiornamento 25/11/2026 — Creator settimane 3–6
Branch: excellence-learning-6.6. File: curriculum-creator.json. Commit applicativo: 3d41ecefbec6ee337a4838dbc1c8368908b55011. Perfezionati 20 quiz base (40 feedback errati) su supervisione, progettazione, qualità, costi, identità visiva, UX e produzione creativa. Verificati 120 testi distinti, confronto integrale JSON con sole modifiche ai feedback errati delle 20 sessioni, tre feedback distinti per ciascuna, rilettura GitHub coincidente. Creator: 90/120 quiz con feedback distinti, 30 perfezionati nell'audit corrente; restano 30 con duplicati (settimane 7–12) e audit qualitativo dei 60 già distinti (13–24). Nessun test runtime, merge o rilascio; nessuna modifica a main, RC1, progressi o migrazione. Prossimo blocco: Creator settimane 7–12.
