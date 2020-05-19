function get_fare_price(questionaire_class, questionaire_cabin) {
    switch(questionaire_class) {
        case "1":
            switch(questionaire_cabin) {
                case "A":
                    return 40;
                case "B":
                    return 113;
                case "C":
                    return 100;
                case "D":
                    return 63;
                case "E":
                    return 55;
            }
            break;
        case "2":
            return 21;
        case "3":
            return 14;
        default:
          "FIX"
      };

};

var fare;
var title;
var first_name;
var last_name;
var gender;
var age;
var class_form;
var cabin;
var sib_sp;
var par_ch;
var depart_from;

var submit_button = document.getElementById('submit_button');

submit_button.addEventListener("click", function(event){

    event.preventDefault();

    title = document.getElementById("title").value;
    first_name = document.getElementById("first_name").value;
    last_name = document.getElementById("last_name").value;
    gender = document.getElementById("gender").value;
    age = document.getElementById("age").value;
    class_form = document.getElementById("class_form").value;
    cabin = document.getElementById("cabin").value;
    sib_sp = document.getElementById("sib_sp").value;
    par_ch = document.getElementById("par_ch").value;
    depart_from = document.getElementById("depart_from").value;

    console.log("title: " + title);
    console.log("first_name: " + first_name);
    console.log("last_name: " + last_name);
    console.log("gender: " + gender);
    console.log("age: " + age);
    console.log("class_form: " + class_form);
    console.log("cabin: " + cabin);
    console.log("sib_sp: " + sib_sp);
    console.log("par_ch: " + par_ch);
    console.log("depart_from: " + depart_from);

    fare = get_fare_price(class_form, cabin);

    document.getElementById("input_fare").innerHTML = fare;

});

var buy_ticket = document.getElementById('buy_ticket');

buy_ticket.addEventListener("click", function(event){

    event.preventDefault();

    var dict = {
        'ticket_class' : class_form,
        'sex' : gender,
        'siblings_spouse' : sib_sp, 
        'parents_children' : par_ch,
        'fare' : fare,
        'age' : age,
        'port' : depart_from,
        'cabin' : cabin
    };

    document.getElementById("ticket_full_name").innerHTML = "Name: " + title + " " + first_name + " " + last_name;
    document.getElementById("ticket_age").innerHTML = "Age: " + age;
    document.getElementById("ticket_gender").innerHTML = "Gender: " + gender;
    document.getElementById("ticket_depart_from").innerHTML = "Depart: " + depart_from;
    document.getElementById("ticket_class").innerHTML = "Class: " + class_form;
    document.getElementById("ticket_cabin").innerHTML = "Cabin: " + cabin;
    document.getElementById("ticket_fare").innerHTML = "Fare: " + fare;

});
