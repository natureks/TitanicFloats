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

    title = document.getElementById("form-title").value;
    first_name = document.getElementById("form-first-name").value;
    last_name = document.getElementById("form-last-name").value;
    gender = document.getElementById("form-gender").value;
    age = document.getElementById("form-age").value;
    class_form = document.getElementById("form-class").value;
    cabin = document.getElementById("form-cabin").value;
    sib_sp = document.getElementById("form-sib_sp").value;
    par_ch = document.getElementById("form-par_ch").value;
    depart_from = document.getElementById("form-depart-from").value;

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

    document.getElementById("fare-section").style.display="block";

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

    base_url = "https://young-beach-08773.herokuapp.com/api/add_passenger/"
    url = base_url + title + "/" + first_name + "/" + 
        last_name + "/" + class_form + "/" + gender + "/" + 
        sib_sp + "/" + par_ch + "/" + fare + "/" +
        age + "/" + depart_from + "/" + cabin;

    console.log(url);
    
    d3.json(url).then(function(data) {
        var probability = data["Probability"];
        var survive_metric = data["Survival"];
        var ticket_number = data["TicketNum"];

        console.log(data);

        document.getElementById("ticket-full-name").innerHTML = title + " " + first_name + " " + last_name;
        document.getElementById("ticket-age").innerHTML = age;
        document.getElementById("ticket-gender").innerHTML = gender;
        document.getElementById("sailing-from").innerHTML = depart_from;
        document.getElementById("ticket-class").innerHTML = class_form;
        document.getElementById("ticket-cabin").innerHTML = cabin;
        document.getElementById("ticket-fare").innerHTML = fare;
        document.getElementById("ticket-sibsp").innerHTML = sib_sp;
        document.getElementById("ticket-parch").innerHTML = par_ch;
        document.getElementById("ticket-ticket-number").innerHTML = ticket_number;
    
        if (survive_metric === "1") {
            document.getElementById("survive-metric").innerHTML = "Survive: " + probability;
        }
        else {
            document.getElementById("survive-prob").innerHTML = "Death: " + probability; 
        }

        
 
    
    });

    document.getElementById("survive-section").style.display="block";
    document.getElementById("ticket-final").style.display="block";

});
