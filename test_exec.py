import urllib.request
import json

code = """import java.util.*;
public class Main {
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        System.out.print("Reversed: [");
        for(int i = arr.length - 1; i >= 0; i--) {
            System.out.print(arr[i] + (i > 0 ? ", " : ""));
        }
        System.out.println("]");
    }
}"""

payload = {
    "code": code,
    "language": "java",
    "question_id": "java-arra-01"
}

req = urllib.request.Request(
    "http://localhost:8000/api/execute",
    data=json.dumps(payload).encode("utf-8"),
    headers={"Content-Type": "application/json"}
)

res = json.loads(urllib.request.urlopen(req).read())
print("Java Fixed Run -> Success:", res["success"])
print("All Tests Passed:", res["all_tests_passed"])
print("Output:", res["output"].strip())
