# Corso 2 «AI per il business e i dati»: i 7 percorsi selezionati con ChatGPT, 48 settimane x 3 sessioni.
import json, sys

URL = {
 "oai": "https://academy.openai.com/pages/courses",
 "ibm": "https://www.coursera.org/specializations/generative-ai-for-executives-and-business-leaders",
 "ibm1": "https://www.coursera.org/learn/generative-ai-for-executives-business-leaders",
 "lq": "https://www.coursera.org/specializations/no-code-ai-for-business",
 "lq1": "https://www.coursera.org/learn/no-code-ai-foundations-for-business-professionals",
 "lq2": "https://www.coursera.org/learn/applied-no-code-ai-for-business-processes",
 "ga": "https://support.google.com/analytics/answer/15440208",
 "pbi": "https://www.coursera.org/professional-certificates/microsoft-power-bi-data-analyst",
 "mk": "https://academy.make.com/",
 "mkf": "https://academy.make.com/bundles/foundation",
 "mki": "https://academy.make.com/bundles/make-intermediate",
 "mka": "https://academy.make.com/bundles/automation-to-ai-agents-foundation",
 "mkadv": "https://academy.make.com/bundles/automation-to-ai-agents-advanced-builder",
 "pl": "https://learn.microsoft.com/training/paths/pl-900-power-platform-fundamentals/",
 "plg": "https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-900",
 "plp": "https://learn.microsoft.com/certifications/exams/pl-900/practice/assessment?assessment-type=practice&assessmentId=34",
}
PLAT = {
 "oai": "OpenAI Academy", "ibm": "IBM · GenAI for Executives (Coursera)", "lq": "LearnQuest · No-Code AI for Business (Coursera)",
 "ga": "Google Analytics Academy (Skillshop)", "pbi": "Microsoft Power BI Data Analyst (Coursera)", "mk": "Make Academy", "pl": "Microsoft Learn · PL-900",
}
def Q(q, opts, a, why): return {"q": q, "options": opts, "answer": a, "why": why}

PHASES = [
 {"n": 1, "title": "OpenAI Academy", "weeks": [1, 4], "goal": "Usare ChatGPT in modo professionale: fondamenti, prompt avanzati, agenti e flussi di lavoro."},
 {"n": 2, "title": "IBM · AI per il management", "weeks": [5, 12], "goal": "Strategia AI, valore di business, rischi, governance e gestione del cambiamento."},
 {"n": 3, "title": "No-Code AI for Business", "weeks": [13, 20], "goal": "Applicare l'AI senza codice ai processi aziendali, con KPI e miglioramento operativo."},
 {"n": 4, "title": "Google Analytics 4", "weeks": [21, 24], "goal": "Misurare traffico, comportamento degli utenti e conversioni di un sito o di un'app."},
 {"n": 5, "title": "Microsoft Power BI", "weeks": [25, 36], "goal": "Preparare, modellare e visualizzare dati aziendali con dashboard e report."},
 {"n": 6, "title": "Make Academy", "weeks": [37, 44], "goal": "Automazioni no-code tra applicazioni e agenti AI, dalle basi al livello avanzato."},
 {"n": 7, "title": "Microsoft Power Platform (PL-900)", "weeks": [45, 48], "goal": "Power Apps, Power Automate, Copilot Studio e preparazione all'esame PL-900."},
]

# Ogni unità = una settimana: (titolo, piattaforma, url, argomento A, argomento B, compito pratico, criteri, domande)
U = []
def unit(*a): U.append(a)

# ---- Fase 1 · OpenAI Academy (4 settimane)
unit("AI foundations", "oai", URL["oai"], "il corso «AI foundations»: come funziona l'AI e come usarla in modo responsabile", "la seconda parte di «AI foundations» e la verifica finale per il badge",
     "Scrivi una pagina «Le mie regole per usare l'AI al lavoro» con 5 regole su dati, verifica e responsabilità.",
     ["Ho 5 regole concrete", "Almeno una regola riguarda i dati riservati", "Ho ottenuto il badge AI foundations o so cosa mi manca"],
     [Q("Che punteggio serve nella verifica per ottenere un badge di OpenAI Academy?", ["Almeno 50%", "Almeno 80%", "100%", "Non serve una verifica"], 1, "Il badge certifica il completamento del corso e il superamento della verifica con almeno l'80%.")])
unit("Iniziare a usare ChatGPT e prompt avanzati", "oai", URL["oai"], "la sezione «Iniziare a usare ChatGPT»: prompting, strumenti e uso quotidiano", "le tecniche avanzate: contesto, esempi, formato, revisione e iterazione",
     "Crea 5 prompt modello per attività ricorrenti del tuo lavoro e provali in ChatGPT e in Claude.",
     ["Ogni prompt ha contesto, compito, formato e criteri", "Li ho provati su due assistenti", "Ho annotato quale funziona meglio e perché"],
     [Q("Quale elemento migliora di più una richiesta generica?", ["Scriverla in maiuscolo", "Aggiungere contesto, obiettivo e formato desiderato", "Renderla più corta possibile", "Ripeterla tre volte"], 1, "Contesto, obiettivo e formato riducono le ipotesi del modello.")])
