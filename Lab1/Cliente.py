from socket import gethostbyname, socket, AF_INET, SOCK_STREAM
from bs4 import BeautifulSoup
import os
import sys
import requests
from tqdm import tqdm
from urllib.parse import urljoin, urlparse

HTTP_HEADER_DELIMITER = b'\r\n\r\n'
CONTENT_LENGTH_FIELD = b'Content-Length:'
ONE_BYTE_LENGTH = 1


def response(sock):

    header = bytes()
    chunk = bytes()

    try:
        while HTTP_HEADER_DELIMITER not in header:
            chunk = sock.recv(ONE_BYTE_LENGTH)
            if not chunk:
                break
            else:
                header += chunk
    except socket.timeout:
        pass

    return header


def content_length(header):

    for line in header.split(b'\r\n'):
        if CONTENT_LENGTH_FIELD in line:
            return int(line[len(CONTENT_LENGTH_FIELD):])
    return 0


def get_body(sock, length):

    body = bytes()
    data = bytes()

    while True:
        data = sock.recv(length)
        if len(data) <= 0:
            break
        else:
            body += data

    return body


def write_body(name_file, extension, body):

    try:
        file = open('./{}.{}'.format(name_file, extension), 'w+')
        file.write(body.decode('latin-1'))
        file.close()
    except:
        return 0
    return 1


def parser_body(file):
    content = open(file)
    soup = BeautifulSoup(content, 'html.parser')
    parser = soup.find_all('<img>', '<object> </object>',
                           '<video> </video>', '<audio> </audio>', '<source>')

    return parser

def download(url, pathname):
    """
    Downloads a file given an URL and puts it in the folder `pathname`
    """
    # if path doesn't exist, make that path dir
    if not os.path.isdir(pathname):
        os.makedirs(pathname)
    # download the body of response by chunk, not immediately
    response = requests.get(url, stream=True)
    # get the total file size
    file_size = int(response.headers.get("Content-Length", 0))
    # get the file name
    filename = os.path.join(pathname, url.split("/")[-1])
    # progress bar, changing the unit to bytes instead of iteration (default by tqdm)
    progress = tqdm(response.iter_content(1024), f"Downloading {filename}", total=file_size, unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "wb") as f:
        for data in progress.iterable:
            # write data read to the file
            f.write(data)
            # update the progress bar manually
            progress.update(len(data))

def get_all_images(url):
    """
    Returns all image URLs on a single `url`
    """
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    urls = []
    for img in tqdm(soup.find_all("img"), "Extracting images"):
        img_url = img.attrs.get("src")
        newUrl = url + img_url
        urls = [newUrl] + urls
    return urls

def main():

    from pathlib import Path
    txt = Path('data.txt').read_text()
    datosFromFile = txt.split(sep='-')
    print('txt', txt)

    host = datosFromFile[1]
    path = ''
    port = datosFromFile[2]
    name_file = 'resultado'
    extension = 'html'
    aux = 0
    fullUrl = datosFromFile[0]
    imgs = get_all_images(fullUrl)
    print("imgs", imgs)
    for img in imgs:
        # for each image, download it
        currentDirectory = os.getcwd()
        os.mkdir('icons')
        download(img, currentDirectory+'/icons')

    print(f'\n# Recibiendo informacion de http://{host}{path}')
    ip_address = host
    print(f'> Servidor remoto {host} direccion ip {ip_address}')

    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((ip_address, int(port)))
    print(f'> Conexion TCP con {ip_address}:{port} establecida')
    request = b'GET / HTTP/1.1\r\nHost: 3.217.183.77\r\n\r\n'
    sock.sendall(request)

    header = response(sock)
    print(type(header))
    print('\n# HTTP Response cabecera ({} bytes)'.format(len(header)))
    print(header)

    length = content_length(header)
    print('\n# Largo del cuerpo')
    print(f"{length} bytes")

    body = get_body(sock, length)

    if(len(body) > 1):

        print('\n# Cuerpo ({} bytes)'.format(len(body)))
        print(body)

        wfile = write_body(name_file, extension, body)

        if wfile == 1:
            print('\n# Archivo guardado')
        else:
            print('\n# Error guardando el archivo')

        if (aux == 1 and wfile == 1):

            parser = parser_body('/{}.{}'.format(name_file, extension))
            print('\n# El archivo se ha parseado: \n {}'.format(parser))
    else:
        print('\n# El archivo no tiene cuerpo ({} bytes)'.format(len(body)))


if __name__ == '__main__':
    main()