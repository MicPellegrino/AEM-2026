# Applicazioni energetiche dei materiali (primavera 2026) - Dinamica Molecolare e Machine Learning

## Indice

- [Come ottenere una distribuzione di Linux](#come-ottenere-una-distribuzione-di-linux)
- [Come creare il virtual environment](#come-creare-il-virtual-environment)
- [Notebook per gli esercizi](#notebook-per-gli-esercizi)
- [Visualizzazione dei risultati](#how-to-visualize-the-results)
- [Software consigliato (facoltativo)](#additional-suggested-software)
- [Ringraziamenti](#acknowledgements)

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
- :yellow_circle: Piano B :yellow_circle: : usare una Virtal Machine (VM) tramite **oVirt**. **[TODO]**

## Come creare il virtual environment

**Step :one: - Installare Conda o una delle sue varianti**:
- Conda: https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html;
- Miniconda: https://www.anaconda.com/docs/getting-started/miniconda/install;
- Mamba: https://mamba.readthedocs.io/en/latest/installation/mamba-installation.html;
- Micromamba: https://mamba.readthedocs.io/en/latest/installation/micromamba-installation.html.

Esempio di installazione di Miniconda (testato su `wsl`):

	wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
	./Miniconda3-latest-Linux-x86_64.sh
	# Follow the instructions

Da ora in poi farò riferimento a Conda, ma tenete presente che qualsiasi variante dovrebbe funzionare in modo analogo. Da esperienza personale, Mamba è decisamente più veloce nella creazione e gestione degli environment, mentre Micromamba è la variante più "lightweight". tuttavia, se Conda è già installato sul vostro sistema, non è necessario installare altre versioni.

:warning: Micromamba è già installato sulle Virtual Machines di oVirt.

:warning: Le istruzioni di installazione spiegano anche come configurare e attivare Conda in modo automatico. Potresti voler (o dover) aggiungere alcune righe al file `.bashrc` nella tua home directory per attivare automaticamente Conda all’apertura di una nuova sessione di `bash`. Ad esempio: **[TODO]**

**Step :two: - Creare il virtual environment** eseguendo:

	conda env create -f environment.yml

Potrebbe essere necessario impostare `channel-priority strict` per costringere `conda` a installare la versione corretta di Jupyter Notebook (comando analogo per `miniconda`):

	conda config --set channel_priority strict
	conda env create -f environment.yml

Per chi invece usa `mamba` (comando analogo per `micromamba`):

	mamba env create -f environment.yml --channel-priority strict

:warning: Poiché questa repository potrebbe essere modificata durante il corso, eseguite sempre `git pull` prima di iniziare a lavorare sugli esercizi e verificate che `environment.yml` non sia cambiato! In caso contrario, aggiornate il virtual environment.

:warning: Se la versione della vostra libreria CUDA di sistema è relativamente recente, la creazione dell’environment potrebbe richiedere un po’ di tempo (1-5 minuti). Non disperate, basta aspettare.

**Step :three: - Testare l'installazione di GROMACS**. Attivate prima il virtual environment eseguendo (nel caso sostituire `conda` con `mamba`, etc...):

	conda activate aem-2026

e poi eseguendo: 

	gmx help mdrun
 
dalla linea di comando. La prima linea di output dovrebbe essere: `:-) GROMACS - gmx help, 2025.4-conda_forge (-:`.

:warning: Se il comando `gmx` non viene trovato oppure ottenete una versiona diversa da `2025.4-conda_forge`, significa che l’environment non è attivo oppure che la libreria (dependency) di GROMACS non è stata installata.

## Notebook per gli esercizi

Move to the any of the folders (e.g. `cd biphase`) and open the related notebook by running:

	jupyter-notebook <name-of-the-notebook>.ipynb

You can now run the notebook cell-by-cell. You may have to edit some simulation configuration file; in this case, open Jupyter Notebook in the folder, by just running:

	jupyter-notebook

and navigate to the file you want to edit. Sorry ladies and gentlemen, the notebook itself is the best, and only, GUI you’re going to get!

Alternatively, you can open the file from `bash` (i.e. _outside the notebook_) using your favourite text editor, like `vim`, `code`, `emacs`, `gedit` or `featherpad`. They are all equal, but `vim` is more equal than the others.

## How to visualize the results

In the notebooks, you will find `nglview` widgets allowing inline visualization of molecular simulation results. There are other (possibly better) solutions _outside the notebook_:
- VMD: https://www.ks.uiuc.edu/Development/Download/download.cgi?PackageName=VMD - free of charge, you just need to register your institutional email;
- OVITO: https://www.ovito.org/manual/installation.html - there's a free limited version and a full commercial version (the free version is more than enough for visualization purposes, plus you can use the complete Python API without having to pay);
- VEGA ZZ: https://www.ddl.unimi.it/cms/index.php?Software_projects:VEGA_ZZ:Download - requires registration and activation key;
- PyMOL: https://www.pymol.org/ - requires registration and activation key.

In terms of "GROMACS friendliness", **VMD** is definitely the best. I really suggest you install VMD.

## Additional suggested software

- **VMD** :film_projector: - see the previous section;
- **Grace** :bar_chart: - a very lightweight plotting software, very GROMACS-friendly (https://plasma-gate.weizmann.ac.il/Grace/);
- **MATLAB** :computer: - the postprocessing scripts for the `cnt` and the `zeolite` are also provided in MATLAB format. 

## Acknowledgements

Provided by the Multi-Scale Modeling Lab of Politecnico di Torino (Italy). These resources are intended for pedagogical purposes, and were designed for the undergraduate and third-cycle courses at Politecnico di Torino (2023-2026).

Authors:
- Matteo Fasano (matteo.fasano@polito.it)
- Michele Pellegrino (michele.pellegrino@polito.it)

