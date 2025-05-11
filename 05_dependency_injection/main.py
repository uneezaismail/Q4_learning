from fastapi import FastAPI, Depends, Query, HTTPException, status
from typing import Annotated

app = FastAPI()


# 1. Root Route
@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI Dependency Injection example!"}



# 2. Simple Dependency
def get_basic_goal():
    return {"objective": "Creating intelligent AI-driven systems to help humans."}

@app.get("/basic-goal")
def basic_goal(goal_info: Annotated[dict, Depends(get_basic_goal)]):
    return goal_info



# 3. Dependency with Parameters
def get_goal_for_user(user: str):
    return {"objective": "AI is revolutionizing industries.", "user": user}

@app.get("/user-goal")
def goal_for_user(data: Annotated[dict, Depends(get_goal_for_user)]):
    return data



# 4. Dependency with Query Parameters
def validate_login(
    username: str = Query(None), 
    password: str = Query(None)
):
    if username == "admin" and password == "admin":
        return {"status": "Access granted"}
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

@app.get("/login")
def login(auth_status: Annotated[dict, Depends(validate_login)]):
    return auth_status




# 5. Multiple Dependencies
def multiply_by_two(num: int):
    return num * 2


def divide_by_two(num: int):
    return num / 2

@app.get("/compute/{num}")
def compute_result(
    num: int, 
    value_one: Annotated[int, Depends(multiply_by_two)], 
    value_two: Annotated[int, Depends(divide_by_two)]
):
    result = value_one * value_two  
    return {"message": f"Result of the calculation: {result}"}



# 6. CLASSES (Custom Dependency with Error Handling)
articles = {
    "1": "The Future of AI",
    "2": "Exploring Deep Learning",
    "3": "AI in Healthcare"
}

user = {
    "101": "Ali",
    "102": "Alia"
}

class FetchDataOr404:
    def __init__(self, model: dict):
        self.model = model

    def __call__(self, id: str):
        data_item = self.model.get(id)
        if not data_item:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Data with ID '{id}' not found"
            )
        return data_item

article_dependency = FetchDataOr404(articles)
person_dependency = FetchDataOr404(user)

@app.get("/article/{id}")
def get_article(article_title: Annotated[str, Depends(article_dependency)]):
    return {"article": article_title}

@app.get("/person/{id}")
def get_person(person_name: Annotated[str, Depends(person_dependency)]):
    return {"person": person_name}
