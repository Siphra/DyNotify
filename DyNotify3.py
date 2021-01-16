# Using FASTAPI

# library block
from fastapi import FastAPI, File, UploadFile, Security, Depends, HTTPException
from fastapi.security.api_key import APIKeyQuery, APIKeyHeader, APIKey
from typing import List
import uvicorn
from PIL import Image, ImageChops, ImageStat
from starlette.status import HTTP_403_FORBIDDEN, HTTP_400_BAD_REQUEST

# Hardcoded API key and key name
API_KEY = 'kmrhn74zgzcq4nqb'
API_KEY_NAME = 'access_token'

# Find the API Key in either the header or query string
api_key_query = APIKeyQuery(name = API_KEY_NAME, auto_error = False)
api_key_header = APIKeyHeader(name = API_KEY_NAME, auto_error = False)

# Call the app
app = FastAPI()

def get_api_key(
    api_key_query: str = Security(api_key_query),
    api_key_header: str = Security(api_key_header),
):
    """
    Gets the API key, this is a dependency for our /images comparison POST

    Args:
        api_key_query:          Looks for the api key in the query of a request
        api_key_header:         Looks for the api key in the header of a request

    Returns:                    API KEy if valid, 403 error if not

    """

    if api_key_query == API_KEY:
        return api_key_query
    elif api_key_header == API_KEY:
        return api_key_header
    else:
        raise HTTPException(status_code=HTTP_403_FORBIDDEN, detail="Could not validate credentials")


@app.post("/images")
async def upload_file(api_key: APIKey = Depends(get_api_key), files: List[UploadFile] = File(...)):

    """
    For uploading two or more files to be checked, only two can be checked at a time, and they are hardcoded
    as the ones in List[0] and List[1]

    Args:
        api_key: Checks the API key called via the dependency (get API key) for validity
        files: Takes in two files of image type into a List

    Returns:

    """
    try:
        q = ImageStat.Stat(
            ImageChops.difference(Image.open(files[0].file).convert('LA'), Image.open(files[1].file).convert('LA')))
        similarity = sum(q.mean) / (len(q.mean) * 255)
        return {'% similarity': 100 * similarity}
    except:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="Unable to comply check file types")

# Run the app via uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host = '127.0.0.1', port = 5000)




