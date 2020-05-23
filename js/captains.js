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


    var cell = row.append('td')
    cell.text(sighting.age)
  })
}

// // initialize the table with all the data
// addTable(data)

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
//     Object.entries(sighting.ticket) => {
//       var cell = row.append('td')
//       cell.text(value)
//     })
//   })
// }

// // // initialize the table with all the data
// // addTable(data)