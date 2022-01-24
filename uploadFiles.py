import os
import dropbox

class transferData:
    def __init__(self,access_token):
        self.access_token=access_token
    def upload_files(self, file_from, file_to,local_path):
        dbx=dropbox.Dropbox(self.access_token)
        for root, dirs, file in os.walk(file_from):
            relatve_path=os.path.relpath(local_path, file_from)
            dropbox_path=os.path.join(file_to. relative_path)
        with open(file_from,'rb') as f:
            dbx.files_upload(f.read(),file_to)

def main():
    access_token='84rKGSiMpGUAAAAAAAAAAREsbCc8aNsv_TGEoirGC2OZGzPtYGkKewX7qAJU7tEi'
    TransferData=transferData(access_token)

    x=input("enter your file name")
    y=input("enter your destination")
    TransferData.upload_files(x,y)
    print("your file has been moved")

main()