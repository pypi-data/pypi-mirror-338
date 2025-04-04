# Python Library to automate tasks with template matching in (non-visible) windows 
heavily inspired by [Botfather](https://botfather.io/)  
uses win32gui -> only works on windows

# Features
* List window titles
* Select window by name/title
    * if multiple found -> choice dialogue
* Taking Screenshots of window
* Use python cv2 wrapper for template matching
* Send mouse/keyboard events to window
* Isolate color ranges for better template matching

# Documentation
* on [GithubPages](https://alpel99.github.io/botpapy/)
* [Example](https://alpel99.github.io/botpapy/#tutorial)

# General
* Some windows don't take input the way this is programmed (new Windows "Apps", Explorer etc.)
* Some windows might not generate any image while minimized:
    * move them to a second desktop in windows `⊞ Win + Tab`
    * keep them "open" there
* If there are only black squares as pictures try a different layer variable for _checkWindowNames_
* This is (not yet) tested on a bigger scale:
    * definitely not full functionality for controls
    * might have bugs
    * performance might not be optimal

# Usage
* `pip install botpapy`
* follow tutorial and documentation
* happy programming