django_slideshare
=================

Overview
--------

django_slideshare is a simple django app that helps you embed http://www.slideshare.net presentations into your django templates.

* Install the app into your django project
* In the admin panel, create a new instance of a Slideshare.
* The only required parameter is the url of a particular slideshare presentation (e.g., http://www.slideshare.net/rashmi/slideshare-zeitgeist-2009).  Upon saving the instance, django_slideshare will pull the rest of the relevant information (title, author, embed code, width, height) directly from slideshare.  You can, of course, override any of these values with your own.

Dependancies
------------
* [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/) for parsing the slideshare url.  In the future, we'll remove this dependency by implementing the slideshare developer API, rather than scrapping it from the site.

Roadmap
-------
* Implement the embed code as a template tag, instead of hard coded in the template
* add a 404 page for when the requested presentation doesn't exist
* use slideshare slug as another URI for the presentation
* Proper package/dependency management using pip, or whatever else the cool kids are using these days
* See if it is possible to use generic views, instead of writing my own
* Use the slideshare developer API, instead of storing the embed code and scraping the presentation metadata from the url
* Subscribe to a user, and automatically discover presentations from that user (with filters/querying)
* Refactor to create a slideshare python binding: perhaps fork/contribute to [PySlideShare](http://code.google.com/p/pyslideshare/)
