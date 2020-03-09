# Analysis



## 1. System Description



We live in an unpredictable world, and unexpected pitfalls may affect anyone when they least expect it; these unpleasant surprises can cost you financially or cause huge personal setbacks. For anyone who wants to stay informed about what matters to them, DontPanic! is a is a free, lightweight application that helps anyone safely navigate life’s many pitfalls in a way that matters to you. Unlike CodeRED, our product is simple to use and allows the user to customize their preferences however they like.



Don’t Panic smartphone **users** download the application from the Google Play Store. Non-smartphone **users** simply sign up online. Both (receive) timely **notifications** relevant to their _**location**_, and designed to help them stay safe and productive. **Users** can (customize) their **profiles**, selecting their preferred _method of delivery_, the types of **notifications** they’re most interested in, and their preferred **notification** frequency. The application **controller**  (sends) only the most relevant **messages**. **Users** may (customize) the frequency and type of **notifications** they receive via the web app or on their smart devices, and may mute non-emergency **notifications** quickly and easily at any time. Critical emergency **notifications** are (sent) to all **users** at risk of impact. **User** interfaces are clean, intuitive, and accessible to anyone.



## 2. Model

![](https://lh6.googleusercontent.com/jn-FxfRtgjz9YBbW_PiRTHlkABWxkKVciUy6FafCa7qFvAwGUkQVM09QC9PcCTdJy-pSbd8DjqTIVHHkCQq85x9WcjPrB3bAkt3Y73e82oodQMA82IsT90DNKCnFS3ZpcVccaLXl)









## 3. Class Responsibilities

For each class, include an explanation about its responsibility and why you included it, mapping the classes to the system requirements.



**User**

* The User Class is responsible for keeping track of a given user's personal information, including contact and authentication data


* It is included because it allows the necessary information pertaining to delivery information and account information to be stored in a single class, and managed easily from the backend.

* It helps meet the system requirements because it enables personalization of message content and delivery method




**Profile**

* The Profile Class stores the preferences of a given user of DontPanic. This includes what kind of notifications they want to receive, and and how they want to receive them.

* It is included to store the users personal preferences. While the User Class focuses on how our back end handles the delivery of information, the Profile Class focuses on what kind of information the user will receive, and how they want to receive it. It is the part that is customizable by them.

* It meets the requirements by giving the user control of the information they want to receive and how they want to receive it.


**Location**

* Because our app uses geo-location, we need to add Location to our diagram.

* This is because we send notifications that are area-specific, and are crucial to the use of our app. *Keeping these messages relevant to the user is a key part of our app and strongly aligns with our system requirements by keeping users informed with information related to their area.



**Controller**

* The Controller is what will functionally get the messages the user will receive. It does not store any data, but grabs the messages, which has the data needed.

* Because the Message Class is data, we need something to get the message and deliver it to the user.

* The Controller will help make the decisions about which messages to receive for the user, and will help keep messages relevant to preferences through keywords/tiers that are associated with Message Class.



**Messages**

* The Messages Class describes message content, message resources, and message tier/keyword information.


* Since each user can customize the kinds of messages they receive, a Message Class needed to be included to that a message can be tailored to their given preferences.

* Message class objects support system requirements by allowing customization of messages delivered given user preferences.
