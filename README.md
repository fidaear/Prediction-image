
# Django Image Classification Demo

![Demo Screenshot](media/screenshot.png) <!-- Add a screenshot if available -->

A simple Django web application that demonstrates image classification (Cat vs Dog) with mock confidence percentages.

## Features

- Upload images through a web interface
- Displays mock classification results (Cat or Dog)
- Shows confidence percentage (always high values for demo purposes)
- Presents the uploaded image alongside results
- No machine learning required - simple demo implementation

## Prerequisites

- Python 3.6+
- Django 3.0+
- Pillow (for image handling)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/django-image-classification-demo.git
   cd django-image-classification-demo
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install django pillow
   ```

4. Set up the database:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser (optional for admin access):
   ```bash
   python manage.py createsuperuser
   ```

## Configuration

1. Add your secret key to `settings.py`:
   ```python
   SECRET_KEY = 'your-secret-key-here'
   ```

2. Configure media settings in `settings.py`:
   ```python
   MEDIA_URL = '/media/'
   MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
   ```

## Running the Application

1. Start the development server:
   ```bash
   python manage.py runserver
   ```

2. Access the application at:
   ```
   http://localhost:8000/predict/
   ```

3. (Optional) Access the admin interface at:
   ```
   http://localhost:8000/admin/
   ```

## Project Structure

```
django-image-classification-demo/
├── ml_app/                  # Main application
│   ├── migrations/          # Database migrations
│   ├── templates/           # HTML templates
│   ├── __init__.py
│   ├── admin.py             # Admin configuration
│   ├── apps.py              # App configuration
│   ├── models.py            # Database models
│   ├── tests.py             # Test cases
│   ├── urls.py              # URL routing
│   └── views.py             # View functions
├── media/                   # Uploaded files
├── django_image_classification_demo/  # Project settings
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py          # Project settings
│   ├── urls.py              # Main URLs
│   └── wsgi.py
├── manage.py                # Django management script
└── README.md                # This file
```

## How It Works

1. Users upload an image through the web interface
2. The system generates a mock classification result:
   - Randomly selects "Cat" or "Dog"
   - Always shows high confidence (90-99%)
3. Displays the uploaded image with the mock results
4. No actual image analysis is performed - this is purely for demonstration purposes

## Customization

To modify the behavior:

1. Change the fixed confidence percentage in `ml_app/views.py`
2. Adjust the mock classification logic in the `predict` view
3. Modify the template in `ml_app/templates/ml_app/predict.html`

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Django framework
- Pillow for image handling
```

### Key Notes:

1. Replace placeholder values (like GitHub URL, secret key) with your actual information
2. Add a screenshot if available (place in `media/screenshot.png`)
3. Adjust the license if you're using something other than MIT
4. Update the "Acknowledgments" section with any additional credits

Would you like me to modify any section or add more details about specific parts of the project?
