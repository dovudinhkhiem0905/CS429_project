import scrapy
import os

class MyCrawler(scrapy.Spider):
    name = 'mycrawler'
    allowed_domains = ['crawler-test.com']
    start_urls = ['https://crawler-test.com/']
    page_count = 0  # Initialize a counter for the pages

    custom_settings = {
        'DEPTH_LIMIT': 3,
        'CLOSESPIDER_PAGECOUNT': 100
    }

    def parse(self, response):
        self.page_count += 1  # Increment the page counter
        output_dir = 'output'
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Format filename to include the page count
        filename = f'{output_dir}/result_{self.page_count}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')

        links = response.css('a::attr(href)').getall()
        for link in links:
            if link is not None and response.urljoin(link).startswith("http"):
                yield response.follow(link, self.parse)
