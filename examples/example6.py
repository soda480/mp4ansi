#   -*- coding: utf-8 -*-
from mp4ansi import MP4ansi
import names, random, logging
logger = logging.getLogger(__name__)

def do_work(*args):
    last_name = names.get_last_name()
    logger.debug(f'processor is {last_name}')
    total = random.randint(50, 125)
    logger.debug(f'processing total of {total}')
    for _ in range(total):
        logger.debug(f'processed {names.get_full_name()}')
        # logger.debug('')
    logger.debug('processing completed')
    return total

def main():
    process_data = [{} for item in range(8)]
    config = {
        'id_regex': r'^processor is (?P<value>.*)$',
        'text_regex': r'^process.*$'
    }
    print('Procesing names...')
    MP4ansi(function=do_work, process_data=process_data, config=config).execute()
    print(f"Total names processed {sum([item['result'] for item in process_data])}")

if __name__ == '__main__':
    main()