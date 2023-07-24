from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import os
import time


# prerequisites
# - get the location that the user wants to download the attachments to
# - open webdriver and go to discord
# - wait 45 seconds to allow the user to log in and navigate to the discord channel they want to go to
print("""Welcome!\n
After you input the download directory, a Microsoft Edge window will open automatically to discord.
From there, you will have 45 seconds to login and navigate to the channel you want to download the
attachments from. Once you navigate to the channel, make sure you click anywhere in the chat box!\n""")
download_directory = input("Enter where the attachments should be downloaded: ")
driver = webdriver.Edge()
driver.get('https://discord.com/login')
time.sleep(45)
actions = ActionChains(driver)
previous_elements = ''
links = []

# find all links on the page.
# stops when the chat box is at the very top and no more links are being loaded in
while True:
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')
    all_elements = soup.find_all()
    if previous_elements == all_elements:
        break

    for link in soup.find_all('a'):
        links.append(link.get('href'))
        links.append(link.get('src'))

    previous_elements = all_elements

    actions.send_keys(Keys.HOME).perform()

    time.sleep(1)
links = [x for x in links if x is not None and x.__contains__('attachment')]
# remove duplicate links:
links = [x for i, x in enumerate(links) if x not in links[:i]]

driver.close()

# write the links to a text file:
links2 = '\n'.join(links)
with open('links.txt', 'w') as file:
    file.writelines(links2)

# begin downloading the links:

save_directory = download_directory

save_directory += "\\"
counter = 1
download_names = []
# download all the links
for link in links:
    response = requests.get(link)
    filename = os.path.basename(link)
    # while loop is used to ensure that the file has a unique name and does not overwrite a pre-existing downloaded file
    while filename in download_names:
        filename = filename.split('.')
        new_name = ''
        num_appended = 0
        length = len(filename)
        number = 0
        new_last_group = ''
        numbers_of_group = ''
        for char in filename[len(filename) - 2]:
            if char.isdigit():
                numbers_of_group += char
            else:
                new_last_group += char
        if len(numbers_of_group) == 1:
            number = int(numbers_of_group)
            number += 1
        if len(numbers_of_group) == 0:
            numbers_of_group = 1
        else:
            if len(numbers_of_group) != 1:
                numbers_of_group = numbers_of_group.lstrip('0')
            number = int(numbers_of_group)
        number += 1
        filename[len(filename) - 2] = str(new_last_group + str(number))
        for group in filename:
            new_name += group
            if num_appended == length - 2:
                new_name = new_name + '.'
            num_appended += 1
        filename = new_name
    download_names.append(filename)

    output_path = save_directory + filename
    with open(output_path, 'wb') as file:
        file.write(response.content)
        print('downloaded', filename, 'attachment number: ', counter)
        counter += 1
