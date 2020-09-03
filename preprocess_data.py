import os
import sys

# train_files = []
# test_dir = []
mapping = {}
with open("./gldv2_dataset/train.csv") as search:
    for line in search:
        mapping[line.split(',')[0]] = line.split(',')[1].rstrip()

count = 0
with open('./input/metadata/landmark-recognition-2020/test.csv', 'w') as f:
    f.write("id,landmark_id\n")
    for root, dirs, files in os.walk("./input/landmark-recognition-2020/test"):
        for name in files:
            count += 1
            file_name = name.split('.')[0]
            land_id = mapping[file_name]

            f.write("%s,%s\n" % (file_name, land_id))
            print(count, end="\r")

    # for name in dirs:
    #     names.append(name)
        # for root, dirs, files in os.walk("./input/data/val"):
        #     # for name in files:
        #     #     test_names.append(name)
        #     for name in dirs:
        #         test_dir.append(name)

        # train_paths = []
        # os.rename("path/to/current/file.foo", "path/to/new/destination/for/file.foo")

        # for train in train_dir:
        #     for root, dirs, files in os.walk("./input/data/train/" + train):
        #         for name in files:
        #             curr = "./input/data/train/" + train + '/' + name
        #             path = './input/landmark-recognition-2020/train/'
        #             for i in range(0, 3):
        #                 path += name[i] + '/'

        #             path = path + name
        #             os.rename(curr, path)

        # for test in test_dir:
        #     for root, dirs, files in os.walk("./input/data/val/" + test):
        #         for name in files:
        #             curr = "./input/data/val/" + test + '/' + name
        #             path = './input/landmark-recognition-2020/test/'
        #             for i in range(0, 3):
        #                 path += name[i] + '/'

        #             path = path + name
        #             os.rename(curr, path)

        # test_paths = []

        # for test in test_names:
        #     path = './test/'
        #     for i in range(0, 3):
        #         path += test[i]
        #         if(i < 2):
        #             path += '/'
        #     if(path not in test_paths):
        #         test_paths.append(path)

        # fw = open("train_paths.txt", "w")
        # for item in train_paths:
        #     fw.write(item + '\n')

        # fw = open("test_paths.txt", "w")
        # for item in test_paths:
        #     fw.write(item + '\n')
