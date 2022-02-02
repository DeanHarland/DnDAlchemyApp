import tkinter as tk
from PIL import ImageTk, Image

ingredients = {'Bloodgrass': 15, 'ChromusSlime': 2, 'DriedEphedra': 5, 'EmeticWax': 4, 'FennelSilk': 11,
               'GengkoBrush': 3, 'HyancinthNectar': 14, 'LavenderSprig': 2, 'MandrakeRoot': 12,
               'MilkweedSeeds': 1, 'WildSageroot': 13}
# Window size
HEIGHT=600
WIDGHT=950

# Crafters max potion modifier allowed (3,6,9...)
global crafting_level
crafting_level = 3
global crafting_mod_cur
crafting_mod_cur = 0


def delAmount(entryNo, ingre, xfact):
    # get inputted number and ingriedent
    inp = int(entryNo)
    ingr = ingredients.get(ingre)
    # remove the 2 number togethor
    total = ingr - inp
    if total < 1:
        total = 0
    # update dictionery with new number
    ingredients[ingre] = total
    xfact.set(ingredients.get(ingre))
    updateRecipe()

def addAmount(entryNo, ingre, xfact):

    # get inputted number and ingriedent
    inp = int(entryNo)
    ingr = ingredients.get(ingre)
    # add the 2 number togethor
    total = inp + ingr
    # update dictionery with new number
    ingredients[ingre] = total
    # update string var with new val
    xfact.set(ingredients.get(ingre))
    updateRecipe()

# Clears the entry of text
def clearText(entry):
    entry.delete(0,'end')

def deslectText(entry):
    entry.select_clear()

def setCharWisdom(entry):
    wisdomMod = int(entry)
    buttonChar.config(bg='green')
    entryChar.config(bg='green')
    label6.config(bg='green')
    label7.config(bg='green')
    if int(entry) >= 10:
        plusminus.set("+")
    if int(entry) < 10:
        plusminus.set("-")
# Positive
    if int(entry) >= 10 < 12:
        wisdomAddifier.set(0)
    if int(entry) >= 12 < 14:
        wisdomAddifier.set(1)
    if int(entry) >= 14 < 16:
        wisdomAddifier.set(2)
    if int(entry) >= 16 < 18:
        wisdomAddifier.set(3)
    if int(entry) >= 18 < 20:
        wisdomAddifier.set(4)
    if int(entry) >= 20:
        wisdomAddifier.set(5)
# Negative
    if int(entry) < 10:
        wisdomAddifier.set(1)
    if int(entry) < 8:
        wisdomAddifier.set(2)
    if int(entry) < 6:
        wisdomAddifier.set(3)
    if int(entry) < 4:
        wisdomAddifier.set(4)
    if int(entry) < 2:
        wisdomAddifier.set(5)

def makerTotal( i1needed, i2needed, *args):
    i1 = args[0]
    i2 = args[1]
    total = 0
    for i in range(i1):
        if i1 >= i1needed and i2 >= i2needed:
            i1 = i1 - i1needed
            i2 = i2 - i2needed
            total+=1
    return total

def updateRecipe():
    if ingredients.get('WildSageroot') >= 1:
        label41.config(fg="#000000")
        label42.config(fg="#000000")
        potion1infobase.set(potion1info.get() + plusminus.get() +str(wisdomAddifier.get()))
        potion1.set(ingredients.get('WildSageroot'))
    elif ingredients.get('WildSageroot') <=0:
        label41.config(fg="#000000")
        label42.config(fg="#000000")
        potion1.set(0)

    if ingredients.get('MandrakeRoot') >= 1:
        labelManPot.config(fg="#000000")
        labelManPot2.config(fg="#000000")
        labelManPot3.config(fg="#000000")
        potionMandrake.set(ingredients.get("MandrakeRoot"))
    elif ingredients.get('MandrakeRoot') <= 0:
        labelManPot.config(fg="#b3b3b3")
        labelManPot2.config(fg="#b3b3b3")
        labelManPot3.config(fg="#b3b3b3")
        potionMandrake.set(0)

    # Hyancinth
    if ingredients.get('HyancinthNectar') >= 1:
        labelHyanPot.config(fg="#000000")
        labelHyanPot2.config(fg="#000000")
        labelHyanPot3.config(fg="#000000")
        potionHyancinth.set(ingredients.get("HyancinthNectar"))
    elif ingredients.get('HyancinthNectar') <= 0:
        labelHyanPot.config(fg="#b3b3b3")
        labelHyanPot2.config(fg="#b3b3b3")
        labelHyanPot3.config(fg="#b3b3b3")
        potionHyancinth.set(0)

        # FennelSilk
    if ingredients.get('FennelSilk') >= 1:
        labelFennPot.config(fg="#000000")
        labelFennPot2.config(fg="#000000")
        labelFennPot3.config(fg="#000000")
        potionFennel.set(ingredients.get("FennelSilk"))
    elif ingredients.get('FennelSilk') <= 0:
        labelFennPot.config(fg="#b3b3b3")
        labelFennPot2.config(fg="#b3b3b3")
        labelFennPot3.config(fg="#b3b3b3")
        potionFennel.set(0)

        # Bloodgrass
    if ingredients.get('Bloodgrass') >= 1:
        labelBloodPot.config(fg="#000000")
        labelBloodPot2.config(fg="#000000")
        labelBloodPot3.config(fg="#000000")
        potionBloodgrass.set(ingredients.get("Bloodgrass"))
    elif ingredients.get('Bloodgrass') <= 0:
        labelBloodPot.config(fg="#b3b3b3")
        labelBloodPot2.config(fg="#b3b3b3")
        labelBloodPot3.config(fg="#b3b3b3")
        potionBloodgrass.set(0)

    if ingredients.get('DriedEphedra') >=1:
        label105.config(fg="#000000")
        label106.config(fg="#000000")
        mat1.set(ingredients.get('DriedEphedra'))
    elif ingredients.get('DriedEphedra') <=0:
        label105.config(fg="#b3b3b3")
        label106.config(fg="#b3b3b3")
        mat1.set(0)

    if ingredients.get('LavenderSprig') >=1:
        label108.config(fg="#000000")
        label109.config(fg="#000000")
        mat2.set(ingredients.get('LavenderSprig'))
    elif ingredients.get('LavenderSprig') <=0:
        label108.config(fg="#b3b3b3")
        label109.config(fg="#b3b3b3")
        mat2.set(0)



    if ingredients.get('GengkoBrush') >=1:
        labelGengko1.config(fg='#000000')
        labelGengko2.config(fg='#000000')
        mat4Geng.set(ingredients.get('GengkoBrush'))
    elif ingredients.get('GengkoBrush') <=0:
        labelGengko1.config(fg='#b3b3b3')
        labelGengko2.config(fg='#b3b3b3')
        mat4Geng.set(0)



    if ingredients.get('EmeticWax') >=1:
        labelEmetic1.config(fg='#000000')
        labelEmetic2.config(fg='#000000')
        mat6Emetic.set(ingredients.get('EmeticWax'))
    elif ingredients.get('EmeticWax') <=0:
        labelEmetic1.config(fg='#b3b3b3')
        labelEmetic2.config(fg='#b3b3b3')
        mat6Emetic.set(0)



    if ingredients.get('ChromusSlime') >= 1:
        labelChromus1.config(fg='#000000')
        labelChromus2.config(fg='#000000')
        mat8Chromus.set(ingredients.get('ChromusSlime'))
    elif ingredients.get('ChromusSlime') <= 0:
        labelChromus1.config(fg='#b3b3b3')
        labelChromus2.config(fg='#b3b3b3')
        mat8Chromus.set(0)

    if ingredients.get('MilkweedSeeds') >= 1:
        labelMilkweed1.config(fg='#000000')
        labelMilkweed2.config(fg='#000000')
        mat9Milkweed.set(ingredients.get('MilkweedSeeds'))
    elif ingredients.get('MilkweedSeeds') <= 0:
        labelMilkweed1.config(fg='#b3b3b3')
        labelMilkweed2.config(fg='#b3b3b3')
        mat9Milkweed.set(0)

