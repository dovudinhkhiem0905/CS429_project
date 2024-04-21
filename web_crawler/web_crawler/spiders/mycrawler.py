import scrapy
import os

class MyCrawler(scrapy.Spider):
    name = 'mycrawler'
    allowed_domains = ['example.com', 'iana.org']
    start_urls = ['http://example.com'] 

    custom_settings = {
        'DEPTH_LIMIT': 3,  # Maximum depth of crawling
        'CLOSESPIDER_PAGECOUNT': 100  # Maximum number of pages to crawl
    }

    def parse(self, response):
        # Ensure the output directory exists
        output_dir = 'output'
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Save the response body as HTML
        page = response.url.split("/")[-1]
        filename = f'{output_dir}/{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file output/{response.url.split("/")[-1]}.html')

    # Extract and follow links
        links = response.css('a::attr(href)').getall()
        for link in links:
            if link is not None and response.urljoin(link).startswith("http"):
                yield response.follow(link, self.parse)
