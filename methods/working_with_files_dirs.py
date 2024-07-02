from os import makedirs
import shutil

from .constants import path_for_translations_chn


def chinese_unpacking():
    with open(
        f'{path_for_translations_chn}/chinese_translations.csv',
        'a',
        encoding='utf-8'
    ) as chn:
        global chinese_wordlist
        for key, value in chinese_wordlist.items():
            chn.write(key.strip() + ';' + value + '\n')


def printing_translations_into_csv(
        word: str, translated_word: str, file_name: str
) -> None:
    """Заносим переводы в csv в папку trans_csv_eng."""
    file_name.write(word.strip() + ';' + translated_word + '\n')


def chinese_recordings(
        word: str, translated_word: str
) -> None:
    global chinese_wordlist
    chinese_wordlist[word] = translated_word


def making_rep(file_path):

    # macOS version
    # new_file_path = '/'.join(
    # file_path.split('/')[:-1]
    # ).replace(
    #     'trans_input_files',
    #     'trans_result_files'
    # )

    # windows version
    new_file_path = '\\'.join(
        file_path.split('\\')[:-1]
    ).replace(
        'trans_input_files',
        'trans_result_files'
    )
    try:
        makedirs(new_file_path)
        return new_file_path
    except Exception:
        return new_file_path


def making_other_files(file):

    # macOS version
    # name_file = file.split('/')[0]
    # new_dir = making_rep(file)
    # shutil.copy2(file, f'{new_dir}/{name_file}')

    # windows version
    name_file = file.split('\\')[0]
    new_dir = making_rep(file)
    shutil.copy2(file, f'{new_dir}\\{name_file}')



chinese_wordlist = dict()
