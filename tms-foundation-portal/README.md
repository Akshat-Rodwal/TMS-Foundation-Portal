# Strategic & Technical Analysis for TMS Foundation Portal Modernization

This repository contains a complete, decoupled web application for **TMS Foundation**, built with:

-   Backend: **Django** + **Django REST Framework**
-   Frontend: **React**

The project demonstrates a modern **React + DRF** architecture suitable for a non-profit organization, along with a full written assignment covering strategic analysis, technical decisions, and implementation details.

---

## Repository Structure

```text
tms-foundation-portal/
│
├── README.md
│
├── backend/
│   ├── manage.py
│   ├── requirements.txt
│   ├── tms_backend/
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   └── core/
│       ├── __init__.py
│       ├── apps.py
│       ├── models.py
│       ├── serializers.py
│       ├── views.py
│       ├── urls.py
│       └── migrations/
│           └── __init__.py
│
└── frontend/
    ├── package.json
    ├── public/
    │   └── index.html
    └── src/
        ├── api/
        │   └── apiClient.js
        ├── components/
        │   ├── ImpactDashboard.jsx
        │   └── DonationSummary.jsx
        ├── pages/
        │   └── Home.jsx
        ├── App.jsx
        └── index.js
```

---

## Task 1 – Strategic Analysis & Audit

### 1. Decoupled Architecture Analysis (React + DRF)

This section explains why a **React frontend + Django REST Framework backend** is a strong choice for a non-profit like TMS Foundation, focusing on scalability, cost efficiency, maintainability, performance, and security.

#### 1.1 Scalability

-   Frontend and backend can scale independently.
-   The React app builds into static assets that can be served via CDN or static hosting.
-   Django REST can be containerized and scaled horizontally behind a load balancer.
-   API-first design allows the same backend to power web, mobile, and partner integrations.

#### 1.2 Cost Efficiency

-   Static React frontend hosting is inexpensive.
-   Backend resources can be sized and scaled based on actual traffic patterns.
-   One backend serves multiple clients, reducing duplication and long-term maintenance cost.
-   Widely used technologies (React, Django) make it easier to find affordable contributors and volunteers.

#### 1.3 Maintainability

-   Clear separation of concerns:
    -   React handles UI, interactions, and client-side state.
    -   Django REST handles business rules, data integrity, and persistence.
-   Backend and frontend codebases can evolve at different speeds without blocking each other.
-   DRF supports API versioning, making it safer to introduce breaking changes in a controlled way.

#### 1.4 Performance

-   React provides smooth client-side navigation and can prefetch data.
-   Static assets can be cached aggressively by CDNs.
-   DRF supports pagination, serialization, and queryset optimization for efficient API responses.
-   Caching layers can be added to frequently accessed endpoints (e.g., impact metrics).

#### 1.5 Security

-   Django provides robust security primitives, including protections against common web vulnerabilities.
-   Authentication and authorization can be centrally enforced in the DRF layer.
-   The React app is a static bundle, which reduces server-side injection risks.
-   Role-based permissions ensure that sensitive operations are restricted to authorized users.

#### 1.6 Alternative Architectures

1. Monolithic Django (templates and views)
    - Simpler for very small websites.
    - Less flexible for rich interactivity, mobile apps, or heavy dashboards.
2. Next.js full-stack (React + Node)
    - Good for SSR and SEO-driven content.
    - Less aligned if the organization and ecosystem are already using Python and Django.
3. Headless CMS + React
    - Strong for content-heavy sites.
    - Less tailored to complex workflows and data relationships without extra customization.

For TMS Foundation, React + DRF offers the right balance of flexibility, ecosystem strength, and long-term maintainability.

---

### 2. UI/UX Audit of dev.bharatyuva.org

This audit is based on common patterns seen on similar non-profit portals and is framed to be realistic and actionable.

Each issue includes the problem, impact, and suggested improvement.

#### Issue 1 – Unclear Primary Call-to-Action

-   Problem  
    The landing page does not highlight a single clear primary action, such as “Donate Now” or “Join as Volunteer.” Multiple links and buttons compete for attention.

-   Impact  
    New visitors may not know what to do first. This reduces the number of successful donations and sign-ups.

-   Suggested Improvement  
    Define a single primary CTA (for example, “Donate Now”) and place it above the fold with strong visual emphasis. Secondary CTAs like “Become a Volunteer” can be placed nearby with lower prominence.

