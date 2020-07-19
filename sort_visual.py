#importing pygame for Visualization
import pygame   
import random   
import time     

#intializing fonts
pygame.font.init()      

#assigning Width and height of the screen   
width, height  = 1000, 700          

#seting up the window
win = pygame.display.set_mode((width,height))       

#caption for the visualization screen
pygame.display.set_caption("Visualization Sort")         

#setting icon
icon = pygame.image.load("icon.png")         
pygame.display.set_icon(icon)

#intializing coordinates for buttons
button_x = 20
button_y = 20
button_width = 60
button_height = 30

#intializing coordinates for popup window
popup_x = 500
popup_y = 450
popup_width = width - popup_x
popup_height = height - popup_y

#declaring names for diffrent colors 
red = ((255,51,51))
yellow = ((255,255,51))
white = ((255,255,255))
button_color = ((64,64,64))
hover_color = ((153,255,153))
background_color = ((250,250,250))
fast_color = ((255,102,178))
slow_color = ((255,255,153))
hover_generate_color = ((255,153,51))
black = ((0,0,0))
pop_color = ((254,197,21))
pop_frame = ((167,212,30))

#intializing speed and number 
speed = 80
number = 5

#class for diffrent buttons used
class button():
    def __init__(self, x, y, color, text_color, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.text_color = text_color
    
    #function to draw button
    def draw(self,window):
        pygame.draw.rect(win,self.color,(self.x, self.y, self.width, self.height),0)

        if self.text != '':
            if self.text.isdigit():
                font = pygame.font.SysFont('comicsans', 25)
            else:
                font = pygame.font.SysFont('comicsans', 20)
            
            if self.text == 'SORTING':
                text = font.render(self.text, 1, red)
                win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))
            else:
                text = font.render(self.text, 1, self.text_color)
                win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    #function to check if mouse is over the button        
    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False

#creating diffrent buttons
#frame
frame = button(0,0,button_color, white,width,(button_height * 2 + 10))

#guide
guide = button(0,(button_height * 2 + 10),slow_color, black,width,(button_height * 2),'click generate to create list & use left and right arrow to increase or decrease elements & click fast or slow to adjust sorting speed & click sort type to start')

#title button
title = button(button_x, button_y, button_color, white, button_width, button_height, 'SORTING')

#bubble sort button
button_x = (button_x + button_width + 20)
bubble_button = button(button_x, button_y, button_color, white, button_width, button_height, 'Bubble')

#insertion sort button
button_x = (button_x + button_width + 10)
insertion_button = button(button_x, button_y, button_color, white, button_width, button_height, 'Insertion')

#selection sort button
button_x = (button_x + button_width + 10)
selection_button = button(button_x, button_y, button_color, white, button_width, button_height, 'Selection')

#merge sort button
button_x = (button_x + button_width + 10)
merge_button = button(button_x, button_y, button_color, white, button_width, button_height, 'Merge')

#heap sort button
button_x = (button_x + button_width + 10)
heap_button = button(button_x, button_y, button_color, white, button_width, button_height, 'Heap')

#quick sort button
button_x = (button_x + button_width + 10)
quick_button = button(button_x, button_y, button_color, white, button_width, button_height, 'Quick')

#no of element 
button_x = (button_x + button_width + 10)
number_x = button_x + 45

element_button = button(button_x , button_y + 20, button_color, white, button_width + 40, button_height/2, 'No. of Element')

#fast button
button_x = (button_x + button_width + 40)
fast_button = button(button_x, button_y, button_color, white, button_width - 5, button_height, 'Fast')

#slider 
button_x = (button_x + button_width - 5 + 10)
speed_x = button_x

speed_button = button(button_x, button_y + 20, white, white, button_width/2, button_height/3)

#slow button
button_x = (button_x + button_width/2 + 10)
slow_button = button(button_x, button_y, button_color, white, button_width - 5, button_height, 'Slow')

