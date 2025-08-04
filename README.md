# TaxBuddy AI

**An AI-Powered Tax Recommendation App (Angular + FastAPI + Azure)**

Get personalized, AI-generated tax-saving tips by logging in, entering your tax info, and receiving instant suggestions powered by Azure OpenAI. Built as a hands-on learning project to master cloud-native full-stack architecture, secure authentication, and LLM (Large Language Model) integration.

> MVP in progress — designed for modern authentication, modular API, robust SQL storage, and seamless cloud deployment.  
> Built to demonstrate enterprise-ready patterns: CI/CD, state management, and AI-powered features.

---

## Tech Stack

- **Frontend**: Angular + TypeScript + RxJS + Bootstrap
- **Backend**: Python + FastAPI + SQLAlchemy + PyODBC + Pydantic
- **Database**: Azure SQL
- **Cloud & AI**: Azure App Services, Azure OpenAI, Azure DevOps
- **Authentication**: JWT (OAuth2 simulation)
- **Testing**: (Planned) Pytest, Swagger UI, E2E with Cypress/Protractor

---

## Authentication & Security

- **JWT Tokens**: Issued on login, required for all protected API routes
- **OAuth2 Simulated**: Secure token flow via FastAPI
- **.env Protection**: Connection strings & secrets excluded with `.gitignore`
- **Verified with Swagger UI**: Authenticated flow tested end-to-end

---

## FEATURES

### What You Can Do (Current Features)

- **Angular frontend is live:** Loads login, tax form and result pages (UI scaffold)
- **Backend is running:** Responds to auth and tax POST requests (mock logic for demo/testing)
- **Test backend endpoints via Swagger UI:** (/auth/login, /tax/)
These respond with stub/dummy data (no real authentication or AI yet)
- **View API docs and test POST requests** at http://localhost:8000/docs

### What's Coming Next

- **Real Authentication:** Implementing full JWT auth with secure user storage and login flow
- **AI Powered Tax Tips:** Connecting to Azure OpenAI (GPT-4o) for live, personalized tax-saving advice
- **Database Integration:** Persisting all user queries and AI tips in Azure SQL for analytics and future retrieval
- **Role-Based Access:** Adding admin and user roles, with protected endpoints and permission logic
- **End-to-End Angular Flow:** Completing form submission, dynamic result display, and error handling in the UI
- **User Experience Upgrades:** Improving validation, error messages, and interactive feedback throughout the app
- **Deployment Pipeline:** Setting up CI/CD and production deployment on Azure App Services and DevOps
- **Document-Based AI (RAG):** Planning future expansion to Retrieval-Augmented Generation for richer, document-sourced answers

---

## CORE MODULES

### **Frontend (Angular)**

- `login.component.ts`: JWT login, route protection
- `tax-form.component.ts`: Reactive form, sends data to backend
- `result.component.ts`: Displays AI-generated tip and DB result

### **Backend (FastAPI)**

- `/auth/login`: User login, JWT issued
- `/tax/`: Accepts tax data, triggers AI, stores & returns result

---

## EXAMPLE API FLOW

1. **POST** `/auth/login`  
   — Authenticate, receive JWT
2. **POST** `/tax/`  
   — Submit tax form (JWT required), get tip + save to DB
3. **GET** `/docs`  
   — Explore endpoints and test flow

---

## DATABASE (Azure SQL) SCHEMA

```sql
CREATE TABLE users (
  id INT PRIMARY KEY IDENTITY,
  email VARCHAR(255) UNIQUE,
  hashed_password VARCHAR(255)
);

CREATE TABLE tax_queries (
  id INT PRIMARY KEY IDENTITY,
  user_id INT FOREIGN KEY REFERENCES users(id),
  income FLOAT,
  deductions FLOAT,
  tip TEXT,
  created_at DATETIME DEFAULT GETDATE()
);
``` 
## 
The current MVP is in progress, but I’m already designing for robust Azure SQL integration. Above is the schema I’ll be implementing next—user info, tax queries, and the relationships between them.
 

## Deployment Plan

- **Frontend**: Build with `ng build --prod`, deploy `/dist` to Azure App Service or Static Web Apps
- **Backend**: Zip FastAPI server and deploy to Azure App Service
- **CI/CD**: Managed with Azure DevOps pipelines (build, test, deploy)
- **Monitoring**: Azure App Insights for logs and metrics

---

## Development & Testing

**Local Quick Start**

```bash
# Clone the repo
git clone https://github.com/your-username/taxbuddy-ai.git
cd taxbuddy-ai

# Frontend
cd client
npm install
ng serve   # runs at http://localhost:4200/

# Backend
cd ../server
python -m venv venv
source venv/Scripts/activate    # (Windows)
pip install -r requirements.txt
python -m uvicorn app.main:app --reload   # API at http://localhost:8000/docs

# Add your .env with: 
AZURE_SQL_CONNECTION_STRING=...
AZURE_OPENAI_KEY=...

## Testing
Manual: Swagger UI for API tests

Planned: Backend unit/integration (pytest), frontend E2E
```

---

## LEARNING PATH / MILESTONES

- [x] **Step 1:** Frontend setup — Angular, RxJS — Login & tax form UI
- [x] **Step 2:** Backend setup — FastAPI, JWT — REST API: login + tax endpoint (stubbed)
- [ ] **Step 3:** Auth/Microservices — OAuth2, Gateway — Secure API, split services
- [ ] **Step 4:** Azure SQL & DB — SQLAlchemy — Connect + write to DB
- [ ] **Step 5:** Azure DevOps/CI/CD — Pipelines — FE + BE deployed to Azure
- [ ] **Step 6:** Azure OpenAI — GPT-4o — AI-powered tips
- [ ] **Step 7:** Refactor, Docs — PyTorch (opt) — Polish, test, write docs



---

## FUTURE IDEAS
 - RAG (Retrieval-Augmented Generation) for richer answers
 - Role-based dashboards
 - Advanced analytics/logging
 - Key Vault integration for secrets
 - PyTorch LLM proof-of-concept

---

## Why This Project?
TaxBuddy AI was inspired by my desire to build and learn with the technologies shaping modern enterprise solutions—Angular, FastAPI, Azure, SQL, and AI-powered features. I wanted to challenge myself by building a full-stack application that mirrors the complexity and scale of today’s real-world engineering problems, including secure authentication, clean API design, and LLM integration.

As I continue growing as a developer, I’m especially interested in working at the intersection of backend systems, cloud platforms, and AI—collaborating with product teams and data scientists to deliver meaningful features.

It represents my commitment to learning and applying modern architectures—and my enthusiasm for contributing to forward-thinking, AI-driven engineering teams.


---

## About Me

I’m a full-stack software developer with a strong backend focus, specializing in secure authentication, cloud-native architecture, and scalable system design. My portfolio highlights hands-on projects that span modern JavaScript (MERN), Python (FastAPI), and cloud platforms like Azure. Lately, I’ve been leveling up my expertise in enterprise SQL, Angular, and AI/LLM integration—always striving to deliver clean, maintainable code and intuitive user experiences. I’m driven by curiosity, rapid learning, and a desire to contribute to technical teams building the next generation of intelligent web applications.

---

## Contact

- 📍 New York, NY  
- 📧 crystaldepalma@yahoo.com  
- 🌐 [crystal-depalma.com](https://crystal-depalma.com)  
- 💼 [LinkedIn](https://linkedin.com/in/crystal-depalma-496710304)  
- 💻 [GitHub](https://github.com/cdepalma32)