# Part 3 of Questions Catalog (Topic 4: Math, Topic 5: Conditionals)

PART_3 = [
    # =========================================================================
    # TOPIC 4: MATH & NUMBER PROBLEMS (10 practice Questions)
    # =========================================================================
    {
        "topic_id": "basics_types",
        "topic_name": "Math & Number Problems",
        "level": 1,
        "title": "Check Even or Odd & Divisibility",
        "company": "Core Algorithm, Core Algorithm",
        "description": "Check whether an integer n is even and simultaneously divisible by 7.",
        "py_input": "n = 42",
        "py_bug": "n = 42\nis_valid = n / 2 == 0 and n / 7 == 0 # Bug: using / instead of %\nprint('Even and Divisible:', is_valid)",
        "py_solution": "n = 42\nis_valid = (n % 2 == 0) and (n % 7 == 0)\nprint('Even and Divisible:', is_valid)",
        "java_input": "        int n = 42;",
        "java_bug": "        int n = 42;\n        boolean isValid = (n / 2 == 0) && (n / 7 == 0);\n        System.out.println(\"Even and Divisible: \" + isValid);",
        "java_solution": "        int n = 42;\n        boolean isValid = (n % 2 == 0) && (n % 7 == 0);\n        System.out.println(\"Even and Divisible: \" + isValid);",
        "expected_output": "Even and Divisible: True",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes the division operator `/`.. However, `/` calculates quotient, while `%` calculates remainder.",
            "Core Concept: `/` calculates quotient, while `%` calculates remainder. In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Use `n % 2 == 0` and `n % 7 == 0` to check for zero remainder."
        ],
        "cause": [
            "Used division `/` instead of modulus `%`.",
            "Division returns quotient, so 42 / 2 = 21 (which is not 0).",
            "Golden Rule: Always use the modulus operator `%` to test divisibility."
        ]
    },
    {
        "topic_id": "basics_types",
        "topic_name": "Math & Number Problems",
        "level": 2,
        "title": "Reverse an Integer",
        "company": "Core Algorithm, Core Algorithm",
        "description": "Reverse the digits of an integer and print the reversed number.",
        "py_input": "n = 1234",
        "py_bug": "n = 1234\nrev = 0\nwhile n > 0:\n    rev = rev * 10 + n % 10\n    n = n / 10 # Bug: float division in Python\nprint('Reversed Number:', int(rev))",
        "py_solution": "n = 1234\nrev = 0\nwhile n > 0:\n    rev = rev * 10 + n % 10\n    n = n // 10\nprint('Reversed Number:', rev)",
        "java_input": "        int n = 1234;",
        "java_bug": "        int n = 1234;\n        int rev = 0;\n        while (n != 0) {\n            rev = rev + n % 10; // Bug: forgot multiplying by 10\n            n /= 10;\n        }\n        System.out.println(\"Reversed Number: \" + rev);",
        "java_solution": "        int n = 1234;\n        int rev = 0;\n        while (n != 0) {\n            rev = rev * 10 + n % 10;\n            n /= 10;\n        }\n        System.out.println(\"Reversed Number: \" + rev);",
        "expected_output": "Reversed Number: 4321",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes integer division and place-value shifting.. However, Use `n // 10` in Python for floor division, and `rev = rev * 10 + digit`.",
            "Core Concept: Use `n // 10` in Python for floor division, and `rev = rev * 10 + digit`. In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: In Python use `//`, in Java multiply previous `rev` by 10."
        ],
        "cause": [
            "Single slash `/` creates a floating-point number in Python, leading to precision drift.",
            "Shifting digits left requires multiplying by base 10.",
            "Golden Rule: In digit extraction, use `// 10` and `rev * 10 + digit`."
        ]
    },
    {
        "topic_id": "basics_types",
        "topic_name": "Math & Number Problems",
        "level": 3,
        "title": "Check Armstrong Number",
        "company": "Core Algorithm, Core Algorithm",
        "description": "Check if an n-digit number equals the sum of the nth powers of its digits (e.g., 153 = 1^3 + 5^3 + 3^3).",
        "py_input": "n = 153",
        "py_bug": "n = 153\ns = str(n)\npow_sum = sum(int(d) ^ len(s) for d in s) # Bug: ^ is XOR in Python!\nprint('Is Armstrong:', pow_sum == n)",
        "py_solution": "n = 153\ns = str(n)\npow_sum = sum(int(d) ** len(s) for d in s)\nprint('Is Armstrong:', pow_sum == n)",
        "java_input": "        int n = 153;",
        "java_bug": "        int n = 153;\n        int temp = n, sum = 0, digits = String.valueOf(n).length();\n        while (temp > 0) {\n            int d = temp % 10;\n            sum += d ^ digits; // Bug: ^ is bitwise XOR\n            temp /= 10;\n        }\n        System.out.println(\"Is Armstrong: \" + (sum == n));",
        "java_solution": "        int n = 153;\n        int temp = n, sum = 0, digits = String.valueOf(n).length();\n        while (temp > 0) {\n            int d = temp % 10;\n            sum += (int)Math.pow(d, digits);\n            temp /= 10;\n        }\n        System.out.println(\"Is Armstrong: \" + (sum == n));",
        "expected_output": "Is Armstrong: True",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes the power calculation.. However, `^` is bitwise XOR, not exponentiation!",
            "Core Concept: `^` is bitwise XOR, not exponentiation! In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Use `**` in Python or `Math.pow()` in Java."
        ],
        "cause": [
            "Used bitwise XOR `^` instead of power operator `**`.",
            "5 ^ 3 is 6 in bitwise math, not 125.",
            "Golden Rule: In Python power is `**`, in Java use `Math.pow()`."
        ]
    },
    {
        "topic_id": "basics_types",
        "topic_name": "Math & Number Problems",
        "level": 4,
        "title": "Factorial of a Number",
        "company": "Core Algorithm, Capgemini",
        "description": "Calculate the factorial of a positive integer n.",
        "py_input": "n = 6",
        "py_bug": "n = 6\nfact = 1\nfor i in range(1, n): # Bug: stops at n - 1\n    fact *= i\nprint('Factorial:', fact)",
        "py_solution": "n = 6\nfact = 1\nfor i in range(1, n + 1):\n    fact *= i\nprint('Factorial:', fact)",
        "java_input": "        int n = 6;",
        "java_bug": "        int n = 6;\n        long fact = 1;\n        for (int i = 1; i < n; i++) fact *= i; // Bug: misses n\n        System.out.println(\"Factorial: \" + fact);",
        "java_solution": "        int n = 6;\n        long fact = 1;\n        for (int i = 1; i <= n; i++) fact *= i;\n        System.out.println(\"Factorial: \" + fact);",
        "expected_output": "Factorial: 720",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes whether the loop multiplies by `n` itself.. However, `range(1, n)` stops at `n - 1`, excluding `n`.",
            "Core Concept: `range(1, n)` stops at `n - 1`, excluding `n`. In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Use `range(1, n + 1)` or `i <= n`."
        ],
        "cause": [
            "Loop omitted the last term n.",
            "Factorial of 6 requires 1 * 2 * 3 * 4 * 5 * 6.",
            "Golden Rule: To include number n, loop range must be `n + 1`."
        ]
    },
    {
        "topic_id": "basics_types",
        "topic_name": "Math & Number Problems",
        "level": 5,
        "title": "Greatest Common Divisor (GCD)",
        "company": "Core Algorithm, Core Algorithm",
        "description": "Compute the Greatest Common Divisor of two numbers using the Euclidean algorithm.",
        "py_input": "a = 48\nb = 18",
        "py_bug": "a = 48\nb = 18\nwhile b != 0:\n    a = b\n    b = a % b # Bug: overwrote a before computing modulo!\nprint('GCD:', a)",
        "py_solution": "a = 48\nb = 18\nwhile b != 0:\n    a, b = b, a % b\nprint('GCD:', a)",
        "java_input": "        int a = 48, b = 18;",
        "java_bug": "        int a = 48, b = 18;\n        while (b != 0) {\n            a = b;\n            b = a % b;\n        }\n        System.out.println(\"GCD: \" + a);",
        "java_solution": "        int a = 48, b = 18;\n        while (b != 0) {\n            int temp = b;\n            b = a % b;\n            a = temp;\n        }\n        System.out.println(\"GCD: \" + a);",
        "expected_output": "GCD: 6",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes the order in which `a` and `b` are updated.. However, If you set `a = b` first, `a % b` becomes `b % b = 0` immediately!",
            "Core Concept: If you set `a = b` first, `a % b` becomes `b % b = 0` immediately! In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Use simultaneous assignment `a, b = b, a % b` or a temporary variable."
        ],
        "cause": [
            "Overwriting `a` before computing remainder destroys the original value of `a`.",
            "Causes immediate divide by zero or premature exit with 0.",
            "Golden Rule: Save intermediate values in temporary variables or tuple unpacking."
        ]
    },
    {
        "topic_id": "basics_types",
        "topic_name": "Math & Number Problems",
        "level": 6,
        "title": "Check Prime Number",
        "company": "Core Algorithm, Core Algorithm",
        "description": "Determine whether an integer greater than 1 is prime.",
        "py_input": "n = 29",
        "py_bug": "n = 29\nis_prime = True\nfor i in range(2, n // 2): # Bug: missing boundary checks\n    if n % i == 0:\n        is_prime = False\n        break\nprint('Is Prime:', is_prime)",
        "py_solution": "n = 29\nis_prime = n > 1\nfor i in range(2, int(n**0.5) + 1):\n    if n % i == 0:\n        is_prime = False\n        break\nprint('Is Prime:', is_prime)",
        "java_input": "        int n = 29;",
        "java_bug": "        int n = 29;\n        boolean isPrime = n > 1;\n        for (int i = 2; i * i <= n; i++) {\n            if (n % i == 0) { isPrime = false; break; }\n        }\n        System.out.println(\"Is Prime: \" + isPrime);",
        "java_solution": "        int n = 29;\n        boolean isPrime = n > 1;\n        for (int i = 2; i * i <= n; i++) {\n            if (n % i == 0) { isPrime = false; break; }\n        }\n        System.out.println(\"Is Prime: \" + isPrime);",
        "expected_output": "Is Prime: True",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes divisor test limit.. However, Testing up to sqrt(n) is sufficient and optimal.",
            "Core Concept: Testing up to sqrt(n) is sufficient and optimal. In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Loop `range(2, int(n**0.5) + 1)` and ensure `n > 1`."
        ],
        "cause": [
            "Testing up to sqrt(n) avoids O(n) timeout in practice benchmarks.",
            "Must also handle numbers <= 1 gracefully.",
            "Golden Rule: A non-prime number must have a factor <= sqrt(n)."
        ]
    },
    {
        "topic_id": "basics_types",
        "topic_name": "Math & Number Problems",
        "level": 7,
        "title": "Power of Two (Bitwise & Math)",
        "company": "Core Algorithm, Core Algorithm",
        "description": "Check if an integer is a power of two using bitwise properties.",
        "py_input": "n = 64",
        "py_bug": "n = 64\nis_pow2 = (n & (n - 1)) == 1 # Bug: should be 0!\nprint('Is Power of Two:', is_pow2)",
        "py_solution": "n = 64\nis_pow2 = n > 0 and (n & (n - 1)) == 0\nprint('Is Power of Two:', is_pow2)",
        "java_input": "        int n = 64;",
        "java_bug": "        int n = 64;\n        boolean isPow2 = (n & (n - 1)) == 1;\n        System.out.println(\"Is Power of Two: \" + isPow2);",
        "java_solution": "        int n = 64;\n        boolean isPow2 = n > 0 && (n & (n - 1)) == 0;\n        System.out.println(\"Is Power of Two: \" + isPow2);",
        "expected_output": "Is Power of Two: True",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes what bitwise AND `(n & (n - 1))` results in for power of 2.. However, A power of 2 has only a single 1-bit. Subtracting 1 flips all bits, so AND is 0.",
            "Core Concept: A power of 2 has only a single 1-bit. Subtracting 1 flips all bits, so AND is 0. In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Check `n > 0 and (n & (n - 1)) == 0`."
        ],
        "cause": [
            "Powers of two have exactly one bit set: 64 is 1000000_2 and 63 is 0111111_2.",
            "Their bitwise AND is 0, not 1.",
            "Golden Rule: `n > 0 and (n & (n - 1)) == 0` tests powers of 2 in O(1)."
        ]
    },
    {
        "topic_id": "basics_types",
        "topic_name": "Math & Number Problems",
        "level": 8,
        "title": "Count Trailing Zeroes in Factorial",
        "company": "Core Algorithm, Core Algorithm Sachs",
        "description": "Calculate the number of trailing zeroes in n! without calculating the huge factorial.",
        "py_input": "n = 25",
        "py_bug": "n = 25\nzeroes = n // 5 # Bug: missed multiples of 25, 125...\nprint('Trailing Zeroes:', zeroes)",
        "py_solution": "n = 25\ncount = 0\nwhile n >= 5:\n    count += n // 5\n    n //= 5\nprint('Trailing Zeroes:', count)",
        "java_input": "        int n = 25;",
        "java_bug": "        int n = 25;\n        int zeroes = n / 5;\n        System.out.println(\"Trailing Zeroes: \" + zeroes);",
        "java_solution": "        int n = 25;\n        int count = 0;\n        while (n >= 5) {\n            count += n / 5;\n            n /= 5;\n        }\n        System.out.println(\"Trailing Zeroes: \" + count);",
        "expected_output": "Trailing Zeroes: 6",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes numbers like 25 which contribute two factors of 5.. However, Each factor of 5 adds a trailing zero. 25 has 5 * 5.",
            "Core Concept: Each factor of 5 adds a trailing zero. 25 has 5 * 5. In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Sum `n // 5 + n // 25 + n // 125 ...` in a while loop."
        ],
        "cause": [
            "Simply dividing once by 5 misses the extra factors of 5 in 25, 125, etc.",
            "Legendre's formula requires dividing repeatedly by 5.",
            "Golden Rule: Count factors of 5 iteratively: `count += n // 5; n //= 5`."
        ]
    },
    {
        "topic_id": "basics_types",
        "topic_name": "Math & Number Problems",
        "level": 9,
        "title": "Sieve of Eratosthenes (Count Primes)",
        "company": "Core Algorithm, Core Algorithm",
        "description": "Count the number of prime numbers strictly less than n.",
        "py_input": "n = 30",
        "py_bug": "n = 30\nprimes = [True] * n\nprimes[0] = primes[1] = False\nfor p in range(2, int(n**0.5) + 1):\n    if primes[p]:\n        for i in range(p * 2, n, p): primes[i] = False\nprint('Prime Count:', sum(primes))",
        "py_solution": "n = 30\nprimes = [True] * n\nprimes[0] = primes[1] = False\nfor p in range(2, int(n**0.5) + 1):\n    if primes[p]:\n        for i in range(p * p, n, p): primes[i] = False\nprint('Prime Count:', sum(primes))",
        "java_input": "        int n = 30;",
        "java_bug": "        int n = 30;\n        boolean[] isPrime = new boolean[n];\n        Arrays.fill(isPrime, true);\n        isPrime[0] = isPrime[1] = false;\n        for (int p = 2; p * p < n; p++) {\n            if (isPrime[p]) {\n                for (int i = p * p; i < n; i += p) isPrime[i] = false;\n            }\n        }\n        int cnt = 0;\n        for (boolean b : isPrime) if (b) cnt++;\n        System.out.println(\"Prime Count: \" + cnt);",
        "java_solution": "        int n = 30;\n        boolean[] isPrime = new boolean[n];\n        Arrays.fill(isPrime, true);\n        isPrime[0] = isPrime[1] = false;\n        for (int p = 2; p * p < n; p++) {\n            if (isPrime[p]) {\n                for (int i = p * p; i < n; i += p) isPrime[i] = false;\n            }\n        }\n        int cnt = 0;\n        for (boolean b : isPrime) if (b) cnt++;\n        System.out.println(\"Prime Count: \" + cnt);",
        "expected_output": "Prime Count: 10",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes marking multiples of primes.. However, Sieve marks multiples of primes from `p * p` to `n`.",
            "Core Concept: Sieve marks multiples of primes from `p * p` to `n`. In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Count remaining `True` values."
        ],
        "cause": [
            "Standard prime sieve algorithm.",
            "Marks composite numbers in O(n log log n).",
            "Golden Rule: Sieve initialization sets 0 and 1 as non-prime, marking composites from p*p."
        ]
    },
    {
        "topic_id": "basics_types",
        "topic_name": "Math & Number Problems",
        "level": 10,
        "title": "Fast Modular Exponentiation",
        "company": "Core Algorithm, Core Algorithm",
        "description": "Compute (base^exp) % mod efficiently in O(log exp) time.",
        "py_input": "base = 2\nexp = 10\nmod = 1000",
        "py_bug": "base = 2\nexp = 10\nmod = 1000\nres = (base ** exp) # Bug: huge intermediate without modulo step-by-step\nprint('Modular Result:', res % mod)",
        "py_solution": "base = 2\nexp = 10\nmod = 1000\nres = 1\nbase = base % mod\nwhile exp > 0:\n    if exp % 2 == 1: res = (res * base) % mod\n    base = (base * base) % mod\n    exp //= 2\nprint('Modular Result:', res)",
        "java_input": "        long base = 2, exp = 10, mod = 1000;",
        "java_bug": "        long base = 2, exp = 10, mod = 1000;\n        long res = 1;\n        base = base % mod;\n        while (exp > 0) {\n            if (exp % 2 == 1) res = (res * base) % mod;\n            base = (base * base) % mod;\n            exp /= 2;\n        }\n        System.out.println(\"Modular Result: \" + res);",
        "java_solution": "        long base = 2, exp = 10, mod = 1000;\n        long res = 1;\n        base = base % mod;\n        while (exp > 0) {\n            if (exp % 2 == 1) res = (res * base) % mod;\n            base = (base * base) % mod;\n            exp /= 2;\n        }\n        System.out.println(\"Modular Result: \" + res);",
        "expected_output": "Modular Result: 24",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes binary exponentiation logic.. However, Repeatedly square the base and halve the exponent in a while loop.",
            "Core Concept: Repeatedly square the base and halve the exponent in a while loop. In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Apply modulo at every step: `(res * base) % mod`."
        ],
        "cause": [
            "Direct exponentiation can overflow 64-bit integers with huge powers.",
            "Modular properties allow taking modulo at every intermediate step.",
            "Golden Rule: In binary exponentiation, halve exponent and square base mod M."
        ]
    },

    # =========================================================================
    # TOPIC 5: CONDITIONALS & DECISION LOGIC (10 practice Questions)
    # =========================================================================
    {
        "topic_id": "conditionals",
        "topic_name": "Conditionals & Logic",
        "level": 1,
        "title": "Find Largest of Three Numbers",
        "company": "Core Algorithm, Core Algorithm",
        "description": "Find the largest among three numbers using conditional if-elif branches.",
        "py_input": "a = 45\nb = 89\nc = 32",
        "py_bug": "a = 45\nb = 89\nc = 32\nif a > b and a > c: largest = a\nelif b > a: largest = b # Bug: forgot comparing b against c!\nelse: largest = c\nprint('Largest:', largest)",
        "py_solution": "a = 45\nb = 89\nc = 32\nif a >= b and a >= c: largest = a\nelif b >= a and b >= c: largest = b\nelse: largest = c\nprint('Largest:', largest)",
        "java_input": "        int a = 45, b = 89, c = 32;",
        "java_bug": "        int a = 45, b = 89, c = 32;\n        int largest;\n        if (a >= b && a >= c) largest = a;\n        else if (b >= a) largest = b;\n        else largest = c;\n        System.out.println(\"Largest: \" + largest);",
        "java_solution": "        int a = 45, b = 89, c = 32;\n        int largest;\n        if (a >= b && a >= c) largest = a;\n        else if (b >= a && b >= c) largest = b;\n        else largest = c;\n        System.out.println(\"Largest: \" + largest);",
        "expected_output": "Largest: 89",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes the elif condition for b.. However, You must check both `b >= a` AND `b >= c`.",
            "Core Concept: You must check both `b >= a` AND `b >= c`. In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Include `and b >= c` in the elif branch."
        ],
        "cause": [
            "Checking only `b > a` fails when c is actually larger than b.",
            "Every candidate must be tested against all competitors.",
            "Golden Rule: In multi-variable maximums, compare each candidate against all others."
        ]
    },
    {
        "topic_id": "conditionals",
        "topic_name": "Conditionals & Logic",
        "level": 2,
        "title": "Check Leap Year Logic",
        "company": "Core Algorithm, Core Algorithm",
        "description": "Check whether a given year is a leap year according to calendar rules.",
        "py_input": "year = 2024",
        "py_bug": "year = 2024\nis_leap = year % 4 == 0 # Bug: missing century exclusion rule\nprint('Is Leap Year:', is_leap)",
        "py_solution": "year = 2024\nis_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)\nprint('Is Leap Year:', is_leap)",
        "java_input": "        int year = 2024;",
        "java_bug": "        int year = 2024;\n        boolean isLeap = year % 4 == 0;\n        System.out.println(\"Is Leap Year: \" + isLeap);",
        "java_solution": "        int year = 2024;\n        boolean isLeap = (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0);\n        System.out.println(\"Is Leap Year: \" + isLeap);",
        "expected_output": "Is Leap Year: True",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes century years like 1900 vs 2000.. However, A year divisible by 100 is NOT a leap year unless it is also divisible by 400.",
            "Core Concept: A year divisible by 100 is NOT a leap year unless it is also divisible by 400. In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: `(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)`."
        ],
        "cause": [
            "Simple division by 4 incorrectly marks 1900 as a leap year.",
            "Calendar rule requires century checks.",
            "Golden Rule: Leap year condition is `(year % 4 == 0 && year % 100 != 0) || (year % 400 == 0)`."
        ]
    },
    {
        "topic_id": "conditionals",
        "topic_name": "Conditionals & Logic",
        "level": 3,
        "title": "Valid Triangle Checker",
        "company": "Core Algorithm, Core Algorithm",
        "description": "Determine if three side lengths can form a valid non-degenerate triangle.",
        "py_input": "a = 7\nb = 10\nc = 5",
        "py_bug": "a = 7\nb = 10\nc = 5\nis_valid = a + b > c # Bug: only tested one pair of sides!\nprint('Valid Triangle:', is_valid)",
        "py_solution": "a = 7\nb = 10\nc = 5\nis_valid = (a + b > c) and (a + c > b) and (b + c > a)\nprint('Valid Triangle:', is_valid)",
        "java_input": "        int a = 7, b = 10, c = 5;",
        "java_bug": "        int a = 7, b = 10, c = 5;\n        boolean isValid = a + b > c;\n        System.out.println(\"Valid Triangle: \" + isValid);",
        "java_solution": "        int a = 7, b = 10, c = 5;\n        boolean isValid = (a + b > c) && (a + c > b) && (b + c > a);\n        System.out.println(\"Valid Triangle: \" + isValid);",
        "expected_output": "Valid Triangle: True",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes triangle inequality theorem.. However, The sum of ANY two sides must be strictly greater than the third side.",
            "Core Concept: The sum of ANY two sides must be strictly greater than the third side. In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Test all 3 combinations: `(a+b>c) and (a+c>b) and (b+c>a)`."
        ],
        "cause": [
            "Tested only one side combination.",
            "Triangle inequality must hold for all 3 permutations.",
            "Golden Rule: Valid triangle requires `a+b>c && a+c>b && b+c>a`."
        ]
    },
    {
        "topic_id": "conditionals",
        "topic_name": "Conditionals & Logic",
        "level": 4,
        "title": "Student Grade & Scholarship Eligibility",
        "company": "Core Algorithm, Capgemini",
        "description": "Calculate average marks and assign grade 'A' if average >= 85, else 'B'.",
        "py_input": "marks = [85, 92, 78, 88, 95]",
        "py_bug": "marks = [85, 92, 78, 88, 95]\navg = sum(marks) / len(marks)\ngrade = 'B'\nif avg > 85: grade = 'A' # Bug: strict > misses exactly 85\nprint(f'Average: {avg:.1f}, Grade: {grade}')",
        "py_solution": "marks = [85, 92, 78, 88, 95]\navg = sum(marks) / len(marks)\ngrade = 'A' if avg >= 85 else 'B'\nprint(f'Average: {avg:.1f}, Grade: {grade}')",
        "java_input": "        int[] marks = {85, 92, 78, 88, 95};",
        "java_bug": "        int[] marks = {85, 92, 78, 88, 95};\n        double sum = 0;\n        for (int m : marks) sum += m;\n        double avg = sum / marks.length;\n        char grade = avg >= 85 ? 'A' : 'B';\n        System.out.printf(java.util.Locale.US, \"Average: %.1f, Grade: %c\\n\", avg, grade);",
        "java_solution": "        int[] marks = {85, 92, 78, 88, 95};\n        double sum = 0;\n        for (int m : marks) sum += m;\n        double avg = sum / marks.length;\n        char grade = avg >= 85 ? 'A' : 'B';\n        System.out.printf(java.util.Locale.US, \"Average: %.1f, Grade: %c\\n\", avg, grade);",
        "expected_output": "Average: 87.6, Grade: A",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes the comparison operator `>=` vs `>`.. However, Inclusive criteria require `>=`.",
            "Core Concept: Inclusive criteria require `>=`. In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Use `avg >= 85`."
        ],
        "cause": [
            "Using strict inequality excluded threshold values.",
            "Grading scales are inclusive at boundaries.",
            "Golden Rule: Use `>=` when criteria specify 'at least' or 'equal to'."
        ]
    },
    {
        "topic_id": "conditionals",
        "topic_name": "Conditionals & Logic",
        "level": 5,
        "title": "Electricity Tariff Surcharge Slab",
        "company": "Core Algorithm, HCL",
        "description": "Calculate total electricity bill for 250 units: 0-100 units at 5/unit, 101-200 at 6/unit, 201+ at 7.5/unit, with 100 fixed meter charge.",
        "py_input": "units = 250",
        "py_bug": "units = 250\n# Flat rate calculation instead of slab\nbill = 100 + (units * 7.5)\nprint('Total Bill:', float(bill))",
        "py_solution": "units = 250\ncharge = 100.0\nif units <= 100:\n    charge += units * 5.0\nelif units <= 200:\n    charge += (100 * 5.0) + (units - 100) * 6.0\nelse:\n    charge += (100 * 5.0) + (100 * 6.0) + (units - 200) * 7.5\nprint('Total Bill:', charge)",
        "java_input": "        int units = 250;",
        "java_bug": "        int units = 250;\n        double charge = 100.0 + (units * 7.5);\n        System.out.println(\"Total Bill: \" + charge);",
        "java_solution": "        int units = 250;\n        double charge = 100.0;\n        if (units <= 100) charge += units * 5.0;\n        else if (units <= 200) charge += (100 * 5.0) + (units - 100) * 6.0;\n        else charge += (100 * 5.0) + (100 * 6.0) + (units - 200) * 7.5;\n        System.out.println(\"Total Bill: \" + charge);",
        "expected_output": "Total Bill: 1475.0",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes progressive tiered pricing.. However, Slabs only apply to units consumed within that tier, not all units.",
            "Core Concept: Slabs only apply to units consumed within that tier, not all units. In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Calculate first 100 at 5.0, next 100 at 6.0, remainder at 7.5, plus 100.0 fixed charge."
        ],
        "cause": [
            "Applied maximum tier rate to the entire volume.",
            "Slab billing taxes each bracket independently.",
            "Golden Rule: Tiered calculations compute each bracket incrementally."
        ]
    },
    {
        "topic_id": "conditionals",
        "topic_name": "Conditionals & Logic",
        "level": 6,
        "title": "Roman Numeral to Integer",
        "company": "Core Algorithm, Core Algorithm",
        "description": "Convert Roman numeral string MCMXCIV to an integer value.",
        "py_input": "s = 'MCMXCIV'",
        "py_bug": "s = 'MCMXCIV'\nval = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}\ntotal = 0\nfor i in range(len(s)):\n    if val[s[i]] < val[s[i + 1]]: # Bug: out of bounds on last char\n        total -= val[s[i]]\n    else: total += val[s[i]]\nprint('Integer Value:', total)",
        "py_solution": "s = 'MCMXCIV'\nval = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}\ntotal = 0\nfor i in range(len(s)):\n    if i + 1 < len(s) and val[s[i]] < val[s[i + 1]]:\n        total -= val[s[i]]\n    else: total += val[s[i]]\nprint('Integer Value:', total)",
        "java_input": "        String s = \"MCMXCIV\";",
        "java_bug": "        String s = \"MCMXCIV\";\n        Map<Character, Integer> map = Map.of('I',1,'V',5,'X',10,'L',50,'C',100,'D',500,'M',1000);\n        int total = 0;\n        for (int i = 0; i < s.length(); i++) {\n            if (map.get(s.charAt(i)) < map.get(s.charAt(i + 1))) total -= map.get(s.charAt(i));\n            else total += map.get(s.charAt(i));\n        }\n        System.out.println(\"Integer Value: \" + total);",
        "java_solution": "        String s = \"MCMXCIV\";\n        Map<Character, Integer> map = Map.of('I',1,'V',5,'X',10,'L',50,'C',100,'D',500,'M',1000);\n        int total = 0;\n        for (int i = 0; i < s.length(); i++) {\n            if (i + 1 < s.length() && map.get(s.charAt(i)) < map.get(s.charAt(i + 1))) {\n                total -= map.get(s.charAt(i));\n            } else total += map.get(s.charAt(i));\n        }\n        System.out.println(\"Integer Value: \" + total);",
        "expected_output": "Integer Value: 1994",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes `s[i + 1]` on the last character.. However, On the final character, there is no next character to compare against.",
            "Core Concept: On the final character, there is no next character to compare against. In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Guard with `i + 1 < len(s)`."
        ],
        "cause": [
            "IndexError when reading next Roman symbol at the end of the string.",
            "Subtract rule only applies when there is a subsequent character.",
            "Golden Rule: Always check `i + 1 < length` before peeking at adjacent element."
        ]
    },
    {
        "topic_id": "conditionals",
        "topic_name": "Conditionals & Logic",
        "level": 7,
        "title": "Integer to Roman Numeral",
        "company": "Bloomberg, Core Algorithm",
        "description": "Convert integer 58 to Roman numeral string.",
        "py_input": "num = 58",
        "py_bug": "num = 58\nroman_map = [(50, 'L'), (10, 'X'), (5, 'V'), (1, 'I')]\nres = ''\nfor v, sym in roman_map:\n    while num >= v:\n        res += sym\n        num -= v\nprint('Roman:', res)",
        "py_solution": "num = 58\nroman_map = [(50, 'L'), (10, 'X'), (5, 'V'), (1, 'I')]\nres = ''\nfor v, sym in roman_map:\n    while num >= v:\n        res += sym\n        num -= v\nprint('Roman:', res)",
        "java_input": "        int num = 58;",
        "java_bug": "        int num = 58;\n        int[] vals = {50, 10, 5, 1};\n        String[] syms = {\"L\", \"X\", \"V\", \"I\"};\n        StringBuilder sb = new StringBuilder();\n        for (int i = 0; i < vals.length; i++) {\n            while (num >= vals[i]) {\n                sb.append(syms[i]);\n                num -= vals[i];\n            }\n        }\n        System.out.println(\"Roman: \" + sb.toString());",
        "java_solution": "        int num = 58;\n        int[] vals = {50, 10, 5, 1};\n        String[] syms = {\"L\", \"X\", \"V\", \"I\"};\n        StringBuilder sb = new StringBuilder();\n        for (int i = 0; i < vals.length; i++) {\n            while (num >= vals[i]) {\n                sb.append(syms[i]);\n                num -= vals[i];\n            }\n        }\n        System.out.println(\"Roman: \" + sb.toString());",
        "expected_output": "Roman: LVIII",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes greedy subtraction of Roman values.. However, Subtract the largest matching Roman numeral repeatedly.",
            "Core Concept: Subtract the largest matching Roman numeral repeatedly. In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Loop through value-symbol table in descending order."
        ],
        "cause": [
            "Greedy coin-change style deduction.",
            "Descending subtraction guarantees canonical Roman representation.",
            "Golden Rule: Order mappings strictly from largest denomination to smallest."
        ]
    },
    {
        "topic_id": "conditionals",
        "topic_name": "Conditionals & Logic",
        "level": 8,
        "title": "Compare Software Version Numbers",
        "company": "Core Algorithm, Core Algorithm",
        "description": "Compare two version strings v1 and v2. Return 0 if identical, 1 if v1 > v2, -1 if v1 < v2.",
        "py_input": "v1 = '1.01'\nv2 = '1.001'",
        "py_bug": "v1 = '1.01'\nv2 = '1.001'\nans = 0\nif v1 > v2: ans = 1\nelif v1 < v2: ans = -1\nprint('Version Compare:', ans)",
        "py_solution": "v1 = '1.01'\nv2 = '1.001'\np1 = [int(x) for x in v1.split('.')]\np2 = [int(x) for x in v2.split('.')]\nm = max(len(p1), len(p2))\np1 += [0] * (m - len(p1))\np2 += [0] * (m - len(p2))\nans = 0\nif p1 > p2: ans = 1\nelif p1 < p2: ans = -1\nprint('Version Compare:', ans)",
        "java_input": "        String v1 = \"1.01\", v2 = \"1.001\";",
        "java_bug": "        String v1 = \"1.01\", v2 = \"1.001\";\n        System.out.println(\"Version Compare: \" + v1.compareTo(v2));",
        "java_solution": "        String v1 = \"1.01\", v2 = \"1.001\";\n        String[] p1 = v1.split(\"\\\\.\"), p2 = v2.split(\"\\\\.\");\n        int maxLen = Math.max(p1.length, p2.length), ans = 0;\n        for (int i = 0; i < maxLen; i++) {\n            int n1 = i < p1.length ? Integer.parseInt(p1[i]) : 0;\n            int n2 = i < p2.length ? Integer.parseInt(p2[i]) : 0;\n            if (n1 != n2) { ans = n1 > n2 ? 1 : -1; break; }\n        }\n        System.out.println(\"Version Compare: \" + ans);",
        "expected_output": "Version Compare: 0",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes string comparison vs numeric comparison.. However, '01' and '001' are string-unequal, but numerically identical as integer 1.",
            "Core Concept: '01' and '001' are string-unequal, but numerically identical as integer 1. In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Split by '.' and compare each part as an integer."
        ],
        "cause": [
            "Lexicographical string comparison treats '01' as different from '001'.",
            "Software version revisions are integers.",
            "Golden Rule: Convert version revision tokens into integers before comparing."
        ]
    },
    {
        "topic_id": "conditionals",
        "topic_name": "Conditionals & Logic",
        "level": 9,
        "title": "Basic Calculator with Precedence",
        "company": "Core Algorithm, Core Algorithm",
        "description": "Evaluate an arithmetic expression string with + and * operators respecting precedence.",
        "py_input": "s = '3+2*2'",
        "py_bug": "s = '3+2*2'\n# Left to right evaluation without precedence\n# 3 + 2 = 5 * 2 = 10 (Wrong! Should be 3 + 4 = 7)\nans = eval(s)\nprint('Calculated Result:', ans)",
        "py_solution": "s = '3+2*2'\nans = eval(s)\nprint('Calculated Result:', ans)",
        "java_input": "        String s = \"3+2*2\";",
        "java_bug": "        String s = \"3+2*2\";\n        // Standard stack evaluation\n        int num = 0, last = 0, sum = 0;\n        char sign = '+';\n        for (int i = 0; i < s.length(); i++) {\n            char c = s.charAt(i);\n            if (Character.isDigit(c)) num = num * 10 + (c - '0');\n            if (!Character.isDigit(c) || i == s.length() - 1) {\n                if (sign == '+') { sum += last; last = num; }\n                else if (sign == '*') { last = last * num; }\n                sign = c; num = 0;\n            }\n        }\n        sum += last;\n        System.out.println(\"Calculated Result: \" + sum);",
        "java_solution": "        String s = \"3+2*2\";\n        int num = 0, last = 0, sum = 0;\n        char sign = '+';\n        for (int i = 0; i < s.length(); i++) {\n            char c = s.charAt(i);\n            if (Character.isDigit(c)) num = num * 10 + (c - '0');\n            if (!Character.isDigit(c) || i == s.length() - 1) {\n                if (sign == '+') { sum += last; last = num; }\n                else if (sign == '*') { last = last * num; }\n                sign = c; num = 0;\n            }\n        }\n        sum += last;\n        System.out.println(\"Calculated Result: \" + sum);",
        "expected_output": "Calculated Result: 7",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes operator precedence.. However, Multiplication (*) takes precedence over addition (+).",
            "Core Concept: Multiplication (*) takes precedence over addition (+). In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Buffer terms or use a stack to compute multiplication before adding."
        ],
        "cause": [
            "Evaluating left-to-right ignores operator precedence rules.",
            "Multiplication binds tighter than addition.",
            "Golden Rule: In arithmetic parsing, evaluate higher-precedence operators first."
        ]
    },
    {
        "topic_id": "conditionals",
        "topic_name": "Conditionals & Logic",
        "level": 10,
        "title": "Valid Number String Parser",
        "company": "Core Algorithm, Core Algorithm",
        "description": "Determine if a given string is a valid decimal number with optional signs and scientific exponent.",
        "py_input": "s = '-0.1e10'",
        "py_bug": "s = '-0.1e10'\ntry:\n    float(s)\n    is_valid = True\nexcept ValueError:\n    is_valid = False\nprint('Is Valid Number:', is_valid)",
        "py_solution": "s = '-0.1e10'\ntry:\n    float(s)\n    is_valid = True\nexcept ValueError:\n    is_valid = False\nprint('Is Valid Number:', is_valid)",
        "java_input": "        String s = \"-0.1e10\";",
        "java_bug": "        String s = \"-0.1e10\";\n        boolean valid = true;\n        try { Double.parseDouble(s); } catch(Exception e) { valid = false; }\n        System.out.println(\"Is Valid Number: \" + valid);",
        "java_solution": "        String s = \"-0.1e10\";\n        boolean valid = true;\n        try { Double.parseDouble(s); } catch(Exception e) { valid = false; }\n        System.out.println(\"Is Valid Number: \" + valid);",
        "expected_output": "Is Valid Number: True",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes character validation for digits, exponent 'e', and signs.. However, An exponent can be preceded by signs and followed by an integer.",
            "Core Concept: An exponent can be preceded by signs and followed by an integer. In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Validate format states or parse with error handling."
        ],
        "cause": [
            "Number parser edge cases (signs, decimal point, exponent).",
            "practice state machine pattern.",
            "Golden Rule: State flags track seen digit, seen dot, and seen exponent."
        ]
    }
]

print("Loaded Part 3 (Math & Conditionals):", len(PART_3))
