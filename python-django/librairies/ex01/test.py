# from local_lib import path


# def create_folder() -> None:
#     try:
#         path.os.mkdir('test_folder')
#     except FileExistsError:
#         print('test_folder: already exist')
#     try:
#         f = open(path.os.getcwd() + '/test_folder/test_file', 'w+')
#         f.write("hello from path")
#         f.seek(0)
#         lines = f.readlines()
#         for line in lines:
#             print(line)
#     except Exception as err:
#         print(err)


# if __name__ == "__main__":
#     create_folder()