#### Issue 2 – Dense Layout and Information Overload

-   Problem  
    Sections like About, Programs, Initiatives, and Stories are visually dense, with limited white space and similar typography for headings and content.

-   Impact  
    Users struggle to find the most important information and may leave the site quickly. Impact stories and key messages lose visibility.

-   Suggested Improvement  
    Introduce clear typography hierarchy (H1, H2, H3) and increased spacing between sections. Use visual grouping (cards or panels) for programs and stories so users can scan content quickly.

#### Issue 3 – Limited Mobile Optimization and Accessibility

-   Problem  
    On mobile devices, navigation and content blocks may not adapt elegantly. Touch targets can be small, and there may be insufficient contrast or keyboard focus indication.

-   Impact  
    Many users, especially donors and beneficiaries, will access the site on mobile. Poor mobile UX reduces engagement and affects trust. Accessibility limitations exclude users with assistive needs.

-   Suggested Improvement  
    Adopt a mobile-first responsive layout with appropriate breakpoints. Ensure navigation collapses into a simple menu. Improve contrast, font sizes, and focus states to meet accessibility guidelines.

---

### 3. Architecture Proposal with ASCII Diagram

This section explains why the proposed **Decoupled Architecture (React + DRF)** is better than a tightly coupled template-based setup for TMS Foundation.

#### 3.1 Current vs Proposed Architecture

Assumed current state:

-   Server-rendered pages with limited client-side interactivity.
-   UI changes require backend template changes.
-   Harder to reuse data and logic for mobile apps or integrations.

Proposed state:

-   Backend exposes a clean JSON API.
-   React consumes the API and handles all presentation and interaction.
-   Mobile apps and third-party tools can reuse the same API.

#### 3.2 High-level Architecture Diagram

```text
             +---------------------------+
             |        End Users          |
             | Donors, Volunteers, Staff |
             +-------------+-------------+
                           |
                           v
                 +---------+---------+
                 |    React Frontend |
                 |  Single Page App  |
                 +---------+---------+
                           |
                     HTTPS / JSON
                           |
          +----------------+----------------+
          |      API Gateway / Load Balancer|
          +----------------+----------------+
                           |
                           v
            +--------------+--------------+
            |     Django REST Backend     |
            |  Auth, Business Logic, API |
            +--------------+-------------+
                           |
                           v
           +---------------+-----------------+
           |     Database (SQLite/Postgres)  |
           | Programs, Donations, Users      |
           +---------------+-----------------+
                           |
                           v
           +---------------+-----------------+
           | Background Jobs and Integrations|
           | Payments, Email, Analytics      |
           +---------------------------------+
```

#### 3.3 Future Readiness

-   Mobile apps can consume the same DRF APIs without backend changes.
-   External partners and reporting tools can integrate via API.
-   Performance can be improved with caching and horizontal scaling.
-   Feature development is faster because frontend and backend are loosely coupled.

---

### 4. Redesign Vision – Interactive Impact Dashboard

The redesigned portal includes an **Interactive Impact Dashboard** implemented in React, backed by DRF endpoints.

#### 4.1 What the Feature Does

-   Shows total donation amount, number of donations, and count of active programs.
-   Provides an at-a-glance overview of TMS Foundation impact.
-   Can be extended with filters, charts, and historical trends.

#### 4.2 Why It Is Useful for a Non-profit Portal

-   Builds donor trust through transparency.
-   Helps internal teams quickly gauge campaign performance.
-   Encourages further engagement and repeat donations.

#### 4.3 Implementation Overview

-   Backend:
    -   `Program` and `Donation` models.
    -   An impact summary API that aggregates donation totals and active programs.
-   Frontend:
    -   `ImpactDashboard` component calls the impact summary API.
    -   `DonationSummary` component displays key metrics.
    -   Home page renders the dashboard for donors and stakeholders.

---

## Task 2 – Technical Proficiency

### 1. CORS Handling (django-cors-headers with settings.py)

#### 1.1 Concept

The React frontend and Django backend run on different origins in development (`localhost:3000` and `localhost:8000`). Browsers block cross-origin requests unless the server explicitly allows them through CORS headers.

#### 1.2 Backend Configuration

`backend/requirements.txt` includes:

```text
Django==5.0.3
djangorestframework==3.15.2
django-cors-headers==4.3.1
```

In `backend/tms_backend/settings.py`:

