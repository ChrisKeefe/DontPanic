//prototype code for dynamically  creating JSON from web form data
//=================================================================

//examples of JSON from w3 schools
//{
//"employees":[
//  {"firstName":"John", "lastName":"Doe"},
//  {"firstName":"Anna", "lastName":"Smith"},
//  {"firstName":"Peter", "lastName":"Jones"}
//]
//}

var content = form.getElementById('element_1').value;
var category = form.getElementById('element_2').value;
var URL = form.getElementById('element_4').value;
var urgency = form.getElementById('element_3').value;

//w3 example of JSON to JS object
//var text = '{ "employees" : [' + '{ "firstName":"John" , "lastName":"Doe" },' + '{ "firstName":"Anna" , "lastName":"Smith" },' + '{ "firstName":"Peter" , "lastName":"Jones" } ]}';

//Our vaiable for a Json to JS object
var json = '{ "messagePayload" : [' + '{ "messageContent":"content" , "category":"category" , "urgency":"urgency" , "URL":"URL", "tags":["tag1", "tag2", "tag3"] }]}';