from config.strings import Strings
from corda import Corda
from espada import Espada


print(Strings.title);
print(Strings.divider);
print(Strings.startGame);

input();
print(Strings.gameStory);
print(Strings.divider);
print("Gatts está vindo em sua direção.\nEscolha um item!")
print(Strings.divider);
print(" ");
print("1. Espada");
print("2. Corda");
print(" ");
menuItem = int(input());
match menuItem:
    case 1: 
        Espada.espadaMenu();
    case 2:
        Corda.cordaMenu();
default: print("GAME OVER!");

input();
