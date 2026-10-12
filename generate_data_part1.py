# Part 1 of Questions Catalog (Topic 1: Arrays & Lists)
# Educational clues that teach the logic behind mistakes and exactly what to change!

PART_1 = [
    # =========================================================================
    # TOPIC 1: ARRAYS & LISTS (10 practice Questions)
    # =========================================================================
    {
        "topic_id": "arrays_lists",
        "topic_name": "Arrays & Lists",
        "level": 1,
        "title": "Reverse an Array",
        "company": "Core Algorithm, Core Algorithm Core Algorithm",
        "description": "Given an array of integers, reverse the elements and print the result.",
        "py_input": "arr = [1, 2, 3, 4, 5]",
        "py_bug": "arr = [1, 2, 3, 4, 5]\nrev = []\nfor i in range(len(arr), 0, -1):\n    rev.append(arr[i])\nprint('Reversed:', rev)",
        "py_solution": "arr = [1, 2, 3, 4, 5]\nrev = []\nfor i in range(len(arr) - 1, -1, -1):\n    rev.append(arr[i])\nprint('Reversed:', rev)",
        "java_input": "        int[] arr = {1, 2, 3, 4, 5};",
        "java_bug": "        int[] arr = {1, 2, 3, 4, 5};\n        System.out.print(\"Reversed: [\");\n        for(int i = arr.length; i >= 0; i--) {\n            System.out.print(arr[i] + (i > 0 ? \", \" : \"\"));\n        }\n        System.out.println(\"]\");",
        "java_solution": "        int[] arr = {1, 2, 3, 4, 5};\n        System.out.print(\"Reversed: [\");\n        for(int i = arr.length - 1; i >= 0; i--) {\n            System.out.print(arr[i] + (i > 0 ? \", \" : \"\"));\n        }\n        System.out.println(\"]\");",
        "expected_output": "Reversed: [5, 4, 3, 2, 1]",
        "hints": [
            "Logic Flaw: When reversing, it is natural to think 'a list with 5 items starts counting back from 5'. But in programming, positions start at 0! A 5-element list only has slots 0, 1, 2, 3, and 4. Trying to read slot 5 immediately crashes because that position does not exist.",
            "Core Concept: In zero-indexed languages, the last valid element of any array of length N is always located at index N - 1. When stepping backwards, your starting boundary must be N - 1, and you must continue down until index 0 is processed.",
            "What to Change in Logic: In Python, change your range to range(len(arr) - 1, -1, -1). In Java, initialize your reverse loop with 'for(int i = arr.length - 1; i >= 0; i--)'. This starts at the true last element (index 4) and stops safely after reading the first element (index 0)."
        ],
        "cause": [
            "Attempted to read arr[length] which is beyond the array boundary.",
            "Indices start at 0, so the last valid index is always length - 1.",
            "Golden Rule: The last item of any list of size N is at index N - 1."
        ],
        "visual_type": "array_bounds",
        "visual_data": {
            "visual_type": "array_bounds",
            "array_name": "arr",
            "elements": [1, 2, 3, 4, 5],
            "length": 5,
            "valid_min": 0,
            "valid_max": 4,
            "attempted_index": 5,
            "is_out_of_bounds": True,
            "note": "Array length is 5. Indices are 0 to 4."
        }
    },
    {
        "topic_id": "arrays_lists",
        "topic_name": "Arrays & Lists",
        "level": 2,
        "title": "Check if Array is Palindrome",
        "company": "Core Algorithm, Core Algorithm Elite",
        "description": "Check whether an array reads the same forward and backward.",
        "py_input": "arr = [1, 2, 3, 2, 1]",
        "py_bug": "arr = [1, 2, 3, 2, 1]\nis_pal = True\nfor i in range(len(arr)):\n    if arr[i] != arr[len(arr) - i]:\n        is_pal = False\n        break\nprint('Is Palindrome:', is_pal)",
        "py_solution": "arr = [1, 2, 3, 2, 1]\nis_pal = True\nfor i in range(len(arr)):\n    if arr[i] != arr[len(arr) - 1 - i]:\n        is_pal = False\n        break\nprint('Is Palindrome:', is_pal)",
        "java_input": "        int[] arr = {1, 2, 3, 2, 1};",
        "java_bug": "        int[] arr = {1, 2, 3, 2, 1};\n        boolean isPal = true;\n        for(int i = 0; i < arr.length; i++) {\n            if (arr[i] != arr[arr.length - i]) { isPal = false; break; }\n        }\n        System.out.println(\"Is Palindrome: \" + isPal);",
        "java_solution": "        int[] arr = {1, 2, 3, 2, 1};\n        boolean isPal = true;\n        for(int i = 0; i < arr.length; i++) {\n            if (arr[i] != arr[arr.length - 1 - i]) { isPal = false; break; }\n        }\n        System.out.println(\"Is Palindrome: \" + isPal);",
        "expected_output": "Is Palindrome: True",
        "hints": [
            "Logic Flaw: You are trying to compare element i with the mirror element from the back using 'len(arr) - i'. But on the very first turn when i = 0, 'len(arr) - 0' equals 5! Slot 5 is off the edge of the array.",
            "Core Concept: In a zero-indexed array, the mirror counterpart of index i from the end is always at position (N - 1) - i. When i = 0, its mirror is N - 1. When i = 1, its mirror is N - 2.",
            "What to Change in Logic: Subtract an additional 1 in your mirror index calculation: change arr[len(arr) - i] to arr[len(arr) - 1 - i] in Python, or arr[arr.length - 1 - i] in Java. This accurately matches opposite symmetrical pairs."
        ],
        "cause": [
            "Formula len(arr) - i causes IndexError at i=0.",
            "Zero-indexed arrays require subtracting 1 before subtracting i.",
            "Golden Rule: Mirror of index i is always at (length - 1 - i)."
        ],
        "visual_type": "array_bounds",
        "visual_data": {
            "visual_type": "array_bounds",
            "array_name": "arr",
            "elements": [1, 2, 3, 2, 1],
            "length": 5,
            "valid_min": 0,
            "valid_max": 4,
            "attempted_index": 5,
            "is_out_of_bounds": True,
            "note": "len(arr) - 0 is 5, which is out of bounds."
        }
    },
    {
        "topic_id": "arrays_lists",
        "topic_name": "Arrays & Lists",
        "level": 3,
        "title": "Find Maximum and Minimum Element",
        "company": "Core Algorithm, Core Algorithm",
        "description": "Find both the smallest and largest number in an unsorted array.",
        "py_input": "nums = [38, 12, 95, 4, 67]",
        "py_bug": "nums = [38, 12, 95, 4, 67]\nmin_val = nums[0]\nmax_val = nums[0]\nfor i in range(1, len(nums) + 1):\n    if nums[i] < min_val: min_val = nums[i]\n    if nums[i] > max_val: max_val = nums[i]\nprint(f'Min: {min_val}, Max: {max_val}')",
        "py_solution": "nums = [38, 12, 95, 4, 67]\nmin_val = nums[0]\nmax_val = nums[0]\nfor i in range(1, len(nums)):\n    if nums[i] < min_val: min_val = nums[i]\n    if nums[i] > max_val: max_val = nums[i]\nprint(f'Min: {min_val}, Max: {max_val}')",
        "java_input": "        int[] nums = {38, 12, 95, 4, 67};",
        "java_bug": "        int[] nums = {38, 12, 95, 4, 67};\n        int min = nums[0], max = nums[0];\n        for(int i = 1; i <= nums.length; i++) {\n            if (nums[i] < min) min = nums[i];\n            if (nums[i] > max) max = nums[i];\n        }\n        System.out.println(\"Min: \" + min + \", Max: \" + max);",
        "java_solution": "        int[] nums = {38, 12, 95, 4, 67};\n        int min = nums[0], max = nums[0];\n        for(int i = 1; i < nums.length; i++) {\n            if (nums[i] < min) min = nums[i];\n            if (nums[i] > max) max = nums[i];\n        }\n        System.out.println(\"Min: \" + min + \", Max: \" + max);",
        "expected_output": "Min: 4, Max: 95",
        "hints": [
            "Logic Flaw: The loop upper bound is set to len(nums) + 1 or i <= nums.length. While we want to inspect all remaining numbers, adding +1 forces the loop to attempt reading index 5 in an array of size 5.",
            "Core Concept: The range boundary in Python range(start, stop) excludes the stop value. If stop is len + 1, the loop will visit index len. But in an array of size N, valid indices only go up to N - 1.",
            "What to Change in Logic: Change range(1, len(nums) + 1) to range(1, len(nums)) in Python, or i < nums.length in Java. This inspects indices 1, 2, 3, and 4 without overshooting."
        ],
        "cause": [
            "The loop tried to inspect index 5 in a 5-element array.",
            "Loop bounds must be strictly less than length.",
            "Golden Rule: Loop limits should use < length, never <= length."
        ],
        "visual_type": "array_bounds",
        "visual_data": {
            "visual_type": "array_bounds",
            "array_name": "nums",
            "elements": [38, 12, 95, 4, 67],
            "length": 5,
            "valid_min": 0,
            "valid_max": 4,
            "attempted_index": 5,
            "is_out_of_bounds": True,
            "note": "Stopping at len(nums) + 1 leads to index 5."
        }
    },
    {
        "topic_id": "arrays_lists",
        "topic_name": "Arrays & Lists",
        "level": 4,
        "title": "Two Sum (Pair with Target Sum)",
        "company": "Core Algorithm, Core Algorithm, Core Algorithm",
        "description": "Find two numbers in a sorted array that sum up to target.",
        "py_input": "nums = [2, 7, 11, 15]\ntarget = 9",
        "py_bug": "nums = [2, 7, 11, 15]\ntarget = 9\nleft, right = 0, len(nums) - 1\nwhile left < right:\n    s = nums[left] + nums[right]\n    if s == target: break\n    elif s < target: right -= 1\n    else: right -= 1\nprint('Pair:', [nums[left], nums[right]])",
        "py_solution": "nums = [2, 7, 11, 15]\ntarget = 9\nleft, right = 0, len(nums) - 1\nwhile left < right:\n    s = nums[left] + nums[right]\n    if s == target: break\n    elif s < target: left += 1\n    else: right -= 1\nprint('Pair:', [nums[left], nums[right]])",
        "java_input": "        int[] nums = {2, 7, 11, 15};\n        int target = 9;",
        "java_bug": "        int[] nums = {2, 7, 11, 15};\n        int target = 9, left = 0, right = nums.length - 1;\n        while(left < right) {\n            int s = nums[left] + nums[right];\n            if (s == target) break;\n            else if (s < target) right--;\n            else right--;\n        }\n        System.out.println(\"Pair: [\" + nums[left] + \", \" + nums[right] + \"]\");",
        "java_solution": "        int[] nums = {2, 7, 11, 15};\n        int target = 9, left = 0, right = nums.length - 1;\n        while(left < right) {\n            int s = nums[left] + nums[right];\n            if (s == target) break;\n            else if (s < target) left++;\n            else right--;\n        }\n        System.out.println(\"Pair: [\" + nums[left] + \", \" + nums[right] + \"]\");",
        "expected_output": "Pair: [2, 7]",
        "hints": [
            "Logic Flaw: When the current sum (nums[left] + nums[right]) is smaller than the target, decrementing right makes the sum even smaller! You need to make the sum larger to reach the target.",
            "Core Concept: In a sorted array, numbers grow larger as you move from left to right. Moving the left pointer forward (left += 1) increases the sum, while moving the right pointer backward (right -= 1) decreases the sum.",
            "What to Change in Logic: Inside the elif s < target branch, change 'right -= 1' to 'left += 1'. Keep 'right -= 1' only for when s > target."
        ],
        "cause": [
            "When current sum is too small, moving right pointer makes it even smaller.",
            "Left pointer controls smaller values; incrementing it increases total sum.",
            "Golden Rule: In two-pointer sorted search, sum < target -> left++, sum > target -> right--."
        ]
    },
    {
        "topic_id": "arrays_lists",
        "topic_name": "Arrays & Lists",
        "level": 5,
        "title": "Remove Duplicates from Sorted Array",
        "company": "Core Algorithm, Core Algorithm",
        "description": "Remove duplicates in-place so unique elements appear at the beginning. Print unique count.",
        "py_input": "nums = [1, 1, 2, 2, 3]",
        "py_bug": "nums = [1, 1, 2, 2, 3]\nwrite = 1\nfor i in range(1, len(nums) + 1):\n    if nums[i] != nums[i - 1]:\n        nums[write] = nums[i]\n        write += 1\nprint('Unique count:', write)",
        "py_solution": "nums = [1, 1, 2, 2, 3]\nwrite = 1\nfor i in range(1, len(nums)):\n    if nums[i] != nums[i - 1]:\n        nums[write] = nums[i]\n        write += 1\nprint('Unique count:', write)",
        "java_input": "        int[] nums = {1, 1, 2, 2, 3};",
        "java_bug": "        int[] nums = {1, 1, 2, 2, 3};\n        int write = 1;\n        for(int i = 1; i <= nums.length; i++) {\n            if (nums[i] != nums[i-1]) nums[write++] = nums[i];\n        }\n        System.out.println(\"Unique count: \" + write);",
        "java_solution": "        int[] nums = {1, 1, 2, 2, 3};\n        int write = 1;\n        for(int i = 1; i < nums.length; i++) {\n            if (nums[i] != nums[i-1]) nums[write++] = nums[i];\n        }\n        System.out.println(\"Unique count: \" + write);",
        "expected_output": "Unique count: 3",
        "hints": [
            "Logic Flaw: You used range(1, len(nums) + 1), which attempts to read nums[len(nums)]. The read pointer walks past the array boundary on the last step.",
            "Core Concept: The in-place two-pointer technique uses a slow 'write' pointer that records distinct items and a fast 'i' pointer that reads every item. The read pointer must strictly stop before len(nums).",
            "What to Change in Logic: Change the loop bound to range(1, len(nums)) in Python, or i < nums.length in Java. Every time nums[i] differs from nums[i-1], overwrite nums[write] and advance write."
        ],
        "cause": [
            "Accessing nums[len] caused IndexError.",
            "Loop reached one step past the last element.",
            "Golden Rule: Array scanning loops should never touch length index."
        ]
    },
    {
        "topic_id": "arrays_lists",
        "topic_name": "Arrays & Lists",
        "level": 6,
        "title": "Move All Zeroes to End",
        "company": "Core Algorithm, Core Algorithm",
        "description": "Shift all zeroes to the end while maintaining the order of non-zero elements.",
        "py_input": "arr = [0, 1, 0, 3, 12]",
        "py_bug": "arr = [0, 1, 0, 3, 12]\ninsert_pos = 0\nfor x in arr:\n    if x != 0:\n        arr[insert_pos] = x\n        insert_pos += 1\nwhile insert_pos <= len(arr):\n    arr[insert_pos] = 0\n    insert_pos += 1\nprint('Moved Zeroes:', arr)",
        "py_solution": "arr = [0, 1, 0, 3, 12]\ninsert_pos = 0\nfor x in arr:\n    if x != 0:\n        arr[insert_pos] = x\n        insert_pos += 1\nwhile insert_pos < len(arr):\n    arr[insert_pos] = 0\n    insert_pos += 1\nprint('Moved Zeroes:', arr)",
        "java_input": "        int[] arr = {0, 1, 0, 3, 12};",
        "java_bug": "        int[] arr = {0, 1, 0, 3, 12};\n        int pos = 0;\n        for(int x : arr) if (x != 0) arr[pos++] = x;\n        while(pos <= arr.length) arr[pos++] = 0;\n        System.out.println(\"Moved Zeroes: \" + java.util.Arrays.toString(arr));",
        "java_solution": "        int[] arr = {0, 1, 0, 3, 12};\n        int pos = 0;\n        for(int x : arr) if (x != 0) arr[pos++] = x;\n        while(pos < arr.length) arr[pos++] = 0;\n        System.out.println(\"Moved Zeroes: \" + java.util.Arrays.toString(arr));",
        "expected_output": "Moved Zeroes: [1, 3, 12, 0, 0]",
        "hints": [
            "Logic Flaw: After copying non-zero elements forward, the while loop to fill remaining positions with zeroes uses '<= len(arr)'. When insert_pos reaches len(arr), writing to arr[insert_pos] causes an out-of-bounds crash.",
            "Core Concept: Filling the remainder of an array requires setting slots from insert_pos up to length - 1. Index len(arr) does not exist.",
            "What to Change in Logic: Change 'while insert_pos <= len(arr):' to 'while insert_pos < len(arr):' (strictly less than length). This safely fills positions up to index 4 without overshooting."
        ],
        "cause": [
            "Using <= len(arr) causes an out-of-bounds write on the final iteration.",
            "Valid indices stop at len - 1.",
            "Golden Rule: Always guard array index writes with < array.length."
        ]
    },
    {
        "topic_id": "arrays_lists",
        "topic_name": "Arrays & Lists",
        "level": 7,
        "title": "Rotate Array by K Places",
        "company": "Core Algorithm, Core Algorithm",
        "description": "Rotate an array to the right by k positions.",
        "py_input": "arr = [1, 2, 3, 4, 5]\nk = 2",
        "py_bug": "arr = [1, 2, 3, 4, 5]\nk = 2\nrotated = arr[k:] + arr[:k]\nprint('Rotated:', rotated)",
        "py_solution": "arr = [1, 2, 3, 4, 5]\nk = 2\nk = k % len(arr)\nrotated = arr[-k:] + arr[:-k]\nprint('Rotated:', rotated)",
        "java_input": "        int[] arr = {1, 2, 3, 4, 5};\n        int k = 2;",
        "java_bug": "        int[] arr = {1, 2, 3, 4, 5};\n        int k = 2 % arr.length;\n        int[] res = new int[arr.length];\n        for(int i = 0; i < arr.length; i++) {\n            res[(i + k) % arr.length] = arr[i];\n        }\n        System.out.println(\"Rotated: \" + java.util.Arrays.toString(res));",
        "java_solution": "        int[] arr = {1, 2, 3, 4, 5};\n        int k = 2 % arr.length;\n        int[] res = new int[arr.length];\n        for(int i = 0; i < arr.length; i++) {\n            res[(i + k) % arr.length] = arr[i];\n        }\n        System.out.println(\"Rotated: \" + java.util.Arrays.toString(res));",
        "expected_output": "Rotated: [4, 5, 1, 2, 3]",
        "hints": [
            "Logic Flaw: Slicing with arr[k:] + arr[:k] shifts elements to the LEFT (producing [3, 4, 5, 1, 2]), but the problem asks for a RIGHT rotation by k places.",
            "Core Concept: In a right rotation, the last k elements wrap around to become the new beginning of the array, and the remaining elements shift rightward.",
            "What to Change in Logic: Normalize k with 'k = k % len(arr)'. In Python, take the last k elements with 'arr[-k:]' and concatenate with 'arr[:-k]'. In Java, assign each element to its new circular index '(i + k) % arr.length'."
        ],
        "cause": [
            "Slicing arr[k:] rotated left instead of right.",
            "Right rotation brings the tail elements to the beginning.",
            "Golden Rule: In right rotation by k, tail elements arr[-k:] become the head."
        ]
    },
    {
        "topic_id": "arrays_lists",
        "topic_name": "Arrays & Lists",
        "level": 8,
        "title": "Best Time to Buy and Sell Stock",
        "company": "Core Algorithm Sachs, Core Algorithm",
        "description": "Maximize profit by picking one day to buy and a future day to sell.",
        "py_input": "prices = [7, 1, 5, 3, 6, 4]",
        "py_bug": "prices = [7, 1, 5, 3, 6, 4]\nmin_price = prices[0]\nmax_profit = 0\nfor i in range(1, len(prices) + 1):\n    if prices[i] < min_price: min_price = prices[i]\n    elif prices[i] - min_price > max_profit: max_profit = prices[i] - min_price\nprint('Max Profit:', max_profit)",
        "py_solution": "prices = [7, 1, 5, 3, 6, 4]\nmin_price = prices[0]\nmax_profit = 0\nfor i in range(1, len(prices)):\n    if prices[i] < min_price: min_price = prices[i]\n    elif prices[i] - min_price > max_profit: max_profit = prices[i] - min_price\nprint('Max Profit:', max_profit)",
        "java_input": "        int[] prices = {7, 1, 5, 3, 6, 4};",
        "java_bug": "        int[] prices = {7, 1, 5, 3, 6, 4};\n        int minP = prices[0], maxProfit = 0;\n        for(int i = 1; i <= prices.length; i++) {\n            if (prices[i] < minP) minP = prices[i];\n            else if (prices[i] - minP > maxProfit) maxProfit = prices[i] - minP;\n        }\n        System.out.println(\"Max Profit: \" + maxProfit);",
        "java_solution": "        int[] prices = {7, 1, 5, 3, 6, 4};\n        int minP = prices[0], maxProfit = 0;\n        for(int i = 1; i < prices.length; i++) {\n            if (prices[i] < minP) minP = prices[i];\n            else if (prices[i] - minP > maxProfit) maxProfit = prices[i] - minP;\n        }\n        System.out.println(\"Max Profit: \" + maxProfit);",
        "expected_output": "Max Profit: 5",
        "hints": [
            "Logic Flaw: The loop boundary len(prices) + 1 causes index i to reach index 6 on the last step. The prices array has 6 elements, which are indexed 0 through 5.",
            "Core Concept: The greedy one-pass algorithm tracks the minimum price seen so far and compares today's profit (price[i] - min_price) against the running maximum profit. The scan must strictly end at len - 1.",
            "What to Change in Logic: Change the range upper bound to 'len(prices)' (remove the '+ 1'). In Java use 'i < prices.length'. At each step update min_price = min(min_price, prices[i]) and max_profit = max(max_profit, prices[i] - min_price)."
        ],
        "cause": [
            "Index out of bounds at final day inspection.",
            "Prices list has length 6, so index 6 does not exist.",
            "Golden Rule: Loop bounds must never exceed list size."
        ]
    },
    {
        "topic_id": "arrays_lists",
        "topic_name": "Arrays & Lists",
        "level": 9,
        "title": "Maximum Subarray Sum (Kadane's Algorithm)",
        "company": "Walmart Global, Core Algorithm",
        "description": "Find the contiguous subarray with the largest sum.",
        "py_input": "nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]",
        "py_bug": "nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]\ncurr_sum = nums[0]\nmax_sum = nums[0]\nfor i in range(1, len(nums) + 1):\n    curr_sum = max(nums[i], curr_sum + nums[i])\n    max_sum = max(max_sum, curr_sum)\nprint('Max Subarray Sum:', max_sum)",
        "py_solution": "nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]\ncurr_sum = nums[0]\nmax_sum = nums[0]\nfor i in range(1, len(nums)):\n    curr_sum = max(nums[i], curr_sum + nums[i])\n    max_sum = max(max_sum, curr_sum)\nprint('Max Subarray Sum:', max_sum)",
        "java_input": "        int[] nums = {-2, 1, -3, 4, -1, 2, 1, -5, 4};",
        "java_bug": "        int[] nums = {-2, 1, -3, 4, -1, 2, 1, -5, 4};\n        int curr = nums[0], max = nums[0];\n        for(int i = 1; i <= nums.length; i++) {\n            curr = Math.max(nums[i], curr + nums[i]);\n            max = Math.max(max, curr);\n        }\n        System.out.println(\"Max Subarray Sum: \" + max);",
        "java_solution": "        int[] nums = {-2, 1, -3, 4, -1, 2, 1, -5, 4};\n        int curr = nums[0], max = nums[0];\n        for(int i = 1; i < nums.length; i++) {\n            curr = Math.max(nums[i], curr + nums[i]);\n            max = Math.max(max, curr);\n        }\n        System.out.println(\"Max Subarray Sum: \" + max);",
        "expected_output": "Max Subarray Sum: 6",
        "hints": [
            "Logic Flaw: Kadane's algorithm starts with nums[0], but your loop upper bound is set to len(nums) + 1. It visits index 9 in an array of size 9, causing an IndexError.",
            "Core Concept: At every element, Kadane asks: 'Should I add this number to my existing subarray sum, or should I throw away the past and start a fresh subarray right here?' The choice is max(nums[i], curr_sum + nums[i]).",
            "What to Change in Logic: Change the loop bound from 'range(1, len(nums) + 1)' to 'range(1, len(nums))' in Python, or 'i < nums.length' in Java. This processes all remaining 8 elements safely."
        ],
        "cause": [
            "Attempted to read nums[len(nums)] which exceeds array length.",
            "Valid indices run from 0 to len - 1.",
            "Golden Rule: Loop boundary for list of length N is 0 to N-1."
        ]
    },
    {
        "topic_id": "arrays_lists",
        "topic_name": "Arrays & Lists",
        "level": 10,
        "title": "Trapping Rain Water",
        "company": "Core Algorithm, Core Algorithm, Core Algorithm",
        "description": "Calculate how much water can be trapped between elevation bars after raining.",
        "py_input": "height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]",
        "py_bug": "height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]\nwater = 0\nfor i in range(len(height)):\n    water += height[i]\nprint('Trapped Water:', water)",
        "py_solution": "height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]\nleft, right = 0, len(height) - 1\nleft_max, right_max = 0, 0\nwater = 0\nwhile left < right:\n    if height[left] < height[right]:\n        if height[left] >= left_max: left_max = height[left]\n        else: water += left_max - height[left]\n        left += 1\n    else:\n        if height[right] >= right_max: right_max = height[right]\n        else: water += right_max - height[right]\n        right -= 1\nprint('Trapped Water:', water)",
        "java_input": "        int[] height = {0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1};",
        "java_bug": "        int[] height = {0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1};\n        int water = 0;\n        for(int h : height) water += h;\n        System.out.println(\"Trapped Water: \" + water);",
        "java_solution": "        int[] height = {0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1};\n        int left = 0, right = height.length - 1, leftMax = 0, rightMax = 0, water = 0;\n        while (left < right) {\n            if (height[left] < height[right]) {\n                if (height[left] >= leftMax) leftMax = height[left];\n                else water += leftMax - height[left];\n                left++;\n            } else {\n                if (height[right] >= rightMax) rightMax = height[right];\n                else water += rightMax - height[right];\n                right--;\n            }\n        }\n        System.out.println(\"Trapped Water: \" + water);",
        "expected_output": "Trapped Water: 6",
        "hints": [
            "Logic Flaw: Simply summing the heights calculates the solid volume of the brick bars, NOT the water trapped in the gaps between bars!",
            "Core Concept: Water trapped above any bar at position i is determined by the minimum of the highest wall to its left and the highest wall to its right: water[i] = min(max_left, max_right) - height[i].",
            "What to Change in Logic: Use the two-pointer approach from both ends (left = 0, right = len - 1). Track left_max and right_max. Move the pointer that has the smaller height inward, adding 'current_max - height[current]' to the total water."
        ],
        "cause": [
            "Simply summing heights measures bar volume, not trapped water between bars.",
            "Water requires boundaries on both left and right to be contained.",
            "Golden Rule: Trapped water at position i is min(left_max, right_max) - height[i]."
        ]
    }
]

print("Loaded Updated Topic 1 Arrays:", len(PART_1))
