import fitz
art_num = 1
#document = fitz.open("C:\\Users\\adria\\Downloads\\D19970483Lj.pdf")

#for page in document:
#    text = page.get_text()
#    with open("C:\\Users\\adria\\Desktop\\konstytucja\\konstytucja_pisemnie.txt", 'a') as file:
#        file.write(text)



with open("C:\\Users\\adria\\Desktop\\konstytucja\\konstytucja_pisemnie.txt", 'r') as file:
    lines = file.readlines()
    textlen = 0
    for line in lines:
        textlen+=1
        for c in line:
            textlen+=1
    text1 = ""
    checked = False

    for line in lines:
        for art in range(len(line)):
        
            text1 += line[art]
            if str(text1).__contains__("Art.") and checked == False:
                text1='Art.'
                checked = True

            if len(text1)>10 and text1.endswith("Art."):
                checked = False

                with open(f'C:\\Users\\adria\\Desktop\\konstytucja\\konstytucja_art{art_num}.txt', 'a') as f:
                    f.write(text1[:-4]) 
                text1='Art.'
                art_num+=1
           