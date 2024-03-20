import csv
import sys


def main():
    # Verifica se foram fornecidos os argumentos corretos na linha de comando
    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        return

    # Obtém os nomes dos arquivos do banco de dados CSV e da sequência de DNA
    database_file = sys.argv[1]
    sequence_file = sys.argv[2]

    # Lê o banco de dados CSV e a sequência de DNA
    database = read_csv(database_file)
    dna_sequence = read_dna(sequence_file)

    # Encontra a correspondência no banco de dados para a sequência de DNA
    match = find_match(database, dna_sequence)

    # Imprime o nome do indivíduo correspondente ou "No match" se não houver correspondência
    if match:
        print(match)
    else:
        print("No match")


def read_csv(file_name):
    # Inicializa um dicionário para armazenar os dados do arquivo CSV
    data = {}

    # Abre o arquivo CSV e lê seu conteúdo
    with open(file_name, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Obtém o nome do indivíduo da primeira coluna
            name = row['name']
            # Armazena as sequências STR como valores no dicionário
            data[name] = {key: int(value) for key, value in row.items() if key != 'name'}

    return data


def read_dna(file_name):
    # Abre o arquivo de sequência de DNA e lê seu conteúdo
    with open(file_name, 'r') as file:
        dna_sequence = file.read().strip()

    return dna_sequence


def find_match(database, sequence):
    # Inicializa um dicionário para armazenar as contagens de STR na sequência de DNA
    str_counts = {key: 0 for key in database[next(iter(database))].keys()}

    # Calcula as contagens de STR na sequência de DNA
    for key in str_counts:
        str_counts[key] = longest_match(sequence, key)

    # Verifica se há correspondência no banco de dados para as contagens de STR
    for name, data in database.items():
        if data == str_counts:
            return name

    return None


def longest_match(sequence, subsequence):
    """Retorna o comprimento da sequência mais longa do subsequência na sequência."""
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    for i in range(sequence_length):
        count = 0
        while True:
            start = i + count * subsequence_length
            end = start + subsequence_length

            if sequence[start:end] == subsequence:
                count += 1
            else:
                break

        longest_run = max(longest_run, count)

    return longest_run


if __name__ == "__main__":
    main()
