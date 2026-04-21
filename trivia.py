import requests
import random
import html

# Category 9 is General Knowledge
# We add 'amount=5' to specify how many questions to fetch
API_URL = "https://opentdb.com/api.php?amount=5&category=9&type=multiple"

def get_education_questions():
    try:
        response = requests.get(API_URL)
        data = response.json()
        
        # OpenTDB returns a response_code; 0 means success
        if data['response_code'] == 0:
            return data['results']
        else:
            return []
    except Exception as e:
        print(f"Error fetching data: {e}")
        return []

def run_quiz():
    questions = get_education_questions()
    
    if not questions:
        print("Failed to fetch educational questions.")
        return
        
    score = 0
    print("--- Welcome to the Education Quiz! ---\n")
    
    for i, q in enumerate(questions, 1):
        # Use html.unescape to fix entities like &quot; or &#039;
        question_text = html.unescape(q['question'])
        correct_answer = html.unescape(q['correct_answer'])
        options = [html.unescape(opt) for opt in q['incorrect_answers']]
        
        # Add the correct answer and shuffle so it's not always in the same spot
        options.append(correct_answer)
        random.shuffle(options)
        
        print(f"Question {i}: {question_text}")
        for idx, opt in enumerate(options, 1):
            print(f"  {idx}. {opt}")
            
        try:
            user_choice = int(input("\nYour answer (number): "))
            if options[user_choice - 1] == correct_answer:
                print("Correct! ✨")
                score += 1
            else:
                print(f"Wrong! The correct answer was: {correct_answer}")
        except (ValueError, IndexError):
            print("Invalid input. Skipping question.")
            
        print("-" * 30)

    print(f"\nQuiz Finished! Your final score: {score}/{len(questions)}")

if __name__ == "__main__":
    run_quiz()
