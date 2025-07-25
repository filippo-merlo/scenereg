# 🖼️ COOCO: Common Objects Out-of-Context

**Authors**: Filippo Merlo\*, Ece Takmaz, Wenkai Chen, Albert Gatt
\*Corresponding author: [f.merlo.research@gmail.com](mailto:f.merlo.research@gmail.com)

**Affiliations**: Utrecht University, University of Trento

This repository supports the paper:

"COOCO -- Common Objects Out-of-Context -- Semantic Violation in Scenes: Investigating Multimodal Context in Referential Communication"
Submitted to TACL 2025
Status: Submission under review

---

## 📦 Dataset Overview

You can download the **COOCO** dataset from [Hugging Face](https://huggingface.co/datasets/fmerlo/COOCO).

**COOCO** is a large-scale dataset designed to investigate how **Vision-Language Models (VLMs)** leverage scene context during **referring expression generation**. It focuses on **semantic violations**, evaluating model performance when target objects have **low**, **medium**, or **high semantic relatedness** to their surrounding scenes.

Each sample in COOCO contains:

* A scene from COCO-Search18 with a labeled **target object**, called Original version
* A version of the scene where the target object is just removed, called Clean version
* Multiple **manipulated versions** with inpainted objects of varying semantic relatedness


Each original image is augmented by replacing the target object with semantically related or unrelated alternatives. Relatedness is computed using **ConceptNet embeddings** and **THINGSplus norms**:

* **Low**
* **Medium**
* **High**
* **Same-target**: original object category generated (control)

Inpainting is guided by LLaVA-generated prompts and verified via an automated visual QA procedure.

---

The dataset supports the study of:

* Referring expression robustness to semantic incongruence

---
