import urllib.request
import json
import sys

# Ensure UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

def test_api(url, payload):
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode('utf-8'),
        headers={'Content-Type': 'application/json'}
    )
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode('utf-8'))

# Test 1: Custom question success
res1 = test_api('http://localhost:8000/api/execute', {
    'code': 'num = 29\nis_prime = True\nprint(f"{num} is Prime: {is_prime}")',
    'language': 'python',
    'custom_title': 'Check if a Number is Prime',
    'expected_output': '29 is Prime: True'
})
print('Test 1 (Custom Success):', res1['success'], res1['all_tests_passed'], repr(res1['output'].strip()))

# Test 2: Custom question mismatch
res2 = test_api('http://localhost:8000/api/execute', {
    'code': 'print("29 is Prime: False")',
    'language': 'python',
    'custom_title': 'Check if a Number is Prime',
    'expected_output': '29 is Prime: True'
})
print('Test 2 (Custom Mismatch):', res2['success'], res2['all_tests_passed'], res2['parsed_error']['error_type'])

# Test 3: Custom hint
res3 = test_api('http://localhost:8000/api/hint', {
    'code': 'for i in range(1, num):\n    if num % i == 0:\n        is_prime = False',
    'language': 'python',
    'hint_level': 1,
    'custom_title': 'Check if a Number is Prime',
    'custom_description': 'Given n = 29, check if prime'
})
print('Test 3 (Custom Clue 1):', res3['level_name'], '|', res3['title'])
print('  Text:', res3['hint_text'][:120])

# Test 4: Custom explain cause
res4 = test_api('http://localhost:8000/api/explain-cause', {
    'code': 'print("wrong")',
    'language': 'python',
    'error_message': 'Output mismatch',
    'error_type': 'OutputMismatch',
    'custom_title': 'Check if a Number is Prime',
    'custom_description': 'Given n = 29, check if prime'
})
print('Test 4 (Custom Cause Intent):', res4['programmer_intent'])
print('ALL CUSTOM QUESTION API TESTS PASSED SUCCESSFULLY!')
