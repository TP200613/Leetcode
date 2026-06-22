import os
import re

FOLDERS = {
    "Easy":   ("EASY_START",   "EASY_END"),
    "Medium": ("MEDIUM_START", "MEDIUM_END"),
    "Hard":   ("HARD_START",   "HARD_END"),
}

def get_problems(folder):
    problems = []
    if not os.path.exists(folder):
        return problems
    for filename in sorted(os.listdir(folder)):
        if not filename.endswith(".py"):
            continue
        name = filename[:-3]  # remove .py
        parts = name.split("_", 1)
        if len(parts) < 2:
            continue
        number = parts[0].zfill(4)
        title = parts[1].replace("_", " ").title()
        problems.append((number, title))
    return problems

def build_table(problems):
    lines = []
    lines.append("| Problem No. | Problem Name |")
    lines.append("| ----------- | ------------ |")
    for number, title in problems:
        lines.append(f"| {number} | {title} |")
    return "\n".join(lines)

def update_section(content, start_marker, end_marker, new_table):
    pattern = rf"(<!-- {start_marker} -->).*?(<!-- {end_marker} -->)"
    replacement = f"<!-- {start_marker} -->\n{new_table}\n<!-- {end_marker} -->"
    return re.sub(pattern, replacement, content, flags=re.DOTALL)

def update_stats(content, counts):
    total = sum(counts.values())
    stats = (
        f"- Total Solved: {total}\n"
        f"- Easy: {counts['Easy']}\n"
        f"- Medium: {counts['Medium']}\n"
        f"- Hard: {counts['Hard']}"
    )
    pattern = r"(<!-- STATS_START -->).*?(<!-- STATS_END -->)"
    replacement = f"<!-- STATS_START -->\n{stats}\n<!-- STATS_END -->"
    return re.sub(pattern, replacement, content, flags=re.DOTALL)

def main():
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    counts = {}
    for folder, (start, end) in FOLDERS.items():
        problems = get_problems(folder)
        counts[folder] = len(problems)
        table = build_table(problems)
        content = update_section(content, start, end, table)

    content = update_stats(content, counts)

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(content)

    print(f"README updated. Total solved: {sum(counts.values())}")

if __name__ == "__main__":
    main()
