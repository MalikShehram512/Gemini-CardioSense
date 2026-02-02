# <p align="center">🫀 Gemini CardioSense</p>
<p align="center">
  <ins><i>Next-Generation AI Phonocardiography & Arrhythmia Detection</i></ins>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/Google%20Gemini-8E75B2?style=for-the-badge&logo=googlegemini&logoColor=white" />
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Status-Clinical%20Prototype-success?style=for-the-badge" />
</p>

---

## 🚀 Live Dashboard
<p align="center">
  <a href="https://gemini-cardiosense-tvbrhahebtdrwse5yjelnb.streamlit.app/">
    <img src="https://img.shields.io/badge/ENTER_VIRTUAL_CLINIC-000000?style=for-the-badge&logo=rocket&logoColor=white&labelColor=FF4B4B" />
  </a>
</p>

---

## 📖 Project Overview
**Gemini CardioSense** (formerly PulsePrint AI) is an intelligent biomedical signal analysis platform. By combining the ubiquity of digital heart sound recordings with the high-reasoning capabilities of **Gemini 2.5 Flash**, we have created a tool that decodes the "biomedical print" of the human heart to identify Atrial Fibrillation (AFib) and other rhythm irregularities.

### 🌟 Advanced Capabilities
* **Multi-Modal Reasoning:** Direct analysis of audio bytes to distinguish between $S_1$ (Lub) and $S_2$ (Dub) heart sounds.
* **Denoising Intelligence:** An AI agent that identifies background friction and applies a custom **Butterworth Bandpass Filter**.
* **Clinical Telemetry:** Calculation of systolic and diastolic intervals to detect "irregularly irregular" patterns.
* **Professional Visualization:** High-fidelity Phonocardiogram (PCG) rendering.



---

## 🛠️ The Tech Stack

| Layer | Technology |
| :--- | :--- |
| **Intelligence Engine** | Google Gemini 2.5 Flash API |
| **Signal Processing** | Librosa, SciPy, NumPy |
| **User Interface** | Streamlit (Medical Dark-Mode) |
| **Data Viz** | Matplotlib |
| **Environment** | Docker / Streamlit Cloud |

---

## 🧠 The Science Behind the AI

The system processes signals through a specific medical pipeline:

1.  **Normalization:** The raw amplitude is scaled for consistency.
2.  **Filtration:** Noise is stripped using a bandpass filter:
    $$f_{isolated} = [20\text{Hz}, 500\text{Hz}]$$
3.  **Inference:** Gemini calculates the Heart Rate using:
    $$BPM = \frac{60}{\Delta t_{S1 \rightarrow S1}}$$



---

## ⚙️ Installation & Setup

### 📦 System Requirements
In your environment (Streamlit Cloud or Linux), ensure `libsndfile1` is installed. 
Create a `packages.txt` file with:
```text
libsndfile1
