#🚀 Career Mentor Agent
------------------------

**Gemini Model: A Career Roadmap Builder**

Tagline: "Transforming career aspirations into personalized skill paths"

📖 Description
--------------

Gemini Model is an AI-powered career roadmap builder that assists individuals in crafting tailored skill paths for various careers. By leveraging advanced natural language processing and machine learning techniques, this project provides a unique solution for career changers, professionals seeking upskilling, and organizations looking to develop their teams' skills.

Gemini Model is designed to be modular, allowing users to input their career aspirations and receive a step-by-step roadmap for skill acquisition. The project's architecture is composed of a series of agents, each responsible for processing user input and generating the skill roadmap.

✨ Features
---------

1. **Career Roadmap Generation**: Gemini Model generates a personalized skill roadmap for the user, providing a clear path for skill acquisition.
2. **Multi-Agent Architecture**: The project features multiple agents, each responsible for a specific task, ensuring a robust and scalable solution.
3. **Natural Language Processing**: Gemini Model uses advanced NLP techniques to process user input and generate the skill roadmap.
4. **Modular Design**: The project's architecture is designed to be modular, allowing for easy extension and modification.
5. **Async Support**: Gemini Model supports asynchronous processing, enabling efficient processing of user requests.
6. **SQLite Session Management**: The project uses SQLite sessions to manage user data and ensure data integrity.
7. **Function Tool Integration**: Gemini Model integrates with function tools to provide a seamless user experience.
8. **Roadmap Visualization**: The project includes a roadmap visualization tool, allowing users to visualize their skill path.

🧰 Tech Stack Table
-------------------

| Component | Technology |
| --- | --- |
| Frontend | None (API-only) |
| Backend | Python 3.9+ |
| Tools | OpenAI, AsyncOpenAI, SQLite, Docker |
| Libraries | agents, OpenAIChatCompletionsModel, RunConfig, dotenv |

📁 Project Structure
-------------------

* **agents**:
	+ `skill_agent.py`: Handles skill roadmap generation
	+ `job_agent.py`: Handles job roadmap generation
	+ `career_agent.py`: Handles career roadmap generation
* **_instructions.py**: Contains instructions for each agent
* **gemini_model.py**: Contains the core logic for Gemini Model
* **roadmap_tool.py**: Contains the roadmap visualization tool
* **main_agent.py**: Manages the main agent
* **__init__.py**: Initialization files for each module
* **job_agent.py**: Handles job roadmap generation
* **career_agent.py**: Handles career roadmap generation

⚙️ How to Run
-------------

### Setup

1. Install the required dependencies using `pip install -r requirements.txt`
2. Create a `.env` file and set the `OPENAI_API_KEY` environment variable
3. Run `docker-compose up` to start the Docker container

### Environment

* Python 3.9+
* OpenAI API key (set in `.env` file)
* SQLite database

### Build

1. Run `python main_agent.py` to start the main agent
2. Use the `roadmap_tool.py` script to generate the skill roadmap

👤 Author
---------

**[Maaz Husyan]**

📝 License
---------

Gemini Model is licensed under the [MIT License](https://opensource.org/licenses/MIT).
