- [1. Description](#1-description)
- [2. Implemented Requirements](#2-implemented-requirements)
  * [Admin Creates a New Message in DB Using the CreateMessageAPI](#admin-creates-a-new-message-in-db-using-the-createmessageapi)
  * [Admin Creates a New Profile in DB Using the ProfileManagerAPI](#admin-creates-a-new-profile-in-db-using-the-profilemanagerapi)
  * [Admin Creates a New User in DB Using the CreateUserAPI](#admin-creates-a-new-user-in-db-using-the-createuserapi)
  * [Admin Creates Message in DB Using a Webform](#admin-creates-message-in-db-using-a-webform)
  * [User Creates Profile Using Android GUI to Customize their Message Preferences](#user-creates-profile-using-android-gui-to-customize-their-message-preferences)
- [3. Demo](#3-demo)
- [4. Code Quality](#4-code-quality)
- [5. Lessons Learned](#5-lessons-learned)

# 1. Description
Don't Panic is a free, minimal app that lets any American stay informed about the pitfalls in your life in a way you care about. Users download Don’t Panic on their mobile devices, or sign up through the web application, and receive timely, geo-targeted notifications warning them about environmental or community risks, and helping them navigate them successfully.  

Don’t Panic is still in early development. A basic Android app GUI allows users to easily customize their message profiles, web GUI allows administrators to create messages, and a basic API allows Administrators to create new User, Message, and Profile data in a scalable realtime database.  

Our Android will be available to select users/developers for alpha testing soon. The app will offer a simple user interface, the ability to quickly activate/deactivate it, and the ability to personalize the information we receive from the app. User profiles allow us to control message timing, preferred types of content, and preferred message type. Ease of use is key for Don’t Panic users: simple design that’s easy for everyone to understand, and a set-it-and-forget-it approach that ensures Don’t Panic never gets in your way.  

[Project Trello Board](https://trello.com/b/91yjEezy/dont-panic)  
[Github Repo](https://github.com/ChrisKeefe/DontPanic)

# 2. Implemented Requirements  
Collectively, team members put roughly 85 man-hours into this week’s deliverable.

## Admin Creates a New Message in DB Using the CreateMessageAPI
**Implementer(s):** Chris Keefe, Mason Rogers  
**Name of Reviewer/Approver:** Drew Sansom    
[Trello Card ](https://trello.com/c/hIsRxlmP/39-stories-admin-creates-new-message-in-db-using-createmessageapi)  
[Pull Request](https://github.com/ChrisKeefe/DontPanic/pull/20)  
**Screen Captures:**  

Messages in DB Before  
![](https://github.com/ChrisKeefe/DontPanic/blob/master/project_documentation/deliverable_media/messagesBefore.png)  
  
Code Example   
![](https://github.com/ChrisKeefe/DontPanic/blob/master/project_documentation/deliverable_media/messagesCode.png)  
 
Messages in DB After   
![](https://github.com/ChrisKeefe/DontPanic/blob/master/project_documentation/deliverable_media/messagesAfter.png)

## Admin Creates a New Profile in DB Using the ProfileManagerAPI  
**Implementer(s):** Chris Keefe, Drew Sansom  
**Name of Reviewer/Approver:** Drew Sansom  
[Trello Card](https://trello.com/c/LArtUh75/40-stories-admin-creates-new-profile-in-db-using-profilemanagerapi)  
[Pull Request](https://github.com/ChrisKeefe/DontPanic/pull/20)  
**Screen Captures:**  

Profiles in DB Before  
![](https://github.com/ChrisKeefe/DontPanic/blob/master/project_documentation/deliverable_media/profileBefore.png)  
  
Code Example  
![](https://github.com/ChrisKeefe/DontPanic/blob/master/project_documentation/deliverable_media/profileCode.png)  
  
Profiles in DB After  
![](https://github.com/ChrisKeefe/DontPanic/blob/master/project_documentation/deliverable_media/profileAfter.png)

## Admin Creates a New User in DB Using the CreateUserAPI
**Implementer(s):** Chris Keefe, Drew Sansom  
**Name of Reviewer/Approver:** Drew Sansom  
[Trello Card](https://trello.com/c/Ff6CcG8E/52-stories-admin-creates-new-user-in-db-using-createuserapi)  
[Pull Request](https://github.com/ChrisKeefe/DontPanic/pull/21)  
**Screen Captures:**  
 
Users in DB Before  
![](https://github.com/ChrisKeefe/DontPanic/blob/master/project_documentation/deliverable_media/usersBefore.png)  
 
Code Example  
![](https://github.com/ChrisKeefe/DontPanic/blob/master/project_documentation/deliverable_media/usersCode.png) 
 
Users in DB After    
![](https://github.com/ChrisKeefe/DontPanic/blob/master/project_documentation/deliverable_media/usersAfter.png)

## Admin Creates Message in DB Using a Webform
**Implementer(s):** Mason Rogers  
**Name of Reviewer/Approver:**  Drew Sansom  
[Trello Card](https://trello.com/c/1IRzyyFe/54-stories-admin-creates-message-in-db-with-webform)  
[Pull Request](https://github.com/ChrisKeefe/DontPanic/pull/26)  
**Screen Captures:**  

The Webform  
![](https://github.com/ChrisKeefe/DontPanic/blob/78468f6597f79b47f3ae56f3b490c993436c3974/project_documentation/deliverable_media/webform.png)  

## User Creates Profile Using Android GUI to Customize their Message Preferences
**Implementer(s):** Brandon Click  
**Name of Reviewer/Approver:** Drew Sansom  
[Trello Card](https://trello.com/c/vCehsiBy/60-stories-user-creates-profile-using-android-gui-to-customize-their-messaging-preferences)  
[Pull Request](https://github.com/ChrisKeefe/DontPanic/pull/27)  
**Screen Captures:**  

The homepage of the DontPanic Application  
![](https://github.com/ChrisKeefe/DontPanic/blob/master/project_documentation/deliverable_media/DontPanic-enabiling.PNG)  

The Profile Creation Page of the app  
![](https://github.com/ChrisKeefe/DontPanic/blob/master/project_documentation/deliverable_media/DontPanic-messagingPrefrence.PNG)

# 3. Demo  
Video walkthroughs of the DontPanic project are available in the links below. Use 1080p when possible for the best experience.  
A preview of the DontPanic Android Application is available [here.](https://www.youtube.com/watch?v=g7xs-yvVRRw&feature=youtu.be)   
A preview of DontPanic's backend and API features is available [here.](https://www.youtube.com/watch?v=_CTMxXml8_U)

# 4. Code Quality
In spite of the many challenges we ran into in working with new technologies (described at length below), we maintained a strong focus on producing high-quality code. We adopted the following approaches, all of which worked well for the team:

- **Working groups** - We split the team into two subgroups, with two members focused on back-end stories, and two focused on front-end stories. This allowed better specialization, and faster turnaround on decision-making in new domains.
- **Story leadership** - individual team members took ownership of stories, taking responsibility for learning the required technology, and helping remove barriers for other team members co-working on those stories. This reduced learning-curve overhead, and allowed individual stories to be advised by the team members who best understood the APIs involved.
- **Pair programming** - developing in new technologies is challenging - we reduced the number of syntax and logic errors by pair-programming solutions using VSCode liveshare and zoom. We caught many errors prior to code review this way.
- **Required code review** - at the beginning of the semester, we restricted access to our master branch, only allowing merging on PRs that have been approved by one or more other team members. This prevented accidental merging of unfinished code, and ensured that good review practices were followed.
- **Documentation** - as development proceeded, we actively documented function behaviors, focusing especially on API specifications to reduce friction at the front-end/back-end interface.

# 5. Lessons Learned
In retrospect, describe what your team learned during this second release and what would you change if you would continue developing the project.

- Learning a new paradigm is hard - as a team, we put over 60 hours into this week’s deliverable, the great majority of which went into understanding Google Cloud Functions and working with the Google Cloud/Firebase stack.
- Documentation isn’t always trustworthy, especially if marketing has been involved - Firebase Cloud Messaging’s docs state that “Notification Messages” are handled automatically by android applications. As of Android 8, however, they are only handled if the app is backgrounded (or you’ve configured foregrounded notification receiving), and a channel has been configured for the incoming messages (at both the client and the server). The “very simple” story of sending a message to our app with Cloud Functions proved too time-costly for us to deliver this cycle.
- Developing towards client-facing deliverables can be frustrating - Our product’s value relies heavily on the backend logic we designed to intelligently select user-appropriate messages. Unfortunately, it isn’t easy to deliver that stuff in a compelling way until you can make the API actually send a message to your device from the database. Because we had to organize ourselves around client-facing, video-communicated deliverables, we spent our time wrestling the google cloud stack instead of writing the bones of the software. 
- Estimating the development time for stories is nearly impossible when working with new tech. Simple-sounding stories turned out to be epics, and we were forced to split our stories aggressively to keep them in the 1-8 hour range.
