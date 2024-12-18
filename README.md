# **Personal Trainer Assistant with OpenAI API**

This project demonstrates how to interact with the OpenAI API to create a custom assistant for fitness and nutrition advice. The assistant can respond to user queries in a personalized and conversational manner.

---

## **Features**

- **Assistant Creation**: Customize an AI assistant with a name, instructions, and a model.
- **Thread Management**: Create threads to maintain conversation context.
- **Message Handling**: Send and retrieve messages in an ongoing thread.
- **Run Monitoring**: Monitor the completion status of a run and log responses.
- **Detailed Logging**: Track execution and response details with clear logs.

---

## **Setup Instructions**

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-name> 
   ```
2. **Install Required Packages**: Ensure    Python 3.8+ is installed. Then, install dependencies:

```bash
    pip install openai python-dotenv 
```
3. **Set Your OpenAI API Key**:
- **Create a .env file in the project root.**
- **Add your OpenAI API key:**
```
OPENAI_API_KEY=your-api-key
```
4. **Run the Script**:
```
python main.py
```
