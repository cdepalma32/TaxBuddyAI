# TaxBuddy AI
**An AI-Powered Tax Recommendation App (Angular + FastAPI + Azure)**

TaxBuddy AI helps users uncover personalized, AI-generated tax-saving tips.
You simply log in, enter your income and deductions, and the system instantly returns a friendly recommendation powered by Azure OpenAI (GPT-4o) — all running securely on the backend.

> MVP in progress — designed for secure authentication, modular APIs, robust Azure SQL storage, 
> and backend-only AI integration.  
> Built to demonstrate enterprise-ready architecture: CI/CD pipelines, cloud infrastructure, and AI-powered logic.

---

### How the AI Works

When you enter your financial details (like income and deductions), the **FastAPI** backend sends that  
information securely to **Azure OpenAI**.  
The AI model — similar to ChatGPT — analyzes the inputs and returns a personalized tax tip,  
such as: "*Consider contributing to an IRA to lower taxable income."*

> **Why the AI runs only in the backend:**

- **Security:** Sensitive data (income, deductions) never touches the browser-side model — it stays on the secure server.  
- **Scalability:** The backend can manage multiple user requests, store results, and log AI usage or cost analytics.  
- **Maintainability:** If you switch AI models (e.g., GPT-4o → newer version), you update the FastAPI logic — not the frontend.  
- **Professional architecture:** Real enterprise systems always handle AI calls server-side to protect data and API keys.

So, while users only see a clean and fast UI, the entire intelligence layer lives in FastAPI — managing data, calling OpenAI, and returning results safely.

---

### What the User Enters

In the upcoming version, users will input simple tax details such as:

- W-2 income or total annual income  
- Estimated deductions (standard or itemized)  
- Optional fields for dependents, filing status, or pre-tax contributions  

These inputs are securely processed by the backend, which sends a summarized prompt to Azure OpenAI.  
The AI then generates personalized, plain-language tax guidance — for example:  
> “Try increasing your 401(k) contributions to reduce taxable income by up to $3,000.”


---

## Tech Stack

- **Frontend**: Angular + TypeScript + RxJS + Bootstrap
- **Backend**: Python + FastAPI + SQLAlchemy + PyODBC + Pydantic
- **Database**: Azure SQL
- **AI Platform**: Azure OpenAI (GPT-4o)
- **Cloud & DevOps**: Azure App Services + Azure DevOps
- **Authentication**: JWT (OAuth2- style)
- **Testing**: Swagger UI (manual) → Pytest/Cypress (planned)

---

## Authentication & Security

- **JWT Tokens**: Issued on login, required for all protected API routes
- **OAuth2 Simulated**: Secure token flow via FastAPI
- **Frontend Guarding**: Angular AuthGuard + Interceptor enforce route access
- **.env Protection**: API keys and connection strings hidden from repo
- **Verified**: Authenticated flow tested via Swagger UI

---

## FEATURES

### What You Can Do (Current Features)

- **Angular frontend is live:** Angular app fully functional: login → form → result
- **Backend is running:** Backend handles POST /tax requests and returns AI-generated tips
- **Testing:** Swagger UI available for API testing (/auth/login, /tax)
- **Modular structure**: routes, guards, services, and interceptors
- **Integration**: Backend integrated with Azure SQL (connection verified)

### What's Coming Next

- **Real Authentication:** Real JWT verification (login/register persistence)
- **SQL Data Persistecne:** Store all tax queries and AI responses in Azure SQL for history and analytics
- **AI Logging & Cost Tracking:** Record token usage and cost per Azure OpenAI call for transparency and optimization
- **AI Powered Tax Tips:** Azure OpenAI (GPT-4o) integrated via services/llm.py
- **Database Integration:** Database storage for all user queries and AI responses
- **Role-Based Access:** Adding admin and user roles, with protected endpoints and permission logic
- **End-to-End Angular Flow:** Completing form submission, dynamic result display, and error handling in the UI
- **Enhanced User Experience:** Add dynamic validation, clearer error messages, loading states, and feedback animations for form submission
- **Deployment Pipeline:** Configure CI/CD in Azure DevOps and deploy both FastAPI (backend) and Angular (frontend) to Azure App Services
- **Phase 2 - Document-Based AI (RAG):** Future expansion to Retrieval-Augmented Generation — where the app references real tax documents or IRS publications to generate richer, source-backed recommendations

