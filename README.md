# Web Scraping - Whisky E-Commerce

<p align="center">
  <img width="300" height="300" src="https://pbs.twimg.com/profile_images/1010136727288152064/K-BhzI9K_400x400.jpg">
</p>
The Whisky Exchange is the registered trademark of Speciality Drinks Limited. Registered in England and Wales (Company No. 4449145).
About Company
Since our founders Rajbir and Sukhinder Singh shipped their first orders back in 1999, our business grew from a two-man operation to the world’s leading retailer of premium spirits.

- **Company Mission**<br>
From the day the Whisky Exchange came online, we’ve sought to build a global community that’s as passionate about quality drinks as we are. We believe in sharing our collective knowledge, encouraging exploration, and championing producers we’re passionate about. Whether you’re visiting our website, attending our events, or shopping in one of our bricks-and-mortar locations, we’ll always find the best bottles for you.

- **Company Range**<br>
We’re a team of enthusiasts and there’s nothing we love more than sharing a glass of something good. Our search for new flavours has led us all over the world, where we’ve found treasures in the unknown, the overlooked and the underrated. The range we offer is neatly curated yet diverse with a continuously-evolving selection of old & rare spirits, exclusive bottlings and new releases.

- **Company Future**<br>
Anyone who’s ever filled a cask or laid down a bottle knows that the drinks business is all about planning for tomorrow. As we go forward, we want to grow the community we’ve built in our first two decades and continue to improve our customer experience. We’ve always been early adopters and we will continue to expand our charitable efforts and our commitment to sustainability. There’s always a new spirit to discover, a new producer to get to know, or a new cocktail to make and we look forward to sharing them all with you.

# What is Web Scraping?
Web scraping, web harvesting, or web data extraction is data scraping used for extracting data from websites. Web scraping a web page involves fetching it and extracting from it. Fetching is the downloading of a page (which a browser does when a user views a page). Therefore, web crawling is a main component of web scraping, to fetch pages for later processing. Once fetched, then extraction can take place. The content of a page may be parsed, searched, reformatted, its data copied into a spreadsheet or loaded into a database. Web scrapers typically take something out of a page, to make use of it for another purpose somewhere else. An example would be to find and copy names and telephone numbers, or companies and their URLs, or e-mail addresses to a list (contact scraping).

# Web Scraping Techniques
In general, there are two ways you can do this:
- Manual: a method where you copy data by copy-pasting from a website
- Automatic: a method that uses code, an application, or a browser extension.

Web scraping is now made easier with the help of browser extensions and applications. There are six commonly used web scraping techniques, namely:
1. Copying data manually
2. Using regular expressions
3. HTML parse
4. Analyze DOM
5. Using XPath
6. Using Google Sheets

# Benefits and Problems of Web Scraping
Following are the four main advantages:
1. Getting Leads
2. Comparing Massive Data
3. Optimization of Reviews, Product Pricing and Service
4. Looking for Company Information

Although web scraping is a very helpful technique in extracting site data, there are also problems to its implementation. At least, the following five things you need to remember if you want to do it:
1. No web scraping technique is 100% effective
1. The data obtained is not always neat
1. Understanding of the structure of the website page remains an obligation
1. Your access to a website may be blocked
1. Not all websites are easy to extract data

# About The Project
The main goal of this project is to collect data from thewhiskeyexchange.com site on the types and names of alcoholic beverages, as well as descriptions, prices, ratings, and reviews of alcoholic beverages. The acquired data will then be recorded in a dataframe, which will then be extracted to a dataset file in Excel or CSV format.

# Built with
- [**pandas**](https://pandas.pydata.org/)
- [**NumPy**](https://numpy.org/)
- [**Selenium**](https://selenium-python.readthedocs.io/)
- [**Request**](https://docs.python-requests.org/en/latest/)
- [**Beautiful Soup**](https://beautiful-soup-4.readthedocs.io/en/latest/)

# Getting Started
Selenium is an open source umbrella project for a range of tools and libraries aimed at supporting browser automation. It provides a playback tool for authoring functional tests without the need to learn a test scripting language. While Beautiful Soup is a Python library for pulling data out of HTML and XML files. It works with your favorite parser to provide idiomatic ways of navigating, searching, and modifying the parse tree. It commonly saves programmers hours or days of work. last but not least is Requests, request allows you to send HTTP/1.1 requests extremely easily. There’s no need to manually add query strings to your URLs, or to form-encode your POST data. Keep-alive and HTTP connection pooling are 100% automatic, thanks to urllib3.

Read more for [**Selenium documentation**](https://selenium-python.readthedocs.io/), [**Beautiful Soup documentation**](https://beautiful-soup-4.readthedocs.io/en/latest/) and [**Request documentation**](https://docs.python-requests.org/en/latest/)
### **Prerequisites**
Here is how to run the library used in this project. First Install the list of libraries below on your device or kernel:
- Selenium <br>
  ```
  pip install selenium
  ```
- Beautiful Soup <br>
  ```
  pip install beautifulsoup4
  ```
- Request <br>
  ```
  pip install requests
  ```
