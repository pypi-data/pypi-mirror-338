![FANTASIA Logo](docs/source/_static/FANTASIA.png)

# FANTASIA

**Functional ANnoTAtion based on embedding space SImilArity**

FANTASIA is an advanced pipeline designed for automatic functional annotation of protein sequences using state-of-the-art protein language models. It integrates deep learning embeddings and similarity searches in vector databases to associate Gene Ontology (GO) terms with proteins.

For full documentation, visit [FANTASIA Documentation](https://fantasia.readthedocs.io/en/latest/).

## Key Features

- **✅ Advanced Embedding Models**  
  Supports protein language models: **ProtT5**, **ProstT5**, and **ESM2** for sequence representation.

- **🔍 Redundancy Filtering**  
  Filters out homologous sequences using **CD-HIT**, allowing controlled redundancy levels through an adjustable threshold, ensuring reliable benchmarking and evaluation.

- **💾 Optimized Data Storage**  
  Embeddings are stored in **HDF5 format** for input sequences, while similarity lookups are performed in a vector database (**pgvector in PostgreSQL**) for fast retrieval.

- **🚀 Efficient Similarity Lookup**  
  Performs high-speed searches using **pgvector**, enabling accurate annotation based on embedding similarity.

- **🔬 Functional Annotation by Similarity**  
  Assigns Gene Ontology (GO) terms to proteins based on **embedding space similarity**, leveraging pre-trained embeddings.

## Pipeline Overview (Simplified)

1. **Embedding Generation**  
   Computes protein embeddings using deep learning models (**ProtT5**, **ProstT5**, and **ESM2**).

2. **GO Term Lookup**  
   Uses vector similarity searches in **pgvector** to assign Gene Ontology terms based on embedding similarity.

## Acknowledgments

FANTASIA is the result of a collaborative effort between **Ana Roja’s Lab** (Andalusian Center for Developmental Biology, CSIC) and **Rosa Fernández’s Lab** (Metazoa Phylogenomics Lab, Institute of Evolutionary Biology, CSIC-UPF). This project demonstrates the synergy between research teams with diverse expertise.

This version of FANTASIA builds upon previous work from:

- [`Metazoa Phylogenomics Lab's FANTASIA`](https://github.com/MetazoaPhylogenomicsLab/FANTASIA)  
  The original implementation of FANTASIA for functional annotation.

- [`bio_embeddings`](https://github.com/sacdallago/bio_embeddings)  
  A state-of-the-art framework for generating protein sequence embeddings.

- [`GoPredSim`](https://github.com/Rostlab/goPredSim)  
  A similarity-based approach for Gene Ontology annotation.

- [`protein-metamorphisms-is`](https://github.com/CBBIO/protein-metamorphisms-is)  
  Serves as the **reference biological information system**, providing a robust data model and curated datasets for protein structural and functional analysis.

We also extend our gratitude to **LifeHUB-CSIC** for inspiring this initiative and fostering innovation in computational biology.

## Citing FANTASIA

If you use **FANTASIA** in your research, please cite the following publications:

1. Martínez-Redondo, G. I., Barrios, I., Vázquez-Valls, M., Rojas, A. M., & Fernández, R. (2024).  
   *Illuminating the functional landscape of the dark proteome across the Animal Tree of Life.*  
   [DOI: 10.1101/2024.02.28.582465](https://doi.org/10.1101/2024.02.28.582465)

2. Barrios-Núñez, I., Martínez-Redondo, G. I., Medina-Burgos, P., Cases, I., Fernández, R., & Rojas, A. M. (2024).  
   *Decoding proteome functional information in model organisms using protein language models.*  
   [DOI: 10.1101/2024.02.14.580341](https://doi.org/10.1101/2024.02.14.580341)


---

### 👥 Project Team

#### 🔧 Technical Team
- **Francisco Miguel Pérez Canales**: [fmpercan@upo.es](mailto:fmpercan@upo.es)  
  *Author of the system’s engineering and technical implementation*  
- **Francisco J. Ruiz Mota**: [fraruimot@alum.us.es](mailto:fraruimot@alum.us.es)  
  *Junior developer*

#### 🧬 Scientific Team & Original Authors of FANTASIA v1
- **Ana M. Rojas**: [a.rojas.m@csic.es](mailto:a.rojas.m@csic.es)  
- **Gemma I. Martínez-Redondo**: [gemma.martinez@ibe.upf-csic.es](mailto:gemma.martinez@ibe.upf-csic.es)  
- **Rosa Fernández**: [rosa.fernandez@ibe.upf-csic.es](mailto:rosa.fernandez@ibe.upf-csic.es)  


---
