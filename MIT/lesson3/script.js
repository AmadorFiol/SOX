function user_input(){
    let my_input = prompt("Enter Something");
    console.log("User input: ", my_input);
    //Challenge:
    document.getElementById("demo").innerHTML = my_input;
}