#




    # Misc cleaup
    # if none set back to grey
    if ingredients.get('WildSageroot') < 1:
        label41.config(fg="#b3b3b3")
        label42.config(fg="#b3b3b3")
    #if less than 1 make sure its 0
    if ingredients.get('WildSageroot') < 1:
        potion1.set(0)



def CopyCraft(information, DRoll, DAmount, ddc, PTC):
    #craftinbase

    global potionTypeCrafting
    potionTypeCrafting = PTC
    craftingBase.set(information)
    #craftingFinal.set(information)
    diceRolled.set(DRoll)
    diceAmount.set(DAmount)
    finalDC.set(ddc)
    craftingDC.set(ddc)
    UpdateFinalCraft()
    resetManualCrafting()



def UpdateFinalCraft():
    if potionTypeCrafting == "wildSage_Bool":
        craftingFinal.set("Heals for:  " + diceRolled.get() + "d" + diceAmount.get())
        craftingDC.set(finalDC.get())
    elif potionTypeCrafting == "hyancinth_Bool":
        craftingFinal.set("Removes: " + diceRolled.get() + "d" + diceAmount.get() +" rounds of poison in the target’s system")
        craftingDC.set(finalDC.get())
    else:
        craftingFinal.set(craftingBase.get())
        craftingDC.set(finalDC.get())

# Changes the label color to active green #f2ffe6
def ActiveColorChange(*args):
    for args in args:
        args.config(bg="#ccff99")
# Changes the label color to active white
def ReturnColorChange(*args):
    for args in args:
        args.config(bg="white")

# Adding and removing manual crafting items
def AddDriedEphera():
    global crafting_mod_cur
    if carryCheck(int(mat1.get()), int(usedDriedE.get()), label105):
        if craftingLevelCheck() == False:
            if int(diceAmount.get()) == 4:
                diceAmount.set(6)
                finalDC.set(int(finalDC.get())+2)
                UpdateFinalCraft()
                ActiveColorChange(label105, label106, label107, usedDriedELabel)
                crafting_mod_cur +=1
                updateAddUsed(usedDriedE)


            elif int(diceAmount.get()) == 6:
                diceAmount.set(8)
                finalDC.set(int(finalDC.get()) + 2)
                ActiveColorChange(label105,label106,label107, usedDriedELabel)

                crafting_mod_cur += 1
                updateAddUsed(usedDriedE)
                UpdateFinalCraft()

            elif int(diceAmount.get()) == 8:
                diceAmount.set(10)
                finalDC.set(int(finalDC.get()) + 2)
                ActiveColorChange(label105, label106, label107, usedDriedELabel)
                crafting_mod_cur += 1
                updateAddUsed(usedDriedE)
                UpdateFinalCraft()

            elif int(diceAmount.get()) == 10:
                diceAmount.set(12)
                finalDC.set(int(finalDC.get()) + 2)
                ActiveColorChange(label105, label106, label107, usedDriedELabel)
                crafting_mod_cur += 1
                updateAddUsed(usedDriedE)
                UpdateFinalCraft()

            elif int(diceAmount.get()) == 12:
                diceAmount.set(20)
                finalDC.set(int(finalDC.get()) + 2)
                usedDriedELabel.config(bg="#ffccb3")
                label106.config(bg='#fff2e6')
                label107.config(bg='#fff2e6')
                crafting_mod_cur += 1
                updateAddUsed(usedDriedE)
                UpdateFinalCraft()
        else:
            print("cannot comply as hit crafting limit")


def MinusDriedEphera():
    global crafting_mod_cur
    if int(diceAmount.get()) == 6:
        diceAmount.set(4)
        finalDC.set(int(finalDC.get())-2)
        crafting_mod_cur -= 1
        UpdateFinalCraft()
        updateMinusUsed(usedDriedE)
        label105.config(bg="white")
        label106.config(bg="white")
        label107.config(bg="white")
        usedDriedELabel.config(bg="white")
    elif int(diceAmount.get()) == 8:
        diceAmount.set(6)
        finalDC.set(int(finalDC.get()) - 2)
        crafting_mod_cur -= 1
        UpdateFinalCraft()
        updateMinusUsed(usedDriedE)
    elif int(diceAmount.get()) == 10:
        diceAmount.set(8)
        finalDC.set(int(finalDC.get()) - 2)
        crafting_mod_cur -= 1
        UpdateFinalCraft()
        updateMinusUsed(usedDriedE)

    elif int(diceAmount.get()) == 12:
        diceAmount.set(10)
        finalDC.set(int(finalDC.get()) - 2)
        crafting_mod_cur -= 1
        UpdateFinalCraft()
        updateMinusUsed(usedDriedE)

    elif int(diceAmount.get()) == 20:
        diceAmount.set(12)
        finalDC.set(int(finalDC.get()) - 2)
        crafting_mod_cur -= 1
        UpdateFinalCraft()
        updateMinusUsed(usedDriedE)
        label105.config(bg="#f2ffe6")
        label106.config(bg="#f2ffe6")
        label107.config(bg="#f2ffe6")
        usedDriedELabel.config(bg="#f2ffe6")


