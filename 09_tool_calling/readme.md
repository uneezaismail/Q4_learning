# Function Calling & Tool Calling

## What is Function Calling?

Function Calling is a feature where the AI model can call predefined functions in your code to fetch real-time data or perform specific actions, instead of just generating text responses.

For example, instead of guessing the weather, the model can call your `get_weather` function that fetches the current temperature from a real API.

---

## What is Tool Calling?

Tool Calling is another name for Function Calling. It means the AI can “use tools” (functions or APIs you provide) to get accurate information or complete tasks for users dynamically.

---

## Difference Between Function Calling and Tool Calling

- **Function Calling:**  
  This is when the AI model calls specific backend functions you define in your code to get data or perform actions. These are usually small, focused pieces of code designed to handle a particular task (like getting weather info).

- **Tool Calling:**  
  This is a broader term that means the AI can use any external tool, API, or function it has access to. A "tool" can be a function, an external API, or any service that helps the model perform tasks beyond text generation.

**In short:**  
Function Calling is a specific type of Tool Calling where the “tool” is a function you define. Tool Calling can include functions but also other external services or APIs.

---

## Why Do We Use Function/Tool Calling?

- **Get Accurate, Real-Time Data:**  
  The AI can access live information (like weather, stocks, or news) instead of guessing or relying on outdated knowledge.

- **Perform Actions Automatically:**  
  It can trigger tasks such as sending emails, making bookings, or updating databases without manual intervention.

- **Enhance User Experience:**  
  Creates interactive and dynamic apps where AI helps users by connecting to external services.

- **Keep Responses Relevant:**  
  By using actual functions and APIs, the AI’s answers are more reliable and trustworthy.

- **Build Smarter Applications:**  
  Combines AI’s language abilities with backend logic and external tools to solve real-world problems.

---

## Common Use Cases

- **Weather Information:**  
  Get live weather updates by calling a weather API function.

- **Booking and Reservations:**  
  Make hotel, flight, or restaurant bookings directly through API calls.

- **E-commerce Actions:**  
  Check product availability, create orders, or update inventory using backend functions.

- **Data Retrieval:**  
  Fetch stock prices, news headlines, or sports scores in real-time.

- **Customer Support:**  
  Automate ticket creation, status checks, or FAQ lookups by calling support system APIs.

- **Home Automation:**  
  Control smart devices like lights, thermostats, or security cameras via function calls.

- **Payment Processing:**  
  Initiate payments, refunds, or check transaction status through payment gateway APIs.

---

## Function Calling Steps

1. **Define your function (tool):**  
   Tell the model what function it can call, with details about the inputs it needs.

2. **Call the model with your function defined:**  
   Send the user’s message along with the list of available functions to the model.

3. **Model decides to call your function:**  
   The model responds with which function to call and what arguments to use.

4. **Run the function in your code:**  
   Use the function name and arguments from the model to get the actual result.

5. **Send the result back to the model:**  
   Give the function output back to the model to create the final answer.

---

## Streaming in Tool Calling

Streaming allows the AI model to send its response incrementally, so your application receives the output in small parts as they are generated, rather than waiting for the complete response.

When combined with tool calling, streaming enables:

- **Faster response times:** Users see replies and updates sooner.
- **Real-time updates:** Partial results from function calls can be displayed immediately.
- **Improved user experience:** Especially useful for long or complex outputs, or when functions take time to return data.

This makes the interaction feel more dynamic and responsive by delivering information progressively.


### How Streaming Works Technically (Simple)

- You send a request to the AI model with functions (tools) defined.
- The model starts streaming back a response chunk by chunk.
- If the model decides to call a function, it sends a function call message.
- Your backend executes the function, which might also stream data.
- The AI resumes streaming output to the user as the function results come in.

This process allows for a smooth, real-time interaction between the user, the AI model, and your backend functions.

---

For a full example and code, see the official OpenAI docs here:  
[OpenAI Function Calling Example](https://platform.openai.com/docs/guides/gpt/function-calling)