unit("ChatGPT per il lavoro", "oai", URL["oai"], "la sezione «ChatGPT per il lavoro»: come i team lo usano nei diversi ruoli", "i casi d'uso più vicini al tuo settore e le buone pratiche di condivisione nel team",
     "Mappa 8 attività del tuo lavoro e indica per ognuna: l'AI la fa, l'AI aiuta, resta umana.",
     ["La mappa ha 8 attività", "Ogni decisione è motivata", "Ho scelto 2 attività da migliorare subito"],
     [Q("Quale attività conviene delegare per prima all'AI?", ["Una decisione strategica irreversibile", "Un compito ripetitivo, facile da verificare", "Un contratto senza rileggerlo", "La firma di un documento"], 1, "Si parte da compiti ripetitivi e verificabili, dove l'errore costa poco.")])
unit("Agenti e flussi di lavoro", "oai", URL["oai"], "i corsi «Applied AI foundations» e «Agents & workflows»: dai singoli prompt ai flussi ripetibili", "come dirigere un agente, rivedere i risultati e mantenere il controllo",
     "Trasforma un'attività ricorrente in un flusso di 4 passaggi con l'AI, con almeno un controllo umano.",
     ["Il flusso ha input, passaggi, controllo e risultato", "L'ho eseguito su un caso reale", "Ho misurato il tempo prima e dopo"],
     [Q("Che cosa distingue un flusso di lavoro ripetibile da un singolo prompt?", ["È più lungo", "Ha passaggi definiti che si possono rieseguire con risultati coerenti", "Usa solo immagini", "Non richiede verifiche"], 1, "Un flusso standardizza i passaggi e rende il risultato prevedibile.")])

# ---- Fase 2 · IBM (8 settimane)
unit("GenAI per i leader: introduzione", "ibm", URL["ibm1"], "il corso «GenAI for Executives & Business Leaders: An Introduction»: storia e impatto della GenAI sul business", "gli approcci per adottare la GenAI in azienda e il ruolo dei dati",
     "Scrivi una pagina su come la GenAI può creare valore nella tua attività (o nel progetto Diario di Viaggio).",
     ["Ho individuato 3 fonti di valore concrete", "Ho indicato quali dati servono", "Ho scritto un rischio principale"],
     [Q("Secondo il percorso IBM, perché i dati sono centrali per l'AI in azienda?", ["Perché rendono l'AI gratuita", "Perché la qualità e la disponibilità dei dati determinano il valore che l'AI può generare", "Perché sostituiscono la strategia", "Non sono importanti"], 1, "Il valore dell'AI aziendale dipende da dati pertinenti, di qualità e governati.")])
unit("Casi d'uso e valore di business", "ibm", URL["ibm"], "i casi d'uso principali come assistenza clienti e modernizzazione delle applicazioni", "come stimare il valore (tempo, costi, qualità) di un caso d'uso",
     "Scegli 3 casi d'uso per la tua attività e stima per ciascuno beneficio e sforzo da 1 a 5.",
     ["Ho 3 casi d'uso con beneficio e sforzo", "Ho scelto il caso con il miglior rapporto", "Ho scritto come misurerei il successo"],
     [Q("Come scegli il primo caso d'uso AI da avviare?", ["Il più costoso", "Quello con alto beneficio, sforzo contenuto e risultati misurabili", "Quello più di moda", "A caso"], 1, "Un primo successo misurabile crea fiducia per i progetti successivi.")])
unit("Fattibilità e ritorno dell'investimento", "ibm", URL["ibm"], "i fattori per valutare la fattibilità di un progetto AI", "come impostare il calcolo del ritorno dell'investimento (ROI)",
     "Prepara una scheda di fattibilità per il caso d'uso scelto: dati, competenze, costi, tempi, ROI stimato.",
     ["La scheda ha tutte e 5 le voci", "Il ROI ha numeri e ipotesi dichiarate", "Ho indicato cosa farebbe fallire il progetto"],
     [Q("Come si calcola in modo semplice il ROI di un progetto?", ["(Benefici − costi) ÷ costi", "Costi × 2", "Benefici − tempo", "Numero di utenti ÷ costi"], 0, "Il ROI confronta il guadagno netto con l'investimento sostenuto.")])
unit("Rischi e output affidabili", "ibm", URL["ibm"], "come mitigare i rischi di implementazione dell'AI", "le buone pratiche per ottenere output validi e utili",
     "Crea un registro rischi del tuo progetto AI: 6 rischi con probabilità, impatto e contromisura.",
     ["Ci sono 6 rischi", "Ognuno ha probabilità, impatto e contromisura", "Almeno uno riguarda errori o allucinazioni del modello"],
     [Q("Qual è una buona pratica per output AI affidabili in azienda?", ["Pubblicare senza rileggere", "Prevedere verifiche umane e fonti per i contenuti critici", "Usare un solo prompt per tutto", "Nascondere che si usa l'AI"], 1, "La revisione umana e le fonti riducono gli errori nei contenuti che contano.")])
