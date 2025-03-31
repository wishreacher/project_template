from app.io import input, output

def main():
    text_from_console = input.input_text()
    text_from_file_builtin = input.read_file_builtin('input.txt')
    text_from_file_pandas = input.read_file_pandas('input.csv')

    output.output_text(text_from_console)
    output.output_text(text_from_file_builtin)
    output.output_text(text_from_file_pandas)

    output.write_file_builtin('output.txt',
                              text_from_console + '\n' + text_from_file_builtin + '\n' + text_from_file_pandas)


if __name__ == "__main__":
    main()