---

## CORE MODULES

### **Frontend (Angular)**

- `login.component.ts`: JWT login, route protection
- `tax-form.component.ts`: Reactive form, sends data to backend
- `result.component.ts`: Displays AI-generated tip and DB result

### **Backend (FastAPI)**

- `/auth/login`: User login, JWT issued
- `/auth/register`: Registers new user
- `/tax/`: Creates new query, calls AI model, returns { id, tip }
- `/tax/queries/{id}`: Retrieves past results
- `/taxcheck`: Confirms DB connection

---

## EXAMPLE API FLOW

1. **POST** `/auth/login`  
   — Authenticate, receive JWT
2. **POST** `/tax/`  
   — Submit tax form (JWT required), get tip + save to DB
3. **GET** `/tax/queries/{id}` 
   — Fetch the saved tip for that session
4. **GET** `/docs`  
   — Explore endpoints via Swagger UI

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

- **Frontend**: ng build --configuration production → deploy /dist to Azure App Service
- **Backend**: Deploy FastAPI with Gunicorn
- **CI/CD**: Azure DevOps pipelines for build/test/deploy
- **Monitoring**: Azure App Insights for logs and performance tracking

---

## Development & Testing

**Local Quick Start**

```bash
# Clone
git clone https://github.com/cdepalma32/TaxBuddyAI.git
cd TaxBuddyAI

# Frontend
cd client
npm install
ng serve   # http://localhost:4200/

# Backend
cd ../server
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
python -m uvicorn app.main:app --reload   # http://localhost:8000/docs

# Add your .env with: 
AZURE_SQL_CONNECTION_STRING=...
AZURE_OPENAI_KEY=...

## Testing
Manual: Swagger UI for API tests

Planned: Backend unit/integration (pytest), frontend E2E
```

---

## LEARNING PATH / MILESTONES

- [x] **Step 1:** Frontend setup — Angular + RxJS → Login → Tax Form → Result flow
- [x] **Step 2:** Backend setup — FastAPI + JWT → Auth routes, /tax endpoint (stubbed)
- [x] **Step 3:** Routing & Guards — Implemented Angular AuthGuard + Interceptor for secure navigation
- [ ] **Step 4:** Azure SQL Integration — Connect via SQLAlchemy and write user queries to DB
- [ ] **Step 5:** Azure OpenAI Integration — Backend-only LLM (GPT-4o) for personalized tax tips
- [ ] **Step 6:** Authentication Persistence — Full JWT verification + refresh tokens across sessions
- [ ] **Step 7:** CI/CD Deployment — Configure Azure DevOps pipeline and deploy FE + BE to App Services
- [ ] **Step 8:** Observability & Monitoring — Enable Application Insights for metrics and AI latency tracking
- [ ] **Step 9:** UX Enhancements — Validation, error feedback, and polished UI interactions
- [ ] **Step 10:** Documentation & Testing — Write technical docs + add unit/integration tests
---

## FUTURE IDEAS
 - **Document-Based AI (RAG):** Retrieval-Augmented Generation using real IRS/tax documents
 - **Role-based dashboards:** Admin vs. User views with query history and analytics
 - **Advanced analytics/logging:** Track token usage, AI costs, and user query patterns
 - **Key Vault Integration:** Secure storage for secrets and API keys
 - **AI Analytics Dashboard:** Visualize AI cost, latency, and accuracy over time

---

## Why This Project?
TaxBuddy AI is both a learning journey and portfolio build — proving how to connect modern full-stack systems using Angular, FastAPI, Azure SQL, and OpenAI in a production-ready way.
It demonstrates secure data flow, modular architecture, and cloud scalability, all with a clear user benefit: smarter, personalized financial insights.

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