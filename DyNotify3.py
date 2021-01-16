# Using FASTAPI

# library block
from fastapi import FastAPI, File, UploadFile, Security, Depends, HTTPException
from fastapi.security.api_key import APIKeyQuery, APIKeyHeader, APIKey
from typing import List
import uvicorn
from PIL import Image, ImageChops, ImageStat
from starlette.status import HTTP_403_FORBIDDEN


API_KEY = 'kmrhn74zgzcq4nqb'
API_KEY_NAME = 'access_token'

api_key_query = APIKeyQuery(name = API_KEY_NAME, auto_error = False)
api_key_header = APIKeyHeader(name = API_KEY_NAME, auto_error = False)

app = FastAPI()

def get_api_key(
    api_key_query: str = Security(api_key_query),
    api_key_header: str = Security(api_key_header),
):

    if api_key_query == API_KEY:
        return api_key_query
    elif api_key_header == API_KEY:
        return api_key_header
    else:
        raise HTTPException(status_code=HTTP_403_FORBIDDEN, detail="Could not validate credentials")



@app.post("/image")
async def upload_file(api_key: APIKey = Depends(get_api_key), files: List[UploadFile] = File(...)):
    q = ImageStat.Stat(
        ImageChops.difference(Image.open(files[0].file).convert('LA'), Image.open(files[1].file).convert('LA')))
    similarity = sum(q.mean) / (len(q.mean) * 255)
    print(q)
    return {'% similarity': 100 * similarity}


if __name__ == "__main__":
    uvicorn.run(app, host = '127.0.0.1', port = 5000)




