import urllib.request
import json

code = """import java.util.Arrays;

public class ReverseArray {
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};

        int left = 0;
        int right = arr.length - 1;

        while (left < right) {
            int temp = arr[left];
            arr[left] = arr[right];
            arr[right] = temp;

            left++;
            right--;
        }

        System.out.println("Reversed: " + Arrays.toString(arr));
    }
}
"""

payload = {
    "code": code,
    "language": "python", # User had Python selected!
    "question_id": "py-arra-01"
}

req = urllib.request.Request(
    "http://localhost:8000/api/execute",
    data=json.dumps(payload).encode("utf-8"),
    headers={"Content-Type": "application/json"}
)

res = json.loads(urllib.request.urlopen(req).read())
print("Success:", res["success"])
print("All Tests Passed:", res["all_tests_passed"])
print("Output:", res["output"].strip())
print("Parsed Error:", res.get("parsed_error"))
