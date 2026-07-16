from groq import generate_response

def bias_mitigation_activity() :
    print('\n=== Bias Mitigation===\n')
    prompt = input('Enter a bias to start the activity(eg. Describe an ideal doctor)').strip()

    if not prompt :
        print("Please enter a prompt to run the activity : ")
        return
    
    initial_response = generate_response(prompt,temperatur=0.3,max_tokens=1024)
    print (f"\nInitial response : {initial_response}")

    modified_prompt = input('Modify the prompt t make it more natural').strip()
    if modified_prompt :
        modified_response = generate_response(modified_prompt, temperature=0.3,max_tokes=1024)
        print(f'Modified response (neutral) {modified_response}')

    else:
        print('No modified promptentered. Skipping neutral response')

def token_limit_activity():
    print("\n=== TOKEN LIMIT ACTIVITY ===\n")
    long_prompt = input(
        "Enter a long prompt (more than 300 words, e.g., a detailed story or description): "
    ).strip()

    if long_prompt:
        long_response = generate_response(long_prompt, temperature=0.3, max_tokens=1024)
        preveiw = (long_response[500:]+'...') if len(long_response) > 500 else long_response
        print (f'\nResponse to long response : {preveiw}')

    else :
        print('No long prompt entered. Skipping long prompt response')
    
    short_prompt = input('Enter a  short more condensed prompt').strip()
    if  short_prompt :
        short_response = generate_response(short_prompt, temperature=0.3,max_tokens=1024)
        print(f"\n Response to short prompt : {short_response}")

    else:
        print('NO condensed prompt enterded. Skipping short response')

def run_activity():
    print("\n=== AI Learning Activity ===")
    print("Choose an activity:")
    print("1) Bias Mitigation")
    print("2) Token Limits")
    choice = input("> ").strip()

    if choice == "1":
        bias_mitigation_activity()
    elif choice == "2":
        token_limit_activity()
    else:
        print("Invalid choice. Please choose 1 or 2.")

if __name__ == "__main__":
    run_activity()
