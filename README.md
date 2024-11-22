# My Flask App

```text
Author : Orhan Chaushev
Date   : 13.04.2023
```

This is a simple Flask app that provides a "Hello from Python Flask" message at the root URL and a JSON data response at the endpoint `/api/data`.

## Installation

1. Clone this repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Run the app with the command `python app.py`.

## Usage

You can access the app by navigating to the appropriate URLs in your web browser or using a tool like cURL or Postman to send HTTP requests. The available endpoints are:

- `/` - Returns a "Hello, World!" message.
- `/api/data` - Returns a JSON data response containing a name, age, and city.

## Testing

Unit tests are included in the `tests` directory. You can run the tests by executing `python -m unittest discover tests` or `python -m unittest discover -v`

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
