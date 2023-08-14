XPATH = [
    {
        "name": "location",
        "xpath": "/html/body/section[2]/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div/div[1]/div/div[2]/h2",
        "get": "innerHTML"
    },

    {
        "name": "textual",
        "xpath": "/html/body/section[2]/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div/div[1]/div/div[1]/div[1]",
        "get": "class"
    },

    {
        "name": "temperature",
        "xpath": "/html/body/section[2]/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div/div[2]/div/div/div/div[1]/span",
        "get": "innerHTML"
    },

    {
        "name": "temperature_min",
        "xpath": "/html/body/section[2]/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div/div[2]/div/div/div/div[2]/span[2]",
        "get": "innerHTML"
    },

    {
        "name": "temperature_max",
        "xpath": "/html/body/section[2]/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div/div[2]/div/div/div/div[2]/span[1]",
        "get": "innerHTML"
    },

    {
        "name": "humidity",
        "xpath": "/html/body/section[2]/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div/div[3]/div/div/div[1]/div[1]/span[2]",
        "get": "innerHTML"
    },

    {
        "name": "wind",
        "xpath": "/html/body/section[2]/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div/div[3]/div/div/div[2]/div/span[2]",
        "get": "innerHTML"
    },

    {
        "name": "pressure",
        "xpath": "/html/body/section[2]/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div/div[3]/div/div/div[1]/div[2]/span[2]",
        "get": "innerHTML"
    },

    {
        "name": "sunrise",
        "xpath": "/html/body/section[2]/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div/div[4]/div/div/div/div[2]/div[2]/span[2]",
        "get": "innerHTML"
    },

    {
        "name": "sunset",
        "xpath": "/html/body/section[2]/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div/div[4]/div/div/div/div[2]/div[1]/span[2]",
        "get": "innerHTML"
    },
    
    {
        "name": "coordinates",
        "xpath": "/html/body/section[2]/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div/div[4]/div/div/div/div[1]/span[2]",
        "get": "innerHTML"
    },

    {
        "name": "datetime",
        "xpath": "/html/body/section[2]/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div/div[1]/div/div[2]/div/div/span[2]",
        "get": "innerHTML"
    }
]