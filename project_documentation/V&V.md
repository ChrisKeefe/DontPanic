# Table of Contents

{{TOC}}

# Description  
Don't Panic is a free, minimal app that lets any American stay informed about the pitfalls in your life in a way you care about. Users download Don’t Panic on their mobile devices, or sign up through the web application, and receive timely, geo-targeted notifications warning them about environmental or community risks, and helping them navigate them successfully. Panic is still in early development. A basic Android app GUI allows users to easily customize their message profiles, web GUI allows administrators to create messages, and a basic API allows Administrators to create new User, Message, and Profile data in a scalable realtime database.  

Our Android app is available to select users/developers for pre-alpha testing. The app will offer a simple user interface, the ability to quickly activate/deactivate it, and the ability to personalize the information we receive from the app. User profiles allow us to control message timing, preferred types of content, and preferred message type. Ease of use is key for Don’t Panic users: simple design that’s easy for everyone to understand, and a set-it-and-forget-it approach that ensures Don’t Panic never gets in your way.  

[Project repo](https://github.com/ChrisKeefe/DontPanic)  
[Trello](https://trello.com/b/91yjEezy/dont-panic)  

# Verification (tests)  
## Unit test
We chose to use python’s unittest framework, because it is a standard library package, relatively simple, and ships with robust testing tools, including tooling for mocks. It is, however, very ugly, and does not include coverage testing, so are using the pytest library as a test runner (for pretty outputs), and the pytest-cov library for coverage.  

Tests are housed in test_cloud_functions.py in our cloud functions directory.  

## Integration Test  
Insert test results here.  

## Acceptance  
Insert test results here.   

# Validation (User Evaluation)  
Insert test results here.  

## Script  
**General questions about the webpage**  

- How do you think the webpage looks?
- Try to fill out the web page. How easy was it?
- What was difficult about it?
- How would you rate the overall ease of use (1 to 10)
- What could be improved?
- Would you use it currently, or wait for it to be developed more?
- If yes, why?
- If no, why?  What should we change?
- Could you give an overall score 1-10?
- Why did you give it this score?
- Imagine you work for an organization that tracks emergency events. Is there other information you would like to include about your specific message that you think should be included in this form?

**General questions about the app**  

- How do you think the app looks?  
- Do you think it looks too complicated?  
- Is it intuitive?  
- Try to change profile settings.
- How easy was it?  
- What was difficult about it?  
- How would you rate the overall ease of use (1-10)?  
- What could be improved?  
- Would you use it currently, or wait for it to be developed more?  
- If yes, why?  
- If no, why?  What should we change?  
- Could you give an overall score (1-10)?  
- Why did you give it this score? 

**Specific follows-ups from inception interview results**  

- Do you feel like settings were buried in the menu?
- Do you feel the app is simple?
- Do you feel the initial alert options are useful to you?
- Do you feel like you are in control?
- What additional features/customization options would make this app more useable?

## Interview Results
### Madisen Lussier:
**Webpage:**  

- How do you think the webpage looks?
	- Very plain. It looks like you (Mason) made it
- Try to fill out the web page.
- How easy was it?
	- It is basically dummy proof
- What was difficult about it?
	- Didn't understand the resource link at first
- How would you rate the overall ease of use (1 to 10)
	- 9
- What could be improved?
	- It should just add more to design so it looks nicer
- Would you use it currently, or wait for it to be developed more?
- If yes, why?
- If no, why?  What should we change?
	- It looks like it needs more to be a finished product
- Could you give an overall score 1-10?
- Why did you give it this score?
	- 6 - It does what it is supposed to, which is the important part. But that's all it does  


**Mobile app:**  

- How do you think the app looks?
- Do you think it looks too complicated?
- Is it intuitive?
	- Very simple, seems prototype-y
- Try to change profile settings.
- How easy was it?
	- It is easy, but there probably needs to be more
- What was difficult about it?
	- Nothing
- How would you rate the overall ease of use (1-10)?
	- 9
- What could be improved?
	- Maybe just look nicer. And more settings
- Would you use it currently, or wait for it to  be developed more?
- If yes, why?
- If no, why?  What should we change?
	- It looks like it needs more to be a finished product
- Could you give an overall score (1-10)?
- Why did you give it this score?
	- 5 - It does what it is supposed to, but probably needs more. And could probably look a little more polished    

## Reflections:  

**Madisen:**  
From the answers we received from Madisen, we realized how much an attractive design can impact a first impression. Her initial thoughts on both the web form and the mobile app were both about appearance. The more she looked at it, the more she say the functionality and the simplicity, but we didn't spend much time on design and that showed for her.
