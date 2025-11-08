"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

# In-memory activity database
activities = {
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    }
}


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    return activities


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """Sign up a student for an activity"""
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Get the specific activity
    # Add 2 more sports related activities, 2 more artistic activities, and 2 more intellectual activities.
    activities["Basketball Team"] = {
        "description": "Join the basketball team and compete against other schools",
        "schedule": "Mondays and Wednesdays, 4:00 PM - 6:00 PM",
        "max_participants": 15,
        "participants": []
    }
    activities["Soccer Team"] = {
        "description": "Join the soccer team and compete against other schools",
        "schedule": "Tuesdays and Thursdays, 4:00 PM - 6:00 PM",
        "max_participants": 15,
        "participants": []
    }
    activities["Art Club"] = {
        "description": "Explore your creativity through various art projects",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": []
    }
    activities["Music Band"] = {
        "description": "Join the school band and perform at events",
        "schedule": "Mondays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": []
    }
    activities["Debate Club"] = {
        "description": "Engage in debates and improve your public speaking skills",
        "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": []
    }
    activities["Science Club"] = {
        "description": "Explore scientific concepts through experiments and projects",
        "schedule": "Thursdays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": []
    }

    # Add student
    # Validate student is not already signed up
    if email in activities[activity_name]["participants"]:
        raise HTTPException(status_code=400, detail="Student already signed up for this activity")
    activities[activity_name]["participants"].append(email)
    return {"message": f"Signed up {email} for {activity_name}"}
