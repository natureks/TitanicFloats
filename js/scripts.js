var form_cabin_select = {
    "1": ["A", "B", "C", "D","E"],
    "2": ["TBD"],
    "3": ["TBD"]
}
console.log(form_cabin_select["1"]);


function change_cabin() {
    var class_value = document.getElementById("form-class").value;
    console.log(class_value);
    var catOptions = "";
    if (class_value.length == 0) {
        document.getElementById("form-cabin").innerHTML = "<option></option>"; 
    }
    else if (class_value == 1) {
        catOptions += '<option value="" selected disabled>Please select</option>';
        for (categoryId in form_cabin_select[class_value]) {
            catOptions += "<option>" + form_cabin_select[class_value][categoryId] + "</option>";
        }
        catOptions += '<option value="Z">No Preference</option>';
        document.getElementById("form-cabin").innerHTML = catOptions;
    }
    else if (class_value == 2) {
        for (categoryId in form_cabin_select[class_value]) {
            catOptions += '<option value="Z" disabled selected>' + form_cabin_select[class_value][categoryId] + "</option>";
        }
        document.getElementById("form-cabin").innerHTML = catOptions;
    }
    else if (class_value == 3) {
        for (categoryId in form_cabin_select[class_value]) {
            catOptions += '<option value="Z" disabled selected>' + form_cabin_select[class_value][categoryId] + "</option>";
        }
        document.getElementById("form-cabin").innerHTML = catOptions;
    }
}

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
                case "Z":
                    return 80;
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

    //document.getElementById("fare-section").style.display="block";

});

var buy_ticket = document.getElementById('buy_ticket');

buy_ticket.addEventListener("click", function(event){
    document.getElementById("questionaire").style.display="none";

    event.preventDefault();

    var ticket_title;
    var ticket_depart_from;
    var ticket_gender;
    var ticket_cabin;



    if (title.length > 0) {
        if (title == "Mr") {
            ticket_title = "Mr.";
        }
        else if (title == "Mrs") {
            ticket_title = "Mrs.";
        }
        else {
            ticket_title = title;
        }
    }
    console.log(ticket_title);

    if (depart_from.length > 0) {
        if (depart_from == "C") {
            ticket_depart_from = "Cherbourg"
        }
        else if (depart_from == "S") {
            ticket_depart_from = "Southhampton"
        }
        else if (depart_from == "Q") {
            ticket_depart_from = "Queenstown"
        }
    }

    if (gender.length > 0 ) {
        if (gender == "m") {
            ticket_gender = "Male"
        }
        else if (gender == "f") {
            ticket_gender = "Female"
        }
    }

    if (cabin.length > 0) {
        if (cabin == "Z") {
            ticket_cabin = "TBD"
        }
        else {
            ticket_cabin = cabin
        }
    }

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

        document.getElementById("ticket-full-name").innerHTML = ticket_title + " " + first_name + " " + last_name;
        document.getElementById("ticket-age").innerHTML = age;
        document.getElementById("ticket-gender").innerHTML = ticket_gender;
        document.getElementById("sailing-from").innerHTML = ticket_depart_from;
        document.getElementById("ticket-class").innerHTML = class_form;
        document.getElementById("ticket-cabin").innerHTML = ticket_cabin;
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

function refreshPage() {
    window.location.reload();
}
