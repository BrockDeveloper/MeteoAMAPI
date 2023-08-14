# MeteoAMAPI

API per il Servizio meteorologico dell'Aeronautica Militare, rielaborazione dei dati presenti e provenienti da https://www.meteoam.it.

## Condizioni di utilizzo
Informazioni elaborate dal Servizio Meteorologico dell’Aeronautica Militare e pubblicate sul sito [www.meteoam.it](http://www.meteoam.it/); pertanto si identifica il servizio Meteo AM quale unico proprietario di tali informazioni.

## API Base (WIP)
https://hostname:8000/{location}

**Response (e.g. Milano):**

    {
		"general": {
			"copyright": "https://www.meteoam.it",
			"location": "Milano",
			"latitude": 45.461,
			"longitude": 9.172,
			"datetime": "2023-08-14T22:00:00"
		},
		"temperature": {
			"current": 30.0,
			"minimum": 25.0,
			"maximum": 35.0,
			"humidity": 0.43,
			"unit": "Celsius degrees"
		},
		"wind": {
			"speed": {
				"value": 7.0,
				"unit": "km/h"
			},
			"direction": {
				"value": 67,
				"unit": "degrees"
			}
		},
		"sun": {
			"sunrise": "06:22",
			"sunset": "20:33"
		},
		"pressure": {
			"value": 1016,
			"unit": "hPa"
		}
	}