def AddLavendersprig():
    global crafting_mod_cur
    if carryCheck(int(mat2.get()), int(usedLavender.get()), label108):
        if craftingLevelCheck() == False:
            if int(usedLavender.get()) ==0:
                finalDC.set(int(finalDC.get()) - 2)
                ActiveColorChange(label108, label109, label110, usedLavenderLabel)
                updateAddUsed(usedLavender)
                UpdateFinalCraft()
                crafting_mod_cur += 1

            elif int(usedLavender.get()) >=1:
                finalDC.set(int(finalDC.get()) - 2)
                updateAddUsed(usedLavender)
                UpdateFinalCraft()
                crafting_mod_cur += 1

def MinusLavendersprig():
    global crafting_mod_cur
    if int(usedLavender.get()) == 0:
        ReturnColorChange(label108, label109, label110, usedLavenderLabel)


    elif int(usedLavender.get()) ==1:
        finalDC.set(int(finalDC.get()) + 2)
        crafting_mod_cur -= 1
        UpdateFinalCraft()
        updateMinusUsed(usedLavender)
        ReturnColorChange(label108, label109, label110, usedLavenderLabel)

    elif int(usedLavender.get()) >1:
        finalDC.set(int(finalDC.get()) + 2)
        updateMinusUsed(usedLavender)
        crafting_mod_cur -= 1
        UpdateFinalCraft()
        label108.config(bg="#f2ffe6")


def AddGengko():
    global crafting_mod_cur
    if carryCheck(int(mat4Geng.get()), int(usedGengko.get()), labelGengko1):
        if craftingLevelCheck() == False:
            if int(usedGengko.get()) == 0:
                ActiveColorChange(labelGengko1, labelGengko2, labelGengko3, usedGengkoLabel)
                finalDC.set(int(finalDC.get()) +2)
                diceRolled.set(int(diceRolled.get())*2)
                updateAddUsed(usedGengko)
                UpdateFinalCraft()
                crafting_mod_cur += 1
            elif int(usedGengko.get()) >= 1:
                finalDC.set(int(finalDC.get()) + 2)
                diceRolled.set(int(diceRolled.get()) * 2)
                updateAddUsed(usedGengko)
                UpdateFinalCraft()
                crafting_mod_cur += 1



def MinusGengko():
    global crafting_mod_cur
    if int(usedGengko.get()) == 0:
        ReturnColorChange(labelGengko1, labelGengko2, labelGengko3, usedGengkoLabel)
    elif int(usedGengko.get()) ==1:
        ReturnColorChange(labelGengko1, labelGengko2, labelGengko3, usedGengkoLabel)
        finalDC.set(int(finalDC.get()) - 2)
        diceRolled.set(int(int(diceRolled.get()) / 2))
        updateMinusUsed(usedGengko)
        crafting_mod_cur -= 1
        UpdateFinalCraft()

    elif int(int(usedGengko.get())) >1:
        finalDC.set(int(finalDC.get()) - 2)
        diceRolled.set(int(int(diceRolled.get()) / 2))
        updateMinusUsed(usedGengko)
        crafting_mod_cur -= 1
        UpdateFinalCraft()
        labelGengko1.config(bg="#f2ffe6")

def AddEmetic():
    global crafting_mod_cur
    if carryCheck(int(mat6Emetic.get()), int(usedEmetic.get()), labelEmetic1):
        if craftingLevelCheck() == False:
            if int(usedEmetic.get()) == 0:
                ActiveColorChange(labelEmetic1,labelEmetic2,labelEmetic3,usedEmeticLabel)
                finalDC.set(int(finalDC.get()) +1)
                updateAddUsed(usedEmetic)
                UpdateFinalCraft()
                crafting_mod_cur += 1
            elif int(usedEmetic.get()) >= 1:
                finalDC.set(int(finalDC.get()) + 1)
                updateAddUsed(usedEmetic)
                UpdateFinalCraft()
                crafting_mod_cur += 1

def MinusEmetic():
    global crafting_mod_cur
    if int(usedEmetic.get()) == 0:
        ReturnColorChange(labelEmetic1, labelEmetic2, labelEmetic3, usedEmeticLabel)
    elif int(usedEmetic.get()) ==1:
        ReturnColorChange(labelEmetic1, labelEmetic2, labelEmetic3, usedEmeticLabel)
        finalDC.set(int(finalDC.get()) - 1)
        updateMinusUsed(usedEmetic)
        crafting_mod_cur -= 1
        UpdateFinalCraft()

    elif int(int(usedEmetic.get())) >1:
        finalDC.set(int(finalDC.get()) - 1)
        updateMinusUsed(usedEmetic)
        crafting_mod_cur -= 1
        UpdateFinalCraft()
        labelEmetic1.config(bg="#f2ffe6")

def AddChromus():
    global crafting_mod_cur
    if carryCheck(int(mat8Chromus.get()), int(usedChromus.get()), labelChromus1):
        if craftingLevelCheck() == False:
            if int(usedChromus.get()) == 0:
                finalDC.set(int(finalDC.get()) + 4)
                ActiveColorChange(labelChromus1,labelChromus3,labelChromus2,usedChromusLabel)
                updateAddUsed(usedChromus)
                UpdateFinalCraft()
                crafting_mod_cur += 1
            elif int(usedChromus.get()) >= 1:
                UpdateFinalCraft()
                usedChromusLabel.config(bg="#ffccb3")
    else:
        print("Else")


def MinusChromus():
    global crafting_mod_cur
    if int(usedChromus.get()) == 0:
        ReturnColorChange(labelChromus1, labelChromus3, labelChromus2, usedChromusLabel)
    elif int(usedChromus.get()) ==1:
        finalDC.set(int(finalDC.get()) - 4)
        ReturnColorChange(labelChromus1, labelChromus3, labelChromus2, usedChromusLabel)
        updateMinusUsed(usedChromus)
        crafting_mod_cur -= 1
        UpdateFinalCraft()

    elif int(int(usedChromus.get())) >1:
        finalDC.set(int(finalDC.get()) - 4)
        updateMinusUsed(usedChromus)
        crafting_mod_cur -= 1
        UpdateFinalCraft()

