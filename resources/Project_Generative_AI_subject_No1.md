# Development of an End-to-End Web Application Leveraging Retrieval Augmented Generation (RAG) and Anthropic's Claude API with Enterprise Data

**Course**: Generative AI  
**University**: Dauphine-PSL University

## Project Description

This project aims to develop a robust web application that integrates the principles of Retrieval Augmented Generation (RAG) and Anthropic's Claude API. The application will utilize enterprise data to demonstrate the potential of Generative AI in enhancing productivity and task automatization, especially in customer interaction and customer service.

## Datasets

Simulated enterprise data will be provided, which includes:
- Twitter's customer support data: tweets from customers and replies from customer service

## Objectives

1. **Product Brainstorming:** 
   - Analysis and understanding of the available data. 
   - Identifying opportunities where Generative AI can provide value.
   - Exploration of potential applications using RAG and Generative AI on those data.
   - Choose an idea of web application to implement.

2. **Data Retrieval and Formatting:**
   - Extracting, cleaning, and organizing the provided data.
   - Formatting the data to be compatible with a RAG system.
   - Start with the sample data `twitter_data_clean_sample`.

3. **Development:**
   - Architectural design of the web application.
   - Building functional back-end components of the application using Flask in Python, integrating Anthropic's Claude API and a RAG system.
   - Building a user-friendly front-end using HTML, CSS, and Javascript.
   - Storing data in a vector database, such as ChromaDB.
   - Version control with Git.

4. **Deployment:**
   - Deploying the application on an appropriate web platform.

## Expected Deliverable

- A fully operational web application that demonstrates the practical application of Retrieval Augmented Generation and generative AI using enterprise data.
- The project is available on GitHub.

## Getting Started

1. Your Anthropic API key will be provided by the instructor during the course.

Set your API key as an environment variable:
```bash
# On macOS/Linux:
export ANTHROPIC_API_KEY=your_api_key_here

# On Windows (Command Prompt):
set ANTHROPIC_API_KEY=your_api_key_here

# On Windows (PowerShell):
$env:ANTHROPIC_API_KEY="your_api_key_here"
```

Or use the `config.ini` file (see the notebook for an example).

#### Please only use the following models from Anthropic (to manage API costs):

- `claude-haiku-3-5-20241022` (Claude 3.5 Haiku) for fast and cheap responses
- For embeddings, use an open-source model via ChromaDB's built-in embedding function, or use `voyage-3-lite` from Voyage AI (available through the Anthropic ecosystem)

2. Install the working environment following the guide

`resources\Guide_Setup_Environment.md`

3. Create a GitHub account

4. Fork the course repository into your GitHub account

Course repository to fork : https://github.com/End2EndAI/Generative-AI-Module-Dauphine-2026

Click on the `Fork` button on the page above, while being connected to your GitHub account.

5. Clone the repository on your laptop

You should have git installed on your laptop. Go to a folder and use the command `SHIFT + Right click`. Click on `Git Bash Here` (If it doesn't appear, just open the program `Git Bash` and go to the folder where you want to clone the repository).

In the opened terminal, use the following command to clone the repository : `git clone <YOUR_FORKED_REPOSITORY_URL>`. 

To get the `<YOUR_FORKED_REPOSITORY_URL>`, go into your forked repository, and click on `<> Code` and copy the HTTPS Web URL.

6. **IMPORTANT** : Copy or recreate the virtual environment

You have two options:
- Copy the `genai_env` folder created during the setup into your forked project folder
- Or recreate the virtual environment in your project folder by following the same steps as in the setup guide

You should have a folder `genai_env` in the folder `Generative-AI-Module-Dauphine-2026`

7. Open your code editor and open the repository

8. Setup your virtual env in your editor

If using VS Code: Click on `Help`, `Show All Commands`. Type `Python: Select Interpreter` and choose your virtual env (`genai_env` from the guide).

9. Test your environment

Open the files `notebooks\getting_started.ipynb` and `test_flask_app.py`, and run them, to see if everything is well configured.

10. Check the data with the notebook `notebooks\getting_started.ipynb`

Use the sample data first `data\twitter_data_clean_sample.csv`. 

#### Warning : there are a lot of data in the full csv data `data\twitter_data_clean.csv`, please be careful especially when processing that data with the API to not consume all the API Credit.

11. You are ready to go!


## Suggestion of the way of work

- USE CLAUDE CODE AS MUCH AS YOU CAN TO GENERATE CODE

- Start with comprehending the data using the sample file and establishing a clear objective for your application, and how your application will look like / work.

- Initially, construct a basic prototype of the front-end interface, utilizing Claude Code for this purpose. I suggest to use HTML, CSS and JS for simplicity, but you are welcome to use more advanced frameworks.

- Once the primary features of the front-end are operational, proceed to develop a straightforward Flask back-end. This could start as simply as returning the input message. Ensure the Flask server is operational and effectively communicating with the front-end. Understand how the connection works between the front-end and the back-end. Experiment by modifying the front, then the back, ...

- Next, enhance the Flask back-end by integrating the Retrieval-Augmented Generation (RAG) system. Start by utilizing the provided sample file `twitter_data_clean_sample.csv` to enable the system to identify and respond with the most relevant tweet, using Claude-generated answers. Initially, employ an Excel file for storing embeddings, progressing later to a more sophisticated vector database solution, such as ChromaDB.

- Evaluate your system using the evaluation dataset `data\twitter_data_clean_eval.csv`.

- Finally, focus on deploying your web application. For hosting the Flask application, consider using a free platform like PythonAnywhere, which allows for hosting, running, and coding Python in a cloud environment. 

## Resources

1. [Guide to use the Anthropic API](https://docs.anthropic.com/en/docs/build-with-claude/overview)
2. [Anthropic Python SDK](https://github.com/anthropics/anthropic-sdk-python)
3. [Guide to build a RAG system](https://docs.anthropic.com/en/docs/build-with-claude/retrieval-augmented-generation)
4. [Guide to implement a ChromaDB vector database](https://docs.trychroma.com/getting-started)
5. [Free hosting for Flask app](https://www.pythonanywhere.com)
6. How to use Git, create a virtual env and how to push on GitHub: Ask Claude Code!
7. [Claude Code documentation](https://docs.anthropic.com/en/docs/claude-code)
