class YaUploader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def upload(self):
        """Метод загруджает файлы по списку file_list на яндекс диск"""

        import requests

        auth = {'Authorization': 'OAuth AgAAAAA0Ob4EAAaGTkK6zysB1EyvnCHHTITPRy8'}
        new_file = 'hw9.txt'

        with open(new_file, encoding='utf8') as f:
            file = f.read()

        responce = requests.get(f'https://cloud-api.yandex.net:443/v1/disk/resources/upload?path=/{file}', headers=auth)
        # print(responce.json())

        href = responce.json()['href']
        # print(href)

        push_file = requests.put(href, data=file)
        print(push_file.text)

        return 'Вернуть ответ об успешной загрузке'


if __name__ == '__main__':
    uploader = YaUploader('c:\my_folder\file.txt')
    result = uploader.upload()