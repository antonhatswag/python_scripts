
class Letter:
    def __init__(self, content, value):
        self.content = content
        self.value = value
        self.direction = None
        self.binary = ""

    def binary_add(self, add):
        self.binary = add + self.binary
    def setDirection(self, direction):
        self.direction = direction

class Bubble:
    def __init__(self, children):
        self.children = children
        value = 0
        for i in children:
            value += i.value
        self.value = value

        #directions in bubbles are possibly useless :)
        self.direction = None

    def binary_add(self, add):
        for x in self.children:
            x.binary_add(add)

    def setDirection(self, direction):
        self.direction = direction




def create_symbol_lists(source):
    charactersDone = []
    letters = []
    b_letters = []


    for i in source:
        # current char hasnt been done
        if charactersDone.count(i) < 1:
            #print(i, "noch nicht gezählt")

            redundance = source.count(i)
            #print(i, redundance)#
            charactersDone.append(i)
            r = Letter(i, redundance)
            b_letters.append(r)
            letters.append(r)
    return (letters, b_letters)



#hört des auf wenn nix verändert?
def bubblesort(list):
    for r in range(len(list)):
        for x in range(len(list) -1):
            if list[x].value > list[x+1].value:
                #swap elements
                list[x], list[x+1] = list[x+1], list[x]
    return (list)



# bei jeder verschmelzung von 2 Elementen erhält addiert jedes Element zu seinem eigenen
# binär code 1/0 oder zu jedem binär code seiner Kinder

# b_letters is only used for building bubble and letter objects
# meanwhile letters may be used to as a dictionary for binary translation later on

#TREE BUILDING

def tree_building(b_letters):
    while len(b_letters) > 1:
        b_letters = bubblesort(b_letters)
        #left = 0 right = 1
        b_letters[0].setDirection("0")
        b_letters[1].setDirection("1")

        b_letters[0].binary_add("0")
        b_letters[1].binary_add("1")
        bubble = Bubble([b_letters[0], b_letters[1]])
        del b_letters[0:2]
        b_letters.append(bubble)

def build_binary_code(source, letters):
    binary_code = ""
    for i in source:
        for r in letters:
            if r.content == i:
                print(r.content, r.binary)
                binary_code += r.binary
    return(binary_code)

def main():
    source = "jette"
    lists = create_symbol_lists(source)
    #b/letters both store the same object references but the lists themselfs are different references,
    #so that one of the may be editted without corrupting the other
    letters = lists[0]
    b_letters = lists[1]

    tree_building(b_letters)

    print(build_binary_code(source, letters))




main()