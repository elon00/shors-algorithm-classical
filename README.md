# Shor's Algorithm — Classical Subroutines

A comprehensive, educational implementation of the **classical subroutines** behind Shor's quantum factoring algorithm — from beginner foundations to advanced end-to-end solutions.

## What is Shor's Algorithm?

Shor's algorithm factors composite numbers in **polynomial time** by using a quantum computer to find the **period** (order) of a modular exponential sequence. The quantum part finds the period exponentially faster than any known classical method — that's the revolutionary speedup.

This repository covers **everything classical**:

- The pre-processing and post-processing steps
- The modular arithmetic that powers the computation
- The continued fractions algorithm that extracts the period from quantum measurements
- Complete simulations showing HOW the pieces fit together

## Architecture

```
shors-classical/
├── shors_classical/          # Core library
│   ├── __init__.py           # Public API
│   ├── gcd.py                # Euclidean algorithm (Beginner)
│   ├── modular_arithmetic.py # Modular exponentiation & inverses (Beginner)
│   ├── continued_fractions.py # Continued fraction expansion (Intermediate)
│   ├── period_finding.py     # Period/order finding (Intermediate/Advanced)
│   └── shor_classical.py     # Complete algorithm (Advanced)
├── examples/                 # Step-by-step scripts
│   ├── 01_gcd_foundation.py
│   ├── 02_modular_arithmetic.py
│   ├── 03_continued_fractions.py
│   ├── 04_period_finding.py
│   ├── 05_full_shors_algorithm.py
│   ├── 06_quantum_simulation.py
│   └── 07_visualizing_periodicity.py
├── tests/                    # Comprehensive test suite
│   ├── test_gcd.py
│   ├── test_modular_arithmetic.py
│   ├── test_continued_fractions.py
│   ├── test_period_finding.py
│   └── test_shor_classical.py
└── notebooks/
    └── shors_walkthrough.ipynb
```

## Quick Start

### Installation

No installation needed — just clone and run:

```bash
git clone <repo-url>
cd shors-classical
pip install pytest  # only needed for tests
```

### Run the examples

```bash
python examples/01_gcd_foundation.py
python examples/03_continued_fractions.py
python examples/05_full_shors_algorithm.py
```

### Run tests

```bash
python -m pytest tests/ -v
```

## The Algorithm, Step by Step

### Step 1: Choose N and check trivial cases

If N is even or a prime power, factor immediately.

### Step 2: Pick a random a

Choose `a` such that `1 < a < N`. Compute `g = gcd(a, N)`. If `g != 1`, we got lucky — `g` is a factor.

### Step 3: Find the period r

This is the **hard part**. We need the smallest `r > 0` such that `a^r ≡ 1 (mod N)`.

| Method | Complexity | What it teaches |
|--------|-----------|-----------------|
| Brute force | O(r) | The baseline — too slow for large N |
| Quantum simulation | O(log N) | How the quantum computer does it |

The quantum approach:
1. Compute `a^x mod N` in superposition
2. Measure to get an approximation of `(j × Q) / r`
3. Use **continued fractions** to extract `r` from the approximation

### Step 4: Check r and compute factors

If `r` is even and `a^(r/2) ≢ ±1 (mod N)`:

```
p = gcd(a^(r/2) - 1, N)
q = gcd(a^(r/2) + 1, N)
```

Then `N = p × q`.

## Key Mathematical Concepts

### 1. Modular Exponentiation (Binary Exponentiation)

Computes `a^b mod n` in O(log b) steps. Essential for computing the modular sequence without overflow.

```
3^5 mod 7 → binary of 5 = 101
→ 3^1 * 3^4 mod 7 = 3 * 4 = 12 mod 7 = 5
```

### 2. Continued Fractions

The quantum computer doesn't give us `r` directly — it gives an approximation. Continued fractions extract the rational approximation:

```
measurement / Q ≈ j / r
→ Continued fraction expansion of measurement/Q
→ Convergents of the expansion
→ Denominator of convergent = candidate r
```

### 3. The Period (Order)

The period `r` of `a` modulo `N` is a divisor of `φ(N)` (Euler's totient). Finding it classically is exponentially hard; the quantum algorithm finds it in polynomial time.

## Example Walkthrough

```
Factoring N = 15

1. Pick a = 7 (gcd(7, 15) = 1)
2. Find period r = 4  (7^1=7, 7^2=4, 7^3=13, 7^4=1 mod 15)
3. r = 4 is even
4. Compute:
   a^(r/2) = 7^2 = 49 ≡ 4 (mod 15)
   p = gcd(4 - 1, 15) = gcd(3, 15) = 3
   q = gcd(4 + 1, 15) = gcd(5, 15) = 5
5. N = 15 = 3 × 5
```

## Running All Examples

```bash
# Beginner
python examples/01_gcd_foundation.py
python examples/02_modular_arithmetic.py

# Intermediate
python examples/03_continued_fractions.py
python examples/04_period_finding.py

# Advanced
python examples/05_full_shors_algorithm.py
python examples/06_quantum_simulation.py

# All Levels
python examples/07_visualizing_periodicity.py
```

## Advanced Notes

### Simulated Quantum Period Finding

The quantum part of Shor's algorithm cannot be run classically for large numbers. Our simulation demonstrates the **mathematical equivalence** by:

1. Generating a random measurement value that models quantum interference
2. Applying the continued fractions algorithm (same as on a real quantum computer)
3. Extracting candidate periods from the convergents

This is the ONLY part that needs a quantum computer — everything else runs on your laptop.

### Why This Matters

- **Classical factoring**: sub-exponential (GNFS), e.g., `O(exp(c × (log N)^(1/3) × (log log N)^(2/3)))`
- **Shor's algorithm**: polynomial, `O((log N)² × log log N × log 1/ε)`

For RSA-2048 (a 617-digit number), the difference is:
- Classical: billions of years
- Quantum (with enough qubits): hours
