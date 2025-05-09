import requests
from bs4 import BeautifulSoup


def download_file():
    print("start")


def login_ip2location():
    
    # Create a session
    session = requests.Session()

    # Define the login URL and your credentials
    login_url = 'https://lite.ip2location.com/log-in'
    payload = {
        'username': '',
        'password': ''  
    }

    # Send a POST request to log in
    response = session.post(login_url, data=payload)

    # Check if login was successful
    if response.ok:
        print("Login successful!")
        # You can now use `session` to make further requests
    else:
        print("Login failed!")

    # Example of accessing a protected page after login
    protected_url = 'https://lite.ip2location.com/database-download'  # Replace with the actual URL
    protected_response = session.get(protected_url)

    if protected_response.ok:
        print("Accessed protected page!")
        print(protected_response.text)  # Print the content of the protected page
    else:
        print("Failed to access protected page.")

if __name__ == "__main__":
    login_ip2location()



