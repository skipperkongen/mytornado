# GreenWords API

## Methods

There are three methods in the api

* `get_random_advertisment(signals, settings): text | image | rich_media`
* `get_random_story(signals, settings): text | image | rich_media`
* `get_location(http_request): location`
* `feedback(to be decided): to be decided`
* `join_live_discussion(item_id): discussion_id`
* `get_live_comments(discussion_id, int page_num, int_page_size)`
* `put_live_comment(discussion_id, comment)`

## Datatypes

When calling a service over the web, these are url encoded.

### Item (advertisement or story)

* id
* content-type
* content
* discussion-id

Hmmm, how to distribute this data? Maybe a more general distributed solution that handles replication of content (items) + associated discussions would be useful... I'm thinking greenwords as a open platform. A network of collaborating nodes. Items don't change (easy to replicate) but discussions are dynamic (although append only) which makes them a bit harder to distribute. Maybe the append only thing is the saving feature. Yeah, that's it. Item is linked with an append only array of associated items. Each associated item is replicated.

### Signal datatype

> **Geo-targeting**
> In Internet marketing, geotargeting is the methods of determining the geolocation of a website visitor with geolocation software, and delivering different content to that visitor based on his or her location, such as latitude and longitude, country, region or state, city, metro code or zip code, organization, Internet Protocol (IP) address, ISP, and other criteria - [wikipedia](http://en.wikipedia.org/wiki/Online_advertising#Geo-targeting)

Logically this information includes:

* IP-address of client
* Geographical location of client

However, this is not information that is given by the 

### Settings datatype

* Dreadlock factor, 1-5. A value of 1 means "luxury", while 5 means "backpacker".
* Media type, one of *text*, *image*, *rich-media*
* Dimensions, one of [web banner standard sizes](http://en.wikipedia.org/wiki/Web_banner#Standard_sizes)

### Location datatype

This is the data returned for location

* Country
* Language
* Nearest city



