import hashlib

def detect_hash_type(hash_value):
    length = len(hash_value)
    if length == 32:
        return 'md5'
    elif length == 40:
        return 'sha1'
    elif length == 64:
        return 'sha256'
    else:
        return None

def load_hashes(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines() if line.strip()]

def load_wordlist(wordlist_path):
    with open(wordlist_path, 'r', encoding="utf-8", errors="ignore") as file:
        return [line.strip() for line in file.readlines()]

def hash_word(word, algo):
    h = getattr(hashlib, algo)()
    h.update(word.encode('utf-8'))
    return h.hexdigest()

def crack_hashes(hashes, wordlist):
    cracked = []
    for h in hashes:
        algo = detect_hash_type(h)
        if not algo:
            print(f"[!] Unknown hash format: {h}")
            continue

        for word in wordlist:
            if hash_word(word, algo) == h:
                print(f"[+] Cracked: {h} -> {word}")
                cracked.append((h, word))
                break
        else:
            print(f"[-] Could not crack: {h}")
    return cracked

def save_results(cracked, output_file="cracked.txt"):
    with open(output_file, 'w') as file:
        for h, word in cracked:
            file.write(f"{h} : {word}\n")

def main():
    hashes = load_hashes("hashes.txt")
    wordlist = load_wordlist("wordlist.txt")
    cracked = crack_hashes(hashes, wordlist)
    save_results(cracked)

if __name__ == "__main__":
    main()
