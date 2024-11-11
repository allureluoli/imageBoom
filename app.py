import imageblast
import os
imageList = os.listdir("readImage")

# 设置范围
level1= 100
level2 = 1000
level3 = 10000


if 'png' in imageList[0]:
    imageblast.pngBlast(imageList, level2)

if 'jpg' in imageList[0]:
    imageblast.pngBlast(imageList, level2)


# for image in imageList:

#     zero = bytes.fromhex('00') 
#     c2 = bytes.fromhex('2c') 
    
#     with open('misc37.txt') as f:
#         file = f.read()

#     print(file)

    # 处理完010的十六进制 ，然后再批量导入再生成图片

    # with open("readImage/" + image, "r") as f:
    #     imageData = f.read()

    #     imageHead = imageData.split(b"89a")[0] + b"89a" # 图片头  
    #     imageData = imageData.split(b"89a")[1]



        # widthStr = imageData[1:3]
        # width = int.from_bytes(imageData[1:3])


        # hex_representation = '\\x'+'\\x'.join(f'{byte:02x}' for byte in imageData)
        # # print(hex_representation)
        # imageFlag = '\\x'.join(f'{byte:02x}' for byte in (zero + c2 + zero + zero + zero + zero))


        # for i in hex_representation.split(imageFlag):
        #     print("分界线--------------")
        #     print(i)



        # print(repr(imageData))

        # data = imageData.split(zero + c2)
 

        # imageData = bytearray(imageData) # 图片数据变为可变的字节序列

#     widthAdd = width
#     widthReduce = width
#     print(imageData[0:2])

# # 有点难搞，先写死吧 手动定位字节位置
#     for i in range(1, level2):
#         with open(f"writeImage/{i}增{image}" , "wb") as f:
#             bytes1 = (widthAdd + i).to_bytes(2, "big")
#             byte1 = bytes1[0:1]  # 获取第一个字节
#             byte2 = bytes1[1:2]  # 获取第二个字节
            
#             # 修改头部宽高
            
#             imageData[0:1] = byte2
#             imageData[1:2] = byte1

#             # # 通过手动定位修改图片帧宽高

#             # imageData[32:33] = byte2
#             # imageData[33:34] = byte1



            # f.write(imageHead + imageData)
#             # 修改图片帧宽高  通过 2C标识 分割图片帧 

  
#     for i in range(1, level2):
#         with open(f"writeImage/{i}减{image}" , "wb") as f:
#             bytes1 = (widthAdd - i).to_bytes(2, "big")
#             byte1 = bytes1[0:1]  # 获取第一个字节
#             byte2 = bytes1[1:2]  # 获取第二个字节
            
#             # 修改头部宽高
            
#             imageData[0:1] = byte2
#             imageData[1:2] = byte1

#             # 通过手动定位修改图片帧宽高

#             imageData[32:33] = byte2
#             imageData[33:34] = byte1

#             f.write(imageHead + imageData)
# #             # 修改图片帧宽高  通过 2C标识 分割图片帧 
            



