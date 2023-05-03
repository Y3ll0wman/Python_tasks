from datetime import datetime

import requests
from colorama import Fore, init

init(autoreset=True)


def ask():
    question = input(Fore.YELLOW + 'Введите запрос\n')
    while question != 'quit_plz':
        api_endpoint = "https://api.openai.com/v1/completions"
        api_key = '******************************************'
        current_time = datetime.now().strftime('%Y-%m-%d%H-%M-%S')

        request_headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + api_key
        }

        request_data = {
            "model": "text-davinci-003",
            "prompt": f"{question}",
            "max_tokens": 500,
            "temperature": 0.5
        }

        response = requests.post(api_endpoint, headers=request_headers, json=request_data)
        if response.status_code == 200:
            response_text = response.json()["choices"][0]["text"]
            with open('history.txt', "a+") as file:
                file.write(f'{current_time}: \n'f'{question}\n{response_text}\n\n\n')
            print(Fore.GREEN + response_text)

            question = input(Fore.YELLOW + 'Введите запрос\n')

        else:
            response_as_dict = response.json()
            print(Fore.RED + f"Request failed with status code: {str(response.status_code)}\n"
                             f"{response_as_dict['error']['message']}")
            question = input(Fore.YELLOW + 'Введите запрос\n')


ask()
