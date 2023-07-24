import requests
import os
save_directory = input("Enter where the attachments should be downloaded: ")

with open('links.txt', 'r') as file:
    links = [line.strip() for line in file.readlines()]
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
        for char in filename[len(filename) -2]:
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
