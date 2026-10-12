# Python script to generate all 10 topics x 10 problems = 100 questions per language (200 problem setups)
import json

TOPICS_DEF = [
    {
        "id": "arrays_lists",
        "name": "Arrays & Lists",
        "icon": "fa-layer-group",
        "tagline": "Array reversal, two-sum, palindrome arrays, sliding windows & Kadane's",
        "description": "Master the most common array practice interview questions asked by Core Algorithm, Core Algorithm, Core Algorithm, and Core Algorithm.",
        "difficulty": "Level 1 to 10",
        "color": "#06b6d4"
    },
    {
        "id": "strings_hashmaps",
        "name": "Strings & Text Processing",
        "icon": "fa-font",
        "tagline": "Palindromes, anagrams, word reversals, and frequency maps",
        "description": "Solve essential string practice questions from palindrome checks to anagram grouping and non-repeating characters.",
        "difficulty": "Level 1 to 10",
        "color": "#f59e0b"
    },
    {
        "id": "loops_indexing",
        "name": "Searching & Loops",
        "icon": "fa-magnifying-glass",
        "tagline": "Linear search, binary search, peak elements & rotated arrays",
        "description": "Master loop algorithms and logarithmic binary search interview problems.",
        "difficulty": "Level 1 to 10",
        "color": "#3b82f6"
    },
    {
        "id": "basics_types",
        "name": "Math & Number Problems",
        "icon": "fa-calculator",
        "tagline": "Reverse integer, Armstrong number, GCD, and prime checks",
        "description": "Essential campus practice math and numerical aptitude programming questions.",
        "difficulty": "Level 1 to 10",
        "color": "#10b981"
    },
    {
        "id": "conditionals",
        "name": "Conditionals & Logic",
        "icon": "fa-code-branch",
        "tagline": "Leap years, Roman numerals, version compares & decision flow",
        "description": "Solve branching logic and multi-condition edge case problems asked in initial technical rounds.",
        "difficulty": "Level 1 to 10",
        "color": "#8b5cf6"
    },
    {
        "id": "stacks_queues",
        "name": "Stacks & Queues",
        "icon": "fa-bars-staggered",
        "tagline": "Valid parentheses, Min Stack, next greater element & queues",
        "description": "Key data structure questions for stack-based evaluation and FIFO/LIFO algorithms.",
        "difficulty": "Level 1 to 10",
        "color": "#ec4899"
    },
    {
        "id": "recursion_backtracking",
        "name": "Recursion & Backtracking",
        "icon": "fa-arrows-split-up-and-left",
        "tagline": "Fibonacci, subset generation, permutations & N-Queens",
        "description": "Master recursion call stacks, base cases, and exhaustive decision trees.",
        "difficulty": "Level 1 to 10",
        "color": "#6366f1"
    },
    {
        "id": "trees_bst",
        "name": "Binary Trees & BSTs",
        "icon": "fa-network-wired",
        "tagline": "Traversals, depth, BST validation, LCA & mirror trees",
        "description": "Solve binary tree traversals, tree pointers, and BST search properties.",
        "difficulty": "Level 1 to 10",
        "color": "#14b8a6"
    },
    {
        "id": "heaps_priority",
        "name": "Heaps & Priority Queues",
        "icon": "fa-arrow-up-wide-short",
        "tagline": "Kth largest element, top-K frequent & meeting room conflicts",
        "description": "High-frequency interview questions for priority sorting and interval scheduling.",
        "difficulty": "Level 1 to 10",
        "color": "#eab308"
    },
    {
        "id": "dynamic_programming",
        "name": "Dynamic Programming",
        "icon": "fa-diagram-project",
        "tagline": "Climbing stairs, coin change, house robber & 0/1 knapsack",
        "description": "The ultimate practice interview round: state memoization, tabulations, and optimal substructure.",
        "difficulty": "Level 1 to 10",
        "color": "#f43f5e"
    }
]

print("Ready to construct 100 questions.")
