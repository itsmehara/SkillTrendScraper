# main.py
import yaml
import logging
from scraper import JobPortalScraper

def setup_logging(log_config):
    logging.basicConfig(
        filename=log_config['file_path'],
        level=getattr(logging, log_config['level'])
    )

def load_config(file_path='conf.yaml'):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def main():
    # Load project configuration
    config = load_config()

    # Set up logging based on configuration
    setup_logging(config['logging'])

    # Initialize the scraper with the configuration
    scraper = JobPortalScraper(config['scraper'])

    # Run the scraper
    scraper.run()

if __name__ == "__main__":
    main()
