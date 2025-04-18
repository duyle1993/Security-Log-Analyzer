Security Log Analyzer with Threat Scoring — Project Reflection

Project Overview
This project focused on designing and implementing a Security Log Analyzer with Threat Scoring, a Python-based tool that automatically parses log files, detects suspicious patterns, assigns severity scores, and maps events to MITRE ATT&CK tactics. The tool serves to enhance situational awareness by flagging potential threats from system logs, and providing visual insights through Jupyter Notebook charts. The project aligns with the principles of security automation by minimizing the need for manual log inspection and promoting data-driven decision-making in incident response.

Approach and Tools Used
The analyzer was built in Python and leverages the re module for regex-based keyword scanning, json for output formatting, and matplotlib/pandas for data visualization in Jupyter Notebooks. A lightweight severity scoring system was implemented, assigning values based on suspicious keywords (e.g., “unauthorized,” “fail,” “error”). MITRE ATT&CK tactics were incorporated by mapping keywords to corresponding tactics like TA0006 (Credential Access) and TA0005 (Defense Evasion). The logs were processed from a sample sample_logs.txt file, and results were exported as threats.json for further analysis.

Use of AI Tools
GitHub Copilot and ChatGPT played a significant role in accelerating development. For instance, prompts such as “Write a Python script that parses logs and assigns threat scores based on keywords” helped generate baseline code. The AI tools also assisted in structuring regular expressions and improving performance with dictionary lookups. Suggestions were reviewed and customized—for example, refactoring Copilot’s generic loops into dictionary-driven parsing logic and replacing static tag matching with a flexible MITRE tag map. Additionally, ChatGPT helped design the visual structure of the Jupyter Notebook.

Challenges and Solutions
One of the main challenges was creating a flexible threat scoring model that could scale and adapt to different log formats. To address this, the scoring and tagging system was made modular using dictionaries, enabling easier updates. Another challenge was ensuring meaningful visual representation of the results—handled by experimenting with chart types and formatting within Jupyter Notebook. File handling errors and inconsistent log formatting were resolved using exception handling and robust string parsing.

Security and Ethical Considerations
From a security perspective, the tool avoids executing any external commands or writing to sensitive directories. It was designed for offline analysis and assumes sanitized input. Ethically, it is important to clarify that the tool should not be used for surveillance or unauthorized monitoring of user activities. Its intended use is in incident response and security auditing by authorized personnel.

What I Learned
This project deepened my understanding of how automated tools can support the work of security analysts. I learned how to integrate threat scoring and basic threat intelligence (MITRE mapping) into log analysis. I also improved my skills in Python scripting, data visualization, and using AI tools responsibly to streamline development without compromising understanding or originality. This experience showed me how automation can be a powerful ally in reducing human error and increasing efficiency in cybersecurity workflows.

Time Spent
The total time spent on the project was approximately 15–18 hours over the course of two weeks, including research, coding, testing, debugging, and documentation.

Reference
Scarfone, K., & Mell, P. (2007). Guide to Intrusion Detection and Prevention Systems (IDPS) (NIST Special Publication 800-94). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-94
