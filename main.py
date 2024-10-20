from JobScapper import JobScrapper


if __name__ == '__main__':
    
    scrapper = JobScrapper()
    job_detail = scrapper.get_job_details("https://www.linkedin.com/jobs/view/4053111765/?alternateChannel=search&refId=XX01iI%2F%2BENcKhWYplhVhEw%3D%3D&trackingId=GLcIjljpNHue29qalUGRwg%3D%3D")
    print(job_detail)