unit("Fiducia, trasparenza e governance", "ibm", URL["ibm"], "l'importanza di fiducia, trasparenza e governance", "i principi di AI responsabile e chi deve decidere cosa in azienda",
     "Scrivi una policy di una pagina sull'uso dell'AI per il tuo team: cosa si può fare, cosa no, chi approva.",
     ["La policy dice quali dati non usare", "Indica chi approva i nuovi usi", "È comprensibile da un collega non tecnico"],
     [Q("A cosa serve la governance dell'AI in un'organizzazione?", ["A vietare l'AI", "A stabilire regole, responsabilità e controlli per un uso sicuro e coerente", "A comprare più licenze", "Solo all'ufficio legale"], 1, "La governance definisce chi decide, con quali regole e come si controlla.")])
unit("Gestione del cambiamento", "ibm", URL["ibm"], "come guidare le persone nell'adozione dell'AI", "come comunicare il cambiamento e gestire le resistenze",
     "Prepara un piano di adozione in 5 passi per introdurre uno strumento AI nel tuo team.",
     ["Il piano ha 5 passi con tempi", "Prevede formazione per le persone", "Indica come raccogliere i riscontri"],
     [Q("Qual è la causa più comune di fallimento nell'adozione dell'AI?", ["La tecnologia troppo veloce", "Le persone non coinvolte né formate", "Troppi dati", "Lo schermo piccolo"], 1, "Senza coinvolgimento e formazione, anche lo strumento migliore resta inutilizzato.")])
unit("Completamento della specializzazione IBM", "ibm", URL["ibm"], "i moduli rimanenti della specializzazione", "la revisione dei laboratori e delle verifiche per il certificato",
     "Completa la specializzazione e scarica il certificato.",
     ["Ho completato tutti i corsi della serie", "Ho il certificato", "Ho annotato i 5 concetti più utili"],
     [Q("Hai finito la specializzazione. Qual è il passo più utile adesso?", ["Dimenticarla", "Applicare subito un concetto a un progetto reale", "Ricominciare da capo", "Cambiare argomento"], 1, "Applicare subito consolida l'apprendimento.")])
unit("Progetto di fase: il business case AI", "ibm", URL["ibm"], "il ripasso di valore, fattibilità, rischi e governance", "la struttura di un business case convincente",
     "Scrivi il business case completo di un progetto AI (2 pagine) e presentalo a una persona.",
     ["Contiene problema, soluzione, ROI, rischi e piano", "L'ho presentato a una persona reale", "Ho raccolto e annotato le sue obiezioni"],
     [Q("Che cosa rende convincente un business case?", ["Tante parole tecniche", "Un problema chiaro, numeri verificabili e rischi gestiti", "Più slide possibili", "Promesse senza numeri"], 1, "Chi decide vuole capire problema, valore e rischi.")])

# ---- Fase 3 · LearnQuest (8 settimane)
unit("No-Code AI Foundations (1)", "lq", URL["lq1"], "il primo modulo di «No-Code AI Foundations for Business Professionals»: dai problemi aziendali alle soluzioni no-code", "come abbinare un problema allo strumento no-code giusto",
     "Elenca 5 problemi del tuo lavoro e abbina a ciascuno un tipo di soluzione AI no-code.",
     ["Ho 5 problemi concreti", "Ogni problema ha una soluzione abbinata", "Ho scelto il problema su cui lavorare in questa fase"],
     [Q("Da dove parte un buon progetto di AI no-code?", ["Dallo strumento più famoso", "Da un problema aziendale concreto e misurabile", "Dal budget massimo", "Da un video virale"], 1, "Il problema guida la scelta dello strumento, non il contrario.")])
unit("No-Code AI Foundations (2)", "lq", URL["lq1"], "il modulo su come promuovere l'AI in azienda e ottenere il consenso", "come costruire il caso per un progetto no-code e gestire la resistenza culturale",
     "Prepara un messaggio di 10 righe per convincere il tuo responsabile (o un socio) a provare il progetto scelto.",
     ["Il messaggio ha problema, soluzione e beneficio", "Anticipa un'obiezione", "Chiede un'azione precisa"],
     [Q("Come si ottiene più facilmente il consenso per un progetto AI?", ["Imponendolo", "Mostrando un beneficio misurabile con un piccolo pilota", "Promettendo risultati enormi", "Evitando di parlarne"], 1, "Un pilota piccolo e misurabile riduce il rischio percepito.")])
unit("Applied No-Code AI (1)", "lq", URL["lq2"], "il corso «Applied No-Code AI for Business Processes»: automazione e innovazione con piattaforme no-code", "come scegliere i KPI per misurare un processo",
     "Disegna il processo scelto com'è oggi e definisci 3 KPI per misurarlo.",
     ["Il processo è disegnato passo per passo", "Ho 3 KPI con unità di misura", "Ho il valore attuale di almeno un KPI"],
     [Q("Che cos'è un KPI?", ["Un software", "Un indicatore chiave che misura le prestazioni rispetto a un obiettivo", "Un tipo di grafico", "Un modello AI"], 1, "Key Performance Indicator: un numero che dice se stai raggiungendo l'obiettivo.")])
unit("Applied No-Code AI (2)", "lq", URL["lq2"], "la parte del corso su bias, conformità e trasparenza", "come misurare i risultati e guidare progetti sostenibili",
     "Ridisegna il processo con l'AI e indica dove servono controlli su bias e privacy.",
     ["Il nuovo processo è disegnato", "Ci sono almeno 2 punti di controllo", "Ho stimato il miglioramento dei KPI"],
     [Q("Perché controllare i bias in un processo con AI?", ["Per rallentarlo", "Perché l'AI può produrre decisioni ingiuste se i dati sono sbilanciati", "Per obbligo di marketing", "Non serve"], 1, "Dati sbilanciati portano a risultati sbilanciati.")])
