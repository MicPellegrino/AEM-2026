# Applicazioni Energetiche dei Materiali (2026) - Dinamica Molecolare e Machine Learning

## Indice

- [Come ottenere una distribuzione di Linux](#come-ottenere-una-distribuzione-di-linux)
- [Come creare il virtual environment](#come-creare-il-virtual-environment)
- [Notebook ed esercizi](#notebook-ed-esercizi)
- [Visualizzazione (facoltativo)](#visualizzazione-facoltativo)
- [Software consigliato (facoltativo)](#software-consigliato-facoltativo)
- [Ringraziamenti](#ringraziamenti)

## Come ottenere una distribuzione di Linux

### Utenti Linux (Ubuntu, Debian, Fedora, ...)
<img src="https://upload.wikimedia.org/wikipedia/commons/3/35/Tux.svg" width="50">

Potete saltare questa sezione; assicuratevi semplicemente che `git` sia installato (e nel caso installatelo).

### Utenti macOS
<img src="https://upload.wikimedia.org/wikipedia/commons/7/71/Finder_icon_macOS_Yosemite.png" width="50">

L'environment e i notebook sono stati testati su distribuzioni recenti di macOS e architettura Apple M4, quindi non _dovrebbero_ esserci problemi. Anche voi potete saltare questa sezione. Anche per voi: assicuratevi semplicemente che `git` sia installato (e nel caso installatelo).

### Utenti Windows
<img src="https://upload.wikimedia.org/wikipedia/commons/6/6d/Windows_Logo_%281992-2001%29.svg" width="50">
Avete due possibilità:

- :green_circle: Scelta consigliata :green_circle: : Attivare e usare **Windows Subsystem for Linux (WSL)** sul vostro laptop. Trovate le istruzioni per l'installazione qui: https://learn.microsoft.com/en-us/windows/wsl/install. Una volta installato, per attivarlo basterà aprire PowerShell ed eseguire `wsl` da linea di comando; dovrebbe aprirsi una sessione `bash` Linux. Assicuratevi di essere nella vostra `home` directory (i.e. **non** `mnt`), nel caso eseguite semplicemente `cd` sulla linea di comando per spostarvi nella `home`. 

- :yellow_circle: Piano B :yellow_circle: : Usare una Virtal Machine (VM) remota tramite **oVirt**. Trovate le istruzioni per accedere alle VM e caricare/scaricare dati a questo link (accessibile da rete PoliTo): https://webdoc.laib.polito.it/index.php/5-procedure-operative/17-4-12-supporto-specifico-ai-corsi/150-vdi-linux-new-2

## Come creare il virtual environment

**Step :zero: - Clonare la repository**, eseguendo:

	git clone https://github.com/MicPellegrino/AEM-2026.git

Spostatevi poi nella cartella della repository:

	cd AEM-2026

:yellow_circle: Per chi usa **oVirt** :yellow_circle: : È possibile clonare da GitHub, tuttavia le VM hanno accesso limitato ad internet (i.e. oltre GitHub, non sarà possibile accedere ad alcun URL fuori dal dominio di PoliTo). Nel caso non riusciste a scaricare/clonare da GitHub, trovate comunque il contenuto della repository sulla pagina del corso sul Portale della Didattica.

**Step :one: - Installare un environment manager**:

**Miniconda**: [https://www.anaconda.com/docs/getting-started/miniconda/install](https://www.anaconda.com/docs/getting-started/miniconda/install/linux-install)

Esempio di installazione di Miniconda da linea di comando `bash` per `wsl`:
- Scaricate lo script di installazione: `wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh`;
- Eseguitelo senza root privileges: `bash Miniconda3-latest-Linux-x86_64.sh`;
- Seguite le istruzioni a terminale.

Per gli utenti macOS: scaricate invece la versione per macOS ([Miniconda3-latest-MacOSX-arm64.sh](https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh)).

Da ora in poi farò riferimento a Miniconda, tenete presente che "varianti" alternative dovrebbero funzionare in modo analogo (e.g. [Mamba](https://mamba.readthedocs.io/en/latest/installation/mamba-installation.html)).

:yellow_circle: Per chi usa **oVirt** :yellow_circle: : Trovate una versione "lightweight" di Mamba, chiamata Micromamba, già installata sulle VM (in `/home/labmd/bin`). Basterà sostituire il comando `conda` con `micromamba`. Le librerie necessarie al corso sono inoltre già state installate, quindi potete passare direttamente allo step :three:.

:warning: Le istruzioni di installazione spiegano anche come configurare e inizializzare l'environment manager in modo automatico. Potreste dover aggiungere alcune righe al file `.bashrc` presente nella vostra home directory per attivare automaticamente l'environment manager all’apertura di una nuova sessione di `bash`.

**Step :two: - Creare il virtual environment** eseguendo:

	conda config --set channel_priority strict
	conda env create -f environment.yml

Per chi invece usa `mamba` (comando analogo per `micromamba`):

	mamba env create -f environment.yml --channel-priority strict

:warning: Se la versione della vostra libreria CUDA di sistema è relativamente recente, la creazione dell’environment potrebbe richiedere un po’ di tempo (1-5 minuti).

**Step :three: - Testare l'installazione di GROMACS**. Attivate il virtual environment eseguendo (nel caso sostituite `conda` con `mamba` o `micromamba`):

	conda activate aem-2026

Eseguite poi: 

	gmx help mdrun
 
dalla linea di comando. La prima linea di output dovrebbe essere: `:-) GROMACS - gmx help, 2025.4-conda_forge (-:`.

:warning: Se il comando `gmx` non viene trovato oppure ottenete una versiona diversa da `2025.4-conda_forge`, significa che l’environment non è attivo oppure che la libreria (dependency) di GROMACS non è stata installata quando avete creato l'environment.

## Notebook ed esercizi

Dalla cartella della repository (`AEM-2026`), spostatevi in una delle sotto-cartelle (ad esempio `cd molecular-dynamics/cnt`) e aprite il notebook corrispondente eseguendo:

	jupyter-notebook <nome-del-notebook>.ipynb

Nel caso il notebook non venga aperto automaticamente, copiate il link che appare su terminale ('token') sul vostro browser preferito (e.g. Google Chrome).

Ora potete eseguire il notebook cella per cella. Negli esercizi, potreste dover ispezionare o modificare i file di configurazione delle simulazioni; in tal caso, aprite Jupyter Notebook nella cartella corrispondente, semplicemente eseguendo:

	jupyter-notebook

e navigate/aprite il file che volete ispezionare/modificare.

In alternativa, potete aprire i file di configurazione da linea di comando (cioè _fuori dal notebook_) usando il vostro editor di testo preferito, come `vim`, `code`, `emacs`, etc...

### Contenuto

- `intro-python`: Contiene un notebook di ripasso su alcuni aspetti fondamentali di Python, NumPy e Jupyter Notebook.
- `molecular-dynamics`: Contiene gli esercizi di Dinamica Molecolare;
  - `cnt`: Il primo esercizio introduce le basi della Dinamica Molecolare (creazione di file di configurazione, algoritmi, campi di forza, topologie, termalizzazione e post-processing). L’obiettivo è valutare la conducibilità termica di un nanotubo di carbonio usando un metodo di non-equilibrio. Zero to hero!
  - `zeolite`: Il secondo esercizio introduce la solvatazione e i modelli dell’acqua. Vi verrà chiesto di simulare una matrice di zeolite a diversi livelli di idratazione per studiarne le proprietà di accumulo di energia. Inoltre, calcolerete il coefficiente di auto-diffusione dell’acqua, un osservabile "tipico" dalla Dinamica Molecolare.
- `machine-learning`: coming soon...

## Visualizzazione (facoltativo)

Le traiettorie e le configurazioni sono visualizzate nei notebooks tramite widgets `nglview`. Esistono altri modi (potenzialmente migliori) per visualizzare configurazioni molecolari usando software dedicato, _fuori dal notebook_:
- **VMD**: https://www.ks.uiuc.edu/Development/Download/download.cgi?PackageName=VMD - gratis, richiede una registrazione con email istituzionale;
- **OVITO**: https://www.ovito.org/manual/installation.html - ha una versione gratuita con funzionalità limitate e una versione commerciale completa (la versione gratuita è più che sufficiente, inoltre consente di usare l’intero API Python per fare post-processing);
- **VEGA ZZ**: https://www.ddl.unimi.it/cms/index.php?Software_projects:VEGA_ZZ:Download - richiede registrazione e codice di attivazione;
- **PyMOL**: https://www.pymol.org/ - richiede registrazione e codice di attivazione.

## Software consigliato (facoltativo)

- :film_projector: **VMD** - vedi sopra;
- :bar_chart: **Grace** - un software di plotting molto leggero, molto "GROMACS-friendly" (https://plasma-gate.weizmann.ac.il/Grace/);
- :computer: **Visual Studio Code** - GUI per editing e programmazione, molto versatile (https://code.visualstudio.com/download);
- :triangular_ruler: **MATLAB** - gli script di post-processing in `molecular-dynamics` sono disponibili anche in un formato leggibile da MATLAB.

## Ringraziamenti

I codici sono messi a disposizione degli studenti del corso "Applicazioni Energetiche dei Materiali", e sono sviluppati e mantenuti dal **multi-Scale ModeLing Laboratory (SMaLL)** del Politecnico di Torino (Torino, Italia). Queste risorse sono destinate a scopi didattici e sono state progettate per corsi di laurea magistrale e di dottorato del Politecnico di Torino (2023-2026). La struttura dei notebook è ispirata ai tutorial ufficiali di GROMACS: https://tutorials.gromacs.org/

Autori:
- Matteo Fasano (matteo.fasano@polito.it)
- Michele Pellegrino (michele.pellegrino@polito.it)
- Marina Provenzano (marina.provenzano@polito.it)
- Fabiano Tarulli (fabiano.tarulli@polito.it)

