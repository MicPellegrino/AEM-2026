### Installare le librerie per ML/NNPs

Alcune librerie necessarie per gli esercizi su Machine Learning e Neural Netweork Potentials non sono ottenibili tramite `conda`/`mamba`. Nei notebooks troverete i comandi `pip` per installare queste librerie all'occorrenza. 

Contrariamente a quanto viene spesso detto, "mischiare" `pip` e `conda` non è in generale sbagliato. In questo caso è necessario.

:yellow_circle: Se usate **oVirt** :yellow_circle: : _Tutte_ le librerie sono _già state installate_, quindi non dovete fare nulla.

:green_circle: Per tutti gli altri :green_circle: : Se volete portarvi avanti, potete già installare `torch` e `mace`.

## PyTorch

**Dopo** aver attivato il l'environment virtuale tramite Conda/Mamba, scaricate la versione di `torch` adatta per il vostro sistema.

### GPU

Potete controllare la disponibilità di una GPU Nvidia e di CUDA eseguendo i comandi:
```
nvcc --version
nvidia-smi
```
Scegliete la versione in base a CUDA: https://pytorch.org/get-started/locally/ (stable, Linux, Python, pip, e la vostra versione di CUDA).

**Ad esempio**, la mia workstation ha una A4000 e CUDA 12.6, quindi:
```
pip3 install torch torchvision --index-url https://download.pytorch.org/whl/cu126
```

### CPU

Verosimilmente, la stragrande maggioranza dei vostri laptop _non_ disporrà di una GPU Nvidia. In tal caso installate `torch` per CPU:
```
pip3 install torch torchvision --index-url https://download.pytorch.org/whl/cpu
```

## MACE

Indipendentemente dall'hardware:
```
pip3 install mace-torch cuequivariance
```

## Testare l'installazione

Aprite Python da linea di comando ed eseguite:
```
import torch
import mace
torch.cuda.is_available()
```
Non dovrebbero esserci errori. Se avete installato `torch` per GPU con supporto CUDA, `torch.cuda.is_available()` dovrebbe restituire `True`.
