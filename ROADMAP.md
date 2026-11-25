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
| Quiz base Creator settimane 13–18 | 0/30 modificati rispetto a RC1 | Prossimo blocco |
| Quiz base Creator settimane 19–24 | 0/30 modificati rispetto a RC1 | Successivo |
| Quiz base Business | Avanzamento non verificato | Audit necessario |
| Revisione qualitativa delle lezioni | Da completare | Screenshot |
| Feedback individuali per risposte errate | Da completare | Screenshot; non assumere completati |
| Risorse esterne | Incompleta | Ultimo dato storico 6/30 indirizzi, da riconfermare |

Avanzamento quiz Creator base verificato: 60/120 (50%). Stima complessiva della revisione: 324/528 (61,4%), sommando 264 avanzati documentati e 60 base verificati; non equivale a qualità certificata né avanzamento dell'intero progetto. Il confronto ha trovato 60 oggetti knowledgeCheck distinti, non costituisce ancora verifica di unicità del solo testo delle domande, correttezza didattica o indici.

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
Creator settimane 13–18: AI Automation & Agents (13–15), AI Integration (16–18). Revisionare 30 quiz base, verificare unicità del testo, tre alternative, correttezza e indici invariati; preservare tutti gli altri campi. Obiettivo 90/120 base Creator. Poi settimane 19–24, audit e revisione Business, feedback, lezioni, link e collaudo. Sequenza successiva da confermare se emergono nuove dipendenze.

## Registro cronologico
- 25/11/2026: recuperata continuità della chat precedente tramite screenshot e confronto GitHub. Branch sviluppo risultava 27 commit avanti a main e divergente da RC1 (10 avanti, 1 indietro). Main osservato: cd19c06596a16fc8fc091a6ea7fd8fb7b00275b0; RC1 osservata: e4ee85918cadccd38499772827e663fef0c34fd5. Verificate modifiche knowledgeCheck per tutte le 60 sessioni Creator settimane 1–12, nessuna per 13–24 rispetto a RC1. Nessuna modifica applicativa in questa fase.
- 25/11/2026: istituito questo registro sul branch di sviluppo. Il commit del registro è consultabile nella cronologia del file.

## Procedura permanente
Prima di riprendere in una nuova chat leggere questo registro, README e stato reale dei branch. Dopo ogni blocco aggiornare il registro con data, branch, file modificati, commit applicativo, conteggi verificati, test realmente eseguiti/esiti, limiti e prossimo passo. Distinguere sempre dichiarato, documentato, verificato e non verificato. Non dichiarare salvataggio senza esito GitHub e SHA; rileggere i file dopo la scrittura. Non alterare la cronologia precedente: aggiungere nuove voci e aggiornare lo stato corrente.

Fonti: screenshot della conversazione precedente forniti dall'utente; README e curriculum Creator dei branch indicati; confronto https://github.com/itopo-ai/AI-Creator-Academy/compare/release-candidate-6.6-rc1...excellence-learning-6.6 .
