
# Project Design

_Group 06 – “[Don't Panic!]”
Date: April 5, 2020
Group Members: Chris Keefe, Mason Rodgers, Brandon Click, Drew Sansom_

## 1. Description

__Provide 1-2 paragraphs to describe your system. This will help understand the context of
your design decisions. You can reuse and update the text from the previous deliverables.__

__Grading: 2 points. Criteria: Completeness (1 pt); Consistency with the rest of the document (0.5 pt); Language (0.5 pt).__

Don't Panic is a free, minimal app that lets any American stay informed about the pitfalls in your life in a way you care about. Users download Don’t Panic on their mobile devices, or sign up through the web application, and receive timely, geo-targeted notifications warning them about environmental or community risks, and helping them navigate them successfully.

Don’t Panic is still in early development, and our Android application is available to select users/developers for alpha testing. The app offers a simple user interface, the ability to quickly activate/deactivate it, and the ability to personalize the information we receive from the app. User profiles allow us to control message timing, preferred types of content, and preferred message type. Ease of use is key for Don’t Panic users: simple design that’s easy for everyone to understand, and a set-it-and-forget-it approach that ensures Don’t Panic never gets in your way.

Project repo: [https://github.com/ChrisKeefe/DontPanic](https://github.com/ChrisKeefe/DontPanic)

Trello: [https://trello.com/b/91yjEezy/dont-panic](https://trello.com/b/91yjEezy/dont-panic)

## 2. Architecture

__Present a diagram of the high-level architecture of your system. Use a UML package diagram to describe the main modules and how they interrelate. Provide a brief rationale of your architecture explaining why you designed it that way.__

__Grading: 5 points. Criteria: Adequate use of UML (2 pts); Adequate design of an architecture for the system (2 pts); Adequate description of the rationale (1 pt).__

Our system design consists of three layers, describing system-specific data types designed to interface cleanly with our database, business logic, and a user-facing presentation layer, comprising an android application, and web applications for profile and message management (to be created as time allows). The business logic includes two APIs which present simple interfaces for users to interact with the system, and a group of message sending tools, called by the sendMessage class.

**![](https://lh5.googleusercontent.com/L9RY59Hqmdx4i-PFXYHnoPHflma4ytZtf9PdfggYGz8rZgktTCebMSFeYajVPKC6a6SuY37XUl4ma0gthnYolbKxKhTQl39oRqct0I-95K-SyizofAGQ0Dlpayt4L2RIpuQ-ypjG)**
## 3. Class diagram

__Present a refined class diagram of your system, including implementation details such as visibilities, attributes to represent associations, attribute types, return types, parameters, etc. The class diagram should match the code you have produced so far, but not be limited to it (e.g., it can contain classes not implemented yet). The difference between this class diagram and the one that you presented in D.3 is that the last focuses on the conceptual model of the domain while the former reflects the implementation. Therefore, the implementation details are relevant in this case.__

__Grading: 6 points. Criteria: Adequate use of UML (2 pts); Adequate choice of classes and relationships (2 pts); Completeness of the diagram (1 pt); Adequate presentation of implementation details (1.0).__

Our class diagram attempts to comprehensively diagram the business logic and data layers of our application. As such, we have chosen to provide [a link to the diagram](https://drive.google.com/file/d/1MSAlQP8ij7GBYuHQNnChBahOyjx482ur/view?usp=sharing) for improved readability:

**[https://drive.google.com/file/d/1MSAlQP8ij7GBYuHQNnChBahOyjx482ur/view?usp=sharing](https://drive.google.com/file/d/1MSAlQP8ij7GBYuHQNnChBahOyjx482ur/view?usp=sharing)**

## 4. Sequence diagram

__Present a sequence diagram that represents how the objects in your system interact for a specific use case. Also include the use case description in this section. The sequence diagram should be consistent with the class diagram and architecture.__

__Grading: 5 points. Criteria: Adequate use of UML (1 pt); Adequate design of the sequence diagram (2 pts); Consistency with the class diagram (1 pt); Consistency with the use case description (1 pt); Not including the use case description (-1.5 pt); Over simplistic diagram (-1 pt).__

**![](https://lh5.googleusercontent.com/8lKRaYvIXx2ypbheMtQPFbuHT-4cxvIg44Jr9Med-hZ_NhFqpoHgiUiv-d7CCNzUv5kAqdhdTuX9DZjWxJknWQt7skofJ-UQ-rNiJxXHb_bVvyvYp1g_0Lq66oIUIuIfMau0LLTd)**

__Use Case Description:__

Use Case: Create Profile

Actor: App User

Description: A smartphone user will download the “DontPanic” app and create a profile

Preconditions: App is installed, user has a userid

Postconditions: They have created a new user profile, it is logged to DB, and the user is notified of successful profile creation

Main Flow:

1.  The user enters required information about his profile (Location, UserID, PhoneNum) into a webform, and clicks submit.

2.  The user profile is created

3.  System logs profile to database

4.  System notifies user of successful profile creation

Alternative Flow:

2a. Profile fails to create:  
1. User is notified of failure

## 5. Design Patterns

__For each subsection, present a UML class diagrams showing the application of a design pattern to your system (a different pattern for each section).__

A) __Strategy Pattern (Behavioral): We use a strategy pattern to send a message in different ways, depending on user preferences:__

![](https://lh4.googleusercontent.com/kDkCFa-OmdvT4OJV-DDFZPZBI3zPN7h7_ZPsOZqMZHyEQSsXnYu_EY1uhcywNp972KJeTTBLcc2KaL1Ey9EnzhdmxSAHqSVUzD1hlzXddcwX7iCcNdIpRPDolcQ2zqAn0HSPTWDr)

B) __Observer Pattern (Behavioral): We use observers in two places in our codebase, triggering database and user-feedback actions at the completion of an API call.__

![](https://lh6.googleusercontent.com/1HENpaNuonSdeWsjDaElF2wq6DptjXFnXFSIYgwfLUFuGcN0i7MVdcswAvlQ0isThH3tYmzrkZyqEvVSnU3EcKcJ2cw3KRodPWF1zmakjWBbvuGFzf0voDPADCyvpPcvhKaiDOZx)

C) __Proxy Pattern (Structural): By using the Google Authenticate tooling built into the Firebase stack, we will be able to avoid building user authentication functionality. If we didn’t have access to that tooling, the Proxy pattern could help us restrict API access to only users who have passed authentication. Here, a web app user calls a method from the Proxy, which authenticates the user, and delegates the call to RealProfileManagerAPI__

![](https://lh5.googleusercontent.com/u2bT5F4tm4zh7WBLlq8D93tjl34FcNpTPLRHdSxLq11qfm5OHCvoBb2anAEloX1bPbyhvkx17OGI3Opq_-zJdvx58EDrtf12e2MDbkFoEebVtdedaJNJS_aAEXFy2_PUPMTOBlug)

## 6. Design Principles

__How does your design observe the SOLID principles? Provide a short description of the following principles giving concrete examples from your classes.__

__Grading: 6 points. Criteria: Show correct understanding of SOLID principles (3 pts); Provide enough details to justify how the principles were observed (3 pts).__

-   __Single responsibility principle__ (a class should have only a single responsibility.)

![](https://lh6.googleusercontent.com/HWy39uQp10f5AeLGBuYvCZqN6oIWNWcsM719jrJVafRg_xhC0F_U7P1CqYtouJOgybGSp34adsaPFjuReYyfzgAPpabqJsvK_E89tThC-MgswyFcg6PXzywfixcxnYo58mmRdDs9)

In our app, we send push notifications for smart phones and text messages for “dumb” phones. We have an SMS sender and a Push sender so each will only have a single responsibility. This Keeps the Message Sender class from having too much responsibility

-   __Open/closed principle__ (“software entities … should be open for extension, but closed for modification”.)

![](https://lh3.googleusercontent.com/SHPJOQHbo8gI-gah9ZVVUN3uT9jDMXnqmeuVpJxBGKX0STagxQAETUbu8TdGEZJejxHMfL1rqX9R2X5uQZn6anryTLibGbICjoOWm4tJn8cwxs-Vr3CaQV9be34FvMuXu-oN4ozr)

For ProfileObserver, we can add more observers if we deem it necessary. The ability to add classes here can make it easier for us, so we don't have to modify existing classes to meet new needs

-   __Liskov substitution principle__ (“objects in a program should be replaceable with instances of their subtypes without altering the correctness of that program”.)

![](https://lh6.googleusercontent.com/HWy39uQp10f5AeLGBuYvCZqN6oIWNWcsM719jrJVafRg_xhC0F_U7P1CqYtouJOgybGSp34adsaPFjuReYyfzgAPpabqJsvK_E89tThC-MgswyFcg6PXzywfixcxnYo58mmRdDs9)

In this case, you can replace Message Sender with SMS Sender, or Push Sender, depending on the situation. The substitution will not affect the program.

-   __Interface segregation principle__ (“many client-specific interfaces are better than one generalpurpose interface.”)

![](https://lh5.googleusercontent.com/u2bT5F4tm4zh7WBLlq8D93tjl34FcNpTPLRHdSxLq11qfm5OHCvoBb2anAEloX1bPbyhvkx17OGI3Opq_-zJdvx58EDrtf12e2MDbkFoEebVtdedaJNJS_aAEXFy2_PUPMTOBlug)

The interface for authentication (As mentioned in part 5c) simplify the interface by only having methods that apply to multiple methods. It makes this interface easier to use by having some actions handled elsewhere.

Our program doesn't have much as far as interfaces go, so there isn't much interface segregation present in our system.

-   __Dependency inversion principle one should__ (“Depend upon Abstractions. Do not depend upon concretions.”)

![](https://lh5.googleusercontent.com/nuOPmbkMpCt2pU0wNOtjSAJaAW9uR7ptGfDVgnELyNeE77hmC2ohC8lPDgtRjZSLof_HWjLtk-lHuO_cq24Zjlx9nQm80fCvE5nI1Uvx6H1GAH-rGu3ZjVuDJJ4Pqi5cxOSxyo1r)

Here, we use MessageCreationObserver to handle MessageToDB, EmergencyMessageSender, MessageCreatedNotifier. CreateMessageAPI depends on MessageCreationObserver (an abstraction) to handle the other classes (which are concrete )
