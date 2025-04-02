# Building a LitePolis UI Module with a React Frontend and Automated Deployment

This tutorial will guide you through the process of creating a LitePolis UI module that utilizes a React.js frontend. We'll also demonstrate how to use GitHub Actions to automate the build and publishing process.

## Prerequisites

* Basic understanding of Python and React.js.
* Node.js and npm (or yarn) installed on your development machine.
* A GitHub account.

## Step 1: Setting Up the Project Structure

This template provides the basic structure for your LitePolis UI module. Here's a quick overview of the key files and directories:

* **`setup.py`**: Contains metadata about your Python package.
* **`litepolis_ui_template/`**: This directory will be renamed to your actual package name (e.g., `litepolis_ui_my_awesome_ui`).
    * **`core.py`**: Contains the core logic for serving your UI's static files and defines the `DEFAULT_CONFIG`.
    * **`static/`**: This directory will hold the static files of your React application.
* **`tests/`**: Contains tests for your module.
* **`app/`**: This directory contains the source code for your React.js frontend.
    * **`package.json`**: Defines the dependencies and build scripts for your React app.
    * **`src/`**: Contains the React application's source code (e.g., `index.js`).
    * **`public/`**: Contains the `index.html`.

## Step 2: Developing Your React Frontend

The frontend for this LitePolis UI module is built using React. You can find the source code in the `app/` directory.

* **`app/package.json`**: This file lists the necessary dependencies for your React application, including `react`, `react-dom`, and `react-scripts`. It also defines the `start` and `build` scripts.
* **`app/src/index.js`**: This is the entry point for your React application. In this example, it renders a simple "Hello, world" message.

You can develop your React application as you normally would within the `app/` directory. To start a development server (if needed), you can navigate to the `app/` directory in your terminal and run:

```bash
cd app
npm start
```

## Step 3: Building Your React Frontend for Production

Before deploying your LitePolis UI module, you need to build your React application into static files. To do this, navigate to the `app/` directory in your terminal and run:

```bash
cd app
npm run build
```

## Step 4: Integrating the React Frontend into the LitePolis UI Module

Now, you need to integrate the built React application into your LitePolis UI module so that it can be served.

1.  **Copy the `build` directory contents:** After running `npm run build` in the `app/` directory, copy the entire contents of the `app/build` directory into the `litepolis_ui_template/static/` directory (or your renamed package's `static/` directory).

    Your directory structure should now look something like this:

    ```
    litepolis-ui-my-awesome-ui/
    ├── litepolis_ui_my_awesome_ui/
    │   ├── core.py
    │   └── static/
    │       ├── index.html
    │       ├── asset-manifest.json
    │       ├── favicon.ico
    │       ├── robots.txt
    │       ├── static/
    │       │   ├── css/
    │       │   └── js/
    │       └── ... (other built assets)
    ├── app/
    │   ├── ...
    ├── tests/
    │   └── test_core.py
    └── setup.py
    ```

2.  **Ensure `core.py` is configured to serve static files:** The `core.py` file in your package should already be set up to serve static files from the `static/` directory. Verify that it looks similar to this:

    ```python
    from fastapi import FastAPI
    from fastapi.staticfiles import StaticFiles

    app = FastAPI()
    app.mount("/static", StaticFiles(directory="static"), name="static")
    ```

## Step 5: Configuring Your Python Package (`setup.py`)

Make sure to update the `setup.py` file with the correct information for your UI module, including the `name` (remember the `litepolis-ui-` prefix), `version`, `description`, etc.

## Step 6: Automating Build and Publish with GitHub Actions

This template includes a GitHub Actions workflow (`python-publish.yml`) to automate the process of building your React application and publishing your LitePolis UI module to PyPI when you create a new release on GitHub.

* **`name: Build`**: Navigates to the `app/` directory and builds the React app using `npm run build`. The output will be in the `app/build` directory we will move it to `<litepolis_package_name>/static`.

By following these steps, you can effectively build a LitePolis UI module with a React frontend and leverage GitHub Actions for automated build and deployment. Remember to replace placeholders with your actual project details.