def AddMilkweed():
    global crafting_mod_cur
    if carryCheck(int(mat9Milkweed.get()), int(usedMilkweed.get()), labelMilkweed1):
        if craftingLevelCheck() == False:
            if int(usedMilkweed.get()) == 0:
                finalDC.set(int(finalDC.get()) + 2)
                ActiveColorChange(labelMilkweed1,labelMilkweed3, labelMilkweed2,usedMilkweedLabel)
                diceRolled.set(int(diceRolled.get()) * 2)
                updateAddUsed(usedMilkweed)
                UpdateFinalCraft()
                crafting_mod_cur += 1
            elif int(usedMilkweed.get()) >= 1:
                finalDC.set(int(finalDC.get()) + 2)
                ActiveColorChange(labelMilkweed1,labelMilkweed3, labelMilkweed2, usedMilkweedLabel)
                diceRolled.set(int(diceRolled.get()) * 2)
                updateAddUsed(usedMilkweed)
                UpdateFinalCraft()
                crafting_mod_cur += 1

    else:
        print("Else")
def MinusMilkweed():
    global crafting_mod_cur
    if int(usedMilkweed.get()) == 0:
        ReturnColorChange(labelMilkweed1,labelMilkweed2,labelMilkweed3,usedMilkweedLabel)

    elif int(usedMilkweed.get()) ==1:
        ReturnColorChange(labelMilkweed1, labelMilkweed2, labelMilkweed3, usedMilkweedLabel)
        finalDC.set(int(finalDC.get()) - 2)
        diceRolled.set(int(int(diceRolled.get()) / 2))
        updateMinusUsed(usedMilkweed)
        crafting_mod_cur -= 1
        UpdateFinalCraft()

    elif int(int(usedMilkweed.get())) >1:
        finalDC.set(int(finalDC.get()) - 2)
        diceRolled.set(int(int(diceRolled.get()) / 2))
        updateMinusUsed(usedMilkweed)
        crafting_mod_cur -= 1
        UpdateFinalCraft()
        labelMilkweed1.config(bg="#f2ffe6")




# Updates manual craftings used totals. ----------------------
def updateAddUsed(ingrident):
    ingrident.set(int(ingrident.get()) + 1)

def updateMinusUsed(ingrident):
    ingrident.set(int(ingrident.get()) - 1)
    if int(ingrident.get()) <=0:
        ingrident.set(0)

def highlightCrafted(selectedAmount,selectedInfo, selectedDC):
    highlightcleanup()
    selectedAmount.config(bg="#ccff99")
    selectedInfo.config(bg="#ccff99")
    selectedDC.config(bg="#ccff99")

def highlightcleanup():
    ReturnColorChange(label40,label41,label42,label108,label109,label110,label105,label106,label107,usedLavenderLabel,usedDriedELabel,
    labelGengko1,labelGengko2,labelGengko3,usedGengkoLabel,labelChromus1,labelChromus2,labelChromus3,usedChromusLabel,labelManPot,
    labelManPot2,labelManPot3,labelHyanPot,labelHyanPot2,labelHyanPot3,labelFennPot,labelFennPot2,labelFennPot3,labelBloodPot,labelBloodPot2,
    labelBloodPot3,labelMilkweed1,labelMilkweed2,labelMilkweed3,usedMilkweedLabel,labelEmetic1,labelEmetic2,labelEmetic3,usedEmeticLabel)






# Checks to see if the user has enough of the ingredient to craft, return true if yes, False if not
def carryCheck(ingredientstock, used, label):
    if ingredientstock > used:
        label.config(bg='#f2ffe6')
        return True
    elif ingredientstock == used:
        label.config(bg='#fff2e6')
        return False

# Resets the crafting/ingredients back to 0; clears the crafting variables
def resetManualCrafting():
    usedLavender.set(0)
    usedDriedE.set(0)
    usedGengko.set(0)
    usedGengko.set(0)
    usedEmetic.set(0)
    usedChromus.set(0)
    usedMilkweed.set(0)
    updateMinusUsed(usedLavender)
    updateMinusUsed(usedDriedE)
    updateMinusUsed(usedGengko)
    updateMinusUsed(usedGengko)
    updateMinusUsed(usedEmetic)
    updateMinusUsed(usedChromus)
    updateMinusUsed(usedMilkweed)
    global crafting_mod_cur
    crafting_mod_cur =0

# Will set and change max amount of crafting dependent on button press, also changes color and indentation to help read
def CraftingLevelButton(button,label,max, level, *args):
    global crafting_level
    button.config(relief="sunken", bg="#ccff99")
    crafting_level = level
    label.config(text=max)
    for args in args:
        args.config(relief="raised", bg="white")


# Undo button, have temp saved variables that you can paste back

# Crafting level max check
def craftingLevelCheck():
    if crafting_mod_cur < crafting_level:
        print("c_mod < "+ str(crafting_mod_cur) + " c_level " + str(crafting_level))
        return False
    else:
        print("c_mod >= "+ str(crafting_mod_cur) + " c_level " + str(crafting_level) )
        return True
    # ^ change color of max crafting variable label to show that they cannot craft more



root = tk.Tk()
root.title("Alchemy App")
# could potentially do bloodgrassx, chromusslimex....,driedepherdax = tk.stringvar()

# StringVars for ingredients(allows for amount to be updated on button press
Bloodgrassx = tk.StringVar()
Bloodgrassx.set(ingredients.get('Bloodgrass'))
ChromusSlimex = tk.StringVar()
ChromusSlimex.set(ingredients.get('ChromusSlime'))
DriedEphedrax = tk.StringVar()
DriedEphedrax.set(ingredients.get('DriedEphedra'))
EmeticWaxx = tk.StringVar()
EmeticWaxx.set(ingredients.get('EmeticWax'))
FennelSilkx = tk.StringVar()
FennelSilkx.set(ingredients.get('FennelSilk'))
GengkoBrushx = tk.StringVar()
GengkoBrushx.set(ingredients.get('GengkoBrush'))
HyancinthNectarx = tk.StringVar()
HyancinthNectarx.set(ingredients.get('HyancinthNectar'))
LavenderSprigx = tk.StringVar()
LavenderSprigx.set(ingredients.get('LavenderSprig'))
MandrakeRootx = tk.StringVar()
MandrakeRootx.set(ingredients.get('MandrakeRoot'))
MilkweedSeedsx = tk.StringVar()
MilkweedSeedsx.set(ingredients.get('MilkweedSeeds'))
WildSagerootx = tk.StringVar()
WildSagerootx.set(ingredients.get('WildSageroot'))

# Canvas root and left most frame
canvas = tk.Canvas(root, height=HEIGHT, width=WIDGHT)
canvas.pack()
frame = tk.Frame(root, bg='#79d2a6')
frame.place( relwidth= 0.4, relheight=1)

