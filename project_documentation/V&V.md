# Table of Contents

{{TOC}}

# Description  
Don't Panic is a free, minimal app that lets any American stay informed about the pitfalls in your life in a way you care about. Users download Don’t Panic on their mobile devices, or sign up through the web application, and receive timely, geo-targeted notifications warning them about environmental or community risks, and helping them navigate them successfully. Panic is still in early development. A basic Android app GUI allows users to easily customize their message profiles, web GUI allows administrators to create messages, and a basic API allows Administrators to create new User, Message, and Profile data in a scalable realtime database.  

Our Android app is available to select users/developers for pre-alpha testing. The app will offer a simple user interface, the ability to quickly activate/deactivate it, and the ability to personalize the information we receive from the app. User profiles allow us to control message timing, preferred types of content, and preferred message type. Ease of use is key for Don’t Panic users: simple design that’s easy for everyone to understand, and a set-it-and-forget-it approach that ensures Don’t Panic never gets in your way.  

[Project repo](https://github.com/ChrisKeefe/DontPanic)  
[Trello](https://trello.com/b/91yjEezy/dont-panic)  

# Verification (tests)  
## Unit test
### 2.1.1
We chose to use python’s unittest framework, because it is a standard library package, relatively simple, and ships with robust testing tools, including tooling for mocks. It is, however, very ugly, and does not include coverage testing, so we are using the pytest library as a test runner (for pretty outputs), and the pytest-cov library for coverage. Our test assertions are built using the cleaner pytest syntax.

### 2.1.2
Tests are housed in test_cloud_functions.py in our [cloud functions directory.](https://github.com/ChrisKeefe/DontPanic/tree/master/functions)

### 2.1.3
[CreateMessageTests.test_receiving_json()](https://github.com/ChrisKeefe/DontPanic/blob/1b4cee8486287a2850ca8eb8f3992c22f76fb4f9/functions/test_cloud_functions.py#L18) mocks a POST request object with a JSON payload of valid data. It tests that the JSON-parsing logic of our create_message() cloud function is working properly. Whenever our test suite calls the test, it actuates the cloud function by POST request, creating a new test record in our Firestore Realtime Database, and returning a POST-specific success message. We use a simple regex-like test to confirm we have received the correct success message as a response.

### 2.1.4
#### Test successes and coverage reporting:
![test_successes](https://github.com/ChrisKeefe/DontPanic/blob/master/project_documentation/deliverable_media/tests_passing_full_cov.png)

#### Messages created in our RealtimeDB during unit testing:
![test_messages](https://github.com/ChrisKeefe/DontPanic/blob/master/project_documentation/deliverable_media/messages_generated_by_testing.png)

## 2.2 Integration Test  
Our application is built on a new-to-us serverless platform, which has thrown us some real curveballs. During development for D6, we were unable to get either our App or Webform to send HTTP requests to our GCF API, though the API readily accepted requests sent through a browser or via curl. After putting six more hours into attempting to wire the web form up this week, we were able to diagnose the problem, but were unable to fix it. Trello has been updated to note the work required. Without any two apps integrated successfully, we have been unable to conduct integration testing, but will speculate on how that might work.

### 2.2.1
We would conduct our integration testing using the Mocha test framework - it is well-documented and has approachable syntax, and would allow us to test the integration between our webform (written in node.js) and the cloud functions API.

### 2.2.2
As noted above, we were unable to conduct integration testing, with no integrated application components.

### 2.2.3
If we had been able to conduct integration testing, our approach would closely mirror the unit testing performed in 2.1, but would do so from the javascript webform. The webform would trigger requests to each cloud function, providing JSON data that is a)well-formed and complete, b)incomplete but well-formed, c) malformed, and would test whether the results matched the expected responses.

### 2.2.4
No print screen available. Sorry!

## 2.3 Acceptance  
We were unable to get any acceptance testing done. Besides the interfaces we built, we can't test other functions the user can use. Like we stated in 2.2, we were unable to get our components to work with each other, which impedes our ability to do integration and acceptance testing.

### 2.3.1
We would conduct our acceptance testing using the Selenium testing framework. It seems to be well documented and can do simple accpetance testing with it

### 2.3.2
Because we could not integrate Acceptance testing, we have no Github folder for it

### 2.3.3
If we had been able to conduct acceptance testing, our approach would be similar to our unit testing, but would do so from the javascript webform.

### 2.3.4 
No print screen available. Sorry!

# Validation (User Evaluation)  

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


**April:**  

**TODO:**  

**Overall:**
