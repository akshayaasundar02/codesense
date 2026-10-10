# Part 2 of Questions Catalog (Topic 2: Strings, Topic 3: Loops & Searching)

PART_2 = [
    # =========================================================================
    # TOPIC 2: STRINGS & TEXT PROCESSING (10 Placement Questions)
    # =========================================================================
    {
        "topic_id": "strings_hashmaps",
        "topic_name": "Strings & Text Processing",
        "level": 1,
        "title": "Check Palindrome String",
        "company": "Amazon, TCS Ninja",
        "description": "Check whether a given string reads identical forwards and backwards.",
        "py_input": "s = 'radar'",
        "py_bug": "s = 'radar'\nis_pal = True\nfor i in range(len(s)):\n    if s[i] != s[len(s) - i]:\n        is_pal = False\n        break\nprint('Is Palindrome:', is_pal)",
        "py_solution": "s = 'radar'\nis_pal = True\nfor i in range(len(s)):\n    if s[i] != s[len(s) - 1 - i]:\n        is_pal = False\n        break\nprint('Is Palindrome:', is_pal)",
        "java_input": "        String s = \"radar\";",
        "java_bug": "        String s = \"radar\";\n        boolean isPal = true;\n        for(int i = 0; i < s.length(); i++) {\n            if (s.charAt(i) != s.charAt(s.length() - i)) { isPal = false; break; }\n        }\n        System.out.println(\"Is Palindrome: \" + isPal);",
        "java_solution": "        String s = \"radar\";\n        boolean isPal = true;\n        for(int i = 0; i < s.length(); i++) {\n            if (s.charAt(i) != s.charAt(s.length() - 1 - i)) { isPal = false; break; }\n        }\n        System.out.println(\"Is Palindrome: \" + isPal);",
        "expected_output": "Is Palindrome: True",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes character indexing from the end.. However, String indices go from 0 to length - 1. When i = 0, length - i tries to access index 5.",
            "Core Concept: String indices go from 0 to length - 1. When i = 0, length - i tries to access index 5. In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Use s[len(s) - 1 - i] or s.charAt(s.length() - 1 - i)."
        ],
        "cause": [
            "Attempted to access index equal to string length at i=0.",
            "Characters in a 5-letter word are indexed 0, 1, 2, 3, 4.",
            "Golden Rule: In string mirror indexing, mirror of index i is length - 1 - i."
        ]
    },
    {
        "topic_id": "strings_hashmaps",
        "topic_name": "Strings & Text Processing",
        "level": 2,
        "title": "Reverse Words in a Sentence",
        "company": "Microsoft, Infosys",
        "description": "Reverse the order of words in a sentence while preserving word letters.",
        "py_input": "s = 'the sky is blue'",
        "py_bug": "s = 'the sky is blue'\nwords = s.split(' ')\n# Reversing words with out-of-range backward loop\nrev_words = []\nfor i in range(len(words), 0, -1):\n    rev_words.append(words[i])\nprint('Reversed Words:', ' '.join(rev_words))",
        "py_solution": "s = 'the sky is blue'\nwords = s.split(' ')\nrev_words = []\nfor i in range(len(words) - 1, -1, -1):\n    rev_words.append(words[i])\nprint('Reversed Words:', ' '.join(rev_words))",
        "java_input": "        String s = \"the sky is blue\";",
        "java_bug": "        String s = \"the sky is blue\";\n        String[] words = s.split(\" \");\n        StringBuilder sb = new StringBuilder();\n        for(int i = words.length; i >= 0; i--) {\n            sb.append(words[i]).append(i > 0 ? \" \" : \"\");\n        }\n        System.out.println(\"Reversed Words: \" + sb.toString());",
        "java_solution": "        String s = \"the sky is blue\";\n        String[] words = s.split(\" \");\n        StringBuilder sb = new StringBuilder();\n        for(int i = words.length - 1; i >= 0; i--) {\n            sb.append(words[i]).append(i > 0 ? \" \" : \"\");\n        }\n        System.out.println(\"Reversed Words: \" + sb.toString());",
        "expected_output": "Reversed Words: blue is sky the",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes the start index of the backward word loop.. However, If there are 4 words, words[4] crashes.",
            "Core Concept: If there are 4 words, words[4] crashes. In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Start from len(words) - 1 or words.length - 1."
        ],
        "cause": [
            "Word array index 4 is out of bounds for a 4-word array.",
            "Array indices stop at length - 1.",
            "Golden Rule: Backward iterations must start at size - 1."
        ]
    },
    {
        "topic_id": "strings_hashmaps",
        "topic_name": "Strings & Text Processing",
        "level": 3,
        "title": "Check Valid Anagram",
        "company": "Adobe, Cognizant",
        "description": "Determine if string s2 is an anagram of string s1 (contains identical characters with same counts).",
        "py_input": "s1 = 'anagram'\ns2 = 'nagaram'",
        "py_bug": "s1 = 'anagram'\ns2 = 'nagaram'\nis_anagram = sorted(s1) == s2 # Bug: comparing sorted list with unsorted string\nprint('Is Anagram:', is_anagram)",
        "py_solution": "s1 = 'anagram'\ns2 = 'nagaram'\nis_anagram = sorted(s1) == sorted(s2)\nprint('Is Anagram:', is_anagram)",
        "java_input": "        String s1 = \"anagram\";\n        String s2 = \"nagaram\";",
        "java_bug": "        String s1 = \"anagram\";\n        String s2 = \"nagaram\";\n        char[] c1 = s1.toCharArray();\n        java.util.Arrays.sort(c1);\n        System.out.println(\"Is Anagram: \" + new String(c1).equals(s2));",
        "java_solution": "        String s1 = \"anagram\";\n        String s2 = \"nagaram\";\n        char[] c1 = s1.toCharArray();\n        char[] c2 = s2.toCharArray();\n        java.util.Arrays.sort(c1);\n        java.util.Arrays.sort(c2);\n        System.out.println(\"Is Anagram: \" + java.util.Arrays.equals(c1, c2));",
        "expected_output": "Is Anagram: True",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes what you are comparing s1 to.. However, You must sort BOTH strings before comparing them.",
            "Core Concept: You must sort BOTH strings before comparing them. In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Compare sorted(s1) == sorted(s2)."
        ],
        "cause": [
            "Compared sorted characters against an unsorted string.",
            "Anagram check requires canonical forms (both sorted) or frequency counts.",
            "Golden Rule: Anagrams match only when both strings have identical sorted orders."
        ]
    },
    {
        "topic_id": "strings_hashmaps",
        "topic_name": "Strings & Text Processing",
        "level": 4,
        "title": "First Non-Repeating Character",
        "company": "Google, Amazon",
        "description": "Find the first character in a string that appears only once.",
        "py_input": "s = 'swiss'",
        "py_bug": "s = 'swiss'\ncounts = {}\nfor c in s:\n    counts[c] = counts.get(c, 0) + 1\nfirst_uniq = None\nfor i in range(len(s) + 1):\n    if counts[s[i]] == 1:\n        first_uniq = s[i]\n        break\nprint('First Non-Repeating:', first_uniq)",
        "py_solution": "s = 'swiss'\ncounts = {}\nfor c in s:\n    counts[c] = counts.get(c, 0) + 1\nfirst_uniq = None\nfor c in s:\n    if counts[c] == 1:\n        first_uniq = c\n        break\nprint('First Non-Repeating:', first_uniq)",
        "java_input": "        String s = \"swiss\";",
        "java_bug": "        String s = \"swiss\";\n        Map<Character, Integer> counts = new HashMap<>();\n        for(char c : s.toCharArray()) counts.put(c, counts.getOrDefault(c, 0) + 1);\n        Character first = null;\n        for(int i = 0; i <= s.length(); i++) {\n            if (counts.get(s.charAt(i)) == 1) { first = s.charAt(i); break; }\n        }\n        System.out.println(\"First Non-Repeating: \" + first);",
        "java_solution": "        String s = \"swiss\";\n        Map<Character, Integer> counts = new HashMap<>();\n        for(char c : s.toCharArray()) counts.put(c, counts.getOrDefault(c, 0) + 1);\n        Character first = null;\n        for(int i = 0; i < s.length(); i++) {\n            if (counts.get(s.charAt(i)) == 1) { first = s.charAt(i); break; }\n        }\n        System.out.println(\"First Non-Repeating: \" + first);",
        "expected_output": "First Non-Repeating: w",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes the second loop iterating through string indices.. However, range(len(s) + 1) or i <= s.length() exceeds string length.",
            "Core Concept: range(len(s) + 1) or i <= s.length() exceeds string length. In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Loop directly over characters in s or stop at i < len(s)."
        ],
        "cause": [
            "Attempted to read index 5 in a 5-character string.",
            "Index is off-by-one at the upper bound.",
            "Golden Rule: String charAt index must be strictly less than string length."
        ]
    },
    {
        "topic_id": "strings_hashmaps",
        "topic_name": "Strings & Text Processing",
        "level": 5,
        "title": "Count Vowels and Consonants",
        "company": "TCS Ninja, Wipro",
        "description": "Count total number of vowels and consonants in a given word.",
        "py_input": "s = 'interview'",
        "py_bug": "s = 'interview'\nvowels = 'aeiou'\nv_count = 0\nc_count = 0\nfor i in range(len(s) + 1):\n    if s[i] in vowels: v_count += 1\n    else: c_count += 1\nprint(f'Vowels: {v_count}, Consonants: {c_count}')",
        "py_solution": "s = 'interview'\nvowels = 'aeiou'\nv_count = 0\nc_count = 0\nfor c in s:\n    if c.lower() in vowels: v_count += 1\n    elif c.isalpha(): c_count += 1\nprint(f'Vowels: {v_count}, Consonants: {c_count}')",
        "java_input": "        String s = \"interview\";",
        "java_bug": "        String s = \"interview\";\n        int v = 0, c = 0;\n        String vowels = \"aeiou\";\n        for(int i = 0; i <= s.length(); i++) {\n            if (vowels.indexOf(s.charAt(i)) != -1) v++;\n            else c++;\n        }\n        System.out.println(\"Vowels: \" + v + \", Consonants: \" + c);",
        "java_solution": "        String s = \"interview\";\n        int v = 0, c = 0;\n        String vowels = \"aeiou\";\n        for(int i = 0; i < s.length(); i++) {\n            if (vowels.indexOf(s.charAt(i)) != -1) v++;\n            else c++;\n        }\n        System.out.println(\"Vowels: \" + v + \", Consonants: \" + c);",
        "expected_output": "Vowels: 4, Consonants: 5",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes the loop range.. However, Stop at len(s) rather than len(s) + 1.",
            "Core Concept: Stop at len(s) rather than len(s) + 1. In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Loop directly with `for c in s:` in Python or `i < s.length()` in Java."
        ],
        "cause": [
            "StringIndexOutOfBoundsException at final iteration.",
            "Indices for a string of length N are 0 through N - 1.",
            "Golden Rule: Iterating directly over characters avoids off-by-one errors."
        ]
    },
    {
        "topic_id": "strings_hashmaps",
        "topic_name": "Strings & Text Processing",
        "level": 6,
        "title": "Longest Common Prefix",
        "company": "Google, Microsoft",
        "description": "Find the longest common prefix string amongst an array of strings.",
        "py_input": "strs = ['flower', 'flow', 'flight']",
        "py_bug": "strs = ['flower', 'flow', 'flight']\nprefix = strs[0]\nfor i in range(1, len(strs) + 1):\n    while not strs[i].startswith(prefix):\n        prefix = prefix[:-1]\nprint('Common Prefix:', prefix)",
        "py_solution": "strs = ['flower', 'flow', 'flight']\nprefix = strs[0]\nfor i in range(1, len(strs)):\n    while not strs[i].startswith(prefix):\n        prefix = prefix[:-1]\n        if not prefix: break\nprint('Common Prefix:', prefix)",
        "java_input": "        String[] strs = {\"flower\", \"flow\", \"flight\"};",
        "java_bug": "        String[] strs = {\"flower\", \"flow\", \"flight\"};\n        String prefix = strs[0];\n        for(int i = 1; i <= strs.length; i++) {\n            while (!strs[i].startsWith(prefix)) {\n                prefix = prefix.substring(0, prefix.length() - 1);\n            }\n        }\n        System.out.println(\"Common Prefix: \" + prefix);",
        "java_solution": "        String[] strs = {\"flower\", \"flow\", \"flight\"};\n        String prefix = strs[0];\n        for(int i = 1; i < strs.length; i++) {\n            while (!strs[i].startsWith(prefix)) {\n                prefix = prefix.substring(0, prefix.length() - 1);\n            }\n        }\n        System.out.println(\"Common Prefix: \" + prefix);",
        "expected_output": "Common Prefix: fl",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes the string array loop bound.. However, strs has 3 items (indices 0, 1, 2). i = 3 is out of range.",
            "Core Concept: strs has 3 items (indices 0, 1, 2). i = 3 is out of range. In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Use `range(1, len(strs))` in Python or `i < strs.length` in Java."
        ],
        "cause": [
            "Loop attempted to inspect strs[3] in a 3-element list.",
            "Array length is 3, valid indices are 0 to 2.",
            "Golden Rule: Loop bounds must never reach the array length."
        ]
    },
    {
        "topic_id": "strings_hashmaps",
        "topic_name": "Strings & Text Processing",
        "level": 7,
        "title": "String Compression (Run-Length)",
        "company": "Bloomberg, Amazon",
        "description": "Compress a string by replacing consecutive repeating characters with count.",
        "py_input": "s = 'aabcccccaaa'",
        "py_bug": "s = 'aabcccccaaa'\nres = []\ncount = 1\nfor i in range(len(s)):\n    if s[i] == s[i + 1]: count += 1\n    else:\n        res.append(s[i] + str(count))\n        count = 1\nprint('Compressed:', ''.join(res))",
        "py_solution": "s = 'aabcccccaaa'\nres = []\ncount = 1\nfor i in range(len(s)):\n    if i + 1 < len(s) and s[i] == s[i + 1]: count += 1\n    else:\n        res.append(s[i] + str(count))\n        count = 1\nprint('Compressed:', ''.join(res))",
        "java_input": "        String s = \"aabcccccaaa\";",
        "java_bug": "        String s = \"aabcccccaaa\";\n        StringBuilder sb = new StringBuilder();\n        int count = 1;\n        for(int i = 0; i < s.length(); i++) {\n            if (s.charAt(i) == s.charAt(i + 1)) count++;\n            else { sb.append(s.charAt(i)).append(count); count = 1; }\n        }\n        System.out.println(\"Compressed: \" + sb.toString());",
        "java_solution": "        String s = \"aabcccccaaa\";\n        StringBuilder sb = new StringBuilder();\n        int count = 1;\n        for(int i = 0; i < s.length(); i++) {\n            if (i + 1 < s.length() && s.charAt(i) == s.charAt(i + 1)) count++;\n            else { sb.append(s.charAt(i)).append(count); count = 1; }\n        }\n        System.out.println(\"Compressed: \" + sb.toString());",
        "expected_output": "Compressed: a2b1c5a3",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes what happens when i reaches the last character in s[i + 1].. However, On the last character, i + 1 points outside the string.",
            "Core Concept: On the last character, i + 1 points outside the string. In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Guard with `i + 1 < len(s)` before checking `s[i] == s[i + 1]`."
        ],
        "cause": [
            "Accessing s[i + 1] at the last character triggers IndexError.",
            "Lookahead comparisons must check bounds before accessing.",
            "Golden Rule: Always check `i + 1 < length` before accessing `s[i + 1]`."
        ]
    },
    {
        "topic_id": "strings_hashmaps",
        "topic_name": "Strings & Text Processing",
        "level": 8,
        "title": "Valid Palindrome with Special Characters",
        "company": "Meta, Apple",
        "description": "Determine if a string is palindrome after converting all uppercase letters to lowercase and removing non-alphanumeric characters.",
        "py_input": "s = 'A man, a plan, a canal: Panama'",
        "py_bug": "s = 'A man, a plan, a canal: Panama'\ncleaned = [c.lower() for c in s if c.isalnum()]\nis_pal = cleaned == cleaned[::-1]\nprint('Is Valid Palindrome:', is_pal)",
        "py_solution": "s = 'A man, a plan, a canal: Panama'\ncleaned = [c.lower() for c in s if c.isalnum()]\nis_pal = cleaned == cleaned[::-1]\nprint('Is Valid Palindrome:', is_pal)",
        "java_input": "        String s = \"A man, a plan, a canal: Panama\";",
        "java_bug": "        String s = \"A man, a plan, a canal: Panama\";\n        String clean = s.replaceAll(\"[^a-zA-Z0-9]\", \"\").toLowerCase();\n        String rev = new StringBuilder(clean).reverse().toString();\n        System.out.println(\"Is Valid Palindrome: \" + clean.equals(rev));",
        "java_solution": "        String s = \"A man, a plan, a canal: Panama\";\n        String clean = s.replaceAll(\"[^a-zA-Z0-9]\", \"\").toLowerCase();\n        String rev = new StringBuilder(clean).reverse().toString();\n        System.out.println(\"Is Valid Palindrome: \" + clean.equals(rev));",
        "expected_output": "Is Valid Palindrome: True",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes how you filter and compare.. However, Keep only alphanumeric characters and compare in lowercase.",
            "Core Concept: Keep only alphanumeric characters and compare in lowercase. In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Filter with c.isalnum() and check equality."
        ],
        "cause": [
            "Punctuation and case sensitivity must be normalized.",
            "Standard interview requirement for palindrome string checking.",
            "Golden Rule: Normalize casing and filter symbols before checking palindrome."
        ]
    },
    {
        "topic_id": "strings_hashmaps",
        "topic_name": "Strings & Text Processing",
        "level": 9,
        "title": "Group Anagrams",
        "company": "Uber, Amazon",
        "description": "Group an array of strings into anagram clusters and print the total number of distinct clusters.",
        "py_input": "words = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']",
        "py_bug": "words = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']\ngroups = {}\nfor w in words:\n    k = ''.join(sorted(w))\n    if k not in groups: groups[k] = []\n    groups[k].append(w)\nprint('Group Count:', len(groups))",
        "py_solution": "words = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']\ngroups = {}\nfor w in words:\n    k = ''.join(sorted(w))\n    if k not in groups: groups[k] = []\n    groups[k].append(w)\nprint('Group Count:', len(groups))",
        "java_input": "        String[] words = {\"eat\", \"tea\", \"tan\", \"ate\", \"nat\", \"bat\"};",
        "java_bug": "        String[] words = {\"eat\", \"tea\", \"tan\", \"ate\", \"nat\", \"bat\"};\n        Map<String, List<String>> groups = new HashMap<>();\n        for(String w : words) {\n            char[] c = w.toCharArray();\n            Arrays.sort(c);\n            String k = new String(c);\n            groups.computeIfAbsent(k, x -> new ArrayList<>()).add(w);\n        }\n        System.out.println(\"Group Count: \" + groups.size());",
        "java_solution": "        String[] words = {\"eat\", \"tea\", \"tan\", \"ate\", \"nat\", \"bat\"};\n        Map<String, List<String>> groups = new HashMap<>();\n        for(String w : words) {\n            char[] c = w.toCharArray();\n            Arrays.sort(c);\n            String k = new String(c);\n            groups.computeIfAbsent(k, x -> new ArrayList<>()).add(w);\n        }\n        System.out.println(\"Group Count: \" + groups.size());",
        "expected_output": "Group Count: 3",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes the signature key used for grouping.. However, All anagrams produce the exact same key when sorted alphabetically.",
            "Core Concept: All anagrams produce the exact same key when sorted alphabetically. In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Use sorted characters as the hash map key."
        ],
        "cause": [
            "Categorization requires a canonical key representing character frequency.",
            "Sorted word acts as the universal key for that anagram family.",
            "Golden Rule: Group anagrams by mapping each word to its sorted character sequence."
        ]
    },
    {
        "topic_id": "strings_hashmaps",
        "topic_name": "Strings & Text Processing",
        "level": 10,
        "title": "Longest Substring Without Repeating Characters",
        "company": "Google, Amazon, Meta",
        "description": "Find the length of the longest substring without duplicate characters using sliding window.",
        "py_input": "s = 'abcabcbb'",
        "py_bug": "s = 'abcabcbb'\nseen = set()\nleft = 0\nmax_len = 0\nfor right in range(len(s) + 1):\n    while s[right] in seen:\n        seen.remove(s[left])\n        left += 1\n    seen.add(s[right])\n    max_len = max(max_len, right - left + 1)\nprint('Max Length:', max_len)",
        "py_solution": "s = 'abcabcbb'\nseen = set()\nleft = 0\nmax_len = 0\nfor right in range(len(s)):\n    while s[right] in seen:\n        seen.remove(s[left])\n        left += 1\n    seen.add(s[right])\n    max_len = max(max_len, right - left + 1)\nprint('Max Length:', max_len)",
        "java_input": "        String s = \"abcabcbb\";",
        "java_bug": "        String s = \"abcabcbb\";\n        Set<Character> seen = new HashSet<>();\n        int left = 0, maxLen = 0;\n        for(int right = 0; right <= s.length(); right++) {\n            while(seen.contains(s.charAt(right))) {\n                seen.remove(s.charAt(left));\n                left++;\n            }\n            seen.add(s.charAt(right));\n            maxLen = Math.max(maxLen, right - left + 1);\n        }\n        System.out.println(\"Max Length: \" + maxLen);",
        "java_solution": "        String s = \"abcabcbb\";\n        Set<Character> seen = new HashSet<>();\n        int left = 0, maxLen = 0;\n        for(int right = 0; right < s.length(); right++) {\n            while(seen.contains(s.charAt(right))) {\n                seen.remove(s.charAt(left));\n                left++;\n            }\n            seen.add(s.charAt(right));\n            maxLen = Math.max(maxLen, right - left + 1);\n        }\n        System.out.println(\"Max Length: \" + maxLen);",
        "expected_output": "Max Length: 3",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes the sliding window loop bound right.. However, range(len(s) + 1) steps beyond the string on the final iteration.",
            "Core Concept: range(len(s) + 1) steps beyond the string on the final iteration. In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Loop over `range(len(s))` or `right < s.length()`."
        ],
        "cause": [
            "StringIndexOutOfBoundsException when right reaches length.",
            "Window right pointer should only span 0 to length - 1.",
            "Golden Rule: In sliding window, right pointer advances strictly from 0 to length - 1."
        ]
    },

    # =========================================================================
    # TOPIC 3: SEARCHING & LOOPS (10 Placement Questions)
    # =========================================================================
    {
        "topic_id": "loops_indexing",
        "topic_name": "Searching & Loops",
        "level": 1,
        "title": "Linear Search for Target Element",
        "company": "TCS, Infosys",
        "description": "Find the 0-based index of a target element in an array using sequential search.",
        "py_input": "nums = [15, 42, 7, 89, 23]\ntarget = 7",
        "py_bug": "nums = [15, 42, 7, 89, 23]\ntarget = 7\nfound_idx = -1\nfor i in range(1, len(nums) + 1):\n    if nums[i] == target:\n        found_idx = i\n        break\nprint('Found at index:', found_idx)",
        "py_solution": "nums = [15, 42, 7, 89, 23]\ntarget = 7\nfound_idx = -1\nfor i in range(len(nums)):\n    if nums[i] == target:\n        found_idx = i\n        break\nprint('Found at index:', found_idx)",
        "java_input": "        int[] nums = {15, 42, 7, 89, 23};\n        int target = 7;",
        "java_bug": "        int[] nums = {15, 42, 7, 89, 23};\n        int target = 7, found = -1;\n        for(int i = 1; i <= nums.length; i++) {\n            if (nums[i] == target) { found = i; break; }\n        }\n        System.out.println(\"Found at index: \" + found);",
        "java_solution": "        int[] nums = {15, 42, 7, 89, 23};\n        int target = 7, found = -1;\n        for(int i = 0; i < nums.length; i++) {\n            if (nums[i] == target) { found = i; break; }\n        }\n        System.out.println(\"Found at index: \" + found);",
        "expected_output": "Found at index: 2",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes the start and end of the loop.. However, Array indexing starts at 0, not 1. Also stop at len(nums).",
            "Core Concept: Array indexing starts at 0, not 1. Also stop at len(nums). In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Loop from 0 to len(nums)."
        ],
        "cause": [
            "Loop started at 1 (skipping index 0) and ended at len + 1 (causing IndexError).",
            "Standard arrays are zero-indexed from 0 to N-1.",
            "Golden Rule: Loop from 0 to N-1 to inspect all array elements."
        ]
    },
    {
        "topic_id": "loops_indexing",
        "topic_name": "Searching & Loops",
        "level": 2,
        "title": "Binary Search on Sorted Array",
        "company": "Google, Amazon",
        "description": "Locate the target element in a sorted array in O(log n) time.",
        "py_input": "nums = [10, 20, 30, 40, 50]\ntarget = 40",
        "py_bug": "nums = [10, 20, 30, 40, 50]\ntarget = 40\nl, r = 0, len(nums) - 1\nans = -1\nwhile l < r:\n    mid = (l + r) // 2\n    if nums[mid] == target: ans = mid; break\n    elif nums[mid] < target: l = mid\n    else: r = mid - 1\nprint('Target index:', ans)",
        "py_solution": "nums = [10, 20, 30, 40, 50]\ntarget = 40\nl, r = 0, len(nums) - 1\nans = -1\nwhile l <= r:\n    mid = (l + r) // 2\n    if nums[mid] == target: ans = mid; break\n    elif nums[mid] < target: l = mid + 1\n    else: r = mid - 1\nprint('Target index:', ans)",
        "java_input": "        int[] nums = {10, 20, 30, 40, 50};\n        int target = 40;",
        "java_bug": "        int[] nums = {10, 20, 30, 40, 50};\n        int target = 40, l = 0, r = nums.length - 1, ans = -1;\n        while (l < r) {\n            int mid = (l + r) / 2;\n            if (nums[mid] == target) { ans = mid; break; }\n            else if (nums[mid] < target) l = mid;\n            else r = mid - 1;\n        }\n        System.out.println(\"Target index: \" + ans);",
        "java_solution": "        int[] nums = {10, 20, 30, 40, 50};\n        int target = 40, l = 0, r = nums.length - 1, ans = -1;\n        while (l <= r) {\n            int mid = (l + r) / 2;\n            if (nums[mid] == target) { ans = mid; break; }\n            else if (nums[mid] < target) l = mid + 1;\n            else r = mid - 1;\n        }\n        System.out.println(\"Target index: \" + ans);",
        "expected_output": "Target index: 3",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes the while loop condition and how l updates.. However, If l = mid, the loop can freeze forever in an infinite loop. Use l = mid + 1.",
            "Core Concept: If l = mid, the loop can freeze forever in an infinite loop. Use l = mid + 1. In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Use `while l <= r:` and `l = mid + 1`."
        ],
        "cause": [
            "Setting l = mid without +1 causes infinite loop when l and r converge.",
            "Binary search requires strictly shrinking the search window on every iteration.",
            "Golden Rule: In binary search, update `l = mid + 1` and `r = mid - 1`."
        ]
    },
    {
        "topic_id": "loops_indexing",
        "topic_name": "Searching & Loops",
        "level": 3,
        "title": "Find Peak Element",
        "company": "Amazon, Apple",
        "description": "Find a peak element that is strictly greater than its neighbors and print its index.",
        "py_input": "nums = [1, 2, 3, 1]",
        "py_bug": "nums = [1, 2, 3, 1]\npeak = 0\nfor i in range(len(nums)):\n    if nums[i] > nums[i + 1]:\n        peak = i\n        break\nprint('Peak index:', peak)",
        "py_solution": "nums = [1, 2, 3, 1]\npeak = 0\nfor i in range(len(nums) - 1):\n    if nums[i] > nums[i + 1]:\n        peak = i\n        break\nelse:\n    peak = len(nums) - 1\nprint('Peak index:', peak)",
        "java_input": "        int[] nums = {1, 2, 3, 1};",
        "java_bug": "        int[] nums = {1, 2, 3, 1};\n        int peak = 0;\n        for(int i = 0; i < nums.length; i++) {\n            if (nums[i] > nums[i + 1]) { peak = i; break; }\n        }\n        System.out.println(\"Peak index: \" + peak);",
        "java_solution": "        int[] nums = {1, 2, 3, 1};\n        int peak = nums.length - 1;\n        for(int i = 0; i < nums.length - 1; i++) {\n            if (nums[i] > nums[i + 1]) { peak = i; break; }\n        }\n        System.out.println(\"Peak index: \" + peak);",
        "expected_output": "Peak index: 2",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes `nums[i + 1]` on the last step of the loop.. However, At the final element, `nums[i + 1]` throws an IndexError.",
            "Core Concept: At the final element, `nums[i + 1]` throws an IndexError. In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Loop up to `len(nums) - 1` or `nums.length - 1`."
        ],
        "cause": [
            "Attempted to read neighbor nums[4] in a 4-item array.",
            "Lookahead comparisons must stop at len - 1.",
            "Golden Rule: Loop only to length - 1 when inspecting `i + 1`."
        ]
    },
    {
        "topic_id": "loops_indexing",
        "topic_name": "Searching & Loops",
        "level": 4,
        "title": "Count Occurrences in Sorted Array",
        "company": "Wipro, Accenture",
        "description": "Count how many times a given target appears in a sorted array.",
        "py_input": "nums = [1, 2, 2, 2, 3, 4]\ntarget = 2",
        "py_bug": "nums = [1, 2, 2, 2, 3, 4]\ntarget = 2\ncount = 0\nfor i in range(len(nums) + 1):\n    if nums[i] == target: count += 1\nprint('Occurrences:', count)",
        "py_solution": "nums = [1, 2, 2, 2, 3, 4]\ntarget = 2\ncount = 0\nfor x in nums:\n    if x == target: count += 1\nprint('Occurrences:', count)",
        "java_input": "        int[] nums = {1, 2, 2, 2, 3, 4};\n        int target = 2;",
        "java_bug": "        int[] nums = {1, 2, 2, 2, 3, 4};\n        int target = 2, count = 0;\n        for(int i = 0; i <= nums.length; i++) {\n            if (nums[i] == target) count++;\n        }\n        System.out.println(\"Occurrences: \" + count);",
        "java_solution": "        int[] nums = {1, 2, 2, 2, 3, 4};\n        int target = 2, count = 0;\n        for(int i = 0; i < nums.length; i++) {\n            if (nums[i] == target) count++;\n        }\n        System.out.println(\"Occurrences: \" + count);",
        "expected_output": "Occurrences: 3",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes the loop boundary.. However, Loop runs up to `len(nums) + 1` or `<= nums.length` which goes past the end.",
            "Core Concept: Loop runs up to `len(nums) + 1` or `<= nums.length` which goes past the end. In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Use `range(len(nums))` or `for (int x : nums)`."
        ],
        "cause": [
            "Off-by-one error caused index out of bounds at index 6.",
            "Array has 6 elements (indices 0 to 5).",
            "Golden Rule: Loop strictly under length."
        ]
    },
    {
        "topic_id": "loops_indexing",
        "topic_name": "Searching & Loops",
        "level": 5,
        "title": "Square Root using Binary Search",
        "company": "Uber, Bloomberg",
        "description": "Compute the integer square root of a non-negative integer x.",
        "py_input": "x = 25",
        "py_bug": "x = 25\nl, r = 1, x\nans = 0\nwhile l <= r:\n    mid = (l + r) // 2\n    if mid * mid == x: ans = mid; break\n    elif mid * mid < x: ans = mid; l = mid\n    else: r = mid - 1\nprint('Sqrt:', ans)",
        "py_solution": "x = 25\nl, r = 1, x\nans = 0\nwhile l <= r:\n    mid = (l + r) // 2\n    if mid * mid == x: ans = mid; break\n    elif mid * mid < x: ans = mid; l = mid + 1\n    else: r = mid - 1\nprint('Sqrt:', ans)",
        "java_input": "        int x = 25;",
        "java_bug": "        int x = 25;\n        int l = 1, r = x, ans = 0;\n        while (l <= r) {\n            int mid = l + (r - l) / 2;\n            if ((long)mid * mid == x) { ans = mid; break; }\n            else if ((long)mid * mid < x) { ans = mid; l = mid; }\n            else r = mid - 1;\n        }\n        System.out.println(\"Sqrt: \" + ans);",
        "java_solution": "        int x = 25;\n        int l = 1, r = x, ans = 0;\n        while (l <= r) {\n            int mid = l + (r - l) / 2;\n            if ((long)mid * mid == x) { ans = mid; break; }\n            else if ((long)mid * mid < x) { ans = mid; l = mid + 1; }\n            else r = mid - 1;\n        }\n        System.out.println(\"Sqrt: \" + ans);",
        "expected_output": "Sqrt: 5",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes `l = mid` in the second condition.. However, Not adding 1 can cause the binary search to hang in an infinite loop.",
            "Core Concept: Not adding 1 can cause the binary search to hang in an infinite loop. In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Update `l = mid + 1`."
        ],
        "cause": [
            "Updating `l = mid` fails to narrow the search interval, trapping execution in an infinite loop.",
            "Binary search intervals must shrink on every comparison.",
            "Golden Rule: Always increment left pointer (`l = mid + 1`) when mid is already tested."
        ]
    },
    {
        "topic_id": "loops_indexing",
        "topic_name": "Searching & Loops",
        "level": 6,
        "title": "Search in Rotated Sorted Array",
        "company": "Microsoft, Adobe",
        "description": "Find target in an array that has been rotated at an unknown pivot.",
        "py_input": "nums = [4, 5, 6, 7, 0, 1, 2]\ntarget = 0",
        "py_bug": "nums = [4, 5, 6, 7, 0, 1, 2]\ntarget = 0\nl, r = 0, len(nums) - 1\nans = -1\nwhile l <= r:\n    mid = (l + r) // 2\n    if nums[mid] == target: ans = mid; break\n    if nums[l] <= nums[mid]:\n        if nums[l] <= target < nums[mid]: r = mid - 1\n        else: l = mid + 1\n    else:\n        if nums[mid] < target <= nums[r]: l = mid + 1\n        else: r = mid - 1\nprint('Target index:', ans)",
        "py_solution": "nums = [4, 5, 6, 7, 0, 1, 2]\ntarget = 0\nl, r = 0, len(nums) - 1\nans = -1\nwhile l <= r:\n    mid = (l + r) // 2\n    if nums[mid] == target: ans = mid; break\n    if nums[l] <= nums[mid]:\n        if nums[l] <= target < nums[mid]: r = mid - 1\n        else: l = mid + 1\n    else:\n        if nums[mid] < target <= nums[r]: l = mid + 1\n        else: r = mid - 1\nprint('Target index:', ans)",
        "java_input": "        int[] nums = {4, 5, 6, 7, 0, 1, 2};\n        int target = 0;",
        "java_bug": "        int[] nums = {4, 5, 6, 7, 0, 1, 2};\n        int target = 0, l = 0, r = nums.length - 1, ans = -1;\n        while(l <= r) {\n            int mid = (l + r) / 2;\n            if (nums[mid] == target) { ans = mid; break; }\n            if (nums[l] <= nums[mid]) {\n                if (nums[l] <= target && target < nums[mid]) r = mid - 1;\n                else l = mid + 1;\n            } else {\n                if (nums[mid] < target && target <= nums[r]) l = mid + 1;\n                else r = mid - 1;\n            }\n        }\n        System.out.println(\"Target index: \" + ans);",
        "java_solution": "        int[] nums = {4, 5, 6, 7, 0, 1, 2};\n        int target = 0, l = 0, r = nums.length - 1, ans = -1;\n        while(l <= r) {\n            int mid = (l + r) / 2;\n            if (nums[mid] == target) { ans = mid; break; }\n            if (nums[l] <= nums[mid]) {\n                if (nums[l] <= target && target < nums[mid]) r = mid - 1;\n                else l = mid + 1;\n            } else {\n                if (nums[mid] < target && target <= nums[r]) l = mid + 1;\n                else r = mid - 1;\n            }\n        }\n        System.out.println(\"Target index: \" + ans);",
        "expected_output": "Target index: 4",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes which half of the rotated array is sorted.. However, One half is always normally sorted. Check if target lies within that half.",
            "Core Concept: One half is always normally sorted. Check if target lies within that half. In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Use `nums[l] <= nums[mid]` to determine the sorted side."
        ],
        "cause": [
            "Rotated arrays split into one sorted half and one rotated half.",
            "Binary search requires identifying the sorted half before eliminating.",
            "Golden Rule: In rotated binary search, check if target is inside the sorted half."
        ]
    },
    {
        "topic_id": "loops_indexing",
        "topic_name": "Searching & Loops",
        "level": 7,
        "title": "Find First and Last Position in Sorted Array",
        "company": "Facebook, Google",
        "description": "Find the starting and ending position of a given target value in a sorted array.",
        "py_input": "nums = [5, 7, 7, 8, 8, 10]\ntarget = 8",
        "py_bug": "nums = [5, 7, 7, 8, 8, 10]\ntarget = 8\n# Naive search with index error\nstart, end = -1, -1\nfor i in range(len(nums) + 1):\n    if nums[i] == target:\n        if start == -1: start = i\n        end = i\nprint('Positions:', [start, end])",
        "py_solution": "nums = [5, 7, 7, 8, 8, 10]\ntarget = 8\nstart, end = -1, -1\nfor i in range(len(nums)):\n    if nums[i] == target:\n        if start == -1: start = i\n        end = i\nprint('Positions:', [start, end])",
        "java_input": "        int[] nums = {5, 7, 7, 8, 8, 10};\n        int target = 8;",
        "java_bug": "        int[] nums = {5, 7, 7, 8, 8, 10};\n        int target = 8, start = -1, end = -1;\n        for(int i = 0; i <= nums.length; i++) {\n            if (nums[i] == target) {\n                if (start == -1) start = i;\n                end = i;\n            }\n        }\n        System.out.println(\"Positions: [\" + start + \", \" + end + \"]\");",
        "java_solution": "        int[] nums = {5, 7, 7, 8, 8, 10};\n        int target = 8, start = -1, end = -1;\n        for(int i = 0; i < nums.length; i++) {\n            if (nums[i] == target) {\n                if (start == -1) start = i;\n                end = i;\n            }\n        }\n        System.out.println(\"Positions: [\" + start + \", \" + end + \"]\");",
        "expected_output": "Positions: [3, 4]",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes loop termination.. However, `range(len(nums) + 1)` crashes at the end.",
            "Core Concept: `range(len(nums) + 1)` crashes at the end. In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Loop over `range(len(nums))`."
        ],
        "cause": [
            "IndexError when checking nums[6].",
            "Array has 6 elements indexed 0 to 5.",
            "Golden Rule: Loop bounds must stay within 0 to len-1."
        ]
    },
    {
        "topic_id": "loops_indexing",
        "topic_name": "Searching & Loops",
        "level": 8,
        "title": "Search a 2D Sorted Matrix",
        "company": "Amazon, Goldman Sachs",
        "description": "Determine if target exists in an m x n matrix where each row is sorted and first integer of each row is greater than last of previous.",
        "py_input": "matrix = [[1, 3, 5], [7, 10, 11], [16, 20, 30]]\ntarget = 10",
        "py_bug": "matrix = [[1, 3, 5], [7, 10, 11], [16, 20, 30]]\ntarget = 10\nm, n = len(matrix), len(matrix[0])\nl, r = 0, m * n\nfound = False\nwhile l <= r:\n    mid = (l + r) // 2\n    val = matrix[mid // n][mid % n] # Bug when mid reaches m * n\n    if val == target: found = True; break\n    elif val < target: l = mid + 1\n    else: r = mid - 1\nprint('Found in Matrix:', found)",
        "py_solution": "matrix = [[1, 3, 5], [7, 10, 11], [16, 20, 30]]\ntarget = 10\nm, n = len(matrix), len(matrix[0])\nl, r = 0, m * n - 1\nfound = False\nwhile l <= r:\n    mid = (l + r) // 2\n    val = matrix[mid // n][mid % n]\n    if val == target: found = True; break\n    elif val < target: l = mid + 1\n    else: r = mid - 1\nprint('Found in Matrix:', found)",
        "java_input": "        int[][] matrix = {{1, 3, 5}, {7, 10, 11}, {16, 20, 30}};\n        int target = 10;",
        "java_bug": "        int[][] matrix = {{1, 3, 5}, {7, 10, 11}, {16, 20, 30}};\n        int target = 10, m = matrix.length, n = matrix[0].length;\n        int l = 0, r = m * n;\n        boolean found = false;\n        while(l <= r) {\n            int mid = (l + r) / 2;\n            int val = matrix[mid / n][mid % n];\n            if (val == target) { found = true; break; }\n            else if (val < target) l = mid + 1;\n            else r = mid - 1;\n        }\n        System.out.println(\"Found in Matrix: \" + found);",
        "java_solution": "        int[][] matrix = {{1, 3, 5}, {7, 10, 11}, {16, 20, 30}};\n        int target = 10, m = matrix.length, n = matrix[0].length;\n        int l = 0, r = m * n - 1;\n        boolean found = false;\n        while(l <= r) {\n            int mid = (l + r) / 2;\n            int val = matrix[mid / n][mid % n];\n            if (val == target) { found = true; break; }\n            else if (val < target) l = mid + 1;\n            else r = mid - 1;\n        }\n        System.out.println(\"Found in Matrix: \" + found);",
        "expected_output": "Found in Matrix: True",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes the initial value of `r`.. However, A matrix of size m * n has elements indexed 0 to `m * n - 1`.",
            "Core Concept: A matrix of size m * n has elements indexed 0 to `m * n - 1`. In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Set `r = m * n - 1`."
        ],
        "cause": [
            "Setting r = m * n attempts to access row index m when mid = m * n.",
            "Virtual 1D array length is m * n, so max index is m * n - 1.",
            "Golden Rule: Virtual 1D index mapped to 2D must satisfy `0 <= index < rows * cols`."
        ]
    },
    {
        "topic_id": "loops_indexing",
        "topic_name": "Searching & Loops",
        "level": 9,
        "title": "Find Minimum in Rotated Sorted Array",
        "company": "Microsoft, Google",
        "description": "Find the minimum element in an array that has been rotated.",
        "py_input": "nums = [4, 5, 6, 7, 1, 2]",
        "py_bug": "nums = [4, 5, 6, 7, 1, 2]\nl, r = 0, len(nums) - 1\nwhile l < r:\n    mid = (l + r) // 2\n    if nums[mid] > nums[r]: l = mid # Bug: infinite loop when l and r differ by 1\n    else: r = mid\nprint('Minimum Element:', nums[l])",
        "py_solution": "nums = [4, 5, 6, 7, 1, 2]\nl, r = 0, len(nums) - 1\nwhile l < r:\n    mid = (l + r) // 2\n    if nums[mid] > nums[r]: l = mid + 1\n    else: r = mid\nprint('Minimum Element:', nums[l])",
        "java_input": "        int[] nums = {4, 5, 6, 7, 1, 2};",
        "java_bug": "        int[] nums = {4, 5, 6, 7, 1, 2};\n        int l = 0, r = nums.length - 1;\n        while (l < r) {\n            int mid = (l + r) / 2;\n            if (nums[mid] > nums[r]) l = mid;\n            else r = mid;\n        }\n        System.out.println(\"Minimum Element: \" + nums[l]);",
        "java_solution": "        int[] nums = {4, 5, 6, 7, 1, 2};\n        int l = 0, r = nums.length - 1;\n        while (l < r) {\n            int mid = (l + r) / 2;\n            if (nums[mid] > nums[r]) l = mid + 1;\n            else r = mid;\n        }\n        System.out.println(\"Minimum Element: \" + nums[l]);",
        "expected_output": "Minimum Element: 1",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes `l = mid`.. However, When `nums[mid] > nums[r]`, mid cannot be the minimum! The minimum must be strictly to the right.",
            "Core Concept: When `nums[mid] > nums[r]`, mid cannot be the minimum! The minimum must be strictly to the right. In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Use `l = mid + 1`."
        ],
        "cause": [
            "Setting `l = mid` without +1 prevents the window from shrinking, causing an infinite loop.",
            "Since nums[mid] > nums[r], nums[mid] is definitely not the minimum.",
            "Golden Rule: Eliminate mid by setting `l = mid + 1` when mid is proven too large."
        ]
    },
    {
        "topic_id": "loops_indexing",
        "topic_name": "Searching & Loops",
        "level": 10,
        "title": "Capacity to Ship Packages Within D Days",
        "company": "Google, Meta",
        "description": "Find the minimum package weight capacity of a ship so all packages can be shipped within days.",
        "py_input": "weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\ndays = 5",
        "py_bug": "weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\ndays = 5\nl, r = max(weights), sum(weights)\nwhile l < r:\n    mid = (l + r) // 2\n    curr, need = 0, 1\n    for w in weights:\n        if curr + w > mid: need += 1; curr = w\n        else: curr += w\n    if need > days: l = mid + 1\n    else: r = mid\nprint('Min Capacity:', l)",
        "py_solution": "weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\ndays = 5\nl, r = max(weights), sum(weights)\nwhile l < r:\n    mid = (l + r) // 2\n    curr, need = 0, 1\n    for w in weights:\n        if curr + w > mid: need += 1; curr = w\n        else: curr += w\n    if need > days: l = mid + 1\n    else: r = mid\nprint('Min Capacity:', l)",
        "java_input": "        int[] weights = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};\n        int days = 5;",
        "java_bug": "        int[] weights = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};\n        int days = 5;\n        int l = 10, r = 55;\n        while(l < r) {\n            int mid = (l + r) / 2;\n            int curr = 0, need = 1;\n            for(int w : weights) {\n                if (curr + w > mid) { need++; curr = w; }\n                else curr += w;\n            }\n            if (need > days) l = mid + 1;\n            else r = mid;\n        }\n        System.out.println(\"Min Capacity: \" + l);",
        "java_solution": "        int[] weights = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};\n        int days = 5;\n        int l = 10, r = 55;\n        while(l < r) {\n            int mid = (l + r) / 2;\n            int curr = 0, need = 1;\n            for(int w : weights) {\n                if (curr + w > mid) { need++; curr = w; }\n                else curr += w;\n            }\n            if (need > days) l = mid + 1;\n            else r = mid;\n        }\n        System.out.println(\"Min Capacity: \" + l);",
        "expected_output": "Min Capacity: 15",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes the binary search space for capacity.. However, Minimum possible capacity is max(weights) and maximum is sum(weights).",
            "Core Concept: Minimum possible capacity is max(weights) and maximum is sum(weights). In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Binary search between max(weights) and sum(weights)."
        ],
        "cause": [
            "Binary search on answer pattern.",
            "Capacity lower bound must hold the largest single weight.",
            "Golden Rule: Binary search on monotonic answer space between max single element and total sum."
        ]
    }
]

print("Loaded Part 2 (Strings & Loops):", len(PART_2))
