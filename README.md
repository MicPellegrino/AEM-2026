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

Potete saltare questo punto.

### Utenti macOS
<img src="https://upload.wikimedia.org/wikipedia/commons/7/71/Finder_icon_macOS_Yosemite.png" width="50">

L'environment e i notebook sono stati testati su distribuzioni recenti di macOS e architettura Apple M4, quindi non _dovrebbero_ esserci problemi.

### Utenti Windows
<img src="https://upload.wikimedia.org/wikipedia/commons/6/6d/Windows_Logo_%281992-2001%29.svg" width="50">
Avete due possibilità:

- :green_circle: Scelta consigliata :green_circle: : attivare e usare **Windows Subsystem for Linux (WSL)**. **[TODO]**
- :yellow_circle: Piano B :yellow_circle: : usare una Virtal Machine (VM) tramite **oVirt**. Trovate le istruzioni per accedere alle VM e caricare/scaricare dati qui: https://webdoc.laib.polito.it/index.php/5-procedure-operative/17-4-12-supporto-specifico-ai-corsi/150-vdi-linux-new-2

## Come creare il virtual environment

**Step :one: - Installare un environment manager**:
- Miniconda: https://www.anaconda.com/docs/getting-started/miniconda/install;
- Mamba: https://mamba.readthedocs.io/en/latest/installation/mamba-installation.html.

Esempio di installazione di Miniconda (testato su `wsl`):

	wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
	./Miniconda3-latest-Linux-x86_64.sh
	# Follow the instructions

Da ora in poi farò riferimento a Miniconda, ma tenete presente che qualsiasi variante dovrebbe funzionare in modo analogo. Da esperienza personale, Mamba è decisamente più veloce nella creazione e gestione degli environment. Tuttavia, se Miniconda è già installato sul vostro sistema, non è necessario installare altre versioni. Sconsiglio di utilizzare Anaconda.

:warning: Una versione "lightweight" di Mamba, chiamata Micromamba, è già installata sulle VM di oVirt, basterà sostituire il comando `mamba` con `micromamba`. **[TODO]**

:warning: Le istruzioni di installazione spiegano anche come configurare e attivare l'environment manager in modo automatico. Potreste voler (o dover) aggiungere alcune righe al file `.bashrc` nella tua home directory per attivare automaticamente l'environment manager all’apertura di una nuova sessione di `bash`. Ad esempio, se usate Miniconda: 

	[TODO]

mentre se usate Mamba:

	# Apri .bashrc con un editor di testo
	export MAMBA_EXE='<directory-dove-hai-installato-mamba>/mambaforge/bin/mamba';
	export MAMBA_ROOT_PREFIX='<directory-dove-hai-installato-mamba>/mambaforge';

**Step :two: - Creare il virtual environment** eseguendo:

	conda env create -f environment.yml

Potrebbe essere necessario impostare `channel-priority strict` per costringere `conda` a installare la versione corretta di Jupyter Notebook (comando analogo per `miniconda`):

	conda config --set channel_priority strict
	conda env create -f environment.yml

Per chi invece usa `mamba` (comando analogo per `micromamba`):

	mamba env create -f environment.yml --channel-priority strict

:warning: Poiché questa repository potrebbe essere modificata mentre il corso è attivo, eseguite sempre `git pull` prima di iniziare a lavorare sugli esercizi e verificate che `environment.yml` non sia cambiato! In caso contrario, aggiornate il virtual environment.

:warning: Se la versione della vostra libreria CUDA di sistema è relativamente recente, la creazione dell’environment potrebbe richiedere un po’ di tempo (1-5 minuti). Non disperate, basta aspettare.

**Step :three: - Testare l'installazione di GROMACS**. Attivate prima il virtual environment eseguendo (nel caso sostituire `conda` con `mamba` o `micromamba`):

	conda activate aem-2026

e poi eseguendo: 

	gmx help mdrun
 
dalla linea di comando. La prima linea di output dovrebbe essere: `:-) GROMACS - gmx help, 2025.4-conda_forge (-:`.

