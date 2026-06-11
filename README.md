Question Generator

Project Overview

The Question Generator is a web application built using Python and FastAPI that helps users generate study questions based on a selected subject and topic. A user can choose a subject, enter a topic they want to learn about, and specify the number of questions they want generated.

The application sends the user’s request to an external AI API which generates the questions dynamically. The generated questions are then displayed on the webpage in an organized list format.

The project was designed to practice:

Form handling
API integration
Dynamic HTML rendering
Basic frontend styling with HTML and CSS

 Steps and Approach

1. Creating the User Interface

An HTML page was created containing:

* A subject dropdown menu
* A text input for topics
* A field for the number of questions
* A submit button

CSS styling and a GIF image were added to improve the visual appearance of the application.


2. Handling Form Submission

When the user clicks the “Generate My Questions” button:

The form sends a POST request to the `/generate` route
An API (FastAPI) retrieves the form data using `Form(...)`

The application then builds a prompt using the user’s inputs.



3. Setting Up the FastAPI Application

Next was creating a FastAPI server in Python. Routes were created for:

Displaying the homepage
Handling question generation requests

Static files such as CSS and images were mounted using FastAPI’s `StaticFiles`.


4. Connecting to the AI API

The app sends the generated prompt to an external AI API using the `requests` library.

The API is expected to return generated questions in JSON format.


5. Displaying Results

The returned questions are:

Parsed into a Python list
Converted into HTML list items
Injected dynamically into the webpage

This allows the questions to appear immediately after generation.


 6. Error Handling and Debugging

Several debugging improvements were added during development:

Handling missing form fields
Fixing static file path errors
Displaying API error messages
Adding debug output for API responses

 Future Improvements

Several improvements can still be made to enhance the project:

1. Replace the Current API

The current API has usage limits. A better long-term solution would be:

Using OpenAI APIs
Running a local AI model
Using a free alternative API

2. Improve the User Interface

The frontend can be improved with:

Better styling
Responsive design for mobile devices
Loading animations
Dark mode support

---

3. Add Question Difficulty Levels

Users could select:

Beginner
Intermediate
Advanced
This would make the generated questions more personalized.

 4. Save Generated Questions

Future versions could allow users to:

Download questions as PDF files
Save previous generations
Print question sheets

5. Add User Authentication

Users could create accounts to:

Save study history
Track progress
Create personalized quizzes

6. Improve Error Handling

The project could include:

Better validation messages
API fallback systems
Retry mechanisms when API requests fail

 Technologies Used

Python
FastAPI
HTML
CSS
Requests Library
JSON





Author

Created by Karen Adazabra.
