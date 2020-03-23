### 1. Introduction

**Provide a short paragraph that describes your system. This paragraph should contain the value proposition and the description of the main features of the software. At the end of the introduction, include links to your project on GitHub and Trello.**

Don't Panic is a free, minimal app that lets any American stay informed about the pitfalls in your life in a way you care about. Users download Don’t Panic on their mobile devices, or sign up through the web application, and receive timely, geo-targeted notifications warning them about environmental or community risks, and helping them navigate them successfully.

Don’t Panic is still in early development, and our Android application is available to select users/developers for alpha testing. The app offers a simple user interface, the ability to quickly activate/deactivate it, and will soon offer users the ability to personalize the information we receive from the app. Ease of use is key for Don’t Panic users: simple design that’s easy for everyone to understand, and a set-it-and-forget-it approach that ensures Don’t Panic never gets in your way.

Project repo: [https://github.com/ChrisKeefe/DontPanic](https://github.com/ChrisKeefe/DontPanic)
Trello: [https://trello.com/b/91yjEezy/dont-panic](https://trello.com/b/91yjEezy/dont-panic)

### 2. Implemented requirements

**List in this section, the requirements (user stories, issues, or use cases) that you
implemented for this release. We expect that you implement/prototype features you
specified in your MVP (c.f. D.2 Requirements). Include who worked on each of the
features. We expect that all the members of the group have been involved in some
programming activities. BTW, we will check if you are using Trello to manage the
implementation tasks.**

- User story 1: “As a user, I want to receive push notifications so that I am informed immediately of issues.”
	Priority: 2
	Estimated Hours: 8

- User story 2: “As a user, I want to have a simple UI so that I can easily navigate the app”
	Priority: 4
	Estimated Hours: 13

### 3. Adopted technologies

**Include a list of adopted technologies with a brief description and justification for
choosing them.**

**Android Studio:**

Android Studio was adopted as the team’s IDE for DontPanic development. Studio is the premiere IDE for Android development, plays well with other components in our tech stack, and makes the development of familiar user interface components quick and easy.

**Google Firebase Stack:**

Google Firebase provides cloud-based tools for database, storage, authentication, notifications, “server”-side code, and integration with Android, iOS, and web applications. It works well in companionship with Android Studio, and it allows for simple creation of web applications that will allow non-smartphone users of DontPanic to sign up for the service. By reducing our need to manage a server, we have made developing this project more feasible for our small team.

**Google Firestore:**

Google Firestore is a real time database that stores user information and integrates seamlessly with firebase, and apps across all major platforms. It is fast, serverless, and provides a more-intuitive architecture than its predecessor, Firebase Realtime DB. All user and message data will be stored in our Firestore Database.

**Firebase Cloud Messaging (FCM):**

FCM is the replacement for Google’s widely popular Google Cloud Messaging (GCM). FCM allows us as developers to easily send notifications to the users of the DontPanic Application, and SMS messages to non-smartphone users.

**Google Cloud Functions (GCF):**

Google cloud functions provide us the ability to write “server”-side code in a serverless stack. Cloud functions will allow us to sort and select the best message for a given client, without bogging down that client’s device. Lightweight design was a common must-have from our interviewees, and GCF will make that possible.

**Summary:**

By sticking with Google’s Ecosystem of products and allowing Firebase to be the backbone of our application, we have been able to streamline the production of our app. By spending more time developing the UI, implementing useful features for the customer, and creating our database, and less time worrying about compatibility, we were able to create an MVP with ease, and will be able to create a higher quality end product.

### 4. Learning/training

**Describe the strategies employed by the team to learn the adopted technologies.**

Our team’s primary learning strategy has been to divide up the research and assign it to different group members according to interests and time available during a weekly cycle. We began by thoroughly investigating our tech stack, figuring that time invested upfront would save us surprises later. Our original idea was to use a server on AWS that implemented technologies like Apache, MySQL, and Twilio, but we then found that many of those can be encompassed in Firebase. We discovered Firebase during the inception phase of our project, and decided that Firebase, along with Firebase Cloud Messaging (FCM), could handle our needs more gracefully than the original stack design.

For any given topic, one or two members research independently, then educate the rest of the group on what they have learned. Because some people had prior knowledge (Chris with Github and Brandon with Android Studio), we were able to cover some topics early on during our weekly meetings. Throughout the semester, we have used Slack as an asynchronous resource for posting resources, and keeping everyone up to speed.

Recent events have made in-person meetings difficult, but we have effectively used phone, Discord-based screen share, and slack work to keep us all learning and developing productively. As the app continues to develop, we hope this cycle of discovery, sharing, and adaptation continues.

### 5. Deployment

**Your system should use containers and Docker. Describe how you are deploying your
system in production. Remember that AWS Educate offers free credits for students. See
the tutorial at https://docker-curriculum.com/ on how to create a container and deploy
it on AWS. Provide a link for the system in production.**

Because Firebase runs the services that would normally run on a container, a Docker image is not needed. This highlights another advantage of choosing Firebase for our application and has been approved by Dr. Gerosa.

### 6. Licensing

**Inform the license you adopted for your source code (remember to configure GitHub
accordingly) and why you adopted this license. For more information, check [https://choosealicense.com/](https://choosealicense.com/) and [http://redhat.slides.com/glikins/open-sourcelicensing-101#/](http://redhat.slides.com/glikins/open-sourcelicensing-101#/)**

**MIT License**

- [MIT license overview](https://choosealicense.com/licenses/mit/)

- [Our License](https://github.com/ChrisKeefe/DontPanic/blob/master/LICENSE)

We chose a MIT license so people can do almost anything they want with our project, like making and distributing closed source versions. We want our project to be as accessible as possible for people who want to work on it

### 7. Readme File

**You should also prepare your repository for receiving new contributors. See an example
of a Readme.md file at [https://gist.github.com/PurpleBooth/109311bb0361f32d87a2](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
Besides the Readme.md file, your repository should contain a CONTRIBUTING.md
file, a LICENSE file, and a CODE_OF_CONDUCT.md file. Search online for some
examples of these files. In this section of the deliverable, put links to these files on GitHub.**

- [README.md](https://github.com/ChrisKeefe/DontPanic/blob/master/README.md)

- [CONTRIBUTING.md](https://github.com/ChrisKeefe/DontPanic/blob/master/CONTRIBUTING.md)

- [CODE_OF_CONDUCT.md](https://github.com/ChrisKeefe/DontPanic/blob/master/CODE_OF_CONDUCT.md)

- [LICENSE](https://github.com/ChrisKeefe/DontPanic/blob/master/LICENSE)

### 8. Look & feel

**Describe the approach you adopted to design your user interface. Include some
Screenshots.**

During our interviews one commonality that arose was a non-intrusive and very simple UI. Interviewees wanted an app they opened once, set up, and could forget about afterwards, only receiving notifications when and how they preferred.

This initial development cycle was scoped to provide users the ability to receive notifications, but does not allow for complex customizations of content. In the interest of providing some level of interactivity and a sense of user control, our UI features a very visible on/off switch.

**![](https://lh6.googleusercontent.com/0cBVlNdXCETJiEUnhnmppT5wNHUmR8g2AJSI_p8ZPDFLhJed0fKg9lrLXR6Y97om4Y4byjy4H2usNC6gT_q2RXFTCohqfAhGQq83xYma8vUILdBhrGZJBglgWBWuWaPTVqA1ETpD)**

We are generating most of the UI with Android Studios tools, rather than trying to implement our own custom features. This is in line with what users wanted: something simple and familiar like android’s interface streamlines both their experience and our development process. Notifications, likewise, are displayed as standard push notifications, and maintain all expected behavior of normal push notifications.

**![](https://lh4.googleusercontent.com/VBa1EQ3bVg3H_fYqUZB-IadRwBH8R4g_73uC7gFl9b52fT5H3ZgV1bh8gu6oSV_dgz8lPAUIF9jibdeKSnXhZRPc-y_tyVPIUPIwVIyd18yRIHHi0-_vf4yJd0EYppjq6yalmEwr)**

### 9. Lessons learned

**In retrospective, describe what your team learned during this first release and what you
are planning to change for the second release.**

Our initial development cycle went well overall. Version control and IDE issues took more time than expected, and our MVP is truly minimal as a result. We've learned a lot in this development cycle, have gotten more comfortable with git, github, and Android Studio, and expect that will make the next round go more smoothly. Each team member really did a good job of playing to their strengths this round, and we plan to continue developing iteratively and with a focus on teamwork.

### 10. Demo

**Include a link to a video showing the system working.**

Demo Link - [https://youtu.be/j9gMyaN6YzI](https://youtu.be/j9gMyaN6YzI)
