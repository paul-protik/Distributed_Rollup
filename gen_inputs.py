import random, os, sys
ARRAY_LEN = 16; N_BITS = 16; SIGNED = True; MODULUS = 2**N_BITS
random.seed(int(sys.argv[1]) if len(sys.argv) > 1 else 42)
lo = -MODULUS//2 if SIGNED else 0
hi = MODULUS//2 - 1 if SIGNED else MODULUS - 1
plaintext = [random.randint(lo, hi) for _ in range(ARRAY_LEN)]
print("Plaintext:", plaintext)
print("Expected sorted:", sorted(plaintext))
os.makedirs("Player-Data", exist_ok=True)
shares = [[] for _ in range(3)]
for v in plaintext:
    v_mod = v % MODULUS
    s = [random.randrange(MODULUS) for _ in range(2)]
    s.append((v_mod - sum(s)) % MODULUS)
    for p in range(3): shares[p].append(s[p])
for p in range(3):
    path = f"Player-Data/Input-P{p}-0"
    open(path, "w").write("\n".join(str(x) for x in shares[p]) + "\n")
    print(f"Wrote {path}")