#generate button
button_x = (button_x + button_width - 5 + 60)
generate_button = button(button_x, button_y - 5, button_color, white, button_width + 10, button_height + 10, 'Generate')

#function to display pseudo code
def blit_text(max_width, max_height, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= (pos[0] + max_width):
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            
            win.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.

#function to redraw the window
def redraw_window():
    
    frame.draw(win)
    guide.draw(win)
    title.draw(win)
    bubble_button.draw(win)
    insertion_button.draw(win)
    selection_button.draw(win)
    merge_button.draw(win)
    heap_button.draw(win)
    quick_button.draw(win)
    slow_button.draw(win)
    fast_button.draw(win)
    speed_change_button = button(speed_x + (speed / 10), button_y + 20, black, white, 10, button_height/3)
    speed_button.draw(win)
    speed_change_button.draw(win)
    number_display_button = button(number_x , button_y, button_color, white, 10, button_height/2, str(number))
    number_display_button.draw(win)
    element_button.draw(win)
    generate_button.draw(win)
    pygame.display.update()

#function to redraw pseudo code and pop window
def redraw_pseudo(sort_type, pseudo_text):
    font = pygame.font.SysFont('comicsans', 35)
    pseudo_font = pygame.font.SysFont('Arial', 20)
    pop_text = font.render(sort_type, 1, button_color)

    if sort_type == 'Bubble Sort':
        x = 650
        y = 450
        x_width = width - x
        y_height = height - y

        pygame.draw.rect(win, pop_color, (x, y, x_width, y_height))
        pygame.draw.rect(win, pop_frame, (x, y, x_width, y_height / 8))
        win.blit(pop_text, (x + (x_width/2 - pop_text.get_width()/2), y + (y_height/16 - pop_text.get_height()/2)))
        blit_text(x_width, (y_height - (y_height / 8)), pseudo_text, ((x + 10), (y + (y_height / 8) + 2)), pseudo_font)

    else:
        pygame.draw.rect(win, pop_color, (popup_x, popup_y, popup_width, popup_height))
        pygame.draw.rect(win, pop_frame, (popup_x, popup_y, popup_width, popup_height / 8))
        win.blit(pop_text, (popup_x + (popup_width/2 - pop_text.get_width()/2), popup_y + (popup_height/16 - pop_text.get_height()/2)))
        blit_text(popup_width, (popup_height - (popup_height / 8)), pseudo_text, ((popup_x + 10), (popup_y + (popup_height / 8) + 2)), pseudo_font)
    pygame.display.update()

#algorithm for insertion sort
def insertion_sort(list, x, y, width, speed):
    name = 'Insertion Sort'
    code = "\nStep 1 - If it is the first element, it is already sorted. return 1;\n"\
    "Step 2 - Pick next element\n"\
    "Step 3 - Compare with all elements in the sorted sub-list\n"\
    "Step 4 - Shift all the elements in the sorted sub-list that is greater \n"\
    "than the value to be sorted\n"\
    "Step 5 - Insert the value\n"\
    "Step 6 - Repeat until list is sorted"
    for i in range(1,len(list)):
            
            key = list[i]
            j=i-1
            while j >= 0 and key < list[j]:
                list[j+1] = list[j]
                j = j-1

                win.fill(background_color)

                show_sorting(list, j, x, y, width, yellow)

                pygame.time.delay(speed)

                redraw_window()
                redraw_pseudo(name, code)

            list[j+1] = key   

#algorithm for bubble sort
def bubble_sort(list, x, y, width, speed):
    name = 'Bubble Sort'
    code = "begin BubbleSort(list)\n\n"\
    "for all elements of list\n"\
    "   if list[i] > list[i+1]\n"\
    "       swap(list[i], list[i+1])\n"\
    "   end if\n"\
    "end for\n"\
    "return list\n"\
    "end BubbleSort"

    for i in range(len(list)):

        for j in range(0,len(list)-i-1):

            if list[j] > list[j+1]:
                list[j+1],list[j] = list[j],list[j+1]

            win.fill(background_color)

            show_sorting(list, j, x, y, width, yellow)
            
            pygame.time.delay(speed)

            redraw_window()
            redraw_pseudo(name, code)

#algorithm for selection sort
def selection_sort(list, x, y, width, speed):
    name = 'Selection Sort'
    code = "Step 1 − Set MIN to location 0\n\n"\
    "Step 2 − Search the minimum element in the list\n\n"\
    "Step 3 − Swap with value at location MIN\n\n"\
    "Step 4 − Increment MIN to point to next element\n\n"\
    "Step 5 − Repeat until list is sorted"
    for i in range(len(list)):
        min_index = i

        for j in range(i+1,len(list)):
            if list[j] < list[min_index]:
                min_index = j

            win.fill(background_color)

            show_sorting(list, j, x, y, width, yellow)

            pygame.time.delay(speed)

            redraw_window()
            redraw_pseudo(name, code)

        list[i],list[min_index] = list[min_index],list[i]
    
    show_sorting(list, j, x, y, width, yellow)

    pygame.time.delay(speed)

    redraw_window()
    redraw_pseudo(name, code)

#algorithm for merge sort
def merge_sort(list, x, y, width, speed):
    name = 'Merge Sort'
    code = "\nStep 1 − if it is only one element in the list it is already sorted, return.\n\n"\
    "Step 2 − divide the list recursively into two halves until it can no more be divided.\n\n"\
    "Step 3 − merge the smaller lists into new list in sorted order.\n"
    list1 = list

    def mergesort(list):
        if len(list)>1:

            mid = len(list) // 2
            left = list[:mid]
            right = list[mid:]

            mergesort(left)
            mergesort(right)

            i = j = k = 0

            while i < len(left) and j < len(right):

                if left[i] < right[j]:
                    list[k] = left[i]
                    i = i + 1

                    win.fill(background_color)
                    build_initial_list(list1, x, y, width, red)
                    show_sorting(list, i, x, y + 220, width, yellow)

                else:
                    list[k] = right[j]
                    j = j + 1

                    win.fill(background_color)
                    build_initial_list(list1, x, y, width, red)
                    show_sorting(list, j, x, y + 220, width, yellow)

                k = k + 1

                pygame.time.delay(speed)

                redraw_window()
                redraw_pseudo(name, code)            
                           
            while i < len(left):
                list[k] = left[i]
                i = i + 1
                k = k + 1

                win.fill(background_color)
                build_initial_list(list1, x, y, width, red)
                show_sorting(list, k, x, y + 220, width, yellow)

                pygame.time.delay(speed)

                redraw_window()
                redraw_pseudo(name, code)            
                
            
            while j < len(right):
                list[k] = right[j]
                j = j + 1
                k = k + 1

                win.fill(background_color)
                build_initial_list(list1, x, y, width, red)
                show_sorting(list, k, x, y + 220, width, yellow)

                pygame.time.delay(speed)

                redraw_window()
                redraw_pseudo(name, code)
        redraw_pseudo(name,code)

    mergesort(list)
    win.fill(background_color)
    build_initial_list(list, x, y, width, red)
    redraw_pseudo(name, code)

#algorithm for heap sort
def heap_sort(list, x, y, width, speed):
    name = 'Heap Sort'
    code = "Step 1 - Build a max heap from the input data.\n\n"\
    "Step 2 - At this point, the largest item is stored at the\n"\
    "root of the heap. Replace it with the last item of the heap\n"\
    "followed by reducing the size of heap by 1.\n"\
    "Finally, heapify the root of tree.\n\n"\
    "Step 3 - Repeat above steps while size of heap is greater than 1"

    def heapify(list,size,index):

        largest = index

        left = 2 * index + 1
        right = 2 * index + 2

        if left < size and list[left] > list[index]:
            largest = left

        if right < size and list[right] > list[largest]:
            largest = right

        if largest != index:
            list[index],list[largest] = list[largest],list[index]
        
            heapify(list,size,largest)

    def heapsort(list):
        size = len(list)

        for i in range(size // 2 - 1, -1, -1):
            heapify(list,size,i)

            win.fill(background_color)

            show_sorting(list, i, x, y, width, yellow)

            pygame.time.delay(speed)

            redraw_window()
            redraw_pseudo(name, code)            

        for i in range(size - 1, 0, -1):
            list[i],list[0] = list[0],list[i]
            heapify(list, i, 0)

            win.fill(background_color)

            show_sorting(list, i, x, y, width, yellow)

            pygame.time.delay(speed)

            redraw_window()
            redraw_pseudo(name, code)            

    heapsort(list)

#algorithm for quick sort
def quick_sort(list, x, y, width, speed):
    name = 'Quick Sort'
    code = "Step 1 − Choose the highest index value has pivot\n"\
    "Step 2 − Take two variables to point left and right of the list excluding pivot\n"\
    "Step 3 − left points to the low index\n"\
    "Step 4 − right points to the high\n"\
    "Step 5 − while value at left is less than pivot move right\n"\
    "Step 6 − while value at right is greater than pivot move left\n"\
    "Step 7 − if both step 5 and step 6 does not match swap left and right\n"\
    "Step 8 − if left ≥ right, the point where they met is new pivot\n"

    low = 0
    max = len(list) - 1

    def partition(list,low,max):

        pivot = list[max]
        i = low - 1

        for j in range(low,max):

            if list[j] < pivot:
                i = i + 1
                list[i],list[j] = list[j],list[i]

            win.fill(background_color)

            show_sorting(list, j, x, y, width, yellow)

            pygame.time.delay(speed)

            redraw_window()
            redraw_pseudo(name, code)

        list[i+1],list[max] = list[max],list[i+1]

        return i+1
    
    def quicksort(list,low,max):

        if low < max:

            index = partition(list,low,max)

            quicksort(list, low, index - 1)
            quicksort(list, index + 1, max)

            win.fill(background_color)

            show_sorting(list, index, x, y, width, yellow)

            pygame.time.delay(speed)

            redraw_window()
            redraw_pseudo(name, code)

    quicksort(list, low, max)

#fucntion to build the list of numbers
def build_initial_list(list, x, y, width, color1):

    font = pygame.font.SysFont('comicsans', 20)
    win.fill((250,250,250))
    for i in range(len(list)):
        pygame.draw.rect(win,color1,(x + (width+5) * i, y, width, -(2 * list[i])))
        no_text = str(list[i])
        text = font.render(no_text, 1, (0,0,0))
        if list[i] > 9:
            win.blit(text, ((x + (width+5) * i) + (width/2 - text.get_width()/2), (y - text.get_height()/2 - 5)))
        else:
            win.blit(text, ((x + (width+5) * i) + (width/2 - text.get_width()/2), (y - (2 * list[i]) - text.get_height()/2 - 8)))

#function to build constantly updating list
def show_sorting(list,j, x, y, width, color2):
    font = pygame.font.SysFont('comicsans', 20)
    for i in range(len(list)):
        if i == j:
            pygame.draw.rect(win,color2,(x + (width+5) * i, y, width, -(2 * list[i])))
        else:
            pygame.draw.rect(win,red,(x + (width+5) * i, y, width, -(2 * list[i])))

        no_text = str(list[i])
        text = font.render(no_text, 1, (0,0,0))
        if list[i] > 9:
            win.blit(text, ((x + (width+5) * i) + (width/2 - text.get_width()/2), (y - text.get_height()/2 - 5)))
        else:
            win.blit(text, ((x + (width+5) * i) + (width/2 - text.get_width()/2), (y - (2 * list[i]) - text.get_height()/2 - 8)))

#main function
def main():
    run = True
    FPS = 60
    x = 30
    y = 350
    width = 20
    global number
    global speed

    list = []

    clock = pygame.time.Clock()

    win.fill(background_color)

    #main loop
    while run:
        clock.tick(FPS)
        redraw_window()
        
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            #QUIT
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
            
            #Key Pressed
            if event.type == pygame.KEYDOWN:
                
                #Left arrow 
                if event.key == pygame.K_LEFT:
                    number = number - 1
                    if number == 30:
                        width = width + 2
                    elif number == 32:
                        width = width + 2 
                    elif number == 36:
                        width = width + 2
                    list.pop()
                    build_initial_list(list,x,y,width,red)
                
                #right arrow
                if event.key == pygame.K_RIGHT:  
                    if number == 30:
                        width = width - 2
                    elif number == 32:
                        width = width - 2
                    elif number == 36:
                        width = width - 2

                    if number < 50:    
                        number = number + 1
                        element = random.randint(0,100)
                        list.append(element)
                        build_initial_list(list,x,y,width,red)                        
            
            #mouse button clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bubble_button.isOver(pos):
                    print('bubble')
                    bubble_sort(list, x, y, width, speed)

                if insertion_button.isOver(pos):
                    print('insertion')
                    insertion_sort(list, x, y, width, speed)

                if selection_button.isOver(pos):
                    print('selection')
                    selection_sort(list, x, y, width, speed)

                if merge_button.isOver(pos):
                    print('merge')
                    merge_sort(list, x, y, width, speed)

                if heap_button.isOver(pos):
                    print('heap')
                    heap_sort(list, x, y, width, speed)

                if quick_button.isOver(pos):
                    print('quick')
                    quick_sort(list, x, y, width, speed)

                if generate_button.isOver(pos):
                    print('Draw')
                    list = random.sample(range(0,100),number)
                    build_initial_list(list,x,y,width,red)

                if slow_button.isOver(pos):
                    print('Slow')
                    if speed >= 10 and speed < 200:
                        speed = speed + 10
                    print(speed)

                if fast_button.isOver(pos):
                    print('Fast')
                    if speed >= 10 and speed < 200:
                        speed = speed - 10
                    print(speed)
                    
                else:
                    print('none')
                
            #mouse button hover
            if event.type == pygame.MOUSEMOTION:
                if bubble_button.isOver(pos):
                    bubble_button.color = hover_color
                    bubble_button.text_color = black
                elif insertion_button.isOver(pos):
                    insertion_button.color = hover_color
                    insertion_button.text_color = black
                elif selection_button.isOver(pos):
                    selection_button.color = hover_color
                    selection_button.text_color = black
                elif merge_button.isOver(pos):
                    merge_button.color = hover_color
                    merge_button.text_color = black
                elif heap_button.isOver(pos):
                    heap_button.color = hover_color 
                    heap_button.text_color = black                                      
                elif quick_button.isOver(pos):
                    quick_button.color = hover_color
                    quick_button.text_color = black            
                elif generate_button.isOver(pos):
                    generate_button.color = hover_generate_color
                    generate_button.text_color = black
                elif slow_button.isOver(pos):
                    slow_button.color = slow_color
                    slow_button.text_color = black
                elif fast_button.isOver(pos):
                    fast_button.color = fast_color
                    fast_button.text_color = black

                else:
                    bubble_button.color = button_color
                    insertion_button.color = button_color
                    generate_button.color = button_color
                    selection_button.color = button_color
                    merge_button.color = button_color
                    heap_button.color = button_color
                    quick_button.color = button_color
                    slow_button.color = button_color
                    fast_button.color = button_color

                    bubble_button.text_color = white
                    insertion_button.text_color = white
                    generate_button.text_color = white
                    selection_button.text_color = white
                    merge_button.text_color = white
                    heap_button.text_color = white
                    quick_button.text_color = white
                    slow_button.text_color = white
                    fast_button.text_color = white

    pygame.quit()



#calling the Main function
main()

