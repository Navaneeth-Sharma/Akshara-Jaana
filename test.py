from AksharaJaana.main import ocr_engine

ocr_engine('/home/navaneeth/Desktop/NandD/OCR_kannada/kan7.jpg')
# ocr_engine('/home/navaneeth/Desktop/NandD/OCR_kannada/CamScanner 06-28-2020 12.12.10.pdf')


# def flatten(A):
#     rt = []
#     for i in A:
#         if isinstance(i,list): rt.extend(flatten(i))
#         else: rt.append(i)
#     return rt

# # A = ['1','2','3',[1,2],5]
# A = [['OUT/0/filename_0.jpg', 'OUT/0/filename_2.jpg', 'OUT/0/filename_4.jpg', 'OUT/0/filename_6.jpg', 'OUT/0/filename_8.jpg', 'OUT/0/filename_10.jpg', 'OUT/0/filename_12.jpg', 'OUT/0/filename_14.jpg', 'OUT/0/filename_16.jpg', 'OUT/0/filename_18.jpg', 'OUT/0/filename_20.jpg', 'OUT/0/filename_22.jpg', 'OUT/0/filename_24.jpg', 'OUT/0/filename_26.jpg', 'OUT/0/filename_28.jpg'], ['OUT/1/filename_0.jpg', 'OUT/1/filename_2.jpg', 'OUT/1/filename_4.jpg', 'OUT/1/filename_6.jpg', 'OUT/1/filename_8.jpg', 'OUT/1/filename_10.jpg', 'OUT/1/filename_12.jpg', 'OUT/1/filename_14.jpg', 'OUT/1/filename_16.jpg', 'OUT/1/filename_18.jpg', 'OUT/1/filename_20.jpg', 'OUT/1/filename_22.jpg', 'OUT/1/filename_24.jpg', 'OUT/1/filename_26.jpg'], ['OUT/2/filename_0.jpg', 'OUT/2/filename_2.jpg', 'OUT/2/filename_3.jpg', 'OUT/2/filename_4.jpg', 'OUT/2/filename_6.jpg']]
# # print(A.flatten())
# print(flatten(A))