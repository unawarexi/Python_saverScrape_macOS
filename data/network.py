import http.client
import ssl
import urllib.parse
from typing import Tuple

def connect(parsed_url: urllib.parse.ParseResult) -> http.client.HTTPConnection:
    context = ssl._create_unverified_context()
    conn = (
        http.client.HTTPSConnection(parsed_url.netloc, context=context)
        if parsed_url.scheme == "https"
        else http.client.HTTPConnection(parsed_url.netloc)
    )
    return conn

def get_content_length(url: str) -> int:
    parsed_url = urllib.parse.urlparse(url)
    conn = connect(parsed_url)
    conn.request("HEAD", parsed_url.path)
    r = conn.getresponse()
    content_length = int(r.getheader("Content-Length", -1))
    conn.close()
    return content_length

def download_file_with_progress(download: Tuple[str, str, str]) -> None:
    """
    Downloads a file with progress display.
    """
    label, url, file_path = download
    parsed_url = urllib.parse.urlparse(url)
    conn = connect(parsed_url)
    conn.request("GET", parsed_url.path)
    r = conn.getresponse()
    
    if r.status == 200:
        content_length = int(r.getheader("Content-Length", 0))
        downloaded = 0
        chunk_size = 1024 * 1024  # 1 MB
        
        with open(file_path, "wb") as f:
            while True:
                chunk = r.read(chunk_size)
                if not chunk:
                    break
                f.write(chunk)
                downloaded += len(chunk)
                
                # Calculate and print the download percentage
                percent = (downloaded / content_length) * 100
                print(f"\rDownloading '{label}'... {percent:.2f}%", end="")
        
    conn.close()
