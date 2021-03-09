# Anteaters Music Website
Welcome to the Anteaters Music Website! We aim to showcase many functions related to music:
* A login function to access the site
* An in-website clickable piano
* An API to access billboard charts and cleanly display information
* A playlists tab to create playlists of songs
 
 <b>How to Access</b><br />
 * Clicking this [link](http://104.63.252.143/) will take you to the front page of the website.
     * Create an account using the login page first to access the other pages.
     * Set your favorite artist and song in the user page by clicking the "User" button on the navbar (can be changed at any time)
     * View other people's favorite artists and songs by clicking the "Favorites" button on the navbar
     * Filter through the top billboards results by clicking the "Billboards" button on the navbar
     * Compose your own music by clicking the "Piano" button on the navbar
 * Secret hidden [page](http://104.63.252.143/references)... try to find where it is

# College Board Considerations
[Details about meeting college board requirements.](https://docs.google.com/document/d/1BHGhnfDmpjqr5_fmVO78Xak6Nz437NrzB6z_cBR10qA/edit?usp=sharing)
 

# Update 2/18
<b>Suggestions from other team review</b><br />
We recieved these suggestions from the Breakertorts and made sure to work on them.
* "UI: Music grid could look a little more exciting" 
    * Initial grid layout replaced with a more aesthetically pleasing keyboard 
    * All keys functional now, currently working on making them change color/look less squished
* "Modeling: As of right now, your music notes are not local"
    * src links to audio replaced with local mp3 files
* "UI: Login page is a little off-center"
    * Margins for pages have been fixed
    * Still working on overall aesthetics of website
* "Code organization: sessions should probably be located in their own class, not in view.py"
    * Code in view.py re-organized and labeled, deleted unused code

<b>Ticket Updates</b><br />
![snipp](https://user-images.githubusercontent.com/70781122/108482698-abc8a100-724e-11eb-92f0-654bcfd76063.JPG)
* Music grid has been updated to a keyboard [ticket](https://github.com/4DISEASE/anteaters-repo/projects/1#card-54738436)
* Working on implimenting a dropdown that brings up images of sheet music to play
* Favorite music function in progress - querys users and adds them to dictionary [ticket](https://github.com/4DISEASE/anteaters-repo/projects/1#card-55044917)
* Working on updating looks of websit e[ticket](https://github.com/4DISEASE/anteaters-repo/projects/1#card-55257236)

 
# Update 2/5
 <b>API Progress</b><br />
 * API is finished with multiple ways to filter + requests
 * Requires CSS styling to look more aesthetically appealing
 * Aligns with collegeboard topic of sequencing and iterating
 * [Link to ticket](https://github.com/4DISEASE/anteaters-repo/projects/1#card-53798918)
 
 <b>Music Grid Progress</b><br />
 * Grid is interactable with colors 
 * Now features piano note sounds 
 * Covers topic of user action and a procedure
 * [Link to ticket](https://github.com/4DISEASE/anteaters-repo/projects/1#card-53767807)
 
 <b>Logins Progress</b><br />
 * Login function is finished, bugs so far are fixed
 * Database allows for storage of users and later, in-progress music
 * Connects to collegeboard topic of a collection of data that is stored
 * [Link to ticket](https://github.com/4DISEASE/anteaters-repo/projects/1#card-53523712)
 
 
# Project Plan
**College Board “Big Ideas”**

Idea 1 <span style="text-decoration:underline;">(Summary)</span>
*   The idea of our website is based around a music maker through the use of buttons dedicated to musical notes. The user is prompted to sign into an account which allows them to save their music through databases. The user is then able to click buttons that correspond to musical notes, and are able to customize the instrument. 

Idea 2: 
*   SQLAlchemy database will be used for user logins, and creation of playlists/playback of created music
*   Flask will be used to create back end of website, using routes to link to front end html pages
*   POST/GET methods used for user input
    *   Ties into SQLAlchemy for user logins
*   Search bar will be implemented into our playlist system to filter through songs
*   Search bar will be implemented into song - maker system
    *   Users will be able to save multiple songs, and filter through them using a search system for ease of use

Idea 3:
*   We will create a base website with a temporary design to start with
    *   Website will be changed based on research done
    *   At first, website will be skeleton with a working routing system, and blank spaces to be filled with soundboard and music player/playlist

Idea 4:
*   We will use the last two weeks of the project to portforward with a Raspberry Pi server, and implement HTTP into our project

Idea 5: 
*   We plan to use music/sounds from online sources
    *   Links and proper credit will be used in credit page
*   Night at the museum will be a time for us to showcase our project

**Delivery Plans and Content for big Milestones**
*   Friday 12/11: Finish Project Scope
*   Friday 12/18: Set up basic layout of website, play sounds on website if possible
*   -Break-
    *   Flexible jobs
    *   Over these two weeks we can finish anything we haven’t, or do some refining touch ups/get ahead if we want
    *   Dylan: Finish up the basic layout of the website w/ flask
    *   Kaila: Look into databases, try to set up a login/ new acc function
    *   Kira: if possible, at least have a good idea of how to go about making an interactive soundgrid (tempo?)
    *   Tyler: Help with the login/information storing
*   Friday 1/8: Hopefully finish an interactive grid(only clicking around) and login program finished
*   Friday 1/15: Functioning grid (without music)
*   Midterms 1/22: Sound implemented into interactable grid
*   Friday 1/29: Saving sounds into a database as a user completed(as a project you can re-open)
*   Friday 2/5: ^ Continuing on this, as it may be a large task
*   Friday 2/12: Other instruments' sounds implemented and saveable
*   Friday 2/19: The fundamental parts of the website have all been completed and the website is functioning
*   Friday 2/26:  Finish port forwarding/raspberry pi, finish implementation of http
*   Friday 3/5: Fix up looks of the website, make sure everything is accessible and aesthetically pleasing
*   N@TM: Project completed and implemented into the N@TM project done
*   Sound Board
    *   Instrument sound effects
        *   [http://theremin.music.uiowa.edu/MISpiano.html](http://theremin.music.uiowa.edu/MISpiano.html)
    *   Buttons to indicate notes “grid” layout
        *   [https://github.com/googlecreativelab/chrome-music-lab](https://github.com/googlecreativelab/chrome-music-lab)
    *   Possibly a piano on the side to determine notes??
*   Log-In System
*   Saving music data
*   Updating database of logins/music

**Big Ticket features with Visuals **
*   Search Bar
*   Log-in
*   Interactive Grid
    *   Replayable Music From Grid (saved by logging in)