# Title Labels
label1 = tk.Label(frame, text="Ingredient", bg="yellow")
label1.grid(row=0, column=0)
label2 = tk.Label(frame, text="Amount", bg="brown")
label2.grid(row=0, column=1)
label3 = tk.Label(frame, text="Input", bg="green", width=7)
label3.grid(row=0, column=2)

# Update button
button64 = tk.Button(frame, text= "Update Recipes", bg='grey',command=lambda :updateRecipe())
button64.grid(row=17, column=6)

# Character statistics part
# Wisdom modifier
wisdomMod = tk.StringVar()
wisdomMod.set(10)
wisdomAddifier = tk.StringVar()
wisdomAddifier.set(0)
plusminus = tk.StringVar()
plusminus.set("+")
label4 = tk.Label(frame, text="Character")
label4.grid(row= 14, column=0)
label5 = tk.Label(frame, text="Wisdom Mod: ", width=15)
label5.grid(row= 15, column=0)
entryChar = tk.Entry(frame , width=5)
entryChar.grid(row=15, column=1)
buttonChar = tk.Button(frame, text="Set",command=lambda:setCharWisdom(entryChar.get()))
buttonChar.grid(row=15, column=2)
label6 = tk.Label(frame, textvariable=plusminus, width=2)
label6.grid(row=15, column=3)
label7 = tk.Label(frame, textvariable=wisdomAddifier, width=5)
label7.grid(row=15, column=4)

# Max modifiers allowed
label_craft_lvl = tk.Label(frame, text="Crafter Lvl(Mods):", width=15)
label_craft_lvl.grid(row=16, column=0)
label_craft_mod = tk.Label(frame,text="Max 3")
label_craft_mod.grid(row=16, column=4)
button_craft_lvl1 = tk.Button(frame, text="lvl1", command = lambda:CraftingLevelButton(button_craft_lvl1,label_craft_mod,"Max 3" ,3, button_craft_lvl2, button_craft_lvl3))
button_craft_lvl1.grid(row=16, column=1)
button_craft_lvl2 = tk.Button(frame, text="lvl2", command = lambda:CraftingLevelButton(button_craft_lvl2,label_craft_mod,"Max 6" ,6, button_craft_lvl1, button_craft_lvl3))
button_craft_lvl2.grid(row=16, column=2)
button_craft_lvl3 = tk.Button(frame, text="lvl3", command = lambda:CraftingLevelButton(button_craft_lvl3,label_craft_mod,"Max 9" ,9, button_craft_lvl1, button_craft_lvl2))
button_craft_lvl3.grid(row=16, column=3)

# List of labels for ingredients
label10 = tk.Label(frame, text="Bloodgrass", bg="yellow", width=15)
label10.grid(row=1, column=0)
label11 = tk.Label(frame, text="Chromus Slime", bg="yellow", width=15)
label11.grid(row=2, column=0)
label12 = tk.Label(frame, text="Dried Ephedra", bg="yellow", width=15)
label12.grid(row=3, column=0)
label13 = tk.Label(frame, text="Emetic Wax", bg="yellow", width=15)
label13.grid(row=4, column=0)
label14 = tk.Label(frame, text="Fennel Silk", bg="yellow", width=15)
label14.grid(row=5, column=0)
label15 = tk.Label(frame, text="Gengko Brush", bg="yellow", width=15)
label15.grid(row=6, column=0)
label16 = tk.Label(frame, text="Hyancinth Nectar", bg="yellow", width=15)
label16.grid(row=7, column=0)
label17 = tk.Label(frame, text="Lavender Sprig", bg="yellow", width=15)
label17.grid(row=8, column=0)
label18 = tk.Label(frame, text="Mandrake Root", bg="yellow", width=15)
label18.grid(row=9, column=0)
label19 = tk.Label(frame, text="Milkweed Seeds", bg="yellow", width=15)
label19.grid(row=10, column=0)
label20 = tk.Label(frame, text="Wild Sageroot", bg="yellow", width=15)
label20.grid(row=11, column=0)


# List of amounts of ingredients
label20 = tk.Label(frame, textvariable=Bloodgrassx, bg="brown", width=5)
label20.grid(row=1, column=1)
label21 = tk.Label(frame,textvariable=ChromusSlimex, bg="brown", width=5)
label21.grid(row=2, column=1)
label22 = tk.Label(frame, textvariable=DriedEphedrax, bg="brown", width=5)
label22.grid(row=3, column=1)
label23 = tk.Label(frame, textvariable=EmeticWaxx, bg="brown", width=5)
label23.grid(row=4, column=1)
label24 = tk.Label(frame, textvariable=FennelSilkx, bg="brown", width=5)
label24.grid(row=5, column=1)
label25 = tk.Label(frame, textvariable=GengkoBrushx, bg="brown", width=5)
label25.grid(row=6, column=1)
label26 = tk.Label(frame, textvariable=HyancinthNectarx, bg="brown", width=5)
label26.grid(row=7, column=1)
label27 = tk.Label(frame, textvariable=LavenderSprigx, bg="brown", width=5)
label27.grid(row=8, column=1)
label28 = tk.Label(frame, textvariable=MandrakeRootx, bg="brown", width=5)
label28.grid(row=9, column=1)
label29 = tk.Label(frame, textvariable=MilkweedSeedsx, bg="brown", width=5)
label29.grid(row=10, column=1)
label30 = tk.Label(frame, textvariable=WildSagerootx, bg="brown", width=5)
label30.grid(row=11, column=1)


# List of entry's
entry0 = tk.Entry(frame, width=5)
entry0.grid(row=1, column=2)
entry1 = tk.Entry(frame, width=5)
entry1.grid(row=2, column=2)
entry2 = tk.Entry(frame, width=5)
entry2.grid(row=3, column=2)
entry3 = tk.Entry(frame, width=5)
entry3.grid(row=4, column=2)
entry4 = tk.Entry(frame, width=5)
entry4.grid(row=5, column=2)
entry5 = tk.Entry(frame, width=5)
entry5.grid(row=6, column=2)
entry6 = tk.Entry(frame, width=5)
entry6.grid(row=7, column=2)
entry7 = tk.Entry(frame, width=5)
entry7.grid(row=8, column=2)
entry8 = tk.Entry(frame, width=5)
entry8.grid(row=9, column=2)
entry9 = tk.Entry(frame, width=5)
entry9.grid(row=10, column=2)
entry10 = tk.Entry(frame, width=5)
entry10.grid(row=11, column=2)


