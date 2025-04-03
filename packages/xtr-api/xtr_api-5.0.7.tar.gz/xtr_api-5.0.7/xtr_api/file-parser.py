import sys
from pathlib import Path

JPEG_IMAGES = []
JPG_IMAGES = []
PNG_IMAGES = []
SVG_IMAGES = []
MP3_AUDIO = []
MP4_VIDEO = []
DOCX_DOCUMENTS = []
TXT_FILES = []
MY_OTHER = []
ARCHIVES = []
PDF_BOOKS = []

REGISTER_EXTENSION = {
    'JPEG': JPEG_IMAGES,
    'JPG': JPG_IMAGES,
    'PNG': PNG_IMAGES,
    'SVG': SVG_IMAGES,
    'MP3': MP3_AUDIO,
    'ZIP': ARCHIVES,
    'DOCX': DOCX_DOCUMENTS,
    'TXT': TXT_FILES,
    'MP4': MP4_VIDEO,
    'PDF': PDF_BOOKS
}

FOLDERS = []
EXTENSION = set()
UNKNOWN = set()


def get_extension(filename: str) -> str:
    return Path(filename).suffix[1:].upper()


def scan(folder: Path) -> None:
    for item in folder.iterdir():
        if item.is_dir():
            if item.name not in ('archives', 'video', 'audio', 'documents', 'images', 'MY_OTHER'):
                FOLDERS.append(item)
                scan(item)
            continue

        ext = get_extension(item.name)
        fullname = folder / item.name
        if not ext:
            MY_OTHER.append(fullname)
        else:
            try:
                container = REGISTER_EXTENSION[ext]
                EXTENSION.add(ext)
                container.append(fullname)
            except KeyError:
                UNKNOWN.add(ext)
                MY_OTHER.append(fullname)


if __name__ == "__main__":
    folder_to_scan = sys.argv[1]
    print(f'Start in folder {folder_to_scan}')
    scan(Path(folder_to_scan))
    print(f'Images jpeg: {JPEG_IMAGES}')
    print(f'Images jpg: {JPG_IMAGES}')
    print(f'Images svg: {SVG_IMAGES}')
    print(f'Images png: {PNG_IMAGES}')
    print(f'Audio mp3: {MP3_AUDIO}')
    print(f'Documents docx: {DOCX_DOCUMENTS}')
    print(f'Books pdf: {PDF_BOOKS}')
    print(f'Files txt: {TXT_FILES}')
    print(f'Archives: {ARCHIVES}')
    print(f'Types of files in folder: {EXTENSION}')
    print(f'Unknown file type: {UNKNOWN}')
    print(f'MY_OTHER: {MY_OTHER}')

    print(FOLDERS)