# Discord_Channel_Attachment_Downloader
Downloads attachments from a specified server on discord. Attachments include all files that were uploaded to a discord server.
All the dependencies have already been included. To run the script, use a terminal window to navigate to the location of 
the link_grabber.py. 

Once this .py file is executed, you input the location of where the attachments should be downloaded. Afterwards, a 
Microsoft Edge window being automated by selenium will open and you will have 45 seconds to log into discord and
navigate to the discord channel/dm where you want the attachments to be downloaded from. 

Once you navigate to the channel/DM, you must left click within the messages window (where all the messages are displayed). 
See example.png for where to click (within the white box outlined in the image). 

Soon the selenium window will start scrolling throught the chatbox. You can minimize the browser window during this process.
Once it reaches the top of the chatbox, the browser window will close. 

Since downloading all the attachments takes a long time and scrolling through the entire chatbox may take an even longer time,
all the download links get saved to a .txt file called 'links.txt'. This way, if the links.txt file is created, you can run
the link_downloader.py to commence the downloads immediately and avoid having to scroll through the chatbox again. 

Either way, the link_grabber.py will grab all the download links and download them. But if you don't have enough time to
grab all the links and download them, the links can just be grabbed and get stored in that .txt file and then be downloaded
from the link_grabber.py. 
