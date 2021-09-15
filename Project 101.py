import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = input("Enter your dropbox access token here: ")
    transferData = TransferData(access_token)

    file_from = input("Enter the path of the file you need to transfer: ")
    file_to = input("Enter the full path to upload the file to your dropbox account: ")
    # API v2
    transferData.upload_file(file_from, file_to)

    print("Your file has successfully been uploaded to Dropbox.")
    
main()
