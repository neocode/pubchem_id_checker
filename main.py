import json
import requests
import urllib.parse as urllib_parse
from fastapi import FastAPI

app = FastAPI(title="PubChem CID and SID Checker", description="Getting PubChem CID or SID by name.", version="1.0")

@app.get("/get_cid_by_name/{name}")
async def get_cid_by_name(name: str):
    try:
        data = requests.get("https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{}/JSON".\
                            format(urllib_parse.quote(name))).json()
        return str(data["PC_Compounds"][0]["id"]["id"]["cid"])
    except:
        return None
    
@app.get("/get_sid_by_name/{name}")
async def get_sid_by_name(name: str):
    try:
        data = requests.get("https://pubchem.ncbi.nlm.nih.gov/rest/pug/substance/name/{}/sids/json".\
                            format(urllib_parse.quote(name))).json()
        sid = str(data["IdentifierList"]["SID"])
        sid = sid.replace("[", "")
        sid = sid.replace("]", "")
        return sid
    except:
        return None