# List of buttons
button1 = tk.Button(frame, text= "Add", bg='grey',command=lambda :(addAmount(entry0.get(),'Bloodgrass', Bloodgrassx),clearText(entry0)))
button1.grid(row=1, column=3)
button102 = tk.Button(frame, text= "Del", bg='grey',command=lambda :(delAmount(entry0.get(),'Bloodgrass',Bloodgrassx),clearText(entry0)) )
button102.grid(row=1, column=4)

button2 = tk.Button(frame, text= "Add", bg='grey',command=lambda :(addAmount(entry1.get(),'ChromusSlime', ChromusSlimex),clearText(entry1)))
button2.grid(row=2, column=3)
button202 = tk.Button(frame, text= "Del", bg='grey',command=lambda :(delAmount(entry1.get(),'ChromusSlime',ChromusSlimex) ,clearText(entry1)))
button202.grid(row=2, column=4)

button3 = tk.Button(frame, text= "Add", bg='grey',command=lambda :(addAmount(entry2.get(),'DriedEphedra', DriedEphedrax),clearText(entry2)))
button3.grid(row=3, column=3)
button302 = tk.Button(frame, text= "Del", bg='grey',command=lambda :(delAmount(entry2.get(),'DriedEphedra',DriedEphedrax),clearText(entry2)) )
button302.grid(row=3, column=4)

button4 = tk.Button(frame, text= "Add", bg='grey',command=lambda :(addAmount(entry3.get(),'EmeticWax', EmeticWaxx),clearText(entry3)))
button4.grid(row=4, column=3)
button402 = tk.Button(frame, text= "Del", bg='grey',command=lambda :(delAmount(entry3.get(),'EmeticWax',EmeticWaxx) ,clearText(entry3)))
button402.grid(row=4, column=4)

button5 = tk.Button(frame, text= "Add", bg='grey',command=lambda :(addAmount(entry4.get(),'FennelSilk', FennelSilkx),clearText(entry4)))
button5.grid(row=5, column=3)
button505 = tk.Button(frame, text= "Del", bg='grey',command=lambda :(delAmount(entry4.get(),'FennelSilk',FennelSilkx) ,clearText(entry4)))
button505.grid(row=5, column=4)

button6 = tk.Button(frame, text= "Add", bg='grey',command=lambda :(addAmount(entry5.get(),'GengkoBrush', GengkoBrushx),clearText(entry5)))
button6.grid(row=6, column=3)
button602 = tk.Button(frame, text= "Del", bg='grey',command=lambda :(delAmount(entry5.get(),'GengkoBrush',GengkoBrushx),clearText(entry5)) )
button602.grid(row=6, column=4)

button7 = tk.Button(frame, text= "Add", bg='grey',command=lambda :(addAmount(entry6.get(),'HyancinthNectar', HyancinthNectarx),clearText(entry6)))
button7.grid(row=7, column=3)
button702 = tk.Button(frame, text= "Del", bg='grey',command=lambda :(delAmount(entry6.get(),'HyancinthNectar',HyancinthNectarx),clearText(entry6)))
button702.grid(row=7, column=4)

button8 = tk.Button(frame, text= "Add", bg='grey',command=lambda :(addAmount(entry7.get(),'LavenderSprig', LavenderSprigx),clearText(entry7)))
button8.grid(row=8, column=3)
button802 = tk.Button(frame, text= "Del", bg='grey',command=lambda :(delAmount(entry7.get(),'LavenderSprig',LavenderSprigx),clearText(entry7)) )
button802.grid(row=8, column=4)

button9 = tk.Button(frame, text= "Add", bg='grey',command=lambda :(addAmount(entry8.get(),'MandrakeRoot', MandrakeRootx),clearText(entry8)))
button9.grid(row=9, column=3)
button902 = tk.Button(frame, text= "Del", bg='grey',command=lambda :(delAmount(entry8.get(),'MandrakeRoot',MandrakeRootx) ,clearText(entry8)))
button902.grid(row=9, column=4)

button10 = tk.Button(frame, text= "Add", bg='grey',command=lambda :(addAmount(entry9.get(),'MilkweedSeeds', MilkweedSeedsx),clearText(entry9)))
button10.grid(row=10, column=3)
button1002 = tk.Button(frame, text= "Del", bg='grey',command=lambda :(delAmount(entry9.get(),'MilkweedSeeds',MilkweedSeedsx),clearText(entry9)) )
button1002.grid(row=10, column=4)

button11 = tk.Button(frame, text= "Add", bg='grey',command=lambda :(addAmount(entry10.get(),'WildSageroot', WildSagerootx),clearText(entry10)))
button11.grid(row=11, column=3)
button1102 = tk.Button(frame, text= "Del", bg='grey',command=lambda :(delAmount(entry10.get(),'WildSageroot',WildSagerootx),clearText(entry10)) )
button1102.grid(row=11, column=4)


# Frame 2, right side of the window, will be used to calculate potions dependent on what ingreidents are owned ------------------------------------------
frame2 = tk.Frame(root, bg='#40bf80')
frame2.place( relx=0.4, relwidth= 0.6, relheight=1)

# Titles for Frame 2
label90 = tk.Label(frame2, text="Amount")
label90.grid(row=1, column=1)
label91 = tk.Label(frame2, text="Information", bg="grey", width=50)
label91.grid(row=1, column=2)
label92 = tk.Label(frame2, text="DC", width=5)
label92.grid(row=1, column=3)

# Potion 1
potion1 = tk.StringVar()
potion1.set(0)
potion1info = tk.StringVar()
potion1info.set("Heals for 2d4 ")
potion1infobase = tk.StringVar()
potion1infobase.set("Heals for 2d4  ")
label40 = tk.Label(frame2, textvariable=potion1, bg="white", width=5)
label40.grid(row=2, column=1)
label41 = tk.Label(frame2, textvariable=potion1infobase, fg="#b3b3b3",width=50)
label41.grid(row=2, column=2)
label42 = tk.Label(frame2, text="10", fg="#b3b3b3",width=5)
label42.grid(row=2, column=3)
buttoncraft1 = tk.Button(frame2, text= "Craft", bg='grey',height=1, command=lambda :(CopyCraft(potion1info.get(),2, 4, 10, "wildSage_Bool"),highlightCrafted(label40, label41, label42) ))
buttoncraft1.grid(row=2, column=4)

