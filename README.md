# ESG Susinvest - Company Analysis for ESG Investing
A web project that takes in a company name as input and scores the company based on the sentiment of news articles involving the company with regard to environment, social and governance (ESG) factors. It aims to be a tool for ESG investors to get a quick estimate of the general ESG value of a company before delving deeper via commercial tools offered by brokers (or otherwise).

This project was created for the 2022 Hack Cambridge Atlas Hackathon in Cambridge, UK.

## Rationale
While there are loads of powerful commercial tools to deal with ESG investing, our web application, SusInvest, aims to give retail and individual investors a quick estimate of how environmentally, socially and governance-conscious a company is before doing a deep dive into ESG analysis.

## Frameworks
Our web application is built using the Django framework with Python. It makes extensive use of Scrapy spiders to do web scraping, and the GDELT article database to do an initial filtering of articles.

## How it works
Users input a query string (ideally a company name). The website then filters through the enormous GDELT website (for the past three months) to find all articles that mention the company. Scrapy was then used to crawl every website returned. The number of hits of certain words were counted and weights them according to a corpus of words (eg. "sustainable": 0.1). The final score is fed into a sigmoid function and displayed on the website as a final score.
