# Percorso AI

App di studio personale: 20 settimane, 100 sessioni da circa un'ora per diventare un operatore AI esperto.
Per ogni sessione: obiettivo, piattaforma, passi da spuntare con il livello di apprendimento ed esercizio di verifica finale.

- `index.html`: l'app
- `curriculum.json`: i contenuti del percorso (aggiornabili senza perdere i progressi)
- `sw.js`, `manifest.webmanifest`, `icons/`: installazione su iPhone e funzionamento offline

La scheda **Progetto** legge in sola lettura l'avanzamento del progetto finale, il Diario di Viaggio, da
`https://itopo-ai.github.io/diario-di-viaggio/progress.json`.

Installazione: apri l'indirizzo in Safari → Condividi → Aggiungi alla schermata Home.

## Studenti

Più studenti possono usare l'app sullo stesso dispositivo: ognuno ha nome e password, e i suoi progressi sono cifrati (AES-GCM con chiave derivata dalla password, PBKDF2). Senza la password i progressi non si possono leggere né recuperare. L'app si blocca da sola dopo 10 minuti in background.
