
# InstaList
## Directory listings made quick & easy 

[TODO]: Build Status & Test Status

There are 2 sections to the project so far. Both independent of each other, "client" and "server". It's mostly a learning/ POC/ Sandbox tool. 

**<span style="color:red; font-weight:bold; text-decoration:underline;">NOTE:</span> **This should not be used for production 'as is' ever**.** 

# Requirements
These requirements should be considered compulsory. All versions based on my local dev versions. 

 - [GIT](https://git-scm.com/downloads) >=V0.0.1 -- Expected you already have this if here. 
 - [NodeJS](https://nodejs.org/it/) >= v14.15.4 -- if you need multiple versions per dev machine look into Node Version Manager - Very nice cli tool for switching live node versions. ([nvm](https://github.com/nvm-sh/nvm))
 - [npm](https://nodejs.org/it/) >= 6.14.10 -- (Should come with NodeJS installer)
 - [MongoDB](https://www.mongodb.com/try/download/community) >= db version v4.4.3 -- (community edition is perfect for this project)

### Recommended 

 - [nodemon](https://www.npmjs.com/package/nodemon) -- Installed globally, (`npm install -g nodemon`) Can be a very useful tool for auto reloading node services while developing. More useful for the "Server" section, as it will behave simular to Angular's 'watch' functionality in `ng serve`.

# Setup & Prep 

 - Clone the repository into wherever you like on your machine.
 
 - With `ssh` setup from your machine to github :
`git clone https://github.com/klexas/InstaList.git`
 - If not;
`git clone https://github.com/klexas/InstaList.git`


# Client Install

Client application is a bespoke standalone Angular 12 project. Using TypeScript, it offers a strongly typed and well structured path.

After the repo has been cloned. You will find 2 folders. "Client" and "Server". Client is where the Angular Front-End (FE) is. 
In order to install/download all the required packages, from the command line of your choice cmd, terminal, powershell etc. 

cd into : `client/instalist` folder.

This is the root of the angular FE. It has its own set of dependencies, installs, tests and scripts via npm.  From here you can run: 

'npm install'

This should take a good few mins first: It's installing all of the packages and dependencies required to interpret & compile Typescript (TS),  transpile, test and serve, as well as any 3rd party packages we add for the front end.  (See later).

 - [x] After install is complete

You can go ahead and run 
`ng serve`

This will compile all the TS into Javascript, transpile any Scss etc into CSS and HTML readable by the browser and host it in a local server instance. By default you should see in the console : 
![Post ng serve](https://images2.imgbox.com/4d/6f/s7BeHXD7_o.png)
If you see something simular/the same. Go to the URL mentioned in your browser. In this case (and by default)

`http://localhost:4200/`

You should be presented with : 

![enter image description here](https://images2.imgbox.com/fb/71/k0XhV7XT_o.png)



## Modifying the source

//[TODO]: Further info on Angular
Angular project is inside the `client/instalist/src` From here its separated into Services, Components, Models. 
I will do a further drill down into this, but the structure/method follows vanilla Angular. 


## Notes

You can export the current file by clicking **Export to disk** in the menu. You can choose to export the file as plain Markdown, as HTML using a Handlebars template or as a PDF.


# Server Install

Much easier than the client. Simply step into the folder 

`cd /server`

Then you can run : 

`npm install`

This will add all the required packages. As this time we are working through vanilla NodeJS for our server (for now). 
We can simply run the main service. 

`node main.js`

// Or if you have nodemon

`nodemon main.js`

That your server running.

## Notes

There are configuration & settings files throughout to make this project as flexible as possible. However with the angular project, if you update the `settings.json` file which contains some static data (to be moved to DB) you will need to recompile the angulr project (`ng serve` again`) in order to see changes. 

Server is extremely light at the moment, not tied in yet. The idea is to grow this and tie them over time. 

This is the initial checkin. 



## TODO

Currently all the test files are paired with their service/component, it would be beneficial to have them all in a separate location collected for pipeline testing. 

## Sandbox Team

[HJTB](https://github.com/hjtb)
[Alexsandro Souza](https://github.com/apssouza22)
