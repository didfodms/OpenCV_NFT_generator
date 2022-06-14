import sys
import cv2
import copy

# 배경 리스트 background[]
background = ['.\\image2\\background\\orange.png',
              '.\\image2\\background\\yellow.png',
              '.\\image2\\background\\green.png',
              '.\\image2\\background\\purple.png',
              '.\\image2\\background\\gray.png']

# 접시 리스트 dish[]
dish = ['.\\image2\\dish\\red.png',
        '.\\image2\\dish\\yellow.png',
        '.\\image2\\dish\\blue.png',
        '.\\image2\\dish\\black.png']

# 생선 리스트 fish[]
fish = ['.\\image2\\fish\\flatfish.png',
        '.\\image2\\fish\\salmon.png',
        '.\\image2\\fish\\tuna.png',
        '.\\image2\\fish\\shrimp.png']

# 효과 리스트 effect[]
effect = ['.\\image2\\effect\\good.png',
          '.\\image2\\effect\\star.png',
          '.\\image2\\effect\\heart.png',
          '.\\image2\\effect\\skeleton.png']

# 리스트 길이
background_len = len(background)
dish_len = len(dish)
fish_len = len(fish)
effect_len = len(effect)
nft_len = background_len * dish_len * fish_len * effect_len

# NFT 대량 생산을 위한 반복문 
nft_count = 1
for i in range(0, background_len) : 
    
    background = cv2.imread(background[i], cv2.IMREAD_COLOR)
    if background is None :
        print('background read error!')
        sys.exit()
              
    for j in range(0, dish_len) :
        
        dish_src = cv2.imread(dish[j], cv2.IMREAD_COLOR)
        dish_mask = cv2.imread(dish[j], cv2.IMREAD_GRAYSCALE)
        if dish_src is None or dish_mask is None :
            print('dish read error!')
            sys.exit()    
                    
        for k in range(0, fish_len) :

            fish_src = cv2.imread(fish[k], cv2.IMREAD_COLOR)
            fish_mask = cv2.imread(fish[k], cv2.IMREAD_GRAYSCALE)
            if fish_src is None or fish_mask is None :
                print('fish read error!')
                sys.exit()
                
            for l in range(0, effect_len) :
                
                effect_src = cv2.imread(effect[l], cv2.IMREAD_COLOR)
                effect_mask = cv2.imread(effect[l], cv2.IMREAD_GRAYSCALE)
                if effect_src is None or effect_mask is None :
                    print('effect read error!')
                    sys.exit()
                
                nft = copy.deepcopy(background)
                nft[dish_mask > 0] = dish_src[dish_mask > 0]
                nft[fish_mask > 0] = fish_src[fish_mask > 0]
                nft[effect_mask > 0] = effect_src[effect_mask > 0]
                    
                file_name = '.\\nft_generated\\NFT'+str(nft_count)+'.png'
                print(file_name+"\n")
                cv2.imwrite(file_name, nft)
                nft_count += 1
