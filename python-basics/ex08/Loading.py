# from tqdm import tqdm
# from time import sleep
# def ft_tqdm(lst: range) -> None:
#     step: int = int(len(lst) / 100)
#     percentage: int = 0
#     for i in range(0, len(lst) + 1, step):
#         progress_bar(percentage, i, len(lst))
#         percentage += 1
#         yield

# def progress_bar(perentage: int, value:float, total: int) -> None:
#     print(f"{perentage}% [", end='')
#     for i in range(perentage):
#         print("=", end='')
#     for i in range(perentage, 99):
#         print(" ", end='')
#     print(f"] {int(value)}/{total}\r", end='', flush=True)
    

# for elem in ft_tqdm(range(100)):
#     sleep(0.05)