import os 
print("file is Running")
def dirCleaner(target):
    
    os.chdir(target)
    for drt in os.listdir(f"{os.getcwd()}/"):
        
        try:
            os.rmdir(f"{drt}")
        except NotADirectoryError:
            os.remove(f"{drt}")
        except OSError:
            dirCleaner(f"{drt}/")
            os.chdir("../")     
            os.rmdir(f"{drt}")

dirCleaner("Bakchodi")

# for i in range (0,70):
#     if os.path.exists(f"TEst/works{i}"):
#         continue
#     os.mkdir(f"TEst/works{i}")
# for i in range (0,70):
#     os.rename(f"TEst/works{i}" ,f"TEst/AssII {i}")



# folders= os.listdir("TEst")
# print(folders)

# for folder in folders:
#     os.rmdir(f"TEst/{folder}")
# e

# os.chdir("TEst/")
# print(os.getcwd())
# os.mkdir("Folder3")


# os.rmdir("folder")



# os.chdir("TEst/")
# print(os.getcwd())
# os.chdir("../")
# print(os.getcwd())
# os.chdir("/")
# # print(os.getcwd())
# print(os.listdir(f"{os.getcwd()}/"))
# os.chdir("Bakchodi")
# print(os.getcwd())

# a=os.listdir(f"{os.getcwd()}")


# for elment in a:
#     try
#         os.rmdir(f"{element}")














