import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def _get_upload_link(self, disk_file_path):
        upload_url1 = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': disk_file_path, 'overwrite': 'true'}
        response = requests.get(upload_url1, headers=headers, params=params)
        return response.json()

    def upload(self, disk_file_path, file_path):
        response_href = self._get_upload_link(disk_file_path=disk_file_path)
        url = response_href.get('href', '')
        response = requests.put(url, data=open(file_path, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print('Success')

if __name__ == '__main__':
    disk_file_path = 'Нетология/test_hw_task-2.txt'
    token = 'AQAAAAALO15nAADLW9_ylVEJr0yrgjnSZcb60Pc'
    uploader = YaUploader(token)
    uploader.upload(disk_file_path=disk_file_path, file_path=r'C:\Users\kuvsh\PycharmProjects\Request_http\test_hw_task-2.txt')
