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

[API Docs on APILayer](https://apilayer.com/marketplace/currency_data-api)