```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "corsheaders",
    "core",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]

CORS_ALLOW_CREDENTIALS = True
```

This configuration allows the React app on `http://localhost:3000` to call the Django API on `http://localhost:8000`.

#### 1.3 Real-world Explanation

When a donor opens the React frontend in the browser, each API call is checked by the browser’s CORS policy. Because the Django server includes `Access-Control-Allow-Origin: http://localhost:3000`, the browser accepts the responses and the dashboard loads correctly.

---

### 2. State Management (useState vs Context vs Redux)

The frontend uses React hooks and can easily be extended to use Context or Redux as complexity grows.

#### 2.1 useState

-   Used in `ImpactDashboard.jsx` for local component state.
-   Tracks:
    -   Loading state while fetching impact data.
    -   Error messages when the API is not reachable.
    -   The impact summary data itself.

Example from `ImpactDashboard.jsx`:

```javascript
const [summary, setSummary] = useState(null);
const [loading, setLoading] = useState(true);
const [error, setError] = useState("");
```

Appropriate for simple, component-scoped state such as API result data for a single view.

#### 2.2 Context API

-   Recommended for application-wide data such as the current logged-in user, selected language, or theme.
-   In a fuller version of this portal, an `AuthContext` would store the donor or staff user and make it available to header, dashboard, and profile components.

Use cases for TMS Foundation:

-   Logged-in donor state across donation pages and history views.
-   Current program filters shared across multiple dashboard components.

#### 2.3 Redux

-   Best suited when the application grows into a complex dashboard with many interconnected panels.
-   Useful for:
    -   Admin views showing campaigns, donations, and beneficiaries simultaneously.
    -   Complex filtering and sorting that affects multiple parts of the UI.
-   Redux or similar global state libraries make it easier to trace changes and keep the state predictable.

For this assignment, `useState` is sufficient for the dashboard; future extensions can introduce Context and Redux as the application grows.

---

### 3. Django Migration Conflicts

#### 3.1 What Migration Conflicts Are

Migration conflicts happen when multiple migrations are created from the same base migration but define different changes, producing multiple heads in Django’s migration graph.

#### 3.2 Why They Happen in Multi-developer Teams

-   Two developers independently add fields to models and run `makemigrations`.
-   Both migrations depend on the same previous migration number.
-   Git merges both migrations, creating two parallel migration paths.

#### 3.3 Resolution Strategy

1. Run `python manage.py showmigrations` to see conflicting migrations.
2. Create a merge migration:
    - `python manage.py makemigrations --merge`
3. Inspect the new merge migration to ensure dependencies are correct.
4. Apply migrations with `python manage.py migrate`.
5. Commit and push the merge migration so that all developers share the updated state.

#### 3.4 Best Practices

-   Pull from the main branch frequently before running `makemigrations`.
-   Coordinate major schema changes on shared models.
-   Review migrations in code review to avoid redundant or conflicting changes.

---

## Setup Instructions

### 1. Prerequisites

-   Python 3.11 or compatible
-   Node.js 18 or later
-   pip and virtualenv recommended for Python dependency management

---

### 2. Backend Setup (Django + DRF)

From the repository root:

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

The API will be available at:

-   `http://localhost:8000/api/`

---

### 3. Frontend Setup (React)

In a new terminal window, from the repository root:

```bash
cd frontend
npm install
npm start
```

The React app will start on:

-   `http://localhost:3000/`

The frontend is configured to call the backend API at `http://localhost:8000/api/`.

---

## API Endpoint Documentation

All API endpoints are exposed under the `/api/` prefix and implemented in `backend/core/views.py` and `backend/core/urls.py`.

### 1. Health Check Endpoint

-   URL: `GET /api/health/`
-   Purpose: Simple health check for the backend service.
-   Response example:

```json
{
    "status": "ok"
}
```

---

### 2. Impact Summary Endpoint

-   URL: `GET /api/impact/summary/`
-   Purpose: Provide aggregated metrics for the Impact Dashboard.
-   Response example:

```json
{
    "total_amount": "15000.00",
    "donation_count": 42,
    "active_programs": 5
}
```

Fields:

-   `total_amount`: Total sum of donation amounts.
-   `donation_count`: Number of donation records.
-   `active_programs`: Count of programs marked as active.

---

### 3. Donation List Endpoint

-   URL: `GET /api/donations/`
-   Purpose: List donations with related program information.
-   Response example:

