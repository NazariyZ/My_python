import dropbox

class dropBoxTool():
    def __init__(self, access_token):
        self.dbx = dropbox.Dropbox(access_token)

    def get_files_name(self, dbx_path):
        """
        Inputs:
            :param dbx_path: folder path on DropBox
        Outputs:
            :return:
        """
        files_list = self.dbx.files_list_folder(dbx_path)
        inp_filses = [x.name for x in files_list._entries_value]
        return (inp_filses)

    def download_files(self, full_file_dbx, full_file_local):
        """
        Inputs:
            :param full_file_dbx: full file path on DropBox
            :param full_file_local: full file local path
        Outputs:
            :return:
        """
        self.dbx.files_download_to_file(full_file_local, full_file_dbx, rev=None)
        return

    def upload_files(self, file_path, dbx_path='/Common_folder/'):
        """
        Inputs:
            :param file_path: local file path should be a list
            :param dbx_path: dropbox path
        Outputs:
            :return: flag download compleated
        """
        if isinstance(file_path, list):
         for x in file_path:
            dbx_filename = (x.replace('/', '\\')).split('\\')[-1]    # add back slash handle
            file = open(x, 'rb')
            is_upload = self.dbx.files_upload(file.read(), dbx_path + dbx_filename)
            # is_upload._is_downloadable_present
        elif isinstance(file_path, str):
            dbx_filename = file_path.split('\\')[-1]
            file = open(file_path, 'rb')
            is_upload = self.dbx.files_upload(file.read(), dbx_path + dbx_filename)
        return