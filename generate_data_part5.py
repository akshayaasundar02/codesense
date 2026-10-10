# Part 5 of Questions Catalog (Topic 8: Trees, Topic 9: Heaps, Topic 10: DP)

PART_5 = [
    # =========================================================================
    # TOPIC 8: BINARY TREES & BSTs (10 Placement Questions)
    # =========================================================================
    {
        "topic_id": "trees_bst",
        "topic_name": "Binary Trees & BSTs",
        "level": 1,
        "title": "Inorder Traversal of Binary Tree",
        "company": "Amazon, TCS",
        "description": "Perform Left-Root-Right inorder traversal on binary tree [1, None, 2, 3].",
        "py_input": "class Node:\n    def __init__(self, val, left=None, right=None):\n        self.val = val; self.left = left; self.right = right\nroot = Node(1, None, Node(2, Node(3), None))",
        "py_bug": "class Node:\n    def __init__(self, val, left=None, right=None):\n        self.val = val; self.left = left; self.right = right\nroot = Node(1, None, Node(2, Node(3), None))\nres = []\ndef inorder(node):\n    res.append(node.val) # Bug: visited root before left!\n    if node.left: inorder(node.left)\n    if node.right: inorder(node.right)\ninorder(root)\nprint('Inorder:', res)",
        "py_solution": "class Node:\n    def __init__(self, val, left=None, right=None):\n        self.val = val; self.left = left; self.right = right\nroot = Node(1, None, Node(2, Node(3), None))\nres = []\ndef inorder(node):\n    if not node: return\n    inorder(node.left)\n    res.append(node.val)\n    inorder(node.right)\ninorder(root)\nprint('Inorder:', res)",
        "java_input": "        class Node { int val; Node left, right; Node(int v){val=v;} }\n        Node root = new Node(1);\n        root.right = new Node(2);\n        root.right.left = new Node(3);",
        "java_bug": "        class Node { int val; Node left, right; Node(int v){val=v;} }\n        Node root = new Node(1);\n        root.right = new Node(2);\n        root.right.left = new Node(3);\n        List<Integer> res = new ArrayList<>();\n        class Traversal {\n            void dfs(Node n) {\n                if (n == null) return;\n                res.add(n.val);\n                dfs(n.left);\n                dfs(n.right);\n            }\n        }\n        new Traversal().dfs(root);\n        System.out.println(\"Inorder: \" + res);",
        "java_solution": "        class Node { int val; Node left, right; Node(int v){val=v;} }\n        Node root = new Node(1);\n        root.right = new Node(2);\n        root.right.left = new Node(3);\n        List<Integer> res = new ArrayList<>();\n        class Traversal {\n            void dfs(Node n) {\n                if (n == null) return;\n                dfs(n.left);\n                res.add(n.val);\n                dfs(n.right);\n            }\n        }\n        new Traversal().dfs(root);\n        System.out.println(\"Inorder: \" + res);",
        "expected_output": "Inorder: [1, 3, 2]",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes where you append the node value.. However, Inorder order is Left -> Root -> Right.",
            "Core Concept: Inorder order is Left -> Root -> Right. In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Recurse on `node.left` first, append `node.val`, then recurse on `node.right`."
        ],
        "cause": [
            "Appending value first produced preorder traversal instead of inorder.",
            "Inorder visits entire left subtree before processing the current root.",
            "Golden Rule: Inorder traversal sequence is `traverse(left)`, `process(node)`, `traverse(right)`."
        ]
    },
    {
        "topic_id": "trees_bst",
        "topic_name": "Binary Trees & BSTs",
        "level": 2,
        "title": "Maximum Depth (Height) of Binary Tree",
        "company": "Google, Microsoft",
        "description": "Find maximum depth (number of nodes along longest path from root to leaf) of tree [3, 9, 20, None, None, 15, 7].",
        "py_input": "class Node:\n    def __init__(self, val, left=None, right=None):\n        self.val = val; self.left = left; self.right = right\nroot = Node(3, Node(9), Node(20, Node(15), Node(7)))",
        "py_bug": "class Node:\n    def __init__(self, val, left=None, right=None):\n        self.val = val; self.left = left; self.right = right\nroot = Node(3, Node(9), Node(20, Node(15), Node(7)))\ndef max_depth(node):\n    # Bug: missing base case for None!\n    return 1 + max(max_depth(node.left), max_depth(node.right))\nprint('Max Depth:', max_depth(root))",
        "py_solution": "class Node:\n    def __init__(self, val, left=None, right=None):\n        self.val = val; self.left = left; self.right = right\nroot = Node(3, Node(9), Node(20, Node(15), Node(7)))\ndef max_depth(node):\n    if not node: return 0\n    return 1 + max(max_depth(node.left), max_depth(node.right))\nprint('Max Depth:', max_depth(root))",
        "java_input": "        class Node { int val; Node left, right; Node(int v){val=v;} }\n        Node root = new Node(3);\n        root.left = new Node(9);\n        root.right = new Node(20);\n        root.right.left = new Node(15);\n        root.right.right = new Node(7);",
        "java_bug": "        class Node { int val; Node left, right; Node(int v){val=v;} }\n        Node root = new Node(3);\n        root.left = new Node(9);\n        root.right = new Node(20);\n        root.right.left = new Node(15);\n        root.right.right = new Node(7);\n        class TreeUtil {\n            int depth(Node n) {\n                return 1 + Math.max(depth(n.left), depth(n.right)); // NullPointerException\n            }\n        }\n        System.out.println(\"Max Depth: \" + new TreeUtil().depth(root));",
        "java_solution": "        class Node { int val; Node left, right; Node(int v){val=v;} }\n        Node root = new Node(3);\n        root.left = new Node(9);\n        root.right = new Node(20);\n        root.right.left = new Node(15);\n        root.right.right = new Node(7);\n        class TreeUtil {\n            int depth(Node n) {\n                if (n == null) return 0;\n                return 1 + Math.max(depth(n.left), depth(n.right));\n            }\n        }\n        System.out.println(\"Max Depth: \" + new TreeUtil().depth(root));",
        "expected_output": "Max Depth: 3",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes what happens when a leaf node calls depth on its null children.. However, `node.left` or `node.right` can be None/null, crashing with AttributeError / NullPointerException.",
            "Core Concept: `node.left` or `node.right` can be None/null, crashing with AttributeError / NullPointerException. In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Guard with `if not node: return 0`."
        ],
        "cause": [
            "Dereferencing null pointer on empty child leaves.",
            "Tree traversal must terminate at null leaves.",
            "Golden Rule: Always check `if not node: return 0` as the first line of tree recursion."
        ]
    },
    {
        "topic_id": "trees_bst",
        "topic_name": "Binary Trees & BSTs",
        "level": 3,
        "title": "Check if Two Binary Trees are Identical",
        "company": "Amazon, Adobe",
        "description": "Determine if two binary trees are structurally identical and have the same node values.",
        "py_input": "class Node:\n    def __init__(self, val, left=None, right=None):\n        self.val = val; self.left = left; self.right = right\nt1 = Node(1, Node(2), Node(3))\nt2 = Node(1, Node(2), Node(3))",
        "py_bug": "class Node:\n    def __init__(self, val, left=None, right=None):\n        self.val = val; self.left = left; self.right = right\nt1 = Node(1, Node(2), Node(3))\nt2 = Node(1, Node(2), Node(3))\ndef is_same(p, q):\n    if not p and not q: return True\n    if not p or not q: return False\n    return p.val == q.val and is_same(p.left, q.left) and is_same(p.right, q.right)\nprint('Are Identical:', is_same(t1, t2))",
        "py_solution": "class Node:\n    def __init__(self, val, left=None, right=None):\n        self.val = val; self.left = left; self.right = right\nt1 = Node(1, Node(2), Node(3))\nt2 = Node(1, Node(2), Node(3))\ndef is_same(p, q):\n    if not p and not q: return True\n    if not p or not q: return False\n    return p.val == q.val and is_same(p.left, q.left) and is_same(p.right, q.right)\nprint('Are Identical:', is_same(t1, t2))",
        "java_input": "        class Node { int val; Node left, right; Node(int v){val=v;} }\n        Node t1 = new Node(1); t1.left = new Node(2); t1.right = new Node(3);\n        Node t2 = new Node(1); t2.left = new Node(2); t2.right = new Node(3);",
        "java_bug": "        class Node { int val; Node left, right; Node(int v){val=v;} }\n        Node t1 = new Node(1); t1.left = new Node(2); t1.right = new Node(3);\n        Node t2 = new Node(1); t2.left = new Node(2); t2.right = new Node(3);\n        class Checker {\n            boolean isSame(Node p, Node q) {\n                if (p == null && q == null) return true;\n                if (p == null || q == null) return false;\n                return p.val == q.val && isSame(p.left, q.left) && isSame(p.right, q.right);\n            }\n        }\n        System.out.println(\"Are Identical: \" + new Checker().isSame(t1, t2));",
        "java_solution": "        class Node { int val; Node left, right; Node(int v){val=v;} }\n        Node t1 = new Node(1); t1.left = new Node(2); t1.right = new Node(3);\n        Node t2 = new Node(1); t2.left = new Node(2); t2.right = new Node(3);\n        class Checker {\n            boolean isSame(Node p, Node q) {\n                if (p == null && q == null) return true;\n                if (p == null || q == null) return false;\n                return p.val == q.val && isSame(p.left, q.left) && isSame(p.right, q.right);\n            }\n        }\n        System.out.println(\"Are Identical: \" + new Checker().isSame(t1, t2));",
        "expected_output": "Are Identical: True",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes base cases for null nodes.. However, Both null -> True, one null -> False, values mismatch -> False.",
            "Core Concept: Both null -> True, one null -> False, values mismatch -> False. In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Recursively compare values and subtrees."
        ],
        "cause": [
            "Structural equality check in binary trees.",
            "Both trees must match in topology and values.",
            "Golden Rule: Compare `not p and not q` before dereferencing node values."
        ]
    },
    {
        "topic_id": "trees_bst",
        "topic_name": "Binary Trees & BSTs",
        "level": 4,
        "title": "Invert (Mirror) a Binary Tree",
        "company": "Google, Twitter",
        "description": "Invert binary tree by swapping left and right subtrees recursively.",
        "py_input": "class Node:\n    def __init__(self, val, left=None, right=None):\n        self.val = val; self.left = left; self.right = right\nroot = Node(4, Node(2), Node(7))",
        "py_bug": "class Node:\n    def __init__(self, val, left=None, right=None):\n        self.val = val; self.left = left; self.right = right\nroot = Node(4, Node(2), Node(7))\ndef invert(node):\n    if not node: return None\n    node.left = invert(node.right) # Bug: overwrote left before inverting original left!\n    node.right = invert(node.left)\n    return node\ninvert(root)\nprint('Inverted Root Value:', root.val)",
        "py_solution": "class Node:\n    def __init__(self, val, left=None, right=None):\n        self.val = val; self.left = left; self.right = right\nroot = Node(4, Node(2), Node(7))\ndef invert(node):\n    if not node: return None\n    node.left, node.right = invert(node.right), invert(node.left)\n    return node\ninvert(root)\nprint('Inverted Root Value:', root.val)",
        "java_input": "        class Node { int val; Node left, right; Node(int v){val=v;} }\n        Node root = new Node(4); root.left = new Node(2); root.right = new Node(7);",
        "java_bug": "        class Node { int val; Node left, right; Node(int v){val=v;} }\n        Node root = new Node(4); root.left = new Node(2); root.right = new Node(7);\n        class Inverter {\n            Node invert(Node n) {\n                if (n == null) return null;\n                Node temp = n.left;\n                n.left = invert(n.right);\n                n.right = invert(temp);\n                return n;\n            }\n        }\n        new Inverter().invert(root);\n        System.out.println(\"Inverted Root Value: \" + root.val);",
        "java_solution": "        class Node { int val; Node left, right; Node(int v){val=v;} }\n        Node root = new Node(4); root.left = new Node(2); root.right = new Node(7);\n        class Inverter {\n            Node invert(Node n) {\n                if (n == null) return null;\n                Node temp = n.left;\n                n.left = invert(n.right);\n                n.right = invert(temp);\n                return n;\n            }\n        }\n        new Inverter().invert(root);\n        System.out.println(\"Inverted Root Value: \" + root.val);",
        "expected_output": "Inverted Root Value: 4",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes swapping left and right pointers.. However, If you overwrite `node.left` first, you lose the reference to the original left subtree!",
            "Core Concept: If you overwrite `node.left` first, you lose the reference to the original left subtree! In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Swap simultaneously with tuple unpacking `node.left, node.right = ...` or use a temp variable."
        ],
        "cause": [
            "Overwriting pointer before saving creates duplicate subtrees.",
            "Tree mutation requires temporary pointer swap.",
            "Golden Rule: Swap pointers simultaneously or preserve the old pointer in a temporary variable."
        ]
    },
    {
        "topic_id": "trees_bst",
        "topic_name": "Binary Trees & BSTs",
        "level": 5,
        "title": "Symmetric Tree (Mirror Image Check)",
        "company": "Microsoft, Amazon",
        "description": "Check whether a binary tree is a mirror of itself around its center.",
        "py_input": "class Node:\n    def __init__(self, val, left=None, right=None):\n        self.val = val; self.left = left; self.right = right\nroot = Node(1, Node(2, Node(3), Node(4)), Node(2, Node(4), Node(3)))",
        "py_bug": "class Node:\n    def __init__(self, val, left=None, right=None):\n        self.val = val; self.left = left; self.right = right\nroot = Node(1, Node(2, Node(3), Node(4)), Node(2, Node(4), Node(3)))\ndef is_sym(t1, t2):\n    if not t1 and not t2: return True\n    if not t1 or not t2: return False\n    return t1.val == t2.val and is_sym(t1.left, t2.right) and is_sym(t1.right, t2.left)\nprint('Is Symmetric:', is_sym(root.left, root.right))",
        "py_solution": "class Node:\n    def __init__(self, val, left=None, right=None):\n        self.val = val; self.left = left; self.right = right\nroot = Node(1, Node(2, Node(3), Node(4)), Node(2, Node(4), Node(3)))\ndef is_sym(t1, t2):\n    if not t1 and not t2: return True\n    if not t1 or not t2: return False\n    return t1.val == t2.val and is_sym(t1.left, t2.right) and is_sym(t1.right, t2.left)\nprint('Is Symmetric:', is_sym(root.left, root.right))",
        "java_input": "        class Node { int val; Node left, right; Node(int v){val=v;} }\n        Node root = new Node(1);\n        root.left = new Node(2); root.left.left = new Node(3); root.left.right = new Node(4);\n        root.right = new Node(2); root.right.left = new Node(4); root.right.right = new Node(3);",
        "java_bug": "        class Node { int val; Node left, right; Node(int v){val=v;} }\n        Node root = new Node(1);\n        root.left = new Node(2); root.left.left = new Node(3); root.left.right = new Node(4);\n        root.right = new Node(2); root.right.left = new Node(4); root.right.right = new Node(3);\n        class Sym {\n            boolean check(Node t1, Node t2) {\n                if (t1 == null && t2 == null) return true;\n                if (t1 == null || t2 == null) return false;\n                return t1.val == t2.val && check(t1.left, t2.right) && check(t1.right, t2.left);\n            }\n        }\n        System.out.println(\"Is Symmetric: \" + new Sym().check(root.left, root.right));",
        "java_solution": "        class Node { int val; Node left, right; Node(int v){val=v;} }\n        Node root = new Node(1);\n        root.left = new Node(2); root.left.left = new Node(3); root.left.right = new Node(4);\n        root.right = new Node(2); root.right.left = new Node(4); root.right.right = new Node(3);\n        class Sym {\n            boolean check(Node t1, Node t2) {\n                if (t1 == null && t2 == null) return true;\n                if (t1 == null || t2 == null) return false;\n                return t1.val == t2.val && check(t1.left, t2.right) && check(t1.right, t2.left);\n            }\n        }\n        System.out.println(\"Is Symmetric: \" + new Sym().check(root.left, root.right));",
        "expected_output": "Is Symmetric: True",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes mirror reflection pairs.. However, `t1.left` must match `t2.right`, and `t1.right` must match `t2.left`.",
            "Core Concept: `t1.left` must match `t2.right`, and `t1.right` must match `t2.left`. In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Compare outer pairs and inner pairs."
        ],
        "cause": [
            "Symmetry requires cross-matching left and right children.",
            "Mirror property matches outer with outer and inner with inner.",
            "Golden Rule: Compare `t1.left` with `t2.right` and `t1.right` with `t2.left`."
        ]
    },
    {
        "topic_id": "trees_bst",
        "topic_name": "Binary Trees & BSTs",
        "level": 6,
        "title": "Search in a Binary Search Tree (BST)",
        "company": "Oracle, Infosys",
        "description": "Find node with val = 5 in BST with root 4, left 2, right 7.",
        "py_input": "class Node:\n    def __init__(self, val, left=None, right=None):\n        self.val = val; self.left = left; self.right = right\nroot = Node(4, Node(2, Node(1), Node(3)), Node(7, Node(5), None))\nval = 5",
        "py_bug": "class Node:\n    def __init__(self, val, left=None, right=None):\n        self.val = val; self.left = left; self.right = right\nroot = Node(4, Node(2, Node(1), Node(3)), Node(7, Node(5), None))\nval = 5\ndef search_bst(node, target):\n    if not node: return False\n    if node.val == target: return True\n    elif target < node.val: return search_bst(node.right, target) # Bug: searched right instead of left!\n    else: return search_bst(node.left, target)\nprint('Found in BST:', search_bst(root, val))",
        "py_solution": "class Node:\n    def __init__(self, val, left=None, right=None):\n        self.val = val; self.left = left; self.right = right\nroot = Node(4, Node(2, Node(1), Node(3)), Node(7, Node(5), None))\nval = 5\ndef search_bst(node, target):\n    if not node: return False\n    if node.val == target: return True\n    elif target < node.val: return search_bst(node.left, target)\n    else: return search_bst(node.right, target)\nprint('Found in BST:', search_bst(root, val))",
        "java_input": "        class Node { int val; Node left, right; Node(int v){val=v;} }\n        Node root = new Node(4);\n        root.left = new Node(2); root.left.left = new Node(1); root.left.right = new Node(3);\n        root.right = new Node(7); root.right.left = new Node(5);\n        int val = 5;",
        "java_bug": "        class Node { int val; Node left, right; Node(int v){val=v;} }\n        Node root = new Node(4);\n        root.left = new Node(2); root.left.left = new Node(1); root.left.right = new Node(3);\n        root.right = new Node(7); root.right.left = new Node(5);\n        int val = 5;\n        class BstSearch {\n            boolean search(Node n, int v) {\n                if (n == null) return false;\n                if (n.val == v) return true;\n                return v < n.val ? search(n.right, v) : search(n.left, v);\n            }\n        }\n        System.out.println(\"Found in BST: \" + new BstSearch().search(root, val));",
        "java_solution": "        class Node { int val; Node left, right; Node(int v){val=v;} }\n        Node root = new Node(4);\n        root.left = new Node(2); root.left.left = new Node(1); root.left.right = new Node(3);\n        root.right = new Node(7); root.right.left = new Node(5);\n        int val = 5;\n        class BstSearch {\n            boolean search(Node n, int v) {\n                if (n == null) return false;\n                if (n.val == v) return true;\n                return v < n.val ? search(n.left, v) : search(n.right, v);\n            }\n        }\n        System.out.println(\"Found in BST: \" + new BstSearch().search(root, val));",
        "expected_output": "Found in BST: True",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes which child you branch towards when target < node.val.. However, In a BST, smaller values are strictly in the LEFT subtree.",
            "Core Concept: In a BST, smaller values are strictly in the LEFT subtree. In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: When `target < node.val`, search `node.left`."
        ],
        "cause": [
            "BST invariant inverted: smaller elements are in left subtree, not right.",
            "Searching the wrong branch misses existing elements.",
            "Golden Rule: In BST, `target < val` goes left, `target > val` goes right."
        ]
    },
    {
        "topic_id": "trees_bst",
        "topic_name": "Binary Trees & BSTs",
        "level": 7,
        "title": "Lowest Common Ancestor (LCA) in BST",
        "company": "Amazon, Meta",
        "description": "Find lowest common ancestor node value for p = 2 and q = 8 in BST with root 6.",
        "py_input": "class Node:\n    def __init__(self, val, left=None, right=None):\n        self.val = val; self.left = left; self.right = right\nroot = Node(6, Node(2), Node(8))\np, q = 2, 8",
        "py_bug": "class Node:\n    def __init__(self, val, left=None, right=None):\n        self.val = val; self.left = left; self.right = right\nroot = Node(6, Node(2), Node(8))\np, q = 2, 8\ncurr = root\nwhile curr:\n    if p < curr.val and q < curr.val: curr = curr.left\n    elif p > curr.val and q > curr.val: curr = curr.right\n    else: break\nprint('LCA Value:', curr.val)",
        "py_solution": "class Node:\n    def __init__(self, val, left=None, right=None):\n        self.val = val; self.left = left; self.right = right\nroot = Node(6, Node(2), Node(8))\np, q = 2, 8\ncurr = root\nwhile curr:\n    if p < curr.val and q < curr.val: curr = curr.left\n    elif p > curr.val and q > curr.val: curr = curr.right\n    else: break\nprint('LCA Value:', curr.val)",
        "java_input": "        class Node { int val; Node left, right; Node(int v){val=v;} }\n        Node root = new Node(6); root.left = new Node(2); root.right = new Node(8);\n        int p = 2, q = 8;",
        "java_bug": "        class Node { int val; Node left, right; Node(int v){val=v;} }\n        Node root = new Node(6); root.left = new Node(2); root.right = new Node(8);\n        int p = 2, q = 8;\n        Node curr = root;\n        while (curr != null) {\n            if (p < curr.val && q < curr.val) curr = curr.left;\n            else if (p > curr.val && q > curr.val) curr = curr.right;\n            else break;\n        }\n        System.out.println(\"LCA Value: \" + curr.val);",
        "java_solution": "        class Node { int val; Node left, right; Node(int v){val=v;} }\n        Node root = new Node(6); root.left = new Node(2); root.right = new Node(8);\n        int p = 2, q = 8;\n        Node curr = root;\n        while (curr != null) {\n            if (p < curr.val && q < curr.val) curr = curr.left;\n            else if (p > curr.val && q > curr.val) curr = curr.right;\n            else break;\n        }\n        System.out.println(\"LCA Value: \" + curr.val);",
        "expected_output": "LCA Value: 6",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes the split point.. However, If p and q lie on opposite sides of the current node, the current node is their lowest common ancestor.",
            "Core Concept: If p and q lie on opposite sides of the current node, the current node is their lowest common ancestor. In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: When one is on the left and one on the right, return current node."
        ],
        "cause": [
            "BST ordering property allows O(height) LCA lookup without storing paths.",
            "Split point uniquely identifies the lowest common ancestor.",
            "Golden Rule: The split point where p and q diverge in a BST is the LCA."
        ]
    },
    {
        "topic_id": "trees_bst",
        "topic_name": "Binary Trees & BSTs",
        "level": 8,
        "title": "Validate Binary Search Tree",
        "company": "Amazon, Microsoft",
        "description": "Validate whether a binary tree strictly obeys the BST rule: all nodes in left subtree are strictly less than node, and all in right are strictly greater.",
        "py_input": "class Node:\n    def __init__(self, val, left=None, right=None):\n        self.val = val; self.left = left; self.right = right\nroot = Node(10, Node(5), Node(15))",
        "py_bug": "class Node:\n    def __init__(self, val, left=None, right=None):\n        self.val = val; self.left = left; self.right = right\nroot = Node(10, Node(5), Node(15))\ndef is_valid(node):\n    # Bug: only checking immediate children, not entire subtree bounds!\n    if not node: return True\n    if node.left and node.left.val >= node.val: return False\n    if node.right and node.right.val <= node.val: return False\n    return is_valid(node.left) and is_valid(node.right)\nprint('Is Valid BST:', is_valid(root))",
        "py_solution": "class Node:\n    def __init__(self, val, left=None, right=None):\n        self.val = val; self.left = left; self.right = right\nroot = Node(10, Node(5), Node(15))\ndef is_valid(node, low=float('-inf'), high=float('inf')):\n    if not node: return True\n    if not (low < node.val < high): return False\n    return is_valid(node.left, low, node.val) and is_valid(node.right, node.val, high)\nprint('Is Valid BST:', is_valid(root))",
        "java_input": "        class Node { int val; Node left, right; Node(int v){val=v;} }\n        Node root = new Node(10); root.left = new Node(5); root.right = new Node(15);",
        "java_bug": "        class Node { int val; Node left, right; Node(int v){val=v;} }\n        Node root = new Node(10); root.left = new Node(5); root.right = new Node(15);\n        class ValidBst {\n            boolean check(Node n, long min, long max) {\n                if (n == null) return true;\n                if (n.val <= min || n.val >= max) return false;\n                return check(n.left, min, n.val) && check(n.right, n.val, max);\n            }\n        }\n        System.out.println(\"Is Valid BST: \" + new ValidBst().check(root, Long.MIN_VALUE, Long.MAX_VALUE));",
        "java_solution": "        class Node { int val; Node left, right; Node(int v){val=v;} }\n        Node root = new Node(10); root.left = new Node(5); root.right = new Node(15);\n        class ValidBst {\n            boolean check(Node n, long min, long max) {\n                if (n == null) return true;\n                if (n.val <= min || n.val >= max) return false;\n                return check(n.left, min, n.val) && check(n.right, n.val, max);\n            }\n        }\n        System.out.println(\"Is Valid BST: \" + new ValidBst().check(root, Long.MIN_VALUE, Long.MAX_VALUE));",
        "expected_output": "Is Valid BST: True",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes range bounds (min and max allowable values).. However, It is not enough for a node to be greater than its left child; it must be greater than ALL nodes in its left subtree.",
            "Core Concept: It is not enough for a node to be greater than its left child; it must be greater than ALL nodes in its left subtree. In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Pass `(low, high)` boundaries recursively down the tree."
        ],
        "cause": [
            "Checking only immediate children allows invalid grandchild violations.",
            "BST definition requires global subtree bounds.",
            "Golden Rule: Pass `(min, max)` interval down the recursion to validate BSTs."
        ]
    },
    {
        "topic_id": "trees_bst",
        "topic_name": "Binary Trees & BSTs",
        "level": 9,
        "title": "Level Order Traversal (BFS)",
        "company": "Google, Amazon",
        "description": "Traverse binary tree level-by-level using a FIFO queue.",
        "py_input": "from collections import deque\nclass Node:\n    def __init__(self, val, left=None, right=None):\n        self.val = val; self.left = left; self.right = right\nroot = Node(3, Node(9), Node(20, Node(15), Node(7)))",
        "py_bug": "from collections import deque\nclass Node:\n    def __init__(self, val, left=None, right=None):\n        self.val = val; self.left = left; self.right = right\nroot = Node(3, Node(9), Node(20, Node(15), Node(7)))\nres = []\nq = deque([root])\nwhile q:\n    level = []\n    for _ in range(len(q)):\n        node = q.popleft()\n        level.append(node.val)\n        if node.left: q.append(node.left)\n        if node.right: q.append(node.right)\n    res.append(level)\nprint('Level Order:', res)",
        "py_solution": "from collections import deque\nclass Node:\n    def __init__(self, val, left=None, right=None):\n        self.val = val; self.left = left; self.right = right\nroot = Node(3, Node(9), Node(20, Node(15), Node(7)))\nres = []\nq = deque([root])\nwhile q:\n    level = []\n    for _ in range(len(q)):\n        node = q.popleft()\n        level.append(node.val)\n        if node.left: q.append(node.left)\n        if node.right: q.append(node.right)\n    res.append(level)\nprint('Level Order:', res)",
        "java_input": "        class Node { int val; Node left, right; Node(int v){val=v;} }\n        Node root = new Node(3); root.left = new Node(9);\n        root.right = new Node(20); root.right.left = new Node(15); root.right.right = new Node(7);",
        "java_bug": "        class Node { int val; Node left, right; Node(int v){val=v;} }\n        Node root = new Node(3); root.left = new Node(9);\n        root.right = new Node(20); root.right.left = new Node(15); root.right.right = new Node(7);\n        List<List<Integer>> res = new ArrayList<>();\n        Queue<Node> q = new LinkedList<>();\n        q.offer(root);\n        while(!q.isEmpty()) {\n            int size = q.size();\n            List<Integer> lvl = new ArrayList<>();\n            for (int i = 0; i < size; i++) {\n                Node n = q.poll();\n                lvl.add(n.val);\n                if (n.left != null) q.offer(n.left);\n                if (n.right != null) q.offer(n.right);\n            }\n            res.add(lvl);\n        }\n        System.out.println(\"Level Order: \" + res);",
        "java_solution": "        class Node { int val; Node left, right; Node(int v){val=v;} }\n        Node root = new Node(3); root.left = new Node(9);\n        root.right = new Node(20); root.right.left = new Node(15); root.right.right = new Node(7);\n        List<List<Integer>> res = new ArrayList<>();\n        Queue<Node> q = new LinkedList<>();\n        q.offer(root);\n        while(!q.isEmpty()) {\n            int size = q.size();\n            List<Integer> lvl = new ArrayList<>();\n            for (int i = 0; i < size; i++) {\n                Node n = q.poll();\n                lvl.add(n.val);\n                if (n.left != null) q.offer(n.left);\n                if (n.right != null) q.offer(n.right);\n            }\n            res.add(lvl);\n        }\n        System.out.println(\"Level Order: \" + res);",
        "expected_output": "Level Order: [[3], [9, 20], [15, 7]]",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes queue size per level.. However, Capture `len(q)` at the start of each level to process all nodes on that horizontal level.",
            "Core Concept: Capture `len(q)` at the start of each level to process all nodes on that horizontal level. In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Loop for `len(q)` iterations and add children to queue."
        ],
        "cause": [
            "Standard BFS queue pattern.",
            "Queue snapshots partition tree by tree level.",
            "Golden Rule: In BFS level order, iterate `len(q)` times to process the current tier."
        ]
    },
    {
        "topic_id": "trees_bst",
        "topic_name": "Binary Trees & BSTs",
        "level": 10,
        "title": "Binary Tree Maximum Path Sum",
        "company": "Google, Meta",
        "description": "Find the maximum path sum of any non-empty path in binary tree [-10, 9, 20, None, None, 15, 7].",
        "py_input": "class Node:\n    def __init__(self, val, left=None, right=None):\n        self.val = val; self.left = left; self.right = right\nroot = Node(-10, Node(9), Node(20, Node(15), Node(7)))",
        "py_bug": "class Node:\n    def __init__(self, val, left=None, right=None):\n        self.val = val; self.left = left; self.right = right\nroot = Node(-10, Node(9), Node(20, Node(15), Node(7)))\nmax_sum = float('-inf')\ndef dfs(node):\n    global max_sum\n    if not node: return 0\n    l = max(0, dfs(node.left))\n    r = max(0, dfs(node.right))\n    max_sum = max(max_sum, node.val + l + r)\n    return node.val + max(l, r)\ndfs(root)\nprint('Max Path Sum:', max_sum)",
        "py_solution": "class Node:\n    def __init__(self, val, left=None, right=None):\n        self.val = val; self.left = left; self.right = right\nroot = Node(-10, Node(9), Node(20, Node(15), Node(7)))\nmax_sum = float('-inf')\ndef dfs(node):\n    global max_sum\n    if not node: return 0\n    l = max(0, dfs(node.left))\n    r = max(0, dfs(node.right))\n    max_sum = max(max_sum, node.val + l + r)\n    return node.val + max(l, r)\ndfs(root)\nprint('Max Path Sum:', max_sum)",
        "java_input": "        class Node { int val; Node left, right; Node(int v){val=v;} }\n        Node root = new Node(-10); root.left = new Node(9);\n        root.right = new Node(20); root.right.left = new Node(15); root.right.right = new Node(7);",
        "java_bug": "        class Node { int val; Node left, right; Node(int v){val=v;} }\n        Node root = new Node(-10); root.left = new Node(9);\n        root.right = new Node(20); root.right.left = new Node(15); root.right.right = new Node(7);\n        class Solver {\n            int max = Integer.MIN_VALUE;\n            int dfs(Node n) {\n                if (n == null) return 0;\n                int l = Math.max(0, dfs(n.left)), r = Math.max(0, dfs(n.right));\n                max = Math.max(max, n.val + l + r);\n                return n.val + Math.max(l, r);\n            }\n        }\n        Solver s = new Solver(); s.dfs(root);\n        System.out.println(\"Max Path Sum: \" + s.max);",
        "java_solution": "        class Node { int val; Node left, right; Node(int v){val=v;} }\n        Node root = new Node(-10); root.left = new Node(9);\n        root.right = new Node(20); root.right.left = new Node(15); root.right.right = new Node(7);\n        class Solver {\n            int max = Integer.MIN_VALUE;\n            int dfs(Node n) {\n                if (n == null) return 0;\n                int l = Math.max(0, dfs(n.left)), r = Math.max(0, dfs(n.right));\n                max = Math.max(max, n.val + l + r);\n                return n.val + Math.max(l, r);\n            }\n        }\n        Solver s = new Solver(); s.dfs(root);\n        System.out.println(\"Max Path Sum: \" + s.max);",
        "expected_output": "Max Path Sum: 42",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes return value vs global maximum update.. However, A path can curve through both children at the apex node (`node.val + l + r`), but can only return one branch (`node.val + max(l, r)`) upward.",
            "Core Concept: A path can curve through both children at the apex node (`node.val + l + r`), but can only return one branch (`node.val + max(l, r)`) upward. In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Discard negative branches with `max(0, ...)`, update global max, and return single branch sum."
        ],
        "cause": [
            "Path split rules: a path can only turn once.",
            "Parent calls can only extend one side.",
            "Golden Rule: Update global answer with `val + l + r`, but return `val + max(l, r)`."
        ]
    },

    # =========================================================================
    # TOPIC 9: HEAPS & PRIORITY QUEUES (10 Placement Questions)
    # =========================================================================
    {
        "topic_id": "heaps_priority",
        "topic_name": "Heaps & Priority Queues",
        "level": 1,
        "title": "Find Kth Smallest Element in Array",
        "company": "Amazon, TCS",
        "description": "Find the 3rd smallest element in [7, 10, 4, 3, 20, 15] using a heap.",
        "py_input": "import heapq\nnums = [7, 10, 4, 3, 20, 15]\nk = 3",
        "py_bug": "import heapq\nnums = [7, 10, 4, 3, 20, 15]\nk = 3\nheapq.heapify(nums)\nfor _ in range(k): # Bug: pops k times, leaving the (k+1)th or overwriting answer\n    ans = heapq.heappop(nums)\nprint('3rd Smallest:', ans)",
        "py_solution": "import heapq\nnums = [7, 10, 4, 3, 20, 15]\nk = 3\nheapq.heapify(nums)\nfor _ in range(k):\n    ans = heapq.heappop(nums)\nprint('3rd Smallest:', ans)",
        "java_input": "        int[] nums = {7, 10, 4, 3, 20, 15};\n        int k = 3;",
        "java_bug": "        int[] nums = {7, 10, 4, 3, 20, 15};\n        int k = 3;\n        PriorityQueue<Integer> pq = new PriorityQueue<>();\n        for (int x : nums) pq.add(x);\n        int ans = -1;\n        for (int i = 0; i < k; i++) ans = pq.poll();\n        System.out.println(\"3rd Smallest: \" + ans);",
        "java_solution": "        int[] nums = {7, 10, 4, 3, 20, 15};\n        int k = 3;\n        PriorityQueue<Integer> pq = new PriorityQueue<>();\n        for (int x : nums) pq.add(x);\n        int ans = -1;\n        for (int i = 0; i < k; i++) ans = pq.poll();\n        System.out.println(\"3rd Smallest: \" + ans);",
        "expected_output": "3rd Smallest: 7",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes min-heap extraction.. However, Min-heap pops the smallest element each time. Popping 3 times gives the 3rd smallest.",
            "Core Concept: Min-heap pops the smallest element each time. Popping 3 times gives the 3rd smallest. In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Heapify array and pop k times."
        ],
        "cause": [
            "Min-heap root is always the current minimum.",
            "Kth poll retrieves the kth smallest element in O(n + k log n).",
            "Golden Rule: Min-heap root guarantees minimum element."
        ]
    },
    {
        "topic_id": "heaps_priority",
        "topic_name": "Heaps & Priority Queues",
        "level": 2,
        "title": "Kth Largest Element in an Array",
        "company": "Goldman Sachs, Uber",
        "description": "Find the 2nd largest element in [3, 2, 1, 5, 6, 4] using a min-heap of size k.",
        "py_input": "import heapq\nnums = [3, 2, 1, 5, 6, 4]\nk = 2",
        "py_bug": "import heapq\nnums = [3, 2, 1, 5, 6, 4]\nk = 2\nh = []\nfor x in nums:\n    heapq.heappush(h, x)\n    if len(h) > k: heapq.heappop(h)\nprint('2nd Largest:', h[0])",
        "py_solution": "import heapq\nnums = [3, 2, 1, 5, 6, 4]\nk = 2\nh = []\nfor x in nums:\n    heapq.heappush(h, x)\n    if len(h) > k: heapq.heappop(h)\nprint('2nd Largest:', h[0])",
        "java_input": "        int[] nums = {3, 2, 1, 5, 6, 4};\n        int k = 2;",
        "java_bug": "        int[] nums = {3, 2, 1, 5, 6, 4};\n        int k = 2;\n        PriorityQueue<Integer> pq = new PriorityQueue<>();\n        for (int x : nums) {\n            pq.offer(x);\n            if (pq.size() > k) pq.poll();\n        }\n        System.out.println(\"2nd Largest: \" + pq.peek());",
        "java_solution": "        int[] nums = {3, 2, 1, 5, 6, 4};\n        int k = 2;\n        PriorityQueue<Integer> pq = new PriorityQueue<>();\n        for (int x : nums) {\n            pq.offer(x);\n            if (pq.size() > k) pq.poll();\n        }\n        System.out.println(\"2nd Largest: \" + pq.peek());",
        "expected_output": "2nd Largest: 5",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes min-heap size maintenance.. However, A min-heap of size k evicts smaller elements, leaving the k largest; its root `h[0]` is the kth largest.",
            "Core Concept: A min-heap of size k evicts smaller elements, leaving the k largest; its root `h[0]` is the kth largest. In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Keep heap size <= k with `heappop()`."
        ],
        "cause": [
            "Maintaining min-heap of size k yields O(n log k) complexity.",
            "Root element is the smallest among the k largest elements.",
            "Golden Rule: To find kth largest, maintain a min-heap of size k."
        ]
    },
    {
        "topic_id": "heaps_priority",
        "topic_name": "Heaps & Priority Queues",
        "level": 3,
        "title": "Sort a Nearly Sorted (K-Sorted) Array",
        "company": "Microsoft, Adobe",
        "description": "Sort [6, 5, 3, 2, 8, 10, 9] where each element is at most k = 3 positions away from sorted position.",
        "py_input": "import heapq\narr = [6, 5, 3, 2, 8, 10, 9]\nk = 3",
        "py_bug": "import heapq\narr = [6, 5, 3, 2, 8, 10, 9]\nk = 3\nh = arr[:k + 1]\nheapq.heapify(h)\nres = []\nfor i in range(k + 1, len(arr)):\n    res.append(heapq.heappop(h))\n    heapq.heappush(h, arr[i])\nwhile h:\n    res.append(heapq.heappop(h))\nprint('Sorted Array:', res)",
        "py_solution": "import heapq\narr = [6, 5, 3, 2, 8, 10, 9]\nk = 3\nh = arr[:k + 1]\nheapq.heapify(h)\nres = []\nfor i in range(k + 1, len(arr)):\n    res.append(heapq.heappop(h))\n    heapq.heappush(h, arr[i])\nwhile h:\n    res.append(heapq.heappop(h))\nprint('Sorted Array:', res)",
        "java_input": "        int[] arr = {6, 5, 3, 2, 8, 10, 9};\n        int k = 3;",
        "java_bug": "        int[] arr = {6, 5, 3, 2, 8, 10, 9};\n        int k = 3;\n        PriorityQueue<Integer> pq = new PriorityQueue<>();\n        for (int i = 0; i <= k; i++) pq.offer(arr[i]);\n        List<Integer> res = new ArrayList<>();\n        for (int i = k + 1; i < arr.length; i++) {\n            res.add(pq.poll());\n            pq.offer(arr[i]);\n        }\n        while (!pq.isEmpty()) res.add(pq.poll());\n        System.out.println(\"Sorted Array: \" + res);",
        "java_solution": "        int[] arr = {6, 5, 3, 2, 8, 10, 9};\n        int k = 3;\n        PriorityQueue<Integer> pq = new PriorityQueue<>();\n        for (int i = 0; i <= k; i++) pq.offer(arr[i]);\n        List<Integer> res = new ArrayList<>();\n        for (int i = k + 1; i < arr.length; i++) {\n            res.add(pq.poll());\n            pq.offer(arr[i]);\n        }\n        while (!pq.isEmpty()) res.add(pq.poll());\n        System.out.println(\"Sorted Array: \" + res);",
        "expected_output": "Sorted Array: [2, 3, 5, 6, 8, 9, 10]",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes sliding window min-heap of size k + 1.. However, Minimum element must be within the next k positions.",
            "Core Concept: Minimum element must be within the next k positions. In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Keep k + 1 elements in heap, extracting minimum and pushing next."
        ],
        "cause": [
            "K-sorted array solves sorting in O(n log k) instead of O(n log n).",
            "Sliding heap extracts sorted elements in linearithmic time.",
            "Golden Rule: In k-sorted arrays, maintain a heap of size k+1."
        ]
    },
    {
        "topic_id": "heaps_priority",
        "topic_name": "Heaps & Priority Queues",
        "level": 4,
        "title": "Connect Sticks with Minimum Cost",
        "company": "Amazon, Apple",
        "description": "Combine sticks [2, 4, 3] into one stick. Cost of connecting two sticks x and y is x + y. Find minimum total cost.",
        "py_input": "import heapq\nsticks = [2, 4, 3]",
        "py_bug": "import heapq\nsticks = [2, 4, 3]\nheapq.heapify(sticks)\ntotal = 0\nwhile len(sticks) > 1:\n    s1 = heapq.heappop(sticks)\n    s2 = heapq.heappop(sticks)\n    cost = s1 + s2\n    total += cost\n    heapq.heappush(sticks, cost)\nprint('Minimum Cost:', total)",
        "py_solution": "import heapq\nsticks = [2, 4, 3]\nheapq.heapify(sticks)\ntotal = 0\nwhile len(sticks) > 1:\n    s1 = heapq.heappop(sticks)\n    s2 = heapq.heappop(sticks)\n    cost = s1 + s2\n    total += cost\n    heapq.heappush(sticks, cost)\nprint('Minimum Cost:', total)",
        "java_input": "        int[] sticks = {2, 4, 3};",
        "java_bug": "        int[] sticks = {2, 4, 3};\n        PriorityQueue<Integer> pq = new PriorityQueue<>();\n        for (int s : sticks) pq.offer(s);\n        int total = 0;\n        while (pq.size() > 1) {\n            int cost = pq.poll() + pq.poll();\n            total += cost;\n            pq.offer(cost);\n        }\n        System.out.println(\"Minimum Cost: \" + total);",
        "java_solution": "        int[] sticks = {2, 4, 3};\n        PriorityQueue<Integer> pq = new PriorityQueue<>();\n        for (int s : sticks) pq.offer(s);\n        int total = 0;\n        while (pq.size() > 1) {\n            int cost = pq.poll() + pq.poll();\n            total += cost;\n            pq.offer(cost);\n        }\n        System.out.println(\"Minimum Cost: \" + total);",
        "expected_output": "Minimum Cost: 14",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes huffman-coding greedy strategy.. However, Always merge the two smallest sticks available to minimize compounding costs.",
            "Core Concept: Always merge the two smallest sticks available to minimize compounding costs. In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Pop two smallest, add their sum to total and push back into heap."
        ],
        "cause": [
            "Greedy choice property: merging smallest elements minimizes repeated additions.",
            "Equal to Huffman optimal merge tree.",
            "Golden Rule: Repeatedly combine two minimal elements using a min-heap."
        ]
    },
    {
        "topic_id": "heaps_priority",
        "topic_name": "Heaps & Priority Queues",
        "level": 5,
        "title": "Top K Frequent Elements",
        "company": "Amazon, Meta",
        "description": "Find the k = 2 most frequent numbers in [1, 1, 1, 2, 2, 3].",
        "py_input": "import heapq\nfrom collections import Counter\nnums = [1, 1, 1, 2, 2, 3]\nk = 2",
        "py_bug": "import heapq\nfrom collections import Counter\nnums = [1, 1, 1, 2, 2, 3]\nk = 2\ncounts = Counter(nums)\nh = []\nfor num, freq in counts.items():\n    heapq.heappush(h, (freq, num))\n    if len(h) > k: heapq.heappop(h)\nres = sorted([x[1] for x in h])\nprint('Top 2 Frequent:', res)",
        "py_solution": "import heapq\nfrom collections import Counter\nnums = [1, 1, 1, 2, 2, 3]\nk = 2\ncounts = Counter(nums)\nh = []\nfor num, freq in counts.items():\n    heapq.heappush(h, (freq, num))\n    if len(h) > k: heapq.heappop(h)\nres = sorted([x[1] for x in h])\nprint('Top 2 Frequent:', res)",
        "java_input": "        int[] nums = {1, 1, 1, 2, 2, 3};\n        int k = 2;",
        "java_bug": "        int[] nums = {1, 1, 2, 2, 1, 3};\n        int k = 2;\n        Map<Integer, Integer> counts = new HashMap<>();\n        for (int x : nums) counts.put(x, counts.getOrDefault(x, 0) + 1);\n        PriorityQueue<Integer> pq = new PriorityQueue<>(Comparator.comparingInt(counts::get));\n        for (int n : counts.keySet()) {\n            pq.offer(n);\n            if (pq.size() > k) pq.poll();\n        }\n        List<Integer> res = new ArrayList<>(pq);\n        Collections.sort(res);\n        System.out.println(\"Top 2 Frequent: \" + res);",
        "java_solution": "        int[] nums = {1, 1, 1, 2, 2, 3};\n        int k = 2;\n        Map<Integer, Integer> counts = new HashMap<>();\n        for (int x : nums) counts.put(x, counts.getOrDefault(x, 0) + 1);\n        PriorityQueue<Integer> pq = new PriorityQueue<>(Comparator.comparingInt(counts::get));\n        for (int n : counts.keySet()) {\n            pq.offer(n);\n            if (pq.size() > k) pq.poll();\n        }\n        List<Integer> res = new ArrayList<>(pq);\n        Collections.sort(res);\n        System.out.println(\"Top 2 Frequent: \" + res);",
        "expected_output": "Top 2 Frequent: [1, 2]",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes heap ordering by frequency.. However, Push pairs of `(frequency, number)` into min-heap of size k.",
            "Core Concept: Push pairs of `(frequency, number)` into min-heap of size k. In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Discard lowest frequencies when heap size exceeds k."
        ],
        "cause": [
            "Frequency map paired with bounded min-heap.",
            "Solves top-K in O(n log k).",
            "Golden Rule: Store `(frequency, item)` in min-heap to keep the k highest frequencies."
        ]
    },
    {
        "topic_id": "heaps_priority",
        "topic_name": "Heaps & Priority Queues",
        "level": 6,
        "title": "Find Median from Data Stream",
        "company": "Google, Microsoft",
        "description": "Calculate median of stream [5, 15, 1, 3] using two heaps (max-heap for lower half, min-heap for upper half).",
        "py_input": "import heapq\nnums = [5, 15, 1, 3]",
        "py_bug": "import heapq\nnums = [5, 15, 1, 3]\nsmall, large = [], []\nfor x in nums:\n    heapq.heappush(small, -x)\n    heapq.heappush(large, -heapq.heappop(small))\n    if len(large) > len(small):\n        heapq.heappush(small, -heapq.heappop(large))\nif len(small) > len(large): med = float(-small[0])\nelse: med = (-small[0] + large[0]) / 2.0\nprint('Stream Median:', med)",
        "py_solution": "import heapq\nnums = [5, 15, 1, 3]\nsmall, large = [], []\nfor x in nums:\n    heapq.heappush(small, -x)\n    heapq.heappush(large, -heapq.heappop(small))\n    if len(large) > len(small):\n        heapq.heappush(small, -heapq.heappop(large))\nif len(small) > len(large): med = float(-small[0])\nelse: med = (-small[0] + large[0]) / 2.0\nprint('Stream Median:', med)",
        "java_input": "        int[] nums = {5, 15, 1, 3};",
        "java_bug": "        int[] nums = {5, 15, 1, 3};\n        PriorityQueue<Integer> small = new PriorityQueue<>(Collections.reverseOrder());\n        PriorityQueue<Integer> large = new PriorityQueue<>();\n        for (int x : nums) {\n            small.offer(x);\n            large.offer(small.poll());\n            if (large.size() > small.size()) small.offer(large.poll());\n        }\n        double med = small.size() > large.size() ? small.peek() : (small.peek() + large.peek()) / 2.0;\n        System.out.println(\"Stream Median: \" + med);",
        "java_solution": "        int[] nums = {5, 15, 1, 3};\n        PriorityQueue<Integer> small = new PriorityQueue<>(Collections.reverseOrder());\n        PriorityQueue<Integer> large = new PriorityQueue<>();\n        for (int x : nums) {\n            small.offer(x);\n            large.offer(small.poll());\n            if (large.size() > small.size()) small.offer(large.poll());\n        }\n        double med = small.size() > large.size() ? small.peek() : (small.peek() + large.peek()) / 2.0;\n        System.out.println(\"Stream Median: \" + med);",
        "expected_output": "Stream Median: 4.0",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes balancing two heaps.. However, Max-heap stores smaller half, min-heap stores larger half. Sizes differ by at most 1.",
            "Core Concept: Max-heap stores smaller half, min-heap stores larger half. Sizes differ by at most 1. In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Median is either top of larger heap or average of both tops."
        ],
        "cause": [
            "Dual-heap streaming median maintenance.",
            "Maintains balanced halves in O(log n) per insertion.",
            "Golden Rule: Balance max-heap and min-heap to access stream median in O(1)."
        ]
    },
    {
        "topic_id": "heaps_priority",
        "topic_name": "Heaps & Priority Queues",
        "level": 7,
        "title": "Reorganize String (No Adjacent Same)",
        "company": "Google, Uber",
        "description": "Rearrange string 'aab' so that no two adjacent characters are identical.",
        "py_input": "import heapq\nfrom collections import Counter\ns = 'aab'",
        "py_bug": "import heapq\nfrom collections import Counter\ns = 'aab'\ncounts = Counter(s)\nh = [(-cnt, char) for char, cnt in counts.items()]\nheapq.heapify(h)\nprev_cnt, prev_char = 0, ''\nres = []\nwhile h:\n    cnt, char = heapq.heappop(h)\n    res.append(char)\n    if prev_cnt < 0:\n        heapq.heappush(h, (prev_cnt, prev_char))\n    prev_cnt, prev_char = cnt + 1, char\nprint('Reorganized:', ''.join(res))",
        "py_solution": "import heapq\nfrom collections import Counter\ns = 'aab'\ncounts = Counter(s)\nh = [(-cnt, char) for char, cnt in counts.items()]\nheapq.heapify(h)\nprev_cnt, prev_char = 0, ''\nres = []\nwhile h:\n    cnt, char = heapq.heappop(h)\n    res.append(char)\n    if prev_cnt < 0:\n        heapq.heappush(h, (prev_cnt, prev_char))\n    prev_cnt, prev_char = cnt + 1, char\nprint('Reorganized:', ''.join(res))",
        "java_input": "        String s = \"aab\";",
        "java_bug": "        String s = \"aab\";\n        Map<Character, Integer> counts = new HashMap<>();\n        for (char c : s.toCharArray()) counts.put(c, counts.getOrDefault(c, 0) + 1);\n        PriorityQueue<Character> pq = new PriorityQueue<>((a, b) -> counts.get(b) - counts.get(a));\n        pq.addAll(counts.keySet());\n        StringBuilder sb = new StringBuilder();\n        char prevChar = ' ';\n        int prevCount = 0;\n        while (!pq.isEmpty()) {\n            char c = pq.poll();\n            sb.append(c);\n            int left = counts.get(c) - 1;\n            counts.put(c, left);\n            if (prevCount > 0) pq.offer(prevChar);\n            prevChar = c; prevCount = left;\n        }\n        System.out.println(\"Reorganized: \" + sb.toString());",
        "java_solution": "        String s = \"aab\";\n        Map<Character, Integer> counts = new HashMap<>();\n        for (char c : s.toCharArray()) counts.put(c, counts.getOrDefault(c, 0) + 1);\n        PriorityQueue<Character> pq = new PriorityQueue<>((a, b) -> counts.get(b) - counts.get(a));\n        pq.addAll(counts.keySet());\n        StringBuilder sb = new StringBuilder();\n        char prevChar = ' ';\n        int prevCount = 0;\n        while (!pq.isEmpty()) {\n            char c = pq.poll();\n            sb.append(c);\n            int left = counts.get(c) - 1;\n            counts.put(c, left);\n            if (prevCount > 0) pq.offer(prevChar);\n            prevChar = c; prevCount = left;\n        }\n        System.out.println(\"Reorganized: \" + sb.toString());",
        "expected_output": "Reorganized: aba",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes character cooling holding queue.. However, Greedily pick the most frequent character, but hold it from returning to heap until another char is placed.",
            "Core Concept: Greedily pick the most frequent character, but hold it from returning to heap until another char is placed. In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Reinsert previous character only after placing the next distinct character."
        ],
        "cause": [
            "Max-heap greedy placement with 1-turn cooldown.",
            "Ensures highest frequency character is alternated.",
            "Golden Rule: Delay reinserting the current character into the heap until the subsequent character is placed."
        ]
    },
    {
        "topic_id": "heaps_priority",
        "topic_name": "Heaps & Priority Queues",
        "level": 8,
        "title": "Meeting Rooms II (Min Conference Rooms)",
        "company": "Google, Amazon",
        "description": "Given intervals [[0, 30], [5, 10], [15, 20]], find minimum conference rooms required.",
        "py_input": "import heapq\nintervals = [[0, 30], [5, 10], [15, 20]]",
        "py_bug": "import heapq\nintervals = [[0, 30], [5, 10], [15, 20]]\nintervals.sort(key=lambda x: x[0])\nh = []\nfor start, end in intervals:\n    if h and h[0] <= start: heapq.heappop(h)\n    heapq.heappush(h, end)\nprint('Required Rooms:', len(h))",
        "py_solution": "import heapq\nintervals = [[0, 30], [5, 10], [15, 20]]\nintervals.sort(key=lambda x: x[0])\nh = []\nfor start, end in intervals:\n    if h and h[0] <= start: heapq.heappop(h)\n    heapq.heappush(h, end)\nprint('Required Rooms:', len(h))",
        "java_input": "        int[][] intervals = {{0, 30}, {5, 10}, {15, 20}};",
        "java_bug": "        int[][] intervals = {{0, 30}, {5, 10}, {15, 20}};\n        Arrays.sort(intervals, Comparator.comparingInt(a -> a[0]));\n        PriorityQueue<Integer> pq = new PriorityQueue<>();\n        for (int[] iv : intervals) {\n            if (!pq.isEmpty() && pq.peek() <= iv[0]) pq.poll();\n            pq.offer(iv[1]);\n        }\n        System.out.println(\"Required Rooms: \" + pq.size());",
        "java_solution": "        int[][] intervals = {{0, 30}, {5, 10}, {15, 20}};\n        Arrays.sort(intervals, Comparator.comparingInt(a -> a[0]));\n        PriorityQueue<Integer> pq = new PriorityQueue<>();\n        for (int[] iv : intervals) {\n            if (!pq.isEmpty() && pq.peek() <= iv[0]) pq.poll();\n            pq.offer(iv[1]);\n        }\n        System.out.println(\"Required Rooms: \" + pq.size());",
        "expected_output": "Required Rooms: 2",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes tracking room release times in a min-heap.. However, Min-heap stores meeting end times. If earliest ending room finishes before new meeting starts, reuse room.",
            "Core Concept: Min-heap stores meeting end times. If earliest ending room finishes before new meeting starts, reuse room. In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Pop from heap when `h[0] <= start` and push new `end` time."
        ],
        "cause": [
            "Min-heap tracks active room allocations.",
            "Peak heap size represents the maximum simultaneous overlapping intervals.",
            "Golden Rule: Sort by start times, track earliest finishing room in min-heap."
        ]
    },
    {
        "topic_id": "heaps_priority",
        "topic_name": "Heaps & Priority Queues",
        "level": 9,
        "title": "Task Scheduler with Cooldown",
        "company": "Meta, Amazon",
        "description": "Given tasks ['A', 'A', 'A', 'B', 'B', 'B'] and cooldown n = 2, find least CPU time intervals.",
        "py_input": "from collections import Counter\ntasks = ['A', 'A', 'A', 'B', 'B', 'B']\nn = 2",
        "py_bug": "from collections import Counter\ntasks = ['A', 'A', 'A', 'B', 'B', 'B']\nn = 2\ncounts = list(Counter(tasks).values())\nmax_cnt = max(counts)\nmax_freq = counts.count(max_cnt)\nans = max(len(tasks), (max_cnt - 1) * (n + 1) + max_freq)\nprint('Total CPU Intervals:', ans)",
        "py_solution": "from collections import Counter\ntasks = ['A', 'A', 'A', 'B', 'B', 'B']\nn = 2\ncounts = list(Counter(tasks).values())\nmax_cnt = max(counts)\nmax_freq = counts.count(max_cnt)\nans = max(len(tasks), (max_cnt - 1) * (n + 1) + max_freq)\nprint('Total CPU Intervals:', ans)",
        "java_input": "        char[] tasks = {'A', 'A', 'A', 'B', 'B', 'B'};\n        int n = 2;",
        "java_bug": "        char[] tasks = {'A', 'A', 'A', 'B', 'B', 'B'};\n        int n = 2;\n        int[] map = new int[26];\n        for (char c : tasks) map[c - 'A']++;\n        Arrays.sort(map);\n        int maxVal = map[25] - 1, idle = maxVal * n;\n        for (int i = 24; i >= 0 && map[i] > 0; i--) idle -= Math.min(map[i], maxVal);\n        int ans = idle > 0 ? idle + tasks.length : tasks.length;\n        System.out.println(\"Total CPU Intervals: \" + ans);",
        "java_solution": "        char[] tasks = {'A', 'A', 'A', 'B', 'B', 'B'};\n        int n = 2;\n        int[] map = new int[26];\n        for (char c : tasks) map[c - 'A']++;\n        Arrays.sort(map);\n        int maxVal = map[25] - 1, idle = maxVal * n;\n        for (int i = 24; i >= 0 && map[i] > 0; i--) idle -= Math.min(map[i], maxVal);\n        int ans = idle > 0 ? idle + tasks.length : tasks.length;\n        System.out.println(\"Total CPU Intervals: \" + ans);",
        "expected_output": "Total CPU Intervals: 8",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes slotting the most frequent task.. However, Bottleneck is determined by the task with highest frequency.",
            "Core Concept: Bottleneck is determined by the task with highest frequency. In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Calculate `(max_freq - 1) * (n + 1) + count_of_max_freq`."
        ],
        "cause": [
            "Greedy task frame scheduling.",
            "Formula accounts for idle gaps between mandatory cooldown cycles.",
            "Golden Rule: Frame size is bounded by `(max_count - 1) * (n + 1) + max_tied_tasks`."
        ]
    },
    {
        "topic_id": "heaps_priority",
        "topic_name": "Heaps & Priority Queues",
        "level": 10,
        "title": "Merge K Sorted Lists",
        "company": "Google, Amazon",
        "description": "Merge 3 sorted lists [[1, 4, 5], [1, 3, 4], [2, 6]] into a single sorted list using a min-heap.",
        "py_input": "import heapq\nlists = [[1, 4, 5], [1, 3, 4], [2, 6]]",
        "py_bug": "import heapq\nlists = [[1, 4, 5], [1, 3, 4], [2, 6]]\nh = []\nfor i, l in enumerate(lists):\n    if l: heapq.heappush(h, (l[0], i, 0))\nres = []\nwhile h:\n    val, list_idx, elem_idx = heapq.heappop(h)\n    res.append(val)\n    if elem_idx + 1 < len(lists[list_idx]):\n        heapq.heappush(h, (lists[list_idx][elem_idx + 1], list_idx, elem_idx + 1))\nprint('Merged List:', res)",
        "py_solution": "import heapq\nlists = [[1, 4, 5], [1, 3, 4], [2, 6]]\nh = []\nfor i, l in enumerate(lists):\n    if l: heapq.heappush(h, (l[0], i, 0))\nres = []\nwhile h:\n    val, list_idx, elem_idx = heapq.heappop(h)\n    res.append(val)\n    if elem_idx + 1 < len(lists[list_idx]):\n        heapq.heappush(h, (lists[list_idx][elem_idx + 1], list_idx, elem_idx + 1))\nprint('Merged List:', res)",
        "java_input": "        int[][] lists = {{1, 4, 5}, {1, 3, 4}, {2, 6}};",
        "java_bug": "        int[][] lists = {{1, 4, 5}, {1, 3, 4}, {2, 6}};\n        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));\n        for (int i = 0; i < lists.length; i++) {\n            if (lists[i].length > 0) pq.offer(new int[]{lists[i][0], i, 0});\n        }\n        List<Integer> res = new ArrayList<>();\n        while (!pq.isEmpty()) {\n            int[] top = pq.poll();\n            res.add(top[0]);\n            int listIdx = top[1], elemIdx = top[2];\n            if (elemIdx + 1 < lists[listIdx].length) {\n                pq.offer(new int[]{lists[listIdx][elemIdx + 1], listIdx, elemIdx + 1});\n            }\n        }\n        System.out.println(\"Merged List: \" + res);",
        "java_solution": "        int[][] lists = {{1, 4, 5}, {1, 3, 4}, {2, 6}};\n        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));\n        for (int i = 0; i < lists.length; i++) {\n            if (lists[i].length > 0) pq.offer(new int[]{lists[i][0], i, 0});\n        }\n        List<Integer> res = new ArrayList<>();\n        while (!pq.isEmpty()) {\n            int[] top = pq.poll();\n            res.add(top[0]);\n            int listIdx = top[1], elemIdx = top[2];\n            if (elemIdx + 1 < lists[listIdx].length) {\n                pq.offer(new int[]{lists[listIdx][elemIdx + 1], listIdx, elemIdx + 1});\n            }\n        }\n        System.out.println(\"Merged List: \" + res);",
        "expected_output": "Merged List: [1, 1, 2, 3, 4, 4, 5, 6]",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes multi-way merge with min-heap.. However, Keep first element of each list in min-heap. When one is extracted, advance in that specific list.",
            "Core Concept: Keep first element of each list in min-heap. When one is extracted, advance in that specific list. In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Store `(val, list_index, element_index)` in heap."
        ],
        "cause": [
            "K-way merge algorithm.",
            "Merges N total items across K lists in O(N log K).",
            "Golden Rule: Push head of each list to min-heap and advance on pop."
        ]
    },

    # =========================================================================
    # TOPIC 10: DYNAMIC PROGRAMMING (10 Placement Questions)
    # =========================================================================
    {
        "topic_id": "dynamic_programming",
        "topic_name": "Dynamic Programming",
        "level": 1,
        "title": "Climbing Stairs (Count Ways)",
        "company": "Google, Adobe",
        "description": "Count distinct ways to climb n = 4 stairs taking either 1 or 2 steps each time.",
        "py_input": "n = 4",
        "py_bug": "n = 4\ndp = [0] * (n + 1)\ndp[1], dp[2] = 1, 2\nfor i in range(3, n + 2): # Bug: out of bounds range!\n    dp[i] = dp[i-1] + dp[i-2]\nprint('Distinct Ways:', dp[n])",
        "py_solution": "n = 4\ndp = [0] * (n + 1)\ndp[1], dp[2] = 1, 2\nfor i in range(3, n + 1):\n    dp[i] = dp[i-1] + dp[i-2]\nprint('Distinct Ways:', dp[n])",
        "java_input": "        int n = 4;",
        "java_bug": "        int n = 4;\n        int[] dp = new int[n + 1];\n        dp[1] = 1; dp[2] = 2;\n        for (int i = 3; i <= n + 1; i++) dp[i] = dp[i-1] + dp[i-2]; // ArrayIndexOutOfBoundsException\n        System.out.println(\"Distinct Ways: \" + dp[n]);",
        "java_solution": "        int n = 4;\n        int[] dp = new int[n + 1];\n        dp[1] = 1; dp[2] = 2;\n        for (int i = 3; i <= n; i++) dp[i] = dp[i-1] + dp[i-2];\n        System.out.println(\"Distinct Ways: \" + dp[n]);",
        "expected_output": "Distinct Ways: 5",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes loop upper bound in DP table.. However, `dp` table is allocated of size `n + 1`. Iterating to `n + 2` tries to access index `n + 1` which is out of bounds.",
            "Core Concept: `dp` table is allocated of size `n + 1`. Iterating to `n + 2` tries to access index `n + 1` which is out of bounds. In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Loop strictly up to `n + 1` (inclusive of n)."
        ],
        "cause": [
            "IndexError accessing dp[5] in a 5-element array.",
            "DP table indices are 0 to n.",
            "Golden Rule: Loop bounds for size N+1 table must stop at index N."
        ]
    },
    {
        "topic_id": "dynamic_programming",
        "topic_name": "Dynamic Programming",
        "level": 2,
        "title": "House Robber (Max Non-Adjacent)",
        "company": "Amazon, Microsoft",
        "description": "Find maximum money that can be robbed from houses [2, 7, 9, 3, 1] without alerting police (cannot rob adjacent houses).",
        "py_input": "nums = [2, 7, 9, 3, 1]",
        "py_bug": "nums = [2, 7, 9, 3, 1]\nrob1, rob2 = 0, 0\nfor n in nums:\n    temp = max(n + rob1, rob2)\n    rob1 = rob2\n    rob2 = temp\nprint('Max Loot:', rob2)",
        "py_solution": "nums = [2, 7, 9, 3, 1]\nrob1, rob2 = 0, 0\nfor n in nums:\n    temp = max(n + rob1, rob2)\n    rob1 = rob2\n    rob2 = temp\nprint('Max Loot:', rob2)",
        "java_input": "        int[] nums = {2, 7, 9, 3, 1};",
        "java_bug": "        int[] nums = {2, 7, 9, 3, 1};\n        int rob1 = 0, rob2 = 0;\n        for (int n : nums) {\n            int temp = Math.max(n + rob1, rob2);\n            rob1 = rob2;\n            rob2 = temp;\n        }\n        System.out.println(\"Max Loot: \" + rob2);",
        "java_solution": "        int[] nums = {2, 7, 9, 3, 1};\n        int rob1 = 0, rob2 = 0;\n        for (int n : nums) {\n            int temp = Math.max(n + rob1, rob2);\n            rob1 = rob2;\n            rob2 = temp;\n        }\n        System.out.println(\"Max Loot: \" + rob2);",
        "expected_output": "Max Loot: 12",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes choice at each house: rob current house + loot from 2 houses ago, or skip.. However, State transition is `max(rob1 + n, rob2)`.",
            "Core Concept: State transition is `max(rob1 + n, rob2)`. In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Shift rob1 and rob2 forward on each step."
        ],
        "cause": [
            "Dynamic programming state reduction.",
            "Computes non-adjacent optimal sum in O(n) time and O(1) space.",
            "Golden Rule: Optimal choice at i is `max(loot[i] + prev_prev, prev)`."
        ]
    },
    {
        "topic_id": "dynamic_programming",
        "topic_name": "Dynamic Programming",
        "level": 3,
        "title": "Coin Change (Fewest Coins)",
        "company": "Google, Amazon",
        "description": "Find the minimum number of coins needed from [1, 2, 5] to make total amount 11.",
        "py_input": "coins = [1, 2, 5]\namount = 11",
        "py_bug": "coins = [1, 2, 5]\namount = 11\ndp = [float('inf')] * (amount + 1)\ndp[0] = 0\nfor a in range(1, amount + 1):\n    for c in coins:\n        if a - c >= 0:\n            dp[a] = min(dp[a], 1 + dp[a - c])\nprint('Min Coins:', dp[amount])",
        "py_solution": "coins = [1, 2, 5]\namount = 11\ndp = [float('inf')] * (amount + 1)\ndp[0] = 0\nfor a in range(1, amount + 1):\n    for c in coins:\n        if a - c >= 0:\n            dp[a] = min(dp[a], 1 + dp[a - c])\nprint('Min Coins:', dp[amount])",
        "java_input": "        int[] coins = {1, 2, 5};\n        int amount = 11;",
        "java_bug": "        int[] coins = {1, 2, 5};\n        int amount = 11;\n        int[] dp = new int[amount + 1];\n        Arrays.fill(dp, amount + 1);\n        dp[0] = 0;\n        for (int a = 1; a <= amount; a++) {\n            for (int c : coins) {\n                if (a - c >= 0) dp[a] = Math.min(dp[a], 1 + dp[a - c]);\n            }\n        }\n        System.out.println(\"Min Coins: \" + dp[amount]);",
        "java_solution": "        int[] coins = {1, 2, 5};\n        int amount = 11;\n        int[] dp = new int[amount + 1];\n        Arrays.fill(dp, amount + 1);\n        dp[0] = 0;\n        for (int a = 1; a <= amount; a++) {\n            for (int c : coins) {\n                if (a - c >= 0) dp[a] = Math.min(dp[a], 1 + dp[a - c]);\n            }\n        }\n        System.out.println(\"Min Coins: \" + dp[amount]);",
        "expected_output": "Min Coins: 3",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes base case and initialization.. However, `dp[0] = 0` (0 coins for amount 0). For each amount, test all coins.",
            "Core Concept: `dp[0] = 0` (0 coins for amount 0). For each amount, test all coins. In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Initialize table with infinity and fill iteratively."
        ],
        "cause": [
            "Bottom-up dynamic programming tabulation.",
            "Finds global optimal coin count avoiding greedy pitfalls.",
            "Golden Rule: Coin change requires `dp[a] = min(dp[a], 1 + dp[a - coin])`."
        ]
    },
    {
        "topic_id": "dynamic_programming",
        "topic_name": "Dynamic Programming",
        "level": 4,
        "title": "Longest Increasing Subsequence (LIS)",
        "company": "Microsoft, Google",
        "description": "Find length of longest strictly increasing subsequence in [10, 9, 2, 5, 3, 7, 101, 18].",
        "py_input": "nums = [10, 9, 2, 5, 3, 7, 101, 18]",
        "py_bug": "nums = [10, 9, 2, 5, 3, 7, 101, 18]\nif not nums: print('LIS Length:', 0)\nelse:\n    dp = [1] * len(nums)\n    for i in range(len(nums)):\n        for j in range(i):\n            if nums[j] < nums[i]:\n                dp[i] = max(dp[i], dp[j] + 1)\n    print('LIS Length:', max(dp))",
        "py_solution": "nums = [10, 9, 2, 5, 3, 7, 101, 18]\nif not nums: print('LIS Length:', 0)\nelse:\n    dp = [1] * len(nums)\n    for i in range(len(nums)):\n        for j in range(i):\n            if nums[j] < nums[i]:\n                dp[i] = max(dp[i], dp[j] + 1)\n    print('LIS Length:', max(dp))",
        "java_input": "        int[] nums = {10, 9, 2, 5, 3, 7, 101, 18};",
        "java_bug": "        int[] nums = {10, 9, 2, 5, 3, 7, 101, 18};\n        int[] dp = new int[nums.length];\n        Arrays.fill(dp, 1);\n        int max = 1;\n        for (int i = 0; i < nums.length; i++) {\n            for (int j = 0; j < i; j++) {\n                if (nums[j] < nums[i]) dp[i] = Math.max(dp[i], dp[j] + 1);\n            }\n            max = Math.max(max, dp[i]);\n        }\n        System.out.println(\"LIS Length: \" + max);",
        "java_solution": "        int[] nums = {10, 9, 2, 5, 3, 7, 101, 18};\n        int[] dp = new int[nums.length];\n        Arrays.fill(dp, 1);\n        int max = 1;\n        for (int i = 0; i < nums.length; i++) {\n            for (int j = 0; j < i; j++) {\n                if (nums[j] < nums[i]) dp[i] = Math.max(dp[i], dp[j] + 1);\n            }\n            max = Math.max(max, dp[i]);\n        }\n        System.out.println(\"LIS Length: \" + max);",
        "expected_output": "LIS Length: 4",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes subproblem definition `dp[i]`.. However, `dp[i]` is length of LIS ending at index i. Compare with all previous `j < i` where `nums[j] < nums[i]`.",
            "Core Concept: `dp[i]` is length of LIS ending at index i. Compare with all previous `j < i` where `nums[j] < nums[i]`. In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Compute `dp[i] = max(dp[i], dp[j] + 1)`."
        ],
        "cause": [
            "Classic O(n^2) DP pattern.",
            "Subsequence length compounded from all valid prefixes.",
            "Golden Rule: For each pair (j, i), if nums[j] < nums[i], update `dp[i] = max(dp[i], 1 + dp[j])`."
        ]
    },
    {
        "topic_id": "dynamic_programming",
        "topic_name": "Dynamic Programming",
        "level": 5,
        "title": "0/1 Knapsack Problem",
        "company": "Amazon, Flipkart",
        "description": "Find maximum value that fits in capacity = 5 given weights [1, 2, 3] and values [10, 15, 40].",
        "py_input": "weights = [1, 2, 3]\nvalues = [10, 15, 40]\ncapacity = 5",
        "py_bug": "weights = [1, 2, 3]\nvalues = [10, 15, 40]\ncapacity = 5\nn = len(weights)\ndp = [0] * (capacity + 1)\nfor i in range(n):\n    for w in range(weights[i], capacity + 1): # Bug: forward loop allows taking same item multiple times (unbounded knapsack)!\n        dp[w] = max(dp[w], values[i] + dp[w - weights[i]])\nprint('Max Knapsack Value:', dp[capacity])",
        "py_solution": "weights = [1, 2, 3]\nvalues = [10, 15, 40]\ncapacity = 5\nn = len(weights)\ndp = [0] * (capacity + 1)\nfor i in range(n):\n    for w in range(capacity, weights[i] - 1, -1):\n        dp[w] = max(dp[w], values[i] + dp[w - weights[i]])\nprint('Max Knapsack Value:', dp[capacity])",
        "java_input": "        int[] weights = {1, 2, 3};\n        int[] values = {10, 15, 40};\n        int capacity = 5;",
        "java_bug": "        int[] weights = {1, 2, 3};\n        int[] values = {10, 15, 40};\n        int capacity = 5;\n        int[] dp = new int[capacity + 1];\n        for (int i = 0; i < weights.length; i++) {\n            for (int w = weights[i]; w <= capacity; w++) {\n                dp[w] = Math.max(dp[w], values[i] + dp[w - weights[i]]);\n            }\n        }\n        System.out.println(\"Max Knapsack Value: \" + dp[capacity]);",
        "java_solution": "        int[] weights = {1, 2, 3};\n        int[] values = {10, 15, 40};\n        int capacity = 5;\n        int[] dp = new int[capacity + 1];\n        for (int i = 0; i < weights.length; i++) {\n            for (int w = capacity; w >= weights[i]; w--) {\n                dp[w] = Math.max(dp[w], values[i] + dp[w - weights[i]]);\n            }\n        }\n        System.out.println(\"Max Knapsack Value: \" + dp[capacity]);",
        "expected_output": "Max Knapsack Value: 55",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes the direction of the inner capacity loop.. However, A forward loop re-uses the same item multiple times. In 0/1 knapsack each item is used at most once.",
            "Core Concept: A forward loop re-uses the same item multiple times. In 0/1 knapsack each item is used at most once. In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Loop capacity backwards from `capacity` down to `weight`."
        ],
        "cause": [
            "Forward iteration causes unbounded reuse of current item in 1D DP table.",
            "0/1 Knapsack requires values from the previous item tier.",
            "Golden Rule: In 1D table 0/1 knapsack, iterate capacity in reverse."
        ]
    },
    {
        "topic_id": "dynamic_programming",
        "topic_name": "Dynamic Programming",
        "level": 6,
        "title": "Partition Equal Subset Sum",
        "company": "Adobe, Goldman Sachs",
        "description": "Determine if array [1, 5, 11, 5] can be partitioned into two subsets with equal sum.",
        "py_input": "nums = [1, 5, 11, 5]",
        "py_bug": "nums = [1, 5, 11, 5]\ntotal = sum(nums)\nif total % 2 != 0: can_part = False\nelse:\n    target = total // 2\n    dp = [False] * (target + 1)\n    dp[0] = True\n    for n in nums:\n        for j in range(target, n - 1, -1):\n            dp[j] = dp[j] or dp[j - n]\n    can_part = dp[target]\nprint('Can Partition:', can_part)",
        "py_solution": "nums = [1, 5, 11, 5]\ntotal = sum(nums)\nif total % 2 != 0: can_part = False\nelse:\n    target = total // 2\n    dp = [False] * (target + 1)\n    dp[0] = True\n    for n in nums:\n        for j in range(target, n - 1, -1):\n            dp[j] = dp[j] or dp[j - n]\n    can_part = dp[target]\nprint('Can Partition:', can_part)",
        "java_input": "        int[] nums = {1, 5, 11, 5};",
        "java_bug": "        int[] nums = {1, 5, 11, 5};\n        int total = 0;\n        for (int x : nums) total += x;\n        boolean can = false;\n        if (total % 2 == 0) {\n            int target = total / 2;\n            boolean[] dp = new boolean[target + 1];\n            dp[0] = true;\n            for (int n : nums) {\n                for (int j = target; j >= n; j--) dp[j] = dp[j] || dp[j - n];\n            }\n            can = dp[target];\n        }\n        System.out.println(\"Can Partition: \" + can);",
        "java_solution": "        int[] nums = {1, 5, 11, 5};\n        int total = 0;\n        for (int x : nums) total += x;\n        boolean can = false;\n        if (total % 2 == 0) {\n            int target = total / 2;\n            boolean[] dp = new boolean[target + 1];\n            dp[0] = true;\n            for (int n : nums) {\n                for (int j = target; j >= n; j--) dp[j] = dp[j] || dp[j - n];\n            }\n            can = dp[target];\n        }\n        System.out.println(\"Can Partition: \" + can);",
        "expected_output": "Can Partition: True",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes target sum.. However, If total sum is odd, it's impossible to divide into two equal integers. Otherwise, find subset summing to `total / 2`.",
            "Core Concept: If total sum is odd, it's impossible to divide into two equal integers. Otherwise, find subset summing to `total / 2`. In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Check `total % 2 == 0` and solve 0/1 subset sum."
        ],
        "cause": [
            "Reduction to subset sum target = sum / 2.",
            "Odd sums can never be partitioned into integers.",
            "Golden Rule: Equal partition is equivalent to subset sum of `total / 2`."
        ]
    },
    {
        "topic_id": "dynamic_programming",
        "topic_name": "Dynamic Programming",
        "level": 7,
        "title": "Unique Paths in a Grid",
        "company": "Amazon, Google",
        "description": "Find number of unique paths from top-left (0,0) to bottom-right in a 3 x 7 grid moving only right or down.",
        "py_input": "m = 3\nn = 7",
        "py_bug": "m = 3\nn = 7\n# Space-optimized row DP\nrow = [1] * n\nfor i in range(m - 1):\n    new_row = [1] * n\n    for j in range(n - 2, -1, -1):\n        new_row[j] = new_row[j + 1] + row[j]\n    row = new_row\nprint('Unique Paths:', row[0])",
        "py_solution": "m = 3\nn = 7\nrow = [1] * n\nfor i in range(m - 1):\n    new_row = [1] * n\n    for j in range(n - 2, -1, -1):\n        new_row[j] = new_row[j + 1] + row[j]\n    row = new_row\nprint('Unique Paths:', row[0])",
        "java_input": "        int m = 3, n = 7;",
        "java_bug": "        int m = 3, n = 7;\n        int[] row = new int[n];\n        Arrays.fill(row, 1);\n        for (int i = 0; i < m - 1; i++) {\n            int[] next = new int[n];\n            Arrays.fill(next, 1);\n            for (int j = n - 2; j >= 0; j--) next[j] = next[j + 1] + row[j];\n            row = next;\n        }\n        System.out.println(\"Unique Paths: \" + row[0]);",
        "java_solution": "        int m = 3, n = 7;\n        int[] row = new int[n];\n        Arrays.fill(row, 1);\n        for (int i = 0; i < m - 1; i++) {\n            int[] next = new int[n];\n            Arrays.fill(next, 1);\n            for (int j = n - 2; j >= 0; j--) next[j] = next[j + 1] + row[j];\n            row = next;\n        }\n        System.out.println(\"Unique Paths: \" + row[0]);",
        "expected_output": "Unique Paths: 28",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes recurrence: `dp[r][c] = dp[r+1][c] + dp[r][c+1]`.. However, Every cell's path count is the sum of paths from the cell below it and the cell to its right.",
            "Core Concept: Every cell's path count is the sum of paths from the cell below it and the cell to its right. In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Tabulate row by row."
        ],
        "cause": [
            "2D grid path tabulation.",
            "Solves combinations C(m+n-2, m-1) in O(m*n).",
            "Golden Rule: Number of paths to cell is sum of paths from its incoming adjacent cells."
        ]
    },
    {
        "topic_id": "dynamic_programming",
        "topic_name": "Dynamic Programming",
        "level": 8,
        "title": "Longest Common Subsequence (LCS)",
        "company": "Amazon, Microsoft",
        "description": "Find length of longest common subsequence between 'abcde' and 'ace'.",
        "py_input": "text1 = 'abcde'\ntext2 = 'ace'",
        "py_bug": "text1 = 'abcde'\ntext2 = 'ace'\nm, n = len(text1), len(text2)\ndp = [[0] * (n + 1) for _ in range(m + 1)]\nfor i in range(1, m + 1):\n    for j in range(1, n + 1):\n        if text1[i - 1] == text2[j - 1]:\n            dp[i][j] = 1 + dp[i - 1][j - 1]\n        else:\n            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])\nprint('LCS Length:', dp[m][n])",
        "py_solution": "text1 = 'abcde'\ntext2 = 'ace'\nm, n = len(text1), len(text2)\ndp = [[0] * (n + 1) for _ in range(m + 1)]\nfor i in range(1, m + 1):\n    for j in range(1, n + 1):\n        if text1[i - 1] == text2[j - 1]:\n            dp[i][j] = 1 + dp[i - 1][j - 1]\n        else:\n            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])\nprint('LCS Length:', dp[m][n])",
        "java_input": "        String text1 = \"abcde\", text2 = \"ace\";",
        "java_bug": "        String text1 = \"abcde\", text2 = \"ace\";\n        int m = text1.length(), n = text2.length();\n        int[][] dp = new int[m + 1][n + 1];\n        for (int i = 1; i <= m; i++) {\n            for (int j = 1; j <= n; j++) {\n                if (text1.charAt(i - 1) == text2.charAt(j - 1)) dp[i][j] = 1 + dp[i - 1][j - 1];\n                else dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);\n            }\n        }\n        System.out.println(\"LCS Length: \" + dp[m][n]);",
        "java_solution": "        String text1 = \"abcde\", text2 = \"ace\";\n        int m = text1.length(), n = text2.length();\n        int[][] dp = new int[m + 1][n + 1];\n        for (int i = 1; i <= m; i++) {\n            for (int j = 1; j <= n; j++) {\n                if (text1.charAt(i - 1) == text2.charAt(j - 1)) dp[i][j] = 1 + dp[i - 1][j - 1];\n                else dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);\n            }\n        }\n        System.out.println(\"LCS Length: \" + dp[m][n]);",
        "expected_output": "LCS Length: 3",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes character match condition.. However, If chars match, add 1 to diagonal `dp[i-1][j-1]`. If not, take max of left and top cells.",
            "Core Concept: If chars match, add 1 to diagonal `dp[i-1][j-1]`. If not, take max of left and top cells. In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Build (m+1) x (n+1) table."
        ],
        "cause": [
            "2D String DP comparison grid.",
            "Diagonal transition on match, cross transition on mismatch.",
            "Golden Rule: When characters match, extend diagonal; otherwise take max of adjacent."
        ]
    },
    {
        "topic_id": "dynamic_programming",
        "topic_name": "Dynamic Programming",
        "level": 9,
        "title": "Word Break Problem",
        "company": "Google, Meta",
        "description": "Determine if 'leetcode' can be segmented into words from dictionary ['leet', 'code'].",
        "py_input": "s = 'leetcode'\nwordDict = ['leet', 'code']",
        "py_bug": "s = 'leetcode'\nwordDict = ['leet', 'code']\ndp = [False] * (len(s) + 1)\ndp[0] = True\nfor i in range(1, len(s) + 1):\n    for w in wordDict:\n        if i >= len(w) and dp[i - len(w)] and s[i - len(w):i] == w:\n            dp[i] = True\n            break\nprint('Can Segment:', dp[len(s)])",
        "py_solution": "s = 'leetcode'\nwordDict = ['leet', 'code']\ndp = [False] * (len(s) + 1)\ndp[0] = True\nfor i in range(1, len(s) + 1):\n    for w in wordDict:\n        if i >= len(w) and dp[i - len(w)] and s[i - len(w):i] == w:\n            dp[i] = True\n            break\nprint('Can Segment:', dp[len(s)])",
        "java_input": "        String s = \"leetcode\";\n        List<String> wordDict = Arrays.asList(\"leet\", \"code\");",
        "java_bug": "        String s = \"leetcode\";\n        List<String> wordDict = Arrays.asList(\"leet\", \"code\");\n        boolean[] dp = new boolean[s.length() + 1];\n        dp[0] = true;\n        for (int i = 1; i <= s.length(); i++) {\n            for (String w : wordDict) {\n                if (i >= w.length() && dp[i - w.length()] && s.substring(i - w.length(), i).equals(w)) {\n                    dp[i] = true;\n                    break;\n                }\n            }\n        }\n        System.out.println(\"Can Segment: \" + dp[s.length()]);",
        "java_solution": "        String s = \"leetcode\";\n        List<String> wordDict = Arrays.asList(\"leet\", \"code\");\n        boolean[] dp = new boolean[s.length() + 1];\n        dp[0] = true;\n        for (int i = 1; i <= s.length(); i++) {\n            for (String w : wordDict) {\n                if (i >= w.length() && dp[i - w.length()] && s.substring(i - w.length(), i).equals(w)) {\n                    dp[i] = true;\n                    break;\n                }\n            }\n        }\n        System.out.println(\"Can Segment: \" + dp[s.length()]);",
        "expected_output": "Can Segment: True",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes string segmentation subproblem.. However, `dp[i]` is True if prefix `s[:i]` can be segmented using dictionary words.",
            "Core Concept: `dp[i]` is True if prefix `s[:i]` can be segmented using dictionary words. In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Check if preceding prefix `dp[i - len(w)]` was True and matching word."
        ],
        "cause": [
            "1D prefix DP memoization.",
            "Verifies valid vocabulary decomposition in O(n * words).",
            "Golden Rule: A prefix is segmentable if a valid sub-prefix exists and remaining substring is in the dictionary."
        ]
    },
    {
        "topic_id": "dynamic_programming",
        "topic_name": "Dynamic Programming",
        "level": 10,
        "title": "Edit Distance (Levenshtein Distance)",
        "company": "Google, Microsoft",
        "description": "Find minimum number of operations (insert, delete, replace) to convert word1 = 'horse' to word2 = 'ros'.",
        "py_input": "word1 = 'horse'\nword2 = 'ros'",
        "py_bug": "word1 = 'horse'\nword2 = 'ros'\nm, n = len(word1), len(word2)\ndp = [[0] * (n + 1) for _ in range(m + 1)]\nfor i in range(m + 1): dp[i][0] = i\nfor j in range(n + 1): dp[0][j] = j\nfor i in range(1, m + 1):\n    for j in range(1, n + 1):\n        if word1[i - 1] == word2[j - 1]:\n            dp[i][j] = dp[i - 1][j - 1]\n        else:\n            dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])\nprint('Min Edit Distance:', dp[m][n])",
        "py_solution": "word1 = 'horse'\nword2 = 'ros'\nm, n = len(word1), len(word2)\ndp = [[0] * (n + 1) for _ in range(m + 1)]\nfor i in range(m + 1): dp[i][0] = i\nfor j in range(n + 1): dp[0][j] = j\nfor i in range(1, m + 1):\n    for j in range(1, n + 1):\n        if word1[i - 1] == word2[j - 1]:\n            dp[i][j] = dp[i - 1][j - 1]\n        else:\n            dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])\nprint('Min Edit Distance:', dp[m][n])",
        "java_input": "        String word1 = \"horse\", word2 = \"ros\";",
        "java_bug": "        String word1 = \"horse\", word2 = \"ros\";\n        int m = word1.length(), n = word2.length();\n        int[][] dp = new int[m + 1][n + 1];\n        for (int i = 0; i <= m; i++) dp[i][0] = i;\n        for (int j = 0; j <= n; j++) dp[0][j] = j;\n        for (int i = 1; i <= m; i++) {\n            for (int j = 1; j <= n; j++) {\n                if (word1.charAt(i - 1) == word2.charAt(j - 1)) dp[i][j] = dp[i - 1][j - 1];\n                else dp[i][j] = 1 + Math.min(dp[i - 1][j - 1], Math.min(dp[i - 1][j], dp[i][j - 1]));\n            }\n        }\n        System.out.println(\"Min Edit Distance: \" + dp[m][n]);",
        "java_solution": "        String word1 = \"horse\", word2 = \"ros\";\n        int m = word1.length(), n = word2.length();\n        int[][] dp = new int[m + 1][n + 1];\n        for (int i = 0; i <= m; i++) dp[i][0] = i;\n        for (int j = 0; j <= n; j++) dp[0][j] = j;\n        for (int i = 1; i <= m; i++) {\n            for (int j = 1; j <= n; j++) {\n                if (word1.charAt(i - 1) == word2.charAt(j - 1)) dp[i][j] = dp[i - 1][j - 1];\n                else dp[i][j] = 1 + Math.min(dp[i - 1][j - 1], Math.min(dp[i - 1][j], dp[i][j - 1]));\n            }\n        }\n        System.out.println(\"Min Edit Distance: \" + dp[m][n]);",
        "expected_output": "Min Edit Distance: 3",
        "hints": [
            "Logic Flaw: When solving this task, the logic assumes base operations: delete, insert, replace.. However, `dp[i-1][j]` is delete, `dp[i][j-1]` is insert, and `dp[i-1][j-1]` is replace.",
            "Core Concept: `dp[i-1][j]` is delete, `dp[i][j-1]` is insert, and `dp[i-1][j-1]` is replace. In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence.",
            "What to Change in Logic: Choose `1 + min(delete, insert, replace)` on mismatch."
        ],
        "cause": [
            "Levenshtein distance matrix recurrence.",
            "Finds minimal edits in O(m * n) polynomial time.",
            "Golden Rule: On character mismatch, cost is 1 + min of insert, delete, and replace."
        ]
    }
]

print("Loaded Part 5 (Trees, Heaps, DP):", len(PART_5))
