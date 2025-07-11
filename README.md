# 💼 Career Mentor Agent (CLI-Based, OpenRouter-Powered)

An AI-powered command-line assistant that guides students through career exploration, skill roadmap building, and job discovery — built using multi-agent logic with dynamic tool integration via OpenRouter.

---

## 🚀 Features

- 🔍 **Career Suggestion**: Recommends career fields based on user interest
- 🛠️ **Skill Roadmap Generator**: Provides dynamic learning paths for selected careers
- 💼 **Job Role Explorer**: Lists real-world job titles and companies
- ♻️ **Agent Handoff Logic**: Seamless flow between CareerAgent → SkillAgent → JobAgent
- 🔐 **OpenRouter Integration**: Uses OpenRouter-compatible models (e.g., Gemini, Claude) — no OpenAI key required

---

## 🧠 Agent Architecture

| Agent         | Role                                                                 |
|---------------|----------------------------------------------------------------------|
| `CareerAgent` | Suggests relevant career fields based on user's interest             |
| `SkillAgent`  | Provides career-specific learning steps using `get_career_roadmap()` |
| `JobAgent`    | Generates job titles via `get_job_listings()`                        |

---

## 🧰 Tools

| Tool Function           | Description                                                |
|-------------------------|------------------------------------------------------------|
| `get_career_roadmap()`  | Uses LLM to generate 5–7 step personalized learning plan   |
| `get_job_listings()`    | Uses LLM to return 2–3 real-world job titles and companies |

---

## 🔄 Agent Handoff Flow

```
graph TD
    A[User enters interest] --> B[CareerAgent]
    B --> C[Suggested Careers]
    C --> D[User selects a career]
    D --> E[SkillAgent → get_career_roadmap()]
    E --> F[Skill Roadmap displayed]
    F --> G[JobAgent → get_job_listings()]
    G --> H[Job Roles displayed]

```
## 🧪 Sample CLI Session

Tell me your interests: web dev

Suggested Careers:
- Frontend Developer
- Backend Developer
- Full-stack Developer

Choose one career to see a skill roadmap: Backend Developer

Skill Roadmap:
1. Learn Python or Node.js
2. Understand APIs and authentication
3. Master SQL/NoSQL databases
...

Do you want to see real-world job titles? yes

Job Roles:
- Backend Developer at ByteCraft (Remote)
- API Engineer at DataNexus (Hybrid - Lahore)
...
