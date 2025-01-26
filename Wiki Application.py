import requests
from bs4 import BeautifulSoup

domains = [
    "Machine_Learning",
    "Data_Science",
    "Artificial_Intelligence",
    "Deep_Learning",
    "Neural_Network",
    "Natural_Language_Processing",
    "Computer_Vision",
    "Data_Mining",
    "Big_Data",
    "Statistics",
    "Predictive_Analytics",
    "Reinforcement_Learning",
    "Supervised_Learning",
    "Unsupervised_Learning",
    "Feature_Engineering"
]


def data(page):
    page_url = page.replace(' ', '_')
    print(page_url)
    url = 'https://en.wikipedia.org/wiki/'
    full_url = url+page_url
    print(full_url)
    response = requests.get(full_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    info = soup.find('p')
    if info and not info.text.strip():
        info = info.find_next('p')
    if info:
        high_lights = [i.text.strip() for i in info]
        for high_light in high_lights:
            print(high_light, end = ' ')
    else:
        print(f"No headlines found for {page}. The content might be loaded dynamically.")
    return

def StartChat(name):
    print(f"Hii {name}, Welcome to mini Wiki Application.")
    print("\n")
    for domain in domains:
        print(domain, end = ', ')
    que = input("\n\nAsk Any Question ('End' to end the chat): ").capitalize()
    while que != 'End':
        data(que)
        print("\n\n")
        for domain in domains:
            print(domain, end = ', ')
        que = input("\n\nAsk Any Question. ('End' to end the Chat): ").capitalize()
    print("ThankYou Visit Again.")
    return

if __name__ == '__main__':
    name = input("Enter Your Name: ").title()
    query = input('Do You want to start the chat Yes/No\n').lower()
    if query == 'yes':
        StartChat(name)
    else:
        print('Thankyou {name}')
