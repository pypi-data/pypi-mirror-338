from selenium import webdriver
from selenium.common.exceptions import (
    StaleElementReferenceException,
    TimeoutException,
    WebDriverException,
)
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from ..core.logging import get_logger

logger = get_logger(__name__)


def get_drive_file_list(folder_id: str, retries: int = 3) -> dict[str, str]:
    """Scrapes a Google Drive folder to extract file IDs and names.

    Uses Selenium to load and scroll through all files in a Google Drive folder,
    extracting their IDs and filenames. The function scrolls through the entire
    folder contents and stops when no new files are loaded after multiple attempts.

    Args:
        folder_id: The Google Drive folder ID to scrape.
        retries: The number of retries to attempt if the page does not load.
    Returns:
        A dictionary mapping filenames (without extensions) to file IDs.
    """
    seen_ids = set()
    same_count_repeats = 0
    all_files = {}

    url = f'https://drive.google.com/drive/folders/{folder_id}'

    logger.info('Starting Google Drive folder scrape', folder_id=folder_id, url=url)

    options = Options()
    options.add_argument('--headless=new')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=900x6000')

    driver: WebDriver | None = None

    try:
        driver = webdriver.Chrome(options=options)

        driver.get(url)
        logger.info('Navigated to Google Drive folder', url=url)

        while same_count_repeats < retries:
            try:
                # Use explicit wait instead of time.sleep
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located(
                        (By.CSS_SELECTOR, 'c-wiz > div:first-of-type[data-id]')
                    )
                )
            except TimeoutException:
                logger.warning(
                    'Timeout waiting for files to load', attempt=same_count_repeats + 1
                )
                same_count_repeats += 1
                continue

            try:
                files = driver.find_elements(
                    By.CSS_SELECTOR, 'c-wiz > div:first-of-type[data-id]'
                )
            except StaleElementReferenceException:
                logger.warning('Stale element reference, retrying')
                continue
            except WebDriverException as e:
                logger.error('WebDriver error while finding elements', error=str(e))
                break

            current_ids = {
                f.get_attribute('data-id') for f in files if f.get_attribute('data-id')
            }

            newly_loaded = current_ids - seen_ids

            for el in files:
                file_id = el.get_attribute('data-id')
                if not file_id:
                    continue

                try:
                    filename = el.find_element(
                        By.CSS_SELECTOR, 'div[data-column-field="6"] > div:last-of-type'
                    ).text
                    all_files[file_id] = filename
                except WebDriverException as e:
                    logger.warning(
                        'Failed to extract filename for file',
                        file_id=file_id,
                        error=str(e),
                    )

            if not newly_loaded:
                same_count_repeats += 1
            else:
                same_count_repeats = 0

            seen_ids.update(current_ids)

            if files:
                try:
                    driver.execute_script(
                        "arguments[0].scrollIntoView({behavior: 'auto', block: 'end'});",
                        files[-1],
                    )
                except WebDriverException as e:
                    logger.error('Failed to scroll', error=str(e))
                    break
    except Exception as e:
        logger.exception('Unexpected error during Google Drive scraping', error=str(e))
        raise
    finally:
        if driver:
            driver.quit()
            logger.debug('WebDriver closed')

    final_file_id_list = {}
    for id_, filename in all_files.items():
        match_id = filename.split('.')[0]
        final_file_id_list[match_id] = id_

    logger.info(
        'Google Drive folder scrape complete',
        folder_id=folder_id,
        total_files=len(final_file_id_list),
    )
    return final_file_id_list
