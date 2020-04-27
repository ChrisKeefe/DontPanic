var form = document.getElementById('main-form');
form.addEventListener('submit', logSubmit);


function logSubmit(event) {
    
    var formData = new FormData( document.getElementById('main-form'));
    
    //prep the json object
    var innerObject = {};
    var tagsArray = [];
    
    formData.forEach( (value, key) => {
        if (key != 'tags')
        {
            innerObject[key] = value 
        }
        else if( key == 'tags')
        {
            tagsArray.push(value);
        }
     });
    
    innerObject['tags'] = tagsArray;
    
    var masterObject = {};
    masterObject['messagePayload'] = innerObject;
    
    var masterString = JSON.stringify(masterObject);
    
    console.log(masterString);
    
    jQuery.post("https://us-central1-dontpanicfbase.cloudfunctions.net/create_message", masterString);
    
    event.preventDefault();
}

