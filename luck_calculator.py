import random
from collections import Counter
import matplotlib.pyplot as plt

def chance():
    rand1 = random.randint(0, 30)
    rand2 = random.randint(0, 30)
    return (rand1 + rand2) - 30

def stats(lst):
    count = Counter(lst)
    # results(lst)
    print("Now for the stats:")
    # Sorted by number because tuple (number, frequency) and number is the first item
    sorted_items = sorted(count.items())
    freq = []
    numbers = []
    probability = []
    probability_percent = []
    all_numbers = sum(count.values())
    for number, frequency in sorted_items:
        print(f'Number {number} occurred this often: {frequency}')
        prob = frequency / all_numbers
        freq.append(frequency)
        numbers.append(number)
        probability.append(prob)
        probability_percent.append(prob * 100)
    for number, frequency in sorted_items:
        prob = frequency / all_numbers
        print(f'Number {number} has this chance to occure: {prob*100}')

    most_common_item = count.most_common(1)
    print(f'The most common number was: {most_common_item[0][0]}')

    plot_stats(numbers, freq, probability_percent)
    
def plot_stats(numbers, freq, probability):
    plt.figure(figsize=(10, 5))
    # Plot 1: Frequency
    plt.subplot(1, 2, 1)
    plt.bar(numbers, freq, color='blue')
    plt.xlabel('Glück')
    plt.ylabel('Häufigkeit')
    plt.title('Häufigkeit von Glück')
    # Plot 2: Probability
    plt.subplot(1, 2, 2)
    plt.bar(numbers, probability, color='green')
    plt.xlabel('Glück')
    plt.ylabel('Wahrscheinlichkeit')
    plt.title('Wahrscheinlichkeit von Glück')

    plt.tight_layout()
    plt.show()

def results(lst):
    print("These are the results:")
    for num in lst:
        print(num)

def loop(x):
    counter = 0
    lst = list()
    for _ in range(x):
        rand = chance()
        lst.append(rand)
        counter += rand
    # print("Counter:", counter)
    return lst

def main():
    x = 10000000
    results = loop(x)
    stats(results)

if __name__ == "__main__":
    main()
