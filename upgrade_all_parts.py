import re
import json

def transform_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Pattern to find each hints block
    # "hints": [\s*"Where to look:[^"]*",\s*"The simple idea:[^"]*",\s*"How to fix:[^"]*"\s*]
    def replacer(match):
        h1 = match.group(1).strip()
        h2 = match.group(2).strip()
        h3 = match.group(3).strip()

        # Clean old prefixes
        h1_clean = re.sub(r"^Where to look:\s*(Look at\s*)?", "", h1, flags=re.IGNORECASE)
        h2_clean = re.sub(r"^The simple idea:\s*", "", h2, flags=re.IGNORECASE)
        h3_clean = re.sub(r"^How to fix:\s*", "", h3, flags=re.IGNORECASE)

        new_h1 = f"Logic Flaw: When solving this task, the logic assumes {h1_clean[:1].lower() + h1_clean[1:] if h1_clean else 'the operation is valid'}. However, {h2_clean}"
        new_h2 = f"Core Concept: {h2_clean} In programming, understanding edge conditions, data structure bounds, and loop terminators prevents unintended state divergence."
        new_h3 = f"What to Change in Logic: {h3_clean}"

        return f'''"hints": [
            "{new_h1}",
            "{new_h2}",
            "{new_h3}"
        ]'''

    pattern = re.compile(
        r'"hints":\s*\[\s*"([^"]+)",\s*"([^"]+)",\s*"([^"]+)"\s*\]',
        re.MULTILINE
    )

    new_content = pattern.sub(replacer, content)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"Transformed {filepath}")

for p in [2, 3, 4, 5]:
    transform_file(f"generate_data_part{p}.py")

print("All parts updated! Recompiling curriculum...")
import curriculum_builder
curriculum_builder.generate_curriculum_file()
print("Done!")
