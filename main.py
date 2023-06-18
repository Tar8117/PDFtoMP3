import io
from pathlib import Path

import pdfplumber
from gtts import gTTS


def pdf_to_mp3(file_path='pdf_files/default_en.pdf', language='en'):
    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':

        print(f'>>> Your file: {Path(file_path).name}')
        print(f'>>> Converting...')

        with open(file=file_path, mode='rb') as f:
            pdf_file = io.BytesIO(f.read())
            with pdfplumber.PDF(pdf_file) as pdf:
                pages = [page.extract_text() for page in pdf.pages]

        text = ''.join(pages)
        text = text.replace('\n', '')

        my_audio = gTTS(text=text, lang=language, slow=False)
        file_name = Path(file_path).stem
        my_audio.save(f'{file_name}.mp3')

        return f'>>> {file_name}.mp3 is ready!'

    else:
        return 'File doesn\'t exist, enter the correct path!'


def main():
    print('Pdf to mp3 converter is ready to help you')
    file_path = input('\n>>> Enter file\'s path: ')
    language = input('>>> Choose language (format: "en" or "ru"): ')
    if file_path == '' and language == '':
        print(pdf_to_mp3())
    else:

        while language not in ('en', 'ru'):
            language = input('Support only "en" or "ru": ')
        print(pdf_to_mp3(file_path, language))


if __name__ == '__main__':
    main()
