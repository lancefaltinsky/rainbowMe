![RAINBOWME](https://i.imgur.com/QnmXPtB.png)
# rainbow me
A short and simple text rainbowifier CLI for Discord chats

## Why
For centuries (ok not literally), Discord chats have been lackluster of a specific type of pizzazz. Then Discord rolled out support for ANSI formatting. But the general public does not use it, and most people don't know what that even is. Thus, I make a simple CLI for generating some epic rainbow text you can paste right into Discord, in seconds.

## Discord mobile woes
At the moment of writing this readme, Discord mobile does NOT support ANSI formatting. This cannot be fixed by anyone other than Discord themselves. Users on mobile will see all of the formatting characters and will think that you're having a stroke.

## Discord limits
It appears that ANSI outputs over 1000 characters will not display in Discord. You will be warned when this happens, and you will notice it when Discord does not generate a proper preview of the ANSI when you paste the code.  

## Usage  
First install requirements, `pip install pyperclip`, or `pip install -r requirements.txt`. Then you are good to go!  
`python rainbowme.py hello world!`  
Or if you want to specify a background color:  
`python rainbowme.py hello world! -bg white`  
Or if you want to specify a style for the text:  
`python rainbowme.py hello world! -style underline`  
You can even add all that together too:  
`python rainbowme.py hello world! -bg white -style underline`  
  
After running the command, everything will be copied to your clipboard, in a format that is in a Discord codeblock. So you can just ctrl+v once and send your message, no need to make your own codeblock!  