unit("Guidare la trasformazione (1)", "lq", URL["lq"], "il corso «Lead the AI-Enabled Business Transformation»: allineare team di business e tecnici", "come mettere il cliente al centro dell'innovazione con l'AI",
     "Organizza una sessione di 30 minuti con 2 persone per raccogliere idee sul tuo processo.",
     ["Ho fatto la sessione", "Ho raccolto almeno 5 idee", "Ho scelto 1 idea da integrare"],
     [Q("Perché coinvolgere chi usa davvero il processo?", ["Per riempire il calendario", "Perché conosce i problemi reali e adotterà più volentieri la soluzione", "Non serve", "Per dividere i costi"], 1, "Chi lavora nel processo vede problemi e soluzioni che dall'alto sfuggono.")])
unit("Guidare la trasformazione (2)", "lq", URL["lq"], "come scalare i progetti AI con governance e conformità fin dalla progettazione", "come completare la specializzazione e ottenere il certificato",
     "Completa la specializzazione e scrivi un piano per estendere il progetto ad altri 2 processi.",
     ["Ho il certificato LearnQuest", "Il piano indica 2 processi nuovi", "Il piano prevede regole di governance"],
     [Q("Che cosa significa «compliance by design»?", ["Pensare alle regole solo dopo il lancio", "Integrare le regole di conformità fin dalla progettazione", "Ignorare le regole", "Delegare tutto all'ufficio legale alla fine"], 1, "Progettare già conformi costa meno che correggere dopo.")])
unit("Pilota no-code (costruzione)", "lq", URL["lq"], "il ripasso dei moduli pratici della specializzazione", "la scelta di uno strumento no-code per il pilota (ad esempio Make, Zapier o le funzioni AI dei fogli di calcolo)",
     "Costruisci un pilota del processo migliorato con uno strumento no-code.",
     ["Il pilota funziona dall'inizio alla fine", "L'ho provato su 3 casi reali", "Ho annotato gli errori"],
     [Q("Che cos'è un pilota?", ["La versione finale", "Una prova su piccola scala per verificare che la soluzione funzioni", "Un manuale", "Un corso"], 1, "Il pilota riduce il rischio prima di investire di più.")])
unit("Progetto di fase: risultati del pilota", "lq", URL["lq"], "il ripasso di KPI e misura dei risultati", "come raccontare i risultati con dati e storia",
     "Misura i KPI dopo il pilota e presenta i risultati in una pagina con un grafico.",
     ["Ho KPI prima e dopo", "C'è un grafico chiaro", "Ho scritto la decisione: continuare, cambiare o fermarsi"],
     [Q("Il pilota migliora un KPI ma ne peggiora un altro. Cosa fai?", ["Nascondo il secondo", "Lo riporto e valuto se il beneficio complessivo giustifica il compromesso", "Fermo tutto", "Cambio KPI"], 1, "Una valutazione onesta considera tutti gli effetti.")])

# ---- Fase 4 · Google Analytics 4 (4 settimane)
unit("GA4: le basi", "ga", URL["ga"], "il primo corso di Analytics Academy su Skillshop: come funziona GA4", "la differenza tra utenti, sessioni ed eventi",
     "Crea un account GA4 dimostrativo (Google offre un account demo) ed esplora i report principali.",
     ["Ho aperto l'account demo", "Ho trovato utenti, sessioni ed eventi", "Ho annotato 3 dati interessanti"],
     [Q("Su cosa si basa la raccolta dati di GA4?", ["Solo sulle visite alle pagine", "Sugli eventi", "Sulle email", "Sui file di log del server"], 1, "In GA4 ogni interazione è un evento, comprese le visualizzazioni di pagina.")])
unit("GA4: raccolta e configurazione dei dati", "ga", URL["ga"], "il corso su come impostare una proprietà e raccogliere i dati necessari", "eventi consigliati, eventi personalizzati e conversioni (eventi chiave)",
     "Progetta gli eventi da misurare per il Diario di Viaggio (es. nuovo_giorno, foto_aggiunta, backup).",
     ["Ho almeno 6 eventi con nome e scopo", "Ho indicato quali sono eventi chiave", "Ho indicato quali dati NON raccogliere per privacy"],
     [Q("Che cosa sono gli eventi chiave (conversioni) in GA4?", ["Eventi che segni come importanti per i tuoi obiettivi di business", "Tutte le visite", "Gli errori del sito", "I clic sui menu"], 0, "Sono le azioni che contano di più per il tuo obiettivo, come un acquisto o un'iscrizione.")])
unit("GA4: report e analisi", "ga", URL["ga"], "il corso sui report e sugli strumenti di analisi", "le esplorazioni e come trovare risposte a domande di business",
     "Nell'account demo rispondi a 3 domande: da dove arrivano gli utenti, quali pagine funzionano, dove si perdono.",
     ["Ho risposto a 3 domande con i dati", "Ho usato almeno un'esplorazione", "Ho proposto un'azione per ogni risposta"],
     [Q("Vuoi capire dove gli utenti abbandonano un percorso. Quale analisi usi?", ["Un'esplorazione a imbuto", "Il numero totale di utenti", "La lista delle pagine", "Il colore del sito"], 0, "L'imbuto mostra quanti passano da un passaggio al successivo.")])
