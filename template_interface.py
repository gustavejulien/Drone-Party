from .... import .... # importer le wrapper du drone
from .... import .... # importer le wrapper de l'api son
from .... import .... # importer le wrapper de reconnaissance faciale


class template_interface:

    def __init__(self):
        self.__running = False
        self.__wrapper1 = ....()
        self.__wrapper2 = ....()
        """
        vous pouvez en ajouter au besoin
        """


    def start(self):
        """
        permet de faire des initialisation de votre coté, test de connection ....
        """
        pass

    def destroy(self):
        """
        potentiellement vide, avec de la suppression d'infomation si vous créer des object le nécissitant. 
        """
        pass

    def featuresloop(self):
        """
        la boucle infinie de la features est ici
        """
        while self.__running == True:
            """
            logique de la fonction
            """
            break

    def activate(self):
        """
        activer la features
        """
        self.__running = True

    def desactivate(self):
        """
        desacative la features
        """
        self.__running = False


    def __logic1(self):
        """
        fonction logique en PRIVEE
        """
        pass

    def __logic2(self):
        """
        fonction logique en PRIVEE
        """
        pass