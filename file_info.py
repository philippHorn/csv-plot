file_info = [
				{
				 	"name" : "csv/48.10391.0.0.12000-3.csv", 
				 	"columns" : ["Code", "Status"], 
				 	"quantity" : "Zustand"
				},

				{
				 	"name" : "csv/48.10391.0.0.12008-4.csv",
				 	"columns" : ["min", "mittel", "max"], 
				 	"quantity" : "Leistung soll", 
				 	"unit" : "%", 
				 	"converter" : lambda x: x/10.0
				},

				{
				 	"name" : "csv/48.10391.0.0.12165-4.csv", 
				 	"columns" : ["min", "mittel", "max"],
				 	"quantity" : "Abgasgebläse", 
				 	"unit" : "U/min"
				},

				{
				 	"name" : "csv/48.10391.0.11094.0-4.csv",
				 	"columns" : ["min", "mittel", "max"], 
				 	"quantity" : "Primärluft", 
				 	"unit" : "%", 
				 	"converter" : lambda x: x/10.0
				},

				{
				 	"name" : "csv/48.10391.0.11095.0-4.csv",
				 	"columns" : ["min", "mittel", "max"], 
				 	"quantity" : "Sekundärluft", 
				 	"unit" : "%", 
				 	"converter" : lambda x: x/10.0
				},

				{
				 	"name" : "csv/48.10391.0.11094.0-4.csv",
				 	"columns" : ["min", "mittel", "max"], 
				 	"quantity" : "Restsauerstoff", 
				 	"unit" : "%", 
				 	"converter" : lambda x: x/100.0
				},

				{
				 	"name" : "csv/48.10391.0.11109.0-4.csv",
				 	"columns" : ["min", "mittel", "max"], 
				 	"quantity" : "Kessel T.", 
				 	"unit" : "°C", 
				 	"converter" : lambda x: x/10.0
				},

				{
				 	"name" : "csv/48.10391.0.11110.0-4.csv",
				 	"columns" : ["min", "mittel", "max"], 
				 	"quantity" : "Abgas T.", 
				 	"unit" : "°C", 
				 	"converter" : lambda x: x/10.0
				},

				{
				 	"name" : "csv/48.10391.0.11160.0-4.csv",
				 	"columns" : ["min", "mittel", "max"], 
				 	"quantity" : "Rücklauf T.", 
				 	"unit" : "°C", 
				 	"converter" : lambda x: x/10.0
				},

				{
				 	"name" : "csv/120.10251.0.11153.0-4.csv", 
				 	"columns" : ["min", "mittel", "max"], 
				 	"quantity" : "Puffer Oben", 
				 	"unit" : "°C", 
				 	"converter" : lambda x: x/10.0
				},

				{
				 	"name" : "csv/120.10251.0.11155.0-4.csv", 
				 	"columns" : ["min", "mittel", "max"], 
				 	"quantity" : "Puffer Unten", 
				 	"unit" : "°C", 
				 	"converter" : lambda x: x/10.0
				}
			]