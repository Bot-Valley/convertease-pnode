from fastapi import FastAPI, UploadFile


app = FastAPI()

@app.post("/convert/{category}")
def read_root(category: str, file: UploadFile, target_filetype: str, output_filename: str=None, max_filesize: str=None):
    print("hello")
    return {"filename": file.filename, "target": target_filetype}