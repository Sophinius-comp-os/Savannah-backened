# Savannah Backend Project

## Overview

The Savannah Backend Project is a Django-based backend application providing order management, customer handling, and SMS notification services. It leverages the Django REST Framework (DRF) for API management, integrates OAuth2 authentication via Google, and is designed with security, scalability, and ease of maintenance in mind. The project also includes continuous integration (CI) capabilities and comprehensive unit testing to ensure reliability.

**Table of Contents**

- [Savannah Backend Project](#savannah-backend-project)
  - [Overview](#overview)
  - [Setup](#setup)
  - [Running Tests](#running-tests)
  - [API Overview](#api-overview)
  - [Security](#security)
    - [Cross-Site Scripting (XSS)](#cross-site-scripting-xss)
    - [OAuth2 Security and OpenID Connect](#oauth2-security-and-openid-connect)
  - [Phone Number Validation](#phone-number-validation)
  - [CI/CD Pipeline](#cicd-pipeline)
  - [Deployment](#deployment)
  - [Environment Variables](#environment-variables)
  - [Future Enhancements](#future-enhancements)

## Setup

To set up the project locally, the following steps should be completed:

1. Clone the repository and install necessary dependencies.
2. Configure the environment variables (detailed in the "Environment Variables" section).
3. Apply the necessary database migrations and launch the development server.

This setup will enable the developer to run the application locally for testing and further development.

## Running Tests

The project includes unit tests for core functionality, focusing on the orders and customers within the orders app. Tests have been implemented for models, views, and serializers.

The test suite can be run through standard Django commands, and the CI/CD pipeline will automatically execute these tests upon each push to the repository.

Additional testing, such as integration, end-to-end, and load testing, can be implemented using tools such as Postman and Locust to ensure the system performs well under higher loads and that full workflows function as expected.

## API Overview

The Savannah Backend exposes a REST API using Django REST Framework (DRF) to handle customer and order management.

**API Features:**

- Endpoints for managing orders and customers (CRUD operations).
- Robust error handling and validation to ensure data integrity.
- Pagination support for large datasets to improve performance and user experience.

While the API is functional, rate limiting has not yet been implemented to prevent abuse and will be considered in future iterations.

## Security

### Cross-Site Scripting (XSS)

Django’s built-in mechanisms automatically handle XSS protection by escaping input data in templates. This ensures that user-submitted data is sanitized before being rendered in the application. Custom JavaScript or templates must also be reviewed to ensure manual escape handling is applied where necessary.

### OAuth2 Security and OpenID Connect

OAuth2 is used for user authentication, with Google serving as the provider. The underlying OAuth2 flow, similar to OpenID Connect, works by securely authenticating users and issuing tokens for secure API access.

**OpenID Connect Workflow**:

1. The client application redirects the user to an OpenID Provider (OP) for authentication.
2. Upon successful authentication, the OP returns authorization tokens.
3. The application uses these tokens to securely access user data from the API.

In this project, Google serves as the OAuth2 provider, offering a similar flow to OpenID Connect, with Google issuing tokens for authentication and secure data access.

## Phone Number Validation

The project ensures that phone numbers are validated and formatted according to international standards. The validation process tests various country formats for robustness, and all phone numbers are standardized using the E.164 format, ensuring global compatibility.

## CI/CD Pipeline

A continuous integration and delivery (CI/CD) pipeline is configured using GitHub Actions. The pipeline performs the following tasks:

- Running tests automatically upon each push to ensure code integrity.
- Verifying that all tests pass successfully before further actions are taken.

Although deployment automation has not yet been implemented, it can be added to the CI/CD pipeline in future releases.

## Deployment

At present, automated deployment has not been integrated into the pipeline. Developers are encouraged to manually test the application in a production environment to verify functionality before deployment.

Future enhancements will include integrating deployment automation into the CI/CD process, ensuring seamless transitions from testing to production environments.

Here's the revised section for the **Environment Variables**, incorporating the additional settings and database configuration:

## Environment Variables

The project relies on several environment variables for configuration. These variables must be set correctly to ensure proper operation of the application.

- **DJANGO_SETTINGS_MODULE**: Specifies the settings configuration for the environment.
- **SECRET_KEY**: The secret key for Django, used to maintain the security of the application.
- **DB_NAME**: The name of the database.
- **DB_USER_NAME**: The username for database access.
- **DB_PASSWORD**: The password for the database user.
- **DB_HOST**: The database host (e.g., IP address or hostname).
- **DB_PORT**: The port on which the database is running.
- **GOOGLE_CLIENT_ID**: Used for Google OAuth2 authentication.
- **GOOGLE_CLIENT_SECRET**: Used for Google OAuth2 authentication.
- **AT_USERNAME**: Africa’s Talking username for SMS services.
- **AT_APIKEY**: Africa’s Talking API key for SMS services.

These environment variables must be configured properly before running the application, either via a `.env` file or directly in the environment settings.

This section now includes both the database configuration and the necessary variables for Google OAuth2 and SMS services.

## Future Enhancements

The following features are planned for future updates to the Savannah Backend:

- **Rate Limiting**: Adding rate limiting to the API to prevent excessive use and potential abuse.
- **Automated Deployment**: Extending the CI/CD pipeline to automate the deployment process.
- 
