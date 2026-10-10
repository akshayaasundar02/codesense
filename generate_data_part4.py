# Part 4 of Questions Catalog (Topic 6: Stacks & Queues, Topic 7: Recursion & Backtracking)

PART_4 = [
    # =========================================================================
    # TOPIC 6: STACKS & QUEUES (10 Placement Questions)
    # =========================================================================
    {
        "topic_id": "stacks_queues",
        "topic_name": "Stacks & Queues",
        "level": 1,
        "title": "Implement Stack Operations",
        "company": "TCS, Infosys",
        "description": "Perform push 10, push 20, push 30, pop once, and print the top element.",
        "py_input": "# Stack operations\nstack = []",
        "py_bug": "stack = []\nstack.append(10)\nstack.append(20)\nstack.append(30)\nstack.pop() # removes 30\nprint('Top Element:', stack[len(stack)]) # Bug: index error accessing len instead of -1",
        "py_solution": "stack = []\nstack.append(10)\nstack.append(20)\nstack.append(30)\nstack.pop()\nprint('Top Element:', stack[-1])",
        "java_input": "        Stack<Integer> stack = new Stack<>();",
        "java_bug": "        Stack<Integer> stack = new Stack<>();\n        stack.push(10);\n        stack.push(20);\n        stack.push(30);\n        stack.pop();\n        System.out.println(\"Top Element: \" + stack.get(stack.size()));",
        "java_solution": "        Stack<Integer> stack = new Stack<>();\n        stack.push(10);\n        stack.push(20);\n        stack.push(30);\n        stack.pop();\n        System.out.println(\"Top Element: \" + stack.peek());",
        "expected_output": "Top Element: 20",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes how you access the top of the stack.. However, `stack[len(stack)]` is out of bounds! Use `stack[-1]` or `peek()`.",
            "Core Concept: `stack[len(stack)]` is out of bounds! Use `stack[-1]` or `peek()`. In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: In Python use `stack[-1]`, in Java use `stack.peek()`."
        ],
        "cause": [
            "Attempted to inspect stack[size], which causes an index out of bounds.",
            "The last valid element in a stack of size N is at index N-1.",
            "Golden Rule: Access stack top via `stack[-1]` in Python or `stack.peek()` in Java."
        ]
    },
    {
        "topic_id": "stacks_queues",
        "topic_name": "Stacks & Queues",
        "level": 2,
        "title": "Valid Parentheses (Balanced Brackets)",
        "company": "Amazon, Google",
        "description": "Given a string containing just '(', ')', '{', '}', '[' and ']', determine if the input string is valid.",
        "py_input": "s = '()[]{}'",
        "py_bug": "s = '()[]{}'\nstack = []\nmapping = {')': '(', '}': '{', ']': '['}\nok = True\nfor char in s:\n    if char in mapping:\n        top = stack.pop() # Bug: crashes with IndexError if stack is empty!\n        if mapping[char] != top: ok = False; break\n    else:\n        stack.append(char)\nprint('Valid Parentheses:', ok and len(stack) == 0)",
        "py_solution": "s = '()[]{}'\nstack = []\nmapping = {')': '(', '}': '{', ']': '['}\nok = True\nfor char in s:\n    if char in mapping:\n        if not stack or mapping[char] != stack.pop():\n            ok = False\n            break\n    else:\n        stack.append(char)\nprint('Valid Parentheses:', ok and len(stack) == 0)",
        "java_input": "        String s = \"()[]{}\";",
        "java_bug": "        String s = \"()[]{}\";\n        Stack<Character> stack = new Stack<>();\n        boolean ok = true;\n        for (char c : s.toCharArray()) {\n            if (c == ')' || c == '}' || c == ']') {\n                char top = stack.pop(); // Bug: EmptyStackException if unbalanced\n                if ((c == ')' && top != '(') || (c == '}' && top != '{') || (c == ']' && top != '[')) { ok = false; break; }\n            } else stack.push(c);\n        }\n        System.out.println(\"Valid Parentheses: \" + (ok && stack.isEmpty()));",
        "java_solution": "        String s = \"()[]{}\";\n        Stack<Character> stack = new Stack<>();\n        boolean ok = true;\n        for (char c : s.toCharArray()) {\n            if (c == ')' || c == '}' || c == ']') {\n                if (stack.isEmpty()) { ok = false; break; }\n                char top = stack.pop();\n                if ((c == ')' && top != '(') || (c == '}' && top != '{') || (c == ']' && top != '[')) { ok = false; break; }\n            } else stack.push(c);\n        }\n        System.out.println(\"Valid Parentheses: \" + (ok && stack.isEmpty()));",
        "expected_output": "Valid Parentheses: True",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes what happens when a closing bracket arrives while the stack is empty.. However, Calling `pop()` on an empty stack crashes your program immediately.",
            "Core Concept: Calling `pop()` on an empty stack crashes your program immediately. In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Always check `if not stack:` or `if (stack.isEmpty())` before popping."
        ],
        "cause": [
            "Popping an empty stack raises IndexError / EmptyStackException.",
            "Unmatched closing brackets leave no opening bracket on the stack.",
            "Golden Rule: Never pop a stack without first verifying that it is not empty."
        ]
    },
    {
        "topic_id": "stacks_queues",
        "topic_name": "Stacks & Queues",
        "level": 3,
        "title": "Reverse a String using Stack",
        "company": "Wipro, Accenture",
        "description": "Reverse string 'developer' by pushing characters onto a stack and popping them.",
        "py_input": "s = 'developer'",
        "py_bug": "s = 'developer'\nstack = list(s)\nrev = ''\nwhile stack:\n    rev += stack.pop(0) # Bug: pop(0) removes from front (Queue FIFO behavior), not LIFO!\nprint('Reversed:', rev)",
        "py_solution": "s = 'developer'\nstack = list(s)\nrev = ''\nwhile stack:\n    rev += stack.pop()\nprint('Reversed:', rev)",
        "java_input": "        String s = \"developer\";",
        "java_bug": "        String s = \"developer\";\n        Stack<Character> st = new Stack<>();\n        for (char c : s.toCharArray()) st.push(c);\n        StringBuilder sb = new StringBuilder();\n        for (int i = 0; i < st.size(); i++) sb.append(st.get(i)); // Bug: read bottom-to-top\n        System.out.println(\"Reversed: \" + sb.toString());",
        "java_solution": "        String s = \"developer\";\n        Stack<Character> st = new Stack<>();\n        for (char c : s.toCharArray()) st.push(c);\n        StringBuilder sb = new StringBuilder();\n        while (!st.isEmpty()) sb.append(st.pop());\n        System.out.println(\"Reversed: \" + sb.toString());",
        "expected_output": "Reversed: repoleved",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes which end of the stack you pop from.. However, `pop(0)` takes from the beginning (FIFO), whereas a stack pops from the top (LIFO).",
            "Core Concept: `pop(0)` takes from the beginning (FIFO), whereas a stack pops from the top (LIFO). In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Use `stack.pop()` without an index."
        ],
        "cause": [
            "Popping index 0 turned the stack into a queue, producing identical forward order.",
            "LIFO principle requires popping the most recently pushed element.",
            "Golden Rule: Stack reversal relies on popping elements from the top (`pop()`)."
        ]
    },
    {
        "topic_id": "stacks_queues",
        "topic_name": "Stacks & Queues",
        "level": 4,
        "title": "Next Greater Element to Right",
        "company": "Amazon, Flipkart",
        "description": "For each element in [4, 5, 2, 25], find the first greater element to its right.",
        "py_input": "nums = [4, 5, 2, 25]",
        "py_bug": "nums = [4, 5, 2, 25]\nres = [-1] * len(nums)\nstack = []\nfor i in range(len(nums) + 1): # Bug: out of range loop\n    while stack and nums[stack[-1]] < nums[i]:\n        res[stack.pop()] = nums[i]\n    stack.append(i)\nprint('Next Greater:', res)",
        "py_solution": "nums = [4, 5, 2, 25]\nres = [-1] * len(nums)\nstack = []\nfor i in range(len(nums)):\n    while stack and nums[stack[-1]] < nums[i]:\n        res[stack.pop()] = nums[i]\n    stack.append(i)\nprint('Next Greater:', res)",
        "java_input": "        int[] nums = {4, 5, 2, 25};",
        "java_bug": "        int[] nums = {4, 5, 2, 25};\n        int[] res = new int[nums.length];\n        Arrays.fill(res, -1);\n        Stack<Integer> st = new Stack<>();\n        for (int i = 0; i <= nums.length; i++) {\n            while (!st.isEmpty() && nums[st.peek()] < nums[i]) {\n                res[st.pop()] = nums[i];\n            }\n            st.push(i);\n        }\n        System.out.println(\"Next Greater: \" + Arrays.toString(res));",
        "java_solution": "        int[] nums = {4, 5, 2, 25};\n        int[] res = new int[nums.length];\n        Arrays.fill(res, -1);\n        Stack<Integer> st = new Stack<>();\n        for (int i = 0; i < nums.length; i++) {\n            while (!st.isEmpty() && nums[st.peek()] < nums[i]) {\n                res[st.pop()] = nums[i];\n            }\n            st.push(i);\n        }\n        System.out.println(\"Next Greater: \" + Arrays.toString(res));",
        "expected_output": "Next Greater: [5, 25, 25, -1]",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes the loop index bound.. However, `len(nums) + 1` steps beyond the array boundary.",
            "Core Concept: `len(nums) + 1` steps beyond the array boundary. In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Loop strictly up to `len(nums)` or `nums.length`."
        ],
        "cause": [
            "Monotonic stack loop stepped beyond array bounds on the final iteration.",
            "Indices are 0 through N-1.",
            "Golden Rule: Loop bounds must never exceed `len(nums)`."
        ]
    },
    {
        "topic_id": "stacks_queues",
        "topic_name": "Stacks & Queues",
        "level": 5,
        "title": "Evaluate Postfix (Reverse Polish)",
        "company": "Google, Microsoft",
        "description": "Evaluate the value of an arithmetic expression in Reverse Polish Notation: ['2', '1', '+', '3', '*'].",
        "py_input": "tokens = ['2', '1', '+', '3', '*']",
        "py_bug": "tokens = ['2', '1', '+', '3', '*']\nstack = []\nfor t in tokens:\n    if t in '+-*/':\n        a = stack.pop()\n        b = stack.pop()\n        if t == '+': stack.append(a + b)\n        elif t == '*': stack.append(a * b)\n    else:\n        stack.append(int(t))\nprint('Postfix Result:', stack[0])",
        "py_solution": "tokens = ['2', '1', '+', '3', '*']\nstack = []\nfor t in tokens:\n    if t in '+-*/':\n        b = stack.pop()\n        a = stack.pop()\n        if t == '+': stack.append(a + b)\n        elif t == '*': stack.append(a * b)\n    else:\n        stack.append(int(t))\nprint('Postfix Result:', stack[0])",
        "java_input": "        String[] tokens = {\"2\", \"1\", \"+\", \"3\", \"*\"};",
        "java_bug": "        String[] tokens = {\"2\", \"1\", \"+\", \"3\", \"*\"};\n        Stack<Integer> st = new Stack<>();\n        for (String t : tokens) {\n            if (t.equals(\"+\")) st.push(st.pop() + st.pop());\n            else if (t.equals(\"*\")) st.push(st.pop() * st.pop());\n            else st.push(Integer.parseInt(t));\n        }\n        System.out.println(\"Postfix Result: \" + st.peek());",
        "java_solution": "        String[] tokens = {\"2\", \"1\", \"+\", \"3\", \"*\"};\n        Stack<Integer> st = new Stack<>();\n        for (String t : tokens) {\n            if (t.equals(\"+\")) {\n                int b = st.pop(), a = st.pop();\n                st.push(a + b);\n            } else if (t.equals(\"*\")) {\n                int b = st.pop(), a = st.pop();\n                st.push(a * b);\n            } else st.push(Integer.parseInt(t));\n        }\n        System.out.println(\"Postfix Result: \" + st.peek());",
        "expected_output": "Postfix Result: 9",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes the order of operands popped from the stack.. However, First pop gives the second operand (b), and next pop gives the first operand (a).",
            "Core Concept: First pop gives the second operand (b), and next pop gives the first operand (a). In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Pop `b = stack.pop()`, then `a = stack.pop()`, then compute `a operator b`."
        ],
        "cause": [
            "Operand order is reversed in LIFO stack popping.",
            "Crucial for non-commutative operations like division `-` and `/`.",
            "Golden Rule: In postfix evaluation, first pop is right operand, second pop is left operand."
        ]
    },
    {
        "topic_id": "stacks_queues",
        "topic_name": "Stacks & Queues",
        "level": 6,
        "title": "Implement Queue using Two Stacks",
        "company": "Microsoft, Adobe",
        "description": "Implement FIFO queue operations using two LIFO stacks. Enqueue 1, 2, 3, dequeue one, check front.",
        "py_input": "# Queue using Two Stacks\ns1, s2 = [], []",
        "py_bug": "s1, s2 = [], []\ndef push(x): s1.append(x)\ndef pop():\n    if not s2:\n        while s1: s2.append(s1.pop())\n    return s2.pop()\npush(1); push(2); push(3)\npop()\nprint('Front Element:', s2[-1])",
        "py_solution": "s1, s2 = [], []\ndef push(x): s1.append(x)\ndef pop():\n    if not s2:\n        while s1: s2.append(s1.pop())\n    return s2.pop()\ndef peek():\n    if not s2:\n        while s1: s2.append(s1.pop())\n    return s2[-1]\npush(1); push(2); push(3)\npop()\nprint('Front Element:', peek())",
        "java_input": "        Stack<Integer> s1 = new Stack<>(), s2 = new Stack<>();",
        "java_bug": "        Stack<Integer> s1 = new Stack<>(), s2 = new Stack<>();\n        s1.push(1); s1.push(2); s1.push(3);\n        while (!s1.isEmpty()) s2.push(s1.pop());\n        s2.pop();\n        System.out.println(\"Front Element: \" + s2.peek());",
        "java_solution": "        Stack<Integer> s1 = new Stack<>(), s2 = new Stack<>();\n        s1.push(1); s1.push(2); s1.push(3);\n        while (!s1.isEmpty()) s2.push(s1.pop());\n        s2.pop();\n        System.out.println(\"Front Element: \" + s2.peek());",
        "expected_output": "Front Element: 2",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes how s2 transfers elements from s1.. However, Transferring elements inverts LIFO order into FIFO order.",
            "Core Concept: Transferring elements inverts LIFO order into FIFO order. In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Only transfer from s1 to s2 when s2 is empty."
        ],
        "cause": [
            "Inverting order through two stacks implements amortized O(1) queue.",
            "Front element is at the top of stack 2.",
            "Golden Rule: Elements move to output stack only when output stack is empty."
        ]
    },
    {
        "topic_id": "stacks_queues",
        "topic_name": "Stacks & Queues",
        "level": 7,
        "title": "Design Min Stack (O(1) getMin)",
        "company": "Amazon, Bloomberg",
        "description": "Design a stack that supports push, pop, top, and retrieving the minimum element in O(1) time.",
        "py_input": "stack, min_stack = [], []",
        "py_bug": "stack, min_stack = [], []\ndef push(x):\n    stack.append(x)\n    min_stack.append(x) # Bug: appended raw x instead of min(x, current_min)\ndef pop():\n    stack.pop()\n    min_stack.pop()\npush(3); push(5); push(2); push(1)\npop()\nprint('Min Element:', min_stack[-1])",
        "py_solution": "stack, min_stack = [], []\ndef push(x):\n    stack.append(x)\n    if not min_stack: min_stack.append(x)\n    else: min_stack.append(min(x, min_stack[-1]))\ndef pop():\n    stack.pop()\n    min_stack.pop()\npush(3); push(5); push(2); push(1)\npop()\nprint('Min Element:', min_stack[-1])",
        "java_input": "        Stack<Integer> stack = new Stack<>(), minStack = new Stack<>();",
        "java_bug": "        Stack<Integer> stack = new Stack<>(), minStack = new Stack<>();\n        int[] vals = {3, 5, 2, 1};\n        for(int v : vals) {\n            stack.push(v);\n            if (minStack.isEmpty() || v <= minStack.peek()) minStack.push(v);\n        }\n        stack.pop(); minStack.pop();\n        System.out.println(\"Min Element: \" + minStack.peek());",
        "java_solution": "        Stack<Integer> stack = new Stack<>(), minStack = new Stack<>();\n        int[] vals = {3, 5, 2, 1};\n        for(int v : vals) {\n            stack.push(v);\n            if (minStack.isEmpty()) minStack.push(v);\n            else minStack.push(Math.min(v, minStack.peek()));\n        }\n        stack.pop(); minStack.pop();\n        System.out.println(\"Min Element: \" + minStack.peek());",
        "expected_output": "Min Element: 2",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes what gets pushed to min_stack.. However, min_stack must always track the minimum value seen so far up to that depth.",
            "Core Concept: min_stack must always track the minimum value seen so far up to that depth. In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Push `min(x, min_stack[-1])` onto min_stack."
        ],
        "cause": [
            "Failing to track historic minimums breaks getMin after elements are popped.",
            "Each stack layer must store the minimum among all elements below it.",
            "Golden Rule: In MinStack, push `min(val, current_min)` to preserve state."
        ]
    },
    {
        "topic_id": "stacks_queues",
        "topic_name": "Stacks & Queues",
        "level": 8,
        "title": "Daily Temperatures (Days to Warmer)",
        "company": "Meta, Google",
        "description": "Given temperatures [73, 74, 75, 71, 69, 72, 76, 73], compute number of days to wait for a warmer temperature.",
        "py_input": "temps = [73, 74, 75, 71, 69, 72, 76, 73]",
        "py_bug": "temps = [73, 74, 75, 71, 69, 72, 76, 73]\nans = [0] * len(temps)\nstack = []\nfor i, t in enumerate(temps):\n    while stack and temps[stack[-1]] < t:\n        prev = stack.pop()\n        ans[prev] = i - prev\n    stack.append(i)\nprint('Wait Days:', ans)",
        "py_solution": "temps = [73, 74, 75, 71, 69, 72, 76, 73]\nans = [0] * len(temps)\nstack = []\nfor i, t in enumerate(temps):\n    while stack and temps[stack[-1]] < t:\n        prev = stack.pop()\n        ans[prev] = i - prev\n    stack.append(i)\nprint('Wait Days:', ans)",
        "java_input": "        int[] temps = {73, 74, 75, 71, 69, 72, 76, 73};",
        "java_bug": "        int[] temps = {73, 74, 75, 71, 69, 72, 76, 73};\n        int[] ans = new int[temps.length];\n        Stack<Integer> st = new Stack<>();\n        for (int i = 0; i < temps.length; i++) {\n            while (!st.isEmpty() && temps[st.peek()] < temps[i]) {\n                int prev = st.pop();\n                ans[prev] = i - prev;\n            }\n            st.push(i);\n        }\n        System.out.println(\"Wait Days: \" + Arrays.toString(ans));",
        "java_solution": "        int[] temps = {73, 74, 75, 71, 69, 72, 76, 73};\n        int[] ans = new int[temps.length];\n        Stack<Integer> st = new Stack<>();\n        for (int i = 0; i < temps.length; i++) {\n            while (!st.isEmpty() && temps[st.peek()] < temps[i]) {\n                int prev = st.pop();\n                ans[prev] = i - prev;\n            }\n            st.push(i);\n        }\n        System.out.println(\"Wait Days: \" + Arrays.toString(ans));",
        "expected_output": "Wait Days: [1, 1, 4, 2, 1, 1, 0, 0]",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes monotonic decreasing stack invariant.. However, Store day indices in stack until a warmer day arrives.",
            "Core Concept: Store day indices in stack until a warmer day arrives. In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Calculate wait duration as `i - prev` when popping."
        ],
        "cause": [
            "Monotonic stack pattern.",
            "Resolves unresolved temperatures in O(n) total time.",
            "Golden Rule: Stack holds indices of unresolved days awaiting a higher temperature."
        ]
    },
    {
        "topic_id": "stacks_queues",
        "topic_name": "Stacks & Queues",
        "level": 9,
        "title": "Largest Rectangle in Histogram",
        "company": "Google, Amazon",
        "description": "Given heights of bars in a histogram, find the area of the largest rectangle.",
        "py_input": "heights = [2, 1, 5, 6, 2, 3]",
        "py_bug": "heights = [2, 1, 5, 6, 2, 3]\nstack = [-1]\nmax_area = 0\nfor i in range(len(heights)):\n    while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:\n        h = heights[stack.pop()]\n        w = i - stack[-1] - 1\n        max_area = max(max_area, h * w)\n    stack.append(i)\nwhile stack[-1] != -1:\n    h = heights[stack.pop()]\n    w = len(heights) - stack[-1] - 1\n    max_area = max(max_area, h * w)\nprint('Max Histogram Area:', max_area)",
        "py_solution": "heights = [2, 1, 5, 6, 2, 3]\nstack = [-1]\nmax_area = 0\nfor i in range(len(heights)):\n    while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:\n        h = heights[stack.pop()]\n        w = i - stack[-1] - 1\n        max_area = max(max_area, h * w)\n    stack.append(i)\nwhile stack[-1] != -1:\n    h = heights[stack.pop()]\n    w = len(heights) - stack[-1] - 1\n    max_area = max(max_area, h * w)\nprint('Max Histogram Area:', max_area)",
        "java_input": "        int[] heights = {2, 1, 5, 6, 2, 3};",
        "java_bug": "        int[] heights = {2, 1, 5, 6, 2, 3};\n        Stack<Integer> st = new Stack<>();\n        st.push(-1);\n        int maxArea = 0;\n        for (int i = 0; i < heights.length; i++) {\n            while (st.peek() != -1 && heights[st.peek()] >= heights[i]) {\n                int h = heights[st.pop()];\n                int w = i - st.peek() - 1;\n                maxArea = Math.max(maxArea, h * w);\n            }\n            st.push(i);\n        }\n        while (st.peek() != -1) {\n            int h = heights[st.pop()];\n            int w = heights.length - st.peek() - 1;\n            maxArea = Math.max(maxArea, h * w);\n        }\n        System.out.println(\"Max Histogram Area: \" + maxArea);",
        "java_solution": "        int[] heights = {2, 1, 5, 6, 2, 3};\n        Stack<Integer> st = new Stack<>();\n        st.push(-1);\n        int maxArea = 0;\n        for (int i = 0; i < heights.length; i++) {\n            while (st.peek() != -1 && heights[st.peek()] >= heights[i]) {\n                int h = heights[st.pop()];\n                int w = i - st.peek() - 1;\n                maxArea = Math.max(maxArea, h * w);\n            }\n            st.push(i);\n        }\n        while (st.peek() != -1) {\n            int h = heights[st.pop()];\n            int w = heights.length - st.peek() - 1;\n            maxArea = Math.max(maxArea, h * w);\n        }\n        System.out.println(\"Max Histogram Area: \" + maxArea);",
        "expected_output": "Max Histogram Area: 10",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes width calculation using bounding indices.. However, Height of bar popped is bounded by previous smaller on left and current smaller on right.",
            "Core Concept: Height of bar popped is bounded by previous smaller on left and current smaller on right. In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Calculate rectangle area as `h * (i - stack[-1] - 1)`."
        ],
        "cause": [
            "Monotonic stack boundary expansion.",
            "Computes largest rectangle in single O(n) pass.",
            "Golden Rule: Area bounded between previous smaller and next smaller bar."
        ]
    },
    {
        "topic_id": "stacks_queues",
        "topic_name": "Stacks & Queues",
        "level": 10,
        "title": "Sliding Window Maximum using Deque",
        "company": "Google, Amazon",
        "description": "Find maximum value in each sliding window of size k = 3 in array [1, 3, -1, -3, 5, 3, 6, 7].",
        "py_input": "from collections import deque\nnums = [1, 3, -1, -3, 5, 3, 6, 7]\nk = 3",
        "py_bug": "from collections import deque\nnums = [1, 3, -1, -3, 5, 3, 6, 7]\nk = 3\nq = deque()\nres = []\nfor i, n in enumerate(nums):\n    while q and nums[q[-1]] < n: q.pop()\n    q.append(i)\n    if q[0] <= i - k: q.popleft()\n    if i >= k - 1: res.append(nums[q[0]])\nprint('Window Maxima:', res)",
        "py_solution": "from collections import deque\nnums = [1, 3, -1, -3, 5, 3, 6, 7]\nk = 3\nq = deque()\nres = []\nfor i, n in enumerate(nums):\n    while q and nums[q[-1]] < n: q.pop()\n    q.append(i)\n    if q[0] <= i - k: q.popleft()\n    if i >= k - 1: res.append(nums[q[0]])\nprint('Window Maxima:', res)",
        "java_input": "        int[] nums = {1, 3, -1, -3, 5, 3, 6, 7};\n        int k = 3;",
        "java_bug": "        int[] nums = {1, 3, -1, -3, 5, 3, 6, 7};\n        int k = 3;\n        Deque<Integer> q = new ArrayDeque<>();\n        List<Integer> res = new ArrayList<>();\n        for (int i = 0; i < nums.length; i++) {\n            while (!q.isEmpty() && nums[q.peekLast()] < nums[i]) q.pollLast();\n            q.offer(i);\n            if (q.peekFirst() <= i - k) q.pollFirst();\n            if (i >= k - 1) res.add(nums[q.peekFirst()]);\n        }\n        System.out.println(\"Window Maxima: \" + res);",
        "java_solution": "        int[] nums = {1, 3, -1, -3, 5, 3, 6, 7};\n        int k = 3;\n        Deque<Integer> q = new ArrayDeque<>();\n        List<Integer> res = new ArrayList<>();\n        for (int i = 0; i < nums.length; i++) {\n            while (!q.isEmpty() && nums[q.peekLast()] < nums[i]) q.pollLast();\n            q.offer(i);\n            if (q.peekFirst() <= i - k) q.pollFirst();\n            if (i >= k - 1) res.add(nums[q.peekFirst()]);\n        }\n        System.out.println(\"Window Maxima: \" + res);",
        "expected_output": "Window Maxima: [3, 3, 5, 5, 6, 7]",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes deque maintaining elements in decreasing order.. However, Head of the deque always holds the index of the maximum element in current window.",
            "Core Concept: Head of the deque always holds the index of the maximum element in current window. In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Discard older and smaller elements from the queue."
        ],
        "cause": [
            "Monotonic queue maintains max element in O(1) per step.",
            "Sliding window advances in linear time.",
            "Golden Rule: Monotonic deque stores indices with decreasing values; front is window max."
        ]
    },

    # =========================================================================
    # TOPIC 7: RECURSION & BACKTRACKING (10 Placement Questions)
    # =========================================================================
    {
        "topic_id": "recursion_backtracking",
        "topic_name": "Recursion & Backtracking",
        "level": 1,
        "title": "Recursive Factorial",
        "company": "Infosys, TCS",
        "description": "Compute factorial of n = 5 recursively.",
        "py_input": "n = 5",
        "py_bug": "n = 5\ndef fact(x):\n    return x * fact(x - 1) # Bug: missing base case causes RecursionError!\nprint('Factorial:', fact(n))",
        "py_solution": "n = 5\ndef fact(x):\n    if x <= 1: return 1\n    return x * fact(x - 1)\nprint('Factorial:', fact(n))",
        "java_input": "        int n = 5;",
        "java_bug": "        int n = 5;\n        // Missing base case causes StackOverflowError\n        System.out.println(\"Factorial: \" + (new Object() {\n            int f(int x) { return x * f(x - 1); }\n        }).f(n));",
        "java_solution": "        int n = 5;\n        System.out.println(\"Factorial: \" + (new Object() {\n            int f(int x) { return x <= 1 ? 1 : x * f(x - 1); }\n        }).f(n));",
        "expected_output": "Factorial: 120",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes the base case.. However, A recursive function without a base case will recurse forever until the call stack blows up.",
            "Core Concept: A recursive function without a base case will recurse forever until the call stack blows up. In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Add `if x <= 1: return 1`."
        ],
        "cause": [
            "Missing base condition caused infinite recursion / stack overflow.",
            "Recursive functions require a termination condition to unwind the call stack.",
            "Golden Rule: Every recursive function must define a base case first."
        ]
    },
    {
        "topic_id": "recursion_backtracking",
        "topic_name": "Recursion & Backtracking",
        "level": 2,
        "title": "N-th Fibonacci Number",
        "company": "Microsoft, Adobe",
        "description": "Compute the 7th Fibonacci number (where F(0)=0, F(1)=1, F(2)=1...).",
        "py_input": "n = 7",
        "py_bug": "n = 7\ndef fib(x):\n    if x == 0: return 0\n    # Bug: missing x == 1 base case!\n    return fib(x - 1) + fib(x - 2)\nprint('Fibonacci:', fib(n))",
        "py_solution": "n = 7\ndef fib(x):\n    if x <= 0: return 0\n    if x == 1: return 1\n    return fib(x - 1) + fib(x - 2)\nprint('Fibonacci:', fib(n))",
        "java_input": "        int n = 7;",
        "java_bug": "        int n = 7;\n        System.out.println(\"Fibonacci: \" + (new Object() {\n            int fib(int x) { if (x == 0) return 0; return fib(x-1) + fib(x-2); }\n        }).fib(n));",
        "java_solution": "        int n = 7;\n        System.out.println(\"Fibonacci: \" + (new Object() {\n            int fib(int x) { if (x <= 0) return 0; if (x == 1) return 1; return fib(x-1) + fib(x-2); }\n        }).fib(n));",
        "expected_output": "Fibonacci: 13",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes base case when x = 1.. However, Fibonacci needs two base cases: F(0) = 0 and F(1) = 1.",
            "Core Concept: Fibonacci needs two base cases: F(0) = 0 and F(1) = 1. In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Return 1 when `x == 1`."
        ],
        "cause": [
            "Omitting the base case for x = 1 causes recursive subtraction into negative numbers.",
            "Second-order recurrences require two base cases.",
            "Golden Rule: Functions with f(n-1) and f(n-2) need base cases for both n=0 and n=1."
        ]
    },
    {
        "topic_id": "recursion_backtracking",
        "topic_name": "Recursion & Backtracking",
        "level": 3,
        "title": "Sum of Digits of a Number",
        "company": "Accenture, Wipro",
        "description": "Recursively compute the sum of digits of n = 9876.",
        "py_input": "n = 9876",
        "py_bug": "n = 9876\ndef digit_sum(x):\n    if x == 0: return 0\n    return x % 10 + digit_sum(x / 10) # Bug: float division prevents reaching exact 0!\nprint('Digit Sum:', int(digit_sum(n)))",
        "py_solution": "n = 9876\ndef digit_sum(x):\n    if x == 0: return 0\n    return x % 10 + digit_sum(x // 10)\nprint('Digit Sum:', digit_sum(n))",
        "java_input": "        int n = 9876;",
        "java_bug": "        int n = 9876;\n        System.out.println(\"Digit Sum: \" + (new Object() {\n            int sum(int x) { return x == 0 ? 0 : x % 10 + sum(x / 10); }\n        }).sum(n));",
        "java_solution": "        int n = 9876;\n        System.out.println(\"Digit Sum: \" + (new Object() {\n            int sum(int x) { return x == 0 ? 0 : x % 10 + sum(x / 10); }\n        }).sum(n));",
        "expected_output": "Digit Sum: 30",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes the recursive division `x / 10`.. However, Single slash `/` produces floats like 987.6, never reaching integer 0.",
            "Core Concept: Single slash `/` produces floats like 987.6, never reaching integer 0. In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Use integer floor division `x // 10`."
        ],
        "cause": [
            "Float division prevented base condition x == 0 from triggering, causing recursion depth exceeded.",
            "Digit reduction requires integer truncation.",
            "Golden Rule: In digit extraction, always use integer floor division `// 10`."
        ]
    },
    {
        "topic_id": "recursion_backtracking",
        "topic_name": "Recursion & Backtracking",
        "level": 4,
        "title": "Power of X to N (Divide and Conquer)",
        "company": "Google, Amazon",
        "description": "Compute x^n where x = 2.0 and n = 10 in O(log n) time.",
        "py_input": "x = 2.0\nn = 10",
        "py_bug": "x = 2.0\nn = 10\ndef power(base, exp):\n    if exp == 0: return 1.0\n    half = power(base, exp // 2)\n    if exp % 2 == 0: return half * half\n    else: return half * half * base\nprint('Power:', power(x, n))",
        "py_solution": "x = 2.0\nn = 10\ndef power(base, exp):\n    if exp == 0: return 1.0\n    half = power(base, exp // 2)\n    if exp % 2 == 0: return half * half\n    else: return half * half * base\nprint('Power:', power(x, n))",
        "java_input": "        double x = 2.0;\n        int n = 10;",
        "java_bug": "        double x = 2.0;\n        int n = 10;\n        System.out.println(\"Power: \" + (new Object() {\n            double pow(double b, int e) {\n                if (e == 0) return 1.0;\n                double half = pow(b, e / 2);\n                return e % 2 == 0 ? half * half : half * half * b;\n            }\n        }).pow(x, n));",
        "java_solution": "        double x = 2.0;\n        int n = 10;\n        System.out.println(\"Power: \" + (new Object() {\n            double pow(double b, int e) {\n                if (e == 0) return 1.0;\n                double half = pow(b, e / 2);\n                return e % 2 == 0 ? half * half : half * half * b;\n            }\n        }).pow(x, n));",
        "expected_output": "Power: 1024.0",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes divide and conquer step.. However, `x^n = (x^(n/2))^2`. Halving the exponent cuts execution time to log n.",
            "Core Concept: `x^n = (x^(n/2))^2`. Halving the exponent cuts execution time to log n. In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Multiply `half * half` when exponent is even, and include base when odd."
        ],
        "cause": [
            "Divide and conquer binary exponentiation.",
            "Calculates power in O(log n) instead of linear time.",
            "Golden Rule: Halve exponent recursively to achieve logarithmic power calculation."
        ]
    },
    {
        "topic_id": "recursion_backtracking",
        "topic_name": "Recursion & Backtracking",
        "level": 5,
        "title": "Tower of Hanoi Move Counter",
        "company": "Amazon, Microsoft",
        "description": "Calculate minimal number of moves required to solve Tower of Hanoi with 3 disks.",
        "py_input": "disks = 3",
        "py_bug": "disks = 3\ndef hanoi(n):\n    if n == 1: return 1\n    return 2 * hanoi(n - 1) + 1\nprint('Hanoi Moves:', hanoi(disks))",
        "py_solution": "disks = 3\ndef hanoi(n):\n    if n == 1: return 1\n    return 2 * hanoi(n - 1) + 1\nprint('Hanoi Moves:', hanoi(disks))",
        "java_input": "        int disks = 3;",
        "java_bug": "        int disks = 3;\n        System.out.println(\"Hanoi Moves: \" + (new Object() {\n            int moves(int n) { return n == 1 ? 1 : 2 * moves(n - 1) + 1; }\n        }).moves(disks));",
        "java_solution": "        int disks = 3;\n        System.out.println(\"Hanoi Moves: \" + (new Object() {\n            int moves(int n) { return n == 1 ? 1 : 2 * moves(n - 1) + 1; }\n        }).moves(disks));",
        "expected_output": "Hanoi Moves: 7",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes moving n-1 disks, the largest disk, and then n-1 disks again.. However, Recurrence is `2 * T(n - 1) + 1`.",
            "Core Concept: Recurrence is `2 * T(n - 1) + 1`. In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: With 3 disks, moves equal 2^3 - 1 = 7."
        ],
        "cause": [
            "Classical recurrence relation T(n) = 2T(n-1) + 1.",
            "Requires 2^n - 1 moves.",
            "Golden Rule: Tower of Hanoi minimal moves equal 2^n - 1."
        ]
    },
    {
        "topic_id": "recursion_backtracking",
        "topic_name": "Recursion & Backtracking",
        "level": 6,
        "title": "Generate All Subsets (Power Set)",
        "company": "Google, Meta",
        "description": "Generate all subsets of [1, 2, 3] and print total count of subsets.",
        "py_input": "nums = [1, 2, 3]",
        "py_bug": "nums = [1, 2, 3]\nsubsets = []\ndef backtrack(idx, curr):\n    subsets.append(curr) # Bug: appended reference instead of copy\n    for i in range(idx, len(nums)):\n        curr.append(nums[i])\n        backtrack(i + 1, curr)\n        curr.pop()\nbacktrack(0, [])\nprint('Total Subsets:', len(subsets))",
        "py_solution": "nums = [1, 2, 3]\nsubsets = []\ndef backtrack(idx, curr):\n    subsets.append(curr[:])\n    for i in range(idx, len(nums)):\n        curr.append(nums[i])\n        backtrack(i + 1, curr)\n        curr.pop()\nbacktrack(0, [])\nprint('Total Subsets:', len(subsets))",
        "java_input": "        int[] nums = {1, 2, 3};",
        "java_bug": "        int[] nums = {1, 2, 3};\n        List<List<Integer>> res = new ArrayList<>();\n        class Solver {\n            void dfs(int idx, List<Integer> curr) {\n                res.add(new ArrayList<>(curr));\n                for (int i = idx; i < nums.length; i++) {\n                    curr.add(nums[i]);\n                    dfs(i + 1, curr);\n                    curr.remove(curr.size() - 1);\n                }\n            }\n        }\n        new Solver().dfs(0, new ArrayList<>());\n        System.out.println(\"Total Subsets: \" + res.size());",
        "java_solution": "        int[] nums = {1, 2, 3};\n        List<List<Integer>> res = new ArrayList<>();\n        class Solver {\n            void dfs(int idx, List<Integer> curr) {\n                res.add(new ArrayList<>(curr));\n                for (int i = idx; i < nums.length; i++) {\n                    curr.add(nums[i]);\n                    dfs(i + 1, curr);\n                    curr.remove(curr.size() - 1);\n                }\n            }\n        }\n        new Solver().dfs(0, new ArrayList<>());\n        System.out.println(\"Total Subsets: \" + res.size());",
        "expected_output": "Total Subsets: 8",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes how current path is saved in the results list.. However, Saving `curr` directly in Python stores a pointer; when backtrack pops, all saved items turn empty!",
            "Core Concept: Saving `curr` directly in Python stores a pointer; when backtrack pops, all saved items turn empty! In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Save a shallow copy `curr[:]` in Python or `new ArrayList<>(curr)` in Java."
        ],
        "cause": [
            "Storing mutable list references causes later modifications (backtracking pop) to corrupt previously recorded paths.",
            "Backtracking requires snapshotting state.",
            "Golden Rule: In backtracking, always copy state (`list[:]` or `new ArrayList<>(list)`) before storing."
        ]
    },
    {
        "topic_id": "recursion_backtracking",
        "topic_name": "Recursion & Backtracking",
        "level": 7,
        "title": "Permutations of an Array",
        "company": "Microsoft, Uber",
        "description": "Generate all permutations of [1, 2, 3] and print total permutations count.",
        "py_input": "nums = [1, 2, 3]",
        "py_bug": "nums = [1, 2, 3]\nres = []\ndef permute(curr):\n    if len(curr) == len(nums):\n        res.append(curr[:])\n        return\n    for x in nums:\n        if x not in curr:\n            curr.append(x)\n            permute(curr)\n            curr.pop()\npermute([])\nprint('Permutations Count:', len(res))",
        "py_solution": "nums = [1, 2, 3]\nres = []\ndef permute(curr):\n    if len(curr) == len(nums):\n        res.append(curr[:])\n        return\n    for x in nums:\n        if x not in curr:\n            curr.append(x)\n            permute(curr)\n            curr.pop()\npermute([])\nprint('Permutations Count:', len(res))",
        "java_input": "        int[] nums = {1, 2, 3};",
        "java_bug": "        int[] nums = {1, 2, 3};\n        List<List<Integer>> res = new ArrayList<>();\n        class Solver {\n            void dfs(List<Integer> curr) {\n                if (curr.size() == nums.length) { res.add(new ArrayList<>(curr)); return; }\n                for (int x : nums) {\n                    if (!curr.contains(x)) {\n                        curr.add(x);\n                        dfs(curr);\n                        curr.remove(curr.size() - 1);\n                    }\n                }\n            }\n        }\n        new Solver().dfs(new ArrayList<>());\n        System.out.println(\"Permutations Count: \" + res.size());",
        "java_solution": "        int[] nums = {1, 2, 3};\n        List<List<Integer>> res = new ArrayList<>();\n        class Solver {\n            void dfs(List<Integer> curr) {\n                if (curr.size() == nums.length) { res.add(new ArrayList<>(curr)); return; }\n                for (int x : nums) {\n                    if (!curr.contains(x)) {\n                        curr.add(x);\n                        dfs(curr);\n                        curr.remove(curr.size() - 1);\n                    }\n                }\n            }\n        }\n        new Solver().dfs(new ArrayList<>());\n        System.out.println(\"Permutations Count: \" + res.size());",
        "expected_output": "Permutations Count: 6",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes permutations decision tree.. However, 3 elements have 3! = 6 unique orderings.",
            "Core Concept: 3 elements have 3! = 6 unique orderings. In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: At each step choose an unvisited element and backtrack."
        ],
        "cause": [
            "Exhaustive search permutations tree.",
            "3! = 6 paths.",
            "Golden Rule: In permutations, check membership and backtrack after exploring."
        ]
    },
    {
        "topic_id": "recursion_backtracking",
        "topic_name": "Recursion & Backtracking",
        "level": 8,
        "title": "Combination Sum",
        "company": "Amazon, Adobe",
        "description": "Find all unique combinations of [2, 3, 6, 7] that sum to target = 7.",
        "py_input": "candidates = [2, 3, 6, 7]\ntarget = 7",
        "py_bug": "candidates = [2, 3, 6, 7]\ntarget = 7\nres = []\ndef dfs(remain, path, start):\n    if remain == 0: res.append(path); return # Bug: missing path copy\n    if remain < 0: return\n    for i in range(start, len(candidates)):\n        path.append(candidates[i])\n        dfs(remain - candidates[i], path, i)\n        path.pop()\ndfs(target, [], 0)\nprint('Found Combinations:', res)",
        "py_solution": "candidates = [2, 3, 6, 7]\ntarget = 7\nres = []\ndef dfs(remain, path, start):\n    if remain == 0: res.append(path[:]); return\n    if remain < 0: return\n    for i in range(start, len(candidates)):\n        path.append(candidates[i])\n        dfs(remain - candidates[i], path, i)\n        path.pop()\ndfs(target, [], 0)\nprint('Found Combinations:', res)",
        "java_input": "        int[] candidates = {2, 3, 6, 7};\n        int target = 7;",
        "java_bug": "        int[] candidates = {2, 3, 6, 7};\n        int target = 7;\n        List<List<Integer>> res = new ArrayList<>();\n        class Solver {\n            void dfs(int remain, List<Integer> path, int start) {\n                if (remain == 0) { res.add(new ArrayList<>(path)); return; }\n                if (remain < 0) return;\n                for (int i = start; i < candidates.length; i++) {\n                    path.add(candidates[i]);\n                    dfs(remain - candidates[i], path, i);\n                    path.remove(path.size() - 1);\n                }\n            }\n        }\n        new Solver().dfs(target, new ArrayList<>(), 0);\n        System.out.println(\"Found Combinations: \" + res);",
        "java_solution": "        int[] candidates = {2, 3, 6, 7};\n        int target = 7;\n        List<List<Integer>> res = new ArrayList<>();\n        class Solver {\n            void dfs(int remain, List<Integer> path, int start) {\n                if (remain == 0) { res.add(new ArrayList<>(path)); return; }\n                if (remain < 0) return;\n                for (int i = start; i < candidates.length; i++) {\n                    path.add(candidates[i]);\n                    dfs(remain - candidates[i], path, i);\n                    path.remove(path.size() - 1);\n                }\n            }\n        }\n        new Solver().dfs(target, new ArrayList<>(), 0);\n        System.out.println(\"Found Combinations: \" + res);",
        "expected_output": "Found Combinations: [[2, 2, 3], [7]]",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes base case result storage.. However, Must save a clone `path[:]`, otherwise popping empties the saved answer.",
            "Core Concept: Must save a clone `path[:]`, otherwise popping empties the saved answer. In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Use `res.append(path[:])`."
        ],
        "cause": [
            "Reference bug in backtracking answer storage.",
            "Backtracking path mutation invalidates uncopied answers.",
            "Golden Rule: Snapshot the solution path before saving."
        ]
    },
    {
        "topic_id": "recursion_backtracking",
        "topic_name": "Recursion & Backtracking",
        "level": 9,
        "title": "Word Search in 2D Grid",
        "company": "Amazon, Microsoft",
        "description": "Determine if word 'ABCCED' exists in the grid using depth-first search backtracking.",
        "py_input": "board = [['A','B','C','E'], ['S','F','C','S'], ['A','D','E','E']]\nword = 'ABCCED'",
        "py_bug": "board = [['A','B','C','E'], ['S','F','C','S'], ['A','D','E','E']]\nword = 'ABCCED'\ndef dfs(r, c, k):\n    if k == len(word): return True\n    if not (0 <= r < len(board) and 0 <= c < len(board[0])) or board[r][c] != word[k]: return False\n    temp, board[r][c] = board[r][c], '#'\n    found = dfs(r+1, c, k+1) or dfs(r-1, c, k+1) or dfs(r, c+1, k+1) or dfs(r, c-1, k+1)\n    board[r][c] = temp\n    return found\nfound = any(dfs(i, j, 0) for i in range(len(board)) for j in range(len(board[0])))\nprint('Word Found:', found)",
        "py_solution": "board = [['A','B','C','E'], ['S','F','C','S'], ['A','D','E','E']]\nword = 'ABCCED'\ndef dfs(r, c, k):\n    if k == len(word): return True\n    if not (0 <= r < len(board) and 0 <= c < len(board[0])) or board[r][c] != word[k]: return False\n    temp, board[r][c] = board[r][c], '#'\n    found = dfs(r+1, c, k+1) or dfs(r-1, c, k+1) or dfs(r, c+1, k+1) or dfs(r, c-1, k+1)\n    board[r][c] = temp\n    return found\nfound = any(dfs(i, j, 0) for i in range(len(board)) for j in range(len(board[0])))\nprint('Word Found:', found)",
        "java_input": "        char[][] board = {{'A','B','C','E'}, {'S','F','C','S'}, {'A','D','E','E'}};\n        String word = \"ABCCED\";",
        "java_bug": "        char[][] board = {{'A','B','C','E'}, {'S','F','C','S'}, {'A','D','E','E'}};\n        String word = \"ABCCED\";\n        class Solver {\n            boolean dfs(int r, int c, int k) {\n                if (k == word.length()) return true;\n                if (r < 0 || r >= board.length || c < 0 || c >= board[0].length || board[r][c] != word.charAt(k)) return false;\n                char temp = board[r][c]; board[r][c] = '#';\n                boolean ok = dfs(r+1,c,k+1) || dfs(r-1,c,k+1) || dfs(r,c+1,k+1) || dfs(r,c-1,k+1);\n                board[r][c] = temp;\n                return ok;\n            }\n        }\n        boolean found = false;\n        Solver s = new Solver();\n        for (int i = 0; i < board.length && !found; i++)\n            for (int j = 0; j < board[0].length && !found; j++)\n                if (s.dfs(i, j, 0)) found = true;\n        System.out.println(\"Word Found: \" + found);",
        "java_solution": "        char[][] board = {{'A','B','C','E'}, {'S','F','C','S'}, {'A','D','E','E'}};\n        String word = \"ABCCED\";\n        class Solver {\n            boolean dfs(int r, int c, int k) {\n                if (k == word.length()) return true;\n                if (r < 0 || r >= board.length || c < 0 || c >= board[0].length || board[r][c] != word.charAt(k)) return false;\n                char temp = board[r][c]; board[r][c] = '#';\n                boolean ok = dfs(r+1,c,k+1) || dfs(r-1,c,k+1) || dfs(r,c+1,k+1) || dfs(r,c-1,k+1);\n                board[r][c] = temp;\n                return ok;\n            }\n        }\n        boolean found = false;\n        Solver s = new Solver();\n        for (int i = 0; i < board.length && !found; i++)\n            for (int j = 0; j < board[0].length && !found; j++)\n                if (s.dfs(i, j, 0)) found = true;\n        System.out.println(\"Word Found: \" + found);",
        "expected_output": "Word Found: True",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes cell visitation marking.. However, Mark visited cell with '#' to prevent reusing it, and restore it upon returning.",
            "Core Concept: Mark visited cell with '#' to prevent reusing it, and restore it upon returning. In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Restore original character `board[r][c] = temp` after exploring all 4 directions."
        ],
        "cause": [
            "Grid backtracking pattern.",
            "State restoration ensures alternate paths can reuse grid cells.",
            "Golden Rule: Always revert board state after recursion branches finish."
        ]
    },
    {
        "topic_id": "recursion_backtracking",
        "topic_name": "Recursion & Backtracking",
        "level": 10,
        "title": "N-Queens Placement Solutions",
        "company": "Google, Meta",
        "description": "Count total valid placements of 4 queens on a 4x4 chessboard with no mutual attacks.",
        "py_input": "n = 4",
        "py_bug": "n = 4\ncols = set()\ndiag1 = set()\ndiag2 = set()\ncount = 0\ndef solve(r):\n    global count\n    if r == n: count += 1; return\n    for c in range(n):\n        if c in cols or (r + c) in diag1 or (r - c) in diag2: continue\n        cols.add(c); diag1.add(r + c); diag2.add(r - c)\n        solve(r + 1)\n        cols.remove(c); diag1.remove(r + c); diag2.remove(r - c)\nsolve(0)\nprint('N-Queens Solutions:', count)",
        "py_solution": "n = 4\ncols = set()\ndiag1 = set()\ndiag2 = set()\ncount = 0\ndef solve(r):\n    global count\n    if r == n: count += 1; return\n    for c in range(n):\n        if c in cols or (r + c) in diag1 or (r - c) in diag2: continue\n        cols.add(c); diag1.add(r + c); diag2.add(r - c)\n        solve(r + 1)\n        cols.remove(c); diag1.remove(r + c); diag2.remove(r - c)\nsolve(0)\nprint('N-Queens Solutions:', count)",
        "java_input": "        int n = 4;",
        "java_bug": "        int n = 4;\n        Set<Integer> cols = new HashSet<>(), d1 = new HashSet<>(), d2 = new HashSet<>();\n        class Solver {\n            int cnt = 0;\n            void solve(int r) {\n                if (r == n) { cnt++; return; }\n                for (int c = 0; c < n; c++) {\n                    if (cols.contains(c) || d1.contains(r + c) || d2.contains(r - c)) continue;\n                    cols.add(c); d1.add(r + c); d2.add(r - c);\n                    solve(r + 1);\n                    cols.remove(c); d1.remove(r + c); d2.remove(r - c);\n                }\n            }\n        }\n        Solver s = new Solver(); s.solve(0);\n        System.out.println(\"N-Queens Solutions: \" + s.cnt);",
        "java_solution": "        int n = 4;\n        Set<Integer> cols = new HashSet<>(), d1 = new HashSet<>(), d2 = new HashSet<>();\n        class Solver {\n            int cnt = 0;\n            void solve(int r) {\n                if (r == n) { cnt++; return; }\n                for (int c = 0; c < n; c++) {\n                    if (cols.contains(c) || d1.contains(r + c) || d2.contains(r - c)) continue;\n                    cols.add(c); d1.add(r + c); d2.add(r - c);\n                    solve(r + 1);\n                    cols.remove(c); d1.remove(r + c); d2.remove(r - c);\n                }\n            }\n        }\n        Solver s = new Solver(); s.solve(0);\n        System.out.println(\"N-Queens Solutions: \" + s.cnt);",
        "expected_output": "N-Queens Solutions: 2",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes column and diagonal conflict sets.. However, Queens cannot share a row, a column, or diagonals (r + c and r - c).",
            "Core Concept: Queens cannot share a row, a column, or diagonals (r + c and r - c). In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Place row by row, tracking occupied columns and diagonals."
        ],
        "cause": [
            "Exhaustive constraint satisfaction problem.",
            "Diagonal indexing using r + c and r - c prevents conflicts.",
            "Golden Rule: Diagonal index invariants are `r + c` and `r - c`."
        ]
    }
]

print("Loaded Part 4 (Stacks & Recursion):", len(PART_4))
