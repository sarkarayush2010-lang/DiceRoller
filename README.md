Dice Roller
---
## Description
Created by me!  
Have you ever wanted to play a game and realized that you were missing your dice? Now how are you supposed to beat your sister in monopoly?  
Well, that's no problem anymore! Just pull up the Dice Roller website and get to playing! Made for desktops AND phones!  
It's never been easier and cleaner to roll dice. just set the amount of dice and the number of sides based on either my presets OR make your own with the easy-to-use sliders.  
Made with Flask and Bootstrap along with CSS and Javascript (new skill aquired for me!), this project is simple and reliable.  

This project was created for Hack Club's Horizons Event!
---

## Features
* **Game Presets:** Classic presets for popular games! Every preset can be adjusted later on with the custom control sliders
* **Custom Control Sliders:** Allows the user to adjust the amount of dice from 1 to 6 dice, and 2 to 20 sides per die. This allows it to be used for literally every single game.
* **Graphic Dice Faces:** using creative commons images i borrowed off the web, displays rolls of numbers 1-6 nicely, and shows the actual number for numbers 7-20, for easy readability.
* **Split-Sreen Layout:** Stacks vertically on mobile and side-by side on desktop. This took me way to long to figure out but I haven't had errors with it!
* **Styling aproved by my dad:** Green and brown fit popular gaming rooms like a pool table - having the app propped open on a tablet/phone fits in perfectly with the game vibe!


---
## Screenshots
<img width="2559" height="1350" alt="image" src="https://github.com/user-attachments/assets/47b5d300-a4f3-4a11-9649-560b114ee73c" />
Main Desktop layout  
<img width="1165" height="734" alt="image" src="https://github.com/user-attachments/assets/9b41aeef-edb4-4f8d-aaab-c474da57ed31" />
Presets  
<img width="2209" height="710" alt="image" src="https://github.com/user-attachments/assets/0a6f85dc-39e0-4cae-9878-ded6e496dc44" />
Example  
<img width="499" height="843" alt="image" src="https://github.com/user-attachments/assets/f109fae0-c7b6-45ef-aa13-797197af9619" />
Mobile Layout


---
## Tech Stack

Uses two files for the main program, app.py and rollmultiple.html.
app.py handles flask management of commands sent by rollmultiple.html. It generates random numbers and sends it back.
rollmultiple.html has 3 main parts. Theres HTML code for the overall structure of the website. Towards the top there is CSS code for the styling of the page. Towards the bottom is a Javascript script, that handles the interactive portions of the site.

```text
📁 DiceRoller/
│
├── 📁 templates/
│   └── rollmultiple.html         # Main Bootstrap UI with custom CSS and JavaScript Styling and functions. runs frontend
│
├── app.py                # Flask server that handles /roll rng command. Backend
├── requirements.txt      # Needed to deploy python app through vercel
└── vercel.json           # Vercel Configuration

```
---
## Motivation

I was motivated to do this when I saw my siblings playing monopoly and they kept scrambling for the dice. I also needed to code some websites...  
then i came up with the amazing idea of doing something that totally isn't built into google and i didn't know until halfway through the project...

---
## How it works
Yeah, you don't even need this part, its soo intuitive!  
All you do is click on the game presets and select what preset you want! Options exist for 2 dice with 6 sides, 1 dice with 8 sides, and 4 dice with 6 sides.  
Need anything more than that?  
Just use the sliders underneath to choose whatever amount of sides and dice count that you want!  
  
Ready? Now click "!!!!!ROLL!!!!!"  
  
The dice on the left(Desktop) or top (Mobile) will spin and settle on some values. The standard dots are there for numbers 1-6 and larger numbers print themselves straight up!  
  
Thats it!  

---
## AI use and Other Resource things
I'm extremely proud to say THIS ISNT AI SLOP (lets go)
As a lot of this was new to me (only knew basic html,css, and python) So i had to search up how to add a lot of things.    
I used w3 schools to learn a lot of the content, and searched some other things up (does google's AI mode count reaaallly count as AI usage?)    
The images that I used are from needpix.com and have a creative commons license.  
the only time I used actual generative ai (gemini) was for uploading the project to vercel as I couldn't figure that out  
and no this readme isnt ai generated

