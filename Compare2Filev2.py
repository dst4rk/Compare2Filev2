import sys
import csv
from typing import List
from tqdm import tqdm

file1, file2 = sys.argv[1], sys.argv[2]

def compare_files(file1: str, file2: str) -> List[str]:
    with open(file1, "r") as f1, open(file2, "r") as f2:
        global set1,set2
        set1 = set(f1)
        set2 = set(f2)
        return list(set1.union(set2))

def write_output(result: List[str]):
    with open("results.csv", "w", newline='') as result_file:
        csv_writer = csv.writer(result_file)
        csv_writer.writerows([line.split(',') for line in result])

if __name__ == '__main__':
    result = compare_files(file1, file2)
    pbar_match = tqdm(total=len(result), desc="Matched lines")
    pbar_unmatch = tqdm(total=len(result), desc="Unmatched lines")
    for line in result:
        if line in set1 and line in set2:
            pbar_match.update(1)
        else:
            pbar_unmatch.update(1)
    pbar_match.close()
    pbar_unmatch.close()
    write_output(result)