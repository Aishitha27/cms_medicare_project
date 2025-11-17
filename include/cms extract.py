from utils import download_zip, unzip_files

def data_pipeline(url):
    """
    Pipeline to download, extract, and save CSV data from a zip file URL.

    Parameters:
        url (str): URL to download the zip file from.
        output_files (list): List of output file paths for each CSV in the zip.
        delimiter (str): Delimiter for reading the CSV files (default is '|').
    """

    # Download the zip file
    zip_content = download_zip(url)

    # Extract CSV(s) from zip file with the specified delimiter
    unzip_files(zip_content)

if __name__ == "__main__":
    url = "https://data.cms.gov/sites/default/files/2023-04/c3d8a962-c6b8-4a59-adb5-f0495cc81fda/Outpatient.zip"

    data_pipeline(url)
