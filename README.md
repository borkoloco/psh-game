
# **PSh-Game**

A full-stack application for generating, simulating, and displaying player statistics for an online game. This project includes a React frontend and a Django backend.

---

## **Table of Contents**
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Setup Instructions](#setup-instructions)
  - [Backend Setup](#backend-setup)
  - [Frontend Setup](#frontend-setup)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [License](#license)

---

## **Features**
- Simulates player stats periodically using a cron-like script.
- Displays the top 10 players on a dynamic leaderboard.
- Supports exporting leaderboard data to a CSV file.
- Backend API for managing player statistics.
- Responsive and user-friendly frontend design.

---

## **Tech Stack**
### **Frontend**
- React
- Axios (for API requests)
- Styled-components (for styling)

### **Backend**
- Django
- Django REST Framework
- MySQL (or your chosen database)
- Python `schedule` for periodic tasks

---

## **Setup Instructions**

### **Backend Setup**
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/psh-game.git
   cd psh-game/backend
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure your `.env` file:
   ```plaintext
   SECRET_KEY=<your-secret-key>
   DATABASE_URL=<your-database-url>
   ```

5. Run migrations and start the server:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py runserver
   ```

6. Start the simulation script:
   ```bash
   python simulate_stats_script.py
   ```

---

### **Frontend Setup**
1. Navigate to the frontend folder:
   ```bash
   cd ../frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm start
   ```

---

## **Usage**
1. Navigate to the React app at `http://localhost:3000/` to view the leaderboard.
2. The backend API is available at `http://localhost:8000/api/stats/`.
3. The simulation script periodically generates new player stats, visible in the frontend.

---

## **API Endpoints**

### **GET /api/stats/**
- Retrieves the top 10 players.
- Example response:
  ```json
  {
    "topPlayers": [
      {
        "player_id": 123,
        "nickname": "PlayerOne",
        "score": 98,
        "creation_date": "2025-01-13T12:34:56Z"
      }
    ],
    "lastUpdated": "2025-01-13 12:34:56"
  }
  ```

---

## **License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
