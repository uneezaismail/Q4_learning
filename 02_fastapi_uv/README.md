# 02_fastapi_uv

##  Project Overview

This project is a simple "Hello World" application built using **FastAPI**. It demonstrates how to set up a basic API using FastAPI and serves as a starting point for further development.

##  Technologies Used

- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python 3.6+.
- **Uvicorn**: A lightning-fast ASGI server used to serve FastAPI apps.
- **uv**: A modern Python packaging and dependency management tool.

##  Installation Instructions

###  Step 1: Clone the Repository

Clone this repository to your local machine and navigate into the directory:

```bash
git clone https://github.com/uneezaismai/02_fastapi_uv.git
cd 02_fastapi_uv
```

### Step 2: Initialize the Project
Use uv init to initialize the project. This will set up the basic structure and configuration for your FastAPI project.

```bash
uv init
```

### Step 3: Create a Virtual Environment (Optional but Recommended)

You can create a virtual environment to isolate the project dependencies. Follow the steps below:

On Windows:
```bash
python -m venv env
.\env\Scripts\activate
```

On MacOS/Linux:
```bash
python -m venv env
source env/bin/activate
```

### Step 4: Install Dependencies

Install FastAPI and Uvicorn:

```bash
uv add fastapi uvicorn
```

## Running the Application

Start the FastAPI server using Uvicorn:

```bash
uvicorn main:app --reload
```

Visit [`http://127.0.0.1:8000/`](http://127.0.0.1:8000/) in your browser to see the API response.
