var url = 'https://young-beach-08773.herokuapp.com/api/get_passengers'
// var age
// var cabin
// var class

fetch(url)
    .then(res => res.json())//response type
    .then(data => addTable(data)); //log the data;

function addTable (tableData) {
    // remove all the existing table data if it exists
    d3.selectAll('td').remove()
    // add the rows
    var tbody = d3.select('tbody')
    tableData.forEach((sighting) => {
        var row = tbody.append('tr')
        var cell;

        if(sighting['survived'] === 1)
        {
            sighting['survived_yesno'] = "Yes"
        }
        else
        {
            sighting['survived_yesno'] = "No"
        }
        // order the items in the dictionary to match with the html
        orderArr = ['ticket', 'title', 'first_name', 'last_name', 'gender', 'age', 'port', 'cabin', 'survived_yesno', 'prob'];
        orderArr.forEach((col) => {
            cell = row.append('td');
            cell.text(sighting[col]);
        })
    })
}

// var url = 'https://young-beach-08773.herokuapp.com/api/get_passengers'

// fetch(url)
//     .then(res => res.json())//response type
//     .then(data => addTable(data)); //log the data;

// function addTable (tableData) {
//   // remove all the existing table data if it exists
//   d3.selectAll('td').remove()

//   // add the rows
//   var tbody = d3.select('tbody')
//   tableData.forEach((sighting) => {
//     var row = tbody.append('tr')
//     Object.entries(sighting).forEach(([key, value]) => {
//       var cell = row.append('td')
//       cell.text(value)
//     })
//   })
// }