unit("GA4: certificazione", "ga", URL["ga"], "il ripasso degli argomenti dei 4 corsi", "la verifica per la Google Analytics Certification su Skillshop",
     "Sostieni la verifica di certificazione Google Analytics.",
     ["Ho ripassato tutti i corsi", "Ho sostenuto la verifica", "Ho la certificazione o so cosa ripassare"],
     [Q("Dove si ottiene la certificazione Google Analytics?", ["Su Skillshop, la piattaforma di formazione di Google", "In una università", "In un negozio", "Su un forum"], 0, "La verifica si svolge online su Skillshop.")])

# ---- Fase 5 · Power BI (12 settimane)
pbi = [
 ("Preparare i dati con Excel (1)", "il corso «Preparing Data for Analysis with Microsoft Excel»: formule e funzioni più comuni", "pulizia dei dati, formattazione e tabelle",
  "Prendi un tuo foglio di dati (es. le spese del viaggio) e puliscilo: colonne coerenti, date corrette, niente duplicati.",
  ["I dati sono in una tabella pulita", "Non ci sono duplicati", "Ho usato almeno 3 funzioni"],
  Q("Quale funzione di Excel somma solo le righe che rispettano una condizione?", ["SOMMA", "SOMMA.SE", "MEDIA", "CONTA.VALORI"], 1, "SOMMA.SE (SUMIF) somma i valori che soddisfano un criterio.")),
 ("Preparare i dati con Excel (2)", "la seconda parte del corso su Excel: funzioni di ricerca e analisi", "tabelle pivot e grafici",
  "Crea una tabella pivot delle spese per categoria e un grafico.",
  ["La pivot riassume per categoria", "Il grafico è leggibile", "Ho verificato a mano un totale"],
  Q("A cosa serve una tabella pivot?", ["A riassumere e raggruppare grandi quantità di dati", "A disegnare", "A scrivere testo", "A proteggere il file"], 0, "La pivot aggrega i dati per categorie in pochi clic.")),
 ("Il potere dei dati con Power BI", "il corso «Harnessing the Power of Data with Power BI»: il ruolo del data analyst", "i componenti di Power BI: Desktop, servizio e app per dispositivi mobili",
  "Installa Power BI Desktop (su PC Windows) o usa il servizio online e importa il tuo foglio pulito.",
  ["Power BI è pronto", "Ho importato i miei dati", "Ho creato un primo grafico"],
  Q("Qual è la differenza tra Power BI Desktop e il servizio Power BI?", ["Nessuna", "Desktop serve a creare report, il servizio online a pubblicarli e condividerli", "Il servizio è solo per Mac", "Desktop è solo per stampare"], 1, "Si crea in Desktop e si condivide nel servizio.")),
 ("Estrarre, trasformare e caricare (1)", "il corso «Extract, Transform and Load Data in Power BI»: le origini dati", "Power Query e le prime trasformazioni",
  "Con Power Query collega due origini dati diverse e unisci i dati.",
  ["Ho collegato 2 origini", "Ho unito o accodato le tabelle", "Ho documentato i passaggi applicati"],
  Q("Che cosa significa ETL?", ["Extract, Transform, Load: estrarre, trasformare e caricare i dati", "Email, Testo, Link", "Errore, Test, Lancio", "Un tipo di grafico"], 0, "È il processo che porta i dati grezzi in forma utilizzabile.")),
 ("Estrarre, trasformare e caricare (2)", "la seconda parte del corso ETL: profilazione e qualità dei dati", "gestione di errori e valori mancanti",
  "Profila i tuoi dati e correggi errori e valori mancanti.",
  ["Ho usato la profilazione delle colonne", "Ho gestito i valori mancanti", "Ho annotato le scelte fatte"],
  Q("Perché profilare i dati prima dell'analisi?", ["Per renderli più pesanti", "Per scoprire errori, valori mancanti e anomalie", "Per cambiare colore", "Non serve"], 1, "Dati sporchi portano a conclusioni sbagliate.")),
 ("Modellare i dati (1)", "il corso «Data Modeling in Power BI»: tabelle dei fatti e delle dimensioni", "relazioni e schema a stella",
  "Organizza i tuoi dati in uno schema a stella con una tabella dei fatti e almeno 2 dimensioni.",
  ["Ho una tabella dei fatti", "Ho almeno 2 dimensioni collegate", "Le relazioni funzionano nei grafici"],
  Q("In uno schema a stella, che cosa contiene la tabella dei fatti?", ["Le misure, come importi e quantità", "Solo i nomi delle categorie", "Le immagini", "Le password"], 0, "I fatti contengono i numeri; le dimensioni descrivono chi, cosa, quando.")),
 ("Modellare i dati (2): DAX", "la parte del corso dedicata alle formule DAX", "misure, colonne calcolate e funzioni temporali",
  "Crea 3 misure DAX: totale, media e variazione rispetto al mese precedente.",
  ["Ho 3 misure funzionanti", "Ho verificato un risultato a mano", "Ho spiegato a parole ogni formula"],
  Q("Che cosa calcola la misura DAX SUM(Spese[Importo])?", ["Il numero di righe", "La somma della colonna Importo", "La media", "Il valore massimo"], 1, "SUM somma tutti i valori della colonna indicata.")),
 ("Analizzare e visualizzare (1)", "il corso «Data Analysis and Visualization with Power BI»: scegliere il grafico giusto", "filtri, slicer e interazioni",
  "Costruisci una pagina di report con 4 grafici e uno slicer per periodo.",
  ["Ogni grafico risponde a una domanda", "Lo slicer filtra tutta la pagina", "Il report si capisce senza spiegazioni"],
  Q("Vuoi mostrare l'andamento delle spese nel tempo. Quale grafico scegli?", ["Torta", "Linee", "Mappa", "Tabella senza ordine"], 1, "Il grafico a linee mostra bene i cambiamenti nel tempo.")),
 ("Analizzare e visualizzare (2)", "la seconda parte del corso: analisi avanzate e insight", "Copilot e le funzioni AI di Power BI (modulo facoltativo sulla GenAI)",
  "Aggiungi al report un'analisi delle anomalie o delle tendenze e scrivi 3 insight.",
  ["Ho 3 insight scritti", "Ogni insight è supportato da un grafico", "Ho indicato un'azione per ciascuno"],
  Q("Che cos'è un insight?", ["Un grafico colorato", "Una scoperta utile dai dati che porta a una decisione", "Un errore", "Un filtro"], 1, "Un insight risponde a «e quindi?».")),
 ("Design dei report", "il corso «Creative Designing in Power BI»: layout, colori e accessibilità", "storytelling con i dati",
  "Ridisegna il report con una gerarchia chiara: numero chiave in alto, dettagli sotto.",
  ["Il messaggio principale si legge in 5 secondi", "I colori hanno un significato", "Il report è leggibile anche da telefono"],
  Q("Qual è una buona regola di design per un dashboard?", ["Usare più colori possibile", "Mettere in alto le informazioni più importanti", "Riempire ogni spazio", "Usare caratteri diversi in ogni grafico"], 1, "Chi legge guarda prima in alto a sinistra.")),
 ("Pubblicare e mantenere", "il corso «Deploy and Maintain Power BI Assets»: workspace, condivisione e aggiornamento", "sicurezza a livello di riga e progetto finale",
  "Pubblica il report nel servizio Power BI e imposta l'aggiornamento dei dati.",
  ["Il report è pubblicato", "L'aggiornamento è configurato", "Ho deciso chi può vederlo"],
  Q("A cosa serve la sicurezza a livello di riga (RLS)?", ["A far vedere a ogni utente solo i dati di sua competenza", "A cambiare i colori", "A velocizzare il report", "A stampare"], 0, "Con RLS lo stesso report mostra dati diversi a persone diverse.")),
 ("Preparazione PL-300 e progetto finale", "il corso di preparazione all'esame PL-300", "il capstone del certificato professionale",
  "Completa il capstone e decidi se sostenere l'esame PL-300 (con lo sconto del 50% per chi completa il certificato).",
  ["Ho completato il capstone", "Ho il certificato professionale", "Ho deciso data o rinuncia all'esame con un motivo"],
  Q("Che cosa offre il certificato professionale per l'esame PL-300?", ["L'esame gratis", "Uno sconto del 50% sull'esame", "Nessun vantaggio", "Un abbonamento Office"], 1, "Chi completa il programma riceve un voucher di sconto del 50%.")),
]
for t, a, b, task, crit, q in pbi: unit(t, "pbi", URL["pbi"], a, b, task, crit, [q])

