import re
import json

SEVERITY_SCORES = {
    "error": 5,
    "fail": 4,
    "unauthorized": 3,
    "denied": 2,
    "warning": 1
}

MITRE_TAGS = {
    "unauthorized": "TA0006: Credential Access",
    "denied": "TA0005: Defense Evasion",
    "fail": "TA0002: Execution"
}

def parse_logs(filepath):
    threats = []
    with open(filepath, 'r') as file:
        for line in file:
            score = 0
            tags = []
            for keyword, value in SEVERITY_SCORES.items():
                if keyword in line.lower():
                    score += value
                    if keyword in MITRE_TAGS:
                        tags.append(MITRE_TAGS[keyword])
            if score > 0:
                threats.append({
                    "log": line.strip(),
                    "score": score,
                    "tags": tags
                })
    return threats

def save_results(threats, output="threats.json"):
    with open(output, 'w') as outfile:
        json.dump(threats, outfile, indent=4)

if __name__ == "__main__":
    log_path = "../data/sample_logs.txt"
    results = parse_logs(log_path)
    save_results(results)
    print(f"[+] Parsed {len(results)} potential threats.")
