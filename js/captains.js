fetch('https://young-beach-08773.herokuapp.com/api/get_passengers')
    .then(res => res.json())//response type
    .then(data => console.log(data)); //log the data;

// var url = "https://young-beach-08773.herokuapp.com/api/get_passengers"
// // Replace ./data.json with your JSON feed
// fetch(url)
//   .then(response => {
//     return response.json()
//   })
//   .then(function addTable (response) {
//     // remove all the existing table data if it exists
//     d3.selectAll('td').remove()
//     // add the rows
//     var tbody = d3.select('tbody')
//     data.forEach((ticket) => {
//       var row = tbody.append('tr')
//       Object.entries(ticket).forEach(([key, value]) => {
//         var cell = row.append('td')
//         cell.text(value)
//       })
//     })
//   })
//   .catch(err => {
//     // Do something for an error here
//   })