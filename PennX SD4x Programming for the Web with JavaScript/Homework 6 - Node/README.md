#### Homework 6 - Node

---
In this assignment, you will use Node.js and Express to develop a Web API that provides services related to data stored in a MongoDB database.

This assignment continues the “pet store” theme from previous assignments. In this case, you will build a Web API that allows applications to get information about the pets at the store and the pet toys that the store sells.

In completing this assignment, you will:

* Learn how to set up Node, Express, Mongo, and related packages
* Apply what you have learned about developing a Node Express app and using various objects and functions
* Implement JavaScript queries using Mongoose to retrieve data from a MongoDB database
* Create a server-side Web application that reads data from an incoming HTTP request and sends back JSON data in an HTTP response

---
##### Usage

1. Create a new folder or directory for your project, then navigate to it using Terminal, Command Prompt, etc.

2. Initialize the project by typing the command: npm init

3. Install Express by typing the command: npm install express --save

4. Install Mongoose by typing the command: npm install mongoose --save

5. Copy all three files to the directory that is the root of your Node Express project, i.e. the directory where you ran “npm init”. 

6. Create an account to use a cloud service such as MongoDB Atlas (https://www.mongodb.com/cloud/atlas)

7. In MongoDB Atlas, Clusters -> CONNECT -> Copy a connection string -> I am using driver 3.4 or earlier -> Copy the URI connection string

8. In Animal.js and Toy.js, replace the parameter of mongoose.connect with your connection string.

9. Replace PASSWORD with the password for your MongoDB Atlas user. Please note that any special characters in your password (%, @, and :) will need to be URL encoded.

10. Use Terminal or Command Prompt to navigate to the root directory of your Node Express project and type the command: node index.js

You should see the message “Listening on port 3000”. Then use your web browser to access http://localhost:3000.