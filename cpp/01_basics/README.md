# 🔐 XOR File Encryptor/Decryptor (C++)

This project is part of my red team journey under **Secverse**. It demonstrates the use of the XOR bitwise operator in **file encryption/decryption** — a classic low-level technique used in malware obfuscation, red team payloads, and CTFs.

---

## 🧠 What is XOR?

**XOR (Exclusive OR)** is a reversible bitwise operation:

| A | B | A XOR B |
|---|---|---------|
| 0 | 0 |   0     |
| 1 | 0 |   1     |
| 0 | 1 |   1     |
| 1 | 1 |   0     |

- Used in **basic encryption** because of its reversibility.
- Same function used to encrypt and decrypt:
  - `Encrypted = Original ^ Key`
  - `Original = Encrypted ^ Key`

---

## 🚀 How to Compile

Make sure you have `g++` installed. Then run:

```bash
g++ xor_cipher.cpp -o xor_cipher
