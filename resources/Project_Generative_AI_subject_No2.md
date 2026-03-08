# Development of an AI Agent Application

**Course**: Generative AI  
**University**: Dauphine-PSL University

## Project Description

This project focuses on building an **AI Agent** — an autonomous system powered by a Large Language Model (LLM) that can reason, plan, and take actions to accomplish tasks. Unlike a simple chatbot that only responds to messages, an AI Agent can use tools, make decisions, and execute multi-step workflows autonomously.

AI Agents represent the next evolution of Generative AI applications. They combine the reasoning capabilities of LLMs with the ability to interact with external systems (APIs, databases, file systems, web services, etc.) to solve real-world problems.

#### USE CLAUDE CODE AS MUCH AS YOU CAN TO BE MORE PRODUCTIVE

## Core Concepts

Your agent should demonstrate the following capabilities:

1. **Reasoning & Planning**: The agent should be able to break down complex tasks into smaller steps and decide on a strategy.
2. **Tool Use**: The agent should be able to call external tools/functions to gather information or take actions (e.g., search the web, query a database, call an API, read/write files).
3. **Iterative Execution**: The agent should be able to execute multiple steps in a loop — observe results, reason about them, and decide the next action.
4. **Memory / Context**: The agent should maintain context across steps within a task.

## Objectives

1. **Agent Definition:**
   - Identify a real-world problem that benefits from an autonomous agent approach
   - Define what tools/actions the agent will need
   - Design the agent's reasoning loop (e.g., ReAct pattern: Reason → Act → Observe → Repeat)
   - Choose appropriate technologies and frameworks

2. **Development:**
   - Implement the agent's core reasoning loop using Anthropic's Claude API with tool use
   - Define and implement at least **3 tools** the agent can call
   - Build a user interface (web app, CLI, or other) for interacting with the agent
   - Handle edge cases: tool failures, ambiguous requests, token limits

3. **Testing and Evaluation:**
   - Test the agent on at least 5 different scenarios
   - Document cases where the agent succeeds and where it struggles
   - Measure and report token usage / cost per task

4. **Deployment:**
   - Deploy your agent to a suitable platform
   - Document setup and usage instructions

## Requirements

1. Your project must:
   - Use Anthropic's Claude API with **tool use** (function calling)
   - Implement at least **3 different tools** the agent can use
   - Have a multi-step reasoning loop (not just a single API call)
   - Have a functional user interface
   - Be properly documented
   - Be deployed and accessible

2. Technical requirements:
   - Use version control (Git)
   - Include a README with setup and usage instructions
   - Include example interactions demonstrating the agent's capabilities

## Getting Started

1. Your Anthropic API key will be provided by the instructor during the course.

```bash
export ANTHROPIC_API_KEY=your_api_key_here
```

#### Please only use `claude-haiku-3-5-20241022` (Claude 3.5 Haiku) to manage API costs.

2. Install the working environment following the guide: `resources\Guide_Setup_Environment.md`

3. Create a GitHub account if you don't have one

4. Fork the course repository into your GitHub account

Course repository to fork : https://github.com/End2EndAI/Generative-AI-Module-Dauphine-2026

5. Create a new branch for your project

6. Start developing your agent

## Agent Ideas

Here are some suggestions to inspire you (but feel free to come up with your own ideas):

1. **Research Agent**
   - Takes a research question, searches the web, reads articles, and produces a structured summary with sources
   - Tools: web search, URL reader, file writer

2. **Data Analysis Agent**
   - Takes a CSV file and a question in natural language, writes and executes Python code to analyze the data, and returns insights with charts
   - Tools: code executor, chart generator, file reader

3. **Email Drafting Agent**
   - Reads your inbox (or a simulated inbox), prioritizes emails, and drafts replies based on your communication style
   - Tools: email reader, email sender, style analyzer

4. **Travel Planning Agent**
   - Takes a destination and preferences, searches for flights, hotels, and activities, and produces a full itinerary
   - Tools: flight search API, hotel search API, activity finder, calendar planner

5. **Code Review Agent**
   - Analyzes a GitHub repository, identifies issues, suggests improvements, and can even create pull requests
   - Tools: GitHub API, code analyzer, PR creator

6. **Personal Finance Agent**
   - Connects to your bank data (simulated), categorizes expenses, identifies trends, and suggests savings
   - Tools: transaction reader, categorizer, chart generator, budget calculator

## Resources

1. [Anthropic Tool Use Documentation](https://docs.anthropic.com/en/docs/build-with-claude/tool-use/overview)
2. [Building Effective Agents (Anthropic Guide)](https://www.anthropic.com/engineering/building-effective-agents)
3. [Anthropic Python SDK](https://github.com/anthropics/anthropic-sdk-python)
4. [Claude Code documentation](https://docs.anthropic.com/en/docs/claude-code)
5. [Free hosting for Flask app](https://www.pythonanywhere.com)
6. [ReAct Pattern Paper](https://arxiv.org/abs/2210.03629) — The foundational pattern for reasoning + acting agents