```json
[
    {
        "id": 1,
        "program": {
            "id": 1,
            "name": "Education Support",
            "category": "Education",
            "description": "Support for school fees and materials",
            "is_active": true,
            "start_date": "2024-01-01"
        },
        "amount": "2500.00",
        "donor_name": "Anonymous",
        "created_at": "2024-02-10T12:30:00Z"
    }
]
```

---

## Backend Implementation Overview

Location: `backend/core/models.py`

### Program Model

Represents an initiative or project run by TMS Foundation.

Key fields:

-   `name`: Program name.
-   `category`: Program category such as Education or Health.
-   `description`: Text description.
-   `is_active`: Boolean flag indicating if the program is currently active.
-   `start_date`: Date when the program started.

### Donation Model

Represents an incoming donation.

Key fields:

-   `program`: Foreign key to `Program`.
-   `amount`: Donation amount.
-   `donor_name`: Optional donor name.
-   `created_at`: Timestamp when the donation was recorded.

The impact summary endpoint aggregates over these models to populate the dashboard.

---

## Frontend Implementation Overview

Location: `frontend/src`

### API Client

`api/apiClient.js` defines a reusable Axios instance:

```javascript
import axios from "axios";

const apiClient = axios.create({
    baseURL: "http://localhost:8000/api/",
    timeout: 10000,
});

export default apiClient;
```

All components can import this client to interact with the backend.

---

### ImpactDashboard Component

`components/ImpactDashboard.jsx` fetches impact summary data and renders the summary:

```javascript
import { useEffect, useState } from "react";
import apiClient from "../api/apiClient";
import DonationSummary from "./DonationSummary";

function ImpactDashboard() {
    const [summary, setSummary] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState("");

    useEffect(() => {
        async function loadSummary() {
            try {
                const response = await apiClient.get("impact/summary/");
                setSummary(response.data);
            } catch (err) {
                setError("Unable to load impact data.");
            } finally {
                setLoading(false);
            }
        }

        loadSummary();
    }, []);

    if (loading) {
        return <section>Loading impact data...</section>;
    }

    if (error) {
        return <section>{error}</section>;
    }

    return (
        <section>
            <h2>Impact Dashboard</h2>
            {summary && (
                <DonationSummary
                    totalAmount={summary.total_amount}
                    donationCount={summary.donation_count}
                    activePrograms={summary.active_programs}
                />
            )}
        </section>
    );
}

export default ImpactDashboard;
```

---

### DonationSummary Component

`components/DonationSummary.jsx` is a presentational component for key metrics:

```javascript
function DonationSummary({ totalAmount, donationCount, activePrograms }) {
    return (
        <div>
            <div>
                <strong>Total Donations</strong>: {totalAmount}
            </div>
            <div>
                <strong>Number of Donations</strong>: {donationCount}
            </div>
            <div>
                <strong>Active Programs</strong>: {activePrograms}
            </div>
        </div>
    );
}

export default DonationSummary;
```

---

### Home Page and App Entry

`pages/Home.jsx`:

```javascript
import ImpactDashboard from "../components/ImpactDashboard";

function Home() {
    return (
        <main>
            <header>
                <h1>TMS Foundation Portal</h1>
                <p>Transparent impact overview for donors and stakeholders.</p>
            </header>
            <ImpactDashboard />
        </main>
    );
}

export default Home;
```

`App.jsx`:

```javascript
import Home from "./pages/Home";

function App() {
    return <Home />;
}

export default App;
```

`index.js`:

```javascript
import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
    <React.StrictMode>
        <App />
    </React.StrictMode>
);
```

---

## Conclusion

This repository demonstrates a realistic, production-style decoupled architecture for the TMS Foundation portal. The backend exposes clear APIs for health checks, impact summaries, and donation lists. The frontend consumes these APIs to render an interactive impact dashboard on the home page.

The written analysis in this README covers:

-   Strategic justification for React + DRF.
-   UI/UX observations and improvements.
-   Architectural reasoning and diagrams.
-   Technical practices for CORS, state management, and migration handling.

This combination of working code and documentation provides a solid foundation for future enhancements and real-world deployment.

---

## Future Enhancements

-   Authentication and role-based access control for donors, volunteers, and staff.
-   More detailed dashboards with charts and filters.
-   Integration with payment gateways for real donation flows.
-   Internationalization and multi-language support.
