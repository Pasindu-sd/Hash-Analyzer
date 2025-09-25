# HashCrackLite

A small, beginner-friendly Python script to detect simple hash types (MD5 / SHA1 / SHA256) and attempt to crack them using a provided wordlist.

> Uses the included `hashcrack.py` and an input file of hashes. See usage below.  
> (This README assumes `hashcrack.py` and `hashes.txt` are in the repo root.) :contentReference[oaicite:0]{index=0} :contentReference[oaicite:1]{index=1}

---

## Features
- Automatically detects hash type by length: MD5 (32), SHA1 (40), SHA256 (64).
- Tries every word from a `wordlist.txt` and reports cracked hashes.
- Saves cracked results to `cracked.txt`.

---

## Requirements
- Python 3.6+  
- A wordlist file named `wordlist.txt` in the repository root (one candidate password per line).

---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/<repo-name>.git
   cd <repo-name>
