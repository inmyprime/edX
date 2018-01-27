var express = require('express');
var app = express();

var Animal = require('./Animal.js');
var Toy = require('./Toy.js');

app.use('/findToy', (req, res) => {
	var query = {};
	if (req.query.id) {
		query.id = req.query.id;

		Toy.findOne( query, (err, toy) => {
			if (err) {
				res.type('html').status(500);
				res.send('Error: ' + err);
			} else if (toy) {
				res.json(toy);
			}
			else {
				res.json({});
			}
		});	  
	} else {
		res.json({});
	}  
});

app.use('/findAnimals', (req, res) => {
	var query = {};
	if (req.query.species) {
		query.species = req.query.species;
	}
	if (req.query.trait) {
		query.traits = req.query.trait;
	}
	if (req.query.gender) {
		query.gender = req.query.gender;
	}

	if (Object.keys(query).length == 0) {
		res.json({});
	} else {
		Animal.find( query, '-_id name species breed gender age', (err, animals) => {
			if (err) {
				res.type('html').status(500);
				res.send('Error: ' + err);
			}
			else {
				res.json(animals);
			}
		});
	}
});

app.use('/animalsYoungerThan', (req, res) => {
	var age = req.query.age;

	if (age && !isNaN(age)) {
		Animal.find({age : {$lt : age}}, (err, animals) => {
			if (err) {
				res.type('html').status(500);
				res.send('Error: ' + err);
			}
			else {
				if (animals.length > 0) {
					var result = {};
					result.count = animals.length;
					result.names = animals.map(animal => animal.name);
					res.json(result);
				} else {
					res.json({count : 0});
				}

			}
		});
	} else {
		res.json({});
	}
});

app.use('/calculatePrice', (req, res) => {
	var query = {};
	if (req.query.id) {
		query.id = req.query.id;
	}
	if (req.query.qty) {
		query.qty = req.query.qty;
	}

	var idToQtyMap = new Map();
	if (query.id && query.qty && query.id.length == query.qty.length) {
		for (var i = 0; i < query.id.length; i++) {
			var id = query.id[i];
			var qty = query.qty[i];

			if (!isNaN(qty) && qty > 0) {
				if (idToQtyMap.has(id)) {
					idToQtyMap.set(id, Number(idToQtyMap.get(id)) + Number(qty));
				} else {
					idToQtyMap.set(id, qty);	
				}
			}
		}

		var idToPriceMap = new Map();
		var items = [];
		var totalPrice = 0;

		Toy.find( {id : Array.from(idToQtyMap.keys())}, (err, toys) => {
			if (err) {
				res.type('html').status(500);
				res.send('Error: ' + err);
			} else {
				toys.forEach(toy => idToPriceMap.set(toy.id, toy.price));

				for (var id of Array.from(idToPriceMap.keys())) {
					var item = {
						item : id,
						qty : idToQtyMap.get(id),
						subtotal : idToQtyMap.get(id) * idToPriceMap.get(id)
					}
					totalPrice += item.subtotal;
					items.push(item);
				}
				res.json({totalPrice : totalPrice, items : items});
			}
		});	
	} else {
		res.json({});
	}
});

app.listen(3000, () => {
	console.log('Listening on port 3000');
});



// Please do not delete the following line; we need it for testing!
module.exports = app;