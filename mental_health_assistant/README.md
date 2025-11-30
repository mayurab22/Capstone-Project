# Mental Health Counseling Agent (India)

## Problem Statement
Mental health needs are often neglected in India due to stigma and lack of awareness. People hesitate to seek help, fearing judgment or ridicule.

## Solution
A confidential AI Counseling Agent that listens, provides empathetic support, suggests coping strategies, and, in extreme cases, recommends professional psychiatrists or counselors.

## Architecture
- **Main Agent**: Orchestrates user interaction
- **Listener Sub-Agent**: Collects and understands user concerns
- **Coping Strategy Sub-Agent**: Suggests solutions and exercises
- **Referral Sub-Agent**: Recommends professionals in extreme cases

![Architecture Diagram](architecture.png)

## Features & Key Concepts
- Agent-based modular architecture
- Use of Gemini (mocked) for empathetic responses and recommendations
- Privacy-focused design
- Code comments and docstrings for clarity

## Setup Instructions
1. Clone the repository
2. Install dependencies (if any):
   ```powershell
   pip install -r requirements.txt
   ```
3. Run the Mental Health Assistant:
   ```powershell
   python mental_health_assistant/main.py
   ```

## Project Journey
- Ideation: Addressed stigma and lack of support for mental health in India
- Design: Architected agent-based solution for privacy and empathy
- Implementation: Developed agents with clear responsibilities and comments
- Integration: Mocked Gemini for safe demo (no API keys)

## Deployment
This project is designed for local execution. For cloud deployment, see comments in code for integration points.

## Bonus
- Gemini used for empathetic responses (mocked)
- Ready for deployment on Agent Engine or Cloud Run (see code comments)
- [Optional] Demo video can be added for submission

## Contact
For questions, reach out via GitHub Issues.
