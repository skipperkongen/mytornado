# Online advertising

There are many types of [online advertising](http://en.wikipedia.org/wiki/Online_advertising). One type is an ad network:

> An online advertising network or ad network is a company that connects advertisers to web sites that want to host advertisements - [wikipedia](http://en.wikipedia.org/wiki/Advertising_network)

There are [three types](http://en.wikipedia.org/wiki/Advertising_network#Types_of_ad_networks) of ad networks:

* **Vertical Networks**: Full transparency for the advertiser about where their ads will run.
* **Blind Networks**: These companies offer good pricing to direct marketers in exchange for those marketers relinquishing control over where their ads will run, though some networks offer a "site opt out" method.
* **Targeted Networks**: Sometimes called “next generation” or “2.0” ad networks, these focus on specific targeting technologies such as behavioral or contextual, that have been built into an Ad server. Targeted networks specialize in using consumer [clickstream](http://en.wikipedia.org/wiki/Clickstream) data to enhance the value of the inventory they purchase.

The most algorithmically advanced ad networks use clickstreams. 

> A clickstream is the recording of the parts of the screen a computer user clicks on while web browsing or using another software application - [wikipedia](http://en.wikipedia.org/wiki/Clickstream)

We should aim for a simple solution like a vertical or blind network. Because we already know alot about the users, we don't need heavy algorithms to learn preferences.

# Big companies and their ad programmes



## Google

### AdSense

Google AdSense is a program run by Google Inc. that allows publishers in the Google Network of content sites to serve automatic text, image, video, and rich media adverts that are targeted to site content and audience. These adverts are administered, sorted, and maintained by Google, and they can generate revenue on either a per-click or per-impression basis.

Google uses its Internet search technology to serve advertisements based on website content, the user's geographical location, and other factors.

#### AdSense Types

* AdSense for Feeds
* AdSense for search
* AdSense for mobile content
* AdSense for domains
* AdSense for video

#### AdSense Links

* [AdSense homepage](adsense.google.com/)
* [AdSense on wikipedia](http://en.wikipedia.org/wiki/AdSense)
* [Guy talks about his AdSense experience](http://www.youtube.com/watch?v=Pxrl4ys9lRA)
* [Getting started with AdSense](https://support.google.com/adsense/bin/answer.py?hl=en&topic=1045719&answer=1045721&parent=1045789)

### AdWords

AdWords offers pay-per-click, i.e., cost-per-click (CPC) advertising, cost-per-thousand-impressions or cost-per-mille (CPM) advertising, and site-targeted advertising for text, banner, and rich-media ads. The AdWords program includes local, national, and international distribution. Google's text advertisements are short, consisting of one headline consisting of 25 characters and two additional text lines consisting of 35 characters each. Image ads can be one of several different Interactive Advertising Bureau (IAB) standard sizes.

#### AdWords Features

* IP address exclusion
* Frequency capping

#### AdWords Links

* [AdWords homepage](adwords.google.com/)
* [AdWords on wikipedia](http://en.wikipedia.org/wiki/AdWords)
* [Getting started with AdWords](http://support.google.com/adwords/bin/answer.py?hl=en&answer=1704410)

## Facebook

### Facebook Beacon (discontinued)

> The controversial service, which became the target of a class action lawsuit, was shut down in September 2009. Mark Zuckerberg, CEO of Facebook, said on the Facebook Blog in November 2011 that Beacon was a "mistake". [wikipedia](http://en.wikipedia.org/wiki/Facebook_Beacon)

### Social network advertising

Social network advertising is a term that is used to describe a form of Online advertising that focuses on social networking sites. One of the major benefits of advertising on a social networking site (facebook, myspace, friendster, bebo, orkut...and many others) is that advertisers can take advantage of the users demographic information and target their ads appropriately.

# Open source software for serving ads

## Python based

* [django-ad-code](https://github.com/mlavin/django-ad-code): *django-ad-code* is a reusable application for managing and rendering ad tags from third-party ad server or ad network such Adsense, DoubleClick or OpenX. *django-ad-code* is not an ad server or full ad management system. It is simply a tool to help you manage the ad tags needed to use an ad network. Last updated 2012.
* [django-adzone](https://github.com/andrewebdev/django-adzone): The concept behind *adzone* is quite simple. You have certain areas on your website reserved for adverts. The size and nature of the ads may differ for each of these areas. Adzone allows exactly this kind of functionality, by choosing 
which adds belong to certain zones. Last updated 2009.
* [django-ads](http://code.google.com/p/django-ads/): Project to create an application for help people to customize ads showing acording to URL/template/page and offers a full advertising system. Last updated 2009.
* [Adjector](http://projects.icapsid.net/adjector/roadmap): Adjector is a lightweight, fast, flexible, open-source ad server written in Python. Adjector serves plain text, HTML, and Javascript ads to your web application in several different ways, even if Adjector is running on a separate machine. It tracks views and clicks of your ads, including Google Adsense ads. Last updated 2009.

Not an ad server, but still interesting. Django app for making money on your website:

* [django-monetize](https://github.com/lethain/django-monetize)

