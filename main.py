from algorithms.enumeration import count_palindromes_enumeration
from algorithms.dynamic_programming import count_palindromes_dynamic
from algorithms.center_expansion import count_palindromes_center_expansion
from metrics.measure_time import measure_time
from data_generator.data_generator import generate_string
from graphs.graphs import create_graph
import pandas as pd

def main():
    
    strings = [100, 200, 300, 400, 500, 600, 700, 800]
    contents = ["same_char", "diff_chars", "random", "enumeration"]
    results = []

    for content in contents:
        for string in strings:
            
            random_string = generate_string(string, content)

            iteration = []
            iteration.append(string)

            enumeration_result, enumeration_time = measure_time(count_palindromes_enumeration, random_string)
            iteration.append(enumeration_result)
            iteration.append(enumeration_time)

            dynamic_result, dynamic_time = measure_time(count_palindromes_dynamic, random_string)
            iteration.append(dynamic_result)
            iteration.append(dynamic_time)

            center_expansion_result, center_expansion_time = measure_time(count_palindromes_center_expansion, random_string)
            iteration.append(center_expansion_result)
            iteration.append(center_expansion_time)

            results.append(iteration)

    df = pd.DataFrame(results)
    print(df)
    create_graph(results=results, graphs=len(contents), contents=contents)

if __name__ == "__main__":
    main()