# potion Hyancinth Root
potionHyancinth = tk.StringVar()
potionHyancinth.set(0)
potionHyancinthInfo = tk.StringVar()
potionHyancinthInfo.set("Removes 1d6 rounds of poison in the target’s system.")
potionHyancinthInfoBase = tk.StringVar()
potionHyancinthInfoBase.set("Removes 1d6 rounds of poison in the target’s system.")
labelHyanPot = tk.Label(frame2, textvariable=potionHyancinth, bg="white", width=5)
labelHyanPot.grid(row=3, column=1)
labelHyanPot2 = tk.Label(frame2, textvariable=potionHyancinthInfoBase, fg="#b3b3b3", width=50)
labelHyanPot2.grid(row=3, column=2)
labelHyanPot3 = tk.Label(frame2, text=11, fg="#b3b3b3", width=5)
labelHyanPot3.grid(row=3, column=3)
buttoncraft3 = tk.Button(frame2, text= "Craft", bg='grey',height=1, command=lambda :(CopyCraft(potionHyancinthInfo.get(),1, 6, 11, "hyancinth_Bool"),highlightCrafted(labelHyanPot, labelHyanPot2, labelHyanPot3) ))
buttoncraft3.grid(row=3, column=4)

# potion Mandrake Root
potionMandrake = tk.StringVar()
potionMandrake.set(0)
potionMandrakeInfo = tk.StringVar()
potionMandrakeInfo.set("Reduce any disease or poison’s potency by half for 2d12 hours.")
potionMandrakeInfoBase = tk.StringVar()
potionMandrakeInfoBase.set("Reduce any disease or poison’s potency by half for 2d12 hours.")
labelManPot = tk.Label(frame2, textvariable=potionMandrake, bg="white", width=5)
labelManPot.grid(row=4, column=1)
labelManPot2 = tk.Label(frame2, textvariable=potionMandrakeInfoBase, fg="#b3b3b3", width=50)
labelManPot2.grid(row=4, column=2)
labelManPot3 = tk.Label(frame2, text=10, fg="#b3b3b3", width=5)
labelManPot3.grid(row=4, column=3)
buttoncraft2 = tk.Button(frame2, text= "Craft", bg='grey',height=1, command=lambda :(CopyCraft(potionMandrakeInfo.get(),0, 0, 10, "mandrake_Bool"),highlightCrafted(labelManPot, labelManPot2, labelManPot3) ))
buttoncraft2.grid(row=4, column=4)


# potion Fennel silk

potionFennel = tk.StringVar()
potionFennel.set(0)
potionFennelInfo = tk.StringVar()
potionFennelInfo.set("Resist cold weather or wet condition penalties for 1 hour")
potionFennelInfoBase = tk.StringVar()
potionFennelInfoBase.set("Resist cold weather orwet condition penalties for 1 hour")
labelFennPot = tk.Label(frame2, textvariable=potionFennel, bg="white", width=5)
labelFennPot.grid(row=5, column=1)
labelFennPot2 = tk.Label(frame2, textvariable=potionFennelInfoBase, fg="#b3b3b3", width=50)
labelFennPot2.grid(row=5, column=2)
labelFennPot3 = tk.Label(frame2, text=10, fg="#b3b3b3", width=5)
labelFennPot3.grid(row=5, column=3)
buttoncraft4 = tk.Button(frame2, text= "Craft", bg='grey',height=1, command=lambda :(CopyCraft(potionFennelInfo.get(),0, 0, 12, "fennel_Bool"),highlightCrafted(labelFennPot,labelFennPot2,labelFennPot3) ))
buttoncraft4.grid(row=5, column=4)

# potion Bloodgrass

potionBloodgrass = tk.StringVar()
potionBloodgrass.set(0)
potionBloodgrassInfo = tk.StringVar()
potionBloodgrassInfo.set("Combine with Potion ingredient to become a food source for 1 day")
potionBloodgrassInfoBase = tk.StringVar()
potionBloodgrassInfoBase.set("Combine with Potion ingredient to become a food source for 1 day")
labelBloodPot = tk.Label(frame2, textvariable=potionBloodgrass, bg="white", width=5)
labelBloodPot.grid(row=6, column=1)
labelBloodPot2 = tk.Label(frame2, textvariable=potionBloodgrassInfoBase, fg="#b3b3b3", width=50)
labelBloodPot2.grid(row=6, column=2)
labelBloodPot3 = tk.Label(frame2, text=12, fg="#b3b3b3", width=5)
labelBloodPot3.grid(row=6, column=3)
buttoncraft5 = tk.Button(frame2, text= "Craft", bg='grey',height=1, command=lambda :(CopyCraft(potionBloodgrassInfo.get(),0, 0, 10,"bloodgrass_Bool"),highlightCrafted(labelBloodPot,labelBloodPot2 , labelBloodPot3) ))
buttoncraft5.grid(row=6, column=4)

# Frame 3 - This is the frame for manual crafting ------------------------------------------------------

frame3 = tk.Frame(root, bg='#40af80')
frame3.place(rely=0.3, relx=0.4, relwidth= 0.6, relheight=0.7)

# Titles for Frame 3
label100 = tk.Label(frame3, text="Base Craft: ", width=8, bg="#e6ccff")
label100.grid(row=1, column=1)
craftingBase = tk.StringVar()
craftingBase.set("")
label101 = tk.Label(frame3, textvariable=craftingBase, bg="#d9b3ff", width=50)
label101.grid(row=1, column=2)

label102 = tk.Label(frame3, text="Amount", width=6)
label102.grid(row=2, column=1)
label103 = tk.Label(frame3, text="Information", bg="grey", width=48)
label103.grid(row=2, column=2)
label104 = tk.Label(frame3, text="DC", width=5)
label104.grid(row=2, column=3)

label105 = tk.Label(frame3, text="Used", width=5)
label105.grid(row=2, column=5)

# Start of crafing materials

#Crafting variables
diceRolled = tk.StringVar()
diceRolled.set(0)
diceAmount = tk.StringVar()
diceAmount.set(0)
finalDC = tk.StringVar()
finalDC.set(10)

# Dried Ephera
mat1 = tk.StringVar()
mat1.set(0)
label105 = tk.Label(frame3, textvariable=mat1, fg="#b3b3b3", width=6)
label105.grid(row=3, column=1)
label106 = tk.Label(frame3, text="Increase the dice-type by 1 size", width=48, fg="#b3b3b3")
label106.grid(row=3, column=2)
label107 = tk.Label(frame3, text="+2", width=5)
label107.grid(row=3, column=3)
buttonDriedE = tk.Button(frame3, text= "Use", bg='grey',height=1, command=lambda :AddDriedEphera())
buttonDriedE.grid(row=3, column=4)
usedDriedE = tk.StringVar()
usedDriedE.set(0)
usedDriedELabel = tk.Label(frame3, textvariable=usedDriedE, width=5 )
usedDriedELabel.grid(row=3, column=5)
buttonDriedEMin = tk.Button(frame3, text= "--", bg='grey',height=1, command=lambda :MinusDriedEphera())
buttonDriedEMin.grid(row=3, column=6)

