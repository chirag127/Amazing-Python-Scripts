import urllib.request


def check_website_status():
    prompt = "Enter the Website URL:  "
    while True:
        url = str(input(prompt))  # prompt
        if not url.startswith('https://') and not url.startswith('http://'):
            url = f'https://{url}'
        try:
            headers = {
                'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \\\x1f            (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
            }

            req = urllib.request.Request(url, headers=headers)
            page = urllib.request.urlopen(req)
            code = str(page.getcode())
            print(f'The website {url} has returned a {code} code')
            break
        except Exception as e:
            print(e)
            print("Make sure you are entering a valid URL")
            try_again = input("Do you want to try again (y/n): ")
            try_again = try_again.lower()
            if try_again == 'y':
                continue
            else:
                break


check_website_status()
