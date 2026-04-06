def is_possible(n_painters, max_time, board_lengths, time_per_unit):
    painters_count = 1
    current_workload = 0
    
    for length in board_lengths:
        time_for_board = length * time_per_unit
        if time_for_board > max_time:
            return False
        
        if current_workload + time_for_board <= max_time:
            current_workload += time_for_board
        else:
            painters_count += 1
            current_workload = time_for_board
            if painters_count > n_painters:
                return False
    return True

def calculate_min_time(K, T, L):
    if not L: return 0
    low = max(L) * T
    high = sum(L) * T
    ans = high
    
    while low <= high:
        mid = (low + high) // 2
        if is_possible(K, mid, L, T):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans
def run_interactive():
    print("Програма розрахунку часу фарбування")
    try:
        K = int(input("Введіть кількість малярів (K): "))
        T = int(input("Введіть час за 1 метр (T): "))
        L_str = input("Введіть довжини щитів через пробіл (наприклад: 10 20 30): ")
        L = [int(x) for x in L_str.split()]
        
        result = calculate_min_time(K, T, L)
        print(f"\nМінімальний необхідний час: {result} хвилин")
    except ValueError:
        print("Помилка: введіть коректні числа.")

if __name__ == "__main__":
    run_interactive()
