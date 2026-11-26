# E07 — Analisi critica del coordinatore e decisione del titolare — 26/11/2026
Fonte originale: E07-original-report.md, commit d6742e111db7bc2898353a5205ce9c3d0aa80232, blob 431f92de2254c2eb7705bfdd505bd09e74f19632. PARZIALE, 17 osservazioni (0 P0,6 P1,7 P2,4 P3). Tutte aperte. Analisi preliminare, non trascrizione.

## Decisione del titolare approvata in chat
L'AI Creator Academy deve essere progettata secondo un approccio Mobile First, assumendo iPhone come piattaforma primaria di utilizzo, riferimento prioritario per l'esperienza utente e dispositivo di collaudo reale.

L'approccio Mobile First non deve tradursi in un'architettura Mobile Only.

Fin dalla progettazione iniziale, l'applicazione deve essere concepita per consentire l'accesso e la fruizione anche da dispositivi Android e computer, attraverso un'interfaccia responsive, accessibile e adattabile alle differenti modalità di interazione.

Le eventuali dipendenze specifiche di una piattaforma devono essere identificate, motivate e accompagnate, ove necessario, da alternative compatibili.

La progettazione deve preservare la continuità dello studio, i progressi, le attività, le valutazioni e le evidenze del portfolio, prevedendo modalità di trasferimento o ripristino tra dispositivi da sottoporre a verifica.

I laboratori che richiedono un computer, uno specifico sistema operativo o particolari requisiti hardware e software devono essere dichiarati preventivamente.

Il collaudo prioritario su iPhone non costituisce automaticamente prova di compatibilità effettiva con Android o computer, che dovrà essere verificata separatamente.

Nessuna compatibilità, accessibilità o efficacia formativa può essere dichiarata come dimostrata in assenza delle evidenze richieste.

## Valutazione critica
| ID | Priorità originale | Valutazione e verifica candidata |
|---|---|---|
| E07-A01 | P1 | Mappatura esplicita C08/accessibilità su R/G esistenti da valutare prima di proporre R13; nessuna modifica approvata. |
| E07-A02 | P1 | Definire soglie e matrice dispositivi; verificare WCAG 2.2 AA e Apple HIG su fonti ufficiali prima dell'adozione; non confondere CSS px e pt. |
| E07-A03 | P1 | Separazione storage Safari/PWA ipotesi, non difetto accertato; test su profili isolati e backup, nessuna modifica schema implicita. |
| E07-A04 | P1 | Campi H/OS e dichiarazione preventiva candidati; distinguere ARTM documentale da schema applicativo. |
| E07-A05 | P1 | Contraddizione da verificare sulle fonti comuni e correggere solo previa approvazione; checkpoint operativo aggiornato separatamente. |
| E07-A06 | P1 | Baseline iPhone reale da pianificare su dati di prova; non alterare main/RC1 o progressi reali. |
| E07-A07 | P2 | Recuperare immagini originali e token; non ricostruire parti coperte. |
| E07-A08 | P2 | Test reflow, codice, tabelle, formule e lettura assistiva; distinguere comportamento tecnico da comprensione umana. |
| E07-A09 | P2 | Mappa flussi critici e perimetro 4C da proporre, non ampliare automaticamente. |
| E07-A10 | P2 | Etichette semantiche e test senza colore, distinguere progresso/competenza. |
| E07-A11 | P2 | Chiarire stime e limiti temporali; verificare accomodamenti senza alterare validità delle prove. |
| E07-A12 | P2 | Evidenza minima per criterio; simulazione non sostituisce runtime, né runtime efficacia empirica. |
| E07-A13 | P2 | Mappatura molti-a-molti R/G e annotazioni storiche candidate. |
| E07-A14 | P3 | Decisione titolare: Android e PC considerati da subito; priorità originale conservata, eventuale nuova priorità da deliberare. |
| E07-A15 | P3 | Riduzione movimento, alternative ai gesti e tastiera da verificare. |
| E07-A16 | P3 | Touch e feedback accessibili; preservare indici quiz, valutare separatamente correlazione risposte. |
| E07-A17 | P3 | Verificare impostazioni visive e contrasto per piattaforma. |

Registro affermazioni pubbliche candidato, nessuna deroga AVS. La conformità tecnica accessibilità può essere valutata su perimetro definito senza inferire esperienza umana o efficacia formativa. Nessun test eseguito. Lettura analitica integrale delle fonti comuni ancora pendente. Nessuna modifica standard, gate, codice o protezioni.
