# Generative AI Course Repository 2026

Welcome to the Generative AI course repository at Dauphine-PSL University for the Master IASD Executive. This repository contains essential materials for the course, including lecture slides, a setup guide, and detailed project descriptions.

## Quick Start

1. Follow the setup guide in `resources/Guide_Setup_Environment.md` to configure your development environment
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Open `notebooks/getting_started.ipynb` to verify your setup

## Repository Structure

```
.
├── data/                  # Directory for datasets and data files (for the project)
├── notebooks/             # Jupyter notebooks for experiments and examples
├── resources/             # Course materials and documentation
│   ├── Guide_Setup_Environment.md
│   ├── Cours Generative AI 2026 - Slides.pdf
│   ├── Project_Generative_AI_subject_No1.md
│   ├── Project_Generative_AI_subject_No2.md
│   └── Project_Generative_AI_subject_No3.md
├── requirements.txt       # Python package dependencies
└── config.ini             # Configuration file
```

## Course Materials

### 1. Environment Setup Guide
Located in `resources/Guide_Setup_Environment.md`, this comprehensive guide provides:

- Step-by-step instructions for setting up your development environment
- Installing Claude Code (AI-powered coding assistant in the terminal)
- Required package installations (including the Anthropic Python SDK)
- IDE configuration

### 2. Course Slides
`resources/Cours Generative AI 2026 - Slides.pdf` contains the lecture materials covering fundamental concepts of Generative AI, theoretical foundations, practical applications, and implementation examples.

### 3. Project Descriptions

The course includes three projects that progressively build your understanding and skills in Generative AI:

#### Project 1: Web Application with RAG and Anthropic API
Located in `resources/Project_Generative_AI_subject_No1.md`

- Development of an end-to-end web application using Retrieval Augmented Generation (RAG)
- Integration with Anthropic's Claude API
- Vector database implementation (ChromaDB)
- Enterprise data processing
- Flask backend with HTML/CSS/JS frontend

#### Project 2: AI Agent Application
Located in `resources/Project_Generative_AI_subject_No2.md`

- Development of an autonomous AI Agent that can reason and take actions
- Tool use and function calling with Claude
- Multi-step reasoning and task decomposition
- Real-world automation use cases

#### Project 3: Voice Note Mobile App for Startup Ideas
Located in `resources/Project_Generative_AI_subject_No3.md`

- Development of an Android or iOS mobile app
- Voice-to-text recording for capturing ideas on the go (biking, walking, driving)
- LLM-powered structuring and enhancement of raw voice notes
- Local storage and idea management

## Dependencies

See `requirements.txt` for the full list. Key packages include: pandas, numpy, flask, anthropic, chromadb.

## Contributing

For any questions or suggestions, please contact:

- Email: louis.fontaine.pro@gmail.com
- GitHub Issues: Feel free to open an issue for any questions or problems

---

Good luck with the projects, and enjoy your journey into the world of Generative AI!
