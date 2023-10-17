# Blood Donor Website

Welcome to the Blood Donor Website! This website is designed to facilitate blood donation and connect donors with those in need. It is built using Django, HTML, CSS, Bootstrap, AJAX, jQuery, and JavaScript to provide a responsive and user-friendly experience.

## Features

- **User Registration and Login**: Users can register for an account, log in, and manage their profiles.

- **Blood Donor Profiles**: Donors can create profiles with their personal information, including blood type and contact details.

- **Search Donors**: Search for donors based on blood type, location, and other criteria.

- **Request Blood**: Individuals in need can send blood requests to donors based on their criteria.

- **Interactive UI**: The website has a clean and interactive user interface thanks to Bootstrap, AJAX, and jQuery.

## Installation

Follow these steps to set up the project on your local development environment:

1. Clone the repository:

   ```bash
https://github.com/ATIF176/Donor.git
   cd blood-donor-website
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

4. Install the project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Migrate the database:

   ```bash
   python manage.py migrate
   ```

6. Create a superuser to access the admin panel:

   ```bash
   python manage.py createsuperuser
   ```

7. Start the development server:

   ```bash
   python manage.py runserver
   ```

8. Access the website in your web browser at `http://127.0.0.1:8000/`.

## Usage

- Navigate to the website in your web browser.

- Register for an account or log in if you have one.

- Create your donor profile with your personal information and blood type.

- Use the search feature to find donors or request blood based on your criteria.

- Interact with the website to facilitate blood donation and requests.

## Contributing

We welcome contributions from the community. To contribute to the project, follow these steps:

1. Fork the repository on GitHub.

2. Clone your forked repository to your local development environment.

3. Create a new branch for your feature or bug fix.

4. Make your changes and commit them.

5. Push your changes to your GitHub fork.

6. Submit a pull request to the main repository.

We appreciate your contributions and will review your pull request as soon as possible.

## License

This project is open-source and available under the [MIT License](LICENSE). You are free to use, modify, and distribute it according to the terms of the license.

## Contact

If you have any questions or need assistance, feel free to contact us at dillawar612@gmail.com.

---

Thank you for using the Blood Donor Website. We hope it serves its purpose of connecting donors with those in need and contributes to a noble cause.
