import re
import os


def split_text_into_chunks(file_path, chunk_size=3000):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        sentences = re.split(r'(?<=[.?!])\s+', text)
        chunks = []
        chunk = ''
        word_count = 0
        for sentence in sentences:
            sentence += ' '  # add space at end to compensate for split
            words = sentence.split()
            sentence_word_count = len(words)
            if word_count + sentence_word_count <= chunk_size:
                chunk += sentence
                word_count += sentence_word_count
            else:
                chunks.append(chunk.strip())
                chunk = sentence
                word_count = sentence_word_count
        if chunk:
            chunks.append(chunk.strip())
        return chunks


def write_chunks_to_files(chunks, filename):
    for i, chunk in enumerate(chunks):
        file_name = f'{filename}_split.txt'
        with open(file_name, 'a', encoding='utf-8') as file:
            file.write(chunk + '\n\n\n\n')


if __name__ == '__main__':
    # wait for input file to be added to input folder
    while True:
        input_files = os.listdir('input')
        output_files = os.listdir('output')
        if len(input_files) == 0:
            print('No input file found. Please add a file to the input folder')
            input('Press enter to continue or press Ctrl+C to exit...')
        elif len(output_files) > 0:
            print('Output folder is not empty.')
            clear = input('Do you want to clear the output folder? (Y/N)')
            if clear.lower() == 'y':
                for output_file in output_files:
                    os.remove(f'output/{output_file}')
                print('Output folder cleared')
                break
        else:
            print(f'Input file found ({len(input_files)}). Continuing...')
            break

    while True:
        chunk_size = input('Enter chunk size: ')
        try:
            chunk_size = int(chunk_size)
            break
        except ValueError:
            print('Invalid chunk size, enter an integer')

    print('\n')
    for input_file in input_files:
        print(f'Processing {input_file}...')
        file_base_name = os.path.basename(input_file).split('.')[0]
        chunks = split_text_into_chunks(f'input/{input_file}', chunk_size)
        write_chunks_to_files(chunks, f'output/{file_base_name}')
        print(f'Finished processing {input_file}\n\n')

    print('Finished processing all files')
    clear = input('Do you want to clear the input folder? (Y/N)')
    if clear.lower() == 'y':
        for input_file in input_files:
            os.remove(f'input/{input_file}')
        print('Input folder cleared')