:warning: Se il comando `gmx` non viene trovato oppure ottenete una versiona diversa da `2025.4-conda_forge`, significa che l’environment non è attivo oppure che la libreria (dependency) di GROMACS non è stata installata quando avete creato l'environment.

## Notebook ed esercizi

Spostatevi in una delle sotto-cartelle (ad esempio `cd molecular-dynamics/cnt`) e aprite il notebook corrispondente eseguendo:

	jupyter-notebook <nome-del-notebook>.ipynb

Ora potete eseguire il notebook cella per cella. Negli esercizi, potreste dover ispezionare o modificare i file di configurazione delle simulazioni; in tal caso, aprite Jupyter Notebook nella cartella corrispondente, semplicemente eseguendo:

	jupyter-notebook

e navigate/aprite il file che volete ispezionare/modificare.

In alternativa, potete aprire i file di configurazione da linea di comando (cioè _fuori dal notebook_) usando il vostro editor di testo preferito, come `vim`, `code`, `emacs`, etc...

### Contenuto

- `intro-python`: Contiene un notebook di ripasso sugli aspetti fondamentali di Python.
- `molecular-dynamics`: Contiene gli esercizi di Dinamica Molecolare;
  - `cnt`: Il primo esercizio introduce le basi della Dinamica Molecolare (creazione di file di configurazione, algoritmi, campi di forza, topologie, termalizzazione e post-processing). L’obiettivo è valutare la conducibilità termica di un nanotubo di carbonio usando un metodo di non-equilibrio. Zero to hero!
  - `zeolite`: Il secondo esercizio introduce la solvatazione e ai modelli dell’acqua. Vi verrà chiesto di simulare una matrice di zeolite a diversi livelli di idratazione per studiarne le proprietà di accumulo di energia. Inoltre, calcolerete il coefficiente di auto-diffusione dell’acqua, un osservabile "tipico" dalla Dinamica Molecolare.
- `machine-learning`: coming soon...

## Visualizzazione (facoltativo)

Le traiettorie e le configurazioni sono visualizzate nei notebooks tramite widgets `nglview`. Esistono anche altre soluzioni (potenzialmente migliori) _fuori dal notebook_:
- VMD: https://www.ks.uiuc.edu/Development/Download/download.cgi?PackageName=VMD - gratis, richiede una registrazione con email istituzionale;
- OVITO: https://www.ovito.org/manual/installation.html - ha una versione gratuita con funzionalità limitate e una versione commerciale completa (la versione gratuita è più che sufficiente, inoltre consente di usare l’intero API Python);
- VEGA ZZ: https://www.ddl.unimi.it/cms/index.php?Software_projects:VEGA_ZZ:Download - richiede registrazione e codice di attivazione;
- PyMOL: https://www.pymol.org/ - richiede registrazione e codice di attivazione.

## Software consigliato (facoltativo)

- **VMD** :film_projector: - vedi sopra;
- **Grace** :bar_chart: - un software di plotting molto leggero, molto "GROMACS-friendly" (https://plasma-gate.weizmann.ac.il/Grace/);
- **Visual Studio Code** :computer: - GUI per editing e programmazione, molto versatile (https://code.visualstudio.com/download);
- **MATLAB** :triangular_ruler: - gli script di post-processing in `molecular-dynamics` sono disponibili anche in formato leggibile da MATLAB.

## Ringraziamenti

Messo a disposizione per gli studenti del corso "Applicazioni Energetiche dei Materiali" dal multi-Scale ModeLing Laboratory (SMaLL) del Politecnico di Torino (Torino, Italia). Queste risorse sono destinate a scopi didattici e sono state progettate per corsi di laurea magistrale e di dottorato del Politecnico di Torino (2023-2026).

Autori:
- Matteo Fasano (matteo.fasano@polito.it)
- Michele Pellegrino (michele.pellegrino@polito.it)
- Marina Provenzano (marina.provenzano@polito.it)
- Fabiano Tarulli (fabiano.tarulli@polito.it)

