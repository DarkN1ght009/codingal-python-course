from groq import generate_response

def reinforecement_learning_activity():
    print('\n=== Renforcement Learnig===\n')
    prompt = input('Enter a prompt for the ai model.eg describe a lion').strip()
    if not prompt :
        print('Please enter a valid prompt to run the activity')
        return
    
    initial_response = generate_response(prompt, temperatur=0.3, max_tokens=1024)
    print (f'\n Initial Ai response: {initial_response}')
    try:
       rating = int(input('Enter a rating from 1(bad) to 5 (good)').strip())
       if rating < 1 or rating > 5 :
          print ('Invalid rating. using 3')
          rating = 3
    except ValueError :
       print ('Invalid rating. using 3')
       rating = 3
       feedback = input('Provide feed back for improvement').strip()
       improved_response = f'{initial_response}(improved using your feedback : {feedback})'
       print (f'\nImproved AI response : {improved_response}')
       print ('\nReflection : ')
       print("1. How did the AI's response improve with your feedback." )
       print("2. How does renforcement learning help Ai to imporve its performance over time")

def role_based_prompt_activity():
    print("\n=== ROLE-BASED PROMPTS ACTIVITY ===\n")
    category = input("Enter a category (e.g., science, history, math): ").strip()
    item = input(f"Enter a specific {category} topic (e.g., 'photosynthesis' for science): ").strip()

    if not category or not item:
        print("Please fill in both fields to run the activity.")
        return

    teacher_prompt = f"You are a teacher. Explain {item} in simple terms."
    expert_prompt = f"You are an expert in {category}. Explain {item} in a detailed, technical manner."

    teacher_response = generate_response(teacher_prompt, temprature=0.3, max_tokens=1024)
    expert_response = generate_response(expert_prompt, temprature=0.3, max_tokens=1024)
    print(f"\n--- Teacher's Perspective ---\n{teacher_response}")
    print(f"\n--- Expert's Perspective ---\n{expert_response}")

    print("\nReflection:")
    print("1. How did the AI's response differ between the teacher's and expert's perspectives?")
    print("2. How can role-based prompts help tailor AI responses for different contexts?")

def run_activity() :
    print('AI learning')
    print ('Choose an activity')
    print('1) Renforcement Learning')
    print('2) Role Based Learning')

    choice = input('>').strip()

    if choice == "1":
      reinforecement_learning_activity()
    elif choice == "2":
      role_based_prompt_activity()
    else:
      print("Invalid choice. Please choose 1 or 2.")

if __name__ == "__main__":
    run_activity()



