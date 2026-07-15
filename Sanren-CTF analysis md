# 🔍 Case Study: SANReN CSC 2024 — Advanced Forensics, Malware Reversing & AI Orchestration

## 📌 Executive Summary
* **Event**: SANReN Cyber Security Challenge (CSC) National Qualifiers
* **Team Placement**: 11th out of 240+ teams nationally (UNISA Representative)
* **Scope**: Evaluated across 50 multi-disciplinary CTF vectors, including OSINT, Steganography, Digital Forensics, Password Cracking, and Reverse Engineering.
* **Core Role**: Served as the technical lead for complex reverse engineering, cryptographic decryption, and defensive AI execution.

---

## 📱 Challenge 1: Android Ransomware Reverse Engineering (Kotlin)
### 1. The Roadblock
The objective was to neutralize a live Android ransomware payload (`ransom.apk`) written in Kotlin. The malware had locked down mock target files, requiring reverse-engineering of the application layer to locate the decryption key and retrieve the flag.

### 2. Technical Execution & AI Orchestration
* **Decompilation**: Analyzed the internal control flow and structural components of the compiled APK archive.
* **AI Logic Guidance**: Leveraged ChatGPT to rapidly trace targeted cryptographic execution functions within the decompiled class files. 
* **Key Recovery**: Developed an automated extraction routine guided by localized LLM prompts to expose the hardcoded decryption key pattern, successfully unlocking the payload's captured datasets.

---

## 📡 Challenge 2: Network Traffic Decryption via Wireshark
### 1. The Roadblock
Intercepted an obfuscated network capture stream containing encrypted authentication packets. Standard stream-following techniques yielded unreadable data segments, requiring custom algorithmic decryption.

### 2. Technical Execution
* **Packet Isolation**: Utilized advanced Wireshark filtering syntax to map, capture, and extract raw hexadecimal payload streams.
* **Scripted Decryption**: Engineered a custom Python decryption script via targeted AI prompting. The script automated the byte-alignment and reverse-hashing processes, stripping the encoding layer to reveal the plaintext authentication credentials inline.

---

## 🖼️ Challenge 3: Steganography & AI Image Processing
### 1. The Roadblock
A visually pristine, seemingly innocent image file contained hidden metadata flags that bypassed traditional local file-signature carving tools.

### 2. Technical Execution
* **Algorithmic Vision Parsing**: Leveraged advanced AI-driven image processing scripts to perform deep structural analysis on the pixel arrays.
* **Exfiltration**: Successfully extracted the hidden steganographic payload data embedded within the lower bit-layers of the image matrix.

---

## 🔑 Challenge 4: High-Compute Password Cracking Lessons
### 1. The Roadblock
Attempted targeted cryptographic cracking against complex enterprise password hashes under compressed competition timelines.

### 2. Hardware Bottlenecks & Practical Realities
* **Tooling Fatigue**: Configured brute-force and hybrid dictionary pipelines using **Hashcat** and **John the Ripper**. Mass execution routines caused severe CPU thermal and compute spikes on local testing hardware.
* **Algorithmic Adaptation**: Promoted a hybrid approach via ChatGPT combining dictionary attacks with specialized pre-computed rainbow table mechanics. 

### 🛡️ Enterprise Security Defenses Discovered
While the specific high-entropy hash remained uncracked due to localized time constraints, this failure provided high-utility defensive engineering insights:
* **Entropy Limits**: Long, highly unique character sequences vastly maximize the computational costs and exhaustion metrics required by adversaries.
* **Time-to-Attack Factors**: Threat actors prioritize rapid entry-and-exit workflows; high-compute defensive obstacles heavily deter active exploitation.
* **Policy Strategy**: Frequent, mandated password rotation schemes drastically minimize the operational lifespan of leaked or cached credentials.

---

## 🧠 Advanced Integration Roadmap
This high-stress competition highlighted the power of combining traditional network fundamentals with automated AI scripting. To scale these methodologies into the enterprise cloud tier, my immediate training roadmap is prioritized as follows:
1. **AWS Certified AI Practitioner (AIF-C01)**: Translating local adversarial prompt strategies into automated cloud-native model protection and data guardrails.
2. **Infrastructure Automation**: Integrating Python automation workflows directly into secure AWS infrastructure pipelines.
