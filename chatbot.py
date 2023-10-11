import openai

# Replace with your OpenAI API key
api_key = "sk-qpdvzMLJ8lK6QiXj9yUUJ2A0yuZ6NKHuqaEJL1OqFGG5EvyW"

# Function to create a CICD pipeline
def create_cicd_pipeline():
    # Initialize the OpenAI API client
    openai.api_key = api_key

    # Welcome message
    user_input = input("Welcome to the CICD Pipeline Chatbot! Which technology do you want to create a pipeline for? ")

    # Initialize pipeline stages based on user's choice
    if user_input.lower() in ["java", "python", "go", "react", "dot net", "node js"]:
        pipeline_stages = input(f"Great! You chose {user_input}. Now, please specify the stages you need in the pipeline: ")

        # Generate pipeline configuration using ChatGPT
        response = openai.Completion.create(
            engine="davinci",
            prompt=f"Create a Groovy-based CICD pipeline for {user_input} with the following stages: {pipeline_stages}",
            max_tokens=100
        )

        # Display the generated pipeline configuration
        print("Here is your CICD pipeline configuration:")
        print(response.choices[0].text)
    else:
        print("Sorry, we currently don't support CICD pipelines for that technology.")

if __name__ == "__main__":
    create_cicd_pipeline()