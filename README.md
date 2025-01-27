# Django Weather Forecast Application

## Overview

This is a Django web application that fetches and displays the weather forecast for a given city. It uses the OpenWeatherMap API to retrieve weather data. The application provides a user-friendly interface where users can enter a city name and view the weather forecast for the next three days, including details like time, weather description, temperature, and weather icons.

## Features

-   **Weather Forecast:** Displays a three-day weather forecast.
-   **Hourly Details:** Shows weather details for each 3-hour interval within the forecast period.
-   **Weather Icons:** Displays appropriate weather icons corresponding to the weather conditions.
-   **Temperature Conversion:** Converts temperature from Kelvin to Celsius.
-   **Responsive Design:** Built with responsive design principles for optimal viewing on various devices.
-   **Interactive UI:** Uses modern web design elements and animations for an engaging user experience.

## Technologies Used

-   **Django:** Web framework for Python.
-   **OpenWeatherMap API:** For fetching weather data.
-   **Requests:** Python library for making HTTP requests.
-   **HTML, CSS, JavaScript:** For frontend design and interactivity.
-   **Animate.css:** For adding CSS animations.
-   **Google Fonts (Poppins):** For enhanced typography.

## Installation

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/<your-github-username>/<your-repo-name>.git
    cd <your-repo-name>
    ```

2. **Set Up a Virtual Environment (Recommended):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate   # On Windows use: venv\Scripts\activate
    ```

3. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## API Key Setup

This application uses the OpenWeatherMap API. You'll need to subscribe and obtain an API key from OpenWeatherMap to use this application:

1. **Sign up for an account at [https://openweathermap.org/](https://openweathermap.org/).**
2. **Get your API key from your OpenWeatherMap account dashboard.**
3. **In the `weather/views.py` file, replace `"YOUR_API_KEY"` in the `weather_search` function with your actual OpenWeatherMap API key:**

    ```python
    api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
    ```

## Usage

1. **Run the Django Development Server:**

    ```bash
    python manage.py runserver
    ```

2. **Open your web browser and go to `http://127.0.0.1:8000/`**

3. **Enter a city name in the search box and click "Search" to get the weather forecast.**

## File Structure

django-weather-forecast/
├── weather/ # Django app for weather functionality
│ ├── migrations/ # Database migration files
│ ├── templates/ # HTML templates
│ │ ├── weather/
│ │ │ ├── error.html
│ │ │ ├── search.html
│ │ │ └── weather_search.html
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py # (empty for this project)
│ ├── tests.py # (Add tests here if you write any)
│ └── views.py
├── your_project_name/ # Main Django project settings
│ ├── init.py
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md