# ---- Fase 6 · Make Academy (8 settimane)
unit("Make Foundation (1)", "mk", URL["mkf"], "il percorso «Make Foundation»: scenari, moduli e mappatura dei dati", "l'interfaccia degli scenari e il primo scenario",
     "Crea un account gratuito su Make e costruisci il tuo primo scenario con 2 moduli.",
     ["L'account è attivo", "Lo scenario gira senza errori", "So spiegare cosa fa ogni modulo"],
     [Q("In Make, che cos'è uno scenario?", ["Un'automazione composta da moduli collegati", "Un tipo di account", "Un grafico", "Un'email"], 0, "Lo scenario è il flusso di lavoro automatico.")])
unit("Make Foundation (2)", "mk", URL["mkf"], "routing, filtri e organizzazione", "operazioni e crediti: come si consumano",
     "Aggiungi al tuo scenario un router con un filtro e stima quanti crediti consuma al mese.",
     ["Il router divide i casi correttamente", "Il filtro funziona", "Ho stimato il consumo di crediti"],
     [Q("A cosa serve un router in Make?", ["A dividere il flusso in più percorsi", "A cancellare dati", "A collegare il Wi-Fi", "A pagare"], 0, "Il router manda i dati su percorsi diversi in base alle condizioni.")])
unit("Make Basics", "mk", URL["mk"], "il percorso «Make Basics»: moduli e manipolazione dei dati", "aggregatori e iteratori",
     "Costruisci uno scenario che raccoglie più righe e le riassume in un unico messaggio.",
     ["Ho usato un aggregatore", "Il risultato è un unico messaggio riassuntivo", "Ho provato con almeno 5 righe"],
     [Q("Che cosa fa un aggregatore in Make?", ["Unisce più elementi in uno solo", "Divide un testo", "Crea un account", "Cancella lo scenario"], 0, "L'aggregatore combina più record in uno.")])
