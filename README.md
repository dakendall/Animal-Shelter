# Animal-Shelter
You work for Global Rain, a software engineering company that specializes in custom software design and development. Your team has been assigned to work on a project for an innovative international rescue-animal training company, Grazioso Salvare. You have been made the lead developer on this project.

As part of its work, Grazioso Salvare identifies dogs that are good candidates for search-and-rescue training. When trained, these dogs are able to find and help to rescue humans or other animals, often in life-threatening conditions. To help identify dogs for training, Grazioso Salvare has reached an agreement with a non-profit agency that operates five animal shelters in the region around Austin, Texas. This non-profit agency will provide Grazioso Salvare with data from their shelters.

In meeting with the client, you have discovered that they look for certain profiles in dogs to train. For example, search-and-rescue training is generally more effective for dogs that are no more than two years old. Additionally, different breeds of dogs are proficient at different types of rescue, such as water rescue, mountain or wilderness rescue, locating humans after a disaster, or finding a specific human by tracking their scent.

Grazioso Salvare is seeking a software application that can work with existing data from the animal shelters to identify and categorize available dogs. Global Rain has contracted for a full stack development of this application, including a database and a client-facing web application dashboard through which users at Grazioso Salvare will access the database.


In the code for this program is maintainable, readable and adaptable. I created a CRUD Python module that has the functions to create a document, read documents, update documents, and delete documents. This is useful because we can use the functions repetitively without having to retype the same code. A programer could also add other functions to this file for the same purpose. As a computer scientist, I had to identify and understand the problem/requirements. One of the requirements by Grazioso Salvare was to be able to look for certain profiles in the animal shelter database. Instead of retyping code that searches the database every time we need to filter the list, we can use the read function in the CRUD Python module. This was applied in the IPYNB file with the radio buttons on the dashboard. We used the parameters that we provided and when a user selects a filter option, the function will read through the database and return the results. I have taken the same approach in previous projects. I identity the problem and understand the problem. Then I find a way to solve the problem and then develop a method. One of the strategies they teach you is how to reuse your code. You have to work smarter not harder. A strategy that I will use going forth is researching the best tools for the program I am trying to create. In this project, we used Mongodb to manage the database and Dash to create the dashboard. A computer scientist's job is important because we have the ability to create programs to make it easier for users such as the training company, Grazioso Salvare. Instead of having to look at each profile to find the specific dog, we created a program that does it for them. The program will return the profiles that they are looking for along with other features. The dashboard that was created also has a pie chart that shows how many dogs are available and a map that shows where a certain dog is located.
