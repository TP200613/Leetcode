import os
import re

# Repository root directory
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

README = os.path.join(ROOT, "README.md")


def get_problems(folder):
    problems = []

    if not os.path.exists(folder):
        return problems

    for file in sorted(os.listdir(folder)):

        # Count only Python solution files
        if not file.endswith(".py"):
            continue

        filename = os.path.splitext(file)[0]

        match = re.match(r"(\d+)[_-](.*)", filename)

        if match:
            problem_no = match.group(1)
            problem_name = (
                match.group(2)
                .replace("_", " ")
                .replace("-", " ")
                .title()
            )
        else:
            problem_no = "-"
            problem_name = filename.replace("_", " ").title()

        problems.append((problem_no, problem_name))

    return problems


def generate_table(problems):
    table = "| Problem No. | Problem Name |\n"
    table += "|------------|-------------|\n"

    for number, name in problems:
        table += f"| {number} | {name} |\n"

    return table


easy = get_problems(os.path.join(ROOT, "Easy"))
medium = get_problems(os.path.join(ROOT, "Medium"))
hard = get_problems(os.path.join(ROOT, "Hard"))

easy_count = len(easy)
medium_count = len(medium)
hard_count = len(hard)

total_count = easy_count + medium_count + hard_count

progress_section = f"""
- Total Solved: {total_count}
- Easy: {easy_count}
- Medium: {medium_count}
- Hard: {hard_count}
""".strip()

easy_table = generate_table(easy)
medium_table = generate_table(medium)
hard_table = generate_table(hard)

with open(README, "r", encoding="utf-8") as file:
    content = file.read()

content = re.sub(
    r"<!-- STATS_START -->(.*?)<!-- STATS_END -->",
    f"<!-- STATS_START -->\n{progress_section}\n<!-- STATS_END -->",
    content,
    flags=re.DOTALL,
)

content = re.sub(
    r"<!-- EASY_START -->(.*?)<!-- EASY_END -->",
    f"<!-- EASY_START -->\n{easy_table}\n<!-- EASY_END -->",
    content,
    flags=re.DOTALL,
)

content = re.sub(
    r"<!-- MEDIUM_START -->(.*?)<!-- MEDIUM_END -->",
    f"<!-- MEDIUM_START -->\n{medium_table}\n<!-- MEDIUM_END -->",
    content,
    flags=re.DOTALL,
)

content = re.sub(
    r"<!-- HARD_START -->(.*?)<!-- HARD_END -->",
    f"<!-- HARD_START -->\n{hard_table}\n<!-- HARD_END -->",
    content,
    flags=re.DOTALL,
)

with open(README, "w", encoding="utf-8") as file:
    file.write(content)

print("README updated successfully!")
print(f"Easy   : {easy_count}")
print(f"Medium : {medium_count}")
print(f"Hard   : {hard_count}")
print(f"Total  : {total_count}")
