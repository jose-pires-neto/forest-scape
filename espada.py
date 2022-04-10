from turtle import delay
from config.strings import Strings


class Espada():
    
    def espadaMenu():
        print(Strings.divider);
        print("Você selecionou a Espada!");
        print(Strings.divider);
        print("Gatts está com uma fodendo Espada Bastarda.\nO que você fará com a sua espada?");
        print(Strings.divider);
        delay(100000);
        print("O Gatts é muito rápido, não deu tempo!");
        print("Que pena, você perdeu!");