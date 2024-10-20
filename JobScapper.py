from jobScrapperUtils import create_session, markdown_converter
from bs4.element import Tag
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs, unquote
import sys
class JobScrapper:
    
    def __init__(self):
        
        self.proxy = None
        self.headers = {
            "authority": "www.linkedin.com",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "accept-language": "en-US,en;q=0.9",
            "cache-control": "max-age=0",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        }


    def get_job_details(self, job_page_url: str) -> dict:
            description = self._get_job_details(job_page_url)
            return description

    def _remove_attributes(self,tag):
        for attr in list(tag.attrs):
            del tag[attr]
            
        return tag.get_text(strip=True)

    def _get_job_details(self, job_page_url: str) -> dict:
        
        
        """
        Retrieves job description and other job details by going to the job page url
        :param job_page_url:
        :return: dict
        """
        try:
            session = create_session(is_tls=False, has_retry=True)
            response = session.get(
                job_page_url, headers=self.headers, timeout=5, proxies=self.proxy
            )
            response.raise_for_status()
        except Exception as e:
            print(f"Error: {e}")
            return {}
        if response.url == "https://www.linkedin.com/signup":
            return {}

        soup = BeautifulSoup(response.text, "html.parser")
        
        job_title = soup.find("h1", class_="top-card-layout__title")
        job_company = soup.find("a", class_="topcard__org-name-link")
        location = soup.find("div", class_="topcard__flavor-row").find("span", class_="topcard__flavor--bullet")
        
        job_title = self._remove_attributes(job_title)
        job_company = self._remove_attributes(job_company)
        location = self._remove_attributes(location)
        
        div_content = soup.find(
            "div", class_=lambda x: x and "show-more-less-html__markup" in x
        )
        
        
        recruiter_link = soup.find('a', class_='message-the-recruiter__cta')

        if recruiter_link:
            recruiter_link = recruiter_link['href']
            parsed_url = urlparse(recruiter_link)
            query_params = parse_qs(parsed_url.query)

            # Retrieve and decode the 'session_redirect' parameter
            session_redirect = query_params.get('session_redirect', [None])[0]
            if session_redirect:
                session_redirect = unquote(session_redirect)
                
            recruiter_link = session_redirect
        
        description = None
        if div_content is not None:

            def remove_attributes(tag):
                for attr in list(tag.attrs):
                    del tag[attr]
                return tag

            div_content = remove_attributes(div_content)
            description = div_content.prettify(formatter="html")
            # if self.scraper_input.description_format == DescriptionFormat.MARKDOWN:
            description = markdown_converter(description)
        return {
            "company_name": job_company,
            "title": job_title,
            "location": location,
            "description": description,
            "job_url" : job_page_url,
            "recruiter_link" : recruiter_link
        }