# Milkweed seeds
mat9Milkweed = tk.StringVar()
mat9Milkweed.set(0)
labelMilkweed1 = tk.Label(frame3, textvariable=mat9Milkweed, fg="#b3b3b3", width = 6)
labelMilkweed1.grid(row=4, column=1)
labelMilkweed2 = tk.Label(frame3, text="Double dice rolled, remove Alchemy modifier ", width=48, fg="#b3b3b3")
labelMilkweed2.grid(row=4, column=2)
labelMilkweed3 = tk.Label(frame3, text="+2", width=5)
labelMilkweed3.grid(row=4, column=3)
buttonMilkweedAdd = tk.Button(frame3, text="Use", bg='grey', height=1, command=lambda: AddMilkweed())
buttonMilkweedAdd.grid(row=4, column=4)
usedMilkweed = tk.StringVar()
usedMilkweed.set(0)
usedMilkweedLabel = tk.Label(frame3, textvariable=usedMilkweed, width=5)
usedMilkweedLabel.grid(row=4, column=5)
buttonMilkweedMin = tk.Button(frame3, text="--", bg='grey', height=1, command=lambda: MinusMilkweed())
buttonMilkweedMin.grid(row=4, column=6)


# Lavender Sprig
mat2 = tk.StringVar()
mat2.set(0)
label108 = tk.Label(frame3, textvariable=mat2, fg="#b3b3b3", width=6)
label108.grid(row=5, column=1)
label109 = tk.Label(frame3, text="Potion is more stable and safer to craft", width=48, fg="#b3b3b3")
label109.grid(row=5, column=2)
label110 = tk.Label(frame3, text="-2", width=5)
label110.grid(row=5, column=3)
buttonLavender = tk.Button(frame3, text= "Use", bg='grey',height=1, command=lambda :AddLavendersprig())
buttonLavender.grid(row=5, column=4)
usedLavender = tk.StringVar()
usedLavender.set(0)
usedLavenderLabel = tk.Label(frame3, textvariable=usedLavender, width=5 )
usedLavenderLabel.grid(row=5, column=5)
buttonLavenderMin = tk.Button(frame3, text= "--", bg='grey',height=1, command=lambda :MinusLavendersprig())
buttonLavenderMin.grid(row=5, column=6)

# Gengko Brusg
mat4Geng = tk.StringVar()
mat4Geng.set(0)
labelGengko1 = tk.Label(frame3, textvariable=mat4Geng, fg="#b3b3b3", width = 6)
labelGengko1.grid(row=6, column=1)
labelGengko2 = tk.Label(frame3, text="Double dice rolled, 1/2 over 2 rounds", width=48, fg="#b3b3b3")
labelGengko2.grid(row=6, column=2)
labelGengko3 = tk.Label(frame3, text="+2", width=5)
labelGengko3.grid(row=6, column=3)
buttonGengkoAdd = tk.Button(frame3, text="Use", bg='grey', height=1, command=lambda: AddGengko())
buttonGengkoAdd.grid(row=6, column=4)
usedGengko = tk.StringVar()
usedGengko.set(0)
usedGengkoLabel = tk.Label(frame3, textvariable=usedGengko, width=5)
usedGengkoLabel.grid(row=6, column=5)
buttonGengkoMin = tk.Button(frame3, text="--", bg='grey', height=1, command=lambda: MinusGengko())
buttonGengkoMin.grid(row=6, column=6)

# Emetic Wax
mat6Emetic = tk.StringVar()
mat6Emetic.set(0)
labelEmetic1 = tk.Label(frame3, textvariable=mat6Emetic, fg="#b3b3b3", width = 6)
labelEmetic1.grid(row=8, column=1)
labelEmetic2 = tk.Label(frame3, text="Delay effect by 1d6 ", width=48, fg="#b3b3b3")
labelEmetic2.grid(row=8, column=2)
labelEmetic3 = tk.Label(frame3, text="+1", width=5)
labelEmetic3.grid(row=8, column=3)
buttonEmeticAdd = tk.Button(frame3, text="Use", bg='grey', height=1, command=lambda: AddEmetic())
buttonEmeticAdd.grid(row=8, column=4)
usedEmetic = tk.StringVar()
usedEmetic.set(0)
usedEmeticLabel = tk.Label(frame3, textvariable=usedEmetic, width=5)
usedEmeticLabel.grid(row=8, column=5)
buttonEmeticMin = tk.Button(frame3, text="--", bg='grey', height=1, command=lambda: MinusEmetic())
buttonEmeticMin.grid(row=8, column=6)

# Chromus Slime
mat8Chromus = tk.StringVar()
mat8Chromus.set(0)
labelChromus1 = tk.Label(frame3, textvariable=mat8Chromus, fg="#b3b3b3", width = 6)
labelChromus1.grid(row=10, column=1)
labelChromus2 = tk.Label(frame3, text="oppisite ", width=48, fg="#b3b3b3")
labelChromus2.grid(row=10, column=2)
labelChromus3 = tk.Label(frame3, text="+4", width=5)
labelChromus3.grid(row=10, column=3)
buttonChromusAdd = tk.Button(frame3, text="Use", bg='grey', height=1, command=lambda: AddChromus())
buttonChromusAdd.grid(row=10, column=4)
usedChromus = tk.StringVar()
usedChromus.set(0)
usedChromusLabel = tk.Label(frame3, textvariable=usedChromus, width=5)
usedChromusLabel.grid(row=10, column=5)
buttonChromusMin = tk.Button(frame3, text="--", bg='grey', height=1, command=lambda: MinusChromus())
buttonChromusMin.grid(row=10, column=6)


# End product of crafting
label999 = tk.Label(frame3, text="Final:", width=6, bg="#b3b3ff")
label999.grid(row=99, column=1)
craftingFinal = tk.StringVar()
craftingFinal.set("")
label901 = tk.Label(frame3, textvariable=craftingFinal, bg="#ccccff", width=50)
label901.grid(row=99, column=2)
craftingDC = tk.StringVar()
craftingDC.set(0)
label902 = tk.Label(frame3, textvariable=craftingDC, bg="#b3b3ff", width=5)
label902.grid(row=99, column=3)


root.mainloop()