unit("Make Intermediate (1)", "mk", URL["mki"], "il percorso «Make Intermediate»: JSON e array", "webhook per ricevere dati in tempo reale",
     "Crea uno scenario attivato da un webhook che riceve dati e li salva in un foglio.",
     ["Il webhook riceve dati", "I dati finiscono nel foglio", "Ho provato con 3 invii"],
     [Q("Che cos'è un webhook?", ["Un indirizzo che riceve dati in tempo reale quando succede un evento", "Un tipo di virus", "Una password", "Un filtro antispam"], 0, "Il webhook fa partire lo scenario appena arriva un dato.")])
unit("Make Intermediate (2)", "mk", URL["mki"], "gestione degli errori", "funzioni per date, condizioni e testi",
     "Aggiungi la gestione degli errori al tuo scenario e prova un caso che fallisce.",
     ["Lo scenario gestisce un errore senza bloccarsi", "Ricevo un avviso in caso di errore", "Ho completato il badge Intermediate o so cosa manca"],
     [Q("Perché gestire gli errori in un'automazione?", ["Per evitare che si blocchi in silenzio e perda dati", "Per renderla più lenta", "Non serve", "Per consumare crediti"], 0, "Un errore non gestito può fermare tutto senza che nessuno se ne accorga.")])
unit("Automation to AI Agents: Foundation (1)", "mk", URL["mka"], "il percorso «Automation to AI Agents: Foundation»: concetti di AI e modelli", "i moduli AI di Make (AI toolkit e AI Content Extractor)",
     "Crea uno scenario che usa un modulo AI per riassumere o classificare testi.",
     ["Il modulo AI dà risultati utili", "Ho scritto un prompt chiaro nel modulo", "Ho verificato 5 risultati a mano"],
     [Q("Quando conviene usare un modulo AI in uno scenario?", ["Quando servono comprensione o classificazione di testi non strutturati", "Per sommare due numeri", "Sempre", "Mai"], 0, "Per calcoli semplici bastano le funzioni normali; l'AI serve per il linguaggio.")])
unit("Automation to AI Agents: Foundation (2)", "mk", URL["mka"], "componenti e funzionamento degli agenti AI", "il primo agente in Make e la verifica del percorso",
     "Costruisci un agente AI semplice con 2 strumenti e completa il badge AI Automation Explorer.",
     ["L'agente usa 2 strumenti", "Ho definito limiti chiari", "Ho il badge o so cosa manca"],
     [Q("Che cosa distingue un agente AI da uno scenario normale?", ["Decide da solo quali strumenti usare per raggiungere un obiettivo", "È più colorato", "Non usa dati", "Funziona solo di notte"], 0, "Lo scenario segue passi fissi; l'agente sceglie i passi.")])
unit("Automation to AI Agents: Advanced", "mk", URL["mkadv"], "il percorso «Automation to AI Agents: Advanced»: strumenti avanzati per agenti", "prompt strategici a più livelli, scelta del modello e sicurezza",
     "Migliora il tuo agente con prompt più solidi e regole di sicurezza; completa il badge AI Agent Builder.",
     ["L'agente è più affidabile su 5 prove", "Ho regole su cosa non può fare", "Ho il badge o so cosa manca"],
     [Q("Qual è una buona regola di sicurezza per un agente?", ["Dare accesso a tutto", "Concedere solo gli strumenti e i dati strettamente necessari", "Condividere le password", "Togliere i controlli"], 1, "Il minimo accesso necessario riduce i danni possibili.")])

# ---- Fase 7 · PL-900 (4 settimane)
unit("Power Platform: valore e componenti", "pl", URL["pl"], "il percorso Microsoft Learn sui fondamenti di Power Platform: componenti e valore di business", "Microsoft Dataverse: come i dati sono strutturati e governati",
     "Scrivi per ciascun componente (Power Apps, Power Automate, Power BI, Power Pages, Copilot Studio) un esempio d'uso nel tuo lavoro.",
     ["Ho un esempio per ogni componente", "Ho indicato quale userei per primo", "Ho collegato almeno un esempio a Microsoft 365"],
     [Q("Quale componente di Power Platform serve a costruire siti web esterni?", ["Power Pages", "Power BI", "Power Automate", "Dataverse"], 0, "Power Pages serve a creare siti web, anche per utenti esterni.")])
unit("Power Apps e Power Automate", "pl", URL["pl"], "Power Apps: app canvas e model-driven con Copilot", "Power Automate: flussi cloud e automazioni",
     "Crea un flusso semplice in Power Automate (es. salvare gli allegati delle email in OneDrive).",
     ["Il flusso funziona", "So distinguere app canvas e model-driven", "Ho annotato le differenze con Make"],
     [Q("A cosa serve Power Automate?", ["A creare flussi che automatizzano attività tra app e servizi", "A disegnare loghi", "A scrivere codice Python", "A tradurre"], 0, "Power Automate è lo strumento di automazione della piattaforma.")])
