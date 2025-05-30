# LITReview Django Project

## Overview
LITReview is a Django-based web application for users to request and share book reviews. Users can create tickets to request critiques and post reviews with star ratings.[](https://github.com/josayko-courses/litreview)

## Features
- Create, edit, and delete review tickets and critiques.
- Display posts with titles, star ratings, and book details (title, author, description, image).
- Responsive UI with centered layout, left-aligned post headers, right-aligned dates, and action buttons.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/devogs/litreview.git
   ```
2. Navigate to the project directory:
   ```bash
   cd litreview
   ```
3. Create a virtual environment:
   ```bash
   python -m venv env
   ```
4. Activate the virtual environment:
   - Windows: `env\Scripts\activate`
   - macOS/Linux: `source env/bin/activate`
5. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
6. Apply migrations:
   ```bash
   python manage.py migrate
   ```
7. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Usage
- Access the app at `http://127.0.0.1:8000`.
- Create tickets to request reviews or post critiques with ratings.
- Edit/delete posts using buttons on the right of each post.
- Posts show titles (1.5em, bold), ratings (★/☆ on same line), and book details.

## Requirements
- Python 3.9+
- Django 3.2+
- Dependencies in `requirements.txt`

