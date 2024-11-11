def pngBlast(imageList, level):
    for image in imageList:
        with open("readImage/" + image, "rb") as f:
            imageData = f.read()

            width = imageData.split("IHDR".encode("utf-8"))[1][2:4]
            hight = imageData.split("IHDR".encode("utf-8"))[1][6:8]

            imageHead = imageData.split("IHDR".encode("utf-8"))[0] # 图片头
            imageData = imageData.split("IHDR".encode("utf-8"))[1] # 图片数据


            width = int.from_bytes(width, "big")
            hight = int.from_bytes(hight, "big")
            # 这AI读我剪切板
        # 根据范围，生成宽度 加减 1~100 的不同图片 先把宽度爆破出来
            imageData = bytearray(imageData) # 图片数据变为可变的字节序列

        widthAdd = width
        widthReduce = width
        
        for i in range(1, level):
            with open(f"writeImage/{i}增{image}" , "wb") as f:
                bytes1 = (widthAdd + i).to_bytes(2, "big")
                byte1 = bytes1[0:1]  # 获取第一个字节
                byte2 = bytes1[1:2]  # 获取第二个字节

                imageData[2:3] = byte1
                imageData[3:4] = byte2

                f.write(imageHead + b'IHDR' + imageData)
        
        for i in range(1, level):
            with open(f"writeImage/{i}降{image}" , "wb") as f:
                
                bytes1 = (widthReduce - i).to_bytes(2, "big")
                byte1 = bytes1[0:1]  # 获取第一个字节
                byte2 = bytes1[1:2]  # 获取第二个字节


                imageData[2:3] = byte1
                imageData[3:4] = byte2

                f.write(imageHead + b'IHDR' + imageData)

def jpgBlast(imageList, level):
    
    for image in imageList:
        with open("readImage/" + image, "rb") as f:
            imageData = f.read()

            imageHead=imageData.split(b"\xff\xc0")[0]
            imageData = bytearray(imageData.split(b"\xff\xc0")[1])

            width = int.from_bytes(imageData[5:7], "big")

            print(width)
            widthAdd = width
            widthReduce = width

            for i in range(1, level):
                with open(f"writeImage/{i}增{image}" , "wb") as f:
                    
                    bytes1 = (widthAdd + i).to_bytes(2, "big")
                    byte1 = bytes1[0:1]  # 获取第一个字节
                    byte2 = bytes1[1:2]  # 获取第二个字节


                    
                    imageData[5:6] = byte1
                    imageData[6:7] = byte2
                    f.write(imageHead + b"\xff\xc0" + imageData)
            
            for i in range(1, level):
                with open(f"writeImage/{i}降{image}" , "wb") as f:
                    
                    bytes1 = (widthReduce - i).to_bytes(2, "big")
                    byte1 = bytes1[0:1]  # 获取第一个字节
                    byte2 = bytes1[1:2]  # 获取第二个字节


                    
                    imageData[5:6] = byte1
                    imageData[6:7] = byte2
                    f.write(imageHead + b"\xff\xc0" + imageData)


def gifBlastNotAuto(imageList, level):
    """ 需要手动指定字节序列 """
    for image in imageList:

        with open("readImage/" + image, "rb") as f:
            imageData = f.read()

            imageHead = imageData.split(b"89a")[0] + b"89a" # 图片头  
            imageData = imageData.split(b"89a")[1]

            width = int.from_bytes(imageData[1:3])
  
            imageData = bytearray(imageData) # 图片数据变为可变的字节序列

        widthAdd = width
        widthReduce = width
        print(imageData[0:2])

    # 有点难搞，先写死吧 手动定位字节位置
        for i in range(1, level):
            with open(f"writeImage/{i}增{image}" , "wb") as f:
                bytes1 = (widthAdd + i).to_bytes(2, "big")
                byte1 = bytes1[0:1]  # 获取第一个字节
                byte2 = bytes1[1:2]  # 获取第二个字节
                
                # 修改头部宽高
                
                imageData[0:1] = byte2
                imageData[1:2] = byte1

                # 通过手动定位修改图片帧宽高

                imageData[32:33] = byte2
                imageData[33:34] = byte1

                f.write(imageHead + imageData)
    #             # 修改图片帧宽高  通过 2C标识 分割图片帧 

    
        for i in range(1, level):
            with open(f"writeImage/{i}减{image}" , "wb") as f:
                bytes1 = (widthReduce - i).to_bytes(2, "big")
                byte1 = bytes1[0:1]  # 获取第一个字节
                byte2 = bytes1[1:2]  # 获取第二个字节
                
                # 修改头部宽高
                
                imageData[0:1] = byte2
                imageData[1:2] = byte1

                # 通过手动定位修改图片帧宽高

                imageData[32:33] = byte2
                imageData[33:34] = byte1

                f.write(imageHead + imageData)
    #             # 修改图片帧宽高  通过 2C标识 分割图片帧 