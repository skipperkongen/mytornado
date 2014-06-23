# Mytornado greenwords application

## API

### Methods

Two types of ads are served. *Commercial* ads (that people pay for, get payed for) and *nonprofit* ads (where no-one gets payed).

* `random_ad (widget_info, client_info)`: Returns a random ad (default)
* `commercial_ad (widget_info, client_info)`: Returns a commercial ad
* `nonprofit_ad (widget_info, client_info)`: Returns a non-profit ad

#### Psedo code for finding an ad to serve

````python
campaign_id = find_a_campaign(widget_info, client_info)
advertisement = pick_random_advertisement(campaign_id)
```

### Schema

`account`:

```sql
-- A user account with Greenwords
CREATE TABLE IF NOT EXISTS account
(
	id INT PRIMARY KEY,
	username TEXT, -- Name of the campaign
	saldo FLOAT, -- Grows if account is displaying ads, shrinks if account is having ads displayed
)
```

`pull_account`:

```sql
-- A pull account belong to someone displaying ads on a website
CREATE TABLE IF NOT EXISTS push_account
(
	id INT PRIMARY KEY,
	username TEXT, -- Name of the campaign
	saldo FLOAT, -- Money earned by pull account
	target_url TEXT, -- The URL that is advertised		
)
```

`campaign`:

```sql
-- A campaign has a saldo, and a set of ads (linked in the 'campaign_entry' table)
CREATE TABLE IF NOT EXISTS advertisements
(
	id INT PRIMARY KEY,
	name TEXT, -- Name of the campaign
	account_id INT, -- Who is paying for the campaign?
	target_url TEXT, -- The URL that is advertised	
	nonprofit BOOLEAN,
	cost_per_view FLOAT, -- Zero for verified non-profit ads
	cost_per_click FLOAT, -- Zero for verified non-profit ads				
)
```

`advertisements`:

```sql
-- Contains attributed for an advertisement that are not used for ranking
CREATE TABLE IF NOT EXISTS advertisements
(
	id INT PRIMARY KEY,
	iab_id INT,
	content_url TEXT, -- The URL where the contents of the ad can be fetched
	format TEXT, -- swf,jpeg,png,html,txt, i.e. the 'format' used to implement the ad type	
)
```

`campaign_metadata`:

```sql
-- Search table for finding a campaign when an ad is requested
CREATE TABLE IF NOT EXISTS campaign_metadata 
(
	id INT PRIMARY KEY,
	campaign_id INT, -- Campaign ID
	-- Constraint properties (match against website widget)
	tier TEXT, -- 'commercial' or 'nonprofit'
	type TEXT, -- rich,image,markup,txt, i.e. the 'type' of ad
	campaign_id INT, -- ID of the campaign
	active BOOLEAN, -- Is the campaign currently active?
	dreadlock_factor FLOAT, -- Between 0 and 1, with 1 being most dreadlocky
	-- Used for ranking (match against client and website)
	lang_code TEXT, -- ISO 639-1 code for language used in ad
	country_code TEXT, -- ISO 3166-1 code for country
	geographical_area GEOMETRY -- Relevance area for ad (Any geometry type is valid)
	start_time DATETIME, -- starting date for ad
	end_time DATETIME -- end date for ad
)
```


`iab_sizes`:

```sql
-- Metadata about the advertisement, used for selecting an appropriate ad
CREATE TABLE IF NOT EXISTS adranking 
(
	id INT PRIMARY KEY,
	iabname TEXT, -- E.g. 'Square Pop-Up'
	width INT,
	height INT
)
```


`contenturls`:

```sql
-- All URLs where the advertisement contents can be fetched
CREATE TABLE IF NOT EXISTS contenturl 
(
	id INT PRIMARY KEY,
	ad_id INT,
	distributor_id INT,
	type TEXT, -- 'cdn' or 'self' or 'partner' 

)
```

`served`:

```sql
-- Keep records of every time an ad has been served to a client
CREATE TABLE IF NOT EXISTS served 
(
	id INT PRIMARY KEY,
	ad_id INT, -- what was served?
	displayer_id INT, -- who showed it?
	client_hash INT, -- who saw it?
	timestamp DATETIME -- when did they see it?
)
```

`clicked`:

```sql
-- Keep records of every time an ad has been clicked by a client
CREATE TABLE IF NOT EXISTS served 
(
	id INT PRIMARY KEY,
	ad_id INT, -- what was served?
	displayer_id INT, -- who showed it?
	client_hash INT, -- who saw it?
	timestamp DATETIME -- when did they see it?
)
```


I can think of a billion more tables that could be useful, but we're keeping it simple this time around.


### Request data

`ad_constrains`:

`ad_preferences`:

`site_info`:

`client_info`

### Response data

An ad result as returned by `random_ad` is a JSON object. There are three types of result objects.

The common attributes are:

* `iabsize`: One of [IAB standardized ad sizes](http://en.wikipedia.org/wiki/Web_banner#Standard_sizes)
* `id`: A unique ID for this ad
* ``

**Rich media result**:

```json
{
	"type": "media",
	"id": 123456789,
	"url":"http://example.com/123456789.swf",
	""
	"width": 256,
	"height": 256
}
```

## Client API

### Methods

* `switch_ad()`: Replace the current ad with another one. Fetches new ad from server, and registers that it was switched (along with parameters)
* `rate_ad()`: 
