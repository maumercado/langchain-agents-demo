# AI-Powered Business Analytics Tool

This project is an AI-powered business analytics tool that leverages natural language processing to generate SQL queries and create reports based on user prompts. It uses a combination of language models, SQL databases, and HTML report generation to provide insights into business data.

## Project Structure

The project consists of the following main components:

1. `main.py`: The entry point of the application. It now uses the `ChatOpenAI` model from `langchain_openai` and integrates a new `ChatModelStartHandler` for handling chat model start events.
2. `handlers/chat_model_start_handler.py`: Handles the initialization and execution of the chat model. It includes a new `ChatModelStartHandler` class that provides detailed logging of messages exchanged with the AI model.
3. `tools/sql.py`: Contains functions for executing SQL queries and retrieving data from the database.
4. `tools/report.py`: Provides functionality for generating HTML reports based on the query results.
5. `top_5_users_by_revenue.html`: An example HTML report showing the top 5 users by revenue.
6. `top_5_products_by_revenue.html`: An example HTML report showing the top 5 products by revenue.

## How It Works

1. The user provides a natural language prompt asking for specific business insights.
2. The chat model processes the prompt and generates an appropriate SQL query.
3. The SQL query is executed against the database using the functions in `tools/sql.py`.
4. The query results are used to generate an HTML report using the functions in `tools/report.py`.
5. The generated report is saved as an HTML file and can be viewed in a web browser.

## Setup and Installation

1. Ensure you have Python 3.12 or later installed on your system.
2. Clone this repository to your local machine.
3. Create a virtual environment:

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

4. Install the required dependencies:

   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. Activate the virtual environment if not already active:

   ```sh
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

2. Run the main script:

   ```sh
   python main.py
   ```

3. Follow the prompts to input your business analytics questions.
4. The generated reports will be saved as HTML files in the project directory.

## Components in Detail

### main.py

This is the entry point of the application. It sets up the necessary configurations, initializes the chat model using `ChatOpenAI`, and handles user input and output. The script now includes a `ChatModelStartHandler` to log the start of chat model interactions and uses a new method to create the agent with `create_openai_functions_agent`.

### handlers/chat_model_start_handler.py

This module is responsible for initializing and running the chat model. It includes the `ChatModelStartHandler` class, which logs detailed information about the messages exchanged with the AI model, including system, human, AI, and function call messages, using the `boxen` library for formatted output.

### tools/sql.py

This module contains functions for interacting with the SQL database. Key functionalities include:

- Establishing database connections
- Executing SQL queries
- Fetching and processing query results
- Handling any database-related errors or exceptions

### tools/report.py

This module is responsible for generating HTML reports based on the data retrieved from SQL queries. It likely includes functions to:

- Create HTML templates for different types of reports
- Populate the templates with data from SQL query results
- Format and style the reports for easy readability
- Save the generated reports as HTML files

### HTML Report Files

The project includes example HTML report files:

- `top_5_users_by_revenue.html`: Shows a report of the top 5 users by revenue.
- `top_5_products_by_revenue.html`: Displays a report of the top 5 products by revenue.

These files serve as examples of the types of reports the tool can generate.

## Customization

To customize the tool for your specific business needs:

1. Modify the SQL queries in `tools/sql.py` to match your database schema.
2. Adjust the report templates in `tools/report.py` to fit your desired output format.
3. Update the chat model prompts in `handlers/chat_model_start_handler.py` to better suit your business domain.

## Troubleshooting

If you encounter any issues:

1. Ensure all dependencies are correctly installed.
2. Check that your database connection settings are correct.
3. Verify that the input prompts are clear and related to the available data.
4. Review the console output for any error messages or logs.

## Contributing

Contributions to this project are welcome. Please fork the repository, make your changes, and submit a pull request with a clear description of your modifications.

## License

[Specify the license under which this project is released, e.g., MIT, Apache 2.0, etc.]