unit("Copilot Studio e amministrazione", "pl", URL["pl"], "Copilot Studio: creare e pubblicare agenti AI", "governance e sicurezza della piattaforma tra ambienti",
     "Crea un agente semplice in Copilot Studio (versione di prova) che risponde a domande su un tuo documento.",
     ["L'agente risponde usando il documento", "Ho testato 5 domande", "Ho annotato le differenze con gli agenti di Make"],
     [Q("A cosa serve Copilot Studio?", ["A costruire e distribuire agenti AI", "A modificare foto", "A gestire le email", "A creare fogli di calcolo"], 0, "Copilot Studio è lo strumento per creare agenti nella Power Platform.")])
unit("Ripasso ed esame PL-900", "pl", URL["plp"], "la guida di studio ufficiale e la verifica di pratica gratuita", "il ripasso degli argomenti più deboli",
     "Fai la verifica di pratica gratuita, ripassa gli errori e decidi la data dell'esame (a pagamento).",
     ["Ho fatto la verifica di pratica", "Ho ripassato gli argomenti sbagliati", "Ho deciso se e quando sostenere l'esame"],
     [Q("Che cosa ti offre gratis Microsoft per preparare il PL-900?", ["Il percorso di studio e una verifica di pratica", "L'esame", "Un PC", "Una licenza a vita"], 0, "Il materiale di studio e la verifica di pratica sono gratuiti; l'esame è a pagamento.")])

assert len(U) == 48, len(U)

weeks = []
for i, (title, plat, url, a, b, task, crit, qs) in enumerate(U, start=1):
    ph = next(p["n"] for p in PHASES if p["weeks"][0] <= i <= p["weeks"][1])
    sid = lambda k: f"b{i:02d}s{k}"
    def steps(sk, items):
        out = []
        for j, (t, link, label) in enumerate(items, start=1):
            st = {"id": f"{sk}-{j}", "text": t}
            if link: st["link"] = link; st["label"] = label
            out.append(st)
        return out
    s1 = {"id": sid(1), "title": f"{title} · studio", "platform": plat, "url": url, "minutes": 60,
          "goal": f"Capire {a.split(':')[0]}.",
          "steps": steps(sid(1), [
             (f"Apri il corso ed entra con il tuo account. 5 min", url, "Inizia il corso"),
             (f"Studia {a}. 35 min", url, "Vai al corso"),
             ("Annota nel diario AI i 3 concetti più importanti con parole tue. 10 min", None, None),
             ("Chiedi a Claude o a ChatGPT di spiegarti il concetto più difficile con un esempio del tuo settore. 10 min", None, None)]),
          "exercise": {"type": "pratica", "task": "Spiega a voce o per iscritto, in 5 frasi, cosa hai imparato oggi come se lo raccontassi a un collega.",
                       "criteria": ["Ho usato parole mie, senza copiare", "Ho fatto almeno un esempio concreto", "Ho indicato un punto che non mi è ancora chiaro"]}}
    s2 = {"id": sid(2), "title": f"{title} · approfondimento", "platform": plat, "url": url, "minutes": 60,
          "goal": f"Approfondire {b.split(':')[0]}.",
          "steps": steps(sid(2), [
             (f"Riprendi il corso dal punto in cui eri rimasto. 5 min", url, "Inizia il corso"),
             (f"Studia {b}. 35 min", url, "Vai al corso"),
             ("Svolgi gli esercizi o i quiz del corso. 15 min", url, "Vai al corso"),
             ("Segna nel diario AI cosa applicherai nella sessione pratica. 5 min", None, None)]),
          "exercise": {"type": "quiz", "questions": qs}}
    s3 = {"id": sid(3), "title": f"{title} · pratica", "platform": plat, "url": url, "minutes": 60,
          "goal": "Applicare quanto studiato a un caso reale.",
          "steps": steps(sid(3), [
             ("Rileggi gli appunti delle due sessioni di studio. 5 min", None, None),
             (f"Esegui il compito pratico: {task} 40 min", None, None),
             ("Chiedi a Claude un parere critico sul risultato e migliora un punto. 10 min", None, None),
             ("Valuta i criteri qui sotto e salva il risultato nel diario AI. 5 min", None, None)]),
          "exercise": {"type": "pratica", "task": task, "criteria": crit}}
    for s in (s1, s2, s3):
        for q in (s["exercise"].get("questions") or []): assert 0 <= q["answer"] < len(q["options"])
    weeks.append({"n": i, "phase": ph, "title": title, "sessions": [s1, s2, s3]})

platforms = {k: {"name": v, "url": URL[k if k in URL else "oai"]} for k, v in PLAT.items()}
platforms["ibm"]["url"] = URL["ibm"]; platforms["lq"]["url"] = URL["lq"]; platforms["mk"]["url"] = URL["mk"]; platforms["pl"]["url"] = URL["pl"]
out = {"version": "1.0.0", "updated": "2026-11-23", "id": "ai-business", "title": "AI per il business e i dati",
       "platforms": platforms, "phases": PHASES, "weeks": weeks}
json.dump(out, open(sys.argv[1], "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("weeks", len(weeks), "sessions", sum(len(w["sessions"]) for w in weeks))
