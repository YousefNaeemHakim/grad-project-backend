## Currency API

### Available Endpoints

Route | Description |
---- | ------------
`/list` | Returns all available currencies.
`/live` | Get the most recent exchange rate data.
`/convert` | Convert one currency to another.
`/historical` | Get historical rates for a specific day.
`/timeframe` | Request exchange rates for a specific period of time.
`/change` | Request any currency's change parameters (margin, percentage).

---

### JSON Example for Supported Symbols

```JSON
{
  "success": true,
  "symbols": {
    "AED": "United Arab Emirates Dirham",
    "AFN": "Afghan Afghani",
    "ALL": "Albanian Lek",
    "AMD": "Armenian Dram",
    [...]
    }
}
```

---

### Request Examples

To reduce bandwidth you can limit the number of output currencies to a specific set of your choice on most API endpoints. To do so, simply append the Fixer API's symbols parameter to your API request and set it to one or more comma-separated currency codes.

```bash
curl --request GET 'https://api.apilayer.com/currency_data/live?base=USD&symbols=EUR,GBP' \
--header 'apikey: YOUR API KEY'
```

It is also possible to convert currencies using historical exchange rate data. To do this, please also use the API's date parameter and set it to your preferred date. (format YYYY-MM-DD)

```bash
curl --request GET 'https://api.apilayer.com/currency_data/convert?base=USD&symbols=EUR,GBP,JPY&amount=5&date=2018-01-01' \
--header 'apikey: YOUR API KEY'
```

---


### GET/change
```JavaScript
var myHeaders = new Headers();
myHeaders.append("apikey", "{API-KEY}");

var requestOptions = {
  method: 'GET',
  redirect: 'follow',
  headers: myHeaders
};

fetch("https://api.apilayer.com/currency_data/change?start_date={start_date}&end_date={end_date}", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```
### Returns
```JSON
{
  "change": true,
  "end_date": "2010-01-01",
  "quotes": {
    "USDAUD": {
      "change": -0.1726,
      "change_pct": -13.4735,
      "end_rate": 1.108609,
      "start_rate": 1.281236
    },
    "USDEUR": {
      "change": -0.0389,
      "change_pct": -5.2877,
      "end_rate": 0.697253,
      "start_rate": 0.73618
    },
    "USDMXN": {
      "change": 1.9594,
      "change_pct": 17.5741,
      "end_rate": 13.108757,
      "start_rate": 11.149362
    }
  },
  "source": "USD",
  "start_date": "2005-01-01",
  "success": true
}

```


[More Info about the API on APILayer](https://apilayer.com/marketplace/currency_data-api)

[API Docs on APILayer](https://apilayer.com/marketplace/currency_data-api#documentation-tab)
